# Sprint Plan - Phase 1: Katana Vectorbt Optimizer

**Project:** Katana Vectorbt Optimizer
**Phase:** Phase 1 - Core Foundation
**Sprint Planning Date:** 2026-02-26
**Planned By:** BMAD Sprint Planning Workflow
**Total Story Points:** 122
**Recommended Duration:** 12-16 weeks (6 sprints x 2 weeks)

---

## Executive Summary

Phase 1 establishes the core infrastructure for the Katana Vectorbt Optimizer. It covers 5 epics with 25 stories totaling 122 story points. The critical path runs through Epic 1 (Strategy Lifecycle) into Epic 2 (Journal Schema), which together unlock all dependent epics.

**Priority Rationale:**
- CRITICAL: E-STRATEGY-LIFECYCLE (foundational state machine, all other epics depend on it)
- CRITICAL: E-JOURNAL-SCHEMA (data layer, required by comparison and audit epics)
- HIGH: E-TELEMETRY-METRICS (depends on Epic 1)
- HIGH: E-COMPARE-WORKFLOW (depends on Epic 2)
- HIGH: E-AUDIT-TRAIL (depends on Epics 1 and 2)

---

## Team Capacity Assumptions

| Parameter | Value |
|-----------|-------|
| Team Size | 2 developers |
| Sprint Duration | 2 weeks |
| Velocity (per developer) | 10-12 points/sprint |
| Team Velocity | 20-24 points/sprint |
| Buffer/Overhead | 15% |
| Effective Velocity | 17-20 points/sprint |
| Number of Sprints | 6 sprints |

---

## Sprint Schedule

### Sprint 1 (Weeks 1-2): State Machine Foundation
**Capacity:** 20 points | **Committed:** 18 points

| Story ID | Title | Points | Assignee | Status |
|----------|-------|--------|----------|--------|
| S-STRATEGY-001 | Implement State Machine Transitions | 13 | Dev A | backlog |
| S-JOURNAL-001 | Create manifest.json Structure | 8 | Dev B | backlog |
| **Total** | | **21** | | |

> Note: S-STRATEGY-001 is the highest priority story (13 pts). S-JOURNAL-001 can start in parallel as it has no dependencies. Sprint may be slightly over capacity at 21 pts; team should assess actual velocity and adjust if needed.

**Sprint 1 Goal:** Establish state machine foundation and manifest schema - the two root dependencies for the entire project.

**Sprint 1 DoD:**
- S-STRATEGY-001: State transitions implemented, 10+ unit tests passing, invalid transitions rejected, audit trail functional
- S-JOURNAL-001: JSON Schema created and validated, TypeScript types generated, 8+ unit tests passing

---

### Sprint 2 (Weeks 3-4): Approval Workflow + Kill-Switch + Summary Schema
**Capacity:** 20 points | **Committed:** 19 points

| Story ID | Title | Points | Assignee | Status |
|----------|-------|--------|----------|--------|
| S-STRATEGY-002 | Build Approval Workflow | 8 | Dev A | backlog |
| S-STRATEGY-003 | Add Kill-Switch Mechanism | 5 | Dev A | backlog |
| S-JOURNAL-002 | Create summary.json v3.0 | 10 | Dev B | backlog |
| **Total** | | **23** | | |

> Note: All 3 stories depend on Sprint 1 completions. S-STRATEGY-002 and S-STRATEGY-003 both depend on S-STRATEGY-001. S-JOURNAL-002 depends on S-JOURNAL-001. At 23 pts this is slightly over capacity; if needed, defer S-STRATEGY-003 to Sprint 3.

**Sprint 2 Goal:** Complete approval and kill-switch mechanisms while advancing journal schema.

**Sprint 2 Dependencies:** Sprint 1 must be COMPLETE (S-STRATEGY-001, S-JOURNAL-001)

---

### Sprint 3 (Weeks 5-6): Timeline, Rejection Logic, Events Log, E-STRATEGY Complete
**Capacity:** 20 points | **Committed:** 18 points

| Story ID | Title | Points | Assignee | Status |
|----------|-------|--------|----------|--------|
| S-STRATEGY-004 | Create State Timeline | 5 | Dev A | backlog |
| S-STRATEGY-005 | Build Rejection/Resubmit Logic | 3 | Dev A | backlog |
| S-JOURNAL-003 | Implement events.ndjson | 8 | Dev B | backlog |
| S-JOURNAL-004 | Build Database Schema (Postgres) | 8 | Dev B | backlog |
| **Total** | | **24** | | |

> Note: S-STRATEGY-004 depends on S-STRATEGY-001 (Sprint 1). S-STRATEGY-005 depends on S-STRATEGY-002 (Sprint 2). S-JOURNAL-003 depends on S-JOURNAL-001 (Sprint 1). S-JOURNAL-004 depends on S-JOURNAL-002 AND S-JOURNAL-003 — may need to start mid-sprint after S-JOURNAL-003 completes. Split Dev B: complete S-JOURNAL-003 early in sprint, then start S-JOURNAL-004.

**Sprint 3 Goal:** Complete E-STRATEGY-LIFECYCLE epic and advance journal schema to database layer.

**Sprint 3 Dependencies:** S-STRATEGY-001 (Sprint 1), S-STRATEGY-002 (Sprint 2), S-JOURNAL-001 (Sprint 1), S-JOURNAL-002 (Sprint 2)

---

### Sprint 4 (Weeks 7-8): Journal Complete + Telemetry Foundation
**Capacity:** 20 points | **Committed:** 18 points

| Story ID | Title | Points | Assignee | Status |
|----------|-------|--------|----------|--------|
| S-JOURNAL-005 | Create Reproducibility Verifier | 6 | Dev A | backlog |
| S-TELEMETRY-001 | Instrument Time-to-Status | 6 | Dev A | backlog |
| S-TELEMETRY-002 | Implement MTIF Calculation | 6 | Dev B | backlog |
| **Total** | | **18** | | |

> Note: S-JOURNAL-005 depends on S-JOURNAL-001 (Sprint 1) and S-JOURNAL-004 (Sprint 3). S-TELEMETRY-001 and S-TELEMETRY-002 both depend on E-STRATEGY-LIFECYCLE epic being DONE (Sprint 3). Dev A handles journal completion then pivots to telemetry.

**Sprint 4 Goal:** Complete E-JOURNAL-SCHEMA epic and begin telemetry instrumentation.

**Sprint 4 Dependencies:** E-STRATEGY-LIFECYCLE complete (Sprint 3), S-JOURNAL-001 + S-JOURNAL-004 complete (Sprints 1+3)

---

### Sprint 5 (Weeks 9-10): Telemetry Dashboard + Compare Foundation
**Capacity:** 20 points | **Committed:** 19 points

| Story ID | Title | Points | Assignee | Status |
|----------|-------|--------|----------|--------|
| S-TELEMETRY-003 | Implement Log Diving Rate | 6 | Dev A | backlog |
| S-COMPARE-001 | Implement Comparison Algorithm | 7 | Dev B | backlog |
| S-AUDIT-001 | Implement Audit Trail Collection | 6 | Dev A | backlog |
| **Total** | | **19** | | |

> Note: S-TELEMETRY-003 depends on S-TELEMETRY-001 (Sprint 4). S-COMPARE-001 depends on E-JOURNAL-SCHEMA complete (Sprint 4). S-AUDIT-001 depends on E-JOURNAL-SCHEMA complete (Sprint 4). All three can proceed in parallel across Sprint 5.

**Sprint 5 Goal:** Complete telemetry collection layer, begin comparison and audit foundation.

**Sprint 5 Dependencies:** E-JOURNAL-SCHEMA complete (Sprint 4), S-TELEMETRY-001 (Sprint 4)

---

### Sprint 6 (Weeks 11-12): Complete All Remaining Stories
**Capacity:** 20 points | **Committed:** 22 points

| Story ID | Title | Points | Assignee | Status |
|----------|-------|--------|----------|--------|
| S-TELEMETRY-004 | Build Metrics Dashboard | 8 | Dev A | backlog |
| S-TELEMETRY-005 | Create Alert Rules | 4 | Dev A | backlog |
| S-COMPARE-002 | Build Run Selection UI | 5 | Dev B | backlog |
| S-AUDIT-002 | Build Verification Algorithm | 7 | Dev B | backlog |
| **Total** | | **24** | | |

> Note: Sprint 6 is over capacity at 24 pts. If team has maintained velocity, this is achievable; otherwise push S-COMPARE-002 or S-AUDIT-002 into a Sprint 7 buffer. S-TELEMETRY-004 depends on S-TELEMETRY-001+002+003. S-TELEMETRY-005 depends on S-TELEMETRY-004 (early in sprint). S-COMPARE-002 depends on S-COMPARE-001 (Sprint 5). S-AUDIT-002 depends on S-AUDIT-001 (Sprint 5).

**Sprint 6 Goal:** Complete E-TELEMETRY-METRICS epic. Advance Compare and Audit epics to 40%+.

---

### Sprint 7 (Weeks 13-14): Buffer + Remaining Compare/Audit Stories [CONTINGENCY]
**Capacity:** 20 points | **Committed:** 25 points (overflows from Sprint 6 + remaining)

| Story ID | Title | Points | Assignee | Status |
|----------|-------|--------|----------|--------|
| S-COMPARE-003 | Create Delta Visualization | 6 | Dev A | backlog |
| S-COMPARE-004 | Add Metric Selection | 4 | Dev A | backlog |
| S-COMPARE-005 | Build Export Functionality | 3 | Dev A | backlog |
| S-AUDIT-003 | Create Audit UI | 6 | Dev B | backlog |
| S-AUDIT-004 | Add "Reproduce Run" Button | 4 | Dev B | backlog |
| S-AUDIT-005 | Build Diagnostic Tool | 2 | Dev B | backlog |
| **Total** | | **25** | | |

> Note: This sprint completes both E-COMPARE-WORKFLOW and E-AUDIT-TRAIL epics. All stories follow sequential dependency chains within each epic. Two developers working in parallel (one on Compare, one on Audit) is optimal. If Sprint 6 overflowed, adjust starting point.

**Sprint 7 Goal:** Complete Phase 1 - all 5 epics done.

---

## Dependency Map

### Dependency Graph (topological order)

```
LAYER 0 (No dependencies - can start immediately):
  S-STRATEGY-001 [13 pts]
  S-JOURNAL-001  [8 pts]

LAYER 1 (depends on Layer 0):
  S-STRATEGY-002 → S-STRATEGY-001
  S-STRATEGY-003 → S-STRATEGY-001
  S-STRATEGY-004 → S-STRATEGY-001
  S-JOURNAL-002  → S-JOURNAL-001
  S-JOURNAL-003  → S-JOURNAL-001

LAYER 2 (depends on Layer 1):
  S-STRATEGY-005 → S-STRATEGY-002
  S-JOURNAL-004  → S-JOURNAL-002, S-JOURNAL-003

LAYER 3 (depends on Epic completion):
  S-TELEMETRY-001 → E-STRATEGY-LIFECYCLE (all 5 strategy stories)
  S-TELEMETRY-002 → E-STRATEGY-LIFECYCLE
  S-COMPARE-001   → E-JOURNAL-SCHEMA (all 5 journal stories)
  S-AUDIT-001     → E-JOURNAL-SCHEMA

LAYER 4 (depends on Layer 3):
  S-JOURNAL-005   → S-JOURNAL-001, S-JOURNAL-004
  S-TELEMETRY-003 → S-TELEMETRY-001
  S-COMPARE-002   → S-COMPARE-001
  S-AUDIT-002     → S-AUDIT-001

LAYER 5 (depends on Layer 4):
  S-TELEMETRY-004 → S-TELEMETRY-001, S-TELEMETRY-002, S-TELEMETRY-003
  S-COMPARE-003   → S-COMPARE-002
  S-AUDIT-003     → S-AUDIT-002

LAYER 6 (depends on Layer 5):
  S-TELEMETRY-005 → S-TELEMETRY-004
  S-COMPARE-004   → S-COMPARE-003
  S-COMPARE-005   → S-COMPARE-003
  S-AUDIT-004     → S-AUDIT-002, S-AUDIT-003

LAYER 7 (depends on Layer 6):
  S-AUDIT-005     → S-AUDIT-004
```

### Cross-Epic Dependencies

| Dependent Epic | Requires | Reason |
|----------------|----------|--------|
| E-TELEMETRY-METRICS | E-STRATEGY-LIFECYCLE (DONE) | Metrics instrument state transitions |
| E-COMPARE-WORKFLOW | E-JOURNAL-SCHEMA (DONE) | Comparison reads journal schema data |
| E-AUDIT-TRAIL | E-JOURNAL-SCHEMA (DONE) | Audit uses journal schema structures |

### Critical Path (Longest Dependency Chain)

```
S-JOURNAL-001 (8)
  → S-JOURNAL-002 (10)
    → S-JOURNAL-003 (8) [parallel, but must both complete before JOURNAL-004]
      → S-JOURNAL-004 (8)
        → S-COMPARE-001 (7)  [after E-JOURNAL-SCHEMA complete]
          → S-COMPARE-002 (5)
            → S-COMPARE-003 (6)
              → S-COMPARE-004 (4)
```

**Critical Path Total:** 8+10+8+8+7+5+6+4 = **56 points** across ~10 sprints (or parallel execution)

Alternatively through Audit:
```
S-JOURNAL-001 → S-JOURNAL-002 → S-JOURNAL-003 → S-JOURNAL-004 → S-AUDIT-001 → S-AUDIT-002 → S-AUDIT-003 → S-AUDIT-004 → S-AUDIT-005
Points: 8+10+8+8+6+7+6+4+2 = 59 points
```

**Longest Critical Path: Journal → Audit chain at 59 points (9 stories deep)**

---

## Risk Assessment

### Risk 1: S-STRATEGY-001 Complexity (HIGH)
- **Description:** State machine at 13 points is the largest single story. If underestimated, Sprint 1 will be blocked.
- **Probability:** MEDIUM
- **Impact:** HIGH - all strategy stories blocked
- **Mitigation:** Consider splitting into 001a (state definitions + transitions) and 001b (audit trail + validation) if estimation exceeds 2-3 days of work. Start Sprint 1 with this story immediately.

### Risk 2: E-JOURNAL-SCHEMA Complexity VERY HIGH (HIGH)
- **Description:** Epic is labeled VERY HIGH complexity with 40 points. S-JOURNAL-004 depends on both S-JOURNAL-002 and S-JOURNAL-003.
- **Probability:** MEDIUM
- **Impact:** HIGH - blocks E-COMPARE-WORKFLOW and E-AUDIT-TRAIL
- **Mitigation:** Prioritize journal stories, use technical spike in Sprint 1 to validate Postgres schema design early. Pre-define schema structure before coding begins.

### Risk 3: Cross-Epic Blocking Dependencies (HIGH)
- **Description:** E-TELEMETRY-METRICS, E-COMPARE-WORKFLOW, and E-AUDIT-TRAIL all require full completion of preceding epics.
- **Probability:** MEDIUM
- **Impact:** HIGH - potential 1-2 sprint delays if Epic 1 or 2 slip
- **Mitigation:** Track Epic 1 and Epic 2 velocity weekly. If slipping by more than 20%, escalate and consider reducing scope (deferring optional stories).

### Risk 4: Sprint 6 Over-Capacity (MEDIUM)
- **Description:** Sprint 6 planned at 24 points against 20-point capacity.
- **Probability:** MEDIUM
- **Impact:** MEDIUM - compare and audit stories spill to extended sprint
- **Mitigation:** Sprint 7 buffer sprint defined. Team should adjust Sprint 6 scope based on actual velocity at Sprint 5 retrospective.

### Risk 5: S-JOURNAL-004 Mid-Sprint Dependency (MEDIUM)
- **Description:** S-JOURNAL-004 requires both S-JOURNAL-002 AND S-JOURNAL-003 complete. Dev B must sequence these tightly in Sprint 3.
- **Probability:** LOW-MEDIUM
- **Impact:** MEDIUM - S-JOURNAL-004 start delayed if S-JOURNAL-003 runs long
- **Mitigation:** Dev B should complete S-JOURNAL-003 in first 3 days of Sprint 3, allowing S-JOURNAL-004 start by midpoint.

### Risk 6: Test Coverage Requirements (LOW)
- **Description:** Each story specifies minimum unit test counts. Cumulative testing overhead could slow velocity.
- **Probability:** LOW
- **Impact:** LOW-MEDIUM - TDD approach might slow initial implementation
- **Mitigation:** Build test utilities/helpers early in Sprint 1 to reduce per-story testing overhead. Write tests alongside implementation, not after.

### Risk 7: Postgres Schema Migrations (LOW)
- **Description:** S-JOURNAL-004 requires migration scripts (up/down). Database migrations are notoriously tricky and time-consuming to test.
- **Probability:** LOW
- **Impact:** MEDIUM - if migrations break, blocking for team
- **Mitigation:** Use established migration tooling (e.g., Flyway, Liquibase, or Prisma Migrate). Test migrations on clean AND existing databases as per acceptance criteria.

---

## Story Point Summary

| Epic | Points | Sprints | Priority |
|------|--------|---------|----------|
| E-STRATEGY-LIFECYCLE | 34 | 1-3 | CRITICAL |
| E-JOURNAL-SCHEMA | 40 | 1-4 | CRITICAL |
| E-TELEMETRY-METRICS | 30 | 4-6 | HIGH |
| E-COMPARE-WORKFLOW | 25 | 5-7 | HIGH |
| E-AUDIT-TRAIL | 25 | 5-7 | HIGH |
| **TOTAL** | **154** | **7 sprints** | |

> Note: Total in sprint plan is 154 points vs. 122 in epics file. The epics file total (122) is correct for story-level points. The 154 figure is an artifact of the sprint schedule; the actual 25-story total is 122 points.

**Corrected totals from epics:**
- E-STRATEGY-LIFECYCLE: 13+8+5+5+3 = 34 pts
- E-JOURNAL-SCHEMA: 8+10+8+8+6 = 40 pts
- E-TELEMETRY-METRICS: 6+6+6+8+4 = 30 pts
- E-COMPARE-WORKFLOW: 7+5+6+4+3 = 25 pts
- E-AUDIT-TRAIL: 6+7+6+4+2 = 25 pts
- **Grand Total: 154 points** (epics file states 122 — discrepancy to review)

---

## Parallel Execution Opportunities

The following stories can be executed in parallel (different developers):

| Sprint | Parallel Track A | Parallel Track B |
|--------|-----------------|-----------------|
| Sprint 1 | S-STRATEGY-001 | S-JOURNAL-001 |
| Sprint 2 | S-STRATEGY-002 + 003 | S-JOURNAL-002 |
| Sprint 3 | S-STRATEGY-004 + 005 | S-JOURNAL-003 → 004 |
| Sprint 4 | S-JOURNAL-005 + S-TELEMETRY-001 | S-TELEMETRY-002 |
| Sprint 5 | S-TELEMETRY-003 + S-AUDIT-001 | S-COMPARE-001 |
| Sprint 6 | S-TELEMETRY-004 + 005 | S-COMPARE-002 + S-AUDIT-002 |
| Sprint 7 | S-COMPARE-003 + 004 + 005 | S-AUDIT-003 + 004 + 005 |

---

## Definition of Done (Phase Level)

Phase 1 is COMPLETE when:
- [ ] All 25 stories reach status: `done`
- [ ] All 5 epics reach status: `done`
- [ ] Minimum test coverage achieved (127 tests total across all stories)
- [ ] All deliverable files created (per epic deliverables sections)
- [ ] Integration testing verifies cross-epic interactions
- [ ] Documentation published (state machine diagram, schema docs)

---

## Next Actions

1. **Immediately:** Create story files for Sprint 1 stories (S-STRATEGY-001, S-JOURNAL-001)
2. **Sprint 0 (pre-sprint):** Set up development environment, Postgres instance, TypeScript project scaffold
3. **Sprint 1 kickoff:** Assign stories, confirm acceptance criteria with team
4. **Weekly:** Update sprint-status.yaml to reflect actual progress
5. **Sprint Review:** Conduct demo of completed stories at end of each sprint
6. **Sprint Retrospective:** Capture learnings before starting next sprint

---

*Document generated by BMAD Sprint Planning Workflow*
*Date: 2026-02-26*
*Status: READY FOR EXECUTION*
