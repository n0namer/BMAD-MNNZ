# Gap Remediation Plan
## katana-vectorbt Implementation Readiness - Critical Gap Resolution

**Created:** 2026-02-26
**Owner:** Implementation Lead
**Timeline:** 12-18 weeks (critical path)
**Status:** Ready for approval

---

## Executive Overview

**Current State:** 5 Epics (122 story points) cover governance & reproducibility but miss core Wave 4 trading features.

**Target State:** 13 Epics (450+ story points) with complete Wave 4 feature set + validation gates.

**Gap:** 8 critical gaps + 12 major gaps must be resolved before feature lock.

**Plan:** Create 8 critical-gap epics + refine 5 provided epics to include major gaps.

---

## Phase 1: Critical Gaps (MUST FIX)

### CRITICAL-1: Multi-Timeframe Trading

**What's Missing:**
- 6 independent Optuna studies (1m, 5m, 15m, 1h, 4h, 1d)
- TF-specific HNSW indices
- Cross-TF conflict resolution rules (MTF confirmation modes)
- TF-specific active_param_count enforcement

**Why Critical:**
- Core Wave 4 feature; all marketing/positioning depends on it
- Without it: only single H4 timeframe (Wave 3 regression)
- Enables signal diversity & scaling

**New Epic:** E-MULTI-TF
**Effort:** 40-50 story points
**Suggested Stories:**
1. S-MTF-001: Parallel Optuna study architecture (13 pts)
2. S-MTF-002: TF-specific HNSW index management (8 pts)
3. S-MTF-003: Cross-TF conflict resolution (MTF modes) (13 pts)
4. S-MTF-004: TF-specific parameter isolation (8 pts)
5. S-MTF-005: Multi-TF testing & validation (8 pts)

**Dependencies:**
- ← CRITICAL-6 (Conditional Optuna must be spec'd first)
- → CRITICAL-7 (gates must test multi-TF)

**Success Criteria:**
- All 6 TF run in parallel
- Each TF has independent optimization
- No cross-TF signal bleeding
- ≥90% test coverage

**Owner:** Optimization Lead
**Timeline:** Weeks 2-5 (parallel with CRITICAL-6, CRITICAL-2)

---

### CRITICAL-2: Distance Function Factory (DFF)

**What's Missing:**
- 6 source type implementations (ATR, StdDev, BB, Range, Fixed%, Corwin-Schultz)
- Role-specific activation (SL/TP/BE/Trail)
- Type-specific parameter contracts
- Trial-level isolation (only 1 type active per role per trial)
- DFF integration in risk calculations

**Why Critical:**
- Risk optimization disabled without it
- Default hardcoded ATR (Wave 3) can't achieve target drawdown
- Blocks Sharpe ratio improvements

**New Epic:** E-DFF
**Effort:** 30-40 story points
**Suggested Stories:**
1. S-DFF-001: DFF architecture & type registry (8 pts)
2. S-DFF-002: ATR & StdDev implementations (8 pts)
3. S-DFF-003: BB, Range, Fixed%, Corwin-Schultz implementations (10 pts)
4. S-DFF-004: Role-specific activation & parameter contracts (8 pts)
5. S-DFF-005: DFF integration in risk/SL/TP calculations (6 pts)

**Dependencies:**
- ← CRITICAL-6 (needs conditional search space to activate only 1 type per trial)
- → CRITICAL-7 (gates must validate DFF effectiveness)

**Success Criteria:**
- All 6 types implemented
- Type isolation enforced in trials
- Parameter contracts validated
- DFF shows 2-5% Sharpe improvement over hardcoded ATR
- ≥90% test coverage

**Owner:** Risk Management Lead
**Timeline:** Weeks 2-6 (parallel with CRITICAL-1, CRITICAL-6)

---

### CRITICAL-3: Rockets Portfolio Model

**What's Missing:**
- 10-strategy bucket allocation logic
- Tier-1 cap enforcement (60% of rocket bucket)
- Max 20% per rocket allocation rules
- Individual rocket kill-switch (40% MaxDD)
- Portfolio kill-switch (50% MaxDD)
- 7-day blacklist & re-optimization on trigger
- Stress-test scenarios (all 10 fail simultaneously)

**Why Critical:**
- Multi-strategy portfolio unavailable without it
- Scaling & profitability validation blocked
- Risk governance incomplete

**New Epic:** E-ROCKETS-GOVERNANCE
**Effort:** 35-45 story points
**Suggested Stories:**
1. S-ROCKETS-001: Bucket allocation algorithm (8 pts)
2. S-ROCKETS-002: Tier-1 cap & allocation rules enforcement (8 pts)
3. S-ROCKETS-003: Individual rocket kill-switch (40% DD) (6 pts)
4. S-ROCKETS-004: Portfolio kill-switch (50% DD) + rebalance (8 pts)
5. S-ROCKETS-005: Blacklist & re-optimization trigger (5 pts)
6. S-ROCKETS-006: Stress-test scenarios & validation (10 pts)

**Dependencies:**
- ← CRITICAL-7 (gates must validate rocket models)
- → E-COMPARE-WORKFLOW (may need bucket-level comparison)

**Success Criteria:**
- Bucket allocation optimal per tier rules
- Kill-switches trigger within ±1% of threshold
- Blacklist re-optimization works automatically
- Stress test: all 10 fail → loss capped at bucket limit
- ≥85% test coverage

**Owner:** Portfolio Manager / Quant Lead
**Timeline:** Weeks 8-12 (after gates in place)

---

### CRITICAL-4: Calendar Safety (HARD)

**What's Missing:**
- Event map management (45+ forex events)
- Daily/weekly refresh jobs
- Risk-off window calculation & enforcement
- Event-pair mapping (e.g., UK CPI → GBPUSD only)
- Artifact generation (risk_flags.json, calendar_snapshot.json)
- Fallback scenarios (data unavailability)

**Why Critical:**
- Safety policy unenforceable without backend
- Regulatory risk; can't prove safety measures exist
- UX spec assumes this exists

**New Epic:** E-CALENDAR-SAFETY
**Effort:** 25-30 story points
**Suggested Stories:**
1. S-CALENDAR-001: Event map data structure & storage (5 pts)
2. S-CALENDAR-002: Daily/weekly refresh jobs (6 pts)
3. S-CALENDAR-003: Risk-off window calculation (5 pts)
4. S-CALENDAR-004: Event-pair impact mapping (5 pts)
5. S-CALENDAR-005: risk_flags.json artifact generation (5 pts)
6. S-CALENDAR-006: Fallback & error handling (5 pts)

**Dependencies:**
- ← E-STRATEGY-LIFECYCLE (needs state machine for risk-off state)
- → E-NEWS-OVERLAY (news overlay must not override HARD)

**Success Criteria:**
- 45+ events in event map
- Refresh jobs run daily/weekly without errors
- Risk-off windows accurate (±1 minute)
- Pair-specific impact scoring correct
- Fallback works when data unavailable
- ≥90% test coverage

**Owner:** Risk/Operations Lead
**Timeline:** Weeks 6-8 (after E-STRATEGY-LIFECYCLE)

---

### CRITICAL-5: News Overlay (SOFT)

**What's Missing:**
- Sentiment data source (manual, API, or ML classification)
- Dovish/hawkish classification rules
- Soft penalty vs. hard block logic
- Optuna parameter optimization for overlay thresholds
- Constraint enforcement (cannot override HARD calendar safety)
- news_overlay.json artifact generation

**Why Critical:**
- Directional alpha unavailable without it
- Marketing: "sentiment-aware trading" (Wave 4 feature)
- Blocks higher return targets

**New Epic:** E-NEWS-OVERLAY
**Effort:** 20-25 story points
**Suggested Stories:**
1. S-NEWS-001: Sentiment data source integration (8 pts)
   *Architecture decision: manual lookup table vs. ML API vs. real-time feed*
2. S-NEWS-002: Dovish/hawkish classification rules (5 pts)
3. S-NEWS-003: Soft penalty logic & parameter optimization (6 pts)
4. S-NEWS-004: Constraint enforcement vs. HARD calendar safety (3 pts)
5. S-NEWS-005: news_overlay.json artifact generation (3 pts)

**Dependencies:**
- ← CRITICAL-4 (Calendar Safety must be in place first)
- ← CRITICAL-6 (Conditional Optuna handles news parameters)

**Success Criteria:**
- Sentiment classification ≥85% accurate (if using ML)
- Soft penalty logic does not increase drawdown >2%
- Cannot override HARD calendar safety windows
- Optional feature (can be disabled)
- ≥80% test coverage

**Owner:** ML/Alpha Research Lead
**Timeline:** Weeks 9-11 (after CRITICAL-4)

**Architecture Decision Required:** Where does sentiment data come from?
- **Option A (MVP):** Manual event lookup table (45+ events pre-classified)
- **Option B:** ML sentiment classifier (training data?)
- **Option C:** Real-time sentiment API (cost/latency tradeoff)
**Recommend:** Option A (MVP) → Option B (Phase 2 if needed)

---

### CRITICAL-6: Conditional Optuna Search Space (SPEC ONLY)

**What's Missing:**
- Specification of define-by-run search space mutation
- Parameter isolation rules per profile
- Inactive parameter handling (fixed to defaults with logging)
- Trial attribute logging for reproducibility
- Pruning integration (MedianPruner, Hyperband)
- Example trial logs & iteration workflow

**Why Critical:**
- **BLOCKING CRITICAL:** All optimization depends on this
- Without it: parameter explosion (100+ active params → resource exhaustion)
- Conditional DFF & Multi-TF require this

**Spec Effort:** 25-30 story points (ARCHITECTURE + DETAILED SPEC)
**Not an Epic:** This is a specification/refinement task, not implementation

**Required Deliverables:**
1. **Conditional Search Space Algorithm** (document)
   - How parameters are selected per trial
   - Which parameters activate per profile
   - Inactive parameter logging
   - Example: "Trial #42, Profile: Scalping, Active params: [param_1, ..., param_43], Inactive: [param_44, ..., param_115]"

2. **Profile Validation Rules** (document + test spec)
   - active_param_count ≤ 70 enforcement
   - Per-profile parameter constraints
   - Rejection rules for invalid configs

3. **Pruning Integration Spec** (document)
   - MedianPruner thresholds
   - Hyperband eta & generations
   - Early-stop criteria
   - Intermediate value reporting

4. **Trial Artifact Schema** (JSON schema)
   - trial_id, trial_number, parameters, results, pruned, intermediate_values
   - Checkpoint format & location

5. **Example Trial Execution Log** (realistic example)
   - Multi-trial workflow with conditional branches

**Dependencies:**
- **Blocks:** CRITICAL-1, CRITICAL-2, CRITICAL-6 (all optimization work)
- **Blocked by:** None (MUST START FIRST)

**Success Criteria:**
- Spec is unambiguous (reviewable by 3+ engineers, zero conflicts)
- Example trials show parameter isolation working
- Pruning rules prevent resource exhaustion
- Reproducibility: every trial run is fully logged

**Owner:** Optimization Architect
**Timeline:** **WEEK 1 ONLY** (CRITICAL PATH BLOCKER)

**Recommendation:** Schedule 8-10 hours with optimization team to finalize spec before any coding starts.

---

### CRITICAL-7: Quality Gate System (7 Gates)

**What's Missing:**
- PSR (Probabilistic Sharpe Ratio) calculation & threshold
- FDR (False Discovery Rate) control
- PBO (Parameter Optimization Bias) detection
- Correlation analysis (strategy-pair, strategy-benchmark)
- Monte Carlo stress testing
- WFE (Walk-Forward Efficiency) metric
- Manual gate A-B approval workflow
- Risk score aggregation & go/no-go decision
- Alert rules & reporting

**Why Critical:**
- PRD gate requirement: "Pass 7 gates before promotion"
- Go-live blocked without this
- Approval workflow depends on gate system

**New Epic:** E-QUALITY-GATES
**Effort:** 40-50 story points
**Suggested Stories:**
1. S-GATES-001: PSR calculation & threshold (8 pts)
2. S-GATES-002: FDR control implementation (8 pts)
3. S-GATES-003: PBO detection algorithm (8 pts)
4. S-GATES-004: Correlation analysis engine (6 pts)
5. S-GATES-005: Monte Carlo stress testing (10 pts)
6. S-GATES-006: WFE metric & walk-forward validation (6 pts)
7. S-GATES-007: Manual approval workflow (Gate A-B) (8 pts)
8. S-GATES-008: Risk score aggregation & go/no-go (4 pts)
9. S-GATES-009: Alert rules & reporting (6 pts)

**Dependencies:**
- ← E-JOURNAL-SCHEMA (needs reproducibility artifacts)
- ← CRITICAL-8 (needs WFO output)
- → CRITICAL-3 (gates validate rocket models)
- → E-STRATEGY-LIFECYCLE (approval workflow integration)

**Success Criteria:**
- All 7 gates implemented & tested
- Risk score aggregation documented
- Manual approval UI functional
- Alert thresholds tuned to <5% false positive rate
- ≥95% test coverage
- Gate pass/fail decisions reproducible

**Owner:** QA Lead / Validation Architect
**Timeline:** Weeks 6-10 (after E-JOURNAL-SCHEMA, CRITICAL-8)

**Gate Thresholds to Define:**
```
Gate 1 (PSR):        PSR > 1.5 ✓ | < 1.5 ✗
Gate 2 (FDR):        FDR < 0.05 ✓ | > 0.05 ✗
Gate 3 (PBO):        PBO ratio < 1.5 ✓ | > 1.5 ✗
Gate 4 (Correlation): ρ < 0.3 w/ benchmark ✓ | > 0.3 ✗
Gate 5 (Monte Carlo): Stress loss < 40% ✓ | > 40% ✗
Gate 6 (WFE):        WFE > 0.5 ✓ | < 0.5 ✗
Gate 7 (Manual):     Reviewer approval required
```

---

### CRITICAL-8: Walk-Forward Optimization (WFO)

**What's Missing:**
- WFO folding strategy algorithm
- Gap handling between folds
- Walk-Forward Efficiency (WFE) metric
- Checkpoint management per fold
- Fold-level reporting & comparison

**Why Critical:**
- Out-of-sample validation impossible without it
- Gate 6 (WFE) depends on this
- Confidence in backtest results low without WFO

**Implementation:** Story in optimization epic or new E-WFO
**Effort:** 20-25 story points
**Suggested Stories:**
1. S-WFO-001: WFO architecture & fold calculation (8 pts)
2. S-WFO-002: Gap handling between folds (6 pts)
3. S-WFO-003: WFE metric calculation (5 pts)
4. S-WFO-004: Fold checkpoint management (4 pts)
5. S-WFO-005: Fold-level reporting (2 pts)

**Dependencies:**
- ← CRITICAL-6 (conditional search space for fold-specific params)
- → CRITICAL-7 (WFE feeds into Gate 6)

**Success Criteria:**
- Fold sizing algorithm matches best practices (typical: 30-40% test fold)
- Gap handling prevents forward-looking bias
- WFE calculation matches academic definition
- All fold checkpoints preserved & recoverable
- ≥90% test coverage

**Owner:** Optimization Lead
**Timeline:** Weeks 2-4 (early start, feeds to gates)

---

## Phase 2: Major Gaps (SHOULD FIX)

These 12 major gaps should be addressed **before feature lock** (week 12-14). Many can be added to existing epics or run in parallel.

### MAJOR-1: Parameter Profile Validation
**Add to:** E-STRATEGY-LIFECYCLE (S-STRATEGY-001)
**Effort:** 5-8 pts | **Priority:** P1
**What:** Enforce active_param_count ≤ 70 rule
**Timeline:** Weeks 3-4

### MAJOR-2: Trial Artifact Schema
**Add to:** E-JOURNAL-SCHEMA (new story)
**Effort:** 8-13 pts | **Priority:** P1
**What:** Define trial_id, parameters, results, checkpoint structure
**Timeline:** Weeks 2-3

### MAJOR-3: Cost Impact Tracking
**Add to:** E-TELEMETRY-METRICS or E-JOURNAL-SCHEMA
**Effort:** 10-13 pts | **Priority:** P1
**What:** Per-trade commission/slippage logging & aggregation
**Timeline:** Weeks 4-6

### MAJOR-4: Signal Coverage Diagnostics Schema
**Add to:** Optimization epic
**Effort:** 8-13 pts | **Priority:** P1
**What:** signal_coverage.json schema for RCA
**Timeline:** Weeks 3-5

### MAJOR-5: Approval Workflow Expansion
**Expand:** S-STRATEGY-002 in E-STRATEGY-LIFECYCLE
**Effort:** 13-18 pts | **Priority:** P1
**What:** Gate-based promotion (can't promote until gates pass)
**Timeline:** Weeks 5-8

### MAJOR-6: Keyboard Accessibility (ARIA)
**Add to:** E-TELEMETRY-METRICS (dashboard)
**Effort:** 8-13 pts | **Priority:** P1
**What:** ARIA roles, keyboard nav, screen reader testing
**Timeline:** Weeks 10-12

### MAJOR-7: Tablet Responsiveness
**Add to:** E-TELEMETRY-METRICS (dashboard)
**Effort:** 5-8 pts | **Priority:** P1
**What:** Responsive breakpoints (1024px+), touch-friendly
**Timeline:** Weeks 10-12

### MAJOR-8: Sentiment Data Integration
**Add to:** E-NEWS-OVERLAY
**Effort:** 13-25 pts | **Priority:** P1 (ARCHITECTURE DECISION FIRST)
**What:** Choose sentiment source (manual, API, ML) + implement
**Timeline:** Weeks 6-8 (decision) + 9-11 (implementation)

### MAJOR-9: Event Map Maintenance SLA
**Add to:** E-CALENDAR-SAFETY
**Effort:** 5-8 pts | **Priority:** P1
**What:** Define refresh cadence, SLA, fallback
**Timeline:** Weeks 6-8

### MAJOR-10: Rollback Criteria & Risk Scoring
**Add to:** E-ROCKETS-GOVERNANCE
**Effort:** 8-13 pts | **Priority:** P1
**What:** Automatic rollback triggers, risk score algorithm
**Timeline:** Weeks 8-10

### MAJOR-11: Operator Health Badge Tuning
**Add to:** QA/Testing
**Effort:** 3-5 pts | **Priority:** P1
**What:** Tune "stalled" threshold, ETA accuracy
**Timeline:** Weeks 11-12

### MAJOR-12: Constraint Enforcement Algorithm
**Add to:** E-ROCKETS-GOVERNANCE
**Effort:** 13-18 pts | **Priority:** P1
**What:** Max leverage (5x), tier caps, allocation limits
**Timeline:** Weeks 8-10

---

## Phase 3: Minor Gaps (NICE TO FIX)

These 7 minor gaps can be addressed in Phase 2 or deferred to later releases.

| Gap | Effort | Priority | Timeline |
|-----|--------|----------|----------|
| MINOR-1: CI/CD Versioning | 3-5 pts | P2 | Weeks 13-14 |
| MINOR-2: Event-Map Versioning | 1-2 pts | P2 | Weeks 8-9 |
| MINOR-3: Cost Breakdown Formula | 2-3 pts | P2 | Weeks 13-14 |
| MINOR-4: ETA Tuning | 3-5 pts | P2 | Weeks 12-13 |
| MINOR-5: Mobile Navigation | 5-8 pts | P3 | Phase 2 |
| MINOR-6: Calendar Fallbacks | 5-8 pts | P2 | Weeks 8-10 |
| MINOR-7: Sentiment Thresholds | 2-3 pts | P2 | Weeks 9-11 |

**Total:** 21-34 story points (1-2 weeks effort)

---

## Sequencing & Critical Path

### Week 1: CRITICAL-6 Specification
```
MUST COMPLETE BEFORE ANY CODING:
├─ Conditional Optuna algorithm spec
├─ Profile validation rules
├─ Pruning integration spec
├─ Trial artifact schema
└─ Example trial execution logs
```

**Owner:** Optimization Architect
**Resources:** 1 architect, 2 senior engineers
**Output:** Signed-off specification (0 conflicts, reviewable)

### Weeks 2-5: Foundation Epics (Parallel)
```
├─ E-MULTI-TF (weeks 2-5)
├─ E-DFF (weeks 2-6)
├─ CRITICAL-8 WFO (weeks 2-4)
└─ E-STRATEGY-LIFECYCLE refinements (weeks 2-5)

ALSO PARALLEL:
├─ E-JOURNAL-SCHEMA refinements (weeks 2-4)
└─ E-TELEMETRY-METRICS refinements (weeks 2-5)
```

**Resources:** 12-15 engineers (distributed)
**Parallel streams:** 4-5 teams working independently

### Weeks 6-10: Gate System & Risk Management
```
├─ E-QUALITY-GATES (weeks 6-10)
├─ E-CALENDAR-SAFETY (weeks 6-8)
├─ E-ROCKETS-GOVERNANCE start (weeks 8-10)
└─ E-AUDIT-TRAIL refinements (weeks 6-8)
```

**Resources:** 8-10 engineers
**Critical:** Gates must be done before Rockets integration

### Weeks 9-12: Advanced Features
```
├─ E-NEWS-OVERLAY (weeks 9-11)
├─ E-ROCKETS-GOVERNANCE complete (weeks 8-12)
├─ E-COMPARE-WORKFLOW refinements (weeks 9-11)
└─ Major gap stories in parallel (weeks 8-12)
```

**Resources:** 10-12 engineers
**Parallel:** Most work independent after week 8

### Week 12-14: Feature Lock & Polish
```
├─ All critical gaps complete
├─ Major gaps resolved
├─ Final QA & accessibility testing
├─ Documentation & runbooks
└─ Preparation for Stage 2 review
```

**Resources:** 8-10 engineers + QA

---

## Resource Allocation

### By Epic (Story Points & Duration)

| Epic | Points | Weeks | Team Size | Owner |
|------|--------|-------|-----------|-------|
| **CRITICAL-6 (Spec)** | 25-30 | 1 | Architect + 2 | Optimization Architect |
| **E-MULTI-TF** | 40-50 | 4 | 3-4 | Optimization Lead |
| **E-DFF** | 30-40 | 5 | 2-3 | Risk Lead |
| **E-WFO** | 20-25 | 3 | 2 | Optimization Lead |
| **E-CALENDAR-SAFETY** | 25-30 | 3 | 2 | Risk/Ops Lead |
| **E-NEWS-OVERLAY** | 20-25 | 3 | 2 | ML/Alpha Lead |
| **E-QUALITY-GATES** | 40-50 | 5 | 3-4 | QA Lead |
| **E-ROCKETS** | 35-45 | 5 | 3 | Portfolio Lead |
| **Provided Epics (1-5)** | 122 | 12 | 4-5 | Multi-team |
| **Major Gaps** | 110-155 | 8 | 4-6 | Distributed |
| **TOTAL** | 467-550 | 14-18 | 28-35 | Implementation Lead |

### Calendar (Gantt Simplified)

```
Week:  1  2  3  4  5  6  7  8  9 10 11 12 13 14
───────────────────────────────────────────────────
CRIT-6 ██
E-MTF     ██████████
E-DFF     ████████████
E-WFO     ████████
E-STRAT   ██████████
E-JOURN   ██████████
E-TELEM   ██████████
E-COMP    ██████████
E-AUDIT   ██████████
E-CALIN        ██████
E-NEWS           ████████
E-GATES        ███████████
E-ROCKETS         ███████████
Major       ╔════════════════╗
Minor          ╚═════╝
Stage2                 ╔════╝

Key: Each bar = team working on epic
     ╔═══╝ = can start after blocker
```

---

## Definition of Done

### For Each Critical Epic

✅ **Acceptance Criteria Met**
- All stories pass AC (unit tested)
- No technical debt accrued
- Code reviewed & merged

✅ **Quality Gates**
- Test coverage ≥90% (CRITICAL) or ≥85% (MAJOR)
- No P0/P1 bugs
- Lint/format passing
- Type checking passing

✅ **Documentation**
- Implementation matches spec
- API documentation complete
- Example code provided
- Runbook/operational guide

✅ **Integration**
- Works with dependent epics
- No regressions in existing features
- Database migrations (if needed) tested

✅ **Performance**
- Benchmarks within SLA
- No memory leaks
- Latency acceptable

---

## Risk Mitigation

### Top Risks

**Risk 1: CRITICAL-6 spec takes longer than 1 week**
- **Mitigation:** Pre-schedule 8-10 hours with team week 0
- **Plan B:** Use iterative spec (spec-a-bit, code-a-bit, refine)

**Risk 2: Multi-TF conflicts with existing codebase**
- **Mitigation:** Create feature branch, PR early & often
- **Plan B:** Refactor codebase for TF-agnostic patterns first

**Risk 3: Sentiment data source unavailable/expensive**
- **Mitigation:** Start with MVP (manual lookup table)
- **Plan B:** Delay E-NEWS-OVERLAY to Phase 2

**Risk 4: Gate system too complex (>50 story points)**
- **Mitigation:** Scope: implement 4 gates (PSR, FDR, PBO, WFE) in Phase 1
- **Plan B:** Other 3 gates (Correlation, MC, Manual) in Phase 2

**Risk 5: Epics slip, compound delays**
- **Mitigation:** Track burndown weekly, escalate blockers
- **Plan B:** Reduce scope (minor gaps → Phase 2)

---

## Success Criteria (Go-Live Gate)

Before Stage 2 Adversarial Review, all of the following must be TRUE:

✅ **All Critical Gaps Resolved**
- 8 critical epics complete (or scoped for Phase 2)
- CRITICAL-6 spec signed off by 3+ engineers
- CRITICAL-7 (gates) shows all 7 gates passing on test strategies

✅ **Major Gaps Addressed**
- 12 major gaps in backlog (with acceptance criteria)
- At least 6 major gaps completed

✅ **Epic Integration**
- 5 provided epics + 8 critical epics tested together
- No feature conflicts
- State machine + journal schema + gates work together

✅ **Quality Metrics**
- Overall test coverage ≥85%
- No P0 bugs
- Lint & type checking 100% passing

✅ **Documentation**
- Brief, PRD, Architecture, UX, Epics all in sync
- Implementation discoveries documented
- New conflicts resolved

✅ **Readiness for Stage 2**
- Detailed spec for each epic reviewed
- Test plans for each gate defined
- Risk register updated

---

## Stakeholder Sign-Off

| Role | Approval | Signature | Date |
|------|----------|-----------|------|
| Product Owner | Plan accepted | ________________ | _____ |
| Engineering Lead | Resources approved | ________________ | _____ |
| Optimization Architect | CRITICAL-6 spec plan | ________________ | _____ |
| QA Lead | Gate system scope | ________________ | _____ |
| Implementation Lead | Timeline & risks | ________________ | _____ |

---

## Appendix: Epic Templates

### New Epic Template

```markdown
# Epic Title

## Context
[What's missing from the codebase?]
[Why is it critical?]
[What depends on it?]

## Scope
- Story 1: [description] (X points)
- Story 2: [description] (Y points)
- Story 3: [description] (Z points)
[total: X+Y+Z points]

## Dependencies
- Blocks: [which epics/stories depend on this?]
- Blocked by: [which must be done first?]

## Success Criteria
- All stories pass AC ✓
- Test coverage ≥85% ✓
- No P0 bugs ✓
- Documentation complete ✓

## Timeline
Start: Week X | End: Week Y (Z weeks)

## Owner
[Name & team]

## Risks
- Risk A: [mitigation]
- Risk B: [mitigation]
```

---

**Plan Status:** ✅ READY FOR APPROVAL
**Next Step:** Leadership sign-off + Schedule CRITICAL-6 refinement workshop
**Owner:** Implementation Lead

---

*Document Version: 1.0*
*Created: 2026-02-26*
*Last Updated: 2026-02-26*
