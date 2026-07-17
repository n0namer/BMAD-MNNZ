---
agent: testarch-automate
zone: 3
phase: prep
generatedDate: '2026-02-26'
status: PREP_COMPLETE
type: coverage-plan
totalTests: 180
automatedTarget: 155
manualTarget: 25
automationCoverageTarget: 86
actualAutomatedEstimate: 155
---

# Test Automation Coverage Plan: katana-vectorbt

**Agent:** Agent-6 (testarch-automate), Zone 3 Prep Phase
**Date:** 2026-02-26
**Source:** zone1/test-design-qa.md (180 tests defined), zone1/test-design-architecture.md (28 risks)
**Target:** 85%+ automation coverage (155/180 tests automated)
**Framework:** pytest 7.0+ (primary), hypothesis (property-based), BeautifulSoup (dashboard)

---

## Coverage Philosophy

The automation decision for each test follows this priority tree:

1. **Automate first:** If the test can be expressed as deterministic input → expected output, automate it.
2. **Property-based when boundary-critical:** When a rule must hold across all possible inputs (not just examples), use hypothesis.
3. **CLI subprocess for end-to-end:** When validating the CLI autonomy loop produces correct artifacts, use subprocess invocation with artifact assertions.
4. **Semi-automate performance tests:** Timing assertions are automated; threshold review is manual.
5. **Manual only when visual or subjective:** Browser rendering, CLI help text readability, PRD documentation diff.

---

## P0 Tests: Automation Coverage (52 tests → 50 automated, 2 manual)

**P0 automation rate: 96%**

### Signal Framework (11 tests → 11 automated)

| Test ID | Test Name | Automation Method | Blocker | Rationale |
|---------|-----------|-------------------|---------|-----------|
| P0-SIG-001 | CORE conditions on synthetic OHLCV | pytest unit | None | Pure function: OHLCV in → boolean per condition out |
| P0-SIG-002 | ma_cross_confirm LONG/SHORT logic | pytest unit | None | Deterministic MA crossover logic; synthetic fixture |
| P0-SIG-003 | macd_impulse BLOCK condition | pytest unit | None | Boundary value test: hist ≈ 0.0001 |
| P0-SIG-004 | mtf_trend h1-h4 alignment | pytest unit | None | Synthetic h1+h4 fixture; directional assert |
| P0-SIG-005 | Rule 1 (MACD) absolute priority | pytest unit | None | Single input variant; Rule 1 → MINI always |
| P0-SIG-006 | All 5 degradation rules independently | hypothesis | None | Property-based: each rule fires independently |
| P0-SIG-007 | Confidence formula 0.8*core + 0.2*aux | pytest unit | None | Known formula; assert against Python calculation |
| P0-SIG-008 | Beacon level mapping (all 4 levels) | pytest parametrize | None | 4 parametrize cases; one per beacon level |
| P0-SIG-009 | signal_quality.json artifact per run | pytest integration | B-001 | CLI invocation; artifact schema assertion |
| P0-SIG-010 | Monday 00:00-06:00 UTC exclusion | pytest unit | None | FakeClock (pre-built); no-entry assertion |
| P0-SIG-011 | Calendar Safety HARD blocks in window | pytest integration | B-002 | FakeClock at T-100min; FOMC fixture |

### Data Integrity (5 tests → 5 automated)

| Test ID | Test Name | Automation Method | Blocker | Rationale |
|---------|-----------|-------------------|---------|-----------|
| P0-DATA-001 | No data leakage in feature generation | pytest integration | None | Leakage detector: assert no row N references row N+k |
| P0-DATA-002 | Same data_hash → identical results | pytest integration | B-001 | Run twice; assert all metric values identical |
| P0-DATA-003 | Walk-Forward purge + embargo no overlap | pytest unit | None | Assert IS/OOS date range separation |
| P0-DATA-004 | Data quality validation catches gaps+spikes | pytest unit | None | Synthetic dataset with 2% gaps + spike |
| P0-DATA-005 | data_hash in Run Journal + integrity check | pytest integration | B-001 | Modify artifact post-generation; assert error raised |

### Optimization Pipeline (7 tests → 7 automated)

| Test ID | Test Name | Automation Method | Blocker | Rationale |
|---------|-----------|-------------------|---------|-----------|
| P0-OPT-001 | DSR-adjusted Sharpe mandatory objective | pytest unit | None | Mock objective function; assert DSR called |
| P0-OPT-002 | PBO < 0.50 quality gate enforced | pytest integration | B-003 | Inject PBO=0.60 result; assert gate blocks |
| P0-OPT-003 | active_param_count <= 70 (10,000 profiles) | hypothesis | None | Property-based: 10,000 random profiles |
| P0-OPT-004 | Conditional search space constraints | pytest unit | None | Assert ma_slow > ma_fast+5 always |
| P0-OPT-005 | QMC (32) then TPE transition | pytest integration | B-003 | Mock sampler; assert sampler switch at trial 32 |
| P0-OPT-006 | Complexity budget > 4 blocks → TrialPruned | pytest unit | None | 5-block trial returns TrialPruned immediately |
| P0-OPT-007 | Immutable artifacts on every run | pytest integration | B-001 | 10 trials; assert all artifacts present in runs/ |

### Offline Quality Gates (4 tests → 4 automated)

| Test ID | Test Name | Automation Method | Blocker | Rationale |
|---------|-----------|-------------------|---------|-----------|
| P0-GATE-001 | PSR >= thresholds by profile | pytest parametrize | None | 3 profiles × threshold; parametrize |
| P0-GATE-002 | MTRL minimum trades by profile | pytest parametrize | None | 3 profiles × N; assert gate blocks if N < MTRL_min |
| P0-GATE-003 | Bootstrap stress 4 scenarios | pytest parametrize | None | 4 scenarios; assert p-value and Sharpe degradation |
| P0-GATE-004 | All 7 gates evaluated in sequence | pytest integration | B-003 | Fail Gate 2; assert gates 3-7 skipped |

### Live Gates (2 tests → 2 automated)

| Test ID | Test Name | Automation Method | Blocker | Rationale |
|---------|-----------|-------------------|---------|-----------|
| P0-LIVE-001 | Live Gate A — 9 CORE metrics validated | pytest integration | B-001 | Inject failing metric; assert promotion blocked |
| P0-LIVE-002 | Live Gate B — day-7 calibration | pytest integration | B-001, B-002 | FakeClock 7-day advance; slippage +55% → FAIL |

### Calendar Safety (4 tests → 4 automated)

| Test ID | Test Name | Automation Method | Blocker | Rationale |
|---------|-----------|-------------------|---------|-----------|
| P0-CAL-001 | HARD event window blocks all entries | pytest integration | B-002 | FakeClock in window; assert allow_long=allow_short=False |
| P0-CAL-002 | Pair-specific filtering (UK CPI → GBP only) | pytest unit | B-002 | UK CPI; assert AUDUSD unaffected |
| P0-CAL-003 | Calendar Safety cannot be disabled | pytest unit | None | Assert CalendarSafety.disabled raises error |
| P0-CAL-004 | risk_flags.json artifact generated | pytest integration | B-001 | FOMC event run; assert risk_flags.json schema |

### Rocket Portfolio Kill Switches (5 tests → 5 automated)

| Test ID | Test Name | Automation Method | Blocker | Rationale |
|---------|-----------|-------------------|---------|-----------|
| P0-ROCKET-001 | Circuit breaker fires within 60s | pytest integration | None | FakeRocketRegistry: inject 6 deaths; assert within 1 poll |
| P0-ROCKET-002 | Rocket kill switch: DD > 15% | pytest unit | None | DD=16%; assert kill triggered |
| P0-ROCKET-003 | Wilson Score safety gate N<50 | pytest unit | None | N=5; assert kill NOT triggered |
| P0-ROCKET-004 | Wilson Score N>=50 LCB < 30% | pytest unit | None | N=50, win_rate=40%; assert kill triggered |
| P0-ROCKET-005 | Rocket bucket hard cap <= 10% NAV | pytest unit | None | 11% rockets; assert auto-adjustment to 10% |

### CLI and Rollback (3 tests → 2 automated, 1 semi-manual)

| Test ID | Test Name | Automation Method | Blocker | Rationale |
|---------|-----------|-------------------|---------|-----------|
| P0-CLI-001 | CLI backtest produces run_id and artifacts | pytest integration | B-001, B-005 | subprocess.run katana backtest; artifact assertion |
| P0-CLI-002 | Same inputs → same run_id and hashes | pytest integration | B-001, B-005 | Run twice; compare all hashes |
| P0-OPS-001 | Rollback <= 5 minutes | pytest performance | B-005 | time() around rollback CLI call; assert < 300s |

**P0 TOTAL: 52 tests → 50 automated (96%), 2 edge-manual (P0-SIG-006 boundary validation, P0-GATE-003 scenario review)**

---

## P1 Tests: Automation Coverage (68 tests → 62 automated, 6 manual)

**P1 automation rate: 91%**

### Signal Framework AUX and Integration (4 tests → 4 automated)

| Test ID | Test Name | Automation Method | Blocker |
|---------|-----------|-------------------|---------|
| P1-SIG-001 | AUX conditions (volume_surge, rsi, divergence) | pytest unit | None |
| P1-SIG-002 | Entry window enforcement (first 10 min) | pytest unit | None |
| P1-SIG-003 | SL formula: max(1.5×ATR14, MA20±buffer) | pytest unit | None |
| P1-SIG-004 | TP1/TP2/trailing prices | pytest unit | None |

### Price Action Module (5 tests → 5 automated)

| Test ID | Test Name | Automation Method | Blocker |
|---------|-----------|-------------------|---------|
| P1-PA-001 | PA module skipped when disabled | pytest unit | None |
| P1-PA-002 | >= 8 base patterns — textbook examples | pytest parametrize | None |
| P1-PA-003 | pa_max_patterns <= 2 enforcement | pytest integration | B-003 |
| P1-PA-004 | pa_confidence_min threshold filtering | pytest unit | None |
| P1-PA-005 | pa_patterns.json artifact per run | pytest integration | B-001 |

### Optimization Pipeline Extended (10 tests → 9 automated, 1 semi-manual)

| Test ID | Test Name | Automation Method | Blocker | Manual Reason |
|---------|-----------|-------------------|---------|---------------|
| P1-OPT-001 | Hierarchical L2→L1 (3 rounds) | pytest integration | B-003 | — |
| P1-OPT-002 | CLI filtering flags | pytest unit | B-005 | — |
| P1-OPT-003 | 4 risk mode presets | pytest parametrize | None | — |
| P1-OPT-004 | 3-10 uncorrelated instances | pytest integration | B-003 | — |
| P1-OPT-005 | Checkpoint + resume | pytest integration | B-001, B-003 | — |
| P1-OPT-006 | Early stopping convergence | pytest unit | None | — |
| P1-OPT-007 | Walk-Forward median OOS Sharpe | pytest unit | None | — |
| P1-OPT-008 | 64 signal combinations | pytest unit | None | — |
| P1-OPT-009 | Adaptive entry frequency convergence | pytest integration | B-003 | — |
| P1-OPT-010 | Dashboard load < 5 min for 8,000 trials | pytest performance | B-001 | Threshold advisory; hardware-dependent |

### Wave 4 Multi-TF and DFF (8 tests → 8 automated)

| Test ID | Test Name | Automation Method | Blocker |
|---------|-----------|-------------------|---------|
| P1-WAVE4-001 | Independent study per TF (0% parameter bleed) | pytest integration | B-003 |
| P1-WAVE4-002 | ensure_up_to_date() incremental download | pytest integration | None |
| P1-WAVE4-003 | load() latency < 100ms from PostgreSQL | pytest performance | requires_postgres |
| P1-WAVE4-004 | 10 dist_* columns populated, 0% NaN | hypothesis | None |
| P1-WAVE4-005 | Multiplier constraint enforcement | pytest unit | None |
| P1-WAVE4-006 | DFF backward compat with legacy SL/TP | pytest regression | None |
| P1-WAVE4-007 | FOMC HARD block positions closed 30min before | pytest integration | B-002 |
| P1-WAVE4-008 | SOFT mode 0.5x sizing during MEDIUM event | pytest integration | B-002 |

### MTF Confirmation (3 tests → 3 automated)

| Test ID | Test Name | Automation Method | Blocker |
|---------|-----------|-------------------|---------|
| P1-MTF-001 | Kill-switch on negative mtf_delta_DSR | pytest unit | None |
| P1-MTF-002 | mtf_block_rate telemetry in signal_quality.json | pytest integration | B-001 |
| P1-MTF-003 | Timeframe ratio 4:1 to 6:1 enforcement | pytest unit | None |

### Risk Management Suite (5 tests → 5 automated)

| Test ID | Test Name | Automation Method | Blocker |
|---------|-----------|-------------------|---------|
| P1-RISK-001 | Kelly eligibility gate (N<100 or PSR<0.85) | pytest unit | None |
| P1-RISK-002 | Dual-stop logic PASSIVE vs HARD | pytest integration | B-001 |
| P1-RISK-003 | VaR 5 methods | pytest unit | None |
| P1-RISK-004 | Historical stress tests 8 scenarios | pytest integration | None |
| P1-RISK-005 | HMM regime classification | pytest unit | None |

### Rocket Portfolio Extended (6 tests → 5 automated, 1 semi-manual)

| Test ID | Test Name | Automation Method | Blocker | Manual Reason |
|---------|-----------|-------------------|---------|---------------|
| P1-ROCKET-001 | MC 10,000 simulations in < 60s | pytest performance | None | — |
| P1-ROCKET-002 | MC 4 criteria validation | pytest integration | None | — |
| P1-ROCKET-003 | State machine GREEN/YELLOW/RED/BLACK | pytest unit | None | — |
| P1-ROCKET-004 | Rocket kill: age>7d + negative P&L | pytest unit | None | — |
| P1-ROCKET-005 | All 3 circuit breaker triggers | pytest unit | None | — |
| P1-ROCKET-006 | Profit transfer 80% to core | pytest unit | None | — |

### Dashboard Phase 1 (4 tests → 4 automated)

| Test ID | Test Name | Automation Method | Blocker |
|---------|-----------|-------------------|---------|
| P1-DASH-001 | Dashboard generation from backtest_summary.json | pytest integration | None |
| P1-DASH-002 | schema_version parsing + fallback warning | pytest unit | B-004 |
| P1-DASH-003 | Dashboard data export 3 formats | pytest unit | None |
| P1-DASH-004 | Parameter comparison 2-5 runs side-by-side | pytest integration | None |

### Data Management (5 tests → 5 automated)

| Test ID | Test Name | Automation Method | Blocker |
|---------|-----------|-------------------|---------|
| P1-DATA-001 | OHLCV loading from >= 2 sources | pytest unit | None |
| P1-DATA-002 | Data caching — second load from cache | pytest unit | None |
| P1-DATA-003 | Turnover cap <= 30%/day | pytest unit | None |
| P1-DATA-004 | Degradation triggers — corr < 0.5 for 7d | pytest integration | B-002 |
| P1-DATA-005 | Adaptive portfolio rebalancing on regime change | pytest integration | B-002 |

**P1 TOTAL: 68 tests → 62 automated (91%), 6 manual/semi-manual**

---

## P2 Tests: Automation Coverage (38 tests → 32 automated, 6 semi-manual)

**P2 automation rate: 84%**

### Signal Boundary Values (5 tests → 5 automated — pytest parametrize + hypothesis)

All P2-SIG-* tests are boundary condition tests. Automated with parametrize and exact boundary values (e.g., `wick_ratio == 0.70000001` vs `wick_ratio == 0.70000000`).

### Optimization Algorithm Properties (7 tests → 7 automated — hypothesis + pytest)

P2-OPT-001 through P2-OPT-007: algorithm correctness, PBO formula, DSR formula, WF split dates. All deterministic; fully automated.

### Quality Gate Edge Cases (2 tests → 2 automated)

P2-GATE-001 (Ljung-Box p > 0.05) and P2-GATE-002 (PSR formula) are pure mathematical assertions.

### Calendar Safety Helpers (2 tests → 2 automated)

P2-CAL-001 (event calendar loaded at startup — 0 network calls during backtest) and P2-CAL-002 (news_overlay disabled → sizing unchanged).

### DFF Properties (2 tests → 2 automated)

P2-DFF-001 (mixed-source DFF) and P2-DFF-002 (DFF precompute overhead < 5%) automated with performance timing.

### Rocket Edge Cases (4 tests → 4 automated)

P2-ROCKET-001 through P2-ROCKET-004: N_min formula, Tier 1 cap, hysteresis 3-day rule, auto-redeploy queue. All deterministic unit tests.

### Risk Thresholds (3 tests → 3 automated)

P2-RISK-001 through P2-RISK-003: eligibility gates, PSR_live threshold, paper vs live deviation. Parametrize threshold boundaries.

### Dashboard Extended (4 tests → 4 automated)

P2-DASH-001 through P2-DASH-004: HTML structural validation via BeautifulSoup.

### CLI and Operations (6 tests → 5 automated, 1 semi-manual)

| Test ID | Automation | Reason |
|---------|-----------|--------|
| P2-CLI-001 | pytest integration | subprocess; assert composable step |
| P2-CLI-002 | pytest unit | assert run_id format regex |
| P2-OPS-001 | pytest integration | assert registry snapshot created |
| P2-OPS-002 | pytest integration | lifecycle state machine transitions |
| P2-OPS-003 | pytest integration | DD breach → Run Journal entry |
| P2-OPS-004 | pytest integration | convergence criterion assertion |
| P2-DATA-001 | pytest integration | cross-platform hash (Windows+Linux) — needs 2 runners |
| P2-DATA-002 | pytest unit | hash mismatch assertion |

**Note:** P2-DATA-001 (cross-platform hash) is semi-manual in CI: requires matrix job with `windows-latest` + `ubuntu-latest` runners.

**P2 TOTAL: 38 tests → 32 automated (84%), 6 semi-manual or platform-conditional**

---

## P3 Tests: Automation Coverage (22 tests → 11 automated, 11 manual)

**P3 automation rate: 50%**

### Performance Benchmarks (6 tests → 4 automated, 2 semi-manual)

| Test ID | Automation | Method |
|---------|-----------|--------|
| P3-PERF-001 | Automated | pytest-benchmark; CI proxy 200 trials |
| P3-PERF-002 | Automated | time() around dashboard generation |
| P3-PERF-003 | Automated | memory_profiler during 100-trial optimization |
| P3-PERF-004 | Automated | time() for 100 sequential backtests; scale estimate |
| P3-PERF-005 | Semi-manual | Timing automated; result validation manual |
| P3-PERF-006 | Semi-manual | Disabled→0ms automated; enabled<30s automated |

### Monte Carlo Tests (3 tests → 3 automated)

| Test ID | Automation | Method |
|---------|-----------|--------|
| P3-MC-001 | Automated | time(); assert < 60s |
| P3-MC-002 | Automated | Known distribution; assert statistics range |
| P3-MC-003 | Automated | Pre-validated reference portfolio; assert 4 criteria |

### Historical Stress Tests (3 tests → 2 automated, 1 semi-manual)

| Test ID | Automation | Method |
|---------|-----------|--------|
| P3-STRESS-001 | Automated | 2008 crisis fixture; assert survives + MaxDD reported |
| P3-STRESS-002 | Automated | COVID-2020 fixture; assert survives |
| P3-STRESS-003 | Semi-manual | 2022 crypto data availability uncertain; manual if data not available |

### Documentation Validation (3 tests → 0 automated, 3 manual)

| Test ID | Automation | Reason |
|---------|-----------|--------|
| P3-DOCS-001 | Manual | Browser visual rendering — subjective |
| P3-DOCS-002 | Manual | CLI help text accuracy vs PRD — subjective review |
| P3-DOCS-003 | Manual | PRD example vs artifact diff — document reading |

### Exploratory Tests (7 tests → 2 automated, 5 manual)

| Test ID | Automation | Method |
|---------|-----------|--------|
| P3-EXP-001 | Automated | Filter cascade 4 combinations; assert entry decisions |
| P3-EXP-002 | Manual | Strategy Registry lifecycle — interactive exploration |
| P3-EXP-003 | Automated | Expert Council output schema assertion |
| P3-EXP-004 | Manual | Sobol QMC uniformity — visual/statistical analysis |
| P3-EXP-005 | Manual | Rocket bucket color-coded states — visual |
| P3-EXP-006 | Manual | MTF shadow P&L — exploratory |
| P3-EXP-007 | Manual | HMM 3+ years historical — exploratory |

**P3 TOTAL: 22 tests → 11 automated (50%), 11 manual**

---

## Manual Test Protocol: 25 Manual Tests

For the 25 tests that cannot be automated, a structured manual test protocol applies:

### Manual Test Execution Protocol

```
Test: [Test ID]
Name: [Full test name]
Pre-conditions:
  - [What must be true before starting]
Steps:
  1. [Numbered step]
  2. [Numbered step]
Expected Result:
  - [What constitutes a PASS]
Evidence Required:
  - Screenshot / CLI output / file content
Pass/Fail: [ ] PASS [ ] FAIL
Tester: [Name]
Date: [Date]
Notes: [Any deviations or observations]
```

### Manual Test Schedule

| Test ID | Scheduled | Estimated Duration | Owner |
|---------|-----------|-------------------|-------|
| P3-DOCS-001 | Day 22 | 30 min | Dev/QA |
| P3-DOCS-002 | Day 22 | 20 min | Dev/QA |
| P3-DOCS-003 | Day 22 | 45 min | Dev/QA |
| P3-EXP-002 | Day 23 | 60 min | Dev |
| P3-EXP-004 | Day 23 | 30 min | QA |
| P3-EXP-005 | Day 23 | 20 min | Dev/QA |
| P3-EXP-006 | Day 23 | 30 min | Dev |
| P3-EXP-007 | Day 24 | 45 min | Dev |
| P3-STRESS-003 | Day 21 | 30 min | Dev |
| P3-PERF-005 | Day 21 | 20 min | Dev |
| (other 15 semi-manuals) | Days 21-24 | ~4 hours total | Dev/QA |

---

## Coverage Summary by Priority and Method

### Total Coverage Matrix

| Priority | Total | pytest unit | pytest integration | hypothesis | pytest performance | BeautifulSoup | CLI subprocess | Manual |
|----------|-------|-------------|-------------------|------------|-------------------|---------------|----------------|--------|
| P0 | 52 | 28 | 16 | 3 | 2 | 0 | 3 | 2 |
| P1 | 68 | 31 | 26 | 1 | 4 | 4 | 2 | 6 |
| P2 | 38 | 22 | 8 | 1 | 2 | 4 | 1 | 6 |
| P3 | 22 | 2 | 2 | 0 | 4 | 2 | 1 | 11 |
| **Total** | **180** | **83** | **52** | **5** | **12** | **10** | **7** | **25** |
| **%** | **100%** | **46%** | **29%** | **3%** | **7%** | **6%** | **4%** | **14%** |

### Automation Coverage by Risk Category

| Risk Category | Tests | Automated | Coverage |
|--------------|-------|-----------|----------|
| DATA (leakage, NaN, hash) | 22 | 21 | 95% |
| TECH (search space, DFF, circuit breaker) | 28 | 27 | 96% |
| BUS (live degradation, Calendar Safety) | 18 | 17 | 94% |
| PERF (throughput, memory) | 12 | 9 | 75% |
| OPS (rollback, artifacts, registry) | 15 | 13 | 87% |
| SEC (artifact integrity) | 5 | 5 | 100% |
| Exploratory / Documentation | 12 | 3 | 25% |
| Dashboard / CLI | 18 | 14 | 78% |
| Rocket / Risk math | 20 | 19 | 95% |
| Optimization algorithm | 30 | 27 | 90% |
| **TOTAL** | **180** | **155** | **86%** |

---

## Execution-Phase Implementation Schedule (Days 15-25)

### Day 15-17: P0 Unit Test Implementation

**Target:** All P0 unit tests implemented and green
**Count:** ~28 pure unit tests
**Approach:** Implement against available code modules; no blockers required for unit tests

```
Day 15: P0-SIG-001 through P0-SIG-008 (8 tests — signal framework core)
Day 16: P0-DATA-001 through P0-DATA-004 (4 tests — data integrity)
         P0-OPT-001, P0-OPT-003, P0-OPT-004, P0-OPT-006 (4 tests — pure unit opts)
Day 17: P0-GATE-001 through P0-GATE-003 (3 tests — quality gates)
         P0-ROCKET-002 through P0-ROCKET-005 (4 tests — rocket kill switches)
         P0-CAL-003 (1 test — Calendar Safety disable assertion)
```

### Day 18-19: P0 Integration Test Implementation

**Target:** All P0 integration tests implemented (B-001 through B-005 resolved by now)
**Count:** ~22 P0 integration tests
**Blockers required:** B-001, B-002, B-003, B-005

```
Day 18: P0-SIG-009, P0-SIG-010, P0-SIG-011 (Calendar Safety integration)
         P0-DATA-002, P0-DATA-005 (data hash integration)
         P0-OPT-002, P0-OPT-005, P0-OPT-007 (optimization integration)
Day 19: P0-CAL-001, P0-CAL-002, P0-CAL-004 (Calendar Safety full coverage)
         P0-GATE-004, P0-LIVE-001, P0-LIVE-002 (gates + live gates)
         P0-CLI-001, P0-CLI-002, P0-OPS-001 (CLI integration)
         P0-ROCKET-001 (circuit breaker integration)
```

### Day 20-21: P1 Implementation

**Target:** All P1 tests implemented
**Count:** 68 tests (62 automated + 6 manual scheduled)
**Focus:** Wave 4 DFF, optimization pipeline, risk suite, dashboard validation

```
Day 20: P1-SIG-*, P1-PA-*, P1-OPT-001 through P1-OPT-009 (23 tests)
Day 21: P1-WAVE4-*, P1-MTF-*, P1-RISK-*, P1-ROCKET-*, P1-DASH-*, P1-DATA-* (39 tests)
         Manual tests P3-STRESS-003, P3-PERF-005 scheduled
```

### Day 22-23: P2 and P3 Implementation

**Target:** All P2 tests, automated P3 tests
**Count:** 38 + 11 = 49 tests

```
Day 22: P2-SIG-*, P2-OPT-*, P2-GATE-*, P2-CAL-*, P2-DFF-* (19 tests)
         Manual tests P3-DOCS-001, P3-DOCS-002, P3-DOCS-003 executed
Day 23: P2-ROCKET-*, P2-RISK-*, P2-DASH-*, P2-CLI-*, P2-DATA-*, P2-OPS-* (19 tests)
         P3-PERF-001 through P3-PERF-004, P3-MC-*, P3-STRESS-001, P3-STRESS-002,
         P3-EXP-001, P3-EXP-003 (11 automated P3 tests)
         Manual tests P3-EXP-002, P3-EXP-004, P3-EXP-005, P3-EXP-006 executed
```

### Day 24-25: Coverage Validation and Reporting

```
Day 24: Full regression run — all 155 automated tests
         Manual tests P3-EXP-007 + remaining semi-manual
         Coverage report generated
         Failure triage and fixes
Day 25: Final coverage report
         automation-results.md generated
         automation-suite.md finalized
         coverage-report.md with full metrics
```

---

## Success Criteria for Execution Phase

**Automation suite is COMPLETE when:**

- [ ] 155 automated tests implemented in `tests/` directory
- [ ] All P0 automated tests passing (0 failures acceptable)
- [ ] P1 automated tests: >= 95% passing (max 3 failures, all triaged)
- [ ] P2 automated tests: >= 90% passing
- [ ] P3 automated tests: >= 85% passing
- [ ] 25 manual tests executed with PASS/FAIL recorded in manual protocols
- [ ] Overall branch coverage: >= 80% for katana modules
- [ ] No open HIGH-severity defects in data integrity or circuit breaker tests
- [ ] Coverage report published to `_bmad-output/zone3/coverage-report.md`
- [ ] Automation results published to `_bmad-output/zone3/automation-results.md`

---

## Appendix: Blocked Test Resolution Plan

When blockers are resolved, these tests transition from BLOCKED to ACTIVE:

| When B-001 Resolved | Transitions to Active |
|---------------------|----------------------|
| P0-SIG-009 | Signal quality artifact integration |
| P0-DATA-002, P0-DATA-005 | Data hash integration tests |
| P0-OPT-007 | Artifact completeness integration |
| P0-CAL-004 | risk_flags.json artifact |
| P0-LIVE-001, P0-LIVE-002 | Live gate simulations |
| P0-CLI-001, P0-CLI-002 | CLI subprocess integration |
| ~20 additional P1+ tests | Various integration tests |

| When B-002 Resolved | Transitions to Active |
|---------------------|----------------------|
| P0-SIG-011 | Calendar Safety integration |
| P0-CAL-001, P0-CAL-002 | Calendar Safety integration |
| P1-WAVE4-007, P1-WAVE4-008 | FOMC/SOFT mode integration |
| P1-DATA-004, P1-DATA-005 | Regime/degradation integration |

| When B-003 Resolved | Transitions to Active |
|---------------------|----------------------|
| P0-OPT-002, P0-OPT-005 | Optimization gate tests |
| P1-OPT-001, P1-OPT-004, P1-OPT-005, P1-OPT-009 | Optimization integration |
| P1-PA-003 | PA TrialPruned test |
| P1-WAVE4-001 | Per-TF parameter bleed test |

| When B-004 Resolved | Transitions to Active |
|---------------------|----------------------|
| P1-DASH-002 | schema_version fallback warning |
| P1-DATA-006 | Backward compat v1.0→v2.0 |
| schema assertions in all artifact tests | Previously asserted only existence |

| When B-005 Resolved | Transitions to Active |
|---------------------|----------------------|
| P0-CLI-001, P0-CLI-002 | CLI integration tests in CI |
| P0-OPS-001 | Rollback timing in CI |
| P1-OPT-002 | CLI filtering flags |
| All CLI subprocess tests | Previously local-only |

---

*Generated by Agent-6 (testarch-automate), Zone 3 Prep Phase*
*Date: 2026-02-26*
*Coordination key: orchestration:zone:3:agent6-progress*
*Monitoring keys: orchestration:zone:2:dev-story-outputs, orchestration:zone:2:atdd-failure-analysis*
