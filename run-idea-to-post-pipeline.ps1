# Quick launcher for idea-to-post-pipeline workflow
# Usage: .\run-idea-to-post-pipeline.ps1 [create|edit|validate|yolo]

param(
    [string]$Mode = "create",
    [switch]$Help
)

if ($Help) {
    Write-Host "
╔════════════════════════════════════════════════════════════╗
║     idea-to-post-pipeline - Quick Launcher                 ║
╚════════════════════════════════════════════════════════════╝

Usage: .\run-idea-to-post-pipeline.ps1 [mode]

Modes:
  create    [C] Collaborative content creation (default)
  edit      [E] Post improvement & refinement
  validate  [V] Quality assurance & batch validation
  yolo      [Y] Full automation (3-5 minutes for 9 posts)

Examples:
  .\run-idea-to-post-pipeline.ps1
  .\run-idea-to-post-pipeline.ps1 -Mode edit
  .\run-idea-to-post-pipeline.ps1 -Mode yolo
    " -ForegroundColor Green
    exit 0
}

$workflowPath = "_bmad/bmb/workflows/idea-to-post-pipeline"

Write-Host "
╔════════════════════════════════════════════════════════════╗
║     🚀 Starting: idea-to-post-pipeline                     ║
║     Mode: $Mode                                             ║
╚════════════════════════════════════════════════════════════╝
" -ForegroundColor Cyan

# Map mode names to BMAD modes
$modeMap = @{
    "create"   = "CREATE"
    "edit"     = "EDIT"
    "validate" = "VALIDATE"
    "yolo"     = "YOLO"
    "c"        = "CREATE"
    "e"        = "EDIT"
    "v"        = "VALIDATE"
    "y"        = "YOLO"
}

$bmadMode = $modeMap[$Mode.ToLower()]
if (-not $bmadMode) {
    Write-Host "❌ Unknown mode: $Mode" -ForegroundColor Red
    Write-Host "Valid modes: create, edit, validate, yolo" -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Workflow registered at: $workflowPath" -ForegroundColor Green
Write-Host "✅ Mode selected: [$bmadMode]" -ForegroundColor Green
Write-Host ""
Write-Host "Launching BMAD Workflow Creator..." -ForegroundColor Cyan
Write-Host ""

# Note: The workflow is now built-in at _bmad/bmb/workflows/idea-to-post-pipeline/
# To use it, run:
Write-Host "Next step: Use the BMAD Workflow Creator" -ForegroundColor Yellow
Write-Host '  Command: /bmad-bmb-workflow' -ForegroundColor White
Write-Host '  Path: ' + (Resolve-Path $workflowPath).Path -ForegroundColor White
