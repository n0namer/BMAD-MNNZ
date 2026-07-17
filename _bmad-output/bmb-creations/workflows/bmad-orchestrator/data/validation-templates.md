# Validation Templates

## Consistency Check List

### Document Structure Consistency
```yaml
checks:
  - name: "Frontmatter Required Fields"
    fields: ["name", "description", "version"]
    severity: error

  - name: "Section Hierarchy"
    check: "H1 → H2 → H3 order"
    severity: warning

  - name: "Link Validity"
    check: "All internal links resolve"
    severity: error

  - name: "Cross-References"
    check: "Referenced documents exist"
    severity: error
```

### Content Consistency
```yaml
content_checks:
  - name: "Terminology Consistency"
    check: "Same terms used throughout"
    severity: warning

  - name: "Date Formats"
    check: "ISO 8601 format"
    severity: warning

  - name: "Naming Conventions"
    check: "kebab-case for files"
    severity: warning
```

## Traceability Matrix Template

### Basic Matrix
```markdown
| Requirement | Source Doc | Design Doc | Impl Doc | Test Doc | Status |
|-------------|------------|------------|----------|----------|--------|
| REQ-001 | brief.md | prd.md | - | - | 🟡 |
| REQ-002 | prd.md | arch.md | - | - | 🟡 |
| FEAT-001 | prd.md | ux.md | - | - | 🟡 |
```

### Extended Matrix
```markdown
| ID | Requirement | Source | Design | Code | Tests | Coverage |
|----|-------------|--------|--------|------|-------|----------|
| R1 | User auth | brief | arch | auth.ts | auth.test.ts | 100% |
| R2 | Data API | brief | arch | api.ts | api.test.ts | 100% |
```

## Validation Report Structure

### Header
```markdown
---
sessionId: '{{sessionId}}'
validationDate: '{{timestamp}}'
status: '{{status}}'
---

# Validation Report

## Summary
- Total Artifacts: {{count}}
- Issues Found: {{issues}}
- Critical: {{critical}}
- Warnings: {{warnings}}
```

### Document Validation Section
```markdown
## Document Validation

{{#documents}}
### {{filename}}
| Check | Status | Details |
|-------|--------|---------|
| Frontmatter | {{fm_status}} | {{fm_details}} |
| Links | {{link_status}} | {{link_details}} |
| Structure | {{struct_status}} | {{struct_details}} |
{{/documents}}
```

### Cascade Consistency Section
```markdown
## Cascade Consistency

### Document Chain
```
{{source}} → {{intermediate}} → {{target}}
```

| Relationship | Status | Coverage |
|--------------|--------|----------|
| {{source}} → {{intermediate}} | {{status1}} | {{coverage1}}% |
| {{intermediate}} → {{target}} | {{status2}} | {{coverage2}}% |
```

## Quality Gates

### Gate Definitions
```yaml
quality_gates:
  minimum_coverage:
    threshold: 80
    metric: "requirement_coverage_percent"
    action: "fail"

  max_orphaned:
    threshold: 0
    metric: "orphaned_requirements"
    action: "fail"

  max_broken_links:
    threshold: 0
    metric: "broken_internal_links"
    action: "fail"

  documentation_complete:
    threshold: 100
    metric: "documented_requirements_percent"
    action: "warn"
```

### Gate Results Template
```markdown
## Quality Gates

| Gate | Threshold | Actual | Status |
|------|-----------|--------|--------|
| Min Coverage | {{thresh_coverage}}% | {{actual_coverage}}% | {{status_coverage}} |
| Max Orphaned | {{thresh_orphaned}} | {{actual_orphaned}} | {{status_orphaned}} |
| Max Broken Links | {{thresh_broken}} | {{actual_broken}} | {{status_broken}} |
| Doc Complete | {{thresh_doc}}% | {{actual_doc}}% | {{status_doc}} |
```

## Issue Classification

### Critical Issues
```yaml
critical:
  - "Missing required frontmatter"
  - "Broken internal links"
  - "Circular dependencies"
  - "Missing required outputs"
  - "Workflow execution failure"
```

### Warnings
```yaml
warnings:
  - "Optional frontmatter missing"
  - "External link unreachable"
  - "Section ordering unconventional"
  - "Coverage below 90%"
  - "Large file without range read"
```

## Final Plan Document Structure

```markdown
---
sessionId: '{{sessionId}}'
status: 'COMPLETE'
stepsCompleted:
  - step-01-discovery
  - step-02-workflow-selection
  - step-03-orchestration-plan
  - step-04-execution-loop
  - step-05-cascade-sync
  - step-06-validation
---

# BMAD Orchestrator Session: {{sessionId}}

## Final Status: ✅ COMPLETE

### Execution Summary
- Started: {{startTime}}
- Completed: {{endTime}}
- Duration: {{duration}}

### Workflows Executed
{{#workflows}}
- [{{status}}] {{name}} ({{duration}})
{{/workflows}}

### Documents Generated
{{#documents}}
- `{{path}}` ({{type}}, {{lines}} lines)
{{/documents}}

### Intermediate Files
- orchestration-session-{{sessionId}}.md
- workflow-selection.md
- orchestration-plan.md
{{#checkpoints}}
- checkpoint-phase-{{number}}.md
{{/checkpoints}}
- sync-report.md
- traceability-matrix.md
- validation-report.md

### Validation Results
- Quality Score: {{qualityScore}}/100
- All Gates: {{gateStatus}}
- Issues: {{issueCount}}

---
*Orchestration complete. Session saved for reference.*
```

## Validation Checklist

### Pre-Execution Validation
- [ ] All required workflows available
- [ ] Input files exist and readable
- [ ] Output directories writable
- [ ] Context size manageable
- [ ] No obvious conflicts

### During Execution Validation
- [ ] Each phase completes successfully
- [ ] Checkpoint files created
- [ ] Context usage monitored
- [ ] Subagent results valid
- [ ] No data corruption

### Post-Execution Validation
- [ ] All outputs generated
- [ ] Documents consistent
- [ ] Links working
- [ ] Cascade synchronized
- [ ] Traceability complete
- [ ] Quality gates passed

## Export Formats

### CSV Export
```csv
ID,Requirement,Source,Design,Implementation,Tests,Coverage,Status
R1,User login,brief.md,arch.md,auth.ts,auth.test.ts,100%,PASS
R2,API endpoint,brief.md,arch.md,api.ts,api.test.ts,100%,PASS
```

### JSON Export
```json
{
  "sessionId": "{{sessionId}}",
  "validation": {
    "status": "{{status}}",
    "qualityScore": {{score}},
    "artifacts": {{artifacts}}
  }
}
```
