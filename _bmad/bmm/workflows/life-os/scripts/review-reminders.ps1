<#
.SYNOPSIS
    Automated reminder system for PDCA reviews across 4 cadences.

.DESCRIPTION
    Checks and prompts for due PDCA reviews:
    - Daily (EOD - 18:00): 5-min standup prompt
    - Weekly (Sunday): 30-min velocity review prompt
    - Monthly (Last Sunday): 1-hour trajectory analysis prompt
    - Quarterly (End of quarter): 2-hour strategic replanning prompt

.PARAMETER Check
    Check only, don't prompt.

.PARAMETER Force
    Force prompt for specific cadence (daily/weekly/monthly/quarterly).

.EXAMPLE
    .\review-reminders.ps1
    Check and prompt for due reviews.

.EXAMPLE
    .\review-reminders.ps1 -Check
    Check only, don't prompt.

.EXAMPLE
    .\review-reminders.ps1 -Force daily
    Force prompt for daily review.

.NOTES
    Task Scheduler setup (run every hour):
    - Action: Start a program
    - Program: powershell.exe
    - Arguments: -ExecutionPolicy Bypass -File "C:\path\to\review-reminders.ps1"
    - Trigger: Daily at 12:00 AM, repeat every 1 hour for 1 day
#>

[CmdletBinding()]
param(
    [switch]$Check,
    [ValidateSet('daily', 'weekly', 'monthly', 'quarterly')]
    [string]$Force
)

# Configuration
$ScriptDir = Split-Path -Parent $PSCommandPath
$LifeOsRoot = Split-Path -Parent $ScriptDir
$ReviewsDir = Join-Path $LifeOsRoot "data\reviews"
$MemoryCmd = "npx"
$MemoryCmdArgs = @("claude-flow@v3alpha", "memory")

# Review cadences configuration
$DailyTime = [TimeSpan]::Parse("18:00")       # 6:00 PM
$WeeklyDay = [DayOfWeek]::Sunday
$WeeklyTime = [TimeSpan]::Parse("19:00")      # 7:00 PM Sunday
$MonthlyDayOffset = 7                          # Last 7 days of month
$MonthlyTime = [TimeSpan]::Parse("19:00")     # 7:00 PM last Sunday
$QuarterlyDayOffset = 7                        # Last 7 days of quarter

# Functions
function Write-Info {
    param([string]$Message)
    Write-Host "[INFO] $Message" -ForegroundColor Cyan
}

function Write-Success {
    param([string]$Message)
    Write-Host "[SUCCESS] $Message" -ForegroundColor Green
}

function Write-Warning {
    param([string]$Message)
    Write-Host "[WARNING] $Message" -ForegroundColor Yellow
}

function Write-Error {
    param([string]$Message)
    Write-Host "[ERROR] $Message" -ForegroundColor Red
}

function Write-Prompt {
    param([string]$Message)
    Write-Host $Message -ForegroundColor Magenta -BackgroundColor Black
}

function Get-CurrentInfo {
    $script:CurrentDate = Get-Date -Format "yyyy-MM-dd"
    $script:CurrentTime = Get-Date
    $script:CurrentHour = $CurrentTime.Hour
    $script:CurrentDow = $CurrentTime.DayOfWeek
    $script:CurrentDay = $CurrentTime.Day
    $script:CurrentMonth = $CurrentTime.Month
    $script:CurrentYear = $CurrentTime.Year
    $script:DaysInMonth = [DateTime]::DaysInMonth($CurrentYear, $CurrentMonth)
}

function Test-LastReview {
    param([string]$Cadence)

    $reviewFile = switch ($Cadence) {
        "daily" {
            Join-Path $ReviewsDir "daily\$CurrentDate.md"
        }
        "weekly" {
            $weekNum = (Get-Date).ToString("'W'ww")
            Join-Path $ReviewsDir "weekly\$CurrentYear-$weekNum.md"
        }
        "monthly" {
            Join-Path $ReviewsDir "monthly\$CurrentYear-$('{0:D2}' -f $CurrentMonth).md"
        }
        "quarterly" {
            $quarter = [Math]::Floor(($CurrentMonth - 1) / 3) + 1
            Join-Path $ReviewsDir "quarterly\Q$quarter-$CurrentYear.md"
        }
    }

    return (Test-Path $reviewFile)
}

function Add-ReminderToMemory {
    param([string]$Cadence)

    Write-Info "Logging reminder to memory: $Cadence"

    $timestamp = Get-Date -Format "o"

    try {
        # Store in memory (silent, don't show output unless error)
        $key = "reminder:${Cadence}:${CurrentDate}"
        $content = "Reminder delivered at $timestamp"
        $null = & $MemoryCmd $MemoryCmdArgs store `
            --namespace "life-os:reviews" `
            --key $key `
            --content $content `
            2>&1
    }
    catch {
        Write-Warning "Failed to log to memory (non-critical)"
    }
}

function Test-DailyReviewTime {
    if ($CurrentTime.TimeOfDay -lt $DailyTime) {
        return $false  # Not time yet
    }

    if ($CurrentHour -gt 22) {
        return $false  # Too late (after 10 PM)
    }

    if (Test-LastReview "daily") {
        Write-Info "Daily review already completed for $CurrentDate"
        return $false
    }

    return $true  # Time for daily review
}

function Test-WeeklyReviewTime {
    if ($CurrentDow -ne $WeeklyDay) {
        return $false  # Not Sunday
    }

    if ($CurrentTime.TimeOfDay -lt $WeeklyTime) {
        return $false  # Not time yet
    }

    if (Test-LastReview "weekly") {
        Write-Info "Weekly review already completed for this week"
        return $false
    }

    return $true  # Time for weekly review
}

function Test-MonthlyReviewTime {
    # Check if we're in last 7 days of month
    $daysRemaining = $DaysInMonth - $CurrentDay
    if ($daysRemaining -gt $MonthlyDayOffset) {
        return $false  # Not last week of month
    }

    # Check if it's Sunday
    if ($CurrentDow -ne $WeeklyDay) {
        return $false  # Not Sunday
    }

    if ($CurrentTime.TimeOfDay -lt $MonthlyTime) {
        return $false  # Not time yet
    }

    if (Test-LastReview "monthly") {
        Write-Info "Monthly review already completed for this month"
        return $false
    }

    return $true  # Time for monthly review
}

function Test-QuarterlyReviewTime {
    $quarter = [Math]::Floor(($CurrentMonth - 1) / 3) + 1
    $quarterEndMonth = $quarter * 3

    # Check if we're in the last month of quarter
    if ($CurrentMonth -ne $quarterEndMonth) {
        return $false  # Not last month of quarter
    }

    # Check if we're in last 7 days of month
    $daysRemaining = $DaysInMonth - $CurrentDay
    if ($daysRemaining -gt $QuarterlyDayOffset) {
        return $false  # Not last week of quarter
    }

    if (Test-LastReview "quarterly") {
        Write-Info "Quarterly review already completed for Q$quarter"
        return $false
    }

    return $true  # Time for quarterly review
}

function Show-ReviewPrompt {
    param(
        [string]$Cadence,
        [string]$Duration,
        [string]$Description
    )

    Write-Host ""
    Write-Prompt "========================================"
    Write-Prompt "TIME FOR $($Cadence.ToUpper()) REVIEW!"
    Write-Prompt "========================================"
    Write-Host ""
    Write-Host "Duration: " -NoNewline -ForegroundColor Cyan
    Write-Host $Duration
    Write-Host "Purpose: " -NoNewline -ForegroundColor Cyan
    Write-Host $Description
    Write-Host ""
    Write-Host "Run: " -NoNewline -ForegroundColor Yellow
    Write-Host "step-07-pdca-review.md" -ForegroundColor White -NoNewline
    Write-Host " and select " -ForegroundColor Yellow -NoNewline
    Write-Host $Cadence -ForegroundColor White -NoNewline
    Write-Host " cadence" -ForegroundColor Yellow
    Write-Host ""
    Write-Prompt "========================================"
    Write-Host ""

    # Log reminder delivery
    Add-ReminderToMemory $Cadence
}

# Main logic
function Main {
    # Ensure reviews directories exist
    @("daily", "weekly", "monthly", "quarterly") | ForEach-Object {
        $dir = Join-Path $ReviewsDir $_
        if (-not (Test-Path $dir)) {
            New-Item -ItemType Directory -Path $dir -Force | Out-Null
        }
    }

    # Get current date/time
    Get-CurrentInfo

    $currentTimeStr = Get-Date -Format 'HH:mm'
    Write-Info "PDCA Review Reminder Check - $CurrentDate $currentTimeStr"

    # Force mode
    if ($Force) {
        switch ($Force) {
            'daily' {
                Show-ReviewPrompt 'daily' '5 minutes' 'Quick EOD standup: what done, what blocked, learnings'
            }
            'weekly' {
                Show-ReviewPrompt 'weekly' '30 minutes' 'Progress to weekly goals, velocity analysis, adjust next week'
            }
            'monthly' {
                Show-ReviewPrompt 'monthly' '1 hour' 'Trajectory to quarterly goals, trend analysis, goal adjustments'
            }
            'quarterly' {
                Show-ReviewPrompt 'quarterly' '2 hours' 'Quarter goal achievement, strategic replanning, set next quarter OKRs'
            }
        }
        return
    }

    # Check cadences in priority order (higher priority = more important)
    # Priority: Quarterly > Monthly > Weekly > Daily

    if (Test-QuarterlyReviewTime) {
        if ($Check) {
            Write-Success 'Quarterly review is DUE'
        }
        else {
            Show-ReviewPrompt 'quarterly' '2 hours' 'Quarter goal achievement, strategic replanning, set next quarter OKRs'
        }
        return
    }

    if (Test-MonthlyReviewTime) {
        if ($Check) {
            Write-Success 'Monthly review is DUE'
        }
        else {
            Show-ReviewPrompt 'monthly' '1 hour' 'Trajectory to quarterly goals, trend analysis, goal adjustments'
        }
        return
    }

    if (Test-WeeklyReviewTime) {
        if ($Check) {
            Write-Success 'Weekly review is DUE'
        }
        else {
            Show-ReviewPrompt 'weekly' '30 minutes' 'Progress to weekly goals, velocity analysis, adjust next week'
        }
        return
    }

    if (Test-DailyReviewTime) {
        if ($Check) {
            Write-Success 'Daily review is DUE'
        }
        else {
            Show-ReviewPrompt 'daily' '5 minutes' 'Quick EOD standup: what done, what blocked, learnings'
        }
        return
    }

    # No reviews due
    if ($Check) {
        Write-Info 'No reviews currently due'
    }
}

# Run main
Main
