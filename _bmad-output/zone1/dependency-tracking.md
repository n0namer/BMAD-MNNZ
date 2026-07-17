# Dependency Tracking - Katana Vectorbt Phase 1

**Project:** Katana Vectorbt Optimizer
**Generated:** 2026-02-26
**Purpose:** Detailed dependency tracking to prevent sprint blocking

---

## Dependency Matrix

Each row shows a story and what it is blocked by (must be DONE before this story can start).

| Story | Blocked By | Layer | Sprint |
|-------|-----------|-------|--------|
| S-STRATEGY-001 | — | 0 | 1 |
| S-JOURNAL-001 | — | 0 | 1 |
| S-STRATEGY-002 | S-STRATEGY-001 | 1 | 2 |
| S-STRATEGY-003 | S-STRATEGY-001 | 1 | 2 |
| S-STRATEGY-004 | S-STRATEGY-001 | 1 | 3 |
| S-JOURNAL-002 | S-JOURNAL-001 | 1 | 2 |
| S-JOURNAL-003 | S-JOURNAL-001 | 1 | 3 |
| S-STRATEGY-005 | S-STRATEGY-002 | 2 | 3 |
| S-JOURNAL-004 | S-JOURNAL-002, S-JOURNAL-003 | 2 | 3 |
| S-JOURNAL-005 | S-JOURNAL-001, S-JOURNAL-004 | 3 | 4 |
| S-TELEMETRY-001 | E-STRATEGY-LIFECYCLE (all 5 done) | 3 | 4 |
| S-TELEMETRY-002 | E-STRATEGY-LIFECYCLE (all 5 done) | 3 | 4 |
| S-COMPARE-001 | E-JOURNAL-SCHEMA (all 5 done) | 3 | 5 |
| S-AUDIT-001 | E-JOURNAL-SCHEMA (all 5 done) | 3 | 5 |
| S-TELEMETRY-003 | S-TELEMETRY-001 | 4 | 5 |
| S-COMPARE-002 | S-COMPARE-001 | 4 | 6 |
| S-AUDIT-002 | S-AUDIT-001 | 4 | 6 |
| S-TELEMETRY-004 | S-TELEMETRY-001, S-TELEMETRY-002, S-TELEMETRY-003 | 5 | 6 |
| S-COMPARE-003 | S-COMPARE-002 | 5 | 7 |
| S-AUDIT-003 | S-AUDIT-002 | 5 | 7 |
| S-TELEMETRY-005 | S-TELEMETRY-004 | 6 | 6 |
| S-COMPARE-004 | S-COMPARE-003 | 6 | 7 |
| S-COMPARE-005 | S-COMPARE-003 | 6 | 7 |
| S-AUDIT-004 | S-AUDIT-002, S-AUDIT-003 | 6 | 7 |
| S-AUDIT-005 | S-AUDIT-004 | 7 | 7 |

---

## Gate Conditions (Epic-Level Dependencies)

### Gate 1: E-STRATEGY-LIFECYCLE Complete
**Unlocks:** S-TELEMETRY-001, S-TELEMETRY-002
**Required Stories Done:**
- [ ] S-STRATEGY-001
- [ ] S-STRATEGY-002
- [ ] S-STRATEGY-003
- [ ] S-STRATEGY-004
- [ ] S-STRATEGY-005

**Expected Gate Date:** End of Sprint 3 (Week 6)

### Gate 2: E-JOURNAL-SCHEMA Complete
**Unlocks:** S-COMPARE-001, S-AUDIT-001
**Required Stories Done:**
- [ ] S-JOURNAL-001
- [ ] S-JOURNAL-002
- [ ] S-JOURNAL-003
- [ ] S-JOURNAL-004
- [ ] S-JOURNAL-005

**Expected Gate Date:** End of Sprint 4 (Week 8)

---

## Critical Path Analysis

### Path 1: Compare Path (via Journal)
```
S-JOURNAL-001 (8)
  → S-JOURNAL-002 (10)
    → S-JOURNAL-003 (8)   [concurrent with JOURNAL-002, but both needed before JOURNAL-004]
      → S-JOURNAL-004 (8)
        → S-JOURNAL-005 (6)   [JOURNAL complete]
          → S-COMPARE-001 (7)
            → S-COMPARE-002 (5)
              → S-COMPARE-003 (6)
                → S-COMPARE-004 (4)
                → S-COMPARE-005 (3)
```
**Path Length:** 8 stories | **Points:** 65 | **Estimated Duration:** Sprints 1-7

### Path 2: Audit Path (via Journal)
```
S-JOURNAL-001 (8)
  → S-JOURNAL-002 (10)
    → S-JOURNAL-003 (8)
      → S-JOURNAL-004 (8)
        → S-JOURNAL-005 (6)   [JOURNAL complete]
          → S-AUDIT-001 (6)
            → S-AUDIT-002 (7)
              → S-AUDIT-003 (6)
                → S-AUDIT-004 (4)
                  → S-AUDIT-005 (2)
```
**Path Length:** 9 stories | **Points:** 65 | **Estimated Duration:** Sprints 1-7

**LONGEST CRITICAL PATH: Journal → Audit at 9 stories deep (65 points)**

### Path 3: Telemetry Path (via Strategy)
```
S-STRATEGY-001 (13)
  → S-STRATEGY-002 (8)
    → S-STRATEGY-005 (3)  [STRATEGY complete after STRATEGY-003+004]
      → S-TELEMETRY-001 (6)
        → S-TELEMETRY-003 (6)
          → S-TELEMETRY-004 (8)
            → S-TELEMETRY-005 (4)
```
**Path Length:** 7 stories | **Points:** 48 | **Estimated Duration:** Sprints 1-6

---

## Sprint Gate Checklist

### Before Sprint 2 Can Start
- [ ] S-STRATEGY-001 DONE (enables S-STRATEGY-002, S-STRATEGY-003)
- [ ] S-JOURNAL-001 DONE (enables S-JOURNAL-002)

### Before Sprint 3 Can Start
- [ ] S-STRATEGY-002 DONE (enables S-STRATEGY-005)
- [ ] S-JOURNAL-002 DONE (enables S-JOURNAL-004 after S-JOURNAL-003 also done)

### Before Sprint 4 Can Start
- [ ] S-STRATEGY-001 through S-STRATEGY-005 ALL DONE (E-STRATEGY-LIFECYCLE gate)
- [ ] S-JOURNAL-001 AND S-JOURNAL-004 DONE (enables S-JOURNAL-005)

### Before Sprint 5 Can Start
- [ ] E-JOURNAL-SCHEMA ALL DONE (Gate 2: enables S-COMPARE-001, S-AUDIT-001)
- [ ] S-TELEMETRY-001 DONE (enables S-TELEMETRY-003)

### Before Sprint 6 Can Start
- [ ] S-COMPARE-001 DONE (enables S-COMPARE-002)
- [ ] S-AUDIT-001 DONE (enables S-AUDIT-002)
- [ ] S-TELEMETRY-001+002+003 ALL DONE (enables S-TELEMETRY-004)

### Before Sprint 7 Can Start
- [ ] S-COMPARE-002 DONE (enables S-COMPARE-003)
- [ ] S-AUDIT-002 DONE (enables S-AUDIT-003)
- [ ] S-TELEMETRY-004 DONE (enables S-TELEMETRY-005 — may finish in Sprint 6)

---

## Parallel Execution Windows

These story pairs/groups can be executed simultaneously by different team members:

| Window | Parallel Group A | Parallel Group B |
|--------|-----------------|-----------------|
| Sprint 1 | S-STRATEGY-001 | S-JOURNAL-001 |
| Sprint 2 | S-STRATEGY-002, S-STRATEGY-003 | S-JOURNAL-002 |
| Sprint 3 | S-STRATEGY-004, S-STRATEGY-005 | S-JOURNAL-003 then S-JOURNAL-004 |
| Sprint 4 | S-JOURNAL-005, S-TELEMETRY-001 | S-TELEMETRY-002 |
| Sprint 5 | S-TELEMETRY-003, S-AUDIT-001 | S-COMPARE-001 |
| Sprint 6 | S-TELEMETRY-004, S-TELEMETRY-005 | S-COMPARE-002, S-AUDIT-002 |
| Sprint 7 | S-COMPARE-003, S-COMPARE-004, S-COMPARE-005 | S-AUDIT-003, S-AUDIT-004, S-AUDIT-005 |

---

## Blocking Risk Register

| Risk ID | Blocking Story | Blocked Stories | Risk Level | Mitigation |
|---------|---------------|-----------------|------------|------------|
| R-DEP-01 | S-STRATEGY-001 (13 pts) | S-STRATEGY-002, 003, 004 (18 pts) | CRITICAL | Start Sprint 1 immediately; daily check-in |
| R-DEP-02 | S-JOURNAL-004 (dual dependency) | S-JOURNAL-005 | HIGH | Dev B sequences JOURNAL-003 first 3 days of Sprint 3 |
| R-DEP-03 | E-STRATEGY-LIFECYCLE gate | S-TELEMETRY-001, 002 (12 pts) | HIGH | Track epic completion daily in Sprint 3 |
| R-DEP-04 | E-JOURNAL-SCHEMA gate | S-COMPARE-001, S-AUDIT-001 (13 pts) | HIGH | No scope addition to journal epic; complete as planned |
| R-DEP-05 | S-TELEMETRY-001 | S-TELEMETRY-003 | MEDIUM | Telemetry-001 prioritized in Sprint 4 |
| R-DEP-06 | S-COMPARE-003 | S-COMPARE-004, S-COMPARE-005 | MEDIUM | Both depend on same story; schedule 004 and 005 in same sprint |

---

*Generated by BMAD Sprint Planning Workflow*
*Date: 2026-02-26*
