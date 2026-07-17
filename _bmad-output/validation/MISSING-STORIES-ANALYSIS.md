---
title: "Missing Stories & Scope Analysis"
project: katana-vectorbt
generated: 2026-02-27
author: Claude Code
analysis_type: STORY_COVERAGE_GAP
---

# Missing Stories & Scope Creep Analysis

## 1. MISSING STORIES FROM BRIEF (NOT IN EPICS)

### 1.1 Critical Missing Stories (Blocking v1.0)

#### Story Gap #1: Audit Logging Framework
**Brief Reference:** Lines 1849-1858 ("Audit Logging" section)

**Requirement:**
```
System MUST log:
- parameter_set
- data_hash
- objective scores
- live fills
- slippage
- kill-switch triggers
- gate evaluation results
```

**Current Status:**
- ❌ Not explicitly in Epic 1 story list
- ⚠️ Partially implied by story-1-0-5-data-contract

**Recommended Story:**
```
Epic: Epic 1 (Dashboard Foundation)
Story ID: story-1-6-audit-logging-framework
Title: Implement comprehensive audit logging for all operations
Points: 8
Acceptance Criteria:
- [ ] Log all parameter sets with timestamp
- [ ] Track data_hash for every optimization run
- [ ] Record all objective scores per trial
- [ ] Log all live trade fills (price, size, time, slippage)
- [ ] Track all kill-switch triggers (drawdown, calendar, etc.)
- [ ] Record gate evaluation results with reasons
- [ ] Logs stored in database (SQLite) with structured schema
- [ ] 100% audit trail completeness
```

**Priority:** HIGH (blocks live validation)

---

#### Story Gap #2: Data Hash & Reproducibility Contract
**Brief Reference:** Lines 1925-1932 ("Dataset Lineage" section)

**Requirement:**
```
- data_hash = SHA256 of concatenated OHLCV dataset
- Hash stored in: optimization config, Run Journal, results artifacts
- Reproducibility: Same data_hash + same config_hash + same code_rev = identical results
- Live performance compared only if data lineage matches original optimization dataset
```

**Current Status:**
- ⚠️ story-1-0-5-data-contract-definition exists but may not cover lineage fully
- ❌ No explicit data_hash tracking in optimization flow

**Recommended Story:**
```
Epic: Epic 1 (Dashboard Foundation)
Story ID: story-1-0-6-data-lineage-tracking
Title: Implement data hash tracking for reproducibility
Points: 5
Acceptance Criteria:
- [ ] Compute SHA256 hash of OHLCV dataset before optimization
- [ ] Store data_hash in optimization config
- [ ] Embed data_hash in all results artifacts
- [ ] Implement lineage comparison (live vs backtest)
- [ ] Prevent live deployment if data_hash mismatches
- [ ] Run Journal includes data_hash for every run
- [ ] Tests verify identical results with same data_hash + config
```

**Priority:** HIGH (blocks v1.0 reproducibility gate)

---

#### Story Gap #3: Cold Start Policy Implementation
**Brief Reference:** Lines 1837-1842 ("Cold Start Policy" section)

**Requirement:**
```
Strategy cannot go live unless:
- IS Sharpe ≥ 1.0
- OOS Sharpe ≥ 0.8 AND OOS degradation ≤ 15%
- PBO ≤ 0.3
```

**Current Status:**
- ⏳ story-2b gates might cover this but not explicitly named
- ❌ No dedicated Cold Start Policy story

**Recommended Story:**
```
Epic: Epic 2b (Walk-Forward Validation)
Story ID: story-2b-9-cold-start-policy
Title: Enforce cold start policy before live deployment
Points: 5
Acceptance Criteria:
- [ ] Implement gate: IS Sharpe ≥ 1.0
- [ ] Implement gate: OOS Sharpe ≥ 0.8
- [ ] Implement gate: OOS degradation ≤ 15%
- [ ] Implement gate: PBO ≤ 0.3
- [ ] All 4 gates must PASS before "ready for live" status
- [ ] Dashboard shows cold start pass/fail for each strategy
- [ ] Strategy rejected to "FAILED" state if any gate fails
- [ ] Test with synthetic data: verify correct rejections
```

**Priority:** HIGH (blocks Live Gate A)

---

#### Story Gap #4: Slippage Monitoring & Validation
**Brief Reference:** Lines 1844-1847 ("Slippage Model" section)

**Requirement:**
```
- Comparison Window: T-20 to T+20 bars around entry/exit (40-bar symmetric)
- Metric: Avg slippage in window vs backtest assumption
- Gate: PASS if |actual - expected| / expected ≤ 50%
```

**Current Status:**
- ⚠️ Mentioned in Epic 3 (Live Trading) but no explicit story
- ❌ No detailed slippage analysis framework

**Recommended Story:**
```
Epic: Epic 3 (Live Trading)
Story ID: story-3-5-slippage-monitoring
Title: Implement live slippage monitoring & validation gate
Points: 8
Acceptance Criteria:
- [ ] Capture live execution price vs order price
- [ ] Calculate average slippage in T-20 to T+20 window
- [ ] Compare with backtest assumptions
- [ ] Implement gate: |actual - expected| / expected ≤ 50%
- [ ] Alert if slippage exceeds 30% of modeled edge
- [ ] Log slippage per trade in database
- [ ] Dashboard metric: "Slippage Impact (%)"
- [ ] Escalate to RCA if gate fails
```

**Priority:** HIGH (blocks Live Gate A)

---

#### Story Gap #5: Kill-Switch Architecture
**Brief Reference:** Lines 1606-1621 (Rockets kill-switches section) + 1787-1812 (Live Gates)

**Requirement:**
```
Rockets:
- Individual DD kill-switch: 40% MaxDD → blacklist 7 days + re-opt
- Portfolio DD kill-switch: 50% MaxDD → freeze new entries + re-opt

Core strategies (Live Gate A):
- Trade frequency check
- Position sizing check
- Max leverage check
- Slippage budget check
- Execution hygiene check
```

**Current Status:**
- ⏳ Epic G (Rockets) has stories but kill-switch details may be implicit
- ❌ No dedicated kill-switch orchestration story

**Recommended Story:**
```
Epic: Epic 3 (Live Trading) + Epic G (Rockets)
Story ID: story-3-6-kill-switch-orchestration
Title: Implement automatic kill-switches for drawdown & risk limits
Points: 13
Acceptance Criteria:
- [ ] Monitor individual strategy MaxDD
- [ ] Trigger kill-switch at 40% DD (core), 40% DD (rocket)
- [ ] Automatic blacklist for 7 days post-trigger
- [ ] Monitor portfolio-level MaxDD (rocket bucket)
- [ ] Trigger portfolio kill-switch at 50% DD
- [ ] Freeze new entries on portfolio kill-switch
- [ ] Trigger re-optimization flow
- [ ] Log all kill-switch events with trigger values
- [ ] Dashboard shows kill-switch status per strategy
- [ ] Tests verify correct trigger conditions
```

**Priority:** CRITICAL (blocks live safety)

---

### 1.2 Important Missing Stories (Should-Have for v1.0)

#### Story Gap #6: Risk Mode Presets Implementation
**Brief Reference:** Lines 1860-1872 ("Risk Mode Presets" section)

**Risk Modes:**
```
| Mode | DFF SL Mult | DFF TP Mult | Risk/Trade | Leverage Cap | Pyramid Levels |
|------|-------------|-------------|------------|--------------|----------------|
| Conservative | 0.5x | 2.0x | 0.5% | 1x | 1 |
| Moderate | 1.0x | 3.0x | 1.5% | 1x | 2 |
| Aggressive | 1.5x | 5.0x | 3.0% | 2x | 3 |
| Rocket-Catching | 2.5x | 10.0x | 5.0% | 5x | 5 |
```

**Current Status:**
- ⏳ Mentioned in Brief but no explicit Epic story
- ❌ DFF details deferred to Phase 4 (Epic R)

**Recommended Story:**
```
Epic: Epic 2a (Optimization Framework) [Phase 2] + Epic R (Phase 4)
Story ID: story-2a-7-risk-mode-presets (Phase 2 baseline)
Title: Implement risk mode presets for strategy configuration
Points: 8 (Phase 2) + 8 (Phase 4)
Phase 2 Acceptance Criteria:
- [ ] Define 4 risk modes (Conservative, Moderate, Aggressive, Rocket-Catching)
- [ ] Create config YAML with mode presets
- [ ] Phase 2: Use ATR-based SL/TP with mode multipliers
- [ ] Leverage cap per mode applied in position sizing
- [ ] Dashboard: Risk mode selector per strategy
- [ ] Tests verify correct SL/TP distances per mode
Phase 4 Acceptance Criteria:
- [ ] Extend to full DFF with per-role source_type selection
- [ ] Optuna search space gated by risk mode
- [ ] Pyramid levels applied in position sizing
- [ ] All 4 risk modes tested in live
```

**Priority:** MEDIUM (can use ATR-only baseline in Phase 2)

---

#### Story Gap #7: Factory CLI & Mass Optimization Entry Point
**Brief Reference:** Lines 1874-1885 ("CLI Interface" section)

**Requirement:**
```bash
python -m katana.mass_optimize \
  --exchange amarkets \
  --pair EURUSD \
  --timeframe 1h \
  --optimization-level both \
  --n-trials 1000 \
  --n-workers 10 \
  --resume
```

**Current Status:**
- 📋 Deferred to Epic C (Control Plane) which is PLANNED
- ❌ No explicit Phase 2 story

**Recommended Story:**
```
Epic: Epic C (Control Plane & Autonomy Loop CLI) [Phase 2 or standalone]
Story ID: story-c-1-mass-optimize-cli
Title: Implement mass_optimize CLI for factory orchestration
Points: 13
Acceptance Criteria:
- [ ] CLI command: python -m katana.mass_optimize
- [ ] Arguments: --exchange, --pair, --timeframe, --optimization-level, --n-trials, --n-workers, --resume
- [ ] Filtering by exchange (amarkets, kucoin, all)
- [ ] Filtering by pair (EURUSD, BTC/USDT, etc.)
- [ ] Filtering by timeframe (1m, 5m, 15m, 1h, 4h, 1d)
- [ ] Optimization levels: regime, strategy, both
- [ ] Parallel execution with N workers
- [ ] Resume capability from checkpoint
- [ ] Progress output to console + Run Journal
- [ ] Exit code 0 on success, 1 on failure
- [ ] Tests verify all argument combinations
```

**Priority:** HIGH (blocks factory automation)

---

## 2. SCOPE CREEP ANALYSIS (EPICS NOT IN BRIEF)

### 2.1 Deferred Epics (Explicitly out-of-scope for v1.0)

#### Epic 3A: API & Integration Layer
**Status:** 📋 PLANNED (Phase 2, explicit deferral)

**Brief Reference:** Explicitly out-of-scope (single-user, local-only)

**Analysis:**
- ✅ Correctly deferred; Brief focuses on single-user desktop
- ✅ REST API is secondary feature; can add post-v1.0
- ✅ No conflict with v1.0 timeline

**Scope Impact:** ZERO - explicitly deferred

---

#### Epic C: Control Plane & Autonomy Loop CLI
**Status:** 📋 PLANNED (Phase 2, partial deferral)

**Brief Reference:** Implicit in "Strategy Factory" and "mass_optimize CLI"

**Analysis:**
- ✅ Autonomy loop exists (Epic M marked COMPLETE)
- ✅ CLI formalization deferred but not blocking
- ⚠️ Phase 2 should include basic CLI (story-c-1-mass-optimize-cli)
- ✅ Full control plane can be Phase 2 or deferred

**Scope Impact:** MINIMAL - can move part of control plane to Phase 2

---

#### Epic D: Data Pipeline & Caching System
**Status:** 📋 PLANNED (deferred, non-blocking)

**Brief Reference:** Implicit in "OHLCVStore PostgreSQL backend"

**Analysis:**
- ✅ Core data ingestion is in-scope (vectorbt + OHLCVStore)
- ✅ Advanced caching layer is nice-to-have, not MVP
- ✅ No blocking dependency for v1.0

**Scope Impact:** ZERO - correctly deferred

---

#### Epic J: Parameter Optimization & Sensitivity Analysis
**Status:** ⏳ PLANNED (Wave 4, Grid Search)

**Brief Reference:** Mentioned as "parameter sensitivity" in Phase 2

**Analysis:**
- ✅ Phase 2 covers Optuna (Epic 2a)
- ✅ Grid search / sensitivity is enhancement, not MVP
- ✅ Can add in Phase 4 (Wave 4)

**Scope Impact:** MINIMAL - Phase 2 has baseline, Phase 4 enhances

---

### 2.2 Wave 4 Features (Advanced, explicitly future)

#### Epic Q: Multi-Timeframe Independent Execution
**Status:** 📋 PLANNED (Phase 4, Wave 4)

**Brief Reference:** Lines 600-650 (6 independent TF caches)

**Analysis:**
- ✅ Architecture is in Brief (6 TF, per-TF Optuna, per-TF HNSW)
- ✅ Formalization deferred to Phase 4; reasonable
- ✅ Phase 2 can start with single TF or limited TFs
- ⚠️ Phase 2 should keep architecture extensible

**Scope Impact:** LOW - well-scoped future feature

---

#### Epic R: Distance Function Factory (DFF)
**Status:** 📋 PLANNED (Phase 4, Wave 4)

**Brief Reference:** Lines 300-400 (6 DFF source types)

**Analysis:**
- ✅ Architecture is in Brief (ATR, StdDev, BB, Range, Fixed %, Corwin-Schultz)
- ✅ Phase 2 uses ATR-only baseline
- ✅ Full DFF in Phase 4; reasonable
- ⚠️ Phase 2 implementation must allow DFF extension

**Scope Impact:** LOW - Phase 2 uses baseline, Phase 4 extends

---

#### Epic S: Calendar Safety & News Integration
**Status:** 📋 PLANNED (Phase 4, Wave 4)

**Brief Reference:** Lines 656-750 (detailed calendar/news architecture)

**Analysis:**
- ✅ Brief describes: HARD (120/60) + SOFT (30/30)
- ✅ Phase 2 can skip advanced calendar/news
- ⚠️ Phase 2 should allow calendar filtering placeholder
- ✅ Full integration in Phase 4

**Scope Impact:** LOW - Phase 4 addition, not MVP blocking

---

#### Epic T: Rockets Venture Capital Portfolio
**Status:** 📋 PLANNED (Phase 4, Wave 4)

**Brief Reference:** Lines 570-621 (Rockets architecture)

**Analysis:**
- ✅ Rockets business logic is in Brief
- ⚠️ Epic G exists (Multi-Rocket Portfolio COMPLETE) but EPicT is formalization
- ✅ Phase 2 can have single-strategy portfolio
- ✅ Rockets (10-bucket) in Phase 4

**Scope Impact:** MINIMAL - Phase 2 has basic portfolio, Phase 4 enhances

---

#### Epic U: 100+ Parameters Tuning Framework
**Status:** 📋 PLANNED (Phase 4, Wave 4)

**Brief Reference:** Lines 360-400 (115 parameters, 16 categories)

**Analysis:**
- ✅ Parameter list is in Brief (canonical values table)
- ✅ Phase 2 uses subset (~50 parameters)
- ✅ Full 115-parameter expansion in Phase 4
- ✅ Properly scoped

**Scope Impact:** LOW - Phase 2 baseline, Phase 4 expansion

---

#### Epic V: Large-Scale Optuna v2 Orchestration
**Status:** 📋 PLANNED (Phase 4, Wave 4)

**Brief Reference:** Lines 430-460 (Optuna v2, multi-study, pruning)

**Analysis:**
- ✅ Optuna v2 baseline in Phase 2 (Epic 2a)
- ✅ Multi-study orchestration (per-TF, per-pair) in Phase 4
- ✅ Properly scoped as enhancement

**Scope Impact:** LOW - Phase 2 has single-study, Phase 4 orchestrates multi-study

---

#### Epic W: Performance Dashboard & Monitoring
**Status:** 📋 PLANNED (Phase 4, Wave 4)

**Brief Reference:** Lines 1947-1954 (Streamlit components Phase 2)

**Analysis:**
- ✅ Brief mentions Phase 2 dashboard components
- ⚠️ Advanced monitoring (heatmaps, KDE) deferred to Phase 4
- ✅ Epic 5 covers Phase 2 reporting basics

**Scope Impact:** MINIMAL - Phase 2 has basic, Phase 4 enhances

---

### 2.3 Explicitly Out-of-Scope (Not v1.0)

#### Epic 9: Multi-Account & Collaboration (Phase 2+)
**Status:** ❌ Out-of-scope for v1.0 (single-user)

**Brief Reference:** Lines 2136-2138 ("Out of Scope for v1.0")

**Analysis:**
- ✅ Correctly excluded
- ✅ No conflict with v1.0

**Scope Impact:** ZERO

---

#### Epic 10: Compliance & Security (Phase 3+)
**Status:** ❌ Out-of-scope for v1.0 (deferred Phase 3)

**Brief Reference:** Lines 2136-2141 ("Out of Scope for v1.0")

**Analysis:**
- ✅ Correctly deferred
- ✅ No blocking dependency

**Scope Impact:** ZERO

---

## 3. SCOPE CREEP VERDICT

### Summary

| Category | Count | Impact | Action |
|----------|-------|--------|--------|
| **Missing Phase 2 Stories** | 7 | HIGH | Add to Phase 2 planning |
| **Deferred Epics (explicit)** | 10+ | ZERO | Correctly deferred |
| **Wave 4 Features** | 7 | LOW | Phase 4 scope |
| **Out-of-Scope (v1.0)** | 2 | ZERO | Correctly excluded |

### Verdict: ✅ **MINIMAL SCOPE CREEP**

**Findings:**
1. ✅ No unplanned scope bloat; all deferred items explicitly marked
2. ✅ Epic structure correctly phases features (MVP → Phase 4 → Future)
3. ⚠️ 7 missing stories in Phase 2 need explicit implementation (non-blocking)
4. ✅ Release gates properly represented in Epic roadmap

---

## 4. RECOMMENDATIONS

### 4.1 Immediate Actions (Next 1-2 weeks)

Priority: **CRITICAL**

1. **Add 7 missing stories to Phase 2 Epics:**
   - story-1-6-audit-logging-framework → Epic 1
   - story-1-0-6-data-lineage-tracking → Epic 1
   - story-2b-9-cold-start-policy → Epic 2b
   - story-3-5-slippage-monitoring → Epic 3
   - story-3-6-kill-switch-orchestration → Epic 3
   - story-2a-7-risk-mode-presets (baseline) → Epic 2a
   - story-c-1-mass-optimize-cli → Epic C or standalone Phase 2

2. **Verify existing story coverage:**
   - Confirm story-1-0-5-data-contract covers OHLCV + trade logs + reproducibility
   - Verify Epic 2b stories include all 7 gates
   - Confirm Epic 3 includes slippage monitoring
   - Check Epic G for kill-switch implementation

3. **Extend Phase 2 architecture docs:**
   - Add extensibility notes for DFF (Phase 2 ATR-only, Phase 4 full)
   - Add extensibility notes for Risk Modes (Phase 2 basic, Phase 4 advanced)
   - Add extensibility notes for Calendar/News (Phase 2 skip, Phase 4 full)

### 4.2 Phase 2 Planning (Weeks 2-3)

Priority: **HIGH**

1. **Refine Epic 2a, 2b, 3, 4, 5 story details**
   - Add points estimates for new stories
   - Define inter-story dependencies
   - Identify critical path stories

2. **Create Phase 2 roadmap with gates**
   - Week 1-4: Epic 1 (already complete)
   - Week 5-8: Epic 2a, 2b (core optimization + validation)
   - Week 9-12: Epic 3, 4 (live trading + analytics)
   - Week 13-14: Epic 5 (reporting + operator panel)
   - Week 15+: Live validation plan (8 weeks)

3. **Document Phase 2 architectural decisions:**
   - Single TF vs multi-TF
   - ATR-only vs DFF baseline
   - Basic risk modes vs full spectrum
   - Calendar integration yes/no

### 4.3 Wave 4 / Phase 4 Planning (Concurrent)

Priority: **MEDIUM**

1. **Finalize Wave 4 epic details (Epics Q-W)**
   - Link to Phase 2 baseline functionality
   - Define extension points
   - Create Phase 4 dependency chain

2. **Create Phase 4 roadmap (12-16 weeks post-Phase 2)**
   - Epic Q: MTF execution (2 weeks)
   - Epic R: DFF framework (3 weeks)
   - Epic S: Calendar/News (2 weeks)
   - Epic T: Rockets portfolio (2 weeks)
   - Epic U: 115+ parameters (2 weeks)
   - Epic V: Optuna orchestration (2 weeks)
   - Epic W: Advanced dashboard (2 weeks)

---

## 5. APPENDIX: STORY TEMPLATE FOR MISSING STORIES

### Template for Adding to Epics File

```markdown
### story-[EPIC-ID]-[SEQUENCE]-[slug]

**Title:** [Human-readable title]

**Epic:** [Epic Name]

**Type:** [Feature | Enhancement | Infrastructure]

**Story Points:** [5|8|13|21]

**Priority:** [HIGH | MEDIUM | LOW]

**Description:**
[Detailed description from Brief or requirements]

**Acceptance Criteria:**
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

**Dependencies:**
- story-X-Y (must complete before)

**Testing:**
- Unit tests: [scope]
- Integration tests: [scope]
- Manual validation: [scope]

**Success Metrics:**
- Metric 1: [target]
- Metric 2: [target]

**Implementation Notes:**
- Architecture: [key decisions]
- Reuse: [existing components]
- Risks: [known risks]
```

---

**Report Status:** ✅ COMPLETE
**Generated:** 2026-02-27
**Next Review:** Phase 2 Story Refinement
**Owner:** Claude Code
