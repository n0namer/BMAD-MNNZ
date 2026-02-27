#!/usr/bin/env bash
###############################################################################
# review-reminders.sh
#
# Automated reminder system for PDCA reviews across 4 cadences:
# - Daily (EOD - 18:00): 5-min standup prompt
# - Weekly (Sunday): 30-min velocity review prompt
# - Monthly (Last Sunday): 1-hour trajectory analysis prompt
# - Quarterly (End of quarter): 2-hour strategic replanning prompt
#
# Usage:
#   ./review-reminders.sh              # Check and prompt for due reviews
#   ./review-reminders.sh --check      # Check only, don't prompt
#   ./review-reminders.sh --force daily    # Force prompt for specific cadence
#
# Cron setup (run every hour):
#   0 * * * * /path/to/review-reminders.sh >> /var/log/pdca-reminders.log 2>&1
###############################################################################

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LIFE_OS_ROOT="$(dirname "$SCRIPT_DIR")"
REVIEWS_DIR="$LIFE_OS_ROOT/data/reviews"
MEMORY_CMD="npx claude-flow@v3alpha memory"

# Review cadences configuration
DAILY_TIME="18:00"          # 6:00 PM
WEEKLY_DAY="0"              # Sunday (0-6, 0=Sunday)
WEEKLY_TIME="19:00"         # 7:00 PM Sunday
MONTHLY_DAY_OFFSET=7        # Last 7 days of month
MONTHLY_TIME="19:00"        # 7:00 PM last Sunday
QUARTERLY_DAY_OFFSET=7      # Last 7 days of quarter

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

log_prompt() {
    echo -e "${MAGENTA}${BOLD}$1${NC}"
}

# Get current date/time info
get_current_info() {
    CURRENT_DATE=$(date +%Y-%m-%d)
    CURRENT_TIME=$(date +%H:%M)
    CURRENT_HOUR=$(date +%H)
    CURRENT_DOW=$(date +%u)  # 1-7 (Monday=1, Sunday=7)
    CURRENT_DAY=$(date +%d)
    CURRENT_MONTH=$(date +%m)
    CURRENT_YEAR=$(date +%Y)
    DAYS_IN_MONTH=$(date -d "$CURRENT_YEAR-$CURRENT_MONTH-01 +1 month -1 day" +%d)
}

# Check if review was already done today/this week/this month
check_last_review() {
    local cadence=$1
    local review_file=""

    case $cadence in
        daily)
            review_file="$REVIEWS_DIR/daily/$CURRENT_DATE.md"
            ;;
        weekly)
            local week_num=$(date +%V)
            review_file="$REVIEWS_DIR/weekly/${CURRENT_YEAR}-W${week_num}.md"
            ;;
        monthly)
            review_file="$REVIEWS_DIR/monthly/${CURRENT_YEAR}-${CURRENT_MONTH}.md"
            ;;
        quarterly)
            local quarter=$(( (CURRENT_MONTH - 1) / 3 + 1 ))
            review_file="$REVIEWS_DIR/quarterly/Q${quarter}-${CURRENT_YEAR}.md"
            ;;
    esac

    if [[ -f "$review_file" ]]; then
        return 0  # Review exists (already done)
    else
        return 1  # Review not done yet
    fi
}

# Store reminder delivery in memory
log_reminder_to_memory() {
    local cadence=$1
    local timestamp=$(date -Iseconds)

    log_info "Logging reminder to memory: $cadence"

    # Store in memory (silent, don't show output unless error)
    $MEMORY_CMD store \
        --namespace "life-os:reviews" \
        --key "reminder:$cadence:$CURRENT_DATE" \
        --content "Reminder delivered at $timestamp" \
        > /dev/null 2>&1 || log_warning "Failed to log to memory (non-critical)"
}

# Check if it's time for daily review
check_daily_review() {
    if [[ "$CURRENT_TIME" < "$DAILY_TIME" ]]; then
        return 1  # Not time yet
    fi

    if [[ "$CURRENT_HOUR" -gt 22 ]]; then
        return 1  # Too late (after 10 PM)
    fi

    if check_last_review "daily"; then
        log_info "Daily review already completed for $CURRENT_DATE"
        return 1
    fi

    return 0  # Time for daily review
}

# Check if it's time for weekly review
check_weekly_review() {
    # Check if it's Sunday (DOW 7 or 0 depending on system)
    if [[ "$CURRENT_DOW" -ne 7 ]] && [[ "$(date +%w)" -ne 0 ]]; then
        return 1  # Not Sunday
    fi

    if [[ "$CURRENT_TIME" < "$WEEKLY_TIME" ]]; then
        return 1  # Not time yet
    fi

    if check_last_review "weekly"; then
        log_info "Weekly review already completed for this week"
        return 1
    fi

    return 0  # Time for weekly review
}

# Check if it's time for monthly review
check_monthly_review() {
    # Check if we're in last 7 days of month
    local days_remaining=$((DAYS_IN_MONTH - CURRENT_DAY))
    if [[ $days_remaining -gt $MONTHLY_DAY_OFFSET ]]; then
        return 1  # Not last week of month
    fi

    # Check if it's Sunday
    if [[ "$CURRENT_DOW" -ne 7 ]] && [[ "$(date +%w)" -ne 0 ]]; then
        return 1  # Not Sunday
    fi

    if [[ "$CURRENT_TIME" < "$MONTHLY_TIME" ]]; then
        return 1  # Not time yet
    fi

    if check_last_review "monthly"; then
        log_info "Monthly review already completed for this month"
        return 1
    fi

    return 0  # Time for monthly review
}

# Check if it's time for quarterly review
check_quarterly_review() {
    local quarter=$(( (CURRENT_MONTH - 1) / 3 + 1 ))
    local quarter_end_month=$(( quarter * 3 ))

    # Check if we're in the last month of quarter
    if [[ $CURRENT_MONTH -ne $quarter_end_month ]]; then
        return 1  # Not last month of quarter
    fi

    # Check if we're in last 7 days of month
    local days_remaining=$((DAYS_IN_MONTH - CURRENT_DAY))
    if [[ $days_remaining -gt $QUARTERLY_DAY_OFFSET ]]; then
        return 1  # Not last week of quarter
    fi

    if check_last_review "quarterly"; then
        log_info "Quarterly review already completed for Q$quarter"
        return 1
    fi

    return 0  # Time for quarterly review
}

# Display review prompt
prompt_review() {
    local cadence=$1
    local duration=$2
    local description=$3

    echo ""
    log_prompt "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    log_prompt "⏰ TIME FOR ${cadence^^} REVIEW!"
    log_prompt "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo -e "${CYAN}Duration:${NC} $duration"
    echo -e "${CYAN}Purpose:${NC} $description"
    echo ""
    echo -e "${YELLOW}Run:${NC} ${BOLD}step-07-pdca-review.md${NC} and select ${BOLD}$cadence${NC} cadence"
    echo ""
    log_prompt "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""

    # Log reminder delivery
    log_reminder_to_memory "$cadence"
}

# Main logic
main() {
    local check_only=false
    local force_cadence=""

    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --check)
                check_only=true
                shift
                ;;
            --force)
                force_cadence="$2"
                shift 2
                ;;
            -h|--help)
                echo "Usage: $0 [OPTIONS]"
                echo ""
                echo "Options:"
                echo "  --check          Check only, don't prompt"
                echo "  --force CADENCE  Force prompt for specific cadence (daily/weekly/monthly/quarterly)"
                echo "  -h, --help       Show this help message"
                exit 0
                ;;
            *)
                log_error "Unknown option: $1"
                exit 1
                ;;
        esac
    done

    # Ensure reviews directories exist
    mkdir -p "$REVIEWS_DIR"/{daily,weekly,monthly,quarterly}

    # Get current date/time
    get_current_info

    log_info "PDCA Review Reminder Check - $CURRENT_DATE $CURRENT_TIME"

    # Force mode
    if [[ -n "$force_cadence" ]]; then
        case $force_cadence in
            daily)
                prompt_review "daily" "5 minutes" "Quick EOD standup: what done, what blocked, learnings"
                ;;
            weekly)
                prompt_review "weekly" "30 minutes" "Progress to weekly goals, velocity analysis, adjust next week"
                ;;
            monthly)
                prompt_review "monthly" "1 hour" "Trajectory to quarterly goals, trend analysis, goal adjustments"
                ;;
            quarterly)
                prompt_review "quarterly" "2 hours" "Quarter goal achievement, strategic replanning, set next quarter OKRs"
                ;;
            *)
                log_error "Invalid cadence: $force_cadence"
                exit 1
                ;;
        esac
        exit 0
    fi

    # Check cadences in priority order (higher priority = more important)
    # Priority: Quarterly > Monthly > Weekly > Daily

    if check_quarterly_review; then
        if $check_only; then
            log_success "Quarterly review is DUE"
        else
            prompt_review "quarterly" "2 hours" "Quarter goal achievement, strategic replanning, set next quarter OKRs"
        fi
        exit 0
    fi

    if check_monthly_review; then
        if $check_only; then
            log_success "Monthly review is DUE"
        else
            prompt_review "monthly" "1 hour" "Trajectory to quarterly goals, trend analysis, goal adjustments"
        fi
        exit 0
    fi

    if check_weekly_review; then
        if $check_only; then
            log_success "Weekly review is DUE"
        else
            prompt_review "weekly" "30 minutes" "Progress to weekly goals, velocity analysis, adjust next week"
        fi
        exit 0
    fi

    if check_daily_review; then
        if $check_only; then
            log_success "Daily review is DUE"
        else
            prompt_review "daily" "5 minutes" "Quick EOD standup: what done, what blocked, learnings"
        fi
        exit 0
    fi

    # No reviews due
    if $check_only; then
        log_info "No reviews currently due"
    fi
}

# Run main
main "$@"
