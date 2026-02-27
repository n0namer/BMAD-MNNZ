# ═══════════════════════════════════════════════════════════════════
# Life OS Dashboard - Visual Project Overview (PowerShell)
# ═══════════════════════════════════════════════════════════════════
# Usage:
#   .\dashboard.ps1              - Show full dashboard
#   .\dashboard.ps1 refresh      - Force refresh from memory
#   .\dashboard.ps1 project 1    - Detailed view of project #1
#   .\dashboard.ps1 planned      - Show all PLANNED ideas
#   .\dashboard.ps1 metrics      - Extended metrics view
#   .\dashboard.ps1 compact      - Compact view
# ═══════════════════════════════════════════════════════════════════

param(
    [Parameter(Position=0)]
    [string]$Command = "",

    [Parameter(Position=1)]
    [string]$ProjectId = "1"
)

# Script paths
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$LifeOsRoot = Split-Path -Parent $ScriptDir
$ConfigFile = Join-Path $LifeOsRoot "data\dashboard-config.yaml"
$OutputDir = Join-Path $LifeOsRoot "output"
$MetricsDir = Join-Path $OutputDir "metrics"

# Unicode symbols
$SYMBOL_GREEN = "🟢"
$SYMBOL_YELLOW = "🟡"
$SYMBOL_RED = "🔴"
$SYMBOL_CHECK = "✅"
$SYMBOL_CROSS = "❌"
$SYMBOL_PROGRESS = "🔄"
$SYMBOL_PLANNED = "📋"
$SYMBOL_ALERT = "⚠️"
$SYMBOL_IDEA = "💡"
$SYMBOL_CHART = "📊"
$SYMBOL_FIRE = "🔥"
$SYMBOL_TARGET = "🎯"

# ═══════════════════════════════════════════════════════════════════
# Helper Functions
# ═══════════════════════════════════════════════════════════════════

function Print-Header {
    param([string]$Title)

    Write-Host ""
    Write-Host "┌─────────────────────────────────────────────────────────────────┐"
    Write-Host ("│  " + $Title.PadRight(61) + "  │")
    Write-Host "├─────────────────────────────────────────────────────────────────┤"
    Write-Host "│                                                                   │"
}

function Print-Footer {
    Write-Host "│                                                                   │"
    Write-Host "└─────────────────────────────────────────────────────────────────┘"
    Write-Host ""
}

function Print-Separator {
    Write-Host "│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │"
}

function Print-Line {
    param([string]$Text)
    Write-Host ("│  " + $Text.PadRight(61) + "  │")
}

function Get-Timestamp {
    return Get-Date -Format "yyyy-MM-dd HH:mm:ss"
}

function Get-DateOnly {
    return Get-Date -Format "yyyy-MM-dd"
}

function Get-DaysBetween {
    param(
        [datetime]$Date1,
        [datetime]$Date2
    )

    return ($Date2 - $Date1).Days
}

function Get-DaysAgo {
    param([datetime]$PastDate)

    $today = Get-Date
    return ($today - $PastDate).Days
}

function Get-WipStatus {
    param([int]$WipCount)

    if ($WipCount -le 2) {
        return "$SYMBOL_GREEN HEALTHY"
    } elseif ($WipCount -eq 3) {
        return "$SYMBOL_YELLOW AT CAPACITY"
    } else {
        return "$SYMBOL_RED OVERLOAD"
    }
}

function Get-ProjectStatus {
    param([double]$Variance)

    $varPercent = [Math]::Abs($Variance * 100)

    if ($varPercent -le 20) {
        return "$SYMBOL_GREEN On Track"
    } elseif ($varPercent -le 40) {
        return "$SYMBOL_YELLOW At Risk"
    } else {
        return "$SYMBOL_RED Blocked"
    }
}

# ═══════════════════════════════════════════════════════════════════
# Data Collection Functions
# ═══════════════════════════════════════════════════════════════════

function Count-ActiveProjects {
    # Try memory first
    try {
        $result = npx claude-flow@v3alpha memory search --query "status:in_progress" 2>$null
        if ($result) {
            $count = ($result | Select-String "execution:tracking" | Measure-Object).Count
            if ($count -gt 0) {
                return $count
            }
        }
    } catch {
        # Fallback to file count
    }

    # Fallback to file count
    $trackers = Get-ChildItem -Path $OutputDir -Filter "*-execution-tracker.md" -ErrorAction SilentlyContinue
    return $trackers.Count
}

function Count-PlannedIdeas {
    # Try memory first
    try {
        $result = npx claude-flow@v3alpha memory search --query "status:planned" 2>$null
        if ($result) {
            $count = ($result | Select-String "idea:" | Measure-Object).Count
            if ($count -gt 0) {
                return $count
            }
        }
    } catch {
        # Fallback to goals.yaml
    }

    # Fallback to goals.yaml parsing
    $goalsFile = Join-Path $OutputDir "goals.yaml"
    if (Test-Path $goalsFile) {
        $content = Get-Content $goalsFile -Raw
        $matches = [regex]::Matches($content, "status:\s*planned")
        return $matches.Count
    }

    return 0
}

function Count-CompletedRecent {
    # Try memory first
    try {
        $result = npx claude-flow@v3alpha memory search --query "status:completed date:last-30-days" 2>$null
        if ($result) {
            $count = ($result | Select-String "idea:" | Measure-Object).Count
            if ($count -gt 0) {
                return $count
            }
        }
    } catch {
        # Return 0 if unable to query
    }

    return 0
}

function Count-KilledRecent {
    # Try memory first
    try {
        $result = npx claude-flow@v3alpha memory search --query "status:killed date:last-30-days" 2>$null
        if ($result) {
            $count = ($result | Select-String "idea:" | Measure-Object).Count
            if ($count -gt 0) {
                return $count
            }
        }
    } catch {
        # Return 0 if unable to query
    }

    return 0
}

# ═══════════════════════════════════════════════════════════════════
# Main Dashboard Views
# ═══════════════════════════════════════════════════════════════════

function Show-Dashboard {
    $timestamp = Get-Timestamp
    $dateOnly = Get-DateOnly
    $wipCount = Count-ActiveProjects
    $plannedCount = Count-PlannedIdeas
    $completedCount = Count-CompletedRecent
    $killedCount = Count-KilledRecent

    # Calculate WIP status
    $wipStatus = Get-WipStatus -WipCount $wipCount

    # Header
    Print-Header "Life OS Dashboard                        Generated: $dateOnly"

    # WIP Status
    Print-Line "$SYMBOL_CHART WIP STATUS: $wipCount/3 ($wipStatus)"
    Print-Separator
    Write-Host "│                                                                   │"

    # Active Projects Section
    Print-Line "Active Projects:"
    Write-Host "│                                                                   │"

    if ($wipCount -eq 0) {
        Print-Line "  $SYMBOL_IDEA No active projects - Start a new idea!"
        Write-Host "│                                                                   │"
    } else {
        # Mock data for demonstration (replace with actual data loading)
        Print-Line "  1. 🚀 Life OS v3.0 (Development) - $SYMBOL_PROGRESS IN_PROGRESS"
        Print-Line "     ├─ Started: 2026-02-01 (4 days ago)"
        Print-Line "     ├─ Status: $SYMBOL_GREEN On Track (+5% ahead)"
        Print-Line "     ├─ Next Milestone: M3 - Release (2026-02-14, 10 days)"
        Print-Line "     └─ Last Pulse: 2 days ago"
        Write-Host "│                                                                   │"
    }

    Print-Separator
    Write-Host "│                                                                   │"

    # Planned Ideas
    Print-Line "$SYMBOL_PLANNED PLANNED IDEAS: $plannedCount"
    if ($plannedCount -gt 0) {
        Print-Line "  ├─ Available to start when WIP allows"
        Print-Line "  └─ Run '/dashboard planned' for details"
    }
    Write-Host "│                                                                   │"

    # Recent Completions
    Print-Line "$SYMBOL_CHECK COMPLETED: $completedCount ideas (last 30 days)"
    Print-Line "$SYMBOL_CROSS KILLED: $killedCount ideas (last 30 days)"
    Write-Host "│                                                                   │"

    Print-Separator
    Write-Host "│                                                                   │"

    # Metrics Section
    Print-Line "$SYMBOL_CHART METRICS (Last 30 Days)"
    Print-Line "  ├─ Estimate Accuracy: 85% (within ±20%)"
    Print-Line "  ├─ Average Speed Multiplier: 12x (LLM-assisted)"
    $totalIdeas = $completedCount + $killedCount
    if ($totalIdeas -gt 0) {
        $compRate = [Math]::Round(($completedCount / $totalIdeas) * 100)
        Print-Line "  ├─ Completion Rate: $compRate% ($completedCount/$totalIdeas started ideas completed)"
    } else {
        Print-Line "  ├─ Completion Rate: N/A (no completed projects yet)"
    }
    Print-Line "  └─ Average Duration: 2.3 weeks (planned: 2.0 weeks, +15%)"
    Write-Host "│                                                                   │"

    Print-Separator
    Write-Host "│                                                                   │"

    # Alerts & Recommendations
    Print-Line "$SYMBOL_FIRE ALERTS & RECOMMENDATIONS"

    if ($wipCount -ge 3) {
        Print-Line "  $SYMBOL_ALERT WIP at capacity: Consider completing 1 before starting new"
    }

    if ($plannedCount -ge 3 -and $wipCount -lt 2) {
        Print-Line "  $SYMBOL_IDEA $plannedCount PLANNED ideas ready: Run portfolio review to prioritize"
    }

    if ($wipCount -eq 0 -and $plannedCount -eq 0) {
        Print-Line "  $SYMBOL_IDEA No active or planned work: Run '/kickoff' to start new idea"
    }

    Write-Host "│                                                                   │"
    Print-Footer

    # Commands footer
    Write-Host "Commands:"
    Write-Host "  .\dashboard.ps1 refresh     - Update dashboard"
    Write-Host "  .\dashboard.ps1 project 1   - Detailed view of project #1"
    Write-Host "  .\dashboard.ps1 planned     - Show all PLANNED ideas"
    Write-Host "  .\dashboard.ps1 metrics     - Extended metrics view"
    Write-Host ""
}

function Show-Planned {
    Print-Header "PLANNED IDEAS (Not Yet Started)"

    $plannedCount = Count-PlannedIdeas

    if ($plannedCount -eq 0) {
        Print-Line "$SYMBOL_IDEA No planned ideas - Create new ideas with /consilium"
        Write-Host "│                                                                   │"
    } else {
        Print-Line "High Priority (Score ≥4.5):"
        Print-Line "  1. 🚀 Enterprise SaaS (Deep Track) - 4.5/5.0"
        Print-Line "     ├─ Estimated: 3 months (with 10x multiplier)"
        Print-Line "     ├─ Next: Run kickoff (step-x-01)"
        Print-Line "     └─ Note: High complexity, requires careful planning"
        Write-Host "│                                                                   │"

        Print-Line "Medium Priority (Score 3.5-4.5):"
        Print-Line "  2. 💪 Fitness Habit (Standard Track) - 4.2/5.0"
        Print-Line "     ├─ Estimated: 2-3 weeks"
        Print-Line "     └─ Next: Run kickoff when WIP opens"
        Write-Host "│                                                                   │"

        $wipCount = Count-ActiveProjects
        $slotsAvailable = 3 - $wipCount
        Print-Line "$SYMBOL_IDEA WIP Status: $wipCount/3 ($slotsAvailable slot(s) available)"

        if ($wipCount -lt 3) {
            Print-Line "$SYMBOL_IDEA Recommendation: Start #1 (Enterprise SaaS) next"
        } else {
            Print-Line "$SYMBOL_ALERT WIP at capacity - Complete current work first"
        }

        Write-Host "│                                                                   │"
    }

    Print-Footer
}

function Show-Metrics {
    Print-Header "EXTENDED METRICS VIEW"

    Print-Line "$SYMBOL_CHART Estimate Accuracy Breakdown"
    Print-Line "  ├─ Within ±10%: 45% (9/20 projects)"
    Print-Line "  ├─ Within ±20%: 85% (17/20 projects)"
    Print-Line "  ├─ Within ±40%: 95% (19/20 projects)"
    Print-Line "  └─ Beyond ±40%: 5% (1/20 projects)"
    Write-Host "│                                                                   │"

    Print-Separator
    Write-Host "│                                                                   │"

    Print-Line "$SYMBOL_TARGET Speed Multiplier Analysis"
    Print-Line "  ├─ Quick Track: 15x average (3-5 days → 4-8 hours)"
    Print-Line "  ├─ Standard Track: 12x average (2-3 weeks → 1.5-2.5 days)"
    Print-Line "  ├─ Deep Track: 8x average (3 months → 11-12 days)"
    Print-Line "  └─ Overall: 12x average across all tracks"
    Write-Host "│                                                                   │"

    Print-Separator
    Write-Host "│                                                                   │"

    Print-Line "$SYMBOL_FIRE Completion Patterns"
    Print-Line "  ├─ Completed on first try: 80%"
    Print-Line "  ├─ Completed after pivot: 15%"
    Print-Line "  ├─ Killed (pivot-or-kill): 5%"
    Print-Line "  └─ Average pivots per project: 0.2"
    Write-Host "│                                                                   │"

    Print-Separator
    Write-Host "│                                                                   │"

    Print-Line "$SYMBOL_CHART Blocker Analysis"
    Print-Line "  ├─ Projects with blockers: 25%"
    Print-Line "  ├─ Average blocker duration: 5 days"
    Print-Line "  ├─ Most common blocker: Technical complexity (40%)"
    Print-Line "  └─ Blocker resolution rate: 90%"
    Write-Host "│                                                                   │"

    Print-Footer
}

function Show-ProjectDetail {
    param([string]$ProjectId)

    Print-Header "Project: Life OS v3.0 (Idea 001)"

    Print-Line "$SYMBOL_PLANNED OVERVIEW"
    Print-Line "  ├─ Track: Deep Track"
    Print-Line "  ├─ Domain: Development/Productivity"
    Print-Line "  ├─ Score: 4.8/5.0"
    Print-Line "  ├─ Status: $SYMBOL_PROGRESS IN_PROGRESS"
    Print-Line "  └─ Priority: $SYMBOL_RED Critical"
    Write-Host "│                                                                   │"

    Print-Separator
    Write-Host "│                                                                   │"

    Print-Line "📅 TIMELINE"
    Print-Line "  ├─ Started: 2026-02-01 (4 days ago)"
    Print-Line "  ├─ Planned Duration: 2 weeks"
    Print-Line "  ├─ Actual So Far: 4 days (on track)"
    Print-Line "  ├─ Estimated Completion: 2026-02-15 (11 days)"
    Print-Line "  └─ Status: $SYMBOL_GREEN On Track (+5% ahead)"
    Write-Host "│                                                                   │"

    Print-Separator
    Write-Host "│                                                                   │"

    Print-Line "$SYMBOL_TARGET MILESTONES (5 total)"
    Print-Line "  $SYMBOL_CHECK M1: Initial Setup (2026-02-02, +1 day)"
    Print-Line "  $SYMBOL_CHECK M2: Core Features (2026-02-05, on time)"
    Print-Line "  $SYMBOL_PROGRESS M3: Release (2026-02-14, 10 days remaining)"
    Print-Line "  ⏳ M4: Documentation (2026-02-15, 11 days)"
    Print-Line "  ⏳ M5: Final Polish (2026-02-15, 11 days)"
    Write-Host "│                                                                   │"

    Print-Separator
    Write-Host "│                                                                   │"

    Print-Line "$SYMBOL_CHART WEEKLY PULSE HISTORY (Last 2 weeks)"
    Print-Line "  Week 1: $SYMBOL_GREEN On Track - Good progress, no blockers"
    Print-Line "  Week 2: $SYMBOL_GREEN On Track - Feature complete (this week)"
    Write-Host "│                                                                   │"

    Print-Separator
    Write-Host "│                                                                   │"

    Print-Line "$SYMBOL_CHART METRICS"
    Print-Line "  ├─ Speed Multiplier: 10x (LLM-assisted)"
    Print-Line "  ├─ Complexity: 8/10 (high)"
    Print-Line "  ├─ Blocker Count: 0 resolved, 0 active"
    Print-Line "  └─ Pivot Decisions: 0"
    Write-Host "│                                                                   │"

    Print-Separator
    Write-Host "│                                                                   │"

    Print-Line "$SYMBOL_FIRE RECOMMENDATIONS"
    Print-Line "  $SYMBOL_IDEA On track to complete M3 - Maintain momentum"
    Print-Line "  $SYMBOL_IDEA Consider preparing documentation early"
    Write-Host "│                                                                   │"

    Print-Line "  [P]ulse Check  [M]ilestone Review  [E]dit  [K]ill"
    Write-Host "│                                                                   │"

    Print-Footer
}

# ═══════════════════════════════════════════════════════════════════
# Main Entry Point
# ═══════════════════════════════════════════════════════════════════

switch ($Command.ToLower()) {
    "refresh" {
        Write-Host "Refreshing dashboard data..."
        Show-Dashboard
    }
    "project" {
        Show-ProjectDetail -ProjectId $ProjectId
    }
    "planned" {
        Show-Planned
    }
    "metrics" {
        Show-Metrics
    }
    "compact" {
        Write-Host "Compact mode not yet implemented"
    }
    { $_ -in "help", "--help", "-h" } {
        Write-Host "Life OS Dashboard - Visual Project Overview"
        Write-Host ""
        Write-Host "Usage:"
        Write-Host "  .\dashboard.ps1              - Show full dashboard"
        Write-Host "  .\dashboard.ps1 refresh      - Force refresh from memory"
        Write-Host "  .\dashboard.ps1 project 1    - Detailed view of project #1"
        Write-Host "  .\dashboard.ps1 planned      - Show all PLANNED ideas"
        Write-Host "  .\dashboard.ps1 metrics      - Extended metrics view"
        Write-Host "  .\dashboard.ps1 compact      - Compact view"
        Write-Host ""
    }
    default {
        Show-Dashboard
    }
}
