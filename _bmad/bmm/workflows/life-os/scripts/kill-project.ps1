# Kill a project (move ACTIVE → KILLED)
# Usage: .\kill-project.ps1 -ProjectPath "..\projects-bank\active\project-001-katana" -KillReason "Market pivot - no longer viable"

param(
    [Parameter(Mandatory=$true)]
    [string]$ProjectPath,

    [Parameter(Mandatory=$true)]
    [string]$KillReason
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

# Check if project.md exists
$ProjectFile = Join-Path $ProjectPath "project.md"
if (-not (Test-Path $ProjectFile)) {
    Write-Host "❌ Error: project.md not found: $ProjectFile" -ForegroundColor Red
    exit 1
}

# Get current date
$KilledDate = Get-Date -Format "yyyy-MM-dd"
$KilledIso = Get-Date -Format "o"

Write-Host "⚠️ KILLING PROJECT: $ProjectName" -ForegroundColor Yellow
Write-Host "📁 Source: $ProjectPath" -ForegroundColor Yellow
Write-Host "💀 Reason: $KillReason" -ForegroundColor Yellow
Write-Host ""

# Determine destination path
$ActiveBase = Split-Path $ProjectPath -Parent
$ParentDir = Split-Path $ActiveBase -Parent
$KilledPath = Join-Path $ParentDir "killed\$ProjectName"

# Check if already exists in killed
if (Test-Path $KilledPath) {
    Write-Host "⚠️ Warning: Project already exists in killed folder" -ForegroundColor Yellow
    Write-Host "❌ Path: $KilledPath" -ForegroundColor Red
    exit 1
}

# Create killed directory if needed
$KilledDir = Join-Path $ParentDir "killed"
New-Item -ItemType Directory -Force -Path $KilledDir | Out-Null

# Create logs directory if it doesn't exist
$LogsDir = Join-Path $ProjectPath "logs"
New-Item -ItemType Directory -Force -Path $LogsDir | Out-Null

Write-Host "📝 Creating kill-analysis.md..." -ForegroundColor Cyan

# Create kill analysis document
$KillAnalysisFile = Join-Path $LogsDir "kill-analysis.md"

$KillAnalysisContent = @"
# Project Kill Analysis

**Project**: $ProjectName
**Killed**: $KilledDate
**Decision By**: [Your Name]

---

## Kill Decision

### Primary Reason
$KillReason

### Contributing Factors
- [Factor 1]
- [Factor 2]
- [Factor 3]

### Timeline of Concerns
- **[Date]**: [First warning sign]
- **[Date]**: [Escalating issue]
- **[Date]**: [Final decision point]

---

## What We Learned

### What Went Wrong
1. **[Issue Area 1]**
   - What happened: ___
   - Root cause: ___
   - Warning signs: ___

2. **[Issue Area 2]**
   - What happened: ___
   - Root cause: ___
   - Warning signs: ___

3. **[Issue Area 3]**
   - What happened: ___
   - Root cause: ___
   - Warning signs: ___

### What We Could Have Done Differently
- [ ] Earlier validation of [assumption]
- [ ] More focus on [area]
- [ ] Different approach to [strategy]
- [ ] Better resource allocation
- [ ] More frequent checkpoints

### Early Warning Signals We Missed
1. ___
2. ___
3. ___

---

## Salvageable Outputs

### What We Preserved
- [ ] Code/artifacts in: artifacts/
- [ ] Documentation in: [location]
- [ ] Learnings captured in: [location]
- [ ] Data/research in: [location]

### Potential Reuse
- **Component X**: Could be used for [future project]
- **Learning Y**: Applicable to [similar situation]
- **Asset Z**: Reusable in [context]

---

## Decision Analysis

### Would We Do This Again?
**[ ] Yes, with changes** | **[ ] No, not viable** | **[ ] Maybe, under different conditions**

**Reasoning**: ___

### Under What Conditions Would This Work?
- Condition 1: ___
- Condition 2: ___
- Condition 3: ___

### Related Ideas Worth Exploring
- [ ] Idea 1: [description]
- [ ] Idea 2: [description]
- [ ] Idea 3: [description]

---

## Future Prevention

### Red Flags to Watch For
1. ___
2. ___
3. ___

### Questions to Ask Next Time
- Before starting: ___
- During execution: ___
- At checkpoints: ___

### Patterns to Avoid
- Pattern 1: ___
- Pattern 2: ___
- Pattern 3: ___

---

## Emotional Reflection

### How Do We Feel About This Decision?
[Honest reflection on the emotional aspect of killing the project]

### What Are We Grateful For?
- Learning 1: ___
- Learning 2: ___
- Learning 3: ___

### How Will This Make Us Better?
[Forward-looking perspective on growth from this experience]

---

**Analysis Completed**: $KilledDate
**Status**: Project killed and archived
**Next Action**: Extract patterns during quarterly review
"@

$KillAnalysisContent | Out-File -FilePath $KillAnalysisFile -Encoding UTF8

Write-Host "✅ Created kill-analysis.md" -ForegroundColor Green
Write-Host ""

Write-Host "🔄 Updating project.md frontmatter..." -ForegroundColor Cyan

# Update frontmatter (status, killed date, reason)
$Content = Get-Content $ProjectFile -Raw

# Update YAML frontmatter fields
$Content = $Content -replace "(?m)^status: .*", "status: killed"
$Content = $Content -replace "(?m)^completed: .*", "killed: $KilledDate"

# Add kill_reason field if not exists
if ($Content -notmatch "(?m)^kill_reason:") {
    $Content = $Content -replace "(?m)(^killed: .*)$", "`$1`nkill_reason: `"$KillReason`""
} else {
    $Content = $Content -replace "(?m)^kill_reason:.*", "kill_reason: `"$KillReason`""
}

# Write back to file
$Content | Out-File -FilePath $ProjectFile -Encoding UTF8 -NoNewline

Write-Host "✅ Updated frontmatter:" -ForegroundColor Green
Write-Host "   - status: killed"
Write-Host "   - killed: $KilledDate"
Write-Host "   - kill_reason: $KillReason"
Write-Host ""

Write-Host "📦 Moving project to killed folder..." -ForegroundColor Cyan

# Move project folder
Move-Item -Path $ProjectPath -Destination $KilledPath

if ($?) {
    Write-Host "✅ Project moved successfully!" -ForegroundColor Green
    Write-Host "📁 New location: $KilledPath" -ForegroundColor Green
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
    status = "killed"
    killed_date = $KilledDate
    killed_iso = $KilledIso
    kill_reason = $KillReason
    project_path = $KilledPath
    kill_analysis_exists = $true
} | ConvertTo-Json -Compress

# Store in life-os namespace
try {
    $null = npx claude-flow@v3alpha memory store `
        --namespace "life-os" `
        --key "killed:project-$ProjectId" `
        --content $MemoryContent 2>$null

    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Saved to global memory: life-os:killed:project-$ProjectId" -ForegroundColor Green
    } else {
        Write-Host "⚠️ Could not save to memory (claude-flow not available)" -ForegroundColor Yellow
    }
} catch {
    Write-Host "⚠️ Skipping memory save (npx not found)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "💀 PROJECT KILLED" -ForegroundColor Yellow
Write-Host ""
Write-Host "📊 Summary:"
Write-Host "   Project: $ProjectName"
Write-Host "   Killed: $KilledDate"
Write-Host "   Reason: $KillReason"
Write-Host "   Location: $KilledPath"
Write-Host ""
Write-Host "📋 Next Steps:"
Write-Host "   1. Review kill-analysis.md and complete all sections"
Write-Host "   2. Extract learnings for future projects"
Write-Host "   3. Update portfolio dashboard"
Write-Host "   4. Consider if salvageable components can be reused"
Write-Host ""
Write-Host "💡 Remember: Killing projects is a sign of good judgment, not failure." -ForegroundColor Cyan
Write-Host ""
