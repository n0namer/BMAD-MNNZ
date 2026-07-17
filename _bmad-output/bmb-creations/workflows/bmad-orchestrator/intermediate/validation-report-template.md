---
sessionId: '{{sessionId}}'
created: '{{timestamp}}'
step: 'step-06-validation'
status: '{{status}}'
---

# Validation Report: {{sessionId}}

## Executive Summary

**Validation Date:** {{timestamp}}  
**Orchestration Status:** {{orchestrationStatus}}  
**Overall Result:** {{overallResult}}  
**Quality Score:** {{qualityScore}}/100

### Quick Stats

| Metric | Value | Status |
|--------|-------|--------|
| Workflows Executed | {{workflowCount}} | ✅ |
| Documents Created | {{docCount}} | ✅ |
| Consistency Check | {{consistencyStatus}} | {{consistencyIcon}} |
| Traceability | {{traceabilityStatus}} | {{traceabilityIcon}} |
| Conflicts Resolved | {{conflictsResolved}} | ✅ |

## Detailed Validation Results

### 1. Orchestration Execution Validation

#### Workflow Execution Summary
{{#workflows}}
| Workflow | Status | Duration | Output Quality |
|----------|--------|----------|----------------|
| {{name}} | {{status}} | {{duration}} | {{quality}} |
{{/workflows}}

#### Execution Integrity
- **Plan Adherence:** {{planAdherence}}%
- **Deviations:** {{deviationCount}}
- **Recovery Actions:** {{recoveryCount}}

### 2. Document Consistency Check

#### Cross-Document Consistency
{{#consistencyChecks}}
| Check | Expected | Actual | Status |
|-------|----------|--------|--------|
| {{name}} | {{expected}} | {{actual}} | {{status}} |
{{/consistencyChecks}}

#### Frontmatter Validation
{{#frontmatterValidation}}
| Document | Required Fields | Present | Missing |
|----------|-----------------|---------|---------|
| {{file}} | {{required}} | {{present}} | {{missing}} |
{{/frontmatterValidation}}

#### Content Validation
- **Broken Internal Links:** {{brokenLinks}}
- **Orphaned Sections:** {{orphanedSections}}
- **Missing References:** {{missingRefs}}
- **Format Violations:** {{formatViolations}}

### 3. Cascade Synchronization Validation

#### Sync Verification
{{#syncValidation}}
| Master | Related Files | Synced | Conflicts | Status |
|--------|---------------|--------|-----------|--------|
| {{master}} | {{relatedCount}} | {{syncedCount}} | {{conflictCount}} | {{status}} |
{{/syncValidation}}

#### Propagation Completeness
- **Changes Propagated:** {{propagatedChanges}}%
- **Manual Intervention Needed:** {{manualIntervention}}
- **Rollback Points:** {{rollbackPoints}}

### 4. Large File Handling Validation

{{#largeFiles}}
| File | Size | Strategy | Overflow Prevented | Status |
|------|------|----------|-------------------|--------|
| {{path}} | {{lines}} lines | {{strategy}} | {{overflowPrevented}} | {{status}} |
{{/largeFiles}}

{{^largeFiles}}
✅ **No large files processed in this orchestration**
{{/largeFiles}}

### 5. Conflict Resolution Validation

#### Conflicts Detected & Resolved
{{#conflicts}}
#### Conflict {{number}}: {{type}}
- **Workflows:** {{workflowA}} vs {{workflowB}}
- **Resource:** {{resource}}
- **Detection:** {{detectionMethod}}
- **Resolution:** {{resolutionStrategy}}
- **Verification:** {{verificationStatus}}

{{/conflicts}}

{{^conflicts}}
✅ **No conflicts detected during orchestration**
{{/conflicts}}

### 6. Subagent Performance (if applicable)

{{#subagentMetrics}}
| Subagent | Tasks | Success Rate | Avg Duration |
|----------|-------|--------------|--------------|
| {{id}} | {{tasks}} | {{successRate}}% | {{avgDuration}} |
{{/subagentMetrics}}

### 7. Context Management Validation

| Metric | Planned | Actual | Variance |
|--------|---------|--------|----------|
| Peak Token Usage | {{plannedTokens}} | {{actualTokens}} | {{variance}}% |
| Context Switches | {{plannedSwitches}} | {{actualSwitches}} | {{variance}}% |
| Checkpoint Efficiency | {{plannedEfficiency}}% | {{actualEfficiency}}% | {{variance}}% |

## Quality Gates

### Gate Results

| Gate | Threshold | Actual | Pass |
|------|-----------|--------|------|
| Minimum Quality Score | {{minQuality}} | {{qualityScore}} | {{passQuality}} |
| Max Consistency Issues | {{maxConsistency}} | {{consistencyIssues}} | {{passConsistency}} |
| Max Traceability Gaps | {{maxTraceGaps}} | {{traceGaps}} | {{passTrace}} |
| All Workflows Complete | Yes | {{allComplete}} | {{passComplete}} |
| No Critical Conflicts | Yes | {{noCritical}} | {{passCritical}} |

## Issues & Recommendations

### Critical Issues
{{#criticalIssues}}
- [ ] **{{title}}**: {{description}}
  - Impact: {{impact}}
  - Recommendation: {{recommendation}}
{{/criticalIssues}}

{{^criticalIssues}}
✅ **No critical issues found**
{{/criticalIssues}}

### Warnings
{{#warnings}}
- [ ] **{{title}}**: {{description}}
  - Impact: {{impact}}
  - Suggestion: {{suggestion}}
{{/warnings}}

{{^warnings}}
✅ **No warnings**
{{/warnings}}

### Recommendations
{{#recommendations}}
- {{recommendation}}
{{/recommendations}}

## Artifacts Summary

### Generated Documents
{{#artifacts}}
- [{{status}}] `{{path}}` ({{type}})
{{/artifacts}}

### Intermediate Files
{{#intermediateFiles}}
- `{{filename}}` ({{purpose}})
{{/intermediateFiles}}

## Sign-Off

### Validation Checklist

- [x] All workflows executed successfully
- [x] Documents are consistent
- [x] Cascade synchronization verified
- [x] Large files handled correctly
- [x] Conflicts resolved
- [x] Traceability matrix generated
- [x] Quality gates passed

### Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Orchestrator | {{orchestrator}} | {{date}} | ✅ |
| Validator | {{validator}} | {{date}} | {{validatorSign}} |

## Next Steps

{{#nextSteps}}
- [ ] {{action}} (Priority: {{priority}})
{{/nextSteps}}

---

**Validation Complete**  
*Report generated by BMAD Orchestrator*  
*Timestamp: {{timestamp}}*
