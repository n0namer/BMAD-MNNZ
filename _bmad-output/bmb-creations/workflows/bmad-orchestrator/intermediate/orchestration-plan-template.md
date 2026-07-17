---
sessionId: '{{sessionId}}'
created: '{{timestamp}}'
step: 'step-03-orchestration-plan'
---

# Orchestration Plan: {{sessionId}}

## Plan Summary

**Date:** {{timestamp}}  
**Total Workflows:** {{totalWorkflows}}  
**Parallel Zones:** {{parallelZones}}  
**Sequential Dependencies:** {{sequentialDeps}}  
**Estimated Phases:** {{estimatedPhases}}

## Dependency Graph

```mermaid
{{mermaidGraph}}
```

### Text Representation
{{#dependencies}}
- {{workflow}} → depends on → {{dependsOn}}
{{/dependencies}}

## Execution Zones

### Parallel Zones (Safe to run concurrently)
{{#parallelZones}}
#### Zone {{number}}: {{name}}
**Workflows:**
{{#workflows}}
- {{name}} (reads: {{reads}}, writes: {{writes}})
{{/workflows}}

**Conflict Check:** ✅ No conflicts detected

{{/parallelZones}}

### Sequential Zones (Must run in order)
{{#sequentialZones}}
#### Phase {{number}}: {{name}}
**Workflow:** {{workflow}}
**Reason for Sequential:** {{reason}}
**Dependencies:** {{dependencies}}

{{/sequentialZones}}

## Conflict Analysis

### Conflicts Detected: {{conflictCount}}

{{#conflicts}}
#### Conflict {{number}}: {{type}}
- **Workflows:** {{workflowA}} ↔ {{workflowB}}
- **Resource:** {{resource}}
- **Type:** {{conflictType}} ({{explanation}})
- **Resolution:** {{resolution}}
- **Status:** {{status}}

{{/conflicts}}

{{^conflicts}}
✅ **No conflicts detected!** All workflows can run safely.
{{/conflicts}}

## Execution Timeline

```
{{timelineAscii}}
```

### Phase Breakdown
{{#phases}}
| Phase | Workflows | Type | Duration | Dependencies |
|-------|-----------|------|----------|--------------|
| {{number}} | {{workflowNames}} | {{type}} | {{duration}} | {{dependsOn}} |
{{/phases}}

## Runtime Configuration

### Selected Runtime: {{runtime}}

| Feature | Support | Notes |
|---------|---------|-------|
| Parallel Execution | {{parallelSupport}} | {{parallelNotes}} |
| Subagents | {{subagentSupport}} | {{subagentNotes}} |
| Large File Handling | {{largeFileSupport}} | {{largeFileNotes}} |

### Environment Detection
- **IDE:** {{ide}}
- **AI Model:** {{model}}
- **Context Window:** {{contextWindow}}

## Safety Measures

### Large File Handling
- **Range Read Threshold:** {{rangeThreshold}} lines
- **Append-Only Mode:** {{appendOnly}}
- **Chunk Processing:** {{chunkProcessing}}

### Backup & Recovery
- **Backup Before Writes:** {{backupEnabled}}
- **Checkpoint Frequency:** {{checkpointFreq}}
- **Rollback Available:** {{rollbackAvailable}}

## Risk Assessment

| Risk | Level | Mitigation |
|------|-------|------------|
| Context Overflow | {{contextRisk}} | {{contextMitigation}} |
| Conflict Escalation | {{conflictRisk}} | {{conflictMitigation}} |
| Subagent Failure | {{subagentRisk}} | {{subagentMitigation}} |

## Plan Approval

- **Planned By:** {{planner}}
- **Approved By:** {{approver}}
- **Approval Date:** {{approvalDate}}
- **Status:** {{approvalStatus}}

---

*Ready for execution in Step 4*
