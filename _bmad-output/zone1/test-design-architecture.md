---
stepsCompleted: ['step-01-detect-mode', 'step-02-load-context', 'step-03-risk-and-testability', 'step-04-coverage-plan', 'step-05-generate-output']
lastStep: 'step-05-generate-output'
lastSaved: '2026-02-26'
workflowType: 'testarch-test-design'
mode: 'system-level'
inputDocuments:
  - 'katana-v-02-prd-katana-vectorbt-2026-01-18.md'
---

# Test Design for Architecture: katana-vectorbt System

**Purpose:** Architectural concerns, testability gaps, and NFR requirements for review by Architecture/Dev teams. Serves as a contract between QA and Engineering on what must be addressed before test development begins.

**Date:** 2026-02-26
**Author:** TEA Agent (BMAD testarch-test-design workflow)
**Status:** Architecture Review Pending
**Project:** katana-vectorbt
**PRD Reference:** katana-v-02-prd-katana-vectorbt-2026-01-18.md
**Scope:** phase2_requirements (full feature set — all Phases, Epics E–J, Wave 4)

---

## Executive Summary

**Scope:** Full system-level test architecture for katana-vectorbt, a single-user algorithmic trading autonomy platform. Covers Phase 1 (Static HTML Dashboard), Phase 4 (MTF + Risk), Epic J (Mass Optimization), and Wave 4 (6 TFs + DFF + Rockets + Calendar Safety + 100+ parameters).

**Business Context** (from PRD):
- **Impact:** Passive income from live trading — deploy a champion portfolio of ≥3 strategies with net P&L > 0 over 14 consecutive calendar days (scaled-live), MaxDD ≤ 25%, operator time ≤ 3 hours/week.
- **Problem:** 95% of algo trading strategies fail in live trading due to overfitting, unrealistic costs, and lack of statistical rigor.
- **Timeline:** 90-day goal (current phase: Epic J integration + Phase 1 MVP gap closure).

**Architecture** (from PRD Technical Architecture section):
- **Core Stack:** vectorbt Pro (backtesting), Optuna TPE multivariate (optimization, conditional search space, active_param_count ≤ 70), AFML-inspired feature engineering, custom DSR/PBO/CSCV/Walk-Forward, Plotly (Phase 1 HTML dashboard), CLI/Dagu DAG orchestration.
- **Storage:** SQLite (Phase 1), PostgreSQL (OHLCV cache + Wave 4 multi-TF), Optuna RDB backend.
- **Parallelization:** ProcessPoolExecutor 8–10 workers for optimization (≤8,000 total trials per run in ≤1 day).
- **Data contracts:** Immutable run artifacts under `runs/<run_id>/` — backtest_summary.json, optimizer_summary.json, risk_flags.json, signal_quality.json, pa_patterns.json, progress.json, events.ndjson.

**Expected Scale:**
- 8,000 total optimization trials per run (fixed budget), ~1,000–1,200 configs per TF × 6 TFs.
- ~5,000 backtests/min (10 cores, vectorized).
- 100K+ entries in vector knowledge base (HNSW <100ms search latency).
- Single-user, single-node operation (Phase 1).

**Risk Summary:**
- **Total risks**: 28
- **High-priority (Score ≥6)**: 11 risks requiring immediate mitigation
- **Test effort**: ~180 tests (~6–8 weeks for 1 QA/dev engineer)

---

## Quick Guide

### BLOCKERS - Team Must Decide (Can't Proceed Without)

**Pre-Implementation Critical Path** — These MUST be completed before QA can write integration tests:

1. **B-001: Deterministic Seed Contract** — Every optimization trial, backtest, and Monte Carlo simulation must expose a `seed` parameter that guarantees identical reproducibility across machines and OS platforms. Without this, integration tests cannot assert exact numeric results. (Recommended owner: Dev/Architect)

2. **B-002: Testability Hooks for Time-Windowed Logic** — Calendar Safety (HARD/SOFT) and session filter logic depend on wall-clock time. Architecture must expose a `clock_source` abstraction (injectable mock) or deterministic fixture mechanism so tests can simulate arbitrary timestamps without relying on real calendar data. (Recommended owner: Dev)

3. **B-003: Optuna Study Isolation Per Test** — Integration tests that exercise the optimization pipeline must create isolated Optuna studies per test (in-memory or per-test SQLite). Without isolation, test parallelization will corrupt shared study state. Architecture must provide a `create_study(storage="in-memory")` test factory. (Recommended owner: Dev)

4. **B-004: Artifact Schema Versioning Contract (FR0.2a)** — All JSON artifacts (progress.json, events.ndjson, risk_flags.json, signal_quality.json) must include a `schema_version` field before integration tests can validate backward compatibility. The versioning contract (v1.0 → v1.5 → v2.0 migration rules) must be finalized. (Recommended owner: Architect/Dev)

5. **B-005: ProcessPoolExecutor Test Shim** — Integration tests for the 8–10 worker parallel optimization cannot run in standard pytest environments without a worker-count override or sequential execution mode. Architecture must provide `--n-workers 1` CLI flag for test execution. (Recommended owner: Dev)

**What we need from team:** Complete these 5 items pre-implementation or integration test development is blocked.

---

### HIGH PRIORITY - Team Should Validate (We Provide Recommendation, You Approve)

1. **R-001: Overfitting in Conditional Search Space** — With 115 total parameters (active_param_count ≤ 70), the optimizer may exploit parameter interactions not visible in IS data. Recommendation: add per-parameter sensitivity analysis as a post-optimization diagnostic. (Owner: Dev/Quant)
2. **R-004: Data Leakage in Walk-Forward CV** — Purged K-Fold with embargo must be validated to have zero lookahead in feature generation. Recommendation: automated leakage detection suite run before every optimization. (Owner: Dev)
3. **R-007: DFF NaN Propagation** — `prepare_features()` must guarantee 0% NaN in all `dist_*` columns or downstream SL/TP calculations silently produce incorrect trades. Recommendation: add a contract test asserting 0% NaN before any backtest. (Owner: Dev)
4. **R-010: Rocket Portfolio Circuit Breaker Timing** — The circuit breaker must trigger within 60 seconds of 6+ simultaneous rocket deaths. At high load, the monitoring loop may miss the threshold. Recommendation: dedicated circuit breaker worker thread with sub-second polling. (Owner: Architect)
5. **R-015: MTF Cache Isolation** — Per-timeframe PostgreSQL tables (`ohlcv_1m`...`ohlcv_1d`) must be isolated from cross-contamination. Recommendation: schema-level TF separation + FK constraints in test fixtures. (Owner: Dev/DBA)

**What we need from team:** Review recommendations and approve (or suggest changes).

---

### INFO ONLY - Solutions Provided (Review, No Decisions Needed)

1. **Test strategy**: Unit (60%) / Integration (30%) / E2E (10%) — Python pytest ecosystem, deterministic fixtures, no browser automation required (CLI/Python-only project).
2. **Tooling**: pytest + pytest-xdist (parallel), hypothesis (property-based), pytest-mock, numpy.testing, pandas.testing, vectorbt backtest fixtures.
3. **Tiered execution**: PRs (<15 min, unit + integration), nightly (performance + Monte Carlo stress), weekly (full Wave 4 regression + 8,000-trial optimization smoke test).
4. **Coverage**: ~180 test scenarios prioritized P0–P3 with risk-based classification. Existing suite: 350+ tests already passing.
5. **Quality gates**: DSR ≥ 0.95, PBO < 0.50, WF degradation ≤ 15%, MaxDD ≤ 25% — validated per test run.

**What we need from team:** Just review and acknowledge (we already have the solution).

---

## For Architects and Devs - Open Topics

### Risk Assessment

**Total risks identified**: 28 (11 high-priority score ≥6, 10 medium, 7 low)

#### High-Priority Risks (Score ≥6) - IMMEDIATE ATTENTION

| Risk ID | Category | Description | Probability | Impact | Score | Mitigation | Owner | Timeline |
|---------|----------|-------------|-------------|--------|-------|------------|-------|----------|
| **R-001** | **TECH** | Conditional search space (active_param_count ≤ 70) exploited by optimizer — IS performance doesn't reflect OOS reality | 3 | 3 | **9** | DSR-adjusted objective + PBO penalty + OOS Walk-Forward mandatory; sensitivity analysis post-optimization | Dev/Quant | Epic J |
| **R-002** | **BUS** | Strategy passes all offline gates but degrades in micro-live — 3-stage pipeline fails to detect live degradation | 2 | 3 | **6** | Live Gate A + B mandatory; PSR_live ≥ 0.85 gate; 14-day scaled-live requirement | Dev | Phase 4 |
| **R-003** | **DATA** | Data leakage / lookahead bias invalidates backtests — purging + embargo misconfigured | 2 | 3 | **6** | FR40 automated leakage detection + data_hash freeze (FR39) every run | Dev | All phases |
| **R-004** | **DATA** | Walk-Forward CV feature leakage — AFML-derived features (fractional diff, labels) have lookahead if not purged correctly | 3 | 2 | **6** | Purged K-Fold with embargo enforced; automated test asserts no future data in features | Dev | Phase 3+ |
| **R-005** | **PERF** | 8,000-trial budget exceeded or time limit missed — optimization doesn't complete in ≤1 day on 8–10 workers | 2 | 3 | **6** | ProcessPoolExecutor 8–10 workers + RDB storage + checkpoint+resume; throughput benchmark test | Dev | Epic J |
| **R-006** | **TECH** | Rocket correlation circuit breaker fires too slowly — 6+ rocket deaths detected >60s after trigger | 2 | 3 | **6** | Dedicated monitoring thread with sub-second polling; integration test simulates 6 simultaneous kills | Architect | Wave 4 |
| **R-007** | **DATA** | DFF NaN propagation — `dist_*` columns contain NaN → SL/TP computed from NaN → incorrect trade prices silently | 3 | 2 | **6** | `prepare_features()` must guarantee 0% NaN; contract test runs before every backtest; FR-W4-DFF03 | Dev | Wave 4 |
| **R-008** | **BUS** | Calendar Safety (HARD) fires false positives — blocks profitable trades during events that don't affect the pair | 2 | 3 | **6** | Pair-specific event filtering (FR0.11-HARD); MaxDD reduction ≥10% quality gate for Calendar Safety | Dev | Phase 4 |
| **R-009** | **TECH** | Parameter profile invariant broken — active_param_count > 70 allowed by optimizer → trial budget wasted on invalid configs | 3 | 2 | **6** | Strict enforcement: trials violating invariant pruned BEFORE backtest; unit test: 10,000 random trials assert 100% compliance | Dev | Epic J |
| **R-010** | **OPS** | Rollback command fails — `time-to-rollback > 5 minutes` when multiple artifact stores exist (registry.db + run artifacts) | 2 | 3 | **6** | Test rollback CLI command on each release; single-command restore validated in CI | Dev | All phases |
| **R-011** | **SEC** | Run artifact integrity — artifacts in `runs/<run_id>/` modified post-generation → reproducibility guarantee broken | 2 | 3 | **6** | data_hash (SHA256) stored in Run Journal; artifact integrity check before report generation | Dev | All phases |

#### Medium-Priority Risks (Score 3-5)

| Risk ID | Category | Description | Probability | Impact | Score | Mitigation | Owner |
|---------|----------|-------------|-------------|--------|-------|------------|-------|
| R-012 | PERF | Dashboard load time >5 min for 8,000-trial result set | 2 | 2 | 4 | Offline parse/index + top-N selection pre-computed; benchmark test <5 min | Dev |
| R-013 | TECH | MTF confirmation mode (hard_block) reduces DSR vs "none" mode — kill-switch not triggered | 2 | 2 | 4 | `mtf_delta_DSR_vs_none` metric mandatory; auto-rollback test simulation | Dev |
| R-014 | DATA | Schema drift between artifact versions — UI shows wrong data for v1.0 artifacts when v2.0 is deployed | 2 | 2 | 4 | schema_version field in all artifacts; UI fallback logic tested for v1.0, v1.5, v2.0 | Dev |
| R-015 | TECH | Per-TF PostgreSQL table isolation — cross-contamination of 1m data into 5m optimization | 2 | 2 | 4 | Schema-level TF separation; FK constraints; integration test asserts 0% parameter bleed | Dev |
| R-016 | BUS | Beacon level miscalculation — degradation rules applied in wrong order (Rule 1 not absolute priority) | 2 | 2 | 4 | Unit test: Rule 1 (MACD) overrides all others; precedence integration test | Dev |
| R-017 | PERF | Memory pressure — 2–4GB per worker × 10 workers = 20–40GB RAM at peak | 2 | 2 | 4 | Memory profiling benchmark; worker count auto-adjustment based on available RAM | Architect |
| R-018 | OPS | Checkpoint+resume corrupted — optimization resumes from wrong trial after crash | 2 | 2 | 4 | Checkpoint integrity test: crash at trial N, resume, assert N+1 continues correctly | Dev |
| R-019 | TECH | Kelly Criterion applied before N_live_trades ≥ 100 threshold — invalid allocation | 2 | 2 | 4 | Integration test: Kelly blocked when N<100 or PSR_live<0.85 | Dev |
| R-020 | DATA | data_hash mismatch — different platforms produce different SHA256 for same logical dataset | 2 | 2 | 4 | Cross-platform hash consistency test (Windows + Linux) | Dev |
| R-021 | BUS | Wilson Score kill switch ignores small-sample protection — kills rocket with N<50 trades | 2 | 2 | 4 | Safety gate unit test: N<50 → skip kill switch; N≥50 → apply LCB formula | Dev |

#### Low-Priority Risks (Score 1-2)

| Risk ID | Category | Description | Probability | Impact | Score | Action |
|---------|----------|-------------|-------------|--------|-------|--------|
| R-022 | OPS | Dagu DAG YAML misconfiguration — step skipped silently | 1 | 2 | 2 | Manual review of DAG YAMLs; validate exit codes on each step | Monitor |
| R-023 | TECH | CUDA GPU fallback — optimization falls back to CPU, no alert | 1 | 2 | 2 | Log GPU/CPU mode at startup; performance test on CPU baseline | Monitor |
| R-024 | DATA | Market data provider outage — data sync fails silently during optimization | 1 | 2 | 2 | Data freshness check before optimization start; provider failover | Monitor |
| R-025 | BUS | Rocket profit transfer (80% to core) miscalculated — wrong bucket balance | 1 | 2 | 2 | Unit test: exact arithmetic for profit transfer formula | Monitor |
| R-026 | OPS | Strategy Registry schema migration fails — candidates lost | 1 | 2 | 2 | Registry backup before migration; restore test | Monitor |
| R-027 | TECH | Divergence AUX condition (O(n²)) performance — disabled by default but if enabled, hangs backtester | 1 | 2 | 2 | Performance test: divergence enabled on 10K bars, assert <30s | Monitor |
| R-028 | BUS | HTML dashboard PDF/PNG export corrupt for large datasets | 1 | 1 | 1 | Manual test for export with >8,000 trial results | Monitor |

---

### Testability Concerns and Architectural Gaps

**ACTIONABLE CONCERNS - Architecture Team Must Address**

#### 1. Blockers to Fast Feedback (WHAT WE NEED FROM ARCHITECTURE)

| Concern | Impact on Testing | What Architecture Must Provide | Owner | Timeline |
|---------|-------------------|-------------------------------|-------|----------|
| **Wall-clock dependency in Calendar Safety** | Tests cannot deterministically simulate pre/post event windows without real timestamps | `clock_source: ClockProtocol` injectable in KatanaTransformer and CalendarSafety modules; test fixture provides `FakeClock(datetime)` | Dev | Pre-Epic J |
| **Optuna study not isolated in integration tests** | Parallel pytest runs corrupt shared Optuna RDB study state → non-deterministic test failures | `create_study(storage="in-memory", sampler=QMCSampler(seed=N))` test factory exposed as pytest fixture | Dev | Pre-Epic J |
| **No `--n-workers 1` override for optimizer** | CI cannot run optimization integration tests without spawning 10 processes → OOM on CI runners | `--n-workers N` flag on all mass_optimize CLI commands; default=1 in test config | Dev | Pre-Epic J |
| **ProcessPoolExecutor pickling errors for complex objects** | Custom samplers and callbacks may not pickle correctly → worker process crashes silently | All sampler and callback objects must pass `pickle.dumps(obj)` contract test | Dev | Pre-Epic J |
| **Artifact schema_version missing** | Cannot test backward compatibility (v1.0 UI with v2.0 artifacts) | Add `schema_version` field to all JSON artifacts (progress.json, events.ndjson, risk_flags.json, signal_quality.json, pa_patterns.json, optimizer_summary.json) | Dev | Pre-Epic J |

#### 2. Architectural Improvements Needed (WHAT SHOULD BE CHANGED)

1. **Centralized Artifact Registry for Test Discovery**
   - **Current problem**: Each integration test must manually construct `runs/<run_id>/` paths and verify artifact existence ad-hoc.
   - **Required change**: Provide `ArtifactRegistry.list_artifacts(run_id)` and `ArtifactRegistry.validate_schema(artifact_path, schema_version)` utilities for test assertions.
   - **Impact if not fixed**: Test code duplicates artifact path logic, becomes brittle to directory structure changes.
   - **Owner**: Dev
   - **Timeline**: Pre-Epic J

2. **Rocket Monitoring Loop Testability**
   - **Current problem**: The hourly kill-switch check and circuit breaker (60-second SLA) cannot be tested without time manipulation.
   - **Required change**: Extract monitoring loop into `RocketMonitor` class with injectable `check_interval_seconds` and `clock` parameters. Test fixture uses `check_interval_seconds=0` and `FakeClock`.
   - **Impact if not fixed**: Circuit breaker timing SLA (60s) is untestable in CI.
   - **Owner**: Architect
   - **Timeline**: Wave 4 pre-implementation

3. **MTF Confirmation Telemetry Assertions**
   - **Current problem**: `mtf_block_rate`, `mtf_delta_DSR_vs_none`, and `mtf_shadow_pnl_blocked` are computed but not asserted in CI. Auto-rollback logic cannot be unit-tested.
   - **Required change**: Expose `MTFConfirmationMetrics` as a typed dataclass returned by the strategy run; write property-based tests asserting rollback triggers when `mtf_block_rate > mtf_block_rate_max`.
   - **Impact if not fixed**: MTF kill-switch logic untested; could silently fail in production.
   - **Owner**: Dev
   - **Timeline**: Phase 4 implementation

4. **DFF Precomputation Contract Test**
   - **Current problem**: `prepare_features()` correctness for all 10 `dist_*` columns relies on manual review of 37 unit tests. No automated NaN assertion runs before every backtest.
   - **Required change**: Add `assert_no_nan_in_dist_columns(df)` call at the top of `KatanaTransformer.generate_signals()`. This assertion runs in production (not just tests) and raises `DataIntegrityError` if violated.
   - **Impact if not fixed**: NaN in dist columns silently produces wrong SL/TP prices → undetected monetary loss.
   - **Owner**: Dev
   - **Timeline**: Wave 4 DFF implementation

---

### Testability Assessment Summary

#### What Works Well

- ✅ **CLI-first design** — Every autonomy loop step (`sync`, `build`, `backtest`, `optimize`, `validate`, `register`, `promote`, `deploy_micro`, `deploy_scaled`, `monitor`, `reoptimize`, `report`) has deterministic CLI entrypoints with exit codes, enabling subprocess-level integration testing.
- ✅ **Immutable run artifacts** — `runs/<run_id>/` structure provides a stable test assertion target: tests can validate artifact existence, schema, and content without knowledge of internal state.
- ✅ **Deterministic seeds** — Fixed seeds in backtesting and Optuna (QMC seed) already exist; extending to all Monte Carlo simulations is a bounded change.
- ✅ **350+ existing tests** — Brownfield baseline with high coverage in risk, sizing, MTF combiner, Kelly, tail risk, and stress test modules.
- ✅ **KatanaTransformer as testability boundary** — Central transformer class provides a clean integration test entry point: given config + OHLCV data → assert signals + metrics.
- ✅ **Data quality validation (FR38)** — Existing `DataQualityCheck` validates missing values, outliers, timestamp monotonicity before any optimization run.

#### Accepted Trade-offs (No Action Required)

For katana-vectorbt Phase 1 MVP, the following trade-offs are acceptable:

- **No E2E browser testing** — Phase 1 dashboard is a static HTML file; UI interactivity tested via manual smoke test + HTML validation. No browser automation (Playwright/Cypress) required until Phase 2 hosted app.
- **Single-node optimization only** — Multi-node distributed optimization deferred; integration tests run on single node with `--n-workers` override.
- **No live-exchange integration testing** — MT5 and CCXT connections tested with paper trading mode only; actual live order execution validated by operator in micro-live phase.

---

### Risk Mitigation Plans (High-Priority Risks ≥6)

#### R-001: Conditional Search Space Exploitation (Score: 9) - CRITICAL

**Mitigation Strategy:**
1. DSR-adjusted Sharpe is the mandatory primary objective (not raw IS Sharpe) for all optimization trials — enforced in `objective_function()` via `calculate_deflated_sharpe_ratio()`.
2. PBO penalty applied (weight=0.05) to composite objective: `objective = 0.30×DSR + 0.15×Sortino + ... - 0.05×PBO_penalty`.
3. Post-optimization diagnostic: per-parameter sensitivity analysis (SHAP or permutation importance on DSR scores) exported to `optimizer_summary.json` for every run.
4. Property-based test (hypothesis): 10,000 random parameter vectors → assert DSR calculation is monotonically bounded.

**Owner:** Dev/Quant
**Timeline:** Pre-Epic J deployment
**Status:** Planned
**Verification:** Integration test: run 200 trials on synthetic data, assert final DSR ≥ 0.95 for promoted strategies.

#### R-003: Data Leakage Prevention (Score: 6) - HIGH

**Mitigation Strategy:**
1. `freeze_dataset()` with SHA256 `data_hash` recorded in Run Journal at backtest start.
2. Automated leakage detection (FR40) runs as CI check: assert no future features in any feature matrix row.
3. Purged K-Fold with embargo (`purge=10 days`, `embargo=1%`) enforced — unit test validates no overlap between IS/OOS windows.
4. `data_hash` comparison: re-run same config with same `data_hash` → assert 100% identical results.

**Owner:** Dev
**Timeline:** Immediately (data integrity is P0)
**Status:** Partially complete (data_hash exists; leakage detection needs CI integration)
**Verification:** CI step: `pytest tests/integrity/ -m leakage` must pass in every PR.

#### R-006: Circuit Breaker 60-Second SLA (Score: 6) - HIGH

**Mitigation Strategy:**
1. `RocketMonitor` class with injectable `check_interval_seconds=1` in production, `check_interval_seconds=0` in tests.
2. Integration test: inject 6 simultaneous rocket deaths via `FakeRocketRegistry`, assert circuit breaker fires within 1 polling cycle.
3. Metric: `circuit_breaker_latency_ms` logged on every trigger; alert if >30,000ms (30s, warn at half SLA).

**Owner:** Architect
**Timeline:** Wave 4 pre-implementation
**Status:** Planned
**Verification:** Test simulates 6 simultaneous deaths → assert `circuit_breaker_triggered=True` within 1s (100ms test tolerance).

#### R-007: DFF NaN Propagation (Score: 6) - HIGH

**Mitigation Strategy:**
1. `prepare_features()` forward-fills NaN in all `dist_*` columns with fallback to `atr_14` column.
2. `assert_no_nan_in_dist_columns(df)` runtime assertion inside `generate_signals()` — raises `DataIntegrityError` in all environments.
3. FR-W4-DFF03 regression test: default `distance_source=atr_14` produces 0% NaN on 37 unit test fixtures.

**Owner:** Dev
**Timeline:** DFF Wave 4 implementation
**Status:** Partially complete (37 existing unit tests; runtime assertion needed)
**Verification:** Property-based test (hypothesis): random OHLCV slices → `prepare_features()` → assert NaN count = 0.

---

### Assumptions and Dependencies

#### Assumptions

1. Python 3.9+ available on all development and CI machines.
2. vectorbt Pro license is active; any breaking API changes in vectorbt Pro require re-validation of 350+ existing tests.
3. PostgreSQL 13+ available for Wave 4 multi-TF OHLCV caching; integration tests may use PostgreSQL test container or SQLite fallback for CI.
4. Optuna 3.x stable API (no breaking changes expected during Epic J timeline).
5. OHLCV data quality ≥95% (as per PRD assumptions); tests use frozen datasets to eliminate data quality variability.

#### Dependencies

1. **B-001 (Deterministic Seed Contract)** — Required before Epic J integration test development.
2. **B-002 (Clock Source Abstraction)** — Required before Calendar Safety integration tests.
3. **B-003 (Optuna Study Isolation)** — Required before any optimization pipeline integration tests.
4. **B-004 (Artifact Schema Versioning)** — Required before backward compatibility tests.
5. **B-005 (--n-workers 1 CLI Flag)** — Required before CI can run optimization integration tests without OOM.
6. **Wave 4 PostgreSQL schema finalized** — Required before per-TF caching integration tests.

#### Risks to Plan

- **Risk**: vectorbt Pro API changes break existing 350+ tests mid-Epic J development.
  - **Impact**: All signal generation and backtesting tests require re-validation.
  - **Contingency**: Pin vectorbt Pro version in requirements.txt; run regression suite before upgrading.

- **Risk**: PostgreSQL not available in CI environment for Wave 4 tests.
  - **Impact**: Per-TF caching integration tests cannot run.
  - **Contingency**: Provide SQLite fallback path in `load(symbol, tf)` for CI; mark PostgreSQL tests with `@pytest.mark.requires_postgres`.

---

**End of Architecture Document**

**Next Steps for Architecture Team:**
1. Review Blockers (B-001 through B-005) and assign owners with Sprint targets.
2. Prioritize R-001, R-003, R-006, R-007 (score ≥6) for immediate mitigation.
3. Provide `ClockProtocol` and `FakeRocket` test stubs for QA to start integration test scaffolding.
4. Confirm artifact schema_version contract before Epic J coding sprint begins.

**Next Steps for QA/Dev Team:**
1. Wait for Blockers B-001 through B-005 to be resolved.
2. Refer to companion QA doc (`test-design-qa.md`) for the full test coverage plan.
3. Begin test infrastructure setup: pytest fixtures, deterministic OHLCV datasets, Optuna in-memory study factory.
