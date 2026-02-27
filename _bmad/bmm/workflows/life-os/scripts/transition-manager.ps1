# ═══════════════════════════════════════════════════════════════════
# Life OS Transition Manager - Automated File Lifecycle
# ═══════════════════════════════════════════════════════════════════
# Called by Claude Flow hooks system to move files between stages
#
# Usage: .\transition-manager.ps1 -Action <action> -IdeaId <id> -StepName <step>
# ═══════════════════════════════════════════════════════════════════

param(
    [Parameter(Mandatory=$true)]
    [ValidateSet(
        "transition-inbox-evaluated",
        "transition-evaluated-planned",
        "transition-planned-active"
    )]
    [string]$Action,

    [Parameter(Mandatory=$true)]
    [string]$IdeaId,

    [Parameter(Mandatory=$true)]
    [string]$StepName,

    [Parameter(Mandatory=$false)]
    [switch]$DryRun = $false
)

# ═══════════════════════════════════════════════════════════════════
# Configuration
# ═══════════════════════════════════════════════════════════════════

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$LifeOsRoot = Split-Path -Parent $ScriptDir
$OutputDir = Join-Path $LifeOsRoot "output"

$Folders = @{
    inbox = Join-Path $OutputDir "inbox"
    evaluated = Join-Path $OutputDir "evaluated"
    planned = Join-Path $OutputDir "planned"
    active = Join-Path $OutputDir "active"
}

# ═══════════════════════════════════════════════════════════════════
# Helper Functions
# ═══════════════════════════════════════════════════════════════════

function Check-Capacity {
    param([string]$Folder)

    $ActiveProjects = Get-ChildItem -Path $Folder -Filter "*.yaml" -ErrorAction SilentlyContinue
    return $ActiveProjects.Count
}

function Move-IdeaFile {
    param(
        [string]$SourceFolder,
        [string]$TargetFolder,
        [string]$IdeaId
    )

    $SourceFile = Join-Path $SourceFolder "idea-$IdeaId.yaml"
    $TargetFile = Join-Path $TargetFolder "idea-$IdeaId.yaml"

    # Validation
    if (-not (Test-Path $SourceFile)) {
        Write-Host "❌ ERROR: Source file not found: $SourceFile" -ForegroundColor Red
        return $false
    }

    if (-not (Test-Path $TargetFolder)) {
        Write-Host "⚠️ Creating target folder: $TargetFolder" -ForegroundColor Yellow
        New-Item -ItemType Directory -Path $TargetFolder -Force | Out-Null
    }

    if (Test-Path $TargetFile) {
        Write-Host "⚠️ WARNING: Target file already exists: $TargetFile" -ForegroundColor Yellow
        Write-Host "Skipping move (file already in correct location)" -ForegroundColor Yellow
        return $true
    }

    # Execute move
    if ($DryRun) {
        Write-Host "🔍 DRY RUN: Would move $SourceFile → $TargetFile" -ForegroundColor Cyan
        return $true
    } else {
        try {
            Move-Item -Path $SourceFile -Destination $TargetFile -Force
            Write-Host "✅ Moved: $SourceFile → $TargetFile" -ForegroundColor Green
            return $true
        } catch {
            Write-Host "❌ ERROR: Failed to move file: $_" -ForegroundColor Red
            return $false
        }
    }
}

function Save-TransitionToMemory {
    param(
        [string]$IdeaId,
        [string]$Action,
        [string]$StepName,
        [bool]$Success,
        [string]$SourceFolder,
        [string]$TargetFolder
    )

    $Timestamp = Get-Date -Format "o"
    $MemoryKey = "transitions:idea-$IdeaId:$(Get-Date -Format 'yyyyMMdd-HHmmss')"

    $MemoryContent = @{
        idea_id = $IdeaId
        action = $Action
        step_name = $StepName
        success = $Success
        source = $SourceFolder
        target = $TargetFolder
        timestamp = $Timestamp
        dry_run = $DryRun.IsPresent
    } | ConvertTo-Json -Compress

    try {
        Write-Host "💾 Saving to global memory..." -ForegroundColor Cyan

        $null = npx claude-flow@v3alpha memory store `
            --namespace "life-os-transitions" `
            --key $MemoryKey `
            --value $MemoryContent 2>$null

        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Saved to memory: life-os-transitions:$MemoryKey" -ForegroundColor Green
        } else {
            Write-Host "⚠️ Could not save to memory (non-critical)" -ForegroundColor Yellow
        }
    } catch {
        Write-Host "⚠️ Skipping memory save (npx not found)" -ForegroundColor Yellow
    }
}

# ═══════════════════════════════════════════════════════════════════
# Main Logic
# ═══════════════════════════════════════════════════════════════════

Write-Host ""
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "  Life OS Transition Manager" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "Action:  $Action" -ForegroundColor White
Write-Host "Idea:    $IdeaId" -ForegroundColor White
Write-Host "Step:    $StepName" -ForegroundColor White
Write-Host "Dry Run: $($DryRun.IsPresent)" -ForegroundColor White
Write-Host ""

$Success = $false

switch ($Action) {
    "transition-inbox-evaluated" {
        Write-Host "📊 Transition: inbox → evaluated (L1-S3 complete)" -ForegroundColor Cyan
        $Success = Move-IdeaFile -SourceFolder $Folders.inbox -TargetFolder $Folders.evaluated -IdeaId $IdeaId
        Save-TransitionToMemory -IdeaId $IdeaId -Action $Action -StepName $StepName -Success $Success `
            -SourceFolder "inbox" -TargetFolder "evaluated"
    }

    "transition-evaluated-planned" {
        Write-Host "📋 Transition: evaluated → planned (L2-S1 complete)" -ForegroundColor Cyan
        $Success = Move-IdeaFile -SourceFolder $Folders.evaluated -TargetFolder $Folders.planned -IdeaId $IdeaId
        Save-TransitionToMemory -IdeaId $IdeaId -Action $Action -StepName $StepName -Success $Success `
            -SourceFolder "evaluated" -TargetFolder "planned"
    }

    "transition-planned-active" {
        Write-Host "🚀 Transition: planned → active (L2-S3 GO decision)" -ForegroundColor Cyan

        # Check capacity
        $ActiveCount = Check-Capacity -Folder $Folders.active
        Write-Host "Current active projects: $ActiveCount / 5" -ForegroundColor White

        if ($ActiveCount -ge 5) {
            Write-Host "❌ CAPACITY FULL: Cannot activate (5/5 projects active)" -ForegroundColor Red
            Write-Host "Please complete or archive an active project first" -ForegroundColor Yellow
            $Success = $false
            Save-TransitionToMemory -IdeaId $IdeaId -Action "capacity-check-failed" -StepName $StepName -Success $false `
                -SourceFolder "planned" -TargetFolder "active"
        } else {
            $Success = Move-IdeaFile -SourceFolder $Folders.planned -TargetFolder $Folders.active -IdeaId $IdeaId
            Save-TransitionToMemory -IdeaId $IdeaId -Action $Action -StepName $StepName -Success $Success `
                -SourceFolder "planned" -TargetFolder "active"

            if ($Success) {
                Write-Host "🎉 Idea activated! ($($ActiveCount + 1)/5 projects now active)" -ForegroundColor Green
            }
        }
    }
}

Write-Host ""
if ($Success) {
    Write-Host "✅ Transition complete!" -ForegroundColor Green
    exit 0
} else {
    Write-Host "❌ Transition failed" -ForegroundColor Red
    exit 1
}
