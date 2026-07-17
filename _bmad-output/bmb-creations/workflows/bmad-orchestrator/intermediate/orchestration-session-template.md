---
sessionId: '{{sessionId}}'
created: '{{timestamp}}'
status: '{{status}}'
currentStep: '{{currentStep}}'
stepsCompleted: []
---

# Orchestration Session: {{sessionId}}

## Session Metadata

| Field | Value |
|-------|-------|
| **Session ID** | {{sessionId}} |
| **Created** | {{timestamp}} |
| **Status** | {{status}} |
| **Current Step** | {{currentStep}} |
| **Last Updated** | {{lastUpdated}} |

## Discovery Phase

### User's Task
{{taskDescription}}

### Source Files Identified
{{#sourceFiles}}
- `{{path}}` ({{lines}} lines, {{type}})
{{/sourceFiles}}

### Target Files
{{#targetFiles}}
- `{{path}}` (purpose: {{purpose}})
{{/targetFiles}}

### Key Requirements
{{#requirements}}
- [{{priority}}] {{description}}
{{/requirements}}

## Workflow Selection Phase

### Selected Workflows
{{#selectedWorkflows}}
- **{{name}}** ({{category}}) — {{reason}}
{{/selectedWorkflows}}

### Workflow Dependencies
```
{{dependencyGraph}}
```

## Orchestration Plan Phase

### Execution Zones
{{#zones}}
- **Zone {{number}}** ({{type}}): {{workflows}}
{{/zones}}

### Conflict Analysis
{{#conflicts}}
- **{{type}}**: {{description}} → {{resolution}}
{{/conflicts}}

### Runtime Environment
- **Selected**: {{runtime}}
- **Parallel Capability**: {{parallelSupport}}

## Execution Progress

### Phase Status
{{#phases}}
| Phase | Status | Started | Completed | Workflows |
|-------|--------|---------|-----------|-----------|
| {{number}} | {{status}} | {{started}} | {{completed}} | {{count}} |
{{/phases}}

### Current Checkpoint
- **Phase**: {{currentPhase}}
- **Workflow**: {{currentWorkflow}}
- **Progress**: {{progress}}%
- **Last Action**: {{lastAction}}

## Cascade Synchronization

### Sync Status
- **Master Documents**: {{masterCount}}
- **Synchronized**: {{syncedCount}}
- **Pending**: {{pendingCount}}
- **Conflicts**: {{conflictCount}}

### Propagated Changes
{{#propagatedChanges}}
- `{{file}}`: {{changeDescription}}
{{/propagatedChanges}}

## Validation Results

### Consistency Check
- **Status**: {{consistencyStatus}}
- **Issues Found**: {{issueCount}}

### Traceability Matrix
- **Generated**: {{matrixGenerated}}
- **Coverage**: {{coverage}}%

## Session Recovery

### To Resume This Session
1. Load `workflow-bmad-orchestrator.md`
2. Select mode: **Continue Existing Session**
3. Session ID: `{{sessionId}}`

### Last Known State
- **Step**: {{currentStep}}
- **Phase**: {{currentPhase}}
- **Checkpoint**: {{checkpointId}}

---

*This session file is auto-generated. Do not edit manually.*
