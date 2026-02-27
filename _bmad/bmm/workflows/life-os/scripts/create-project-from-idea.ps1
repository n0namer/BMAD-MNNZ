# Create project from planned idea (PLANNED → ACTIVE)
# Usage: .\create-project-from-idea.ps1 -IdeaFile "..\ideas-bank\planned\idea-001-finance-katana-vectorbt.md"

param(
    [Parameter(Mandatory=$true)]
    [string]$IdeaFile
)

$IsoDate = Get-Date -Format "yyyy-MM-dd"

# Validate input
if (-not (Test-Path $IdeaFile)) {
    Write-Host "❌ Error: Idea file not found: $IdeaFile" -ForegroundColor Red
    Write-Host "Example: .\create-project-from-idea.ps1 -IdeaFile '..\ideas-bank\planned\idea-001-finance-katana.md'" -ForegroundColor Yellow
    exit 1
}

# Extract filename and parse components
$Filename = [System.IO.Path]::GetFileNameWithoutExtension($IdeaFile)

# Parse: idea-XXX-sphere-name
if ($Filename -match '^idea-(\d+)-([^-]+)-(.+)$') {
    $IdeaId = $Matches[1]
    $Sphere = $Matches[2]
    $IdeaName = $Matches[3]
} else {
    Write-Host "❌ Error: Invalid filename format. Expected: idea-XXX-sphere-name.md" -ForegroundColor Red
    Write-Host "Got: $Filename" -ForegroundColor Yellow
    exit 1
}

$ProjectId = "project-$IdeaId"
$ProjectName = $IdeaName
$ProjectFolder = "..\projects-bank\active\$ProjectId-$ProjectName"

Write-Host "🚀 Creating project from idea..." -ForegroundColor Cyan
Write-Host "   Idea: idea-$IdeaId ($Sphere)" -ForegroundColor Gray
Write-Host "   Name: $IdeaName" -ForegroundColor Gray
Write-Host "   Project: $ProjectId-$ProjectName" -ForegroundColor Gray
Write-Host ""

# Create project directory structure
Write-Host "📁 Creating project structure..." -ForegroundColor Cyan
try {
    New-Item -ItemType Directory -Force -Path "$ProjectFolder\tasks" | Out-Null
    New-Item -ItemType Directory -Force -Path "$ProjectFolder\artifacts" | Out-Null
    New-Item -ItemType Directory -Force -Path "$ProjectFolder\logs" | Out-Null
} catch {
    Write-Host "❌ Failed to create project folders: $_" -ForegroundColor Red
    exit 1
}

# Extract track from idea frontmatter (if present)
$IdeaContent = Get-Content $IdeaFile -Raw
$Track = "untracked"

if ($IdeaContent -match '(?m)^track:\s*(.+)$') {
    $Track = $Matches[1].Trim()
}

# Extract plan section from idea (everything after "## Plan" or "## Implementation Plan")
Write-Host "📋 Extracting plan from idea..." -ForegroundColor Cyan
$PlanContent = ""

if ($IdeaContent -match '(?s)^## (Implementation )?Plan(.*)') {
    $PlanContent = "## " + $Matches[1] + "Plan" + $Matches[2]
} else {
    $PlanContent = @"
# Implementation Plan

No detailed plan found in original idea.
Please create implementation steps here.
"@
}

# Create plan.md
$PlanContent | Out-File -FilePath "$ProjectFolder\plan.md" -Encoding UTF8
Write-Host "✅ Created plan.md" -ForegroundColor Green

# Create project.md with metadata
Write-Host "📝 Creating project metadata..." -ForegroundColor Cyan
$ProjectMetadata = @"
---
id: $ProjectId
name: $ProjectName
status: active
origin-idea: idea-$IdeaId
sphere: $Sphere
track: $Track
started: $IsoDate
---

# Project: $ProjectName

## Origin
- **Idea ID**: idea-$IdeaId
- **Sphere**: $Sphere
- **Activated**: $IsoDate

## Status
- **Current**: ACTIVE
- **Track**: $Track

## Structure
- ``plan.md`` - Implementation plan
- ``tasks/`` - Task tracking files
- ``artifacts/`` - Project outputs and deliverables
- ``logs/`` - Execution logs and notes

## Next Steps
1. Review plan.md
2. Break down into tasks (create task files in tasks/)
3. Begin execution

---

*Project activated from idea-$IdeaId on $IsoDate*
"@

$ProjectMetadata | Out-File -FilePath "$ProjectFolder\project.md" -Encoding UTF8
Write-Host "✅ Created project.md" -ForegroundColor Green

# Archive original idea to activated folder
$ArchiveFolder = "..\ideas-bank\archive\activated"
New-Item -ItemType Directory -Force -Path $ArchiveFolder | Out-Null

$ArchivedIdeaFile = "$ArchiveFolder\idea-$IdeaId-activated-$IsoDate.md"

Write-Host "📦 Archiving original idea..." -ForegroundColor Cyan

# Update frontmatter
$UpdatedContent = ""

if ($IdeaContent -match '(?s)^---\r?\n(.+?)\r?\n---\r?\n(.*)$') {
    # Has frontmatter - update it
    $Frontmatter = $Matches[1]
    $Body = $Matches[2]

    # Update status
    $UpdatedFrontmatter = $Frontmatter -replace '(?m)^status:.*$', "status: activated"

    # Add activated_date if not present
    if ($UpdatedFrontmatter -notmatch '(?m)^activated_date:') {
        $UpdatedFrontmatter += "`nactivated_date: $IsoDate"
    }

    # Add became_project if not present
    if ($UpdatedFrontmatter -notmatch '(?m)^became_project:') {
        $UpdatedFrontmatter += "`nbecame_project: $ProjectId"
    }

    $UpdatedContent = @"
---
$UpdatedFrontmatter
---
$Body
"@
} else {
    # No frontmatter - add it
    $UpdatedContent = @"
---
status: activated
activated_date: $IsoDate
became_project: $ProjectId
sphere: $Sphere
track: $Track
---

$IdeaContent
"@
}

$UpdatedContent | Out-File -FilePath $ArchivedIdeaFile -Encoding UTF8
Write-Host "✅ Archived to: $ArchivedIdeaFile" -ForegroundColor Green

# Remove original idea from planned folder
Remove-Item $IdeaFile -Force
Write-Host "✅ Removed original idea from planned folder" -ForegroundColor Green

# Save to Claude Flow memory
try {
    Write-Host ""
    Write-Host "💾 Saving to global memory..." -ForegroundColor Cyan

    $MemoryContent = @{
        id = $ProjectId
        name = $ProjectName
        status = "active"
        origin_idea = "idea-$IdeaId"
        sphere = $Sphere
        track = $Track
        started = $IsoDate
        project_path = $ProjectFolder
        archived_idea = $ArchivedIdeaFile
    } | ConvertTo-Json -Compress

    $null = npx claude-flow@v3alpha memory store `
        --namespace "shared-knowledge" `
        --key "life-os:projects:$ProjectId" `
        --content $MemoryContent 2>$null

    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Saved to global memory: shared-knowledge:life-os:projects:$ProjectId" -ForegroundColor Green
    } else {
        Write-Host "⚠️ Could not save to memory (claude-flow not available)" -ForegroundColor Yellow
    }
} catch {
    Write-Host "⚠️ Skipping memory save (npx not found)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Green
Write-Host "🎉 Project Created Successfully!" -ForegroundColor Green
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Green
Write-Host ""
Write-Host "📁 Project Location: $ProjectFolder" -ForegroundColor Cyan
Write-Host "📋 Files Created:" -ForegroundColor Cyan
Write-Host "   - project.md (metadata)" -ForegroundColor Gray
Write-Host "   - plan.md (implementation plan)" -ForegroundColor Gray
Write-Host "   - tasks/ (for task tracking)" -ForegroundColor Gray
Write-Host "   - artifacts/ (for deliverables)" -ForegroundColor Gray
Write-Host "   - logs/ (for execution logs)" -ForegroundColor Gray
Write-Host ""
Write-Host "📦 Original Idea:" -ForegroundColor Cyan
Write-Host "   - Archived to: $ArchivedIdeaFile" -ForegroundColor Gray
Write-Host "   - Status updated: activated" -ForegroundColor Gray
Write-Host "   - Linked to: $ProjectId" -ForegroundColor Gray
Write-Host ""
Write-Host "🚀 Next Steps:" -ForegroundColor Cyan
Write-Host "   1. cd $ProjectFolder" -ForegroundColor Yellow
Write-Host "   2. Review plan.md" -ForegroundColor Yellow
Write-Host "   3. Create task files in tasks/" -ForegroundColor Yellow
Write-Host "   4. Begin execution!" -ForegroundColor Yellow
Write-Host ""
