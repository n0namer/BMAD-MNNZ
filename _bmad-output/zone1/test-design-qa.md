---
stepsCompleted: ['step-01-detect-mode', 'step-02-load-context', 'step-03-risk-and-testability', 'step-04-coverage-plan', 'step-05-generate-output']
lastStep: 'step-05-generate-output'
lastSaved: '2026-02-26'
workflowType: 'testarch-test-design'
mode: 'system-level'
inputDocuments:
  - 'katana-v-02-prd-katana-vectorbt-2026-01-18.md'
---

# Test Design for QA: katana-vectorbt System

**Purpose:** Test execution recipe for QA/Dev team. Defines what to test, how to test it, and what is needed from other teams.

**Date:** 2026-02-26
**Author:** TEA Agent (BMAD testarch-test-design workflow)
**Status:** Draft
**Project:** katana-vectorbt
**Scope:** phase2_requirements — full feature set (all Phases, Epics E–J, Wave 4)

**Related:** See Architecture doc (`test-design-architecture.md`) for testability concerns, architectural blockers (B-001 to B-005), and high-priority risk mitigation plans.

---

## Executive Summary

**Scope:** System-level test plan for katana-vectorbt — a single-user algorithmic trading autonomy platform. Covers all functional requirements from the PRD: KATANA Signal Framework, Optimization Pipeline (Epic J), Wave 4 (6 TFs + DFF + Calendar Safety), Risk Management Suite, Rocket Portfolio, Phase 1 Dashboard, and all Offline/Live quality gates.

**Risk Summary:**
- Total Risks: 28 (11 high-priority score ≥6, 10 medium, 7 low)
- Critical Categories: DATA (leakage, NaN propagation), TECH (conditional search space, DFF, circuit breaker), BUS (live degradation, false Calendar Safety blocks)

**Coverage Summary:**
- P0 tests: ~52 (critical paths, data integrity, offline gates, signal correctness)
- P1 tests: ~68 (integration paths, optimization pipeline, risk management)
- P2 tests: ~38 (edge cases, boundary conditions, regression)
- P3 tests: ~22 (performance benchmarks, exploratory, Monte Carlo stress)
- **Total**: ~180 tests (~6–8 weeks with 1 QA/Dev engineer)

**Note:** Existing suite has ~350+ passing tests covering Phase 3 (Phases 1–3 quant methodology). This plan focuses on the gap areas: Epic J, Wave 4, Phase 1 Dashboard completion, and Live Gate validation.

---

## Not in Scope

| Item | Reasoning | Mitigation |
|------|-----------|------------|
| **Phase 2 REST API** | Explicitly deferred; not required for 90-day single-user goal | Covered in future Phase 2 test plan |
| **Multi-user collaboration** | Single-user only (v1.0 scope) | N/A — feature deferred |
| **SOC2 / PCI-DSS compliance** | Enterprise compliance deferred to Phase 2+ | Risk accepted; documented in PRD |
| **Browser E2E automation (Playwright)** | Phase 1 is static HTML; no backend or live UI interactions | Manual smoke test + HTML schema validation |
| **MT5 / CCXT live order execution** | Real brokerage integration tested via paper trading mode; live testing is operator responsibility | Paper mode integration tests + operator micro-live validation |
| **Streamlit Phase 2 hosted app** | Deferred to Phase 2 | Phase 2 test plan |
| **GPU-accelerated backtesting** | Optional acceleration; CPU fallback tested | GPU path validated manually when CUDA available |

**Note:** Items listed here have been reviewed and accepted as out-of-scope by QA and Nikita (owner-operator).

---

## Dependencies & Test Blockers

**CRITICAL:** QA cannot proceed with integration test implementation without these items.

### Backend/Architecture Dependencies (Pre-Implementation)

**Source:** See Architecture doc "Blockers" section for detailed mitigation plans.

1. **B-001: Deterministic Seed Contract** — Dev — Sprint 1 of Epic J
   - Need: `seed` parameter exposed in all optimization, backtest, and Monte Carlo calls.
   - Blocks: Any integration test that asserts exact numeric results (DSR values, PBO scores, equity curves).

2. **B-002: Clock Source Abstraction (CalendarSafety)** — Dev — Pre-Wave 4
   - Need: Injectable `clock_source: ClockProtocol` in `CalendarSafety` and `KatanaTransformer`.
   - Blocks: All Calendar Safety integration tests (HARD/SOFT mode, pre/post buffers, position exit timing).

3. **B-003: Optuna Study Isolation** — Dev — Sprint 1 of Epic J
   - Need: `create_study(storage="in-memory", sampler=QMCSampler(seed=N))` pytest fixture.
   - Blocks: All optimization pipeline integration tests that use multiple workers.

4. **B-004: Artifact Schema Versioning (schema_version field)** — Dev/Architect — Pre-Epic J
   - Need: `schema_version` in `progress.json`, `events.ndjson`, `risk_flags.json`, `signal_quality.json`, `pa_patterns.json`, `optimizer_summary.json`.
   - Blocks: Backward compatibility tests (v1.0 → v2.0 artifact migration).

5. **B-005: --n-workers 1 CLI Override** — Dev — Pre-Epic J
   - Need: `--n-workers N` on all mass_optimize CLI commands.
   - Blocks: CI-safe optimization integration tests (prevents OOM on GitHub Actions runners).

### QA Infrastructure Setup (Pre-Implementation)

1. **Deterministic OHLCV Test Datasets**
   - Frozen OHLCV fixtures (SHA256-hashed) for each of 6 timeframes (1m, 5m, 15m, 1h, 4h, 1d)
   - Minimum: 1,000 bars per fixture (sufficient for Walk-Forward 5-window CV)
   - Location: `tests/fixtures/ohlcv/`
   - Owner: Dev

2. **Optuna In-Memory Study Factory**
   ```python
   @pytest.fixture
   def optuna_study(tmp_path):
       study = optuna.create_study(
           storage="sqlite:///:memory:",
           sampler=optuna.samplers.QMCSampler(seed=42),
           direction="maximize"
       )
       return study
   ```

3. **Artifact Validation Helpers**
   ```python
   def assert_artifact_schema(artifact_path: Path, schema_version: str):
       data = json.loads(artifact_path.read_text())
       assert data.get("schema_version") == schema_version
       assert "run_id" in data
       # ... schema-specific assertions
   ```

4. **FakeClock for Calendar Safety Tests**
   ```python
   class FakeClock:
       def __init__(self, fixed_time: datetime):
           self._time = fixed_time
       def now(self) -> datetime:
           return self._time
       def advance(self, minutes: int):
           self._time += timedelta(minutes=minutes)
   ```

5. **Test Environments**
   - Local: `pytest tests/ -m "unit" --n-workers 1` (fast, <5 min)
   - CI (GitHub Actions): `pytest tests/ -m "unit or integration" --n-workers 1 -x` (<15 min)
   - Nightly: `pytest tests/ -m "performance or monte_carlo" --n-workers 4` (30–60 min)
   - Weekly: Full regression suite including `tests/wave4/` (2–4 hours)

---

## Risk Assessment

**Note:** Full risk details in Architecture doc. This section summarizes risks relevant to QA test planning.

### High-Priority Risks (Score ≥6)

| Risk ID | Category | Description | Score | QA Test Coverage |
|---------|----------|-------------|-------|-----------------|
| **R-001** | TECH | Conditional search space exploitation — IS overfit | **9** | P0-OPT-001: DSR mandatory; P0-OPT-002: PBO < 0.50 gate; P1-OPT-010: sensitivity analysis output |
| **R-002** | BUS | Strategy passes offline gates but degrades in micro-live | **6** | P0-LIVE-001: Live Gate A full matrix; P0-LIVE-002: Live Gate B day-7 simulation |
| **R-003** | DATA | Data leakage / lookahead bias | **6** | P0-DATA-001: Automated leakage detection suite; P0-DATA-002: data_hash reproducibility |
| **R-004** | DATA | Walk-Forward CV feature leakage | **6** | P0-DATA-003: Purged K-Fold embargo validation; P1-DATA-004: Feature matrix lookahead check |
| **R-005** | PERF | 8,000-trial budget + 1-day time limit missed | **6** | P3-PERF-001: Throughput benchmark (8,000 trials ≤1 day); P1-OPT-005: checkpoint+resume test |
| **R-006** | TECH | Circuit breaker 60-second SLA | **6** | P0-ROCKET-001: Circuit breaker timing test (<60s); P1-ROCKET-002: 6-death simultaneous simulation |
| **R-007** | DATA | DFF NaN propagation → wrong SL/TP prices | **6** | P0-DFF-001: 0% NaN assertion on all dist_* columns; P0-DFF-002: property-based NaN test |
| **R-008** | BUS | Calendar Safety false positives — blocks trades incorrectly | **6** | P0-CAL-001: Pair-specific filtering test; P1-CAL-002: MaxDD reduction ≥10% quality gate |
| **R-009** | TECH | active_param_count > 70 allowed — invalid trials | **6** | P0-OPT-003: 10,000 random trials assert 100% invariant compliance |
| **R-010** | OPS | Rollback >5 minutes | **6** | P0-OPS-001: Rollback CLI timing test (≤5 min) |
| **R-011** | SEC | Artifact integrity violation — SHA256 mismatch | **6** | P0-DATA-005: Artifact integrity check before report generation |

### Medium/Low-Priority Risks

| Risk ID | Category | Description | Score | QA Test Coverage |
|---------|----------|-------------|-------|-----------------|
| R-012 | PERF | Dashboard load >5 min for 8,000 trials | 4 | P3-PERF-002: Dashboard load benchmark |
| R-013 | TECH | MTF kill-switch not triggered | 4 | P1-MTF-001: mtf_delta_DSR_vs_none auto-rollback |
| R-014 | DATA | Schema drift between artifact versions | 4 | P1-DATA-006: Backward compat v1.0→v2.0 |
| R-015 | TECH | Per-TF table cross-contamination | 4 | P1-WAVE4-001: 0% parameter bleed per TF |
| R-016 | BUS | Beacon level degradation rule precedence | 4 | P0-SIG-005: Rule 1 absolute priority test |
| R-017 | PERF | Memory pressure under 10 workers | 4 | P3-PERF-003: Memory profile benchmark |
| R-018 | OPS | Checkpoint+resume corruption | 4 | P1-OPT-006: Crash recovery test |
| R-019 | TECH | Kelly before N≥100 threshold | 4 | P1-RISK-001: Kelly eligibility gate test |
| R-020 | DATA | Cross-platform data_hash mismatch | 4 | P2-DATA-007: Hash consistency test |
| R-021 | BUS | Wilson Score small-sample protection | 4 | P0-ROCKET-003: Wilson LCB N<50 safety gate |

---

## Entry Criteria

**QA testing cannot begin until ALL of the following are met:**

- [ ] B-001 through B-005 blockers resolved (seed contract, clock abstraction, Optuna isolation, schema_version, n-workers flag)
- [ ] All requirements from PRD agreed upon by Nikita and Dev
- [ ] Deterministic OHLCV test fixtures committed to `tests/fixtures/ohlcv/` (SHA256-hashed)
- [ ] Optuna in-memory study factory available as pytest fixture
- [ ] `FakeClock` injectable into `CalendarSafety` module
- [ ] CI pipeline configured with `--n-workers 1` default
- [ ] Phase 1 Dashboard HTML generator code deployed to local dev environment

## Exit Criteria

**Testing phase is complete when ALL of the following are met:**

- [ ] All P0 tests passing (52 tests)
- [ ] All P1 tests passing or failures triaged and accepted by Nikita
- [ ] No open HIGH-severity bugs (data leakage, NaN propagation, circuit breaker SLA violations)
- [ ] DSR ≥ 0.95, PBO < 0.50, WF degradation ≤ 15% gates validated on at least one full optimization run
- [ ] Rollback CLI completes in ≤5 minutes on representative dataset
- [ ] Phase 1 HTML dashboard generates correctly for a 200-trial result set
- [ ] Calendar Safety HARD mode blocks confirmed on FOMC/NFP test fixtures
- [ ] 0% data leakage confirmed in automated leakage detection suite

---

## Project Team

| Name | Role | Testing Responsibilities |
|------|------|--------------------------|
| Nikita | Owner-Operator / PM | Requirements clarification, acceptance criteria, UAT sign-off, micro-live validation |
| Dev Team | Developer | Unit tests, integration test support, testability hook implementation (B-001 to B-005) |
| TEA Agent | QA Architect | Test strategy, test design document, coverage plan, risk assessment |

---

## Test Coverage Plan

**P0/P1/P2/P3 = priority and risk level** (focus here if time-constrained), NOT execution timing. See "Execution Strategy" for when tests run.

---

### P0 (Critical) — ~52 Tests

**Criteria:** Blocks core functionality + High risk (≥6) + No workaround + Affects autonomy loop or data integrity

#### Signal Framework (KATANA Core)

| Test ID | Requirement | Test Level | Risk Link | Notes |
|---------|-------------|------------|-----------|-------|
| **P0-SIG-001** | FR-SIG-CORE-001: All 5 CORE conditions computed correctly on synthetic OHLCV | Unit | R-001 | Deterministic synthetic fixture; assert boolean per condition |
| **P0-SIG-002** | FR-SIG-CORE-001: ma_cross_confirm — LONG/SHORT logic with confirmation_bars | Unit | - | Test rising/falling MA5 vs MA20, 2-3 bar confirmation |
| **P0-SIG-003** | FR-SIG-CORE-001: macd_impulse — BLOCK condition (hist < 0.0001) | Unit | R-016 | Assert mini beacon forced when hist ≈ 0 |
| **P0-SIG-004** | FR-SIG-CORE-001: mtf_trend — h1 ↔ h4 alignment | Unit | - | Synthetic h1 + h4 fixture; assert directional alignment |
| **P0-SIG-005** | FR-SIG-DEGRADE-001: Rule 1 (MACD) absolute priority over Rules 2–5 | Unit | R-016 | If macd_impulse=False → beacon=mini regardless of other rules |
| **P0-SIG-006** | FR-SIG-DEGRADE-001: All 5 degradation rules applied independently | Unit | R-016 | Property-based: Rule 2 fires when fractal_breakout=False + beacon in [working, kotleta] |
| **P0-SIG-007** | FR-SIG-BEACON-001: Confidence formula correctness — weighted 0.8*core + 0.2*aux | Unit | - | Assert formula against known core/aux combinations |
| **P0-SIG-008** | FR-SIG-BEACON-001: Beacon level mapping — all 4 levels correct | Unit | R-016 | Assert confidence 0.60→mini, 0.70→mayak, 0.80→working, 0.95→kotleta |
| **P0-SIG-009** | FR-SIG-METRICS-001: signal_quality.json artifact generated per run | Integration | R-011 | Assert artifact exists, schema matches spec, all required fields present |
| **P0-SIG-010** | FR-SIG-SESSION-001: Monday 00:00–06:00 UTC exclusion | Unit | - | FakeClock at Monday 03:00 UTC → assert no entries generated |
| **P0-SIG-011** | FR-SIG-SESSION-001: Calendar Safety HARD blocks entries in event window | Integration | R-008 | FakeClock at T-100min (pre-buffer=120) + NFP event → assert allow_long=False, allow_short=False |

#### Data Integrity & Reproducibility

| Test ID | Requirement | Test Level | Risk Link | Notes |
|---------|-------------|------------|-----------|-------|
| **P0-DATA-001** | FR40: No data leakage / lookahead bias in feature generation | Integration | R-003, R-004 | Automated leakage detector: no row N has feature from row N+k |
| **P0-DATA-002** | FR39: Same data_hash → identical backtest results (deterministic) | Integration | R-003 | Run twice with frozen dataset; assert all metrics identical |
| **P0-DATA-003** | FR40: Walk-Forward purge + embargo — no IS/OOS overlap | Unit | R-004 | Assert IS bars end before OOS bars start; embargo gap enforced |
| **P0-DATA-004** | FR38: Data quality validation — missing values <1%, outliers >10% rejected | Unit | - | Synthetic dataset with 2% gaps + price spike; assert validation catches both |
| **P0-DATA-005** | FR0.2: data_hash recorded in Run Journal; artifact integrity check | Integration | R-011 | Modify artifact post-generation → assert integrity check raises error |

#### Optimization Pipeline (Epic J)

| Test ID | Requirement | Test Level | Risk Link | Notes |
|---------|-------------|------------|-----------|-------|
| **P0-OPT-001** | FR-OPT-006: DSR-adjusted Sharpe is mandatory primary objective | Unit | R-001 | Assert `calculate_deflated_sharpe_ratio()` called for every trial |
| **P0-OPT-002** | FR-OPT-007: PBO < 0.50 quality gate enforced | Integration | R-001 | Generate synthetic results with PBO=0.60 → assert gate blocks promotion |
| **P0-OPT-003** | Parameter Profiles: active_param_count ≤ 70 invariant — 10,000 random profiles | Unit | R-009 | Property-based (hypothesis): 10,000 profiles; assert 100% compliance or TrialPruned |
| **P0-OPT-004** | FR-OPT-001: Conditional search space — constraints respected in all trials | Unit | R-009 | Assert ma_slow > ma_fast + 5 always; take_profit > stop_loss * 1.5 always |
| **P0-OPT-005** | FR-OPT-005: QMC (32 trials) → TPE transition | Integration | - | Mock optimizer; assert QMC sampler used for trials 0–31, TPE for trials 32+ |
| **P0-OPT-006** | FR-OPT-016: Complexity budget — >4 active blocks → TrialPruned (no backtest) | Unit | - | Assert trials with complexity=5 return TrialPruned status instantly |
| **P0-OPT-007** | FR-OPT-013: Immutable run artifacts — every run writes complete artifact set | Integration | R-011 | Run 10 trials; assert all artifacts present in runs/<run_id>/ |

#### Offline Quality Gates

| Test ID | Requirement | Test Level | Risk Link | Notes |
|---------|-------------|------------|-----------|-------|
| **P0-GATE-001** | FR-GATE-004: PSR ≥ 0.95 (stable), ≥ 0.90 (return), ≥ 0.80 (rocket) | Unit | - | Assert calculation matches statistical definition; gate blocks strategies below threshold |
| **P0-GATE-002** | FR-GATE-004: MTRL minimum trades enforced by profile | Unit | - | Stable: N≥60, Return: N≥40, Rocket: N≥20; assert gate blocks if N < MTRL_min |
| **P0-GATE-003** | FR-GATE-006: Bootstrap stress — p-value < 0.05 for all 4 scenarios | Unit | - | Normal / High Vol / Low Liq / Black Swan scenarios; assert Sharpe_effective ≥ 0.70×backtest |
| **P0-GATE-004** | Offline Gates 1–7: All 7 gates evaluated in sequence | Integration | R-002 | Synthetic strategy fails Gate 2 (PBO>0.75) → assert gate 3–7 not evaluated; promotion blocked |

#### Live Gates

| Test ID | Requirement | Test Level | Risk Link | Notes |
|---------|-------------|------------|-----------|-------|
| **P0-LIVE-001** | FR-LIVE-001: Live Gate A — all 9 CORE metrics validated per profile | Integration | R-002 | CORE strategy: avg_trade_interval=6h (FAIL, >4h) → assert promotion blocked |
| **P0-LIVE-002** | FR-LIVE-002: Live Gate B — day-7 calibration pass/warning/fail determination | Integration | R-002 | Simulate 7-day micro-live; inject slippage +55% (FAIL) → assert FAIL outcome |

#### Calendar Safety

| Test ID | Requirement | Test Level | Risk Link | Notes |
|---------|-------------|------------|-----------|-------|
| **P0-CAL-001** | FR0.10-HARD: All entries blocked in HARD event window | Integration | R-008 | FakeClock in window; assert allow_long=False, allow_short=False for affected pairs |
| **P0-CAL-002** | FR0.11-HARD: Pair-specific filtering — UK CPI only blocks GBPUSD, not AUDUSD | Unit | R-008 | UK CPI event → assert AUDUSD unaffected |
| **P0-CAL-003** | FR0.12-HARD: Calendar Safety cannot be disabled (except debug flag) | Unit | R-008 | Assert CalendarSafety.disabled raises error without debug flag |
| **P0-CAL-004** | FR0.14-HARD: risk_flags.json artifact generated per run | Integration | R-011 | Run with 1 FOMC event → assert risk_flags.json matches schema spec |

#### Rocket Portfolio — Critical Kill Switches

| Test ID | Requirement | Test Level | Risk Link | Notes |
|---------|-------------|------------|-----------|-------|
| **P0-ROCKET-001** | FR-RISK-005: Circuit breaker triggers within 60s of 6+ simultaneous deaths | Integration | R-006 | FakeRocketRegistry: inject 6 deaths → assert circuit_breaker=True within 1 polling cycle |
| **P0-ROCKET-002** | FR78: Rocket kill switch — DD > 15% → immediate kill | Unit | - | Assert rocket killed; capital transferred to Tier 2 |
| **P0-ROCKET-003** | FR-RISK-004: Wilson Score safety gate — N<50 → skip kill switch | Unit | R-021 | N=5 trades, win_rate=40% → assert kill NOT triggered |
| **P0-ROCKET-004** | FR-RISK-004: Wilson Score N≥50 — LCB < 30% → kill | Unit | - | N=50, win_rate=40% → LCB=26.8% → assert kill triggered |
| **P0-ROCKET-005** | FR72: Rocket bucket hard cap ≤10% NAV | Unit | - | Total rockets at 11% → assert auto-adjustment to 10% |

#### CLI & Rollback

| Test ID | Requirement | Test Level | Risk Link | Notes |
|---------|-------------|------------|-----------|-------|
| **P0-CLI-001** | FR0.1: CLI autonomy loop commands produce run_id and artifacts | Integration | R-011 | `katana backtest` → assert run_id in output, artifacts in runs/ |
| **P0-CLI-002** | FR0.2: Reproducible artifacts — same inputs → same run_id, config_hash, data_hash | Integration | R-003 | Run twice with same config → assert all hashes identical |
| **P0-OPS-001** | Rollback: time-to-rollback ≤ 5 minutes | Performance | R-010 | Time `katana rollback --to last-champion`; assert elapsed < 300s |

**Total P0: ~52 tests**

---

### P1 (High) — ~68 Tests

**Criteria:** Important features + Medium risk (3–5) + Common workflows + Workaround exists but difficult

#### Signal Framework — AUX & Integration

| Test ID | Requirement | Test Level | Risk Link | Notes |
|---------|-------------|------------|-----------|-------|
| **P1-SIG-001** | FR-SIG-AUX-001: volume_surge, rsi_recovery, divergence conditions | Unit | - | Each AUX condition; assert confidence boost when present |
| **P1-SIG-002** | FR-SIG-ENTRY-EXIT-001: Entry window enforcement (first 10 min of h1 bar) | Unit | - | FakeClock at 14:15 (outside window) → assert no entry |
| **P1-SIG-003** | FR-SIG-ENTRY-EXIT-001: SL formula — max(1.5×ATR14, MA20 ± buffer) | Unit | - | Known OHLCV fixture; assert exact SL price calculation |
| **P1-SIG-004** | FR-SIG-ENTRY-EXIT-001: TP1=1.0×ATR14, TP2=2.0×ATR14, trailing at 0.8×ATR14 | Unit | - | Assert TP1, TP2 prices; trailing activation after TP1 hit |

#### Price Action Module

| Test ID | Requirement | Test Level | Risk Link | Notes |
|---------|-------------|------------|-----------|-------|
| **P1-PA-001** | FR-PA-001: PA module skipped when enable_pa_filter=False | Unit | - | Assert 0ms overhead (no PA code executed) |
| **P1-PA-002** | FR-PA-002: ≥8 base patterns — each passes deterministic textbook examples | Unit | - | Textbook pinbar/engulfing/inside_bar/hammer/etc. OHLCV |
| **P1-PA-003** | FR-PA-003: pa_max_patterns ≤ 2 — 3+ patterns → TrialPruned | Integration | - | Trial with 3 PA patterns → assert TrialPruned immediately |
| **P1-PA-004** | FR-PA-004: pa_confidence_min threshold filtering | Unit | - | conf=0.45 (below 0.60 default) → assert pattern filtered |
| **P1-PA-005** | FR-PA-005: pa_patterns.json artifact per run | Integration | R-011 | Run with PA enabled → assert pa_patterns.json exists, schema valid |

#### Optimization Pipeline — Extended

| Test ID | Requirement | Test Level | Risk Link | Notes |
|---------|-------------|------------|-----------|-------|
| **P1-OPT-001** | FR-OPT-002: Hierarchical L2→L1 optimization — 3 rounds + convergence | Integration | - | Assert L1 receives L2 results; 3 rounds complete; stop when Sharpe improvement <1% |
| **P1-OPT-002** | FR-OPT-003: CLI filtering — --exchange/--pair/--timeframe/--optimization-level | Unit | - | Filter matrix; assert only matching configs executed |
| **P1-OPT-003** | FR-OPT-008: 4 risk mode presets — parameters overridden correctly | Unit | - | rocket_catching preset: SL=5%, TP=50%, leverage=5x, pyramid=True |
| **P1-OPT-004** | FR-OPT-009: 3–10 uncorrelated instances — pairwise correlation <0.50 for ≥80% pairs | Integration | - | 5 Sobol-sampled instances; assert correlation matrix |
| **P1-OPT-005** | FR-OPT-013: Checkpoint + resume — crash at trial N → resume from N+1 | Integration | R-018 | Simulate crash; restart; assert trial N+1 continues, no duplicate |
| **P1-OPT-006** | FR-OPT-005: Early stopping — convergence at std(last_20) < 0.01 | Unit | - | Mock sampler with converging objectives; assert early stop triggered |
| **P1-OPT-007** | FR-OPT-006: Walk-Forward median OOS Sharpe used (not IS) | Unit | R-004 | Assert objective function uses OOS fold scores, not IS raw Sharpe |
| **P1-OPT-008** | FR-OPT-011: 64 signal combinations (2^6 feature toggles) | Unit | - | All combinations generated; assert disabled indicators not evaluated |
| **P1-OPT-009** | FR-OPT-012: Adaptive entry frequency targeting — convergence within 10 iterations | Integration | - | target=10 trades/day, initial=5; assert convergence in ≤10 iterations |
| **P1-OPT-010** | FR-OPT-004: Optimization results dashboard — loads in <5 min for 8,000 trials | Performance | R-012 | Time dashboard generation; assert <300 seconds |

#### Wave 4 — Multi-Timeframe & DFF

| Test ID | Requirement | Test Level | Risk Link | Notes |
|---------|-------------|------------|-----------|-------|
| **P1-WAVE4-001** | FR-W4-TF01 through TF06: Independent study per TF — 0% parameter bleed | Integration | R-015 | Run 1m optimization; assert no 1m params appear in 5m study |
| **P1-WAVE4-002** | FR-W4-CACHE: ensure_up_to_date() — incremental download only | Integration | - | Pre-loaded cache; add 10 bars; assert only 10 new bars fetched |
| **P1-WAVE4-003** | FR-W4-CACHE: load() latency <100ms from PostgreSQL | Performance | - | Measure read latency for 1-year 1h dataset; assert <100ms |
| **P1-WAVE4-004** | FR-W4-DFF01: All 10 dist_* columns populated, 0% NaN after prepare_features() | Unit | R-007 | Property-based: random OHLCV slices → assert NaN count = 0 for all dist_* |
| **P1-WAVE4-005** | FR-W4-DFF02: Multiplier constraint tp1_distance_mult > sl_distance_mult * 1.2 | Unit | - | Violating trial → TrialPruned |
| **P1-WAVE4-006** | FR-W4-DFF03: Backward compatibility — default atr_14 = legacy SL/TP prices | Regression | R-007 | 100 trades: DFF default vs legacy code; assert 100% match |
| **P1-WAVE4-007** | FR-W4-CAL01: FOMC HARD block — positions closed 30min before event | Integration | R-008 | FakeClock at T-35min; assert positions force-closed; no new entries |
| **P1-WAVE4-008** | FR-W4-CAL02: SOFT mode — 0.5x sizing during MEDIUM impact event | Integration | - | FakeClock in MEDIUM event window; assert position size = 0.5× normal |

#### MTF Confirmation

| Test ID | Requirement | Test Level | Risk Link | Notes |
|---------|-------------|------------|-----------|-------|
| **P1-MTF-001** | MTF Confirmation kill-switch — mtf_delta_DSR_vs_none < 0 → auto-rollback | Unit | R-013 | Inject negative delta; assert rollback to "soft_penalty" or "none" |
| **P1-MTF-002** | mtf_block_rate telemetry — % blocked signals tracked per run | Integration | - | Assert mtf_block_rate in signal_quality.json |
| **P1-MTF-003** | FR55: Timeframe ratio validation — 4:1 to 6:1 enforced | Unit | - | 1m + 10m combo (10:1 ratio) → assert validation error |

#### Risk Management Suite

| Test ID | Requirement | Test Level | Risk Link | Notes |
|---------|-------------|------------|-----------|-------|
| **P1-RISK-001** | FR62: Kelly eligibility gate — blocked when N<100 or PSR_live<0.85 | Unit | R-019 | N=80, PSR=0.90 → assert Kelly disabled; N=120, PSR=0.88 → assert Kelly enabled |
| **P1-RISK-002** | FR47: Dual-stop logic — PASSIVE (warning only) vs HARD (halt + exit) | Integration | - | DD=26% → assert HARD stop; P(SR<0.5)>0.7 for 7d → assert PASSIVE warning |
| **P1-RISK-003** | FR98: VaR calculation — 5 methods (historical, parametric, Cornish-Fisher, EWMA, modified) | Unit | - | Known returns distribution; assert VaR values within tolerance |
| **P1-RISK-004** | FR100: Historical stress tests — 8 crisis scenarios | Integration | - | Each scenario produces valid output; Sharpe degradation measured |
| **P1-RISK-005** | FR-OPT-014: HMM regime classification — 4 regimes assigned to historical periods | Unit | - | Synthetic 4-regime data; assert HMM classifier ≥80% accuracy |

#### Rocket Portfolio — Extended

| Test ID | Requirement | Test Level | Risk Link | Notes |
|---------|-------------|------------|-----------|-------|
| **P1-ROCKET-001** | FR67: Monte Carlo 10,000+ simulations in <60s | Performance | - | Assert elapsed time <60s; output statistics match expected distributions |
| **P1-ROCKET-002** | FR-VALIDATION-MC: All 4 criteria pass before deployment | Integration | - | Inject mean_return=8% (< 10% threshold) → assert DO NOT DEPLOY |
| **P1-ROCKET-003** | FR76: State machine transitions — GREEN/YELLOW/RED/BLACK with hysteresis (3 days) | Unit | - | Inject core DD=12% for 3 days → assert YELLOW transition; 2 days → assert no transition |
| **P1-ROCKET-004** | FR79: Rocket kill switch — age>7 days + negative P&L | Unit | - | FakeClock advance 8 days, P&L=-5% → assert rocket killed |
| **P1-ROCKET-005** | FR82: All 3 circuit breaker triggers validated | Unit | R-006 | Trigger 1: 6 deaths, Trigger 2: median corr >0.80, Trigger 3: order book <50% |
| **P1-ROCKET-006** | FR75: Profit transfer — 20% stays in bucket, 80% to core | Unit | - | Rocket gains $1,000 → assert $200 retained, $800 transferred to core |

#### Dashboard (Phase 1 MVP)

| Test ID | Requirement | Test Level | Risk Link | Notes |
|---------|-------------|------------|-----------|-------|
| **P1-DASH-001** | FR1-FR8: Dashboard generation from backtest_summary.json | Integration | - | Load fixture JSON; assert HTML output includes Net P&L, Profit Factor, equity curve |
| **P1-DASH-002** | FR0.2a: schema_version parsing — v1.0 artifact shows fallback warning | Unit | R-014 | v1.0 artifact → assert UI warning "Upgrade for full visibility" in HTML |
| **P1-DASH-003** | FR8: Dashboard data export in 3 formats (HTML + optional PDF/PNG) | Unit | - | Assert HTML export valid; PDF/PNG snapshot generation |
| **P1-DASH-004** | FR7: Parameter comparison — 2–5 runs side-by-side | Integration | - | Load 3 fixture JSONs; assert diff highlighting in HTML output |

#### Data Management

| Test ID | Requirement | Test Level | Risk Link | Notes |
|---------|-------------|------------|-----------|-------|
| **P1-DATA-001** | FR36: OHLCV data loading from ≥2 sources (file-based + external) | Unit | - | Both sources load identical data; assert equal DataFrames |
| **P1-DATA-002** | FR37: Data caching — second load from cache | Unit | - | Time first load vs second; assert cache hit >10x faster |
| **P1-DATA-003** | FR42: Turnover cap ≤30%/day enforced | Unit | - | Strategy exceeds 30% → assert turnover_capped logged |
| **P1-DATA-004** | FR43: Degradation triggers — corr<0.5 for 7d → re-optimize policy | Integration | - | Inject 7 days of low correlation; assert re-optimize triggered |
| **P1-DATA-005** | FR-OPT-014: Adaptive portfolio rebalancing on regime change | Integration | - | Regime shift detected → assert rebalancing triggered |

**Total P1: ~68 tests**

---

### P2 (Medium) — ~38 Tests

**Criteria:** Secondary features + Low risk (1–2) + Edge cases + Regression prevention

| Test ID | Requirement | Test Level | Notes |
|---------|-------------|------------|-------|
| **P2-SIG-001** | MACD histogram near-zero block (hist < 0.0001) | Unit | Boundary value test |
| **P2-SIG-002** | Fractal zone detection with 20-bar lookback | Unit | Edge: fewer than 20 bars available |
| **P2-SIG-003** | Upper wick degradation — wick > 0.7×ATR14 triggers Rule 4 | Unit | Boundary: wick exactly 0.7×ATR |
| **P2-SIG-004** | Abnormal volatility rule — ATR_ratio at boundaries 0.6 and 1.6 | Unit | Boundary value: exactly at edge |
| **P2-SIG-005** | Timeout exit — position > 2×h1_timeframe | Unit | FakeClock: position at exactly 2h → assert force-close |
| **P2-OPT-001** | QMC sampler seed consistency — same seed → same trial order | Unit | Property-based |
| **P2-OPT-002** | PBO calculation correctness — known combinatorial baseline | Unit | Compare against scipy reference |
| **P2-OPT-003** | DSR formula — accounts for multiple testing (n_trials parameter) | Unit | Known input → known DSR output |
| **P2-OPT-004** | Walk-Forward 5-window split — correct IS/OOS date ranges | Unit | Assert split dates match specification |
| **P2-OPT-005** | Complexity score penalty calculation — penalty=0.15×(complexity-1) | Unit | complexity=3 → penalty=0.30 |
| **P2-OPT-006** | FR-OPT-009: Sobol sampling ±10% variance | Unit | Assert instances within ±10% range of base config |
| **P2-OPT-007** | FR-OPT-010: Portfolio weight constraints — Σw=1.0, min=0.05, max=0.50 | Unit | scipy optimizer; assert all constraints satisfied |
| **P2-GATE-001** | Bootstrap CI lower bound > 0 (Ljung-Box test, p > 0.05) | Unit | Autocorrelation check |
| **P2-GATE-002** | PSR formula — known Sharpe + N_trades → known PSR | Unit | Compare against statistical reference |
| **P2-CAL-001** | Event calendar loaded at process start — no network calls during backtest | Unit | Mock network; assert 0 network calls during optimization |
| **P2-CAL-002** | news_overlay_enabled=False → SOFT overlay not applied | Unit | Assert position sizing unchanged during SOFT event |
| **P2-DFF-001** | Mixed-source DFF — SL=stddev_20, TP=atr_14 work together | Unit | Assert correct column used per role |
| **P2-DFF-002** | DFF precompute performance — <5% overhead in prepare_features() | Performance | Baseline without DFF vs with DFF |
| **P2-ROCKET-001** | FR66: N_min calculation for positive expected value | Unit | 60% failure, 150% avg gain → N_min=6 |
| **P2-ROCKET-002** | FR73: Tier 1 cap per individual rocket — max=60% of bucket | Unit | Assert max_allocation_per_rocket = 0.60 × rocket_bucket_total |
| **P2-ROCKET-003** | FR77: Hysteresis — 3 consecutive days required for state transition | Unit | 2 days YELLOW trigger → assert still GREEN |
| **P2-ROCKET-004** | FR89: Deployment queue — auto-redeploy when rocket dies | Integration | Rocket killed → assert next in queue deployed |
| **P2-RISK-001** | FR45a: Micro-Live → Scaled-Live gate — N_live_trades ≥ 30, live_days ≥ 14 | Unit | N=25 → assert promotion blocked |
| **P2-RISK-002** | FR45b: PSR_live ≥ 0.85 gate | Unit | PSR_live=0.82 → assert promotion blocked |
| **P2-RISK-003** | FR49: Paper vs live synchronization | Integration | Assert paper and live equity curves within 10% deviation |
| **P2-DATA-001** | Cross-platform data_hash consistency (Windows + Linux) | Integration | Assert same SHA256 on both platforms |
| **P2-DATA-002** | data_hash mismatch → optimization blocked | Unit | Modified dataset vs original hash → assert error |
| **P2-DASH-001** | FR6: Walk-forward validation window visualization in HTML | Unit | Assert WF window data present in generated HTML |
| **P2-DASH-002** | FR5: Equity curve zoom/pan controls in HTML | Unit | Assert Plotly interactive controls present |
| **P2-DASH-003** | FR9: Smoke test results display | Integration | Load smoke_test_results fixture → assert display in HTML |
| **P2-DASH-004** | FR12: IS/OOS comparison visualization | Unit | Assert IS and OOS equity curves both present |
| **P2-CLI-001** | FR0.3: CLI composable DAG — each step runs independently | Integration | Run backtest step alone; assert no dependency on optimize step |
| **P2-CLI-002** | FR0.2: run_id format consistent across runs | Unit | Assert run_id matches expected format (e.g., ISO timestamp + hash) |
| **P2-OPS-001** | Registry snapshot before schema migration | Unit | Assert snapshot file created; restore test passes |
| **P2-OPS-002** | Strategy lifecycle transitions — CANDIDATE → PAPER → MICRO_LIVE → SCALED_LIVE | Integration | Valid transitions allowed; invalid transitions blocked |
| **P2-OPS-003** | Degradation trigger — DD breach → re-optimize/retire policy logged to Run Journal | Integration | Inject DD breach; assert Run Journal entry |
| **P2-OPS-004** | FR-OPT-012: Adaptive entry frequency — convergence |/current-target| < 1.0 | Integration | Verify convergence criterion |

**Total P2: ~38 tests**

---

### P3 (Low) — ~22 Tests

**Criteria:** Performance benchmarks + Monte Carlo validation + Exploratory + Documentation validation

| Test ID | Requirement | Test Level | Notes |
|---------|-------------|------------|-------|
| **P3-PERF-001** | 8,000 total trials ≤ 1 day on 8–10 workers (throughput benchmark) | Performance | Subset: 200 trials as CI proxy; full 8,000 weekly |
| **P3-PERF-002** | Dashboard load <5 min for 8,000-trial result set | Performance | Time full dashboard generation |
| **P3-PERF-003** | Memory profile — 2–4GB per worker × 8 workers ≤ 32GB RAM | Performance | Memory profiler during 100-trial optimization |
| **P3-PERF-004** | Backtest speed — ~5,000 backtests/min (10 cores) | Performance | Time 100 sequential backtests; scale estimate |
| **P3-PERF-005** | OHLCV cache warm-up — all 6 TF tables populated <10 min | Performance | Time `sync_ohlcv --all-timeframes` on synthetic dataset |
| **P3-PERF-006** | Divergence AUX condition (O(n²)) — disabled→0ms, enabled→<30s on 10K bars | Performance | Verify expensive computation bounded |
| **P3-MC-001** | FR-VALIDATION-MC: 10,000 Monte Carlo simulations in <60s | Performance | Time simulation run; assert statistics distribution correct |
| **P3-MC-002** | FR67: Monte Carlo output statistics — VaR5% > -20%, prob_loss < 30% | Exploratory | Known parameter set → assert output matches expected distribution |
| **P3-MC-003** | FR94a: All 4 Monte Carlo acceptance criteria pass on reference portfolio | Validation | Pre-validated reference portfolio → assert all 4 criteria met |
| **P3-STRESS-001** | FR100: Historical stress test — 2008 crisis scenario | Exploratory | Assert strategy survives; MaxDD reported |
| **P3-STRESS-002** | FR100: COVID-2020 crash scenario | Exploratory | Assert strategy survives; Sharpe degradation measured |
| **P3-STRESS-003** | FR100: 2022 crypto winter scenario | Exploratory | Assert strategy survives |
| **P3-DOCS-001** | HTML dashboard renders correctly in Chrome/Firefox/Edge | Manual | Visual inspection of generated HTML |
| **P3-DOCS-002** | CLI help text accurate and up-to-date for all 12 commands | Manual | `katana --help` vs PRD FR0.1 command list |
| **P3-DOCS-003** | data contract examples in PRD match actual artifact schemas | Manual | Diff PRD examples against generated artifacts |
| **P3-EXP-001** | Exploratory: filter cascade scenarios (4 combinations) produce expected entry decisions | Exploratory | Scenario 1–4 from PRD Filter Cascade section |
| **P3-EXP-002** | Exploratory: Strategy Registry state machine — all valid lifecycle transitions | Exploratory | 6-state machine; exhaustive valid transition test |
| **P3-EXP-003** | Exploratory: Expert Council decision output schema | Exploratory | Assert FR85 output schema (profit transfers, rebalance, allocation) |
| **P3-EXP-004** | Exploratory: Sobol QMC low-discrepancy property | Unit | Assert coverage uniformity metric for 32 initial trials |
| **P3-EXP-005** | Exploratory: Rocket bucket GREEN/YELLOW/RED/BLACK state visualization | Manual | Dashboard shows correct color-coded state indicator |
| **P3-EXP-006** | Exploratory: MTF shadow P&L tracking (blocked signals in shadow-sim) | Integration | Assert mtf_shadow_pnl_blocked calculated when mode != "none" |
| **P3-EXP-007** | Exploratory: HMM regime detection on 3+ years historical data | Exploratory | Assert ≥4 distinct regimes identified |

**Total P3: ~22 tests**

---

## Execution Strategy

**Philosophy:** Run lightweight tests in every PR. Defer expensive infrastructure tests to nightly/weekly. Parallelize with pytest-xdist.

### Every PR: Unit + Integration Tests (~10–15 min)

- All P0 unit tests + P0 integration tests (using in-memory Optuna, FakeClock, frozen fixtures)
- All P1 unit tests
- Selected P2 tests (boundary conditions, regression prevention)
- **Parallelization**: `pytest -n 4` (4 workers, isolated in-memory state per worker)
- **Total PR tests**: ~90 tests (~10–15 min)
- **Tags**: `@pytest.mark.unit`, `@pytest.mark.integration`

```bash
# Every PR
pytest tests/ -m "unit or integration" --n-workers 1 -n 4 -x --timeout=60
```

### Nightly: Performance + Monte Carlo (~30–60 min)

- All P3 performance benchmarks (throughput, memory, latency)
- Monte Carlo 10,000 simulations (P3-MC-001 through P3-MC-003)
- Historical stress tests (P3-STRESS-001 through P3-STRESS-003)
- Full optimization integration tests with --n-workers 4
- **Total nightly tests**: ~35 tests (~30–60 min)
- **Tags**: `@pytest.mark.performance`, `@pytest.mark.monte_carlo`

```bash
# Nightly
pytest tests/ -m "performance or monte_carlo or stress" -n 4 --timeout=3600
```

### Weekly: Full Wave 4 + Regression (~2–4 hours)

- Full Wave 4 per-TF integration tests (requires PostgreSQL)
- 200-trial optimization smoke test (proxy for 8,000-trial benchmark)
- Full regression suite including all 350+ existing passing tests
- Manual tests: Dashboard visual inspection, CLI help validation, artifact schema review
- **Tags**: `@pytest.mark.wave4`, `@pytest.mark.requires_postgres`, `@pytest.mark.regression`

```bash
# Weekly
pytest tests/ -m "wave4 or regression" -n 4 --timeout=7200
```

### Manual Tests (Not Automated)

- Dashboard visual inspection in Chrome/Firefox/Edge
- CLI help text accuracy review
- Live paper trading validation (operator responsibility)
- Rollback procedure walkthrough
- Expert Council output review

---

## QA Effort Estimate

**QA/Dev test development effort** (for new tests beyond existing 350+ suite):

| Priority | Count | Effort Range | Notes |
|----------|-------|--------------|-------|
| P0 | ~52 | ~3–4 weeks | Complex setup: FakeClock, Optuna isolation, artifact validation, circuit breaker timing |
| P1 | ~68 | ~3–4 weeks | Standard integration: optimization pipeline, Wave 4, dashboard |
| P2 | ~38 | ~1–2 weeks | Edge cases, boundary conditions, regression |
| P3 | ~22 | ~1 week | Performance benchmarks, exploratory |
| **Total** | **~180** | **~8–11 weeks** | **1 dev/QA engineer, part-time (alongside implementation)** |

**Assumptions:**
- Includes test design, implementation, debugging, CI integration
- Existing 350+ tests maintained by Dev team (not counted here)
- B-001 through B-005 blockers resolved by Dev team before integration test development starts
- Deterministic OHLCV fixtures and test infrastructure (~1 week setup) included in P0 estimate

---

## Implementation Planning Handoff

Tasks for Dev team to unblock QA:

| Work Item | Owner | Target Sprint | Dependencies/Notes |
|-----------|-------|---------------|-------------------|
| B-001: Deterministic seed contract | Dev | Sprint 1 Epic J | All optimization + Monte Carlo tests blocked |
| B-002: ClockProtocol abstraction | Dev | Sprint 1 Epic J | All Calendar Safety tests blocked |
| B-003: Optuna in-memory study fixture | Dev | Sprint 1 Epic J | All optimization integration tests blocked |
| B-004: schema_version in all artifacts | Dev/Architect | Sprint 1 Epic J | Backward compat tests blocked |
| B-005: --n-workers 1 CLI flag | Dev | Sprint 1 Epic J | CI optimization tests OOM without this |
| Frozen OHLCV test fixtures (6 TFs) | Dev | Sprint 1 Epic J | Wave 4 tests blocked |
| FakeRocketRegistry test stub | Dev | Wave 4 Sprint | Circuit breaker tests blocked |
| ArtifactRegistry.validate_schema() | Dev | Sprint 2 Epic J | Artifact schema tests need this |

---

## Tooling & Access

| Tool or Service | Purpose | Access Required | Status |
|-----------------|---------|-----------------|--------|
| pytest + pytest-xdist | Parallel test execution | Already installed | Ready |
| hypothesis | Property-based testing (NaN, invariant) | `pip install hypothesis` | Ready |
| pytest-mock | FakeClock, network mocking | Already installed | Ready |
| PostgreSQL (test container) | Wave 4 per-TF caching tests | Docker in CI | Pending |
| numpy.testing, pandas.testing | Numeric assertions | Already available | Ready |
| vectorbt Pro test fixtures | Backtesting test harness | License required | Ready (license active) |
| Optuna 3.x in-memory backend | Study isolation in CI | Already available | Ready |

**Access requests needed:**
- [ ] PostgreSQL test container in CI (GitHub Actions / Docker Compose)
- [ ] Wave 4 PostgreSQL schema DDL from Dev team for test fixture setup

---

## Interworking & Regression

| Service/Component | Impact | Regression Scope | Validation Steps |
|-------------------|--------|------------------|-----------------|
| **KatanaTransformer** | Core entry/exit/beacon logic | All 5 CORE + 3 AUX conditions; degradation rules | Run existing signal generation test suite; assert 0 regressions |
| **Optuna Study Engine** | Optimization pipeline | Existing optimizer tests (FR-OPT-001 through FR-OPT-006) | Run existing optimization unit tests; assert trial count unchanged |
| **Calendar Safety Module** | Risk management | Existing calendar safety tests (FR0.9 through FR0.14) | Run existing HARD-mode tests; assert pair filtering unchanged |
| **Rocket Portfolio Engine** | Capital management | Kill switches (FR78–FR84), state machine (FR76–FR77) | Run existing rocket unit tests; assert kill switch thresholds unchanged |
| **Walk-Forward / CSCV** | Anti-overfitting | Existing WF/CSCV/PBO/DSR tests (Phase 3 suite) | Run `pytest tests/quant/` suite; assert 0 regressions |
| **Risk Suite (VaR/CVaR)** | Risk management | Existing tail risk tests (57 passing) | `pytest tests/risk/tail_risk`; assert all 57 pass |
| **Sizing Engine** | Position sizing | Existing sizing engine tests (67 passing) | `pytest tests/risk/sizing_engine`; assert all 67 pass |
| **HTML Dashboard Generator** | Reporting | FR1–FR8 (Phase 1 MVP stories 1.1–1.5) | Validate HTML output against all acceptance criteria |

**Regression test strategy:**
- Before every release: run full 350+ existing test suite; any regression is a P0 blocker.
- Before Wave 4 deployment: run per-TF isolation tests (P1-WAVE4-001) to confirm no parameter bleed.
- After DFF changes: run FR-W4-DFF03 backward compatibility test (100-trade comparison against legacy code).

---

## Appendix A: Pytest Patterns for This Project

**Deterministic OHLCV fixture pattern:**
```python
@pytest.fixture(scope="session")
def ohlcv_1h_fixture():
    """Frozen 1h OHLCV fixture (SHA256: abc123...). Loads in <10ms."""
    df = pd.read_parquet("tests/fixtures/ohlcv/btcusdt_1h_1000bars.parquet")
    assert len(df) == 1000  # contract: exactly 1000 bars
    return df

def test_katana_transformer_signals(ohlcv_1h_fixture):
    config = KatanaConfig(seed=42, strategy_profile="return")
    transformer = KatanaTransformer(config, clock=FakeClock(datetime(2024, 3, 15, 14, 0)))
    signals = transformer.generate_signals(ohlcv_1h_fixture)
    assert signals["ma_cross_confirm"].sum() > 0
    assert signals["beacon_level"].isin(["mini", "mayak", "working", "kotleta"]).all()
```

**Calendar Safety test pattern:**
```python
def test_calendar_safety_hard_blocks_fomc(ohlcv_1h_fixture):
    fomc_event = EconomicEvent(
        datetime_utc=datetime(2024, 3, 20, 18, 0),  # 18:00 UTC
        event_name="FOMC Rate Decision",
        impact_level="HIGH",
        affected_pairs=["EURUSD", "GBPUSD"]
    )
    clock = FakeClock(datetime(2024, 3, 20, 16, 30))  # T-90min (inside 120min pre-buffer)
    safety = CalendarSafety(events=[fomc_event], clock=clock)
    result = safety.check_entry("EURUSD", clock.now())
    assert result.allow_long == False
    assert result.allow_short == False
    assert result.reason == "calendar_safety_hard_block"
    # Pair-specific: AUDUSD not affected by FOMC
    result_aud = safety.check_entry("AUDUSD", clock.now())
    assert result_aud.allow_long == True
```

**Optimization invariant test pattern:**
```python
from hypothesis import given, settings
from hypothesis import strategies as st

@given(st.integers(min_value=0, max_value=1000000))
@settings(max_examples=10000)
def test_active_param_count_invariant(seed):
    """Property-based: active_param_count MUST be ≤ 70 for any random seed."""
    sampler = ParameterProfileSampler(seed=seed, profile="rocket")
    params = sampler.suggest()
    active_count = sum(1 for p in params.values() if p is not None)
    assert active_count <= 70, f"Invariant violated: {active_count} active params with seed={seed}"
```

**Tags for selective CI execution:**
```bash
# Critical path only (PR gate, <5 min)
pytest tests/ -m "unit and not slow" --timeout=30

# Full integration (pre-merge, ~15 min)
pytest tests/ -m "unit or integration" -n 4 --timeout=60

# Nightly performance
pytest tests/ -m "performance" --timeout=3600

# Wave 4 (weekly, requires PostgreSQL)
pytest tests/ -m "wave4" --timeout=7200
```

---

## Appendix B: Knowledge Base References

- **Risk Governance**: `_bmad/tea/testarch/knowledge/adr-quality-readiness-checklist.md` — Risk scoring methodology
- **API Testing Patterns**: `_bmad/tea/testarch/knowledge/api-testing-patterns.md` — CLI-based integration test patterns
- **Test Levels Framework**: Unit vs Integration vs E2E selection for Python CLI projects
- **PRD Source of Truth**: `katana-v-02-prd-katana-vectorbt-2026-01-18.md` — All acceptance criteria

---

**Generated by:** TEA Agent (BMAD testarch-test-design workflow v5.0)
**Mode:** System-Level (Phase 3)
**Workflow:** `_bmad/tea/workflows/testarch/test-design`
**Date:** 2026-02-26
