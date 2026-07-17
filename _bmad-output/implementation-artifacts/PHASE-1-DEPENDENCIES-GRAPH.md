# Phase 1 Dependencies Graph & Critical Path Analysis

**Project**: Katana VectorBT Phase 1
**Date**: 2026-02-26
**Purpose**: Execution sequencing, team coordination, critical path identification

---

## SECTION 1: EPIC DEPENDENCY MATRIX

### 1.1 Direct Epic Dependencies

```
DEPENDENCY GRAPH (→ = "blocks" or "enables"):

CRITICAL PATH (Longest):
[E1: STATE MACHINE] (10-16h) → [E3: TELEMETRY] (14-20h)
                    ↓
            [E4: COMPARE] (10-14h)
                    ↓
        [E5: AUDIT TRAIL] (16-22h)

PARALLEL TRACKS:
[E2: SCHEMA] (14-20h) → [E5: AUDIT TRAIL] (16-22h)

TOTAL CRITICAL PATH: E1 + E3 + E4 + E5 = 50-72 hours = 1.25-1.8 weeks
TOTAL CALENDAR TIME: 4-6 weeks (with 3 parallel teams + 2-3 week buffer)
```

### 1.2 Dependency Details

| Epic | Depends On | Blocking | Rationale | Start Date |
|------|-----------|----------|-----------|-----------|
| **E1: STATE MACHINE** | None | E3, E4, E5 | Core state management data | Week 1, Day 1 |
| **E2: SCHEMA** | None | E3, E4, E5 | Data validation gates | Week 1, Day 1 |
| **E3: TELEMETRY** | E1, E2 | E4, E5 | Needs state + schema data | Week 1, after E1 core (Day 3-4) |
| **E4: COMPARE** | E1, E2, E3 | E5 | Diff algorithm needs all data | Week 2, after E1-E3 core |
| **E5: AUDIT TRAIL** | E1, E2, E3, E4 | None | Chain depends on all epics | Week 2, after E1-E4 core |

### 1.3 Parallelization Strategy

**Week 1** (P0 Implementation):
```
Team-1 (Backend-A):    E1 Core    [STATE MACHINE] (Days 1-5)
Team-2 (Backend-B):    E2 Core    [SCHEMA] (Days 1-5) — Parallel with E1
Team-3 (QA):           Framework  [PYTEST + ISOLATION] (Days 1-3)
Team-4 (DevOps):       CI/CD      [GITHUB ACTIONS] (Days 1-2)

After Day 3:
Team-1: E1 → E1 Integration tests (Days 3-5)
Team-3: E1 Unit tests (Days 2-3)
```

**Week 2** (P1 + Dependencies):
```
Team-1 (Backend-A):    E1 Complete → E3 Core  [START TELEMETRY]
Team-2 (Backend-B):    E2 Complete → E3 Core  [START TELEMETRY WITH E1]
Team-3 (DevOps/Perf):  E3 Core                [METRICS INFRASTRUCTURE]
Team-4 (Frontend-A):   E1 Complete → E4 Core  [START COMPARE]

After Day 10:
Team-1-4: Continue E3, E4 in parallel; E5 planning begins
```

**Week 3** (P2 + Polish):
```
Team-1-4: E3-E4 complete → E5 Core  [START AUDIT TRAIL]
QA Team:  18 E2E tests (all epics)
```

---

## SECTION 2: CRITICAL PATH ANALYSIS

### 2.1 Longest Path Calculation

```
CRITICAL PATH SEQUENCE:

E1 (10-16h) STATE MACHINE
├─ Unit tests:        4-6h
├─ Integration tests: 3-4h
├─ E2E tests:         2-3h
├─ Accessibility:     1-2h
└─ Total:             10-16h

E3 (14-20h) TELEMETRY (depends on E1 state data)
├─ Unit tests:        4-5h
├─ Integration tests: 4-6h
├─ E2E + performance: 5-7h
├─ Performance optimization: 1-2h
└─ Total:             14-20h

E4 (10-14h) COMPARE (depends on E1, E2, E3)
├─ Unit tests:        3-4h
├─ Integration tests: 3-4h
├─ E2E tests:         3-4h
├─ Export validation: 1-2h
└─ Total:             10-14h

E5 (16-22h) AUDIT TRAIL (depends on E1, E2, E3, E4)
├─ Unit tests:        4-5h
├─ Integration tests: 3-4h
├─ E2E tests:         4-5h
├─ Crypto validation: 3-4h
├─ Chain reconstruction: 2-3h
└─ Total:             16-22h

CRITICAL PATH TOTAL: 50-72 hours = 1.25-1.8 weeks (single team)
PARALLEL TEAMS:      50-72 hours ÷ 4 teams ≈ 12-18 hours per team = 1.5-2.25 days
CALENDAR TIME:       4-6 weeks (includes integration, testing, contingency)
```

### 2.2 Critical Path Slack Analysis

```
AVAILABLE TIME:     4-6 weeks = 160-240 hours
CRITICAL PATH:      50-72 hours
SLACK BUFFER:       88-190 hours = 2.2-4.75 weeks (!)

BUFFER ALLOCATION:
├─ Team coordination overhead: 10-15h (1 week)
├─ Integration testing gaps: 20-30h (1 week)
├─ WCAG accessibility fixes: 40-50h (1 week)
├─ Performance optimization: 10-15h (0.5 week)
└─ Contingency (unexpected blockers): 20-30h (1 week)

RESULT: Significant buffer available; timeline is realistic and achievable
```

### 2.3 Minimum Viable Timeline

**If All Parallel (Best Case)**:
- Week 1: All unit tests + core implementations
- Week 2: All integration tests + E2E tests
- Week 3: Polish + performance optimization
- **Total: 3 weeks** ← Optimistic (doesn't account for real-world coordination)

**Realistic Timeline (Parallel with Coordination)**:
- Week 1: Core implementations + framework setup
- Week 2: Integration + dependency resolution
- Week 3: E2E + performance + accessibility
- **Total: 3 weeks** ← Still achievable with good coordination

**Conservative Timeline (Includes Contingency)**:
- Week 1-2: Core implementations + integration
- Week 2-3: E2E + performance + accessibility
- Week 4+: Polish + UAT preparation
- **Total: 4-6 weeks** ← Current plan (realistic with buffers)

---

## SECTION 3: TEAM ALLOCATION & CRITICAL PATH MAPPING

### 3.1 Team Assignments per Epic

```
PHASE 1 TEAM STRUCTURE:

┌─────────────────────────────────────────────────────────────┐
│ TEAM BACKEND-A (E-STRATEGY-LIFECYCLE)                       │
├─────────────────────────────────────────────────────────────┤
│ Size: 3 developers                                           │
│ Week 1: E1 core (state machine) + unit tests                │
│ Week 2: E1 integration + E3 core setup                      │
│ Week 3: E3 completion + performance optimization            │
│ Effort: 2-2.5 weeks / 40-50 person-hours                    │
│ Critical Path: YES (blocks E3, E4, E5)                      │
│ Blocker Dependencies: None (E1 is critical path start)      │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ TEAM BACKEND-B (E-JOURNAL-SCHEMA)                           │
├─────────────────────────────────────────────────────────────┤
│ Size: 3 developers                                           │
│ Week 1: E2 core (schema validation) + unit tests            │
│ Week 2: E2 integration + E5 core setup                      │
│ Week 3: E5 completion + audit trail finish                  │
│ Effort: 2-2.5 weeks / 40-50 person-hours                    │
│ Critical Path: PARALLEL (parallel to Backend-A)             │
│ Blocker Dependencies: None (E2 independent)                 │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ TEAM DEVOPS/PERF (E-TELEMETRY-METRICS)                      │
├─────────────────────────────────────────────────────────────┤
│ Size: 2 developers                                           │
│ Week 1: E3 infrastructure + unit tests                      │
│ Week 2: E3 integration (depends on E1 + E2) + performance   │
│ Week 3: Performance tuning + load testing                   │
│ Effort: 2-2.5 weeks / 40-50 person-hours                    │
│ Critical Path: YES (E1 → E3 dependency)                     │
│ Blocker Dependencies: E1 state data (Day 4-5 Week 1)        │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ TEAM FRONTEND-A (E-COMPARE-WORKFLOW)                        │
├─────────────────────────────────────────────────────────────┤
│ Size: 2 developers                                           │
│ Week 1: E1 UI setup + component library                     │
│ Week 2: E4 core (diff algorithm) + integration              │
│ Week 3: E4 completion + UI polish                           │
│ Effort: 1.5-2 weeks / 30-40 person-hours                    │
│ Critical Path: E1 → E4 (UI dependency)                      │
│ Blocker Dependencies: E1 state machine data (Day 4 Week 1)  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ TEAM SECURITY/BACKEND (E-AUDIT-TRAIL)                       │
├─────────────────────────────────────────────────────────────┤
│ Size: 3 developers                                           │
│ Week 1: E5 infrastructure + crypto unit tests               │
│ Week 2: E5 integration (depends on E1-E4) + chain reconstruction │
│ Week 3: E5 completion + reproducibility validation          │
│ Effort: 2-3 weeks / 50-60 person-hours                      │
│ Critical Path: YES (final epic, E1→E3→E4→E5 chain)         │
│ Blocker Dependencies: All epics (E1, E2, E3, E4)           │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ TEAM QA/TESTING (ALL EPICS)                                 │
├─────────────────────────────────────────────────────────────┤
│ Size: 2 QA engineers                                         │
│ Week 1: Framework setup + 42 unit tests                     │
│ Week 2: 26 integration tests + nightly execution            │
│ Week 3: 18 E2E tests + performance baselines                │
│ Effort: 3-4 weeks / 60-80 person-hours                      │
│ Critical Path: YES (test execution enables all)             │
│ Blocker Dependencies: None (parallel with dev)              │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Weekly Team Sync Schedule

**Daily Standup** (09:00 UTC, 5 min per team):
```
Backend-A: "E1 state machine progress, E3 readiness"
Backend-B: "E2 schema progress, E5 readiness"
DevOps/Perf: "E3 infrastructure, performance baselines"
Frontend-A: "E4 diff algorithm, UI integration"
Security: "E5 crypto validation, chain reconstruction"
QA: "Test execution status, coverage metrics"
```

**Weekly Sync** (Thursday 14:00 UTC, 60 minutes):
```
1. Coverage trends (10 min)
2. Blocker resolution (15 min)
3. Critical path status (15 min)
4. Integration points (10 min)
5. Phase 2 planning (10 min)
```

---

## SECTION 4: INTEGRATION POINTS & DATA FLOW

### 4.1 Inter-Epic Data Dependencies

```
DEPENDENCY FLOW DIAGRAM:

┌──────────────────────────────────────────────────────────────┐
│ E1: STATE MACHINE (Week 1-2)                                │
│ Outputs: strategy_state, approval_timestamp, state_history  │
└────┬─────────────────────────────────────────────────────────┘
     │
     ├──→ E3: TELEMETRY (depends on strategy_state)
     │    Calculates metrics based on strategy state
     │    Returns: net_pnl, win_rate, drawdown, time_to_status
     │
     ├──→ E4: COMPARE (depends on strategy_state + E3)
     │    Compares metrics from different states
     │    Returns: diff_report, delta_analysis
     │
     └──→ E5: AUDIT TRAIL (depends on all)
          Validates reproducibility chain
          Returns: chain_integrity, artifact_hashes

┌──────────────────────────────────────────────────────────────┐
│ E2: SCHEMA (Week 1-2)                                        │
│ Outputs: validated_artifacts, schema_gates, data_hashes     │
└────┬─────────────────────────────────────────────────────────┘
     │
     ├──→ E3: TELEMETRY (depends on validated_artifacts)
     │    Reads artifact data for metric calculation
     │
     ├──→ E4: COMPARE (depends on data_hashes)
     │    Uses hashes for reproducibility verification
     │
     └──→ E5: AUDIT TRAIL (depends on all data)
          Validates entire artifact chain

┌──────────────────────────────────────────────────────────────┐
│ E3: TELEMETRY (Week 2-3)                                     │
│ Outputs: dashboard_data, performance_metrics, Time-to-Status │
└────┬─────────────────────────────────────────────────────────┘
     │
     ├──→ E4: COMPARE (depends on performance_metrics)
     │    Compares performance across strategies
     │
     └──→ E5: AUDIT TRAIL (depends on dashboard_data)
          Validates metric computation integrity

┌──────────────────────────────────────────────────────────────┐
│ E4: COMPARE (Week 2-3)                                       │
│ Outputs: comparison_report, diff_metadata, export_artifacts │
└────┬─────────────────────────────────────────────────────────┘
     │
     └──→ E5: AUDIT TRAIL (depends on comparison_report)
          Validates comparison integrity in audit chain

EXECUTION SEQUENCE:
Week 1: E1, E2 cores implemented
Week 2: E1, E2 integration complete; E3, E4 cores start (after E1-E2)
Week 3: E3, E4 integration complete; E5 core starts (after E1-E4)
```

### 4.2 Critical Integration Checkpoints

| Week | Checkpoint | Verification | Owner | Risk |
|------|-----------|---------------|-------|------|
| **1** | E1 unit tests passing | 8/8 tests ✓ | Backend-A | HIGH |
| **1** | E2 unit tests passing | 12/12 tests ✓ | Backend-B | HIGH |
| **1** | E1 state machine integration ready | Data contract ✓ | Backend-A | HIGH |
| **2** | E1 integration tests passing | 5/5 tests ✓ | Backend-A | MEDIUM |
| **2** | E2 integration tests passing | 6/6 tests ✓ | Backend-B | MEDIUM |
| **2** | E3 can access E1 state data | API contract ✓ | DevOps | HIGH |
| **2** | E3 can access E2 artifact data | API contract ✓ | DevOps | HIGH |
| **3** | E4 can access E1-E3 data | API contract ✓ | Frontend | MEDIUM |
| **3** | E5 can access E1-E4 data | API contract ✓ | Security | HIGH |
| **3** | All 86 tests passing | Coverage ≥88% ✓ | QA | CRITICAL |

---

## SECTION 5: RISK & CONTINGENCY PLANNING

### 5.1 Critical Path Risk Mitigation

**Risk 1: E1 State Machine Delay**
```
Impact: Cascades to E3, E4, E5 (all downstream epics blocked)
Probability: High (complexity 9/10)
Mitigation:
├─ 8 unit tests in Week 1 (early detection)
├─ Peer review + code walkthrough
├─ Formal verification of state transitions
├─ Parallel E2 work unaffected
└─ Contingency: Add 1 extra Backend-A engineer if needed
```

**Risk 2: E3 Performance Regression (Time-to-Status >10s)**
```
Impact: Fails critical NFR, blocks Phase 1 success
Probability: Medium (performance testing in Week 3)
Mitigation:
├─ 4 performance tests in E3-E2E (load testing)
├─ Weekly performance baselines
├─ Early optimization in Week 2
├─ Database query optimization
└─ Contingency: Extend Week 3 timeline for tuning
```

**Risk 3: E5 Reproducibility Chain Corruption**
```
Impact: Critical security risk (audit trail invalid)
Probability: Medium (complexity 9/10)
Mitigation:
├─ 8 crypto unit tests in Week 1
├─ 5 chain reconstruction tests in Week 2
├─ 4 E2E reproducibility tests in Week 3
├─ Cross-platform validation
└─ Contingency: Security audit + external verification
```

### 5.2 Contingency Buffers

| Scenario | Buffer | Allocated | Action |
|----------|--------|-----------|--------|
| **1 critical task 1 week late** | 1 week | Available ✓ | Extend critical path by 1 week |
| **2 critical tasks 1 week late** | 2 weeks | Available ✓ | Extend critical path by 2 weeks |
| **Major blocker discovered** | 2-3 weeks | Available ✓ | Pause less critical work, focus on blocker |
| **WCAG accessibility overrun** | 2 weeks | Available ✓ | Defer to Phase 2, keep MVP on track |
| **Database isolation failure** | 1 week | Available ✓ | Fix CI/CD, continue local testing |

---

## SECTION 6: EXECUTION ROADMAP

### 6.1 Week-by-Week Execution Plan

**Week 1: P0 Core Implementation (Feb 27 - Mar 5)**

```
MONDAY (Feb 27) - Kickoff Day
├─ 09:00 UTC: Phase 1 Kickoff (90 min)
│  └─ All teams, stakeholders, team lead confirmations
├─ 10:30 UTC: Team breakout sessions (30 min each)
│  ├─ Backend-A: E1 architecture deep dive
│  ├─ Backend-B: E2 architecture deep dive
│  ├─ DevOps: CI/CD setup + database isolation
│  ├─ Frontend-A: UI component library setup
│  ├─ Security: E5 crypto specification review
│  └─ QA: Test framework + pytest configuration
└─ 12:00 UTC: Development starts

TUESDAY - WEDNESDAY (Feb 28 - Mar 1)
├─ Backend-A: E1 state machine core (3-5 hours)
├─ Backend-B: E2 schema validation (3-5 hours)
├─ QA: 42 unit tests implementation (6-8 hours)
├─ DevOps: GitHub Actions CI/CD setup (2-3 hours)
└─ Daily standup: 09:00 UTC (5 min per team)

THURSDAY (Mar 2) - Weekly Sync
├─ 14:00 UTC: Weekly sync (60 min)
│  ├─ Coverage progress (E1-2 cores 60% done)
│  ├─ Blocker check (none expected)
│  └─ Preview of coming week
├─ Backend-A: E1 integration tests (2-3 hours)
├─ Backend-B: E2 integration tests (2-3 hours)
└─ QA: Unit test validation

FRIDAY (Mar 3) - Status Check
├─ Backend-A: E1 ready for testing (90% complete)
├─ Backend-B: E2 ready for testing (90% complete)
├─ QA: 42 unit tests passing ✓
├─ DevOps: PR gate activated (<15 min)
└─ Team leads confirm readiness for Week 2

WEEK 1 GATES:
├─ ✅ E1 core implementation (10-16h starting)
├─ ✅ E2 core implementation (10-16h starting)
├─ ✅ 42 unit tests passing (100% P0 pass rate)
├─ ✅ PR gate activated + <15 min execution
└─ ✅ Framework setup complete
```

**Week 2: P1 Implementation + Dependencies (Mar 6 - Mar 12)**

```
MONDAY (Mar 6)
├─ Backend-A: E1 integration tests + E3 core kickoff
├─ Backend-B: E2 integration tests + E5 core kickoff
├─ DevOps: E3 telemetry infrastructure setup
├─ Frontend-A: E4 core (diff algorithm)
├─ QA: 26 integration tests implementation
└─ Daily standup: 09:00 UTC

TUESDAY - WEDNESDAY (Mar 7-8)
├─ All teams: Full parallel execution
├─ E1 + E2 integration tests running (nightly)
├─ E3 + E4 + E5 cores being implemented
├─ QA: Integration test execution + validation
└─ Performance baselines started for E3

THURSDAY (Mar 9) - Weekly Sync
├─ 14:00 UTC: Weekly sync (60 min)
│  ├─ Coverage progress (P0+P1 tests 70% done)
│  ├─ Critical path status (on track)
│  ├─ Dependency validation (E1-E2 data flowing)
│  └─ Week 3 planning
├─ Critical path checkpoint
├─ E1-E2 integration complete
├─ E3-E4-E5 cores at 50% (start integration next week)
└─ Nightly execution: 90 min ✓

FRIDAY (Mar 10) - Status Check
├─ Backend-A: E1 complete (100%)
├─ Backend-B: E2 complete (100%)
├─ DevOps: E3 core ready for integration
├─ Frontend-A: E4 core ready for integration
├─ QA: 26 integration tests ≥95% passing
└─ All P0 + P1 tests passing

WEEK 2 GATES:
├─ ✅ E1 complete (100%)
├─ ✅ E2 complete (100%)
├─ ✅ E3-E4-E5 cores implemented (50%)
├─ ✅ 26 integration tests passing (≥95%)
├─ ✅ P0 + P1 coverage ≥92%
└─ ✅ Nightly execution <90 min
```

**Week 3: E2E + Performance + Polish (Mar 13 - Apr 10)**

```
MONDAY (Mar 13)
├─ Backend-A-B: E3-E4-E5 integration + completion
├─ Frontend-A: E4 integration + E2E tests
├─ Security: E5 chain reconstruction
├─ QA: 18 E2E tests implementation + performance testing
└─ WCAG accessibility champion begins (parallel)

TUESDAY - WEDNESDAY (Mar 14-15)
├─ E3-E4-E5 integration tests running
├─ E2E tests being executed (Playwright)
├─ Performance baselines established
├─ WCAG fixes for critical blockers (1-2 fixes)
└─ Code coverage trending toward ≥88%

THURSDAY (Mar 16) - Weekly Sync
├─ 14:00 UTC: Weekly sync (60 min)
│  ├─ Coverage progress (80%+ done)
│  ├─ E3-E4-E5 completion status
│  ├─ Performance metrics (Time-to-Status ≤10s ✓?)
│  └─ WCAG accessibility progress (20-30h used)
├─ Critical path status: E1→E3→E4→E5 nearing complete
├─ Contingency allocation: Used 10-15h so far (good)
└─ E2E execution: 18/18 tests expected passing

FRIDAY - WEDNESDAY (Mar 17 - Apr 2)
├─ Sprint 3 continued execution
├─ All 86 tests targeting ≥88% coverage
├─ Performance optimization (Time-to-Status, MTIF)
├─ WCAG accessibility polish (20-30h continuing)
├─ UAT preparation
└─ Phase 2 planning begins

THURSDAY (Mar 23) - Phase 1 Wrap-Up Sync
├─ 14:00 UTC: Weekly sync (60 min)
│  ├─ Final coverage verification (≥88% target)
│  ├─ Performance validation (SLAs met?)
│  ├─ WCAG remediation status (40-50h allocation)
│  ├─ All 86 tests passing (100% P0, ≥95% P1)
│  └─ Phase 2 kickoff planning
├─ All core features complete
├─ Performance baselines established
├─ WCAG accessibility phase 1 complete
└─ UAT prep: test cases + team training

WEEK 3+ GATES:
├─ ✅ E1-E2-E3-E4-E5 complete (100%)
├─ ✅ All 18 E2E tests passing
├─ ✅ All 86 tests passing (≥88% coverage)
├─ ✅ Performance SLAs met (Time-to-Status ≤10s)
├─ ✅ WCAG accessibility phase 1 complete (Lighthouse ≥90)
├─ ✅ UAT preparation complete
└─ ✅ Phase 1 READY FOR UAT + Phase 2 kickoff
```

### 6.2 Phase 1 Success Criteria Timeline

| Criteria | Week 1 | Week 2 | Week 3 | Final Status |
|----------|--------|--------|--------|------------|
| E1 (state machine) | 50% | 100% | 100% | ✅ Complete |
| E2 (schema) | 50% | 100% | 100% | ✅ Complete |
| E3 (telemetry) | 20% | 50% | 100% | ✅ Complete |
| E4 (compare) | 20% | 50% | 100% | ✅ Complete |
| E5 (audit trail) | 20% | 50% | 100% | ✅ Complete |
| Unit tests (42) | 100% | 100% | 100% | ✅ 42/42 |
| Integration tests (26) | 50% | 100% | 100% | ✅ 26/26 |
| E2E tests (18) | 20% | 50% | 100% | ✅ 18/18 |
| Code coverage | 85% | ≥85% | ≥88% | ✅ 88% |
| Performance SLAs | — | Testing | ✓ Met | ✅ Pass |
| WCAG accessibility | — | 30% | 100% | ✅ Complete |

---

## CONCLUSION

**Phase 1 critical path is well-defined and achievable.**

- Longest path: E1 → E3 → E4 → E5 (50-72 hours)
- Available calendar: 4-6 weeks (160-240 hours)
- Slack buffer: 2-4 weeks (88-190 hours)
- Risk profile: All 6 critical risks mitigated by test coverage

**Team coordination is essential** - daily standups + weekly syncs ensure data flow between epics.

**Go/No-Go Decision**: ✅ **PROCEED WITH PHASE 1** (2026-02-27 09:00 UTC)

---
