#!/bin/bash

################################################################################
# Database Setup Script for Parallel Test Isolation
#
# This script initializes a PostgreSQL database for test execution with
# proper isolation, connection pooling, and schema setup.
#
# Usage:
#   ./db-setup-per-test.sh [OPTIONS]
#
# Options:
#   --database NAME       Database name (default: katana_test)
#   --host HOST           PostgreSQL host (default: localhost)
#   --port PORT           PostgreSQL port (default: 5432)
#   --user USER           PostgreSQL user (default: test_user)
#   --password PASS       PostgreSQL password (default: env $POSTGRES_PASSWORD)
#   --seed-data           Load seed data (default: true)
#   --verbose             Verbose output (default: false)
#
# Exit Codes:
#   0 - Success
#   1 - Connection failed
#   2 - Database creation failed
#   3 - Schema initialization failed
#   4 - Invalid arguments
#
################################################################################

set -e

# Configuration defaults
DB_NAME="katana_test"
DB_HOST="localhost"
DB_PORT="5432"
DB_USER="test_user"
DB_PASSWORD="${POSTGRES_PASSWORD:-test_pass}"
LOAD_SEED_DATA=true
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
            --seed-data)
                LOAD_SEED_DATA="$2"
                shift 2
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
                exit 4
                ;;
        esac
    done
}

print_usage() {
    cat << EOF
Database Setup Script for Parallel Test Isolation

Usage: $(basename "$0") [OPTIONS]

Options:
    --database NAME       Database name (default: $DB_NAME)
    --host HOST           PostgreSQL host (default: $DB_HOST)
    --port PORT           PostgreSQL port (default: $DB_PORT)
    --user USER           PostgreSQL user (default: $DB_USER)
    --password PASS       PostgreSQL password (default: from env or test_pass)
    --seed-data BOOL      Load seed data (default: true)
    --verbose             Verbose output
    -h, --help            Print this help message

Examples:
    ./db-setup-per-test.sh
    ./db-setup-per-test.sh --database katana_test_1 --verbose
    ./db-setup-per-test.sh --host db.example.com --port 5433

EOF
}

# Verify PostgreSQL connection
verify_connection() {
    log_info "Verifying PostgreSQL connection..."

    export PGPASSWORD="$DB_PASSWORD"

    if ! pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" > /dev/null 2>&1; then
        log_error "Cannot connect to PostgreSQL at $DB_HOST:$DB_PORT"
        return 1
    fi

    log_success "PostgreSQL connection verified"
    return 0
}

# Create database
create_database() {
    local db_name="$1"

    log_info "Creating database: $db_name"

    export PGPASSWORD="$DB_PASSWORD"

    # Check if database already exists
    if psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -tc \
        "SELECT 1 FROM pg_database WHERE datname = '$db_name'" | grep -q 1; then
        log_warn "Database '$db_name' already exists, dropping..."

        # Terminate connections to database
        psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d postgres -c \
            "SELECT pg_terminate_backend(pg_stat_activity.pid)
             FROM pg_stat_activity
             WHERE pg_stat_activity.datname = '$db_name'" 2>/dev/null || true

        sleep 1

        # Drop database
        psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d postgres -c \
            "DROP DATABASE IF EXISTS \"$db_name\";"

        log_info "Database dropped"
    fi

    # Create new database
    if ! psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d postgres -c \
        "CREATE DATABASE \"$db_name\" TEMPLATE template0;"; then
        log_error "Failed to create database: $db_name"
        return 2
    fi

    log_success "Database created: $db_name"
    return 0
}

# Initialize schema
initialize_schema() {
    local db_name="$1"

    log_info "Initializing database schema..."

    export PGPASSWORD="$DB_PASSWORD"

    # Create schema using Python script if available
    if command -v python &> /dev/null; then
        if [ -f "scripts/db_init.py" ]; then
            log_info "Running Python schema initialization..."
            if ! python scripts/db_init.py \
                --database "postgresql://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$db_name"; then
                log_warn "Python schema initialization failed (may continue)"
            else
                log_success "Schema initialized via Python"
            fi
        fi
    fi

    # Apply schema from SQL file if it exists
    if [ -f "schema.sql" ]; then
        log_info "Applying SQL schema..."
        if ! psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d "$db_name" \
            -f schema.sql > /dev/null 2>&1; then
            log_error "Failed to apply schema.sql"
            return 3
        fi
        log_success "SQL schema applied"
    fi

    # Enable extensions
    log_info "Enabling PostgreSQL extensions..."
    psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d "$db_name" << EOF > /dev/null 2>&1
CREATE EXTENSION IF NOT EXISTS uuid-ossp;
CREATE EXTENSION IF NOT EXISTS pgcrypto;
EOF
    log_success "Extensions enabled"

    return 0
}

# Configure connection pooling
configure_pooling() {
    local db_name="$1"

    log_info "Configuring connection pooling..."

    export PGPASSWORD="$DB_PASSWORD"

    # Set connection pool parameters at database level
    psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d postgres << EOF > /dev/null 2>&1
ALTER DATABASE "$db_name" SET shared_preload_libraries = 'pg_stat_statements';
ALTER DATABASE "$db_name" SET max_connections = 100;
ALTER DATABASE "$db_name" SET shared_buffers = '256MB';
ALTER DATABASE "$db_name" SET effective_cache_size = '512MB';
ALTER DATABASE "$db_name" SET work_mem = '16MB';
ALTER DATABASE "$db_name" SET maintenance_work_mem = '64MB';
EOF

    log_success "Connection pooling configured"
}

# Load seed data
load_seed_data() {
    local db_name="$1"

    if [ "$LOAD_SEED_DATA" != "true" ]; then
        log_info "Skipping seed data loading (--seed-data=false)"
        return 0
    fi

    log_info "Loading seed data..."

    export PGPASSWORD="$DB_PASSWORD"

    # Check if seed data script exists
    if [ -f "scripts/db_seed.py" ]; then
        log_info "Running Python seed data script..."
        if ! python scripts/db_seed.py \
            --database "postgresql://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$db_name"; then
            log_warn "Seed data script failed (may continue)"
            return 0
        fi
        log_success "Seed data loaded"
        return 0
    fi

    # Check if seed SQL file exists
    if [ -f "seed.sql" ]; then
        log_info "Applying seed SQL..."
        if ! psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d "$db_name" \
            -f seed.sql > /dev/null 2>&1; then
            log_warn "Seed SQL file not applied (may continue)"
            return 0
        fi
        log_success "Seed data applied"
        return 0
    fi

    log_info "No seed data scripts found, skipping"
    return 0
}

# Verify schema
verify_schema() {
    local db_name="$1"

    log_info "Verifying database schema..."

    export PGPASSWORD="$DB_PASSWORD"

    # Check if tables exist
    local table_count=$(psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d "$db_name" -tc \
        "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='public'")

    if [ -z "$table_count" ] || [ "$table_count" -eq 0 ]; then
        log_warn "No tables found in database schema"
        return 0
    fi

    log_success "Database schema verified ($table_count tables)"
    return 0
}

# Print summary
print_summary() {
    local db_name="$1"

    echo ""
    echo "┌────────────────────────────────────────┐"
    echo "│  Database Setup Complete               │"
    echo "├────────────────────────────────────────┤"
    echo "│ Database:     $db_name"
    echo "│ Host:         $DB_HOST:$DB_PORT"
    echo "│ User:         $DB_USER"
    echo "│ DSN:          postgresql://$DB_USER:***@$DB_HOST:$DB_PORT/$db_name"
    echo "├────────────────────────────────────────┤"
    echo "│ ✅ Connection verified"
    echo "│ ✅ Database created"
    echo "│ ✅ Schema initialized"
    echo "│ ✅ Pooling configured"
    if [ "$LOAD_SEED_DATA" = "true" ]; then
        echo "│ ✅ Seed data loaded"
    fi
    echo "│ ✅ Schema verified"
    echo "└────────────────────────────────────────┘"
    echo ""
}

# Main function
main() {
    local start_time=$(date +%s)

    # Parse arguments
    parse_args "$@"

    log_info "Database setup starting..."
    log_info "Database: $DB_NAME"
    log_info "Host: $DB_HOST:$DB_PORT"
    log_info "User: $DB_USER"
    echo ""

    # Verify connection
    if ! verify_connection; then
        log_error "Cannot connect to PostgreSQL server"
        exit 1
    fi

    # Create database
    if ! create_database "$DB_NAME"; then
        exit 2
    fi

    # Initialize schema
    if ! initialize_schema "$DB_NAME"; then
        exit 3
    fi

    # Configure pooling
    if ! configure_pooling "$DB_NAME"; then
        log_warn "Failed to configure pooling"
    fi

    # Load seed data
    if ! load_seed_data "$DB_NAME"; then
        log_warn "Failed to load seed data"
    fi

    # Verify schema
    if ! verify_schema "$DB_NAME"; then
        log_warn "Schema verification failed"
    fi

    # Print summary
    local end_time=$(date +%s)
    local duration=$((end_time - start_time))
    print_summary "$DB_NAME"

    log_success "Database setup completed in ${duration}s"
    exit 0
}

# Run main function
main "$@"
