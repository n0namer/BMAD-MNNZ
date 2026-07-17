---
title: "Phase Checkpoint Report"
checkpoint_id: "[auto-generated: checkpoint-YYYY-MM-DD-HHmmss]"
session_id: "[session_id]"
phase_number: "[X]"
total_phases: "[N]"
parallel_zones_count: "[M]"
status: "[IN_PROGRESS|PENDING_REVIEW|APPROVED|NEEDS_REWORK]"
timestamp: "[ISO 8601]"
---

# Phase [X] Checkpoint Report

**Session:** [session_id]
**Phase:** [X] of [N]
**Created:** [timestamp]
**Status:** [IN_PROGRESS|PENDING_REVIEW|APPROVED|NEEDS_REWORK]

---

## Executive Summary

**Objective:** [What this phase aims to accomplish]

**Scope:** [Number of workflows, parallel zones, sequential dependencies]

**Duration:** [Actual: X min | Planned: Y min]

**Overall Status:** [PASS|NEEDS_REWORK|BLOCKED]

---

## Phase Overview

### Phase Metadata

| Property | Value |
|----------|-------|
| **Phase Number** | [X] |
| **Total Phases** | [N] |
| **Parallel Zones** | [M] |
| **Sequential Steps** | [K] |
| **Critical Path** | [Critical path duration] |
| **Slack Time** | [Total slack available] |

### Phase Workflows

| Sequence | Workflow ID | Workflow Name | Type | Status |
|----------|-------------|---------------|------|--------|
| [seq] | [wf_id_1] | [Workflow 1] | [type] | [PASS\|FAIL\|PENDING] |
| [seq] | [wf_id_2] | [Workflow 2] | [type] | [PASS\|FAIL\|PENDING] |
| [seq] | [wf_id_3] | [Workflow 3] | [type] | [PASS\|FAIL\|PENDING] |

---

## Parallel Zone Results

### Parallel Zone 1: [Zone Name]

**Workflows in Zone:**
- [Workflow A]
- [Workflow B]
- [Workflow C]

**Execution Model:** [Concurrent / Sequential within zone]

**Zone Status:** [PASS|FAIL|PENDING]

#### Workflow A Results

**ID:** [workflow_id]
**Status:** [PASS|FAIL|PENDING]
**Duration:** [Actual: X min | Planned: Y min]
**Output Location:** [Path to output artifact]
**Validation:** [PASS|FAIL|MANUAL_REVIEW]

**Key Outputs:**
- [ ] Output artifact 1: [File path or URL]
- [ ] Output artifact 2: [File path or URL]
- [ ] Output artifact 3: [File path or URL]

**Issues/Notes:**
- [Issue 1 or Note 1]
- [Issue 2 or Note 2]

---

#### Workflow B Results

**ID:** [workflow_id]
**Status:** [PASS|FAIL|PENDING]
**Duration:** [Actual: X min | Planned: Y min]
**Output Location:** [Path to output artifact]
**Validation:** [PASS|FAIL|MANUAL_REVIEW]

**Key Outputs:**
- [ ] Output artifact 1: [File path or URL]
- [ ] Output artifact 2: [File path or URL]

**Issues/Notes:**
- [Issue 1 or Note 1]

---

#### Workflow C Results

**ID:** [workflow_id]
**Status:** [PASS|FAIL|PENDING]
**Duration:** [Actual: X min | Planned: Y min]
**Output Location:** [Path to output artifact]
**Validation:** [PASS|FAIL|MANUAL_REVIEW]

**Key Outputs:**
- [ ] Output artifact 1: [File path or URL]

**Issues/Notes:**
- [Issue 1 or Note 1]

---

### Parallel Zone 2: [Zone Name]

**Workflows in Zone:**
- [Workflow D]
- [Workflow E]

**Execution Model:** [Concurrent / Sequential within zone]

**Zone Status:** [PASS|FAIL|PENDING]

#### Workflow D Results
[Same structure as above]

#### Workflow E Results
[Same structure as above]

---

## Sequential Dependencies Analysis

### Dependency Chain 1

```
[Workflow X] ──→ [Workflow Y] ──→ [Workflow Z]
   (PASS)          (WAITING)       (PENDING)
   Output:         Input from X
   artifact_1      artifact_1
```

**Status:** [BLOCKED|READY|IN_PROGRESS|COMPLETE]
**Critical Path:** [YES|NO]
**Slack Time:** [0 min | X min]

**Validation:**
- [✓] Input validation passed
- [✓] Data consistency confirmed
- [X] Output format verified

---

### Dependency Chain 2

```
[Workflow A] ──→ [Workflow B]
   (PASS)        (RUNNING)
```

**Status:** [BLOCKED|READY|IN_PROGRESS|COMPLETE]
**Critical Path:** [YES|NO]
**Slack Time:** [X min]

---

## Conflict Detection & Resolution

### Conflict 1: [Conflict Type]

**Type:** [Read-After-Write|Write-After-Write|Resource|Data]

**Workflows Involved:**
- [Workflow A]
- [Workflow B]

**Issue Description:**
[Description of the conflict and why it occurred]

**Resolution Applied:**
[How the conflict was resolved]

**Status:** [RESOLVED|UNRESOLVED|PENDING_REVIEW]

---

### Conflict 2: [Conflict Type]

**Type:** [Read-After-Write|Write-After-Write|Resource|Data]

**Workflows Involved:**
- [Workflow X]
- [Workflow Y]

**Issue Description:**
[Description of the conflict]

**Resolution Applied:**
[How the conflict was resolved]

**Status:** [RESOLVED|UNRESOLVED|PENDING_REVIEW]

---

## Result Aggregation

### Phase Metrics

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| **Completion Rate** | [X]% | 100% | [✓|✗] |
| **On-Time Rate** | [X]% | >90% | [✓|✗] |
| **Quality Score** | [X]/100 | >80 | [✓|✗] |
| **Validation Rate** | [X]% | 100% | [✓|✗] |
| **Conflict Rate** | [X]% | <10% | [✓|✗] |

### Aggregated Outputs

**Total Artifacts Generated:** [N]

**Artifact Categories:**
- Documents: [N] files
- Code: [N] files
- Data: [N] files
- Configuration: [N] files

**Output Location:** [`phase-[X]-outputs/`]

**Artifact Manifest:**
```
Phase [X] Outputs:
├── [artifact_type_1]/
│   ├── [artifact_1.md]
│   ├── [artifact_2.yml]
│   └── [artifact_3.json]
├── [artifact_type_2]/
│   ├── [artifact_4.py]
│   └── [artifact_5.js]
└── [artifact_type_3]/
    ├── [artifact_6.csv]
    └── [artifact_7.xml]
```

### Data Consistency Check

**Cross-Workflow Validation:**
- [ ] Artifact A (from Workflow 1) matches expected schema
- [ ] Artifact B (from Workflow 2) references Artifact A correctly
- [ ] Artifact C (from Workflow 3) integrates data from A and B properly
- [ ] No data conflicts or duplicates detected
- [ ] All references/links are valid

**Status:** [PASS|FAIL|MANUAL_REVIEW]

---

## Next Phase Dependencies

### Inputs Required for Phase [X+1]

| Input | Source | Status | Location |
|-------|--------|--------|----------|
| [Input 1] | [Phase X, Workflow A] | [Available|Pending|N/A] | [path] |
| [Input 2] | [Phase X, Workflow B] | [Available|Pending|N/A] | [path] |
| [Input 3] | [Phase X, Parallel Zone 1] | [Available|Pending|N/A] | [path] |

### Blockers/Issues for Phase [X+1]

- [ ] [Blocker 1] - Severity: [Critical|High|Medium|Low]
- [ ] [Blocker 2] - Severity: [Critical|High|Medium|Low]

### Recommendations for Phase [X+1]

1. **Optimization:** [Suggested improvement]
2. **Risk Mitigation:** [Proactive measure]
3. **Resource Allocation:** [Team/tool consideration]

---

## Validation Checklist

### Phase Completion Criteria

- [ ] All required workflows completed
- [ ] All outputs generated and validated
- [ ] No unresolved conflicts
- [ ] All artifacts in correct format
- [ ] All documentation complete
- [ ] All tests passed (if applicable)
- [ ] Performance within acceptable range
- [ ] Security requirements met (if applicable)

### Quality Gates

- [ ] Code review completed (if code generation)
- [ ] Output validation against requirements
- [ ] Dependency satisfaction verified
- [ ] Performance benchmarks met
- [ ] User acceptance criteria passed

### Approval Status

**Phase [X] Status:** [READY_FOR_APPROVAL|NEEDS_REWORK|BLOCKED]

**Approval Decision:**
- [ ] APPROVED - Proceed to Phase [X+1]
- [ ] APPROVED WITH NOTES - Proceed with cautions documented
- [ ] NEEDS REWORK - [Specific issues to fix]
- [ ] BLOCKED - Cannot proceed until [blockers resolved]

**Approved By:** [User/Coordinator]
**Approval Date:** [ISO 8601]
**Approval Notes:** [Additional context]

---

## Issues & Resolution Log

### Issue 1

**ID:** [issue_id_1]
**Severity:** [Critical|High|Medium|Low]
**Status:** [RESOLVED|OPEN|DEFERRED]

**Description:** [Detailed issue description]

**Root Cause:** [Why it occurred]

**Resolution:** [How it was fixed]

**Verification:** [How resolution was verified]

---

### Issue 2

**ID:** [issue_id_2]
**Severity:** [Critical|High|Medium|Low]
**Status:** [RESOLVED|OPEN|DEFERRED]

[Same structure as Issue 1]

---

## Timeline Analysis

### Actual vs. Planned Duration

```
Workflow A:  ████████░░ (80 min / 100 min planned) -20% faster
Workflow B:  ██████░░░░ (60 min / 60 min planned) On-time
Workflow C:  ████░░░░░░ (40 min / 80 min planned) -50% variance

Phase Total: 180 min / 240 min planned (-25% efficiency gain)
```

**Performance Notes:**
- [Note 1: Why some workflows were faster/slower]
- [Note 2: Resource utilization insights]
- [Note 3: Parallelization effectiveness]

---

## Traceability & Audit Trail

**Phase Checkpoint ID:** [checkpoint_id]
**Session ID:** [session_id]
**Session Timestamp:** [ISO 8601]
**Phase Created:** [ISO 8601]
**Phase Completed:** [ISO 8601]
**Last Modified:** [ISO 8601]

**Related Documents:**
- Orchestration Plan: [`orchestration-session-[SESSION-ID].md`]
- Phase Outputs: [`phase-[X]-outputs/`]
- Next Checkpoint: [`checkpoint-phase-[X+1].md`] (if created)

**Execution Record:**
```
Phase [X] Execution Timeline:

14:00 - Phase [X] started
14:15 - Parallel Zone 1 completed (all 3 workflows)
14:30 - Conflict detected in Zone 2, resolved
14:45 - Sequential dependency chain validated
15:00 - Artifact aggregation complete
15:10 - All validations passed
15:12 - Phase [X] checkpoint created
```

---

*Checkpoint Version: 2.0 | Last Updated: 2026-02-26*
