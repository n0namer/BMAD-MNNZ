# CODE-TEST IMPLEMENTATION PLAN: 2x EXPANSION
## katana-vectorbt v2.0 | Phase 2 Extended (20 weeks)

**Generated:** 2026-02-27
**Status:** ✅ IMPLEMENTATION READY
**Scope:** 574 atomic FRs (2x expansion) + 350+ user stories + 13 FTE team consideration
**Duration:** 20 weeks (Feb 28 - Jul 18, 2026)
**Recommended Team Capacity:** 6.5 FTE × 20 weeks = 6,500 hours
**Alternative:** 13 FTE × 12 weeks = 6,240 hours (faster delivery, higher cost)

---

## EXECUTIVE SUMMARY

This plan extends the Phase 2 implementation to cover **2x the original scope** while maintaining team stability at 6.5 FTE. The extended 20-week timeline allows for:

1. **Comprehensive feature expansion** from 287 FRs → 574 FRs
2. **Enhanced quality gates** with 350+ user stories and iterative validation
3. **Sustainable pace** avoiding team burnout (40 SP/week/person instead of 80+)
4. **Parallel epic execution** in 10 sprints of 2 weeks each
5. **Risk mitigation** with 4-week buffer for unforeseen issues

### Key Metrics Comparison

| Metric | Option A (13 FTE, 12w) | Option B (6.5 FTE, 20w) | Recommendation |
|--------|------------------------|------------------------|-----------------|
| **Team Size** | 13 FTE | 6.5 FTE | ✅ B (cost-effective) |
| **Duration** | 12 weeks | 20 weeks | ✅ B (sustainable) |
| **Velocity** | 33 SP/week/person | 40 SP/week/person | ✅ B (realistic) |
| **Total Hours** | 6,240 | 6,500 | Comparable |
| **Estimated Cost** | $960K | $950K | ✅ B (cheaper) |
| **Context Switching** | HIGH (10-12 parallel epics) | MEDIUM (2-3 parallel) | ✅ B (efficiency) |
| **Quality Risk** | MEDIUM (tight schedule) | LOW (sustainable pace) | ✅ B (quality) |

### Why Option B (6.5 FTE, 20 weeks) is Recommended

**Advantages:**
- ✅ Team continuity - no hiring/onboarding overhead
- ✅ Code quality - time for refactoring and testing
- ✅ Knowledge preservation - maintains team expertise
- ✅ Cost efficiency - $950K vs $960K for 13 FTE
- ✅ Risk mitigation - 4-week buffer for issues
- ✅ Sustainable velocity - 40 SP/week reasonable for 6.5 FTE
- ✅ Better testing coverage - 350+ stories includes comprehensive QA

**Success Criteria:**
- ✅ All 574 FRs implemented and integrated
- ✅ All 350+ stories completed with full documentation
- ✅ 576+ test cases passing (>95% pass rate)
- ✅ Code coverage ≥85% across all modules
- ✅ Performance targets met (<100ms queries, <10ms state transitions)
- ✅ Security audit complete (zero critical findings)
- ✅ Zero critical production blockers at launch

---

## PART 1: SCOPE EXPANSION (287 FRs → 574 FRs)

### 1.1 Feature Requirement Expansion Map

#### **Phase 1 (Original 287 FRs)**

| Category | Original FRs | Complexity | Hours |
|----------|------------|-----------|-------|
| Trivial (CRUD, formatters) | 25 | 0.5h each | 12.5 |
| Easy (basic logic, schemas) | 78 | 2-3h each | 175 |
| Medium (algorithms, workflows) | 126 | 4-6h each | 570 |
| Hard (optimization, security) | 58 | 8-12h each | 580 |
| **Original Subtotal** | **287** | - | **1,337.5** |

#### **Phase 2 Expansion (Additional 287 FRs - 2x scaling)**

**Expansion Areas:**

1. **Multi-Framework Support** (+87 FRs, 624 hours)
   - TensorFlow 2.x implementation (28 FRs) - 210h
   - PyTorch execution layer (22 FRs) - 165h
   - JAX/NumPy optimization (18 FRs) - 135h
   - Framework abstraction layer (19 FRs) - 114h

2. **Advanced Parameterization** (+68 FRs, 544 hours)
   - Dynamic parameter profiles (24 FRs) - 192h
   - Sensitivity analysis engine (20 FRs) - 160h
   - Parameter optimization workflows (24 FRs) - 192h

3. **Rocket Portfolio Features** (+56 FRs, 448 hours)
   - Multi-asset portfolio support (18 FRs) - 144h
   - Portfolio-level metrics (16 FRs) - 128h
   - Sector/category analysis (22 FRs) - 176h

4. **Advanced Persistence** (+42 FRs, 336 hours)
   - HNSW vector indexing (16 FRs) - 128h
   - Time-series database optimization (15 FRs) - 120h
   - Persistent caching layer (11 FRs) - 88h

5. **Risk Management Framework** (+34 FRs, 272 hours)
   - Risk metrics calculation (12 FRs) - 96h
   - Drawdown analysis (10 FRs) - 80h
   - VaR/CVaR computation (12 FRs) - 96h

| Expansion Area | New FRs | Complexity | Hours | Weeks (1 eng) |
|----------------|---------|-----------|-------|---------------|
| Multi-TF Support | 87 | Medium-Hard | 624 | 12.5 |
| Parameterization | 68 | Medium-Hard | 544 | 10.8 |
| Rocket Portfolio | 56 | Medium | 448 | 9 |
| Persistence | 42 | Medium-Hard | 336 | 6.7 |
| Risk Management | 34 | Hard | 272 | 5.4 |
| **Expansion Subtotal** | **287** | - | **2,224** | **44.4** |

**Total for 2x Plan: 574 FRs, 3,561.5 hours**

---

### 1.2 BLOCKER Expansion (5 → 13 BLOCKERs)

#### **Original BLOCKERs (Weeks 1-12)**

| BLOCKER | Epic | Stories | FRs | Hours | Weeks (2 eng) |
|---------|------|---------|-----|-------|---------------|
| 1 | STRATEGY-LIFECYCLE | 5 | 23 | 90 | 2.25 |
| 2 | BACKTEST-METADATA | 6 | 48 | 197 | 2.5 |
| 3 | TELEMETRY | 4 | 54 | 185 | 2.3 |
| 4 | COMPARISON | 4 | 42 | 220 | 2.75 |
| 5 | AUDIT | 4 | 46 | 260 | 3.25 |
| **Original Total** | **5** | **23** | **213** | **952** | **13.1** |

#### **New BLOCKERs (Expansion)**

| BLOCKER | Epic | Stories | FRs | Hours | Focus Area |
|---------|------|---------|-----|-------|-----------|
| 6 | MULTI-TF-EXECUTION | 8 | 87 | 624 | TensorFlow/PyTorch/JAX execution |
| 7 | DFF-PARAMETERIZATION | 12 | 68 | 544 | Dynamic parameter profiles + sensitivity |
| 8 | CALENDAR-SAFETY | 6 | 24 | 192 | Calendar safety + utilities |
| 9 | ROCKET-PORTFOLIO | 10 | 56 | 448 | Multi-asset portfolio framework |
| 10 | HNSW-PERSISTENCE | 6 | 42 | 336 | Vector indexing + caching |
| 11 | RISK-MANAGEMENT | 8 | 34 | 272 | Risk metrics + analysis |
| 12 | EXECUTION-SCALABILITY | 9 | 42 | 336 | Performance optimization + concurrency |
| 13 | INTEGRATION-POLISH | 14 | 28 | 224 | API integration + documentation + polish |
| **New Total** | **8** | **73** | **361** | **2,876** | - |

**Grand Total: 13 BLOCKERs, 96 stories, 574 FRs, 3,828 hours**

---

## PART 2: 20-WEEK SPRINT ROADMAP

### 2.1 Sprint Structure (10 Sprints × 2 weeks)

```
Sprint 1-2 (Weeks 1-4): Foundations & State Machine [CRITICAL PATH]
├─ BLOCKER-1 completion (State Machine - weeks 1-2)
├─ BLOCKER-2 start (Journal Schema - weeks 2-4)
├─ BLOCKER-6 infrastructure (Multi-TF framework setup - weeks 3-4)
└─ Validation gates + code review

Sprint 3-4 (Weeks 5-8): Core Systems & Parameterization
├─ BLOCKER-2 completion (Journal - week 5)
├─ BLOCKER-3 start (Telemetry - weeks 5-7)
├─ BLOCKER-7 start (DFF Parameterization - weeks 5-8)
└─ Integration testing

Sprint 5-6 (Weeks 9-12): Parallel Build - Portfolio & Persistence
├─ BLOCKER-3 completion (Telemetry - week 9)
├─ BLOCKER-4 (Comparison - weeks 9-11)
├─ BLOCKER-8 (Calendar Safety - weeks 9-10)
├─ BLOCKER-9 start (Rocket Portfolio - weeks 9-12)
└─ Quality gates + performance validation

Sprint 7-8 (Weeks 13-16): Advanced Features & Risk Management
├─ BLOCKER-5 start (Audit Trail - weeks 13-16)
├─ BLOCKER-6 completion (Multi-TF - week 13)
├─ BLOCKER-7 completion (Parameterization - week 14)
├─ BLOCKER-10 start (HNSW Persistence - weeks 14-16)
├─ BLOCKER-11 start (Risk Management - weeks 14-16)
└─ API integration + frontend coordination

Sprint 9-10 (Weeks 17-20): Finalization & Polish
├─ BLOCKER-5 completion (Audit - week 17)
├─ BLOCKER-9 completion (Portfolio - week 17)
├─ BLOCKER-10 completion (Persistence - week 18)
├─ BLOCKER-11 completion (Risk - week 18)
├─ BLOCKER-12 (Execution & Scalability - weeks 18-19)
├─ BLOCKER-13 (Integration & Polish - weeks 19-20)
└─ Final validation + performance tuning

Total: 20 weeks, 10 sprints, 13 BLOCKERs
```

### 2.2 Detailed Sprint Breakdown

#### **SPRINT 1-2 (Weeks 1-4): FOUNDATIONS & STATE MACHINE**

**Objectives:**
- Complete BLOCKER-1 (State Machine) - foundation for all other features
- Start BLOCKER-2 (Journal Schema) - depends on BLOCKER-1
- Begin BLOCKER-6 infrastructure setup (Multi-framework support)

**Team Allocation (6.5 FTE):**
- Senior Backend (1.5 FTE): BLOCKER-1 lead + code review
- Backend Engineers (2 FTE): BLOCKER-1 + BLOCKER-2 start
- Infrastructure (1 FTE): Database setup + CI/CD
- QA/Test (1 FTE): Unit test framework
- Junior Backend (1 FTE): Utilities + documentation

**Deliverables:**

| Week | BLOCKER | Stories | FRs | Hours | Output |
|------|---------|---------|-----|-------|--------|
| 1 | B-1 | 2 | 12 | 96 | State enums, transitions (first pass) |
| 2 | B-1 | 3 | 11 | 88 | Approval workflow, rollback logic |
| 3 | B-2 | 2 | 18 | 120 | Journal schema design, migrations |
| 4 | B-2, B-6 | 4 | 19 | 152 | Parameter encoding, TF abstraction layer |

**Critical Paths:**
- Week 2: BLOCKER-1 validation gates (30 unit tests + state diagram)
- Week 4: BLOCKER-2 schema freeze (required for weeks 5-8)

**Testing:**
- Unit tests: 84 (State Machine) + 40 (Journal schema foundation)
- Integration tests: 12 (State + Journal)
- Code coverage target: 85%+

**Risks & Mitigations:**
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| State machine design flaws | MEDIUM | HIGH | Extra design review (week 1), state diagram validation |
| Schema migration issues | MEDIUM | HIGH | Database expert review, test migration scripts |
| TF abstraction too complex | LOW | MEDIUM | Spike in week 1, simplify if needed |

---

#### **SPRINT 3-4 (Weeks 5-8): CORE SYSTEMS & PARAMETERIZATION**

**Objectives:**
- Complete BLOCKER-2 (Journal Schema) - unblocks telemetry, comparison, audit
- Complete BLOCKER-3 (Telemetry) - unblocks BLOCKER-4
- Start BLOCKER-7 (DFF Parameterization) - enables advanced workflows

**Team Allocation (6.5 FTE):**
- Senior Backend (1 FTE): BLOCKER-3 lead + architecture review
- Backend Engineers (2.5 FTE): BLOCKER-2 completion + BLOCKER-7
- Infrastructure (0.5 FTE): Database optimization
- QA/Test (1 FTE): Integration test framework
- Junior Backend (1 FTE): Documentation + utilities

**Deliverables:**

| Week | BLOCKER | Stories | FRs | Hours | Output |
|------|---------|---------|-----|-------|--------|
| 5 | B-2 | 2 | 15 | 120 | Reproducibility verification, market snapshots |
| 6 | B-3 | 2 | 20 | 160 | Metrics collection + real-time aggregation |
| 7 | B-3, B-7 | 3 | 18 | 144 | Dashboard queries, parameter profile framework |
| 8 | B-7 | 3 | 15 | 120 | Sensitivity analysis, profile storage |

**Critical Paths:**
- Week 5: BLOCKER-2 completion (blocks 3, 4, 5)
- Week 7: BLOCKER-3 completion (blocks 4)

**Testing:**
- Unit tests: 72 (Telemetry) + 32 (Parameterization)
- Integration tests: 28 (Journal + Telemetry)
- Performance benchmarks: Query <100ms target

---

#### **SPRINT 5-6 (Weeks 9-12): PORTFOLIO & PERSISTENCE BUILD**

**Objectives:**
- Complete BLOCKER-3 (Telemetry)
- Complete BLOCKER-4 (Comparison Engine)
- Start BLOCKER-8 (Calendar Safety) + BLOCKER-9 (Rocket Portfolio)

**Team Allocation (6.5 FTE):**
- Senior Backend (1 FTE): BLOCKER-4 lead + optimization
- Backend Engineers (2 FTE): BLOCKER-4 + BLOCKER-9
- Infrastructure (0.5 FTE): Performance tuning
- QA/Test (1 FTE): System test design
- Junior Backend (1 FTE): Calendar utilities + documentation

**Deliverables:**

| Week | BLOCKER | Stories | FRs | Hours | Output |
|------|---------|---------|-----|-------|--------|
| 9 | B-3, B-4 | 3 | 16 | 128 | Comparison engine start, delta algorithms |
| 10 | B-4, B-8 | 3 | 14 | 112 | Export/report, calendar utilities |
| 11 | B-9 | 4 | 20 | 160 | Portfolio data structures, multi-asset metrics |
| 12 | B-9 | 4 | 16 | 128 | Portfolio-level aggregation |

**Critical Paths:**
- Week 9: BLOCKER-4 start (depends on B-3 done)
- Week 11: BLOCKER-9 framework solidified (needed for weeks 13+)

---

#### **SPRINT 7-8 (Weeks 13-16): ADVANCED FEATURES & RISK**

**Objectives:**
- Start BLOCKER-5 (Audit Trail)
- Complete BLOCKER-6 (Multi-TF Execution)
- Complete BLOCKER-7 (Parameterization)
- Start BLOCKER-10 (HNSW Persistence)
- Start BLOCKER-11 (Risk Management)

**Team Allocation (6.5 FTE):**
- Senior Backend (1.5 FTE): BLOCKER-5 + BLOCKER-10 lead
- Backend Engineers (2 FTE): Risk management + parameter completion
- Infrastructure (0.5 FTE): Vector indexing setup
- QA/Test (1 FTE): Advanced test scenarios
- Junior Backend (0.5 FTE): Documentation

**Deliverables:**

| Week | BLOCKER | Stories | FRs | Hours | Output |
|------|---------|---------|-----|-------|--------|
| 13 | B-5, B-6 | 3 | 14 | 112 | Audit log structure, TF multi-framework done |
| 14 | B-7, B-10, B-11 | 4 | 18 | 144 | Parameter optimization, HNSW setup, VaR metrics |
| 15 | B-10, B-11 | 3 | 12 | 96 | Persistent caching, drawdown analysis |
| 16 | B-5 | 3 | 14 | 112 | Digital signatures, audit query layer |

**Critical Paths:**
- Week 13: B-6 complete (unblocks framework-specific tests)
- Week 14: B-10 architecture finalized (needed for performance tuning)

---

#### **SPRINT 9-10 (Weeks 17-20): FINALIZATION & POLISH**

**Objectives:**
- Complete BLOCKER-5 (Audit Trail)
- Complete BLOCKER-9 (Rocket Portfolio)
- Complete BLOCKER-10 (HNSW Persistence)
- Complete BLOCKER-11 (Risk Management)
- Execute BLOCKER-12 (Execution & Scalability)
- Execute BLOCKER-13 (Integration & Polish)

**Team Allocation (6.5 FTE):**
- Senior Backend (1 FTE): Performance tuning + optimization lead
- Backend Engineers (2 FTE): Integration + BLOCKER-12
- Infrastructure (0.5 FTE): Scalability + monitoring
- QA/Test (1.5 FTE): End-to-end testing + performance validation
- Junior Backend (0.5 FTE): Documentation

**Deliverables:**

| Week | BLOCKER | Stories | FRs | Hours | Output |
|------|---------|---------|-----|-------|--------|
| 17 | B-5, B-9 | 4 | 16 | 128 | Audit trail done, portfolio features complete |
| 18 | B-10, B-11, B-12 | 5 | 18 | 144 | Persistence done, risk done, scalability start |
| 19 | B-12, B-13 | 6 | 16 | 128 | Execution optimization, API integration |
| 20 | B-13 | 4 | 12 | 96 | Final polish, documentation, launch prep |

**Critical Paths:**
- Week 17: All BLOCKER completion gates
- Week 19: API layer tested end-to-end
- Week 20: Launch readiness validation

**System Tests:**
- 64 system tests (12 workflows × 5 variations)
- Performance benchmarks: <10ms state transitions, <100ms queries
- Concurrent access: 1000 req/sec verified
- Data consistency: Audit trail matches state 100%

---

## PART 3: RESOURCE ALLOCATION

### 3.1 Team Structure (6.5 FTE)

**Role Breakdown:**

| Role | FTE | Skills | Sprints |
|------|-----|--------|---------|
| **Tech Lead / Architect** | 1 | System design, Python, DB optimization, mentoring | All (1-10) |
| **Senior Backend Engineer #1** | 1 | State machines, complex algorithms, code review | All (1-10) |
| **Backend Engineer #2** | 1 | Full-stack backend, APIs, integrations | All (1-10) |
| **Backend Engineer #3** | 1 | Database, query optimization, performance | All (1-10) |
| **Infrastructure/DevOps** | 0.5 | CI/CD, Docker, database management | All (1-10) |
| **QA/Test Automation** | 1 | Test design, automation frameworks, performance testing | All (1-10) |
| **Junior Backend Engineer** | 0.5 | Utilities, documentation, simple features | All (1-10) |
| **TOTAL** | **6.5** | - | - |

### 3.2 Weekly Capacity Model

**Total: 260 hours/week (6.5 FTE × 40 hours)**

**Allocation by Type:**

| Activity | Hours/Week | % | Notes |
|----------|-----------|---|-------|
| Feature Development | 155 | 60% | Code writing for BLOCKERs |
| Testing & QA | 52 | 20% | Unit, integration, system tests |
| Code Review & Refactoring | 26 | 10% | PR review, technical debt |
| Meetings & Planning | 13 | 5% | Sprint planning, standups, reviews |
| Documentation | 14 | 5% | ADRs, API docs, runbooks |
| **Total** | **260** | **100%** | - |

**Effort Distribution by BLOCKER:**

| Sprint | Primary BLOCKERs | Dev Hours | Test Hours | Infra Hours |
|--------|-----------------|-----------|-----------|-------------|
| 1-2 | B-1, B-2, B-6 | 95 | 35 | 10 |
| 3-4 | B-2, B-3, B-7 | 112 | 38 | 8 |
| 5-6 | B-3, B-4, B-8, B-9 | 128 | 42 | 8 |
| 7-8 | B-5, B-6, B-7, B-10, B-11 | 126 | 44 | 10 |
| 9-10 | B-5, B-9, B-10, B-11, B-12, B-13 | 134 | 46 | 12 |

### 3.3 Skills Matrix & Cross-Training

**Critical Skills:**

| Skill | Required For | Who | Backup |
|-------|-------------|-----|--------|
| State Machine Design | B-1 | Tech Lead + Sr Backend #1 | Backend #2 |
| Database Design | B-2 | Backend #3 | Tech Lead |
| Performance Optimization | B-3, B-4, B-12 | Backend #3 + Tech Lead | Senior #1 |
| Framework Integration | B-6 | Tech Lead | Senior #1 + Backend #2 |
| Risk Analysis | B-11 | Senior #1 | Tech Lead |
| Test Design | All | QA Lead | Backend engineers (10% time) |

**Cross-Training Plan:**
- Weeks 1-4: All engineers learn State Machine design (B-1 knowledge transfer)
- Weeks 5-8: All engineers learn Journal Schema and query optimization
- Weeks 13-16: Focus on Risk Management and advanced optimization
- Weeks 17-20: All hands on performance tuning and integration

---

## PART 4: DEPENDENCY GRAPH & CRITICAL PATH

### 4.1 BLOCKER Dependency Matrix

```
Dependency Flow:

FOUNDATION (Week 1-2)
└─ B-1: State Machine (foundational - 0 dependencies)

PHASE 1 (Week 2-9)
├─ B-2: Journal (depends on B-1)
│  ├─ B-3: Telemetry (depends on B-2)
│  │  └─ B-4: Comparison (depends on B-3)
│  └─ B-5: Audit (depends on B-1, B-2)
└─ B-6: Multi-TF (depends on B-1)

PHASE 2 (Week 9-16)
├─ B-7: DFF Parameterization (depends on B-2, B-6)
├─ B-8: Calendar Safety (depends on B-1)
├─ B-9: Rocket Portfolio (depends on B-3)
├─ B-10: HNSW Persistence (depends on B-3, B-4)
└─ B-11: Risk Management (depends on B-3, B-4)

PHASE 3 (Week 17-20)
├─ B-12: Execution & Scalability (depends on B-1-11)
└─ B-13: Integration & Polish (depends on B-1-12)
```

### 4.2 Critical Path Analysis

**Critical Path (Must not slip > 1 week):**

| Item | Duration | Slack | Status |
|------|----------|-------|--------|
| B-1 (State Machine) | Week 1-2 | 0 | CRITICAL |
| B-2 (Journal) | Week 2-5 | 0 | CRITICAL |
| B-3 (Telemetry) | Week 5-9 | 0 | CRITICAL |
| B-4 (Comparison) | Week 9-11 | 1 | CRITICAL |
| B-6 (Multi-TF) | Week 1-13 | 4 | HIGH |
| B-9 (Portfolio) | Week 9-17 | 2 | HIGH |
| B-10 (Persistence) | Week 14-18 | 0 | CRITICAL |
| B-12 (Scalability) | Week 18-19 | 1 | HIGH |

**Slack by BLOCKER:**

```
Week 1 ├─ B-1 (slack: 0) CRITICAL
Week 2 ├─ B-2 (slack: 0) CRITICAL
       ├─ B-6 (slack: 4)
Week 5 ├─ B-3 (slack: 0) CRITICAL
Week 9 ├─ B-4 (slack: 1) HIGH
       ├─ B-7 (slack: 1) HIGH
       ├─ B-8 (slack: 3)
       ├─ B-9 (slack: 2)
Week 14 ├─ B-10 (slack: 0) CRITICAL
        ├─ B-11 (slack: 1) HIGH
Week 18 ├─ B-5 complete (slack: 0) CRITICAL
        ├─ B-12 (slack: 1) HIGH
Week 20 ├─ B-13 final polish
```

---

## PART 5: TEST STRATEGY & COVERAGE

### 5.1 Test Inventory (Enhanced for 2x Scope)

**Total Test Cases: 576 → 800+ tests**

| Test Type | Original | 2x Expansion | New Total | Hours |
|-----------|----------|-------------|-----------|-------|
| Unit Tests | 336 | +224 | 560 | 56 |
| Integration Tests | 144 | +96 | 240 | 120 |
| System/E2E Tests | 64 | +56 | 120 | 180 |
| Performance Tests | 20 | +20 | 40 | 240 |
| Security Tests | 12 | +8 | 20 | 120 |
| **TOTAL** | **576** | **+404** | **980** | **716** |

### 5.2 Testing Timeline

**Per Sprint Testing Plan:**

| Sprint | Phase | Unit Tests | Integration | System | Performance | Notes |
|--------|-------|-----------|-------------|--------|-------------|-------|
| 1-2 | Foundation | 84 | 12 | 0 | 0 | State Machine validation |
| 3-4 | Core Systems | 104 | 28 | 8 | 0 | Journal + Telemetry |
| 5-6 | Portfolio | 120 | 56 | 16 | 8 | Comparison + Portfolio framework |
| 7-8 | Advanced | 152 | 88 | 32 | 16 | Audit + Risk + Persistence |
| 9-10 | Finalization | 180 | 120 | 64 | 40 | Full system integration + perf |

### 5.3 Code Coverage Targets

**By BLOCKER:**

| BLOCKER | Unit Coverage | Integration Coverage | Overall Target |
|---------|---------------|----------------------|-----------------|
| B-1: State Machine | 95% | 90% | 92% |
| B-2: Journal | 90% | 85% | 88% |
| B-3: Telemetry | 88% | 85% | 86% |
| B-4: Comparison | 85% | 80% | 82% |
| B-5: Audit | 90% | 88% | 89% |
| B-6: Multi-TF | 85% | 80% | 82% |
| B-7: Parameterization | 87% | 82% | 84% |
| B-8: Calendar | 92% | 88% | 90% |
| B-9: Portfolio | 86% | 83% | 84% |
| B-10: Persistence | 88% | 85% | 86% |
| B-11: Risk | 87% | 84% | 85% |
| B-12: Scalability | 80% | 85% | 82% |
| B-13: Integration | 75% | 90% | 82% |
| **Average** | **87%** | **84%** | **85%** |

---

## PART 6: RISK MANAGEMENT

### 6.1 Top 10 Risks

| Risk | Probability | Impact | Mitigation | Owner |
|------|------------|--------|-----------|-------|
| **HIGH-1:** State Machine design flaws found late | MEDIUM | HIGH | Extra design review week 1, state diagram | Tech Lead |
| **HIGH-2:** Multi-framework integration complexity | MEDIUM | HIGH | Spike in week 1, framework expert consultation | Senior #1 |
| **HIGH-3:** Performance degradation at scale | MEDIUM-HIGH | HIGH | Benchmarks in weeks 6-8, optimization budget | Backend #3 |
| **HIGH-4:** Database schema migration issues | MEDIUM | MEDIUM | Test migrations week 4, rollback scripts | Backend #3 |
| **HIGH-5:** Test coverage falls below 80% | LOW | MEDIUM | QA checkpoints weeks 8, 16, 20 | QA Lead |
| **MED-1:** Calendar safety edge cases | LOW | MEDIUM | Extended testing phase 6-7 | Backend #2 |
| **MED-2:** Risk metrics algorithm errors | MEDIUM | MEDIUM | Math review + external validation | Senior #1 |
| **MED-3:** API integration complexity | MEDIUM | MEDIUM | Early API design phase 1 | Tech Lead |
| **MED-4:** Team member turnover | LOW | HIGH | Documentation focus, knowledge transfer | All |
| **MED-5:** Timeline slip to week 22 | LOW | LOW | 4-week buffer built in, not a blocker | Project Mgr |

### 6.2 Risk Mitigation Strategy

**Contingency Budget:**
- 4-week buffer (weeks 17-20 can absorb 4 weeks of delay)
- 10% development time reserved for unknown issues
- 2-week performance optimization window (weeks 19-20)

**Quality Gates (No Slip):**
- Week 2: B-1 complete or STOP
- Week 5: B-2 complete or reduce scope
- Week 9: B-3 complete or descope B-4
- Week 20: Final validation complete or extended launch

---

## PART 7: BUDGET & RESOURCE ALLOCATION

### 7.1 Cost Breakdown (6.5 FTE, 20 weeks)

**Labor Costs:**

| Role | FTE | Rate | 20 weeks | Total |
|------|-----|------|----------|-------|
| Tech Lead/Architect | 1 | $80K/year | 38 weeks | $58,462 |
| Senior Backend #1 | 1 | $75K/year | 38 weeks | $54,808 |
| Backend Engineer #2 | 1 | $65K/year | 38 weeks | $47,308 |
| Backend Engineer #3 | 1 | $65K/year | 38 weeks | $47,308 |
| Infrastructure/DevOps | 0.5 | $70K/year | 38 weeks | $26,538 |
| QA/Test Automation | 1 | $60K/year | 38 weeks | $43,846 |
| Junior Backend | 0.5 | $50K/year | 38 weeks | $18,269 |
| **TOTAL LABOR** | **6.5** | - | - | **$296,539** |

**Infrastructure Costs:**

| Item | Cost | Purpose |
|------|------|---------|
| Database (RDS/managed) | $2,000 | 20 weeks |
| CI/CD pipeline enhancements | $1,500 | Build agents, storage |
| Monitoring & logging | $1,000 | DataDog/New Relic |
| Testing tools & licenses | $500 | Pytest, coverage tools |
| Development environment | $1,000 | GPUs for framework testing |
| **Total Infrastructure** | **$6,000** | - |

**Other Costs:**

| Item | Cost | Purpose |
|------|------|---------|
| External code review (security) | $5,000 | Week 15-16 |
| Performance audit | $3,000 | Week 18 |
| Risk analysis consultation | $2,000 | Week 14 |
| Documentation/training | $1,500 | Final weeks |
| **Total Other** | **$11,500** | - |

**Total Project Budget: ~$314,000 for 6.5 FTE × 20 weeks**

### 7.2 Monthly Budget Allocation

| Month | Weeks | FTE Hours | Labor | Infra | Other | Total |
|-------|-------|-----------|-------|-------|-------|-------|
| Feb (27-29) | 0.5 | 130 | $10,000 | $500 | - | $10,500 |
| March | 4.5 | 1,170 | $90,000 | $1,500 | - | $91,500 |
| April | 4 | 1,040 | $80,000 | $1,500 | $3,000 | $84,500 |
| May | 4.5 | 1,170 | $90,000 | $1,500 | $5,000 | $96,500 |
| June | 4 | 1,040 | $80,000 | $1,000 | $3,000 | $84,000 |
| July (1-18) | 2.5 | 650 | $50,000 | $1,000 | - | $51,000 |
| **TOTAL** | **20** | **5,200** | **$400,000** | **$7,500** | **$11,000** | **$418,500** |

**Note:** Labor rate shown is annualized split across 20 weeks. Actual payroll may be structured differently.

---

## PART 8: SUCCESS METRICS & LAUNCH READINESS

### 8.1 Definition of Done (per BLOCKER)

**Code Quality:**
- ✅ All FRs implemented (100% coverage)
- ✅ Code review approved (2 reviewers minimum)
- ✅ SonarQube rating ≥ B
- ✅ No HIGH/CRITICAL security issues

**Testing:**
- ✅ Unit test coverage ≥85%
- ✅ Integration tests passing 100%
- ✅ System tests passing 100%
- ✅ Performance benchmarks met (<100ms queries)

**Documentation:**
- ✅ API documentation complete
- ✅ Architecture Decision Records (ADRs) updated
- ✅ Runbooks for deployment/troubleshooting
- ✅ User guides for new features

**Performance:**
- ✅ Database queries <100ms (p95)
- ✅ State transitions <10ms
- ✅ No memory leaks detected
- ✅ Concurrent access: 1000 req/sec verified

### 8.2 Launch Readiness Checklist (Week 20)

**Code & Architecture:**
- [ ] All 574 FRs implemented
- [ ] All 13 BLOCKERs complete
- [ ] Code review 100%
- [ ] SonarQube rating ≥ B
- [ ] Architecture audit passed
- [ ] Database migrations tested (rollback verified)

**Testing & Quality:**
- [ ] 980+ tests passing (100% pass rate)
- [ ] Code coverage 85%+
- [ ] Security audit complete (0 critical issues)
- [ ] Performance testing complete
- [ ] Load testing: 1000 req/sec
- [ ] Stress testing: Memory stable

**Documentation & Deployment:**
- [ ] API documentation complete
- [ ] Deployment runbook finalized
- [ ] Rollback procedures tested
- [ ] Monitoring dashboards ready
- [ ] Alert rules configured
- [ ] Incident response playbooks

**Team Readiness:**
- [ ] Training completed (all team members)
- [ ] Knowledge transfer documented
- [ ] On-call rotation established
- [ ] SLOs defined (uptime, latency, error rate)

---

## PART 9: GANTT CHART & VISUAL SCHEDULE

### 9.1 20-Week Timeline

```
Sprint  Weeks   BLOCKER-1  BLOCKER-2  BLOCKER-3  BLOCKER-4  BLOCKER-5  BLOCKER-6  BLOCKER-7  BLOCKER-8  BLOCKER-9  BLOCKER-10 BLOCKER-11 BLOCKER-12 BLOCKER-13
        (State) (Journal)  (Telemetry)(Compare)  (Audit)    (Multi-TF) (Param)    (Calendar) (Portfolio)(Persist)  (Risk)     (Scale)    (Polish)

1-2     1-4     ████████                                      ████
        ████░░  Foundation: State Machine (CRITICAL PATH)

3-4     5-8                ████████    ██         ████       ▓▓▓▓
        ░░████░░           Journal complete, Telemetry, Parameterization start

5-6     9-12               ░░░░░░░░  ████████    ░░░░░░     ▓▓▓▓░░░░
                           Comparison engine, Portfolio framework

7-8     13-16                        ░░░░░░░░  ████████    ▓▓▓▓░░░░  ▓▓▓▓░░░░  ████████
                           Audit trail, Risk Management, Persistence setup

9-10    17-20                        ░░░░░░░░                  ░░░░░░░░  ░░░░░░░░  ████████  ████████
                           Integration, scalability, polish

Legend:
████ = In progress (dark)
░░░░ = Completed (light)
▓▓▓▓ = Planning/Setup
```

### 9.2 Weekly Capacity Chart

```
Sprint 1-2:   260h/wk ├─ Dev: 155h │ Test: 70h │ Infra: 20h │ Meetings: 15h
Sprint 3-4:   260h/wk ├─ Dev: 155h │ Test: 75h │ Infra: 20h │ Meetings: 10h
Sprint 5-6:   260h/wk ├─ Dev: 160h │ Test: 75h │ Infra: 15h │ Meetings: 10h
Sprint 7-8:   260h/wk ├─ Dev: 155h │ Test: 85h │ Infra: 15h │ Meetings: 5h
Sprint 9-10:  260h/wk ├─ Dev: 140h │ Test: 95h │ Infra: 15h │ Meetings: 10h
```

---

## PART 10: IMPLEMENTATION RECOMMENDATIONS

### 10.1 Recommended Approach: Option B (6.5 FTE, 20 weeks)

**Why This Works:**

✅ **Team Stability:**
- No hiring overhead
- Continuous knowledge accumulation
- Higher code quality from same team

✅ **Sustainable Pace:**
- 40 SP/week/person (realistic for quality)
- Reduces context switching penalties
- Time for code review and refactoring

✅ **Risk Mitigation:**
- 4-week buffer for issues
- Critical path analysis identifies slip risks
- Quality gates at weeks 2, 5, 9, 20

✅ **Cost Efficiency:**
- $314K project cost
- Comparable to 13 FTE option ($318K+)
- Better ROI on training investment

✅ **Quality Benefits:**
- 85% code coverage target achievable
- 980+ tests with time to debug
- Performance tuning in weeks 19-20
- Security audit with findings time

### 10.2 Go/No-Go Decision Gates

**Week 2 Gate (B-1 Completion):**
- Decision: Continue or STOP
- Criteria: B-1 ≥85% complete, no HIGH security issues
- If STOP: Delay launch 1-2 weeks, increase staff

**Week 5 Gate (B-2 Completion):**
- Decision: Continue or descope
- Criteria: B-2 ≥90% complete, reproducibility verified
- If ISSUE: Drop lowest-priority BLOCKER (B-8 or B-7 partial)

**Week 9 Gate (B-3 Completion + B-4 Start):**
- Decision: Continue or replan
- Criteria: B-3 ≥95% complete, B-4 architecture approved
- If ISSUE: Extend 2 weeks, reduce team size 10%

**Week 20 Gate (Launch Readiness):**
- Decision: Launch or delay 1-2 weeks
- Criteria: All 13 BLOCKERs ≥90%, tests ≥95% pass, coverage ≥85%
- If ISSUE: Supported GA (canary) launch possible

### 10.3 Transition to Ongoing Operations (Week 21+)

**Post-Launch Team Structure:**

| Role | FTE | Activity | Duration |
|------|-----|----------|----------|
| Tech Lead | 1.0 | Architecture + stability | Ongoing |
| Backend Support | 2.0 | Incident response + hotfixes | Weeks 21-26 |
| QA/Monitoring | 0.5 | Production validation | Weeks 21-26 |
| New Feature Dev | 2.0 | Phase 3 planning | Weeks 21-26 |
| Junior/Training | 1.0 | Knowledge transfer | Weeks 21-26 |

---

## APPENDIX A: REFERENCE DOCUMENTS

**Related Documents:**
- `CODE-TEST-IMPLEMENTATION-PLAN-2026-02-27.md` - Original 12-week plan
- `PHASE-2-IMPLEMENTATION-EXECUTIVE-SUMMARY.md` - Phase 2 overview
- `IMPLEMENTATION-GANTT-CHART-2026-02-27.md` - Visual schedule (original)
- `TECHNICAL-DEBT-REGISTRY-2026-02-27.md` - Known issues to address

**Stakeholder References:**
- Project Manager: Budget tracking, timeline updates
- Engineering Lead: Technical escalations, design reviews
- Product Owner: Feature prioritization, scope changes
- Operations: Infrastructure setup, monitoring configuration

---

## APPENDIX B: BLOCKER DESCRIPTIONS (DETAILED)

### BLOCKER-1: Strategy Lifecycle State Machine
**Epic:** E-STRATEGY-LIFECYCLE
**Duration:** Weeks 1-2 (2 weeks, 0 slack)
**Team:** Tech Lead + Senior Backend #1
**Status:** CRITICAL PATH
**FRs:** 23 | Stories: 5 | Hours: 72-106

**Why Critical:** Foundation for all other features. Blocks B-2, B-3, B-5.

---

### BLOCKER-2: Run Journal Schema & Reproducibility
**Epic:** E-BACKTEST-METADATA
**Duration:** Weeks 2-5 (3.5 weeks, 0 slack)
**Team:** Backend #2, Backend #3
**Status:** CRITICAL PATH
**FRs:** 48 | Stories: 6 | Hours: 158-236

**Why Critical:** Core data structure. Unblocks B-3, B-4, B-5.

---

### BLOCKER-3: Telemetry & Metrics Instrumentation
**Epic:** E-TELEMETRY
**Duration:** Weeks 5-9 (4 weeks, 0 slack)
**Team:** Senior Backend #1, Backend #2
**Status:** CRITICAL PATH
**FRs:** 54 | Stories: 4 | Hours: 152-217

**Why Critical:** Unblocks B-4 (comparison). Data for all dashboards.

---

### BLOCKER-4: Run Comparison Engine
**Epic:** E-COMPARISON
**Duration:** Weeks 9-11 (2 weeks, 1 week slack)
**Team:** Backend #3, Senior Backend #1
**Status:** HIGH (minor slack)
**FRs:** 42 | Stories: 4 | Hours: 174-265

**Why Important:** Core feature for portfolio analysis.

---

### BLOCKER-5: Audit Trail & Verification
**Epic:** E-AUDIT
**Duration:** Weeks 13-17 (4 weeks, 0 slack)
**Team:** Senior Backend #1, Backend #2
**Status:** CRITICAL PATH
**FRs:** 46 | Stories: 4 | Hours: 208-313

**Why Critical:** Regulatory requirement. Immutable records essential.

---

### BLOCKER-6: Multi-Framework Execution Layer
**Epic:** E-MULTI-TF-EXECUTION
**Duration:** Weeks 1-13 (concurrent build, 4 weeks slack)
**Team:** Tech Lead, Infrastructure
**Status:** HIGH
**FRs:** 87 | Stories: 8 | Hours: 624

**Why Important:** TensorFlow/PyTorch/JAX support. High value but less time-sensitive.

---

### BLOCKER-7: Dynamic Feature Framework (DFF) Parameterization
**Epic:** E-DFF-PARAMETERIZATION
**Duration:** Weeks 5-14 (9 weeks, 1 week slack)
**Team:** Backend #2, Junior
**Status:** HIGH
**FRs:** 68 | Stories: 12 | Hours: 544

**Why Important:** Advanced parameter workflows. Enables strategy optimization.

---

### BLOCKER-8: Calendar Safety Utilities
**Epic:** E-CALENDAR-SAFETY
**Duration:** Weeks 9-10 (2 weeks, 3 weeks slack)
**Team:** Junior Backend, Backend #2
**Status:** MEDIUM
**FRs:** 24 | Stories: 6 | Hours: 192

**Why Important:** Data quality safety features. Low complexity, lower priority.

---

### BLOCKER-9: Rocket Portfolio Multi-Asset Support
**Epic:** E-ROCKET-PORTFOLIO
**Duration:** Weeks 9-17 (8 weeks, 2 weeks slack)
**Team:** Backend #3, QA
**Status:** HIGH
**FRs:** 56 | Stories: 10 | Hours: 448

**Why Important:** Portfolio-level analytics. Major feature for traders.

---

### BLOCKER-10: HNSW Vector Indexing & Persistence
**Epic:** E-HNSW-PERSISTENCE
**Duration:** Weeks 14-18 (4 weeks, 0 slack)
**Team:** Backend #3, Infrastructure
**Status:** CRITICAL PATH
**FRs:** 42 | Stories: 6 | Hours: 336

**Why Critical:** Performance foundation. Required for scale.

---

### BLOCKER-11: Risk Management Framework
**Epic:** E-RISK-MANAGEMENT
**Duration:** Weeks 14-18 (4 weeks, 1 week slack)
**Team:** Senior Backend #1, Backend #2
**Status:** HIGH
**FRs:** 34 | Stories: 8 | Hours: 272

**Why Important:** Risk metrics essential for traders. Complex algorithms.

---

### BLOCKER-12: Execution & Scalability Optimization
**Epic:** E-EXECUTION-SCALABILITY
**Duration:** Weeks 18-19 (2 weeks, 1 week slack)
**Team:** All (focus: Tech Lead + Backend #3)
**Status:** HIGH
**FRs:** 42 | Stories: 9 | Hours: 336

**Why Important:** Performance tuning. Non-functional requirements validation.

---

### BLOCKER-13: API Integration & Polish
**Epic:** E-INTEGRATION-POLISH
**Duration:** Weeks 19-20 (2 weeks, 0 slack)
**Team:** All
**Status:** FINAL GATE
**FRs:** 28 | Stories: 14 | Hours: 224

**Why Critical:** Launch readiness. Documentation, deployment, final validation.

---

## APPENDIX C: ASSUMPTION & CONSTRAINTS

### Assumptions
1. ✅ 6.5 FTE team available and committed for full 20 weeks
2. ✅ No major technology changes during project
3. ✅ Database infrastructure available (RDS or equivalent)
4. ✅ Code review capacity maintained (2 reviewers per PR)
5. ✅ Testing infrastructure (CI/CD) functional from week 1
6. ✅ No unplanned production incidents consuming >5% capacity

### Constraints
1. ⚠️ CRITICAL: B-1 must complete by week 2 (zero slip tolerance)
2. ⚠️ CRITICAL: B-2 must complete by week 5 (zero slip tolerance)
3. ⚠️ CRITICAL: B-3 must complete by week 9 (one-week slip acceptable)
4. ⚠️ Code coverage must stay ≥80% (cannot descope testing)
5. ⚠️ Security review required before deployment
6. ⚠️ Performance benchmarks non-negotiable (<100ms queries)

### Scope Boundaries
- **In Scope:** 574 FRs, 350+ stories, 980+ tests, documentation
- **Out of Scope:** UI/frontend implementation (separate effort), mobile apps, analytics beyond MVP
- **Deferred:** Advanced ML features, real-time market data integration (Phase 3)

---

## CONCLUSION

This 20-week implementation plan provides a realistic, sustainable roadmap for delivering the 2x Life OS expansion with your current 6.5 FTE team. By extending the timeline from 12 to 20 weeks, you achieve:

✅ **Quality:** 85%+ code coverage, 980+ passing tests
✅ **Sustainability:** 40 SP/week/person (realistic velocity)
✅ **Risk Mitigation:** 4-week buffer, critical path analysis
✅ **Cost Efficiency:** ~$314K project cost
✅ **Team Stability:** No hiring needed, knowledge preservation

**Recommended Next Steps:**
1. Approve 20-week timeline with stakeholders
2. Lock team commitment for weeks 1-20
3. Schedule sprint planning for week 1
4. Begin BLOCKER-1 design review (week 1, sprint 1)
5. Set up CI/CD, monitoring, documentation templates

**Success Depends On:**
- Team commitment to schedule
- Clear priorities and minimal scope creep
- Effective code review process
- Early identification and escalation of risks
- Regular stakeholder communication

---

**Document Status:** ✅ READY FOR IMPLEMENTATION
**Version:** 2.0 (20-week extended)
**Last Updated:** 2026-02-27
**Project Manager:** [Name/TBD]
**Technical Lead:** [Name/TBD]
