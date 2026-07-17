---
title: "Orchestration Session Report"
session_id: "[auto-generated: session-YYYY-MM-DD-HHmmss]"
session_date: "[YYYY-MM-DD]"
user_task: "[Original user task/requirement]"
yolo_level: "[0|1|2|3]"
approval_method: "[auto|manual|hybrid]"
user: "[Username or identifier]"
orchestrator_version: "2.0"
status: "[DISCOVERY|PLANNING|EXECUTION|VALIDATION|COMPLETE|FAILED]"
---

# Orchestration Session Report

**Session ID:** [session_id]
**Started:** [ISO 8601 timestamp]
**Completed:** [ISO 8601 timestamp]
**Duration:** [Total time for complete orchestration]
**User:** [User identifier]

---

## Executive Summary

**Task:** [High-level summary of what user asked to do]

**Approach:** [Which orchestration strategy was used - YOLO auto, manual approval, hybrid]

**Result:** [Overall success/failure status and key metrics]

**Outcome:** [What was delivered and key artifacts]

---

## 1. Task Discovery (From Step 01)

### User Input

**Original Request:**
> [Exact user task/question]

**Task Complexity:** [Low|Medium|High]
**Task Scope:** [Narrow|Medium|Broad]
**Time Sensitivity:** [Routine|Urgent|Critical]

### Discovered Intent

**What User Needs:**
1. [Need 1]
2. [Need 2]
3. [Need 3]

**Context & Constraints:**
- **Domain:** [Domain of task]
- **Stakeholders:** [Who is involved]
- **Constraints:** [Time, resources, dependencies]
- **Success Criteria:** [What success looks like]

### Clarifications Made

- [ ] Clarification 1: [Original assumption → Updated understanding]
- [ ] Clarification 2: [Original assumption → Updated understanding]
- [ ] Clarification 3: [Original assumption → Updated understanding]

---

## 2. Workflow Selection (From Step 02)

### Search Strategy Used

**CSV Sources Queried:**
- [ ] workflow-manifest.csv (Primary)
- [ ] advanced-elicitation methods.csv (If applicable)
- [ ] problem-solving methods.csv (If applicable)

**MCP Sources Queried:**
- [ ] Memory (ReasoningBank patterns)
- [ ] OctoCode (GitHub patterns)
- [ ] Brave/Tavily (Public solutions)
- [ ] Context7 (Documentation)

### Selected Workflows

#### Primary Workflow: [Workflow 1]

| Property | Value |
|----------|-------|
| **Workflow ID** | [wf_id_1] |
| **Module** | [bmm\|bmb\|tea\|cis\|core] |
| **Type** | [planning\|implementation\|testing\|design\|analysis] |
| **Steps** | [N] |
| **Est. Duration** | [X minutes] |
| **Confidence** | [XX]% |
| **CSV Score** | [XX] |
| **MCP Score** | [XX] |

**Why Selected:** [Key matching factors and reasoning]

---

#### Secondary Workflow: [Workflow 2] (If applicable)

| Property | Value |
|----------|-------|
| **Workflow ID** | [wf_id_2] |
| **Module** | [module] |
| **Role** | [Prerequisite\|Parallel\|Followup] |
| **Confidence** | [XX]% |

**Integration Point:** [How this workflow relates to primary workflow]

---

#### Tertiary Workflow: [Workflow 3] (If applicable)

| Property | Value |
|----------|-------|
| **Workflow ID** | [wf_id_3] |
| **Module** | [module] |
| **Role** | [Prerequisite\|Parallel\|Followup] |
| **Confidence** | [XX]% |

**Integration Point:** [How this workflow relates to primary workflow]

---

### Rejected Alternatives

**Alternative A: [Workflow Name]**
- **Score:** [XX]%
- **Reason for Rejection:** [Why this wasn't selected]
- **Could Use If:** [Conditions when this would be better]

**Alternative B: [Workflow Name]**
- **Score:** [XX]%
- **Reason for Rejection:** [Why this wasn't selected]
- **Could Use If:** [Conditions when this would be better]

---

## 3. Orchestration Plan (From Step 03)

### Orchestration Strategy

**Overall Strategy:** [Serial|Parallel|Hybrid]

**Orchestration Model:**
- **Topology:** [hierarchical|mesh|adaptive]
- **Max Parallel Agents:** [N]
- **Consensus Algorithm:** [raft|byzantine|gossip]
- **Load Balancing:** [round-robin|adaptive|weighted]

### Execution Timeline

**Phase Structure:**
```
┌─────────────────────────────────────────────────┐
│ PHASE 1: [Phase Name] (Sequential or Parallel)   │
│                                                   │
│  ├─ Workflow A (Duration: Y min)                 │
│  ├─ Workflow B (Duration: Y min) [Depends on A]  │
│  └─ Workflow C (Duration: Y min)                 │
│                                                   │
│  → Checkpoint 1: Validate Phase 1 outputs        │
└─────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────┐
│ PHASE 2: [Phase Name] (Parallel Zones)           │
│                                                   │
│  ┌─ Zone 2A ──┬─ Workflow D (Y min)             │
│  │            └─ Workflow E (Y min)             │
│  │                                              │
│  └─ Zone 2B ──┬─ Workflow F (Y min)             │
│               └─ Workflow G (Y min)             │
│                                                   │
│  → Checkpoint 2: Validate Phase 2 outputs        │
└─────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────┐
│ PHASE 3: [Phase Name] (Sequential with Fallback) │
│                                                   │
│  ├─ Workflow H [Primary Path]                    │
│  ├─ Workflow I [Fallback Path]                   │
│  └─ Workflow J [Aggregation]                     │
│                                                   │
│  → Checkpoint 3: Final Validation                │
└─────────────────────────────────────────────────┘
```

### Parallel Zones Definition

**Parallel Zone 1: [Zone Name]**
- **Workflows:** [Workflow A, Workflow B, Workflow C]
- **Type:** [Independent|Partially dependent]
- **Max Parallelism:** [3]
- **Constraint:** [If any constraint exists]

**Parallel Zone 2: [Zone Name]**
- **Workflows:** [Workflow X, Workflow Y]
- **Type:** [Independent|Partially dependent]
- **Max Parallelism:** [2]
- **Constraint:** [If any constraint exists]

### Sequential Dependencies

```
Workflow A (2h) ──→ Workflow B (1h) ──→ Workflow C (0.5h)
                                             ↓
                                      Workflow D (1h)
                                             ↓
                                      Aggregate Outputs
```

**Critical Path:** [Workflow A → B → C → D] (4.5 hours total)
**Slack Paths:** [Any non-critical workflows and their slack time]

### Conflict Analysis

**Detected Conflicts:**
- [ ] Conflict 1: [Type] - [Workflows involved] - [Resolution strategy]
- [ ] Conflict 2: [Type] - [Workflows involved] - [Resolution strategy]
- [ ] No conflicts detected: Workflows can execute independently

**Conflict Resolution Strategy:**
1. [Strategy for conflict type 1]
2. [Strategy for conflict type 2]
3. [Fallback strategy if conflicts persist]

---

## 4. Execution Phase (From Step 04)

### Phase Execution Summary

**Total Phases:** [N]
**Phases Completed:** [M]
**Current Phase:** [K of N]
**Overall Progress:** [X%]

### Phase 1 Results: [Phase Name]

**Status:** [PASS|FAIL|IN_PROGRESS]
**Duration:** [Actual: X min | Planned: Y min]

**Workflow Results:**

| Workflow | Status | Duration | Output Loc | Notes |
|----------|--------|----------|-----------|-------|
| [WF A] | PASS | 45 min | [path] | Completed on-time |
| [WF B] | PASS | 60 min | [path] | Completed with notes |
| [WF C] | PASS | 30 min | [path] | Faster than expected |

**Artifacts Generated:**
- [ ] artifact_1.md - [Description]
- [ ] artifact_2.yml - [Description]
- [ ] artifact_3.json - [Description]

**Issues/Notes:**
- [Issue 1 and resolution]
- [Issue 2 and resolution]

**Checkpoint Status:** [APPROVED|NEEDS_REWORK|BLOCKED]

---

### Phase 2 Results: [Phase Name]

**Status:** [PASS|FAIL|IN_PROGRESS]
**Duration:** [Actual: X min | Planned: Y min]

**Parallel Zone Results:**

**Zone 2A:**
| Workflow | Status | Duration | Output |
|----------|--------|----------|--------|
| [WF D] | [Status] | X min | [path] |
| [WF E] | [Status] | Y min | [path] |

**Zone 2B:**
| Workflow | Status | Duration | Output |
|----------|--------|----------|--------|
| [WF F] | [Status] | X min | [path] |
| [WF G] | [Status] | Y min | [path] |

**Zone Performance:** [All zones completed in parallel, total time: X min]

**Artifacts Generated:**
- [ ] artifact_4.md
- [ ] artifact_5.json
- [ ] artifact_6.csv

**Checkpoint Status:** [APPROVED|NEEDS_REWORK|BLOCKED]

---

### Phase 3 Results: [Phase Name]

**Status:** [PASS|FAIL|IN_PROGRESS]
**Duration:** [Actual: X min | Planned: Y min]

**Workflow Results:**
- [Workflow H]: [Status] - [Duration] - [Output]
- [Workflow I]: [Status] - [Duration] - [Output]
- [Workflow J]: [Status] - [Duration] - [Output]

**Artifacts Generated:**
- [ ] artifact_7.md
- [ ] artifact_8.yml

**Checkpoint Status:** [APPROVED|NEEDS_REWORK|BLOCKED]

---

## 5. Cascade Synchronization (From Step 05)

### Document Synchronization

**Master Documents Updated:**
- [ ] [Document 1] - Synced with outputs from Phase [X]
- [ ] [Document 2] - Synced with outputs from Phase [Y]
- [ ] [Document 3] - Synced with outputs from Phase [Z]

### Cross-Workflow Integration

**Data Flow:**
```
Phase 1 Output ──→ Phase 2 Processing ──→ Phase 3 Aggregation
   (artifact_1)      (uses artifact_1)        (final output)
```

**Validation:**
- [ ] All cross-phase references valid
- [ ] Data types consistent across workflows
- [ ] No data loss in transformation
- [ ] Integrity verified at each cascade point

### Synchronization Conflicts Resolved

- [Conflict 1 and resolution]
- [Conflict 2 and resolution]

**Final Sync Status:** [SUCCESS|PARTIAL|FAILED]

---

## 6. Validation Results (From Step 06)

### Quality Validation

**Output Validation:**
- [ ] All required artifacts present
- [ ] Artifacts match expected format/schema
- [ ] All data fields populated
- [ ] No data corruption detected

**Completeness Check:**
- [ ] All workflow outputs included
- [ ] All phases documented
- [ ] All checkpoints validated
- [ ] All artifacts cross-referenced

**Consistency Check:**
- [ ] No contradictions between documents
- [ ] Cross-references resolve correctly
- [ ] Data types aligned across workflows
- [ ] Version consistency verified

### Compliance Validation

**Workflow Compliance:**
- [ ] All workflows executed as planned
- [ ] Step sequences followed correctly
- [ ] Input/output contracts honored
- [ ] Deviations documented

**Format Compliance:**
- [ ] Markdown formatting correct
- [ ] YAML/JSON schemas valid
- [ ] File naming conventions followed
- [ ] Directory structure correct

**Traceability Validation:**
- [ ] Session ID consistent across documents
- [ ] All artifacts traceable to source workflow
- [ ] Timestamps logical and consistent
- [ ] All decisions documented

### Overall Validation Status

**Validation Result:** [PASS|FAIL|MANUAL_REVIEW]

**Pass Criteria Met:**
- [ ] 100% artifact validation
- [ ] 100% completeness
- [ ] 100% consistency
- [ ] 100% compliance

**Issues Found & Resolution:**
- [Issue 1 - Resolution]
- [Issue 2 - Resolution]

---

## Traceability Matrix

### Requirements Traceability

| Requirement | Selected Workflow | Phase | Artifact | Status |
|-------------|------------------|-------|----------|--------|
| [Req 1] | [Workflow A] | [Phase X] | [artifact] | ✓ Covered |
| [Req 2] | [Workflow B] | [Phase Y] | [artifact] | ✓ Covered |
| [Req 3] | [Workflow C] | [Phase Z] | [artifact] | ✓ Covered |

### Artifact Traceability

| Artifact | Generated By | Phase | Used By | Status |
|----------|--------------|-------|---------|--------|
| [artifact_1] | [Workflow A] | [1] | [Workflow B] | ✓ Valid |
| [artifact_2] | [Workflow B] | [2] | [Workflow C] | ✓ Valid |
| [artifact_3] | [Workflow C] | [3] | Final Output | ✓ Final |

---

## Session Metadata & Statistics

### Session Information

| Property | Value |
|----------|-------|
| **Session ID** | [session_id] |
| **Created** | [ISO 8601] |
| **Completed** | [ISO 8601] |
| **Total Duration** | [X hours Y minutes] |
| **User** | [Username] |
| **YOLO Level** | [0-3] |
| **Approval Method** | [auto\|manual\|hybrid] |

### Orchestration Statistics

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| **Workflows Executed** | [N] | [planned] | ✓|✗ |
| **Total Phases** | [N] | [planned] | ✓|✗ |
| **Parallel Zones** | [N] | [planned] | ✓|✗ |
| **Artifacts Generated** | [N] | [planned] | ✓|✗ |
| **Execution Success Rate** | [X]% | >90% | ✓|✗ |
| **On-Time Completion** | [X]% | >85% | ✓|✗ |
| **Quality Score** | [X]/100 | >85 | ✓|✗ |

### Performance Metrics

**Planned vs. Actual:**
```
Planned Duration: 4.0 hours
Actual Duration:  3.5 hours
Efficiency Gain:  +12.5%

Phase 1:  Planned 1.5h → Actual 1.3h (Faster)
Phase 2:  Planned 1.5h → Actual 1.7h (Slower - wait time for dependencies)
Phase 3:  Planned 1.0h → Actual 0.5h (Much faster - optimized)
```

**Resource Utilization:**
- Peak agents active: [N] of [max_agents]
- Average agents active: [N]
- Parallelization efficiency: [X]%
- Wait time: [X%] of total (due to dependencies)

---

## Final Outputs & Deliverables

### Output Summary

**Location:** [`orchestration-session-[SESSION-ID]/`]

**Artifact Inventory:**
```
orchestration-session-[SESSION-ID]/
├── phase-1-outputs/
│   ├── artifact_1.md
│   ├── artifact_2.yml
│   └── artifact_3.json
├── phase-2-outputs/
│   ├── artifact_4.md
│   ├── artifact_5.json
│   └── artifact_6.csv
├── phase-3-outputs/
│   ├── artifact_7.md
│   └── artifact_8.yml
├── checkpoints/
│   ├── checkpoint-phase-1.md
│   ├── checkpoint-phase-2.md
│   └── checkpoint-phase-3.md
├── session-summary/
│   ├── orchestration-session-[SESSION-ID].md (this file)
│   ├── traceability-matrix.md
│   └── performance-report.md
└── logs/
    ├── execution-log.txt
    └── errors-warnings.log
```

### Key Deliverables

1. **[Deliverable 1]** - [Description and use]
2. **[Deliverable 2]** - [Description and use]
3. **[Deliverable 3]** - [Description and use]

### Quality Metrics of Deliverables

- **Completeness:** [X]% (target: 100%)
- **Accuracy:** [X]% (target: 100%)
- **Validation:** [X]% (target: 100%)

---

## Session Status & Recommendations

### Overall Status

**Session Result:** [SUCCESSFUL|PARTIAL_SUCCESS|FAILED]

**Final Verdict:**
- ✓ All critical workflows completed
- ✓ All outputs validated
- ✓ All artifacts consistent
- ✓ Session objectives achieved

OR

- ✗ [Issue 1] - impacted deliverables
- ✗ [Issue 2] - requires manual intervention

### Recommendations for Next Steps

**Immediate Actions:**
1. [Action 1 - urgency/owner]
2. [Action 2 - urgency/owner]
3. [Action 3 - urgency/owner]

**Optimizations for Future Sessions:**
- [Optimization 1 - why and how to implement]
- [Optimization 2 - why and how to implement]

**Known Limitations:**
- [Limitation 1 - workaround if applicable]
- [Limitation 2 - workaround if applicable]

---

## Related Documentation

- **Workflow Selection Details:** `workflow-selection-[SESSION-ID].md`
- **Phase 1 Checkpoint:** `checkpoint-phase-1.md`
- **Phase 2 Checkpoint:** `checkpoint-phase-2.md`
- **Phase 3 Checkpoint:** `checkpoint-phase-3.md`
- **Execution Log:** `logs/execution-log.txt`
- **Traceability Matrix:** `traceability-matrix.md`

---

*Orchestration Report Version: 2.0 | Last Updated: 2026-02-26*
