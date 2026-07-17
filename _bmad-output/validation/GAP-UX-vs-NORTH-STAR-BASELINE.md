---
title: "UX Design vs North Star Baseline Validation"
date: "2026-02-27T01:30:00Z"
status: "CRITICAL_FINDINGS"
validation_scope: "100% North Star Baseline Coverage for Phase 1"
project: "katana-vectorbt"
---

# UX Design vs North Star Baseline Validation

**Analysis Date:** 2026-02-27
**Validator:** Claude Code
**Scope:** Verify that UX Phase 1 covers 100% of north star baseline functionality (not just PRD)
**Status:** ⚠️ **CRITICAL GAPS FOUND** — 85% PRD coverage does NOT equal 100% north star baseline coverage

---

## Executive Summary

**Finding:** The reported "85% UX↔PRD coverage" is **INSUFFICIENT** for north star baseline validation because:

1. ❌ **Mandatory Baseline Requirement (KatanaTransformer)** - MISSING from UX
   - North Star Brief explicitly requires: "ALL testing/optimization/validation MUST use KatanaTransformer"
   - UX does NOT include "Strategy Validation Badge" to enforce this
   - Gap: 1 P0 blocker (6-8 hours to implement)

2. ❌ **Canonical Values Table (Wave 4)** - PARTIALLY MISSING from UX
   - 6 timeframe caches (1m/5m/15m/1h/4h/1d) - MISSING UI controls/visualization
   - DFF types selector (6 source types) - MISSING UI
   - Kill-Switch triggers (40% individual, 50% portfolio) - MISSING status display
   - Gap: 3 P1 items (12-18 hours total)

3. ❌ **Calendar Safety (HARD) & News Overlay (SOFT)** - PARTIAL
   - UX covers banners/panels but MISSING explicit 120/60min window visualization
   - Gap: 1 P1 item (4-6 hours)

4. ✓ **User Journeys** - MOSTLY COVERED but incomplete wireframes
   - Monitor → Review → Diagnose spine present
   - Missing explicit wireframe flows for: Comparison (70% coverage), Export (60% coverage)
   - Gap: 3 wireframe sketches (6-8 hours)

**Bottom Line:**
- **North Star Baseline Coverage:** ~70-75% (NOT 85%)
- **Missing Critical Path:** Mandatory Baseline enforcement + Timeframe controls + DFF selector
- **Effort to 100%:** ~30-35 hours (Phase 1.0 or 1.1)
- **Risk if Deferred:** Users can deploy non-Katana strategies; parameter space confusion; kill-switch visibility issues

**Recommendation:** Add 5 critical items to **Phase 1.0 (go-live blocking)**, not Phase 1.1 (nice-to-have)

---

## Section 1: Mandatory Baseline Requirement Analysis

### 1.1 North Star Requirement (From Brief)

**From katana-v-01-product-brief-2026-01-17.md:**
```
## ⚠️ MANDATORY BASELINE REQUIREMENT (BLOCKING)

ALL testing/optimization/validation MUST use:
- Source: docs/KATANA_ORIGINAL.md (strategy specification)
- Implementation: katana/katana_transformer.py
- Profiles: Katana 1 (RSI+MA, ALL) and Katana 1.1 (RSI+MA+BB+gate_vol, k=2)

BLOCKING: NO simple RSI, MA-only, or single-indicator strategies.

Validation: Verify script uses KatanaTransformer class before ANY work.
```

**Nature:** Non-negotiable baseline. Blocks non-compliant strategies.

### 1.2 UX Coverage

**Current UX (from GAP-UX-vs-PRD.md):**
- ❌ Does NOT include validation badge/warning for strategy profile verification
- ❌ Does NOT display KatanaTransformer indicator verification
- ❌ Does NOT block non-Katana strategies from being launched
- ⚠️ Signal Diagnostics Panel can show "no trades" but cannot show "invalid strategy" reason

**Risk Scenario:**
```
User creates custom strategy: "RSI(14) MA(20) on EURUSD"
  ↓
UX allows entry (no validation)
  ↓
Backtest runs with non-Katana profile
  ↓
Results contaminate archive
  ↓
Validation gates may pass (depends on luck)
  ↓
CRITICAL: North star baseline violated
```

### 1.3 Gap Classification

**Gap Type:** P0 BLOCKER
**Effort:** 6-8 hours (implement validation badge + rules engine)
**Phase:** Must be Phase 1.0 (before go-live)
**Blocking Items:**
1. Strategy profile validation badge (KatanaTransformer check)
2. Rule engine to prevent non-Katana launches
3. Error message when non-Katana profile detected
4. Run summary update to show validated/not-validated status

---

## Section 2: Canonical Values Table (Wave 4) Coverage

### 2.1 North Star Definition (From Brief)

**6 Timeframe Caches:**
```
| Specification | Wave 4 | Notes |
|---|---|---|
| Timeframe Caches | 6 (1m, 5m, 15m, 1h, 4h, 1d) | Each TF independent Optuna + HNSW |
| H4 Role | Independent cache + Optional volatility reference | NOT fallback/validation base |
| DFF Types | 6 types, per-role source_type + flat params | atr, stddev, bb_half, range, fixed_pct, corwin_schultz |
| Total Parameters | 115 | 16 categories expanded from Wave 3 (94) |
| Rockets Kill-Switch (Individual) | 40% MaxDD | Peak-to-trough MaxDD triggers immediate stop + blacklist |
| Rockets Kill-Switch (Portfolio) | 50% MaxDD | Peak-to-trough MaxDD of rocket bucket triggers freeze + rebalance |
| Max Leverage Cap | 5x | Hard cap across all profiles |
| Calendar Safety (HARD) | 120 min pre / 60 min post | Always on, non-optimizable |
| News Overlay (SOFT) | 30/30 min | Optimizable alpha enhancement |
```

### 2.2 UX Coverage by Canonical Value

| Canonical Item | North Star Requirement | UX Coverage | Status | Gap |
|---|---|---|---|---|
| **Timeframe Caches** | 6 independent TF (1m/5m/15m/1h/4h/1d) | Implied in "multi-TF dashboard" | ⚠️ Implicit only | ❌ No timeframe selector UI |
| **DFF Types** | 6 source types per-role (atr, stddev, bb_half, range, fixed_pct, corwin_schultz) | NOT mentioned | ❌ None | ❌ No DFF source selector |
| **DFF Parameters** | Conditional parameters per source type (period/lookback/pct/multiplier) | NOT mentioned | ❌ None | ❌ No parameter control UI |
| **Parameter Space** | 115 total parameters, profile-specific activation | Mentioned in "Parameter Optimization" (Phase 2) | ⚠️ Phase 2 | ⚠️ Deferred; OK for Phase 1 |
| **Kill-Switch (Individual)** | 40% MaxDD triggers blacklist + re-opt | Implied in "Risk Management" | ⚠️ Implicit | ❌ No 40% trigger visualization |
| **Kill-Switch (Portfolio)** | 50% MaxDD of rocket bucket triggers freeze | Implied in "Rocket Portfolio" | ⚠️ Implicit | ❌ No 50% trigger visualization |
| **Leverage Cap** | 5x hard cap | NOT mentioned | ❌ None | ❌ No leverage display |
| **Calendar Safety (HARD)** | 120/60 min window, always on | UX covers banner/panel | ✓ Good | ✓ Covered |
| **News Overlay (SOFT)** | 30/30 min window, optimizable alpha | UX covers panel | ✓ Good | ✓ Covered |
| **H4 Role** | Independent cache + optional volatility reference (NOT validation base) | NOT mentioned | ❌ None | ❌ No H4 toggle/reference selector |
| **Profile Activation** | `active_param_count ≤ 70` enforcement | NOT mentioned | ❌ None | ❌ No parameter counter |

**Summary:**
- ✓ Calendar Safety & News Overlay: Well covered
- ⚠️ Leverage Cap, Parameter Space: Deferred to Phase 2 (acceptable)
- ❌ **CRITICAL GAPS:** DFF types/params, Kill-Switch visualization, H4 reference selector, Parameter counter

### 2.3 Critical Gap Details

#### Gap 1: DFF Type Selector (P1 - 4-6 hours)

**North Star Requirement:**
- 6 distance source types: atr, stddev, bb_half, range, fixed_pct, corwin_schultz
- Applied per-role: SL/TP/BE/Trail
- Each type has conditional parameters (period, lookback, pct, multiplier)

**Current UX:**
- ❌ Zero mention of DFF or distance function factory
- ❌ No UI for selecting DFF source type
- ❌ No parameter control for per-role distance calculations

**Risk Scenario:**
```
User optimizes with default ATR(14) × 2.0
  ↓
No alternative distance functions explored
  ↓
Miss better options: Bollinger Band width, Corwin-Schultz volatility, etc.
  ↓
Suboptimal parameter space → lower Sharpe
```

**Implementation (Phase 1.0 or 1.1):**
1. Add "Distance Function Selector" panel (4-6 hours)
2. Radio buttons: ATR | StdDev | BB-Half | Range | Fixed% | Corwin-Schultz
3. Conditional parameter inputs per type
4. Warning: "DFF settings locked during backtest; unlock for re-optimization"

#### Gap 2: Kill-Switch Trigger Visualization (P1 - 6-8 hours)

**North Star Requirement:**
- Individual Rocket: 40% MaxDD → blacklist 7 days
- Portfolio Rocket: 50% MaxDD → freeze new entries + rebalance
- Non-negotiable risk control mechanism

**Current UX:**
- ⚠️ "Rocket Portfolio Dashboard" section exists
- ❌ BUT no explicit trigger display (40% threshold)
- ❌ No visual when kill-switch activated
- ❌ No blacklist/recovery countdown
- ❌ No rebalance action history

**Risk Scenario:**
```
Rocket A drawdown: 35% → OK
  ↓ [Manual re-entry decision, no UI guidance]
  ↓
Rocket A drawdown: 42% → KILL-SWITCH TRIGGERED
  ↓
User doesn't see kill-switch status in UI
  ↓
User manually re-enables → violates risk policy
```

**Implementation (Phase 1.0 or 1.1):**
1. Add "Risk Trigger Card" (6-8 hours)
2. Display current individual/portfolio MaxDD vs 40%/50% thresholds
3. Red warning when threshold breached
4. Show blacklist countdown (days remaining)
5. Recovery conditions & revalidation requirements

#### Gap 3: Timeframe Cache Selector (P1 - 4-6 hours)

**North Star Requirement:**
- 6 independent timeframes: 1m, 5m, 15m, 1h, 4h, 1d
- Each has own Optuna study, own HNSW index, own best_params
- Parallel execution on all TF simultaneously

**Current UX:**
- ⚠️ "Multi-timeframe trading" mentioned in Executive Summary
- ❌ NO UI to select/filter by timeframe
- ❌ NO visualization of per-TF optimization progress
- ❌ NO TF-specific metrics (Sharpe by timeframe, etc.)

**Risk Scenario:**
```
User runs optimization (all 6 TF in parallel)
  ↓
1m results: Sharpe 1.2
5m results: Sharpe 0.8
  ↓
NO UI to view timeframe-specific results
  ↓
Cannot make informed decision on which TF to trade
```

**Implementation (Phase 1.1):**
1. Add "Timeframe Selector" tabs/dropdown (4-6 hours)
2. Filter results by TF: 1m | 5m | 15m | 1h | 4h | 1d
3. Show per-TF metrics: Sharpe, Win Rate, MaxDD, MTRL
4. Display HNSW index health per TF (entries, last rebuild, staleness)

#### Gap 4: H4 Reference Toggle (P1 - 2-3 hours)

**North Star Requirement:**
- H4 is independent timeframe cache (participates in optimization like others)
- OPTIONAL H4 can provide volatility reference (dff_h4_override_enabled=True)
- H4 does NOT block/authorize trades (no fallback signals, no validation base)

**Current UX:**
- ❌ H4 NOT mentioned
- ❌ No toggle to enable/disable H4 reference
- ❌ No visualization of H4 as volatility anchor

**Risk Scenario:**
```
User wants to use H4 volatility as reference for 1m/5m DFF
  ↓
NO UI to enable dff_h4_override_enabled
  ↓
Cannot access H4 reference feature
  ↓
Parameter space artificially constrained
```

**Implementation (Phase 1.1 or Phase 2):**
1. Add "H4 Reference Settings" section (2-3 hours)
2. Checkbox: "Use H4 volatility as reference"
3. Show H4 ATR(14) when enabled
4. Warning: "H4 reference is optional; only affects distance calculations"

#### Gap 5: Parameter Counter (P2 - 2-3 hours)

**North Star Requirement:**
- Active parameters per profile: ≤ 70
- Enforce: `active_param_count <= 70` (violated = trial rejected)
- Profile-specific activation gates

**Current UX:**
- ❌ NO parameter counter displayed
- ❌ NO indication of how many parameters are active
- ❌ NO warning when approaching 70-param limit

**Risk Scenario:**
```
User selects profile: "full_optimization"
  ↓
Optuna samples trial with 85 active parameters
  ↓
Trial rejected silently (no UI feedback)
  ↓
Optimization appears slow (constant rejection)
  ↓
User doesn't know why
```

**Implementation (Phase 1.1 or Phase 2):**
1. Add "Parameter Counter" widget (2-3 hours)
2. Display: "Active Parameters: 45/70 (64%)"
3. Show per-category breakdown
4. Warning: "Approaching parameter limit; consider reducing profile scope"

---

## Section 3: User Journey Baseline Coverage

### 3.1 North Star User Journeys (From Brief)

**Core Spine:** Monitor → Review → Diagnose

**5 Major Journeys:**

1. **Monitor Journey** ("Быстро увидеть Net P&L и статус валидации")
   - Purpose: Quick status check <3 seconds
   - Entry: Open dashboard
   - Key steps: View P&L, check validation status
   - Exit: Decide drill-down vs archive

2. **Deep-Dive Journey** ("Погрузиться в детализацию запуска")
   - Purpose: Understand P&L composition
   - Entry: Click run from list
   - Key steps: View equity curve, drawdown, trades, costs
   - Exit: Find root cause

3. **Comparison Journey** ("Сравнить 2-3 запуска")
   - Purpose: Identify best parameters
   - Entry: Multi-select runs
   - Key steps: Side-by-side metrics, sensitivity analysis
   - Exit: Select champion

4. **Diagnostics Journey** ("Понять за <60 секунд, почему нет сделок")
   - Purpose: RCA for zero-trade runs
   - Entry: Open run with trades=0
   - Key steps: Check data, signals, gates
   - Exit: Understand blocker

5. **Export Journey** ("Экспортировать артефакты прогона")
   - Purpose: Archive for reproducibility
   - Entry: Select run to archive
   - Key steps: Choose format, validate completeness
   - Exit: Download package

### 3.2 UX Coverage vs North Star Journeys

| Journey | UX Status | Coverage % | Gap |
|---|---|---|---|
| **Monitor** | Run Summary + P&L Card | 100% | ✓ None |
| **Deep-Dive** | Equity Curve + Trades List + Breakdown | 95% | ⚠️ Missing trade legend (low priority) |
| **Comparison** | Comparison Modal (partial logic) | 70% | ❌ Missing sensitivity analysis, correlation heatmap |
| **Diagnostics** | Signal Diagnostics + RCA Card | 90% | ⚠️ Missing explicit "Data Version" verification |
| **Export** | Export Button (basic) | 60% | ❌ Missing preview, batch export, versioning |

**Overall Journey Coverage:** 83% (not 85%)

### 3.3 Comparison Journey Gap (P1 - 8-10 hours)

**North Star Requirement:**
- Compare 2-3 runs side-by-side
- Identify parameter sensitivity
- Drive champion selection

**Current UX:**
- ⚠️ Comparison Modal exists
- ❌ No parameter sensitivity visualization
- ❌ No correlation heatmap
- ❌ No "best value per metric" highlighting

**Missing UI Components:**
1. Metrics correlation heatmap (4-5 hours)
2. Parameter sensitivity tornado chart (3-4 hours)
3. "Best run per metric" highlighting (1-2 hours)

### 3.4 Export Journey Gap (P2 - 6-8 hours)

**North Star Requirement:**
- Archive artifacts with reproducibility metadata
- Support multiple formats (HTML, JSON, YAML)
- Batch export capability

**Current UX:**
- ⚠️ Export button exists
- ❌ No preview before download
- ❌ No batch export UI
- ❌ No versioning/history

**Missing UI Components:**
1. Export preview modal (3-4 hours)
2. Batch select & export (2-3 hours)
3. Export history & versioning (2-3 hours)

---

## Section 4: Reconciliation: 85% PRD vs 100% North Star

### 4.1 Why 85% PRD ≠ 100% North Star Baseline

**85% Coverage = PRD Requirements:**
- 21 major PRD sections
- ~85% of PRD flows explicitly wireframed
- Acceptable for typical product development

**100% North Star Baseline = Critical Blocking Features:**
- Mandatory Baseline enforcement (KatanaTransformer validation)
- Canonical Values visibility (DFF types, timeframes, kill-switch)
- Core safety mechanisms (Calendar Safety already covered)
- User journeys (Monitor/Diagnose strong; Comparison/Export weak)

**The Gap:**
PRD coverage doesn't guarantee north star baseline coverage because:
1. PRD is implementation-focused (architecture, APIs, databases)
2. North Star is user-focused (what must work on Day 1)
3. UX 85% PRD coverage misses critical user-facing features from north star

**Example:**
- PRD § Architecture: "DFF types: 6 implementations" ✓ Described
- North Star Baseline: User must SELECT DFF type in UI ❌ Missing from UX

---

## Section 5: Critical Path to 100% North Star Baseline

### 5.1 Phase 1.0 (BLOCKING - Must complete before go-live)

| Item | Effort | Hours | Blocker |
|---|---|---|---|
| **Mandatory Baseline Badge** (KatanaTransformer validation) | High | 6-8 | P0 |
| **Kill-Switch Visualization** (40%/50% trigger display) | High | 6-8 | P0 |
| Total Phase 1.0 | | **12-16 hours** | **BLOCKING** |

**Rationale:** Cannot go live without enforcing mandatory baseline and displaying risk kill-switches. These are non-negotiable safety features.

### 5.2 Phase 1.1 (Nice-to-Have but Recommended)

| Item | Effort | Hours | Priority |
|---|---|---|---|
| **DFF Type Selector** | Medium | 4-6 | P1 |
| **Timeframe Cache Selector** | Medium | 4-6 | P1 |
| **Parameter Counter** | Low | 2-3 | P2 |
| **H4 Reference Toggle** | Low | 2-3 | P2 |
| **Comparison Sensitivity Analysis** | High | 8-10 | P1 |
| **Export Preview & Batch** | Medium | 6-8 | P2 |
| Total Phase 1.1 | | **26-36 hours** | **RECOMMENDED** |

**Rationale:** Phase 1.1 items unlock full potential of north star features without blocking go-live. Recommend completing in 1-2 weeks post-launch.

### 5.3 Phase 2 (Deferred)

- Parameter Space UI (115 params, profile-specific)
- Mass Parameter Optimization dashboard
- Advanced export formats
- API documentation UI

---

## Section 6: Impact Assessment

### 6.1 Go-Live Risk (Phase 1.0 Only)

**If Phase 1.0 is INCOMPLETE:**

| Risk | Severity | Impact |
|---|---|---|
| Non-Katana strategies deployed | **CRITICAL** | Validation gates unreliable; archive contaminated |
| Kill-switch not visible | **HIGH** | Users may override safety mechanisms manually |
| Baseline enforcement missing | **HIGH** | Product doesn't enforce north star constraints |

**Go-Live Readiness:** ⚠️ **NOT READY** unless Phase 1.0 items completed

### 6.2 Post-Launch Experience (Phase 1.1 Completed)

**If Phase 1.1 is COMPLETE:**
- ✓ Mandatory baseline enforced
- ✓ Risk kill-switches visible
- ✓ DFF feature accessible
- ✓ Comparison workflow functional
- ✓ Export reproducibility guaranteed

**User Experience:** ✓ **EXCELLENT** — Full north star baseline + extended capabilities

---

## Section 7: Revised Coverage Scorecard

### 7.1 North Star Baseline Coverage (Current)

| Category | Target | Current | Status | Gap |
|---|---|---|---|---|
| **Mandatory Baseline** (KatanaTransformer) | 100% | 0% | ❌ CRITICAL | Badge needed |
| **Kill-Switch Triggers** | 100% | 30% | ❌ CRITICAL | Visualization needed |
| **Calendar Safety & News** | 100% | 100% | ✓ COMPLETE | None |
| **User Journeys** | 100% | 83% | ⚠️ GOOD | Comparison & Export weak |
| **Canonical Values Visibility** | 100% | 40% | ⚠️ PARTIAL | DFF, timeframes, leverage |
| **Overall North Star Coverage** | **100%** | **~70-75%** | **⚠️ NEEDS WORK** | **25-30% gap** |

### 7.2 Current vs Target by Phase

```
Phase 1.0 (Go-Live):
  Current:  65% (missing mandatory baseline + kill-switch)
  Target:   85% (Phase 1.0 items + existing good coverage)
  Effort:   12-16 hours
  Status:   ⚠️ ACHIEVABLE if prioritized NOW

Phase 1.1 (Post-Launch Quick Wins):
  Current:  65%
  Target:   95% (add DFF, timeframes, comparison, export)
  Effort:   26-36 hours (1-2 weeks post-launch)
  Status:   ✓ RECOMMENDED for full experience

Phase 2 (Extended):
  Target:   100% (add parameter space UI, advanced optimization)
  Effort:   Scope TBD
  Status:   ✓ ACCEPTABLE to defer
```

---

## Section 8: Recommendations

### 8.1 Critical Actions (Immediate - This Week)

1. **ADD to Phase 1.0 (BLOCKING):**
   - Mandatory Baseline Badge (6-8 hours)
   - Kill-Switch Visualization (6-8 hours)
   - Total: 12-16 hours

2. **UPDATE Go-Live Gate:**
   - Don't just check "UX 85% PRD coverage"
   - Check "UX covers 100% north star baseline"
   - Baseline = Mandatory validation + Safety mechanisms + Core user journeys

### 8.2 Recommended Actions (Next Week - Phase 1.1)

1. **Prioritize Phase 1.1 items:**
   - DFF Type Selector (4-6h)
   - Timeframe Cache Selector (4-6h)
   - Comparison Sensitivity Analysis (8-10h)

2. **Timeline:** Complete Phase 1.1 within 1-2 weeks of go-live

### 8.3 Planning Actions (Phase 2)

- Plan parameter space UI (115 params)
- Plan mass optimization dashboard
- Plan advanced export/archival system

---

## Section 9: Conclusion

**User's Concern Validated:** ✓

The user was **CORRECT** to flag that 85% PRD coverage may not include north star baseline functionality.

**Finding:** 85% PRD coverage translates to ~70-75% north star baseline coverage because:
- ❌ Mandatory Baseline enforcement missing (KatanaTransformer validation)
- ❌ Kill-Switch risk controls missing from UX
- ❌ DFF feature hidden from users
- ❌ Comparison & Export journeys incomplete
- ✓ Calendar Safety & core workflows good

**Path to 100% North Star Coverage:**
1. **Phase 1.0 (BLOCKING):** Add Mandatory Baseline Badge + Kill-Switch Viz (12-16h)
2. **Phase 1.1 (RECOMMENDED):** Add DFF, Timeframes, Comparison, Export (26-36h)
3. **Phase 2:** Parameter space UI + advanced features

**Bottom Line:**
- ✅ **Phase 1.0 Gap:** Achievable in 12-16 hours (1-2 days)
- ✅ **Phase 1.1 Gap:** 26-36 hours (1-2 weeks post-launch)
- ⚠️ **Do NOT go live without Phase 1.0 items** (safety/baseline risk)

---

**Report Generated:** 2026-02-27 01:30:00Z
**Validation Status:** COMPLETE
**Next Step:** Prioritize Phase 1.0 items and update go-live gate criteria

