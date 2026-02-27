# Archive an idea to quarterly folder
# Usage: .\archive-idea.ps1 -IdeaId "001" -Status "completed"
# Usage: .\archive-idea.ps1 -IdeaId "006" -Status "killed" -Reason "Market validation failure"

param(
    [Parameter(Mandatory=$true)]
    [string]$IdeaId,

    [Parameter(Mandatory=$true)]
    [ValidateSet("completed", "killed")]
    [string]$Status,

    [Parameter(Mandatory=$false)]
    [string]$Reason = ""
)

# Get current quarter
$Year = Get-Date -Format "yyyy"
$Month = (Get-Date).Month

if ($Month -le 3) {
    $Quarter = "q1"
} elseif ($Month -le 6) {
    $Quarter = "q2"
} elseif ($Month -le 9) {
    $Quarter = "q3"
} else {
    $Quarter = "q4"
}

# Paths
$ArchiveBase = "..\output\archive"
$QuarterFolder = "$Year-$Quarter"
$ArchivePath = "$ArchiveBase\$Status\$QuarterFolder"
$OutputFolder = "..\output"

# Create quarter folder if needed
New-Item -ItemType Directory -Force -Path $ArchivePath | Out-Null

# Find idea files
$RetrospectiveFile = "$OutputFolder\idea-$IdeaId-retrospective.md"
$ExecutionTracker = "$OutputFolder\idea-$IdeaId-execution-tracker.md"
$PivotKillFile = "$OutputFolder\step-x-04-decision-$IdeaId.md"

# Check if retrospective exists
if (-not (Test-Path $RetrospectiveFile)) {
    Write-Host "⚠️ Warning: Retrospective not found: $RetrospectiveFile" -ForegroundColor Yellow
    Write-Host "Archive will be created without full retrospective data." -ForegroundColor Yellow
}

# Create archive entry
$ArchiveFile = "$ArchivePath\idea-$IdeaId-archive.md"

Write-Host "📦 Archiving idea $IdeaId as $Status..." -ForegroundColor Cyan

# Generate archive entry
$StatusBadge = if ($Status -eq "completed") { "✅ COMPLETED" } else { "❌ KILLED" }
$ArchiveDate = Get-Date -Format "yyyy-MM-dd"

$Content = @"
# Idea $IdeaId Archive

**Status:** $StatusBadge
**Archived:** $ArchiveDate
**Quarter:** $QuarterFolder

"@

# Add kill reason if provided
if ($Status -eq "killed" -and $Reason -ne "") {
    $Content += "**Kill Reason:** $Reason`n`n"
}

# Copy retrospective content if exists
if (Test-Path $RetrospectiveFile) {
    $Content += "---`n`n"
    $Content += "## Retrospective`n`n"
    $Content += Get-Content $RetrospectiveFile -Raw
}

# Add execution tracker summary if exists
if (Test-Path $ExecutionTracker) {
    $Content += "`n---`n`n"
    $Content += "## Execution Timeline`n`n"

    $TrackerContent = Get-Content $ExecutionTracker -Raw
    if ($TrackerContent -match "(?s)## Timeline.*") {
        $Content += $Matches[0]
    } else {
        $Content += "*Execution tracker found but no timeline section*`n"
    }
}

# Add pivot-or-kill analysis if exists (for killed ideas)
if ($Status -eq "killed" -and (Test-Path $PivotKillFile)) {
    $Content += "`n---`n`n"
    $Content += "## Pivot-or-Kill Analysis`n`n"
    $Content += Get-Content $PivotKillFile -Raw
}

# Add archive footer
$Content += @"

---

**Archived by:** Archive Script
**Archive Date:** $ArchiveDate
**Archive Location:** $ArchivePath\idea-$IdeaId-archive.md
"@

# Write archive file
$Content | Out-File -FilePath $ArchiveFile -Encoding UTF8

Write-Host "✅ Idea $IdeaId archived successfully!" -ForegroundColor Green
Write-Host "📁 Location: $ArchiveFile" -ForegroundColor Green

# Store in memory (if claude-flow is available)
try {
    $MemoryContent = @{
        idea_id = $IdeaId
        status = $Status
        quarter = $QuarterFolder
        archive_date = $ArchiveDate
        archive_path = $ArchiveFile
        reason = $Reason
    } | ConvertTo-Json -Compress

    Write-Host "💾 Saving to global memory..." -ForegroundColor Cyan

    $null = npx claude-flow@v3alpha memory store `
        --namespace "archive" `
        --key "$Status`:idea-$IdeaId`:$QuarterFolder" `
        --content $MemoryContent 2>$null

    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Saved to global memory: archive:$Status`:idea-$IdeaId`:$QuarterFolder" -ForegroundColor Green
    } else {
        Write-Host "⚠️ Could not save to memory (claude-flow not available)" -ForegroundColor Yellow
    }
} catch {
    Write-Host "⚠️ Skipping memory save (npx not found)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "🎉 Archive complete!" -ForegroundColor Green
Write-Host "Next: Run pattern mining during quarterly review to learn from this idea"
