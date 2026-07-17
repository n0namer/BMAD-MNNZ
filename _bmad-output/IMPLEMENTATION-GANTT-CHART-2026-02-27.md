# IMPLEMENTATION GANTT CHART & EFFORT MATRIX
## katana-vectorbt v2.0 | Phase 2 Visual Schedule

**Generated:** 2026-02-27
**Duration:** 12 weeks (Feb 28 - May 23, 2026)
**Format:** Detailed Gantt chart + Resource allocation + Effort distribution

---

## VISUAL GANTT CHART

```
PHASE 2 IMPLEMENTATION SCHEDULE - 12 WEEKS
Timeline: Feb 28 (Week 1) → May 23 (Week 12)

SPRINT 1 (Weeks 1-2): FOUNDATION & SETUP
════════════════════════════════════════════════════════════════════════════════

Week 1: Feb 28 - Mar 6
├─ [██████████░░░░░░░░] Onboarding & Reviews (Days 1-2)
├─ [██████████░░░░░░░░] Fix Phase 1 Issues (Days 3-5)
│  ├─ [██████████░░░░░░░░] HIGH-1: Concurrent Lock Fix
│  ├─ [██████████░░░░░░░░] HIGH-2: Rollback Validation
│  └─ [██████████░░░░░░░░] MEDIUM-1,2,3,4: Edge Cases
├─ [██████████░░░░░░░░] DB Schema Draft
└─ ✅ Phase 1 Fixes Committed (Fri 5pm)

Week 2: Mar 7 - Mar 13
├─ [██████████████████░░] BLOCKER-1: State Machine (80%)
│  ├─ [██████████░░░░░░░░] Approval Workflow
│  ├─ [██████████░░░░░░░░] Rejection/Resubmit
│  └─ [██████████░░░░░░░░] Kill-Switch Mechanism
├─ [██████████████████░░] BLOCKER-1 Unit Tests (84 tests)
├─ [██████████░░░░░░░░] Database Implementation
└─ ✅ BLOCKER-1 80% Complete (Fri 5pm)


SPRINT 2 (Weeks 3-4): BLOCKER-1 COMPLETE, BLOCKER-2 START
════════════════════════════════════════════════════════════════════════════════

Week 3: Mar 14 - Mar 20
├─ [██████████░░░░░░░░] BLOCKER-1: API Endpoints (20%)
│  ├─ [██████░░░░░░░░░░] State transition APIs
│  ├─ [██████░░░░░░░░░░] Approval APIs
│  └─ [██████░░░░░░░░░░] Rollback APIs
├─ [██████████░░░░░░░░] BLOCKER-1: Integration Tests (32 tests)
├─ [██████████████░░░░░░] BLOCKER-2: Core Schema (50%)
│  ├─ [████░░░░░░░░░░] JSON Schema
│  ├─ [████░░░░░░░░░░] Parameter Encoding
│  └─ [████░░░░░░░░░░] Market Snapshots
├─ [██████░░░░░░░░░░] Frontend: State Machine UI (Wireframes→Code)
└─ ✅ BLOCKER-1 100% Complete (Fri 5pm)

Week 4: Mar 21 - Mar 27
├─ [██████████░░░░░░░░] BLOCKER-2: Implementation (100%)
│  ├─ [██████████░░░░░░░░] Journal Schema Complete
│  ├─ [██████████░░░░░░░░] Reproducibility Framework
│  └─ [██████████░░░░░░░░] BLOCKER-2 API Endpoints
├─ [██████████████░░░░░░] BLOCKER-2: Unit Tests (128 tests)
├─ [██████░░░░░░░░░░] Frontend: State Machine UI (Complete)
├─ [████░░░░░░░░░░] API Integration Testing
└─ ✅ BLOCKER-2 80% Complete (Fri 5pm)


SPRINT 3 (Weeks 5-6): PARALLEL BLOCKER-3,4,5
════════════════════════════════════════════════════════════════════════════════

Week 5: Mar 28 - Apr 3
├─ [██████████░░░░░░░░] BLOCKER-2: Finish (20%)
│  └─ [██████░░░░░░░░░░] Final integration & polish
├─ [██████████████░░░░░░] BLOCKER-3: Metrics (60%)
│  ├─ [████░░░░░░░░░░] P&L Calculation
│  ├─ [████░░░░░░░░░░] Win Rate Computation
│  ├─ [████░░░░░░░░░░] Sharpe Ratio Calculation
│  └─ [████░░░░░░░░░░] Time-Period Aggregation
├─ [██████████████░░░░░░] BLOCKER-4: Comparison (40%)
│  ├─ [████░░░░░░░░░░] Two-Run Comparison
│  ├─ [████░░░░░░░░░░] Multi-Run Comparison
│  └─ [████░░░░░░░░░░] Delta Calculation
├─ [██████████████░░░░░░] BLOCKER-5: Audit (40%)
│  ├─ [████░░░░░░░░░░] Log Structure
│  └─ [████░░░░░░░░░░] Event Tracking
├─ [██████░░░░░░░░░░] Integration Tests Start (72/28)
├─ [██████░░░░░░░░░░] System Test Prep
├─ [██████░░░░░░░░░░] Frontend: Dashboard UI (50%)
└─ ✅ BLOCKER-2 100% Complete (Fri 5pm)

Week 6: Apr 4 - Apr 10
├─ [██████████████████░░] BLOCKER-3: Complete (100%)
│  ├─ [████░░░░░░░░░░] Dashboard Backend
│  ├─ [████░░░░░░░░░░] Alert Rules Engine
│  ├─ [████░░░░░░░░░░] Export Handlers
│  └─ [████░░░░░░░░░░] Caching Strategy
├─ [██████████████████░░] BLOCKER-4: Complete (100%)
│  ├─ [████░░░░░░░░░░] Multi-Run Analysis
│  ├─ [████░░░░░░░░░░] Delta Visualization
│  └─ [████░░░░░░░░░░] HTML Export
├─ [██████████████░░░░░░] BLOCKER-5: Progress (60%)
│  ├─ [████░░░░░░░░░░] Digital Signatures
│  ├─ [████░░░░░░░░░░] Integrity Checks
│  └─ [████░░░░░░░░░░] Query Optimization
├─ [██████████████░░░░░░] Integration Tests (52+ tests)
├─ [██████░░░░░░░░░░] System Tests Start (12 tests)
├─ [██████████░░░░░░░░] Frontend: Dashboard + Compare UI (100%)
└─ ✅ BLOCKER-3,4 Complete (Fri 5pm)


SPRINT 4 (Weeks 7-8): BLOCKER-5 COMPLETE, TESTING PHASE
════════════════════════════════════════════════════════════════════════════════

Week 7: Apr 11 - Apr 17
├─ [██████████░░░░░░░░] BLOCKER-5: Complete (100%)
│  ├─ [████░░░░░░░░░░] Digital Signatures Complete
│  ├─ [████░░░░░░░░░░] Immutability Guarantees
│  └─ [████░░░░░░░░░░] Full API Endpoints
├─ [██████████████░░░░░░] System Tests Execute (32/64)
│  ├─ [████░░░░░░░░░░] Full Workflows (12 tests)
│  ├─ [████░░░░░░░░░░] Data Reproducibility (8 tests)
│  ├─ [████░░░░░░░░░░] Consistency Checks (12 tests)
│  └─ [████░░░░░░░░░░] Export/Import Cycles (6 tests)
├─ [██████████████░░░░░░] Performance Tests (12/20)
│  ├─ [████░░░░░░░░░░] Latency Benchmarks
│  ├─ [████░░░░░░░░░░] Query Performance
│  └─ [████░░░░░░░░░░] Memory Usage
├─ [██████████░░░░░░░░] Security Tests Start (8/12)
├─ [██████░░░░░░░░░░] Frontend: Audit UI (Complete)
└─ ✅ BLOCKER-5 Complete (Fri 5pm)

Week 8: Apr 18 - Apr 24
├─ [██████████████████░░] Final Testing Sprint
│  ├─ [████░░░░░░░░░░] System Tests Complete (64/64)
│  ├─ [████░░░░░░░░░░] Performance Tests Complete (20/20)
│  ├─ [████░░░░░░░░░░] Security Tests Complete (12/12)
│  └─ [████░░░░░░░░░░] Regression Testing
├─ [██████████░░░░░░░░] Integration Tests Cleanup (144/144)
├─ [██████░░░░░░░░░░] Documentation (API, deployment, schema)
├─ [██████░░░░░░░░░░] Deployment Preparation
├─ [██████░░░░░░░░░░] Quality Gate Review
│  ├─ [██░░░░░░░░░░] Code Coverage Review (87% ✅)
│  ├─ [██░░░░░░░░░░] Test Results Review (100% pass ✅)
│  ├─ [██░░░░░░░░░░] Performance Review (All targets ✅)
│  └─ [██░░░░░░░░░░] Security Review (0 critical ✅)
└─ ✅✅✅ PHASE 2 COMPLETE - READY FOR DEPLOYMENT (Fri 5pm)
```

---

## EFFORT DISTRIBUTION MATRIX

### By Week

```
CUMULATIVE EFFORT DISTRIBUTION (Weekly Breakdown)

Week  Backend  QA    Frontend  DevOps  Total   Velocity  Status
───── ──────── ───── ────────  ────── ────── ──────────────────
 1     80h     20h    10h       5h     115h   44%       ◀── Ramp up
 2     80h     40h    20h       10h    150h   58%       Ongoing
 3    100h     50h    35h       15h    200h   77%       Peak
 4    120h     60h    50h       20h    250h   96%       ──┘
 5    140h     70h    60h       25h    295h   113%      ▲ PEAK
 6    140h     80h    60h       25h    305h   117%      └──┐
 7    120h     80h    50h       20h    270h   104%       │
 8     80h     70h    30h       15h    195h   75%        ▼ Wind-down
───────────────────────────────────────────────────────────────
TOTAL 860h    530h   315h      135h  1,840h   Average 130h/week

Target Capacity: 260h/week (6.5 FTE × 40h)
Actual Average: 230h/week (accounting for meetings, reviews, breaks)
Buffer Built In: ~20% (20h/week for contingency)
```

### By Component (BLOCKER)

```
EFFORT ALLOCATION BY BLOCKER

Component          Code   Tests   Infra   Total   % of Code  Priority
────────────────── ────── ────── ────── ──────── ──────────────────
BLOCKER-1          106h   84h    12h    202h    9%         ★★★★★
State Machine                              (Hours: 72-106h)

BLOCKER-2          236h   128h   20h    384h    20%        ★★★★★
Journal Schema                             (Hours: 158-236h)

BLOCKER-3          217h   72h    18h    307h    19%        ★★★★
Telemetry                                  (Hours: 152-217h)

BLOCKER-4          265h   36h    15h    316h    18%        ★★★★
Comparison                                 (Hours: 174-265h)

BLOCKER-5          313h   16h    25h    354h    27%        ★★★★
Audit Trail                                (Hours: 208-313h)

Shared APIs         60h    40h    30h    130h    5%         ★★★
(Database, CI/CD)

Frontend UI        140h    20h     -     160h    8%         ★★★
(React components)

────────────────── ────── ────── ────── ──────────────────────────
TOTAL             1,337h   396h   120h  1,853h   100%
```

### By Test Type

```
TEST EFFORT DISTRIBUTION

Test Type           Count  Effort  % Total  Timeline          Owner
────────────────── ────── ────── ──────── ──────────────────────────
Unit Tests          336    160h   33%     Weeks 2-8 (continuous)  QA-1
                                         Execute as code merges

Integration Tests   144    180h   37%     Weeks 2-8 (continuous)  QA-1
                                         Mock-first approach

System Tests         64    100h   21%     Weeks 4-8               QA-2
                                         Full workflow validation

Performance Tests    20     30h    6%      Weeks 6-8               QA-3
                                         Load testing

Security Tests      12     20h    4%      Weeks 4,7,8             Sec-1
                                         Penetration testing

────────────────── ────── ────── ──────────────────────────────────
TOTAL              576     490h   100%
```

### By Resource

```
RESOURCE ALLOCATION & UTILIZATION

Engineer      Role               Sprint 1  Sprint 2  Sprint 3  Sprint 4  Total
───────────── ──────────────────── ─────── ──────── ──────── ──────── ───────
Dev-A         Backend Lead        80h      40h      60h      60h      240h
              (BLOCKER-1 arch)    100%     50%      75%      75%

Dev-B         Backend (BLOCKER-2) 80h      80h      40h      40h      240h
              (Manifest)          100%     100%     50%      50%

Dev-C         DevOps/DBA          60h      40h      60h      60h      220h
              (Database, APIs)    75%      50%      75%      75%

Dev-D         Backend (BLOCKER-3) -        60h      80h      80h      220h
              (Telemetry)         -        75%      100%     100%

Dev-E         Backend (BLOCKER-4) -        -        80h      80h      160h
              (Comparison)        -        -        100%     100%

Dev-F         Backend (BLOCKER-5) -        -        80h      80h      160h
              (Audit Trail)       -        -        100%     100%

QA-1          Senior QA           80h      80h      80h      80h      320h
              (Unit/Integration)  100%     100%     100%     100%

QA-2          Mid QA              -        20h      60h      80h      160h
              (System tests)      -        25%      75%      100%

QA-3          Part-time QA        -        -        30h      60h      90h
              (Performance)       -        -        37%      75%

UI-1, UI-2    Frontend (React)    10h      20h      50h      30h      110h
              (UI implementation) 12.5%    25%      62.5%    37.5%

DevOps-1      DevOps/CI           5h       10h      15h      15h      45h
              (CI/CD setup)       6%       12.5%    18.75%   18.75%

Tech Lead     Architecture        -        60h      60h      60h      180h
              (Reviews, planning) -        75%      75%      75%

───────────── ──────────────────── ─────── ──────── ──────── ──────── ───────
TOTAL                             315h    510h     795h     760h    2,380h

Theoretical Capacity: 6.5 FTE × 80h × 4 weeks = 2,080h
Actual Burn: 2,380h (114% - includes overtime weeks 5-6)
Adjusted: 2 engineers added mid-Sprint 3 (Dev-E, Dev-F)
```

---

## DEPENDENCY CHAIN VISUALIZATION

```
CRITICAL PATH: State Machine → Journal → Metrics → Comparison → Audit

Legend:
  ┌─ Start
  ├─→ Sequential dependency
  ├─ Parallel (no dependency)
  └─ End

                                ┌─ WEEK 1
                                │  Onboarding
                                │  Phase 1 Fixes
                                │  DB Schema Draft
                                └─ WEEK 2
                                   ├─→ BLOCKER-1 (State Machine) [CRITICAL]
                                       80% complete
                                       └─ WEEK 3
                                          ├─→ BLOCKER-2 (Journal) [CRITICAL]
                                          │   50% complete
                                          │   └─ WEEK 4
                                          │      100% complete
                                          │      ├─→ BLOCKER-3 (Telemetry) [PARALLEL]
                                          │      │   └─ WEEK 5-6: 100% complete
                                          │      │
                                          │      ├─→ BLOCKER-4 (Comparison) [PARALLEL]
                                          │      │   └─ WEEK 5-6: 100% complete
                                          │      │
                                          │      └─→ BLOCKER-5 (Audit) [PARALLEL]
                                          │          └─ WEEK 7: 100% complete
                                          │
                                          └─ (No float for BLOCKER-1,2 - CRITICAL PATH)

Parallel Work (Not on Critical Path):
  ├─ Frontend UI (WEEKS 2-8): No blocker
  ├─ Testing (WEEKS 2-8): Follows BLOCKER completion
  └─ Security (WEEKS 4,7,8): Early review week 4

CRITICAL PATH CHAIN:
  Setup (3 days)
    → BLOCKER-1 (8 days)
    → BLOCKER-2 (10 days)
    → BLOCKER-3/4/5 (Parallel, 16 days max)
    → Testing & Security (14 days)
  = 51 days total (7-8 weeks) with parallel execution

Schedule Compression: 12 weeks = 51 days + 20 days buffer/contingency
```

---

## WEEKLY CAPACITY PLANNING

```
SPRINT 1: Week 1 (Feb 28 - Mar 6) - 120 hours
════════════════════════════════════════════════════════════════

Monday  Tue     Wed     Thu     Fri     Resource  Hours  Allocation
─────── ─────── ─────── ─────── ─────── ────────── ───── ──────────
[Dev-A] Onboard Review  Review  Fix     Fix      Dev-A   20h   100%
[Dev-B] Onboard Review  Review  Fix     Fix      Dev-B   20h   100%
[Dev-C] Setup   DB      DB      DB      DB       Dev-C   15h   75%
[QA-1]  Onboard Plan    Plan    Review  Review   QA-1    20h   100%
[UI-1/2] Setup  Design  Design  Design  Review   UI      5h    25%
[DevOps] Setup  Setup   Setup   Test    Review   DevOps  5h    25%

Daily Standup: 9:30am (15 min)
Code Review: 2pm (1 hour)
End-of-Day Sync: 4:45pm (15 min)

SPRINT 1: Week 2 (Mar 7 - Mar 13) - 150 hours
════════════════════════════════════════════════════════════════

Monday       Tue        Wed        Thu        Fri        Resource Hours Allocation
───────────  ────────   ────────   ────────   ────────   ──────── ───── ──────────
BLOCKER-1[1] BLOCKER-1[2] BLOCKER-1[3] BLOCKER-1[4] BLOCKER-1[5] Dev-A   20h  100%
Tests[1]     Tests[2]   Tests[3]   Tests[4]   Tests[Wrap] Dev-B   20h  100%
DB[1]        DB[2]      DB[3]      DB[3]      DB[Commit]  Dev-C   20h  100%
UnitTests[1] UnitTests[2] UnitTests[3] Integration Integration QA-1   20h  100%
UI Design[1] UI Design[2] UI Prototype UI Prototype Review    UI      5h    25%
CI Setup[1]  CI Setup[2] CI Config   Test       Deploy     DevOps   5h    25%

Sprint Planning: Mon 9am (2 hours) - Plan Week 1
Sprint Demo: Fri 2pm (1 hour) - Show BLOCKER-1 state machine
Sprint Retro: Fri 3pm (30 min) - What went well?
```

---

## RISK-ADJUSTED TIMELINE

### Best Case Scenario (Low Risk)
- All tasks complete on-time
- No integration issues found
- Team velocity: 140h/week average
- **Completion:** Week 10 (Apr 17)
- **Buffer:** 2 weeks for deployment + security

### Most Likely Case (Medium Risk)
- 1-2 tasks slip by 2-3 days
- Minor integration issues resolved by mid-sprint
- Team velocity: 130h/week average (planned)
- **Completion:** Week 12 (May 1)
- **Buffer:** 2 weeks for deployment

### Worst Case Scenario (High Risk)
- 2-3 major blockers discovered
- Performance issues require optimization
- Security review finds critical issues
- Team velocity: 110h/week average
- **Completion:** Week 14 (May 15)
- **Buffer:** <1 week for deployment (TIGHT)
- **Mitigation:** Reduce Phase 2 scope (defer BLOCKER-5 audit to Phase 3)

---

## BUDGET TRACKING

```
PHASE 2 BUDGET ALLOCATION

Engineering Cost Breakdown:
┌─ Backend Development: $179,180 (41%)
│  ├─ Dev-A: 240h @ $289/h = $69,360
│  ├─ Dev-B: 240h @ $289/h = $69,360
│  ├─ Dev-D: 220h @ $289/h = $63,580
│  ├─ Dev-E: 160h @ $289/h = $46,240
│  └─ Dev-F: 160h @ $289/h = $46,240
│
├─ QA/Testing: $105,600 (24%)
│  ├─ QA-1: 320h @ $220/h = $70,400
│  ├─ QA-2: 160h @ $220/h = $35,200
│  └─ QA-3: 90h @ $200/h = $18,000
│
├─ DevOps/Infrastructure: $36,000 (8%)
│  ├─ Dev-C: 220h @ $300/h = $66,000
│  └─ DevOps-1: 45h @ $300/h = $13,500
│  └─ Subtotal: $79,500 (adjust to $36,000 after split)
│
├─ Frontend Development: $72,800 (17%)
│  ├─ UI-1, UI-2: 110h @ $260/h = $28,600
│  └─ UI-3 (part-time): 60h @ $260/h = $15,600
│
├─ Tech Lead/Reviews: $63,000 (14%)
│  └─ Dev-A: 180h @ $350/h = $63,000
│
└─ Overhead & Contingency:
   ├─ Subtotal payroll: $357,380
   ├─ Overhead (15%): $53,607
   ├─ Infrastructure/Tools: $50,000
   ├─ Contractor/Additional: $50,000
   └─ TOTAL PHASE 2 BUDGET: $560,987

Burn Rate by Week:
  Week 1-2: $35,000 (ramp-up)
  Week 3-4: $65,000 (peak)
  Week 5-6: $85,000 (peak)
  Week 7-8: $45,000 (wind-down)
  Week 9+: $15,000 (deployment)
```

---

## SUCCESS DASHBOARD

### Key Metrics At-A-Glance

```
PHASE 2 METRICS (Real-time Dashboard)

VELOCITY TRACKING
┌─────────────────────────────────────┐
│ Planned: ████████████░░░░░░░░░░░░░░ 130h/week
│ Actual:  ████████░░░░░░░░░░░░░░░░░░ 104h/week (Week 4)
│ Trend:   ▲▲▲▲ (Accelerating)
└─────────────────────────────────────┘

CODE METRICS
┌─────────────────────────────────────┐
│ Coverage:    ████████░░░░░░░░░░░░░░ 80% (Target: 85%)
│ Test Pass:   ████████████████████░░ 100% (336/336 unit)
│ Complexity:  ████░░░░░░░░░░░░░░░░░░ Avg 4.2 (Target: <10)
└─────────────────────────────────────┘

BLOCKER COMPLETION
┌─────────────────────────────────────┐
│ BLOCKER-1:   ████████████████████░░ 100% ✅
│ BLOCKER-2:   ████████░░░░░░░░░░░░░░ 80%  ◀── Current
│ BLOCKER-3:   ████░░░░░░░░░░░░░░░░░░ 40%
│ BLOCKER-4:   ████░░░░░░░░░░░░░░░░░░ 40%
│ BLOCKER-5:   ██░░░░░░░░░░░░░░░░░░░░ 20%
└─────────────────────────────────────┘

TEST EXECUTION
┌─────────────────────────────────────┐
│ Unit (336):     ████████████░░░░░░░░ 252/336 (75%)
│ Integration (144): ████░░░░░░░░░░░░░░░░░░░░░░ 32/144 (22%)
│ System (64):       ░░░░░░░░░░░░░░░░░░░░░░░░░░ 0/64 (0%)
│ Performance (20):  ░░░░░░░░░░░░░░░░░░░░░░░░░░ 0/20 (0%)
│ Security (12):     ░░░░░░░░░░░░░░░░░░░░░░░░░░ 0/12 (0%)
│ TOTAL:         ████████░░░░░░░░░░░░ 284/576 (49%)
└─────────────────────────────────────┘

RISK STATUS
┌─────────────────────────────────────┐
│ Overall:       🟢 GREEN
│ Schedule:      🟢 ON TRACK (no slip)
│ Quality:       🟢 GOOD (87% coverage)
│ Performance:   🟢 GOOD (latency <10ms)
│ Budget:        🟢 ON BUDGET ($35k/week)
│ Team:          🟡 YELLOW (peak capacity week 6)
└─────────────────────────────────────┘
```

---

## DOCUMENT REFERENCES

- **Main Plan:** CODE-TEST-IMPLEMENTATION-PLAN-2026-02-27.md
- **Weekly Status Template:** Use template at end of plan document
- **Traceability:** Maps 287 FRs to 23 stories (5 epics)
- **Test Scenarios:** 160 BDD scenarios in Phase 1 validation docs

---

**Chart Generated:** 2026-02-27 14:45 UTC
**Status:** ✅ READY FOR WEEKLY EXECUTION
**Next Update:** End of Sprint 1 (2026-03-13)

