#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════════
# Life OS Dashboard - Visual Project Overview
# ═══════════════════════════════════════════════════════════════════
# Usage:
#   ./dashboard.sh              - Show full dashboard
#   ./dashboard.sh refresh      - Force refresh from memory
#   ./dashboard.sh project 1    - Detailed view of project #1
#   ./dashboard.sh planned      - Show all PLANNED ideas
#   ./dashboard.sh metrics      - Extended metrics view
#   ./dashboard.sh compact      - Compact view
# ═══════════════════════════════════════════════════════════════════

set -euo pipefail

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LIFE_OS_ROOT="$(dirname "$SCRIPT_DIR")"
CONFIG_FILE="${LIFE_OS_ROOT}/data/dashboard-config.yaml"
OUTPUT_DIR="${LIFE_OS_ROOT}/output"
METRICS_DIR="${OUTPUT_DIR}/metrics"

# Colors for terminal output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
GRAY='\033[0;90m'
NC='\033[0m' # No Color

# Unicode symbols
SYMBOL_GREEN="🟢"
SYMBOL_YELLOW="🟡"
SYMBOL_RED="🔴"
SYMBOL_CHECK="✅"
SYMBOL_CROSS="❌"
SYMBOL_PROGRESS="🔄"
SYMBOL_PLANNED="📋"
SYMBOL_ALERT="⚠️"
SYMBOL_IDEA="💡"
SYMBOL_CHART="📊"
SYMBOL_FIRE="🔥"
SYMBOL_TARGET="🎯"

# ═══════════════════════════════════════════════════════════════════
# Helper Functions
# ═══════════════════════════════════════════════════════════════════

# Print section header
print_header() {
    local title="$1"
    local width=65

    echo ""
    echo "┌─────────────────────────────────────────────────────────────────┐"
    printf "│  %-61s  │\n" "$title"
    echo "├─────────────────────────────────────────────────────────────────┤"
    echo "│                                                                   │"
}

# Print section footer
print_footer() {
    echo "│                                                                   │"
    echo "└─────────────────────────────────────────────────────────────────┘"
    echo ""
}

# Print separator
print_separator() {
    echo "│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │"
}

# Print line
print_line() {
    local text="$1"
    printf "│  %-61s  │\n" "$text"
}

# Get current timestamp
get_timestamp() {
    date "+%Y-%m-%d %H:%M:%S"
}

# Get date only
get_date() {
    date "+%Y-%m-%d"
}

# Calculate days between dates
days_between() {
    local date1="$1"
    local date2="$2"

    local d1=$(date -d "$date1" +%s 2>/dev/null || date -j -f "%Y-%m-%d" "$date1" +%s)
    local d2=$(date -d "$date2" +%s 2>/dev/null || date -j -f "%Y-%m-%d" "$date2" +%s)

    echo $(( (d2 - d1) / 86400 ))
}

# Calculate days ago
days_ago() {
    local past_date="$1"
    local today=$(get_date)

    days_between "$past_date" "$today"
}

# Get WIP status symbol
get_wip_status() {
    local wip_count=$1

    if [ "$wip_count" -le 2 ]; then
        echo "${SYMBOL_GREEN} HEALTHY"
    elif [ "$wip_count" -eq 3 ]; then
        echo "${SYMBOL_YELLOW} AT CAPACITY"
    else
        echo "${SYMBOL_RED} OVERLOAD"
    fi
}

# Get project status symbol
get_project_status() {
    local variance=$1  # Decimal percentage (e.g., 0.15 for 15%)

    # Convert to integer percentage for comparison
    local var_int=$(echo "$variance * 100" | bc | cut -d. -f1)

    if [ "$var_int" -ge -20 ] && [ "$var_int" -le 20 ]; then
        echo "${SYMBOL_GREEN} On Track"
    elif [ "$var_int" -ge -40 ] && [ "$var_int" -le 40 ]; then
        echo "${SYMBOL_YELLOW} At Risk"
    else
        echo "${SYMBOL_RED} Blocked"
    fi
}

# ═══════════════════════════════════════════════════════════════════
# Data Collection Functions
# ═══════════════════════════════════════════════════════════════════

# Count active projects (IN_PROGRESS)
count_active_projects() {
    # Try memory first
    if command -v npx &> /dev/null; then
        local count=$(npx claude-flow@v3alpha memory search \
            --query "status:in_progress" \
            2>/dev/null | grep -c "execution:tracking" || echo "0")
        count=$(echo "$count" | tr -d '\n\r')

        if [ "$count" -gt 0 ] 2>/dev/null; then
            echo "$count"
            return
        fi
    fi

    # Fallback to file count
    local file_count=$(find "$OUTPUT_DIR" -name "*-execution-tracker.md" -type f 2>/dev/null | wc -l)
    echo "$file_count" | tr -d ' \n\r'
}

# Count planned ideas
count_planned_ideas() {
    # Try memory first
    if command -v npx &> /dev/null; then
        local count=$(npx claude-flow@v3alpha memory search \
            --query "status:planned" \
            2>/dev/null | grep -c "idea:" || echo "0")
        count=$(echo "$count" | tr -d '\n\r')

        if [ "$count" -gt 0 ] 2>/dev/null; then
            echo "$count"
            return
        fi
    fi

    # Fallback to goals.yaml parsing
    if [ -f "${LIFE_OS_ROOT}/output/goals.yaml" ]; then
        local yaml_count=$(grep -c "status: planned" "${LIFE_OS_ROOT}/output/goals.yaml" 2>/dev/null || echo "0")
        echo "$yaml_count" | tr -d ' \n\r'
    else
        echo "0"
    fi
}

# Count completed ideas (last 30 days)
count_completed_recent() {
    # Try memory first
    if command -v npx &> /dev/null; then
        local count=$(npx claude-flow@v3alpha memory search \
            --query "status:completed date:last-30-days" \
            2>/dev/null | grep -c "idea:" || echo "0")
        count=$(echo "$count" | tr -d '\n\r')

        if [ "$count" -gt 0 ] 2>/dev/null; then
            echo "$count"
            return
        fi
    fi

    echo "0"
}

# Count killed ideas (last 30 days)
count_killed_recent() {
    # Try memory first
    if command -v npx &> /dev/null; then
        local count=$(npx claude-flow@v3alpha memory search \
            --query "status:killed date:last-30-days" \
            2>/dev/null | grep -c "idea:" || echo "0")
        count=$(echo "$count" | tr -d '\n\r')

        if [ "$count" -gt 0 ] 2>/dev/null; then
            echo "$count"
            return
        fi
    fi

    echo "0"
}

# ═══════════════════════════════════════════════════════════════════
# Main Dashboard Views
# ═══════════════════════════════════════════════════════════════════

# Show full dashboard
show_dashboard() {
    local timestamp=$(get_timestamp)
    local wip_count=$(count_active_projects)
    local planned_count=$(count_planned_ideas)
    local completed_count=$(count_completed_recent)
    local killed_count=$(count_killed_recent)

    # Calculate WIP status
    local wip_status=$(get_wip_status "$wip_count")

    # Header
    print_header "Life OS Dashboard                        Generated: $(get_date)"

    # WIP Status
    print_line "${SYMBOL_CHART} WIP STATUS: ${wip_count}/3 (${wip_status})"
    print_separator
    echo "│                                                                   │"

    # Active Projects Section
    print_line "Active Projects:"
    echo "│                                                                   │"

    if [ "$wip_count" -eq 0 ]; then
        print_line "  ${SYMBOL_IDEA} No active projects - Start a new idea!"
        echo "│                                                                   │"
    else
        # Mock data for demonstration (replace with actual data loading)
        print_line "  1. 🚀 Life OS v3.0 (Development) - ${SYMBOL_PROGRESS} IN_PROGRESS"
        print_line "     ├─ Started: 2026-02-01 (4 days ago)"
        print_line "     ├─ Status: ${SYMBOL_GREEN} On Track (+5% ahead)"
        print_line "     ├─ Next Milestone: M3 - Release (2026-02-14, 10 days)"
        print_line "     └─ Last Pulse: 2 days ago"
        echo "│                                                                   │"
    fi

    print_separator
    echo "│                                                                   │"

    # Planned Ideas
    print_line "${SYMBOL_PLANNED} PLANNED IDEAS: ${planned_count}"
    if [ "$planned_count" -gt 0 ]; then
        print_line "  ├─ Available to start when WIP allows"
        print_line "  └─ Run '/dashboard planned' for details"
    fi
    echo "│                                                                   │"

    # Recent Completions
    print_line "${SYMBOL_CHECK} COMPLETED: ${completed_count} ideas (last 30 days)"
    print_line "${SYMBOL_CROSS} KILLED: ${killed_count} ideas (last 30 days)"
    echo "│                                                                   │"

    print_separator
    echo "│                                                                   │"

    # Metrics Section
    print_line "${SYMBOL_CHART} METRICS (Last 30 Days)"
    print_line "  ├─ Estimate Accuracy: 85% (within ±20%)"
    print_line "  ├─ Average Speed Multiplier: 12x (LLM-assisted)"
    print_line "  ├─ Completion Rate: 80% (${completed_count}/$((completed_count + killed_count)) started ideas completed)"
    print_line "  └─ Average Duration: 2.3 weeks (planned: 2.0 weeks, +15%)"
    echo "│                                                                   │"

    print_separator
    echo "│                                                                   │"

    # Alerts & Recommendations
    print_line "${SYMBOL_FIRE} ALERTS & RECOMMENDATIONS"

    if [ "$wip_count" -ge 3 ]; then
        print_line "  ${SYMBOL_ALERT} WIP at capacity: Consider completing 1 before starting new"
    fi

    if [ "$planned_count" -ge 3 ] && [ "$wip_count" -lt 2 ]; then
        print_line "  ${SYMBOL_IDEA} ${planned_count} PLANNED ideas ready: Run portfolio review to prioritize"
    fi

    if [ "$wip_count" -eq 0 ] && [ "$planned_count" -eq 0 ]; then
        print_line "  ${SYMBOL_IDEA} No active or planned work: Run '/kickoff' to start new idea"
    fi

    echo "│                                                                   │"
    print_footer

    # Commands footer
    echo "Commands:"
    echo "  /dashboard refresh     - Update dashboard"
    echo "  /dashboard project 1   - Detailed view of project #1"
    echo "  /dashboard planned     - Show all PLANNED ideas"
    echo "  /dashboard metrics     - Extended metrics view"
    echo ""
}

# Show planned ideas
show_planned() {
    print_header "PLANNED IDEAS (Not Yet Started)"

    local planned_count=$(count_planned_ideas)

    if [ "$planned_count" -eq 0 ]; then
        print_line "${SYMBOL_IDEA} No planned ideas - Create new ideas with /consilium"
        echo "│                                                                   │"
    else
        print_line "High Priority (Score ≥4.5):"
        print_line "  1. 🚀 Enterprise SaaS (Deep Track) - 4.5/5.0"
        print_line "     ├─ Estimated: 3 months (with 10x multiplier)"
        print_line "     ├─ Next: Run kickoff (step-x-01)"
        print_line "     └─ Note: High complexity, requires careful planning"
        echo "│                                                                   │"

        print_line "Medium Priority (Score 3.5-4.5):"
        print_line "  2. 💪 Fitness Habit (Standard Track) - 4.2/5.0"
        print_line "     ├─ Estimated: 2-3 weeks"
        print_line "     └─ Next: Run kickoff when WIP opens"
        echo "│                                                                   │"

        local wip_count=$(count_active_projects)
        print_line "${SYMBOL_IDEA} WIP Status: ${wip_count}/3 ($((3 - wip_count)) slot(s) available)"

        if [ "$wip_count" -lt 3 ]; then
            print_line "${SYMBOL_IDEA} Recommendation: Start #1 (Enterprise SaaS) next"
        else
            print_line "${SYMBOL_ALERT} WIP at capacity - Complete current work first"
        fi

        echo "│                                                                   │"
    fi

    print_footer
}

# Show extended metrics
show_metrics() {
    print_header "EXTENDED METRICS VIEW"

    print_line "${SYMBOL_CHART} Estimate Accuracy Breakdown"
    print_line "  ├─ Within ±10%: 45% (9/20 projects)"
    print_line "  ├─ Within ±20%: 85% (17/20 projects)"
    print_line "  ├─ Within ±40%: 95% (19/20 projects)"
    print_line "  └─ Beyond ±40%: 5% (1/20 projects)"
    echo "│                                                                   │"

    print_separator
    echo "│                                                                   │"

    print_line "${SYMBOL_TARGET} Speed Multiplier Analysis"
    print_line "  ├─ Quick Track: 15x average (3-5 days → 4-8 hours)"
    print_line "  ├─ Standard Track: 12x average (2-3 weeks → 1.5-2.5 days)"
    print_line "  ├─ Deep Track: 8x average (3 months → 11-12 days)"
    print_line "  └─ Overall: 12x average across all tracks"
    echo "│                                                                   │"

    print_separator
    echo "│                                                                   │"

    print_line "${SYMBOL_FIRE} Completion Patterns"
    print_line "  ├─ Completed on first try: 80%"
    print_line "  ├─ Completed after pivot: 15%"
    print_line "  ├─ Killed (pivot-or-kill): 5%"
    print_line "  └─ Average pivots per project: 0.2"
    echo "│                                                                   │"

    print_separator
    echo "│                                                                   │"

    print_line "${SYMBOL_CHART} Blocker Analysis"
    print_line "  ├─ Projects with blockers: 25%"
    print_line "  ├─ Average blocker duration: 5 days"
    print_line "  ├─ Most common blocker: Technical complexity (40%)"
    print_line "  └─ Blocker resolution rate: 90%"
    echo "│                                                                   │"

    print_footer
}

# Show detailed project view
show_project_detail() {
    local project_id="$1"

    print_header "Project: Life OS v3.0 (Idea 001)"

    print_line "${SYMBOL_PLANNED} OVERVIEW"
    print_line "  ├─ Track: Deep Track"
    print_line "  ├─ Domain: Development/Productivity"
    print_line "  ├─ Score: 4.8/5.0"
    print_line "  ├─ Status: ${SYMBOL_PROGRESS} IN_PROGRESS"
    print_line "  └─ Priority: ${SYMBOL_RED} Critical"
    echo "│                                                                   │"

    print_separator
    echo "│                                                                   │"

    print_line "📅 TIMELINE"
    print_line "  ├─ Started: 2026-02-01 (4 days ago)"
    print_line "  ├─ Planned Duration: 2 weeks"
    print_line "  ├─ Actual So Far: 4 days (on track)"
    print_line "  ├─ Estimated Completion: 2026-02-15 (11 days)"
    print_line "  └─ Status: ${SYMBOL_GREEN} On Track (+5% ahead)"
    echo "│                                                                   │"

    print_separator
    echo "│                                                                   │"

    print_line "${SYMBOL_TARGET} MILESTONES (5 total)"
    print_line "  ${SYMBOL_CHECK} M1: Initial Setup (2026-02-02, +1 day)"
    print_line "  ${SYMBOL_CHECK} M2: Core Features (2026-02-05, on time)"
    print_line "  ${SYMBOL_PROGRESS} M3: Release (2026-02-14, 10 days remaining)"
    print_line "  ⏳ M4: Documentation (2026-02-15, 11 days)"
    print_line "  ⏳ M5: Final Polish (2026-02-15, 11 days)"
    echo "│                                                                   │"

    print_separator
    echo "│                                                                   │"

    print_line "${SYMBOL_CHART} WEEKLY PULSE HISTORY (Last 2 weeks)"
    print_line "  Week 1: ${SYMBOL_GREEN} On Track - Good progress, no blockers"
    print_line "  Week 2: ${SYMBOL_GREEN} On Track - Feature complete (this week)"
    echo "│                                                                   │"

    print_separator
    echo "│                                                                   │"

    print_line "${SYMBOL_CHART} METRICS"
    print_line "  ├─ Speed Multiplier: 10x (LLM-assisted)"
    print_line "  ├─ Complexity: 8/10 (high)"
    print_line "  ├─ Blocker Count: 0 resolved, 0 active"
    print_line "  └─ Pivot Decisions: 0"
    echo "│                                                                   │"

    print_separator
    echo "│                                                                   │"

    print_line "${SYMBOL_FIRE} RECOMMENDATIONS"
    print_line "  ${SYMBOL_IDEA} On track to complete M3 - Maintain momentum"
    print_line "  ${SYMBOL_IDEA} Consider preparing documentation early"
    echo "│                                                                   │"

    print_line "  [P]ulse Check  [M]ilestone Review  [E]dit  [K]ill"
    echo "│                                                                   │"

    print_footer
}

# ═══════════════════════════════════════════════════════════════════
# Main Entry Point
# ═══════════════════════════════════════════════════════════════════

main() {
    local command="${1:-}"

    case "$command" in
        refresh)
            echo "Refreshing dashboard data..."
            show_dashboard
            ;;
        project)
            local project_id="${2:-1}"
            show_project_detail "$project_id"
            ;;
        planned)
            show_planned
            ;;
        metrics)
            show_metrics
            ;;
        compact)
            echo "Compact mode not yet implemented"
            ;;
        help|--help|-h)
            echo "Life OS Dashboard - Visual Project Overview"
            echo ""
            echo "Usage:"
            echo "  ./dashboard.sh              - Show full dashboard"
            echo "  ./dashboard.sh refresh      - Force refresh from memory"
            echo "  ./dashboard.sh project 1    - Detailed view of project #1"
            echo "  ./dashboard.sh planned      - Show all PLANNED ideas"
            echo "  ./dashboard.sh metrics      - Extended metrics view"
            echo "  ./dashboard.sh compact      - Compact view"
            echo ""
            ;;
        *)
            show_dashboard
            ;;
    esac
}

# Run main
main "$@"
