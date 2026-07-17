# PRD Flows NOT Covered in UX Design
## katana-vectorbt Project | Phase 1 Validation

**Generated:** 2026-02-27
**Purpose:** Identify all PRD functional flows and user flows that lack explicit wireframe/screen definitions in UX Design document

---

## Summary

| Category | Count | Status | Phase |
|----------|-------|--------|-------|
| **Critical Missing Flows** | 6 | ❌ Blockers / Deferrals | 1.1-2 |
| **Partial Coverage Flows** | 4 | ⚠️ Needs enhancement | 1.5-2 |
| **Deferred by Design** | 2 | ✓ Intentional P2 deferral | 2+ |
| **Total Gaps Identified** | 12 | | |

---

## Critical Missing Flows (BLOCKER - Must Address in Phase 1.1)

### 1. USER JOURNEYS: Explicit Wireframed Journeys

**PRD Reference:** § User Journeys (mentioned but not detailed in visible excerpt)

**What PRD Says:**
- User journey definitions for owner-operator persona
- Top tasks and pain points
- End-to-end flow from "problem identification" to "resolution"

**What PRD Implies:**
From Executive Summary section:
```
Основные пользовательские задачи (Top tasks):
- Быстро увидеть Net P&L и статус валидации
- Погрузиться в детализацию запуска: equity curve, drawdown, cost impact, trade-by-trade
- Сравнить 2-3 запуска по параметрам и метрикам
- Экспортировать артефакты прогона
- Понять за <60 секунд, почему нет сделок
```

**UX Coverage:** ⚠️ Scattered
- UX defines individual screens (P&L Overview, Drawdown, etc.)
- **Missing:** Explicit end-to-end journey WIREFRAMES showing:
  - Entry point → Key steps → Decision point → Exit
  - Transition paths between screens
  - User mental model visualization

**What's Needed:**
1. **Journey 1: Monitor & Quick Assessment** (5-7 steps)
   ```
   Open Dashboard
   ↓ (< 3s)
   Scan Net P&L + Status
   ↓ (Decision: profitable?)
   IF YES: Approve deployment
   IF NO: Drill into root cause
   ↓
   Exit: Archive run
   ```

2. **Journey 2: Diagnostics - Why Zero Trades** (4-6 steps)
   ```
   Open run with entries=0
   ↓
   View Signal Diagnostics Panel
   ↓ (Decision: root cause?)
   IF signal coverage < 5%: Fix entry condition
   IF data_bars < minimum: Extend lookback
   IF gates blocked: Review gate rules
   ↓
   Exit: Adjust and re-run
   ```

3. **Journey 3: Parameter Sensitivity Comparison** (6-8 steps)
   ```
   Select 2-3 candidate runs
   ↓
   Open Comparison Modal
   ↓
   Choose comparison criteria (Sharpe? MaxDD? Trades?)
   ↓
   Review side-by-side metrics
   ↓
   Identify best configuration
   ↓
   Exit: Deploy or tweak parameters
   ```

**Priority:** ❌ **P0 BLOCKER** - Phase 1.1
**Effort:** 6-8 hours (design + validation)

---

### 2. MASS PARAMETER OPTIMIZATION SYSTEM UI (PRD § Epic J)

**PRD Reference:** § Mass Parameter Optimization System (Epic J)

**PRD Detailed Requirements:**
- Industrial-scale search across 115+ parameters
- 8,000 trials total budget
- Parallel execution (8-10 workers)
- Risk mode presets (Conservative, Moderate, Aggressive, Rocket-Catching)
- Structural search (grammar-based strategy composition)
- QMC → TPE optimization sequence
- 7 quality gates (Walk-Forward, PBO, DSR, PSR, FDR, Stress, Monte Carlo)

**UX Coverage:** ❌ **NONE**
- No control panel for launching optimizations
- No progress visualization for 8,000 trial budget
- No risk mode selector
- No parameter space visualization
- No trial results display

**What's Needed:**
1. **Optimization Launcher Modal**
   - Profile selection (stable/return/rocket)
   - Risk mode preset selector
   - Budget allocation (8,000 trials)
   - Estimated duration (≤1 day on 8-10 workers)
   - "Launch Optimization" CTA

2. **Optimization Progress Dashboard**
   - Trial counter: "1,234 / 8,000 trials"
   - Time tracking: "Elapsed: 4h 23m | Remaining: ~18h"
   - Worker status (8 workers, N running)
   - Checkpoint indicator (auto-save)
   - Pause/Resume/Cancel CTAs

3. **Trial Results View**
   - Top-10 candidates by profile
   - Metrics table (Sharpe, Calmar, DSR, PBO, WF_degrad)
   - Gate status (which gates passed/failed)
   - Promotion readiness indicator
   - Parameter heatmap (sensitivity analysis)

4. **Risk Mode Comparison Panel**
   - Conservative vs Moderate vs Aggressive vs Rocket side-by-side
   - Metrics diff (Sharpe Δ, DD Δ, Calmar Δ)
   - Recommendation engine ("Best for stability: Conservative")

5. **Structural Search Visualization**
   - Module selection (which indicators, PA patterns, filters active)
   - Search space size (N configurations)
   - Coverage heatmap (which structures explored)
   - Best structure by metric

**Priority:** ❌ **Intentional Phase 2 Deferral** ✓
**Scope:** Phase 2 Epic J (not Phase 1)
**Effort:** 20-30 hours (design + prototyping)

---

### 3. PROFILE SWEEP ORCHESTRATION UI

**PRD Reference:** § Profile Sweep Orchestration

**PRD Requirements:**
- Automatic enumeration across 3 strategy profiles (stable/return/rocket)
- Per-profile results aggregation
- Promotion rules (which profiles advance to live trading)
- Champion portfolio selection from all 3 profiles
- Profile comparison (metrics, risk profiles, capital allocation)

**UX Coverage:** ⚠️ **Partial (Rocket only)**
- UX defines "ROCKET PORTFOLIO DASHBOARD" (only rocket profile UI)
- **Missing:**
  - Profile selector/toggle (stable, return, rocket tabs)
  - Stable profile dashboard
  - Return profile dashboard
  - Cross-profile comparison view
  - Champion portfolio selection panel

**What's Needed:**
1. **Profile Selector Tabs** (top of dashboard)
   ```
   [Stable] [Return] [Rocket] [Compare All]
   ```

2. **Per-Profile Dashboard** (for Stable/Return)
   - Strategies in this profile (list)
   - Aggregate metrics (portfolio Sharpe, MaxDD, Calmar)
   - Promotion status (how many ready for micro-live?)
   - Capital allocation (% of total)

3. **Cross-Profile Comparison Panel**
   ```
   Metric          | Stable  | Return  | Rocket  | Winner
   ────────────────┼─────────┼─────────┼─────────┼────────
   Portfolio Sharpe| 1.2     | 1.8     | 2.5*    | Rocket
   Max Drawdown    | 8%*     | 15%     | 22%     | Stable
   Calmar Ratio    | 0.95*   | 0.82    | 0.75    | Stable
   Trades/month    | 12      | 24*     | 48      | Return
   Capital req'd   | $5k*    | $10k    | $50k    | Stable
   ```

4. **Champion Portfolio Builder**
   - Add Stable strategy #1
   - Add Return strategy #3
   - Add Rocket strategy #5
   - Total portfolio allocation: 60% Stable + 30% Return + 10% Rocket
   - Estimated combined Sharpe: 1.45
   - [Deploy as Champion]

**Priority:** ⚠️ **Medium** - Phase 1.5 or Phase 2
**Effort:** 12-16 hours

---

### 4. PRODUCTION PIPELINE DIAGNOSTICS UI (PRD § Production Pipeline Diagnostics)

**PRD Reference:** § Production Pipeline Diagnostics (New Requirements)

**PRD Gate System (7 Offline + 2 Live):**
```
Offline Gates:
  1. Walk-Forward Validation (degrad ≤ 15%, purging + embargo)
  2. PBO (< 50% pass, 50-75% fail, > 75% critical)
  3. IS/OOS Correlation (≥ 0.50, p < 0.05)
  4. Statistical Power (PSR ≥ 0.95, N ≥ MTRL)
  5. FDR/Deflation (DSR/PSR thresholds per profile)
  6. Execution Realism (Effective Sharpe ≥ 70% backtested)
  7. Monte Carlo Stress (worst-case DD < 40%)

Live Gates:
  A. Micro-Live Eligibility (trade freq, position size, leverage)
  B. Calendar/News Impact Calibration (day 7 live check)
```

**UX Coverage:** ⚠️ **Minimal/None for gates**
- Signal Diagnostics Panel covers "why zero trades" (RCA)
- **Missing:**
  - Gate-by-gate status display
  - Gate pass/fail indicators
  - Gate failure details (what failed, why, remediation)
  - Promotion workflow (offline → micro-live → scaled-live)

**What's Needed:**
1. **Gate Status Card** (per run)
   ```
   ┌─ OFFLINE GATES ─────────────────┐
   │ 1. Walk-Forward Validation      │ ✓ 12% degrad (target ≤15%)
   │ 2. PBO Analysis                 │ ⚠️ 68% fail rate (target <50%)
   │ 3. IS/OOS Correlation           │ ✓ 0.58 p<0.001
   │ 4. Statistical Power (PSR)      │ ✓ 0.97 (target ≥0.95)
   │ 5. FDR/Deflation (DSR)          │ ✓ 0.96 (target ≥0.95)
   │ 6. Execution Realism            │ ✓ 78% Effective Sharpe
   │ 7. Monte Carlo Stress           │ ✗ 42% worst-case DD (target <40%)
   │                                 │
   │ OFFLINE STATUS: ⚠️ FAIL (gate 7 │
   │                                 │
   ├─ LIVE GATES ────────────────────┤
   │ A. Micro-Live Eligibility       │ ⏱️ Pending offline gates
   │ B. Calendar/News Calibration    │ ⏱️ Pending micro-live placement
   │
   │ LIVE STATUS: ⏳ NOT YET ELIGIBLE
   └─────────────────────────────────┘
   ```

2. **Gate Failure Details Modal**
   - What failed: "Monte Carlo stress test: 42% worst-case DD > 40% limit"
   - Why: "Tail risk during high-volatility regimes (2022-03 stress period)"
   - Remediation options:
     * Reduce leverage (currently 2x → try 1.5x)
     * Tighten stop-loss (currently 3% → try 2%)
     * Add volatility filter (skip trades when VIX > 30)
   - [Adjust parameters & re-run] or [Accept risk & proceed]

3. **Promotion Workflow**
   ```
   Offline gates: ✓ 6/7 pass
   ↓ [Escalate despite gate 7 failure] or [Fix parameters]
   ↓
   Micro-Live: Place in demo account
   ↓ (Day 1-7 monitoring)
   ↓
   Live Gate B: Calendar/News impact calibration
   ↓ (Decision: micro-live → scaled-live)
   ↓
   Scaled-Live: Deploy 25% of capital
   ↓ (Ongoing monitoring, kill-switch armed)
   ```

**Priority:** ⚠️ **Medium** - Phase 2
**Effort:** 10-14 hours

---

## Partial Coverage Flows (MEDIUM - Enhance in Phase 1.5)

### 5. RUN COMPARISON FLOW

**PRD Requirement:**
> "Сравнить 2-3 запуска по параметрам и метрикам" (Compare 2-3 runs by parameters and metrics)

**UX Coverage:** ⚠️ **Basic (exists but thin)**
- UX defines "Comparison Modal (2-3 runs)"
- **Missing:**
  - Comparison criteria selector (which metrics?)
  - Parameter-by-parameter diff
  - Correlation analysis (are differences meaningful?)
  - Statistical significance tests (t-test for Sharpe difference)

**What's Needed:**
1. **Comparison Criteria Selector**
   ```
   Metrics to compare:
   ☑ Sharpe Ratio        ☑ Max Drawdown     ☑ Calmar Ratio
   ☑ Win Rate            ☑ Profit Factor    ☑ Trades/month
   ☑ Avg Trade Return    ☑ Std Dev Returns  ☐ DSR
   ☐ PBO                 ☐ PSR              ☐ Other...

   Parameters to compare:
   ☑ Entry signal        ☑ Risk mode        ☑ MTF settings
   ☑ Stop-loss %         ☑ Take-profit %    ☑ Position size
   ☐ All (115+)
   ```

2. **Comparison Table** (enhanced)
   ```
   Metric              | Run A      | Run B      | Run C      | Δ A-B | Sig?
   ─────────────────────────────────────────────────────────────────────
   Sharpe Ratio        | 1.23       | 1.18       | 1.45       | 0.05  | NS
   Max Drawdown        | 12.5%      | 14.2%      | 11.8%      | -1.7% | **
   Calmar Ratio        | 0.98       | 0.83       | 1.23       | 0.15  | *
   Trades/month        | 24         | 22         | 36         | 2     | -
   Avg Trade Return    | 0.58%      | 0.52%      | 0.71%      | 0.06% | NS

   Entry Signal        | MA(50)     | MA(50)     | MACD       | -     | -
   Risk Mode           | Moderate   | Moderate   | Aggressive | -     | -
   SL %                | 2.0%       | 2.0%       | 3.0%       | -     | -
   TP %                | 4.5%       | 4.5%       | 10.0%      | -     | -
   ```
   Legend: `*` p<0.05, `**` p<0.01, `NS` not significant

3. **Parameter Sensitivity Heatmap**
   ```
   Which parameters drove the biggest difference between Run A & B?

   Parameter              | Run A | Run B | Δ | Impact
   ─────────────────────────────────────────────────────
   MA fast period         | 12    | 14    | +2 | High
   MA slow period         | 50    | 50    | 0  | None
   RSI overbought         | 70    | 75    | +5 | Low
   ```

**Priority:** ⚠️ **Medium** - Phase 1.5
**Effort:** 6-8 hours

---

### 6. RUN JOURNAL: EVENT STREAM VISUALIZATION

**PRD Reference:** § Executive Summary
> "Run Journal is the source of truth for runtime history and ops"

**PRD Requirement:**
- Timeline of run events (start, checkpoint, gate pass/fail, completion)
- Event filtering (by type, severity, time range)
- Event detail drilldown

**UX Coverage:** ✓ **Partial (exists implicitly)**
- UX mentions "Run Status Card" reading from `events.ndjson`
- UX mentions "last update timestamp"
- **Missing:** Visual timeline/event stream

**What's Needed:**
1. **Run Journal Timeline**
   ```
   2026-02-27 10:00:00 | ▶ Optimization started
                        | Trials: 0 / 8000
                        | Workers: 8 active

   2026-02-27 10:15:00 | ✓ Checkpoint #1 saved
                        | Trials: 245 / 8000 (3%)
                        | Best Sharpe: 1.23

   2026-02-27 11:30:00 | ⚠️ Worker #3 stalled
                        | Restarted successfully
                        | No trials lost

   2026-02-27 18:45:00 | ✓ Optimization complete
                        | Trials: 8000 / 8000
                        | Duration: 8h 45m
                        | Best Sharpe: 2.14 (profile: rocket)

   2026-02-27 18:46:00 | ⚠️ Gate 2 (PBO) FAILED
                        | Result: 68% fail rate (target <50%)
                        | Action: Review or escalate

   2026-02-27 18:47:00 | ✓ Run promotion: MICRO_LIVE
                        | Status: Ready for paper trading
                        | Next: Deploy to paper account
   ```

2. **Event Filter**
   ```
   Filter by:
   ☑ Checkpoint saved    ☑ Gate pass    ☑ Gate fail
   ☑ Error/warning       ☑ Promotion    ☑ Worker events

   Time range: [2026-02-27 10:00] to [2026-02-27 20:00]

   [Clear filters]
   ```

3. **Event Detail Modal**
   - Event timestamp
   - Event type (checkpoint, gate, promotion, error)
   - Full message
   - Associated metrics (if gate: which gates passed/failed)
   - Remediation CTA (if error)

**Priority:** ⚠️ **Low-Medium** - Phase 2
**Effort:** 8-10 hours

---

### 7. EXPORT WORKFLOW: Preview & Batch

**PRD Requirement:**
> "Экспортировать артефакты прогона: HTML + machine-readable (JSON/YAML) для архива и воспроизводимости"

**UX Coverage:** ⚠️ **Minimal**
- UX mentions CTAs ("Generate CLI / YAML", "Open run folder", "Refresh report")
- **Missing:**
  - Export preview before download
  - Batch export (multiple runs)
  - Export history/versioning
  - Format customization (JSON vs YAML fields)

**What's Needed:**
1. **Export Dialog** (enhanced)
   ```
   ┌─ EXPORT RUN ─────────────────────┐
   │ Run ID: 20260227-optimization-1  │
   │                                  │
   │ Format:                          │
   │ [○] HTML Report                  │
   │ [×] JSON Artifacts               │
   │ [ ] YAML Format                  │
   │ [ ] CSV Trades                   │
   │ [×] Summary only (not full logs) │
   │                                  │
   │ Filename: run-20260227-opt1.zip  │
   │                                  │
   │ Size estimate: ~15 MB            │
   │                                  │
   │ [Preview] [Export] [Cancel]      │
   └──────────────────────────────────┘
   ```

2. **Export Preview**
   ```
   ┌─ PREVIEW ─────────────────────┐
   │ Your export will include:      │
   │                               │
   │ ✓ run_summary.json (12 KB)    │
   │ ✓ runs/trades.csv (8.4 MB)    │
   │ ✓ runs/events.ndjson (2.3 MB) │
   │ ✓ report.html (120 KB)        │
   │ ✓ risk_flags.json (5 KB)      │
   │                               │
   │ Total: 10.8 MB                │
   │                               │
   │ This run is reproducible:      │
   │ ✓ Data hash: a1b2c3d4... ✓    │
   │ ✓ Code version: v1.2.3 ✓      │
   │ ✓ Dataset frozen: Yes ✓       │
   │                               │
   └───────────────────────────────┘
   ```

3. **Batch Export**
   ```
   Select runs to export:
   ☑ Run A (20260227-opt1)
   ☑ Run B (20260227-opt2)
   ☑ Run C (20260227-paper-1)

   Export as single ZIP or separate files?
   [○] Single ZIP (combined archive)
   [×] Separate files (import-friendly)

   [Batch export 3 runs]
   ```

**Priority:** ⚠️ **Low** - Phase 2
**Effort:** 6-8 hours

---

## Deferred by Design (Intentional Phase 2)

### 8. JUPYTER NOTEBOOK UI (PRD → Phase 2+)

**PRD Reference:** § Executive Summary
> "futurePhases: 'jupyter_then_streamlit_evaluation'"

**Status:** ✓ **Intentional deferral to Phase 2** (noted in UX DEFERRED UX SPECIFICATIONS)

**Phase 1:** Static HTML dashboard (current scope)
**Phase 2:** Interactive Jupyter notebook environment (future evaluation)

---

### 9. MULTI-USER/ENTERPRISE FEATURES

**PRD Reference:** § Scope note (Brief‑First)
> "Any content about multi-user SaaS, revenue targets, support ops, SOC2/PCI/GDPR, or 99.9% uptime is **deferred** and **not required** for the 90-day single-user passive-income goal."

**Status:** ✓ **Intentional deferral** (out of Phase 1 scope)

---

## Summary Table: All Missing Flows

| # | Flow Name | PRD Section | UX Status | Priority | Phase | Effort |
|---|---|---|---|---|---|---|
| 1 | User Journeys Wireframes | User Journeys | ❌ Missing | ❌ P0 | 1.1 | 6-8h |
| 2 | Mass Optimization UI | Epic J | ❌ None | ✓ Deferred | 2 | 20-30h |
| 3 | Profile Sweep UI | Profile Sweep Orch. | ⚠️ Partial | ⚠️ P2 | 1.5-2 | 12-16h |
| 4 | Gate Status Display | Prod Pipeline Diag. | ❌ None | ⚠️ P3 | 2 | 10-14h |
| 5 | Run Comparison Enhanced | User Journey | ⚠️ Partial | ⚠️ P2 | 1.5 | 6-8h |
| 6 | Event Stream Timeline | Run Journal | ⚠️ Implicit | ⚠️ P3 | 2 | 8-10h |
| 7 | Export Preview/Batch | Artifact Mgmt | ⚠️ Minimal | ⚠️ P3 | 2 | 6-8h |
| 8 | Jupyter Notebook UI | Phase 2+ | ✓ Deferred | ✓ Deferred | 2+ | 30-40h |
| 9 | Multi-user Features | Out of scope | ✓ Deferred | ✓ Deferred | 3+ | TBD |

---

## Recommendations

### Phase 1.1 Action Items (MUST DO)
1. ✓ Create 3 user journey wireframes (Monitor, Diagnostics, Comparison)
2. ✓ Add strategy validation badge to Run Summary
3. ✓ Enhance comparison modal with criteria selector

**Effort:** 8-10 hours total
**Impact:** Closes 3/7 critical gaps, unlocks Phase 1 MVP

### Phase 1.5 Nice-to-Have
1. Full comparison table with statistical significance
2. Parameter sensitivity heatmap
3. Profile comparison tabs (stable/return/rocket)

**Effort:** 12-16 hours
**Impact:** Enhances user experience, de-risks Phase 2

### Phase 2 Planned Deferrals
1. Mass Parameter Optimization UI (Epic J)
2. Gate Status Card (Pipeline Diagnostics)
3. Event Stream Timeline (Run Journal)
4. Batch Export & Preview
5. Jupyter Notebook Integration

---

**Status: ✓ Ready for Phase 1 with identified enhancements**
**Next Review: After Phase 1.1 implementation**
