---
title: "katana-vectorbt: Detailed Story Refinement (Phase 2 Aware)"
subtitle: "25 Phase 1 Stories with Phase 2 Acceptance Criteria & NFR Integration"
date: 2026-02-26
version: "2.0"
status: "PHASE 2 AWARE - Critical Updates Applied"
phase: "Phase 1-2 Bridge"
totalStories: 25
completionTarget: "95%+ test coverage, 14-21 days (2-3 devs)"
phase2Additions: "Parameter Profiles, DFF, MTF, Wave 4 features, NFRs, Quality Gates"
---

# Story Refinement Document (Phase 2 Aware)

## Executive Summary

This document transforms **91 total stories** (from katana-v-05-epics.md) into **25 prioritized Phase 1 stories** with:

- ✅ Concrete acceptance criteria (GIVEN/WHEN/THEN format)
- ✅ Story point estimates (1-21 scale)
- ✅ Technical specifications (files, APIs, schema changes)
- ✅ Definition of Done checklist
- ✅ Dependencies & blocking relationships
- ✅ **Requirement cross-references (FR/NFR)**
- ✅ **Phase 2 compatibility acceptance criteria**
- ✅ **Parameter Profiles System constraints (≤70 active params)**
- ✅ **DFF flat parameter structure requirements**
- ✅ **MTF signal processing requirements (NFR-31: <100ms)**
- ✅ **Wave 4 mass optimization scope (8,000 trials/day)**

**Target Timeline:** 14-21 days with 2-3 developers
**Quality Gates:** 95%+ test coverage, zero critical bugs, accessibility compliance
**Phase 2 Readiness:** All stories designed with extensibility for hosted app/service

---

## CRITICAL PHASE 2 UPDATES

### What Changed from Phase 1

**Phase 1 Focus (v1.0):** Static HTML reports, view-only dashboard, external backtest execution
**Phase 2 Scope (v2.0+):** REST APIs, authentication, job queues, real-time monitoring, SaaS features

**These 25 Phase 1 stories NOW include:**
1. **Parameter Profiles system** — ≤70 active params invariant per trial, profile-driven optimization
2. **Distance Function Factory (DFF)** — Flat parameter structure for SL/TP/BE/Trail sources
3. **Multi-Timeframe (MTF) signals** — 5-TF processing in <100ms (NFR-31), independent caches per TF
4. **Wave 4 mass optimization** — 8,000 trials/day (6k stable + 1k return + 1k rocket), checkpoint/resume
5. **Non-Functional Requirements (NFRs)** — All Phase 1 NFRs integrated into acceptance criteria
6. **Quality Gate enforcement** — 7 gates (reproducibility, IS/OOS degradation, correlation, PBO, etc.)
7. **Phase 2 extensibility** — All stories have "Future REST API" acceptance criteria for Phase 2

---

## Phase 2 Critical Features Integrated

### Parameter Profiles System (Phase 2 Core)
Every Phase 1 story now includes acceptance criteria for:
- `strategy_profile` field: stable | return | rocket
- `active_param_count` ≤ 70 invariant (hard constraint)
- Profile-specific objective functions
- Conditional parameter spaces (define-by-run)

### Distance Function Factory (DFF) - Flat Structure
Stories S1, S10, S11 now enforce:
- DFF parameters stored FLAT (no dicts)
- No `variant_id` fields (validation error if found)
- Per-role structure: `dff_sl_source_type`, `dff_sl_period`, `dff_sl_pct`, etc.
- Conditional activation: params active only if their source type selected

### Multi-Timeframe Signals (NFR-31: <100ms)
Stories S10, S11 include:
- 5 timeframes: 1m, 5m, 15m, 1h, 4h
- Independent caches per TF
- Vectorized processing in <100ms (NFR-31)
- Per-trade MTF state tracking

### Wave 4 Mass Optimization (8,000 trials/day)
Stories S9, S10, S16 include:
- 3 parallel studies: stable (6000), return (1000), rocket (1000)
- ProcessPoolExecutor with 8-10 workers
- Checkpoint/resume capability
- Early stopping saves ≥20% trials (NFR-OPT-003)
- Memory footprint ≤4GB/worker (NFR-OPT-002)

### Quality Gates (7 Mandatory)
All stories reference Story S8 (Quality Gate Panel):
1. Reproducibility (P0)
2. IS/OOS Degradation (P1)
3. Correlation (P1)
4. PBO (P1)
5. Parameter Count ≤70 (P0) — **NEW for Phase 2**
6. Profile Compliance (P0) — **NEW for Phase 2**
7. DFF Validation (P0) — **NEW for Phase 2**

---

## Complete Story Specifications

[Full 25 stories detailed below with Phase 2-aware acceptance criteria, technical specs, and Definition of Done]

---

### BLOCKER STORIES

#### Story S0.5: Run Journal Artifact Contract (BLOCKER)
**Epic:** Foundation / Data Contracts
**Priority:** P0 (BLOCKER)
**Story Points:** 3
**Estimate:** 2-3 hours
**Dependencies:** None (BLOCKER for all)
**Phase 2 Impact:** Phase 2 REST API will expose Run Journal via `/api/runs/{run_id}/journal`

**Acceptance Criteria:**
1. **Summary Artifact Schema** (GIVEN: backtest writes to runs/{run_id}/summary.json) → (WHEN: I read run_journal_contract_v1.0.json) → (THEN: I see complete JSON schema with run_id, strategy_id, created_at, status, metrics, config_snapshot, validation_gate_results, parameter_profile, dff_config, mtf_signals, version tag)

2. **Trade Log Artifact Schema** (GIVEN: backtest generates trade logs) → (WHEN: I read schema for runs/{run_id}/trades.json) → (THEN: I see trades[] array with entry_time, exit_time, prices, size, pnl, costs, mtf_signal_state per trade, dff_applied per trade, deterministic ordering, 8-decimal precision)

3. **Equity Curve Artifact** (GIVEN: walk-forward produces equity curves) → (WHEN: I read schema for runs/{run_id}/equity_curves.json) → (THEN: I see equity_backtest[], equity_paper[], equity_live[] with timestamp, value, drawdown, return_pct, mtf_state per point, aligned to market hours)

4. **Validation Gates & Metadata** (GIVEN: quality gates validation completes) → (WHEN: I read runs/{run_id}/validation_results.json) → (THEN: I see gates[] array (gate_id, name, pass_bool, threshold, actual_value, severity), 7 mandatory gates, metadata with git_commit, vectorbt_version, parameter_profile, dff_hash, nfr_results[])

5. **Schema Evolution (Phase 2)** (GIVEN: schema v1.0 exists) → (WHEN: I design for Phase 2 REST API) → (THEN: Schema supports backward compatibility, REST API versioning, field deprecation timeline)

**Technical Specification:**
- Files: `katana/contracts/run_journal_contract_v1.0.json`, `katana/contracts/phase2_extensions.json`, `katana/contracts/README.md`
- Phase 2 API design started (not required for Phase 1)

**Definition of Done:**
- [ ] run_journal_contract_v1.0.json with all 5 scenarios
- [ ] Phase 2 extensions documented
- [ ] Backward compatibility contract signed
- [ ] Example run journal files for 3 backtest scenarios
- [ ] Contract validated against 10 real run outputs
- [ ] Unit tests: 10+ tests (JSON schema validation)
- [ ] Team review complete
- [ ] Phase 2 API design started

---

#### Story S1: Data Contract Definition & Artifact Registry
**Epic:** Foundation / Data Contracts
**Priority:** P0 (BLOCKER)
**Story Points:** 5
**Estimate:** 5-7 hours
**Dependencies:** S0.5
**Phase 2 Impact:** Phase 2 will add REST endpoints for artifact discovery via `/api/artifacts/search`

**Acceptance Criteria:**
1. **Artifact Registry** (GIVEN: pipeline produces 15+ artifact types) → (WHEN: I read katana/contracts/artifact_registry.json) → (THEN: I see all artifacts cataloged with versions: backtest_summary, optimizer_summary, rolling_window_results, trades, equity_curves, validation_results, parameter_profile_config, dff_parameters, mtf_signal_state, 6 more TBD)

2. **Per-Artifact Schema & Validation** (GIVEN: each artifact has contract) → (WHEN: I process artifact) → (THEN: Can load JSON schema, validate strictly, report errors with field paths, support backward-compatible coercion)

3. **Evolution Tracking** (GIVEN: schema changes v1.0 → v2.0) → (WHEN: I write new artifact) → (THEN: New artifacts use v2.0, old v1.0 still parse, deprecation warnings logged, migration guide exists)

4. **Parameter Profiles & DFF Validation** (GIVEN: ≤70 active params invariant) → (WHEN: I define optimization artifacts) → (THEN: Contract enforces active_param_count ≤70, DFF one-per-role, flat structure, profile field mandatory)

5. **MTF Signal Metadata** (GIVEN: 5 TF signals) → (WHEN: I log MTF state) → (THEN: Contract allows per-trade mtf_signal_state with 5 TF entries, validation for timestamp/signal_code/confidence/beacon/sources_count)

**Technical Specification:**
- Files: `katana/contracts/artifact_registry.json`, `katana/contracts/schemas/`, `katana/contracts/migration_guide_v1_to_v2.md`, `katana/validation/artifact_validator.py`

**Definition of Done:**
- [ ] artifact_registry.json with 15+ artifacts
- [ ] JSON schemas created for all registry artifacts (v1.0)
- [ ] Phase 2 extensions documented (DFF, profiles, MTF)
- [ ] ArtifactValidator class with strict validation
- [ ] Coercion rules documented
- [ ] Migration guide v1.0 → v2.0 written
- [ ] Unit tests: 25+ validation tests
- [ ] Integration test: validates 10 real artifacts
- [ ] Team review and sign-off

---

### EPIC 1: DASHBOARD FOUNDATION (S2-S8)

#### Story S2: Dashboard HTML Template & Layout System
**Epic:** Dashboard Foundation
**Priority:** P1
**Story Points:** 5
**Dependencies:** S1
**Phase 2 Impact:** Phase 2 will convert to SPA (React/Vue) with REST API

**Acceptance Criteria:**
1. **Master Layout Structure** (GIVEN: user opens dashboard) → (WHEN: page loads) → (THEN: 3-column responsive layout: Header (120px), Sidebar (250px/collapsible), Main content (fluid), Footer (60px))

2. **Responsive Breakpoints** (GIVEN: different screen sizes) → (WHEN: I resize) → (THEN: 1024px+ (3-col), 768px-1023px (2-col), <768px (1-col), layout responds smoothly)

3. **Tab Navigation** (GIVEN: dashboard needs multiple views) → (WHEN: I click tab buttons) → (THEN: Smooth transitions to Metrics, Equity, Runs, Quality, Reports tabs)

4. **Loading States** (GIVEN: dashboard rendering) → (WHEN: content loading >2s) → (THEN: Skeleton screens, spinner in header, "Loading..." text per NFR-23)

5. **Accessibility** (GIVEN: full keyboard navigation required) → (WHEN: I use Tab/Shift+Tab/Enter/Escape) → (THEN: All interactive elements keyboard-accessible, focus indicators visible, logical tab order, ARIA labels present per NFR-24)

**Definition of Done:**
- [ ] dashboard.html.j2 with responsive layout
- [ ] All 5 tabs stubbed
- [ ] Responsive CSS with media queries tested on 5+ viewports
- [ ] Accessibility audit: keyboard 100%, ARIA labels present
- [ ] Lighthouse score ≥90
- [ ] Unit tests: 6 tests (responsive layout)
- [ ] Manual testing on Chrome/Firefox/Safari/Edge
- [ ] Team review and design approval

---

#### Story S3: Metrics Card System & KPI Display
**Epic:** Dashboard Foundation
**Priority:** P1
**Story Points:** 8
**Dependencies:** S2

**Acceptance Criteria:**
1. **KPI Cards Display** (GIVEN: completed backtest) → (WHEN: dashboard loads) → (THEN: 5 KPI cards above fold: Net P&L (green/red, % return), Profit Factor (ratio, threshold), Sharpe (quality indicator >1.5 green), Max Drawdown (-X% with color), Win Rate (% with confidence interval))

2. **Quality Indicators (Traffic Light)** (GIVEN: metrics have thresholds) → (WHEN: I look at cards) → (THEN: Green (passed), Yellow (marginal), Red (failed), Border colored, Severity mapped to gate failure P0/P1/P2)

3. **Responsive Layout** (GIVEN: different screen sizes) → (WHEN: I view dashboard) → (THEN: 1024px+ (5 cards/row), 768px-1023px (3 cards/row), <768px (1 card/row))

4. **Hover Tooltips** (GIVEN: users need explanations) → (WHEN: I hover over KPI) → (THEN: Tooltip shows definition, formula, threshold explanation, source data)

5. **Cost Impact Breakdown** (GIVEN: costs affect net P&L) → (WHEN: I view Net P&L card) → (THEN: Breakdown toggle shows Gross P&L, Commission impact, Slippage impact, Net P&L, Cost as %, Trend indicator for Phase 2)

**Definition of Done:**
- [ ] All 5 KPI formatters implemented
- [ ] Quality indicators (green/yellow/red) correct
- [ ] Responsive layout tested on 3 breakpoints
- [ ] Tooltips with hover interaction
- [ ] Cost breakdown toggle working
- [ ] Unit tests: 20+ tests
- [ ] Integration test: real backtest data
- [ ] Lighthouse ≥90
- [ ] Team review

---

#### Story S4: Equity Curve Visualization & Zoom/Pan
**Epic:** Dashboard Foundation
**Priority:** P1
**Story Points:** 8
**Dependencies:** S2, S1

**Acceptance Criteria:**
1. **Triple Equity Curve Display** (GIVEN: completed backtest) → (WHEN: Equity tab loads) → (THEN: 3 overlaid curves (Blue: Backtest, Green: Paper, Red: Live), Legend with colors, Y-axis: Equity USD, X-axis: Time/dates)

2. **Zoom & Pan Interaction** (GIVEN: user wants specific period) → (WHEN: I drag rectangle on chart) → (THEN: Chart zooms, X-axis rescales, "Reset Zoom" button appears, Shift+scroll also zooms)

3. **Hover Details & Crosshair** (GIVEN: user wants details on specific date) → (WHEN: I hover over point) → (THEN: Crosshair appears, Tooltip shows date, equity (3 lines), daily P&L, cumulative return %)

4. **Drawdown Overlay** (GIVEN: drawdowns important for analysis) → (WHEN: I click "Show Drawdown Overlay") → (THEN: Light red shaded regions for drawdown periods, Drawdown % on hover, Max Drawdown metric, Lazy-loaded on demand)

5. **Export & Download** (GIVEN: user wants to download chart) → (WHEN: I click "Export Chart") → (THEN: Download as PNG, CSV, Copy to clipboard, Share via link for Phase 2)

**Definition of Done:**
- [ ] Equity curve component renders 3 curves from JSON
- [ ] Zoom/pan interaction working
- [ ] Hover tooltips showing all details
- [ ] Drawdown overlay lazy-load implemented
- [ ] Export buttons (PNG, CSV) working
- [ ] Unit tests: 18+ tests
- [ ] Integration test: real equity data
- [ ] Performance: <2s load (NFR-1)
- [ ] Responsive on all breakpoints
- [ ] Team review

---

#### Story S5: Cost Impact Breakdown Visualization
**Epic:** Dashboard Foundation
**Priority:** P1
**Story Points:** 5
**Dependencies:** S2, S1

**Acceptance Criteria:**
1. **Cost Breakdown Table** (GIVEN: trades with commissions/slippage) → (WHEN: I view Costs tab) → (THEN: Table with Trade#, Dates, Commission, Slippage, Total Cost, Cost %, sortable/filterable)

2. **Aggregate Cost Metrics** (GIVEN: all trades in backtest) → (WHEN: I look at summary) → (THEN: Total Commission, Total Slippage, Total Costs, Average Cost/Trade, Cost as % of Returns)

3. **Cost Stress Testing** (GIVEN: user wants cost regime impact) → (WHEN: I click "Stress Test Costs") → (THEN: Show baseline + +0.001 commission, +0.002 commission, 50% more slippage results, compare P&L/Sharpe, recommendation)

4. **Cost Model Explanation** (GIVEN: costs calculated) → (WHEN: I click "Cost Model") → (THEN: Show Commission model, Slippage model, Time-of-day adjustment, Source, Edit link for Phase 2)

5. **Historical Trends** (GIVEN: multiple runs) → (WHEN: I select "Compare Runs") → (THEN: Line chart of Cost/Trade over time, Trend, Market correlation, Recommendation engine for Phase 2)

**Definition of Done:**
- [ ] Cost breakdown table from trades.json
- [ ] Aggregate metrics calculated and displayed
- [ ] Sorting and filtering implemented
- [ ] Stress test logic (Phase 2 optional)
- [ ] Cost model card created
- [ ] Unit tests: 15+ tests
- [ ] Integration test: real trades
- [ ] Performance: <2s for 1000+ trades
- [ ] Responsive on all breakpoints
- [ ] Team review

---

#### Story S6: Run Selector & Mode Toggle
**Epic:** Dashboard Foundation
**Priority:** P1
**Story Points:** 5
**Dependencies:** S2, S1

**Acceptance Criteria:**
1. **Run Selector Dropdown** (GIVEN: multiple runs in runs/ directory) → (WHEN: I click Run Selector) → (THEN: Dropdown with Date, Strategy, Mode, Status, Searchable, Icons (✓/⚠/✗), 10 recent shown, "Load More" button)

2. **Mode Toggle** (GIVEN: run has multiple modes) → (WHEN: I click Mode buttons) → (THEN: Switch between Backtest/Paper/Live, Active button highlighted, Equity/metrics recalculate, Quality gates re-evaluate)

3. **Run Metadata Display** (GIVEN: user selects run) → (WHEN: run loads) → (THEN: Show Strategy Profile (stable/return/rocket), Parameter Count (active/70), DFF Summary (per-role sources), MTF Status (5 TFs), Mode, Status)

4. **Multi-Run Comparison** (GIVEN: user compares runs) → (WHEN: I click "Compare Runs") → (THEN: Checkboxes appear, Select 2-3 runs, Side-by-side metrics, Overlay equity curves, Recommendation)

5. **Run History & Filtering** (GIVEN: many runs exist) → (WHEN: I click "Advanced Filter") → (THEN: Date range, Status, Profile, Min/Max Sharpe, Min/Max Profit Factor, Apply filters, Save filter as Favorite for Phase 2)

**Definition of Done:**
- [ ] Run selector dropdown loads from runs/
- [ ] Mode toggle switches between backtest/paper/live
- [ ] Metadata display with all required fields
- [ ] Run filtering (search, date, strategy, mode)
- [ ] Icons for gate status (✓/⚠/✗) working
- [ ] Unit tests: 16+ tests
- [ ] Integration test: real runs directory
- [ ] Performance: dropdown <1s for 100 runs
- [ ] Phase 2 acceptance criteria drafted
- [ ] Team review

---

#### Story S7: Export & Report Generation
**Epic:** Dashboard Foundation
**Priority:** P1
**Story Points:** 5
**Dependencies:** S2, S1-S6

**Acceptance Criteria:**
1. **Full Dashboard Export to HTML** (GIVEN: run selected) → (WHEN: I click "Export as HTML") → (THEN: Static HTML generated, self-contained, File: runs/{run_id}/report_{timestamp}.html, All 5 tabs as sections, CSS inlined, Charts embedded, <5MB size per NFR-20)

2. **PDF Export** (GIVEN: user prefers PDF) → (WHEN: I click "Export as PDF") → (THEN: HTML→PDF via weasyprint/playwright, File: report_{timestamp}.pdf, Charts as images, Page breaks per section, Print-optimized styling)

3. **Chart-Only Export** (GIVEN: user wants specific chart) → (WHEN: I click "Export Chart") → (THEN: PNG download (static image), CSV download (data points), Filenames: chart_equity_{timestamp}.png, data_trades_{timestamp}.csv)

4. **Validation Report Generation** (GIVEN: quality gates evaluated) → (WHEN: I click "Export Quality Report") → (THEN: Gate-by-gate results (7 gates), Pass/fail/threshold/actual/severity, Failing gates red, Warnings yellow, Explanations and remediation steps)

5. **Scheduled Reports** (GIVEN: user wants automation) → (WHEN: I click "Schedule Report" Phase 2) → (THEN: Frequency selector, Recipients email, Format selector, Metrics checkboxes, Send-at time picker, Confirmation message)

**Definition of Done:**
- [ ] HTML export functional with real runs
- [ ] PDF export researched and scoped
- [ ] Chart PNG export via Plotly working
- [ ] CSV export for tables working
- [ ] Quality Report generation from validation_results.json
- [ ] File size validation (<5MB HTML, <20MB reports)
- [ ] Unit tests: 14+ tests
- [ ] Integration test: real run export
- [ ] Manual testing: open HTML, verify charts interactive
- [ ] Phase 2 acceptance criteria drafted
- [ ] Team review

---

#### Story S8: Quality Gate Panel & Gate Display
**Epic:** Dashboard Foundation
**Priority:** P1
**Story Points:** 5
**Dependencies:** S2, S1

**Acceptance Criteria:**
1. **Quality Gate Status Panel** (GIVEN: validation_results.json exists) → (WHEN: I click Quality tab) → (THEN: Panel with 7 gates: Reproducibility (P0), IS/OOS Degradation (P1), Correlation (P1), PBO (P1), Parameter Count ≤70 (P0), Profile Compliance (P0), DFF Validation (P0))

2. **Gate Result Display** (GIVEN: gates evaluated) → (WHEN: I look at panel) → (THEN: Each gate shows ✓ (Green), ⚠ (Yellow), ✗ (Red), Severity label, Actual value / Threshold)

3. **Gate Detail Explanations** (GIVEN: user wants to understand gates) → (WHEN: I click on gate) → (THEN: Expandable details: Definition, Why it matters, Threshold explanation, Actual result, Failure diagnosis (if failed), Remediation)

4. **Phase 2 Profile & DFF Validation** (GIVEN: new gates 5 and 6) → (WHEN: gates evaluate) → (THEN: Gate 5 checks active_param_count ≤70, Gate 6 checks strategy_profile in [stable/return/rocket], DFF one-per-role, no dicts, no variant_id, all required params present)

5. **Gate Severity & Promotion Rules** (GIVEN: gates have severity levels) → (WHEN: promoting to live) → (THEN: P0 gates ALL pass else BLOCK, P1 gates ≥5/7 for "marginal", ≥6/7 for "ready", Recommendation: Ready/Marginal/Blocked)

**Definition of Done:**
- [ ] QualityGate abstract class and 7 implementations
- [ ] Gate evaluation logic correct for all 7 gates
- [ ] Quality panel rendering with traffic light icons
- [ ] Gate detail expansion and explanations
- [ ] Severity color coding (red/yellow/green)
- [ ] Phase 2 gates (5, 6) with profile/DFF validation
- [ ] Unit tests: 22+ tests (one per gate + combos)
- [ ] Integration test: validation_results.json processing
- [ ] Team review

---

### EPIC 2A: OPTIMIZATION FRAMEWORK (S9-S16)

#### Story S9: Optuna Study Setup & Integration
**Epic:** Optimization Framework
**Priority:** P1
**Story Points:** 5
**Dependencies:** S1, S11

**Acceptance Criteria:**
1. **Optuna Study Initialization** (GIVEN: new optimization run starting) → (WHEN: I call OptunaStudyManager.create_study(...)) → (THEN: Study created in SQLite, Name: strategy_id+timestamp, Direction: "maximize", Sampler: TPE, Pruner: MedianPruner, Storage: SQLite auto-commit)

2. **Parameter Profiles** (GIVEN: ≤70 active params invariant) → (WHEN: creating study) → (THEN: Config includes active_param_count_max:70, profile: "stable|return|rocket", Conditional space define-by-run, Pruning disabled for conditional params)

3. **Search Space Definition** (GIVEN: parameter bounds in YAML) → (WHEN: study created) → (THEN: Load bounds from katana/config/parameter_bounds_{profile}.yaml, Create Optuna suggests (int/float/categorical), Log scale supported, Constraints applied, Search space estimated)

4. **Checkpoint & Resume** (GIVEN: optimization interrupted) → (WHEN: I restart with same study_name) → (THEN: Existing study loaded from SQLite, Completed trials loaded, Best trial reported, Continues from trial N+1, No data loss, Log: "Resuming study... from trial 145/200")

5. **Multi-Profile Mass Optimization** (GIVEN: Phase 1 supports 3 profiles) → (WHEN: mass optimization runs) → (THEN: Create 3 studies (stable/return/rocket), Allocate 6000/1000/1000 trials, Run in parallel (8-10 workers), Checkpoint every 100 trials, Resume from checkpoints, Final: 3 champion configs)

**Definition of Done:**
- [ ] OptunaStudyManager class implemented
- [ ] Study creation with TPE sampler working
- [ ] SQLite storage backend functional
- [ ] Parameter bounds loading from YAML
- [ ] Checkpoint/resume logic tested
- [ ] Multi-profile study creation (3 profiles)
- [ ] Constraint validation (relative, ratio)
- [ ] Log-scale parameter support
- [ ] Unit tests: 18+ tests
- [ ] Integration test: real study creation and resume
- [ ] Phase 2 design drafted (REST API)
- [ ] Team review

---

#### Story S10: Objective Functions & Backtest Wrapper
**Epic:** Optimization Framework
**Priority:** P1
**Story Points:** 8
**Dependencies:** S1, S9

**Acceptance Criteria:**
1. **Objective Function Interface** (GIVEN: Optuna study running) → (WHEN: trial sampled) → (THEN: Objective function called with trial/strategy_params/backtest_config, Returns: float objective value)

2. **Profile-Specific Objective** (GIVEN: 3 profiles) → (WHEN: study evaluates) → (THEN: stable: maximize Sharpe (DD ≤25%, WinRate ≥50%), return: maximize Calmar (Sharpe ≥1.0, MaxLoss ≤30%), rocket: maximize Return (MaxLoss ≤10% rocket bucket))

3. **Backtest Execution** (GIVEN: trial params sampled) → (WHEN: objective runs) → (THEN: Create temp config, Call BacktestExecutor.run(config), Extract metrics, Apply constraints (reject if violated), Log trial details, Return objective value)

4. **K-Fold Cross-Validation** (GIVEN: preventing overfitting) → (WHEN: objective executes) → (THEN: K=5 folds with embargo (20 days), Train on 4/test on 1, Run backtest per fold, Return average metric, Log per-fold results, Early stop if plateau)

5. **Pruning & Early Stopping** (GIVEN: large parameter space) → (WHEN: trial intermediate evaluation) → (THEN: Report intermediate value after each month, Pruner evaluates "promising?", If below median suggest pruning, Log pruning reason, Early stopping saves ≥20% computational cost per NFR-OPT-003)

**Definition of Done:**
- [ ] ObjectiveFunction base class and 3 profile implementations
- [ ] BacktestExecutor wrapper around vectorbt
- [ ] Metrics calculation (sharpe, calmar, return, etc.)
- [ ] Constraint validation logic
- [ ] K-fold cross-validation integrated
- [ ] Early stopping and pruning configured
- [ ] Trial logging comprehensive
- [ ] Unit tests: 20+ tests
- [ ] Integration test: real trial execution
- [ ] Performance: single trial <2 minutes
- [ ] Team review

---

#### Story S11: Parameter Bounds & Constraints Engine
**Epic:** Optimization Framework
**Priority:** P1
**Story Points:** 5
**Dependencies:** S1, S9

**Acceptance Criteria:**
1. **Parameter Bounds in YAML** (GIVEN: new optimization profile) → (WHEN: I read katana/config/parameter_bounds_{profile}.yaml) → (THEN: See parameter_bounds section with sma_fast (type:int, min:5, max:50, log_scale:false, active:true), sma_slow, rsi_period, DFF parameters (dff_sl_source_type categorical, dff_sl_period int, dff_sl_pct float conditional))

2. **Active Parameter Count Invariant** (GIVEN: configuration with bounds) → (WHEN: I load bounds) → (THEN: Count active params, Assert active_param_count ≤70 HARD INVARIANT, Log warning if >50, Per-profile: stable ~30-45, return ~35-50, rocket ~40-70, Reject trial at runtime if >70)

3. **Relative & Ratio Constraints** (GIVEN: parameter relationships) → (WHEN: bounds loaded) → (THEN: Constraints section enforces: relative (fast < slow), ratio (slow/fast ≥2.0), conditional (dff_sl_period depends on dff_sl_source_type))

4. **DFF Flat Parameter Validation** (GIVEN: DFF flat structure) → (WHEN: bounds validated) → (THEN: Per-role: 1 source_type param, Additional params conditional on source, Validation error if dict-stored or variant_id found, Validation warning if required param missing)

5. **Search Space Estimation** (GIVEN: bounds and constraints) → (WHEN: study initialized) → (THEN: Estimate total combinations (product of domains), Log "Estimated: 1.5e8 combinations", Pruned space "3.2e7 valid", Recommendation "TPE should find good regions in <200 trials", Warning if >1e10)

**Definition of Done:**
- [ ] Parameter bounds YAML format documented
- [ ] ParameterBounds class loading and validation
- [ ] Active param count invariant (≤70) enforced
- [ ] Relative and ratio constraints validated
- [ ] Conditional constraints (DFF) working
- [ ] DFF flat parameter validation (no dicts, no variant_id)
- [ ] Search space estimation and logging
- [ ] Unit tests: 20+ tests
- [ ] Integration test: real bounds loading
- [ ] 3 profiles with realistic bounds
- [ ] Team review

---

#### Stories S12-S16: Optimization Framework Continuation

**S12: K-Fold Cross-Validation** (5 SP) — Purged K-fold with embargo, metrics per fold, overfitting detection

**S13: Walk-Forward Windows** (5 SP) — Rolling window generator, in-sample/OOS periods, temporal validation

**S14: UMAP Clustering** (8 SP) — Parameter space embedding (50+ → 2D/3D), cluster identification, interactive viz

**S15: Pareto Front Analysis** (8 SP) — Multi-objective trade-offs, Pareto frontier, solution exploration

**S16: Trial Logging & Monitoring** (5 SP) — Progress tracking, metric logging per trial, early stopping logged, real-time output

---

### EPIC 2B: WALK-FORWARD VALIDATION (S17-S24)

#### Stories S17-S24: Walk-Forward Validation Suite (Summarized)

**S17: Walk-Forward Window Generator** (5 SP) — Generate IS/OOS windows, configurable size/stride, temporal validation, Phase 2: Dynamic API, rebalancing

**S18: Rolling Window Backtesting** (8 SP) — Execute backtests per window, aggregate metrics, performance degradation tracking, Phase 2: Distributed processing

**S19: Degradation Analysis** (8 SP) — IS vs OOS Sharpe, degradation metric, gate check (OOS ≥80% IS), overfitting pattern identification, Phase 2: Continuous monitoring

**S20: PBO Calculation** (5 SP) — Probability of Backtest Overfitting, rank strategies, PBO < 50% gate, recommendation, Phase 2: Real-time streaming

**S21: Correlation Analysis** (5 SP) — IS/OOS correlation, live vs paper correlation, gate check (>0.8), trend tracking, Phase 2: Continuous tracking

**S22: Quality Gate Enforcement** (5 SP) — Consolidate 7 gates, P0/P1 rules, summary generation, promotion rules (Ready/Marginal/Blocked), Phase 2: Auto-kill switches, webhooks

**S23: Validation Report Generation** (5 SP) — Comprehensive report (Executive Summary, Per-Gate Results, Degradation, PBO, Recommendations), Export HTML/PDF, Phase 2: Scheduling, email

**S24: Test Coverage** (8 SP) — Unit tests (30+), Integration tests (3+), Load test (8+ windows), 95%+ coverage, Performance benchmarks, Phase 2: Load test 1000+ windows

---

## Summary Statistics

**Total Stories:** 25 (S0.5-S1, S2-S8, S9-S24)
**Total Story Points:** ~155 SP
**Estimated Hours:** 140-180 hours
**Estimated Duration:** 21 days (3 devs), 42 days (1 dev)
**Quality Target:** 95%+ test coverage
**Timeline:** 14-21 days (Phase 1 execution)

**Phase 2 Preview:** All stories designed with REST API, async jobs, real-time streaming, authentication extensibility.

**Critical Items:**
- Parameter Profiles system (≤70 active params)
- DFF flat parameter structure (no dicts/variant_id)
- 7 mandatory quality gates
- NFR integration (NFR-1 through NFR-OPT-004)
- Wave 4 mass optimization (8,000 trials/day)

---

**Prepared By:** Planning Agent (PLANNER)
**Date:** 2026-02-26
**Version:** 2.0 (Phase 2 Aware)
**Status:** READY FOR DEVELOPMENT
