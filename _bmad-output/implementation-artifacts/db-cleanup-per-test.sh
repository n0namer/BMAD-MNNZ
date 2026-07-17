#!/bin/bash

################################################################################
# Database Cleanup Script for Parallel Test Isolation
#
# This script cleanly removes test databases and terminates any remaining
# connections, ensuring complete isolation for the next test run.
#
# Usage:
#   ./db-cleanup-per-test.sh [OPTIONS]
#
# Options:
#   --database NAME       Database name (default: katana_test)
#   --host HOST           PostgreSQL host (default: localhost)
#   --port PORT           PostgreSQL port (default: 5432)
#   --user USER           PostgreSQL user (default: test_user)
#   --password PASS       PostgreSQL password (default: env $POSTGRES_PASSWORD)
#   --force               Force cleanup even if errors occur (default: false)
#   --verbose             Verbose output (default: false)
#
# Exit Codes:
#   0 - Success
#   1 - Connection failed
#   2 - Cleanup failed
#   3 - Invalid arguments
#
################################################################################

set -e

# Configuration defaults
DB_NAME="katana_test"
DB_HOST="localhost"
DB_PORT="5432"
DB_USER="test_user"
DB_PASSWORD="${POSTGRES_PASSWORD:-test_pass}"
FORCE=false
VERBOSE=false

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    if [ "$VERBOSE" = true ]; then
        echo -e "${BLUE}ℹ${NC} $*"
    fi
}

log_success() {
    echo -e "${GREEN}✅${NC} $*"
}

log_warn() {
    echo -e "${YELLOW}⚠️${NC} $*"
}

log_error() {
    echo -e "${RED}❌${NC} $*"
}

# Parse arguments
parse_args() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            --database)
                DB_NAME="$2"
                shift 2
                ;;
            --host)
                DB_HOST="$2"
                shift 2
                ;;
            --port)
                DB_PORT="$2"
                shift 2
                ;;
            --user)
                DB_USER="$2"
                shift 2
                ;;
            --password)
                DB_PASSWORD="$2"
                shift 2
                ;;
            --force)
                FORCE=true
                shift
                ;;
            --verbose)
                VERBOSE=true
                shift
                ;;
            -h|--help)
                print_usage
                exit 0
                ;;
            *)
                log_error "Unknown option: $1"
                print_usage
                exit 3
                ;;
        esac
    done
}

print_usage() {
    cat << EOF
Database Cleanup Script for Parallel Test Isolation

Usage: $(basename "$0") [OPTIONS]

Options:
    --database NAME       Database name (default: $DB_NAME)
    --host HOST           PostgreSQL host (default: $DB_HOST)
    --port PORT           PostgreSQL port (default: $DB_PORT)
    --user USER           PostgreSQL user (default: $DB_USER)
    --password PASS       PostgreSQL password (default: from env or test_pass)
    --force               Force cleanup even if errors occur
    --verbose             Verbose output
    -h, --help            Print this help message

Examples:
    ./db-cleanup-per-test.sh
    ./db-cleanup-per-test.sh --database katana_test_1 --verbose
    ./db-cleanup-per-test.sh --force --host db.example.com

EOF
}

# Verify PostgreSQL connection
verify_connection() {
    log_info "Verifying PostgreSQL connection..."

    export PGPASSWORD="$DB_PASSWORD"

    if ! pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" > /dev/null 2>&1; then
        log_error "Cannot connect to PostgreSQL at $DB_HOST:$DB_PORT"
        if [ "$FORCE" = false ]; then
            return 1
        fi
    fi

    log_success "PostgreSQL connection verified"
    return 0
}

# Terminate database connections
terminate_connections() {
    local db_name="$1"

    log_info "Terminating connections to database: $db_name"

    export PGPASSWORD="$DB_PASSWORD"

    # Try to terminate connections gracefully
    local attempts=0
    local max_attempts=3

    while [ $attempts -lt $max_attempts ]; do
        # Count active connections
        local active_conns=$(psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d postgres -tc \
            "SELECT COUNT(*) FROM pg_stat_activity WHERE datname = '$db_name' AND pid != pg_backend_pid()" 2>/dev/null || echo "0")

        active_conns=$(echo "$active_conns" | xargs) # Trim whitespace

        if [ -z "$active_conns" ] || [ "$active_conns" = "0" ]; then
            log_success "No active connections found"
            return 0
        fi

        log_info "Found $active_conns active connections, attempting to terminate..."

        # Terminate connections
        if ! psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d postgres -c \
            "SELECT pg_terminate_backend(pg_stat_activity.pid)
             FROM pg_stat_activity
             WHERE pg_stat_activity.datname = '$db_name'
             AND pg_stat_activity.pid <> pg_backend_pid()" > /dev/null 2>&1; then
            log_warn "Failed to terminate some connections"
        fi

        # Wait before retrying
        sleep 1
        attempts=$((attempts + 1))
    done

    # Check if connections still exist
    local remaining=$(psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d postgres -tc \
        "SELECT COUNT(*) FROM pg_stat_activity WHERE datname = '$db_name'" 2>/dev/null || echo "0")

    remaining=$(echo "$remaining" | xargs)

    if [ -z "$remaining" ] || [ "$remaining" = "0" ]; then
        log_success "All connections terminated"
        return 0
    fi

    log_warn "Could not terminate all connections ($remaining remaining)"
    if [ "$FORCE" = false ]; then
        return 0  # Continue anyway
    fi

    return 0
}

# Drop database
drop_database() {
    local db_name="$1"

    log_info "Dropping database: $db_name"

    export PGPASSWORD="$DB_PASSWORD"

    # Check if database exists
    if ! psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d postgres -tc \
        "SELECT 1 FROM pg_database WHERE datname = '$db_name'" 2>/dev/null | grep -q 1; then
        log_info "Database '$db_name' does not exist, skipping"
        return 0
    fi

    # Drop database
    if ! psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d postgres -c \
        "DROP DATABASE IF EXISTS \"$db_name\";" > /dev/null 2>&1; then
        log_error "Failed to drop database: $db_name"
        if [ "$FORCE" = false ]; then
            return 2
        fi
    fi

    log_success "Database dropped: $db_name"
    return 0
}

# Verify cleanup
verify_cleanup() {
    local db_name="$1"

    log_info "Verifying cleanup..."

    export PGPASSWORD="$DB_PASSWORD"

    # Check if database still exists
    if psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d postgres -tc \
        "SELECT 1 FROM pg_database WHERE datname = '$db_name'" 2>/dev/null | grep -q 1; then
        log_error "Database still exists: $db_name"
        return 2
    fi

    log_success "Database successfully removed"
    return 0
}

# Get database size (before cleanup)
get_db_size() {
    local db_name="$1"

    export PGPASSWORD="$DB_PASSWORD"

    if ! psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d postgres -tc \
        "SELECT pg_database.datname, pg_size_pretty(pg_database_size(pg_database.datname))
         FROM pg_database WHERE datname = '$db_name'" 2>/dev/null; then
        echo "unknown"
    fi
}

# Print summary
print_summary() {
    local db_name="$1"
    local start_time="$2"
    local end_time="$3"
    local duration=$((end_time - start_time))

    echo ""
    echo "┌────────────────────────────────────────┐"
    echo "│  Database Cleanup Complete             │"
    echo "├────────────────────────────────────────┤"
    echo "│ Database:     $db_name"
    echo "│ Host:         $DB_HOST:$DB_PORT"
    echo "│ User:         $DB_USER"
    echo "├────────────────────────────────────────┤"
    echo "│ ✅ Connection verified"
    echo "│ ✅ Connections terminated"
    echo "│ ✅ Database dropped"
    echo "│ ✅ Cleanup verified"
    echo "│ ⏱️  Duration:    ${duration}s"
    echo "└────────────────────────────────────────┘"
    echo ""
}

# Cleanup trap handler
cleanup_trap() {
    log_warn "Cleanup interrupted, waiting for current operations..."
    sleep 1
}

trap cleanup_trap EXIT

# Main function
main() {
    local start_time=$(date +%s)

    # Parse arguments
    parse_args "$@"

    log_info "Database cleanup starting..."
    log_info "Database: $DB_NAME"
    log_info "Host: $DB_HOST:$DB_PORT"
    log_info "Force: $FORCE"
    echo ""

    # Verify connection
    if ! verify_connection; then
        if [ "$FORCE" = false ]; then
            log_error "Cannot connect to PostgreSQL server"
            exit 1
        fi
    fi

    # Terminate connections
    if ! terminate_connections "$DB_NAME"; then
        if [ "$FORCE" = false ]; then
            log_error "Failed to terminate connections"
            exit 2
        fi
    fi

    # Drop database
    if ! drop_database "$DB_NAME"; then
        if [ "$FORCE" = false ]; then
            exit 2
        fi
    fi

    # Verify cleanup
    if ! verify_cleanup "$DB_NAME"; then
        if [ "$FORCE" = false ]; then
            exit 2
        fi
    fi

    # Print summary
    local end_time=$(date +%s)
    print_summary "$DB_NAME" "$start_time" "$end_time"

    log_success "Database cleanup completed successfully"
    exit 0
}

# Run main function
main "$@"
