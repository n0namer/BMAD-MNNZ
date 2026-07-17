# Phase 2: Revalidate Frontmatter after Fixes
# Check: Frontmatter integrity, unused variables, path formats, forbidden patterns

param(
    [string]$WorkflowPath = "D:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad-output\bmb-creations\workflows\idea-to-post-pipeline"
)

$metrics = @{
    filesChecked = 0
    filesWithFrontmatter = 0
    unusedVariables = 0
    pathIssues = 0
    violations = 0
    missingFrontmatter = @()
    invalidFrontmatter = @()
    unusedVars = @()
    pathProblems = @()
    forbiddenPatterns = @()
}

# Get all step files
$stepFiles = Get-ChildItem -Path $WorkflowPath -Filter "step-*.md" -Recurse -File

Write-Host "Scanning $($stepFiles.Count) step files..." -ForegroundColor Cyan

foreach ($file in $stepFiles) {
    $metrics.filesChecked++
    $content = Get-Content -Path $file.FullName -Raw
    
    # CHECK 1: Frontmatter exists
    if ($content -match "^---\n") {
        $metrics.filesWithFrontmatter++
        
        # CHECK 2: Extract frontmatter
        $fmMatch = $content -match "^---\n([\s\S]*?)\n---"
        if ($fmMatch) {
            $frontmatter = $matches[1]
            
            # CHECK 3: Check for unused variables (step-00, step-01, step-yolo files)
            $fileName = $file.Name
            if ($fileName -match "^step-(00|01|yolo)") {
                # These should NOT have unused variables
                if ($frontmatter -match "variableId:|variable_id:|unused") {
                    $metrics.unusedVariables++
                    $metrics.unusedVars += $file.FullName
                }
            }
            
            # CHECK 4: Path format validation
            if ($frontmatter -match "path:\s*[\/]{2,}" -or $frontmatter -match "path:.*\\\\") {
                $metrics.pathIssues++
                $metrics.pathProblems += $file.FullName
            }
        } else {
            $metrics.invalidFrontmatter += $file.FullName
            $metrics.violations++
        }
    } else {
        $metrics.missingFrontmatter += $file.FullName
        $metrics.violations++
    }
    
    # CHECK 5: Forbidden patterns
    $forbiddenPatterns = @(
        "{{.*}}",           # Unresolved template variables
        "\$\{.*\}",         # Unresolved env vars
        "TODO.*FIXME",      # Outstanding tasks
        "REMOVE-ME"         # Leftover markers
    )
    
    foreach ($pattern in $forbiddenPatterns) {
        if ($content -match $pattern) {
            $metrics.forbiddenPatterns += @{
                file = $file.FullName
                pattern = $pattern
            }
            $metrics.violations++
        }
    }
}

# Report
Write-Host "`n========== FRONTMATTER REVALIDATION REPORT ==========" -ForegroundColor Yellow
Write-Host "Phase: Revalidate Frontmatter after Fixes" -ForegroundColor Cyan
Write-Host "Date: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Gray
Write-Host ""
Write-Host "FILES CHECKED: $($metrics.filesChecked)" -ForegroundColor White
Write-Host "Files with valid frontmatter: $($metrics.filesWithFrontmatter)" -ForegroundColor Green
Write-Host "Missing frontmatter: $($metrics.missingFrontmatter.Count)" -ForegroundColor $(if ($metrics.missingFrontmatter.Count -eq 0) { "Green" } else { "Red" })
Write-Host "Invalid frontmatter: $($metrics.invalidFrontmatter.Count)" -ForegroundColor $(if ($metrics.invalidFrontmatter.Count -eq 0) { "Green" } else { "Red" })
Write-Host ""
Write-Host "QUALITY CHECKS:" -ForegroundColor White
Write-Host "Unused variables found: $($metrics.unusedVariables)" -ForegroundColor $(if ($metrics.unusedVariables -eq 0) { "Green" } else { "Yellow" })
Write-Host "Path format issues: $($metrics.pathIssues)" -ForegroundColor $(if ($metrics.pathIssues -eq 0) { "Green" } else { "Red" })
Write-Host "Forbidden patterns detected: $($metrics.forbiddenPatterns.Count)" -ForegroundColor $(if ($metrics.forbiddenPatterns.Count -eq 0) { "Green" } else { "Red" })
Write-Host ""
Write-Host "TOTAL VIOLATIONS: $($metrics.violations)" -ForegroundColor $(if ($metrics.violations -eq 0) { "Green" } else { "Red" })
Write-Host ""

$status = if ($metrics.violations -eq 0) { "PASS" } else { "FAIL" }
Write-Host "FINAL STATUS: $status" -ForegroundColor $(if ($status -eq "PASS") { "Green" } else { "Red" })

# Details if issues found
if ($metrics.missingFrontmatter.Count -gt 0) {
    Write-Host "`nFiles missing frontmatter:" -ForegroundColor Yellow
    $metrics.missingFrontmatter | ForEach-Object { Write-Host "  - $_" -ForegroundColor Gray }
}

if ($metrics.unusedVars.Count -gt 0) {
    Write-Host "`nFiles with unused variables:" -ForegroundColor Yellow
    $metrics.unusedVars | ForEach-Object { Write-Host "  - $_" -ForegroundColor Gray }
}

if ($metrics.pathProblems.Count -gt 0) {
    Write-Host "`nFiles with path format issues:" -ForegroundColor Yellow
    $metrics.pathProblems | ForEach-Object { Write-Host "  - $_" -ForegroundColor Gray }
}

if ($metrics.forbiddenPatterns.Count -gt 0) {
    Write-Host "`nFiles with forbidden patterns:" -ForegroundColor Yellow
    $metrics.forbiddenPatterns | ForEach-Object {
        Write-Host "  - $($_.file)" -ForegroundColor Gray
        Write-Host "    Pattern: $($_.pattern)" -ForegroundColor DarkGray
    }
}

Write-Host "`n" 
Write-Host "{phase: `"frontmatter`", filesChecked: $($metrics.filesChecked), unused: $($metrics.unusedVariables), pathIssues: $($metrics.pathIssues), violations: $($metrics.violations), status: `"$status`"}" -ForegroundColor Cyan

