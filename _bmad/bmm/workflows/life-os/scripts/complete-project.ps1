# Complete a project (move ACTIVE → COMPLETED)
# Usage: .\complete-project.ps1 -ProjectPath "..\projects-bank\active\project-001-katana"

param(
    [Parameter(Mandatory=$true)]
    [string]$ProjectPath
)

# Check if project exists
if (-not (Test-Path $ProjectPath)) {
    Write-Host "❌ Error: Project folder not found: $ProjectPath" -ForegroundColor Red
    exit 1
}

# Extract project name from path
$ProjectName = Split-Path $ProjectPath -Leaf

# Extract project ID (assumes format: project-NNN-name)
if ($ProjectName -match "project-(\d+)-.+") {
    $ProjectId = $Matches[1]
} else {
    Write-Host "❌ Error: Invalid project name format. Expected: project-NNN-name" -ForegroundColor Red
    exit 1
}

# Check if retrospective exists (REQUIRED)
$RetrospectiveFile = Join-Path $ProjectPath "logs\retrospective.md"
if (-not (Test-Path $RetrospectiveFile)) {
    Write-Host "❌ Error: Retrospective not found: $RetrospectiveFile" -ForegroundColor Red
    Write-Host "❌ Cannot complete project without retrospective." -ForegroundColor Red
    Write-Host ""
    Write-Host "Create retrospective first:"
    Write-Host "  1. Create file: $RetrospectiveFile"
    Write-Host "  2. Answer: What worked? What didn't? What would you do differently?"
    Write-Host "  3. Run this script again"
    exit 1
}

# Check if project.md exists
$ProjectFile = Join-Path $ProjectPath "project.md"
if (-not (Test-Path $ProjectFile)) {
    Write-Host "❌ Error: project.md not found: $ProjectFile" -ForegroundColor Red
    exit 1
}

# Get current date
$CompletedDate = Get-Date -Format "yyyy-MM-dd"
$CompletedIso = Get-Date -Format "o"

Write-Host "📦 Completing project: $ProjectName" -ForegroundColor Cyan
Write-Host "📁 Source: $ProjectPath" -ForegroundColor Cyan
Write-Host ""

# Determine destination path
$ActiveBase = Split-Path $ProjectPath -Parent
$ParentDir = Split-Path $ActiveBase -Parent
$CompletedPath = Join-Path $ParentDir "completed\$ProjectName"

# Check if already exists in completed
if (Test-Path $CompletedPath) {
    Write-Host "⚠️ Warning: Project already exists in completed folder" -ForegroundColor Yellow
    Write-Host "❌ Path: $CompletedPath" -ForegroundColor Red
    exit 1
}

# Create completed directory if needed
$CompletedDir = Join-Path $ParentDir "completed"
New-Item -ItemType Directory -Force -Path $CompletedDir | Out-Null

Write-Host "🔄 Updating project.md frontmatter..." -ForegroundColor Cyan

# Update frontmatter (status, completed date)
$Content = Get-Content $ProjectFile -Raw

# Update YAML frontmatter fields
$Content = $Content -replace "(?m)^status: .*", "status: completed"
$Content = $Content -replace "(?m)^completed: .*", "completed: $CompletedDate"
$Content = $Content -replace "(?m)^progress: .*", "progress: 100"

# Write back to file
$Content | Out-File -FilePath $ProjectFile -Encoding UTF8 -NoNewline

Write-Host "✅ Updated frontmatter:" -ForegroundColor Green
Write-Host "   - status: completed"
Write-Host "   - completed: $CompletedDate"
Write-Host "   - progress: 100"
Write-Host ""

Write-Host "📦 Moving project to completed folder..." -ForegroundColor Cyan

# Move project folder
Move-Item -Path $ProjectPath -Destination $CompletedPath

if ($?) {
    Write-Host "✅ Project moved successfully!" -ForegroundColor Green
    Write-Host "📁 New location: $CompletedPath" -ForegroundColor Green
} else {
    Write-Host "❌ Error: Failed to move project" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "💾 Saving to global memory..." -ForegroundColor Cyan

# Create JSON content for memory
$MemoryContent = @{
    project_id = $ProjectId
    project_name = $ProjectName
    status = "completed"
    completed_date = $CompletedDate
    completed_iso = $CompletedIso
    project_path = $CompletedPath
    retrospective_exists = $true
} | ConvertTo-Json -Compress

# Store in life-os namespace
try {
    $null = npx claude-flow@v3alpha memory store `
        --namespace "life-os" `
        --key "completed:project-$ProjectId" `
        --content $MemoryContent 2>$null

    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Saved to global memory: life-os:completed:project-$ProjectId" -ForegroundColor Green
    } else {
        Write-Host "⚠️ Could not save to memory (claude-flow not available)" -ForegroundColor Yellow
    }
} catch {
    Write-Host "⚠️ Skipping memory save (npx not found)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "🎉 PROJECT COMPLETED!" -ForegroundColor Green
Write-Host ""
Write-Host "📊 Summary:"
Write-Host "   Project: $ProjectName"
Write-Host "   Completed: $CompletedDate"
Write-Host "   Location: $CompletedPath"
Write-Host ""
Write-Host "📋 Next Steps:"
Write-Host "   1. Review retrospective for learnings"
Write-Host "   2. Extract patterns for future projects"
Write-Host "   3. Update portfolio dashboard"
Write-Host ""
