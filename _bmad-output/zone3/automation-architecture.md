---
agent: testarch-automate
zone: 3
phase: prep
generatedDate: '2026-02-26'
status: PREP_COMPLETE
version: 1.0.0
inputDocuments:
  - zone1/test-design-qa.md
  - zone1/test-design-architecture.md
  - zone1/test-framework-setup.md
blockersPending:
  - B-001
  - B-002
  - B-003
  - B-004
  - B-005
expectedDayExecutionBegins: 15
automationReadinessPercent: 72
---

# Automation Architecture: katana-vectorbt

**Agent:** Agent-6 (testarch-automate), Zone 3 Prep Phase
**Date:** 2026-02-26
**Phase:** Preparation (execution begins Day 15)
**Target:** 85%+ automation coverage of 180 ATDD tests by Day 25
**Framework Basis:** Zone 1 outputs — test-design-qa.md + test-framework-setup.md + test-design-architecture.md

---

## Executive Summary

This document defines the automation architecture for the katana-vectorbt test suite. The system targets 180 test scenarios across four priority tiers (P0–P3). Based on Zone 1 analysis, the project uses a Python-first CLI architecture with a Phase 1 static HTML dashboard — this directly shapes the automation strategy.

**Key Architectural Finding:** The katana-vectorbt project is CLI/Python-primary. Phase 1 has NO live REST API or interactive browser UI. Playwright E2E automation is deferred to Phase 2. The automation stack is therefore pytest-dominant with structured subprocess invocation patterns for CLI integration tests.

**Automation Coverage Target:**

| Priority | Tests | Automation Rate | Rationale |
|----------|-------|-----------------|-----------|
| P0 | 52 | 96% (50 auto, 2 manual) | Critical paths — zero tolerance for manual gaps |
| P1 | 68 | 91% (62 auto, 6 manual) | High-value integration paths; 6 performance benchmarks semi-manual |
| P2 | 38 | 84% (32 auto, 6 manual) | Edge cases; some exploratory boundary tests semi-manual |
| P3 | 22 | 50% (11 auto, 11 manual) | Performance + exploratory; many inherently semi-manual |
| **Total** | **180** | **86% (155 auto, 25 manual)** | Exceeds 85% target |

---

## 1. Tool Selection

### 1.1 Primary Automation Stack

#### pytest 7.0+ (Python) — PRIMARY ENGINE

**Why pytest is the dominant tool:**
- All katana-vectorbt logic is Python (vectorbt Pro, Optuna, pandas, numpy)
- CLI is Python-invocable via subprocess
- 350+ existing tests already use pytest; zero migration cost
- hypothesis library enables property-based tests (critical for R-001, R-007, R-009)
- pytest-xdist for parallel test execution (4 workers in CI, 1 in integration tests)

**Critical plugins:**
```
pytest>=7.0.0
pytest-cov>=4.0.0          # Coverage reporting (target: >80% branches)
pytest-timeout>=2.1.0       # Per-test timeout enforcement
pytest-xdist>=3.0.0         # Parallel execution (-n 4 for unit, -n 1 for integration)
hypothesis>=6.0.0           # Property-based testing (R-001, R-007, R-009)
pytest-mock>=3.0.0          # Mock injection for FakeClock, FakeRocketRegistry
pandas-testing              # DataFrame equality assertions
numpy.testing               # Array-level assertions with tolerance
```

#### Playwright 1.43+ (TypeScript) — DEFERRED TO PHASE 2

Per Zone 1 test-design-qa.md (Not in Scope): "Phase 1 is static HTML; no backend or live UI interactions. No browser automation (Playwright/Cypress) required until Phase 2 hosted app."

**Phase 2 trigger:** When the Streamlit/Dash live application is deployed, Playwright automation activates. The framework scaffold from Zone 1 (test-framework-setup.md) remains ready.

**Phase 1 Playwright scope (limited):**
- HTML validation of generated static reports (not browser automation)
- `playwright test --project=api` for REST endpoint smoke tests (Phase 2+)
- Dashboard HTML structural assertions via regex/BeautifulSoup (Python)

#### subprocess + REST client (Python) — CLI INTEGRATION LAYER

For CLI integration tests (P0-CLI, P0-OPS, P1-OPT checkpoint/resume):
```python
# Pattern: CLI subprocess invocation
import subprocess
import json
import time

def run_katana(args: list[str], timeout: int = 300) -> dict:
    """Run katana CLI command, return parsed JSON output."""
    result = subprocess.run(
        ["python", "-m", "katana"] + args,
        capture_output=True,
        text=True,
        timeout=timeout
    )
    assert result.returncode == 0, f"katana {args} failed: {result.stderr}"
    return json.loads(result.stdout) if result.stdout else {}
```

#### hypothesis (Python) — PROPERTY-BASED TESTING

Required for three critical risk areas:
- **R-001/R-009:** `active_param_count <= 70` invariant across 10,000 random parameter profiles
- **R-007:** NaN propagation across random OHLCV slices in `prepare_features()`
- **P2-OPT-001:** QMC sampler seed consistency (determinism property)

```python
from hypothesis import given, settings
from hypothesis import strategies as st

@given(st.fixed_dictionaries({
    "ma_fast": st.integers(5, 50),
    "ma_slow": st.integers(20, 200),
    "rsi_period": st.integers(7, 21),
}))
@settings(max_examples=10_000)
def test_param_profile_invariant(params):
    """R-009: active_param_count <= 70 for any valid parameter combination."""
    profile = build_parameter_profile(params)
    assert profile.active_param_count <= 70 or profile.trial_status == "PRUNED"
```

#### BeautifulSoup4 + lxml — HTML DASHBOARD VALIDATION

For Phase 1 static HTML dashboard tests (P1-DASH-001 through P1-DASH-004, P2-DASH-*):
```python
from bs4 import BeautifulSoup

def assert_dashboard_structure(html_path: Path):
    """Assert Phase 1 HTML report contains required sections."""
    soup = BeautifulSoup(html_path.read_text(), "lxml")
    assert soup.find(id="net-pnl"), "Net P&L section missing"
    assert soup.find(id="equity-curve"), "Equity curve missing"
    assert soup.find(id="profit-factor"), "Profit Factor section missing"
```

---

## 2. Test Category Automation Mapping

### 2.1 Fully Automated Categories (pytest)

#### Category A: Pure Unit Tests — 100% automation

All signal framework unit tests (P0-SIG-001 through P0-SIG-011), data integrity
(P0-DATA-001 through P0-DATA-005), optimization invariants (P0-OPT-001 through P0-OPT-007),
quality gates (P0-GATE-001 through P0-GATE-004), risk suite (P1-RISK-*), and rocket
kill-switch logic (P0-ROCKET-002 through P0-ROCKET-005).

**Automation pattern:** Pure function call → assert output

```python
def test_p0_sig_005_rule1_absolute_priority():
    """R-016: Rule 1 (MACD) overrides all other beacon rules."""
    # Given: MACD impulse is False (Rule 1 trigger)
    signal_state = SignalState(
        macd_impulse=False,          # Rule 1 trigger
        fractal_breakout=True,       # Rule 2: normally no downgrade
        mtf_trend=True,              # Rule 3: normally no downgrade
        upper_wick_ratio=0.3,        # Rule 4: below threshold
        volatility_ratio=1.0,        # Rule 5: normal
    )
    # When: beacon level computed
    beacon = compute_beacon_level(signal_state)
    # Then: Rule 1 forces mini regardless of other rules
    assert beacon == BeaconLevel.MINI, (
        f"Expected MINI when MACD impulse False, got {beacon}"
    )
```

#### Category B: Property-Based Tests — 100% automation (hypothesis)

- P0-OPT-003: 10,000 random parameter profiles assert `active_param_count <= 70`
- P0-DFF-002: Random OHLCV slices produce 0% NaN in `dist_*` columns
- P2-OPT-001: QMC sampler determinism across seeds

#### Category C: Integration Tests with Injectable Doubles — 98% automation

Tests requiring `FakeClock`, `FakeRocketRegistry`, in-memory Optuna study factory.
All injectable via pytest fixtures (awaiting B-002 and B-003 from Dev).

**FakeClock integration pattern:**
```python
@pytest.fixture
def fake_clock_fomc():
    """Clock fixture: T-100min before FOMC (within 120min pre-buffer)."""
    fomc_event = datetime(2026, 3, 20, 14, 0, 0, tzinfo=timezone.utc)
    return FakeClock(fixed_time=fomc_event - timedelta(minutes=100))

def test_p0_cal_001_hard_block_in_event_window(calendar_safety, fake_clock_fomc):
    """R-008: All entries blocked during HARD event window."""
    calendar_safety.clock = fake_clock_fomc
    result = calendar_safety.evaluate("EURUSD", signal_type="LONG")
    assert result.allow_long is False
    assert result.allow_short is False
    assert result.block_reason == "HARD_EVENT_WINDOW"
```

#### Category D: CLI Subprocess Integration — 90% automation

Tests invoking `katana` CLI via subprocess. Requires B-005 (`--n-workers 1`) to avoid OOM.

```python
def test_p0_cli_001_backtest_produces_artifacts(tmp_path, katana_config):
    """FR0.1: katana backtest produces run_id and complete artifact set."""
    result = run_katana([
        "backtest",
        "--config", str(katana_config),
        "--n-workers", "1",
        "--output-dir", str(tmp_path),
    ], timeout=120)
    run_id = result["run_id"]
    run_dir = tmp_path / "runs" / run_id
    # Assert all required artifacts present
    for artifact in ["backtest_summary.json", "signal_quality.json", "risk_flags.json"]:
        assert (run_dir / artifact).exists(), f"Missing artifact: {artifact}"
```

#### Category E: HTML Dashboard Validation — 100% automation (BeautifulSoup)

```python
def test_p1_dash_001_dashboard_generation(tmp_path, backtest_summary_fixture):
    """FR1-FR8: Dashboard generates HTML from backtest_summary.json."""
    html_path = tmp_path / "report.html"
    generate_dashboard(backtest_summary_fixture, output=html_path)
    assert html_path.exists()
    soup = BeautifulSoup(html_path.read_text(), "lxml")
    # Assert Net P&L with correct sign
    net_pnl = float(soup.find(id="net-pnl").text.strip().replace("$", "").replace(",", ""))
    assert abs(net_pnl - backtest_summary_fixture["net_pnl"]) < 0.01
```

### 2.2 Semi-Automated Categories (Hybrid: pytest triggers, manual verification)

#### Category F: Performance Benchmarks — 50% automation

Performance tests (P3-PERF-001 through P3-PERF-006) require automated execution
but threshold validation needs operator judgment due to hardware variability.

**Automation approach:** pytest-benchmark captures timing; thresholds flagged as advisory.

```python
@pytest.mark.performance
@pytest.mark.timeout(120)
def test_p3_perf_001_optimization_throughput(benchmark_optimization_runner):
    """8,000 total trials <= 1 day. CI proxy: 200 trials <= CI_PROXY_BUDGET_SECONDS."""
    CI_PROXY_BUDGET_SECONDS = 300  # 5 min CI proxy for 200 trials
    start = time.monotonic()
    result = benchmark_optimization_runner.run(n_trials=200, n_workers=1)
    elapsed = time.monotonic() - start
    # Assert CI proxy (200 trials in 5 min)
    assert elapsed < CI_PROXY_BUDGET_SECONDS, (
        f"CI proxy: 200 trials took {elapsed:.1f}s (budget: {CI_PROXY_BUDGET_SECONDS}s)"
    )
    # Report scale estimate
    estimated_8000_hours = (elapsed / 200 * 8000) / 3600
    print(f"\nScale estimate: 8,000 trials ~ {estimated_8000_hours:.1f} hours (1 worker)")
```

#### Category G: Monte Carlo Stress Tests — 60% automation

Monte Carlo tests (P3-MC-001, P1-ROCKET-001) are fully automated for timing,
but output distribution validation may need manual judgment.

```python
@pytest.mark.monte_carlo
def test_p1_rocket_001_monte_carlo_timing(rocket_portfolio):
    """FR67: 10,000 Monte Carlo simulations complete in <60s."""
    start = time.monotonic()
    results = rocket_portfolio.run_monte_carlo(n_simulations=10_000)
    elapsed = time.monotonic() - start
    assert elapsed < 60.0, f"Monte Carlo: {elapsed:.1f}s exceeded 60s budget"
    assert len(results.simulations) == 10_000
    # Distribution sanity checks (automated)
    assert results.statistics.var_5pct > -0.25, "VaR5% too extreme"
    assert results.statistics.prob_loss < 0.50, "Probability of loss too high"
```

### 2.3 Manual Test Categories

| Test | Reason Not Automated | Manual Approach |
|------|---------------------|-----------------|
| P3-DOCS-001: HTML renders in Chrome/Firefox/Edge | Visual layout; browser differences | Cross-browser screenshot review |
| P3-DOCS-002: CLI help text accuracy | Subjective correctness against PRD | Dev reads `--help` output vs PRD table |
| P3-DOCS-003: PRD artifact schema examples match output | Document diffing | Manual diff of PRD code block vs generated artifact |
| P3-EXP-002: Strategy Registry lifecycle | Exhaustive manual exploration | Dev walks all state transitions interactively |
| P3-EXP-005: Rocket bucket state visualization | Visual color-coding in dashboard | Dashboard review with rocket states |
| P2-CLI-002: run_id format consistency | Low risk; format validated by assertion | `katana backtest` output inspection |

---

## 3. Automation Architecture Diagram

```
katana-vectorbt Test Automation Architecture
============================================

                    ┌─────────────────────────────────┐
                    │     pytest 7.0+ (Python)        │
                    │     PRIMARY TEST RUNNER          │
                    └──────────┬──────────────────────┘
                               │
              ┌────────────────┼────────────────────┐
              │                │                    │
     ┌────────▼──────┐ ┌──────▼──────┐ ┌──────────▼──────┐
     │ Unit Tests    │ │ Integration │ │ Property-Based  │
     │ (pytest)      │ │ Tests       │ │ (hypothesis)    │
     │               │ │ (pytest)    │ │                 │
     │ P0-SIG-*      │ │             │ │ P0-OPT-003      │
     │ P0-DATA-*     │ │ P0-CAL-001  │ │ P0-DFF-002      │
     │ P0-OPT-001    │ │ P0-OPT-007  │ │ P2-OPT-001      │
     │ P0-GATE-*     │ │ P0-CLI-*    │ │                 │
     │ P0-ROCKET-*   │ │ P1-WAVE4-*  │ │ 10,000+         │
     │ P1-SIG-*      │ │ P1-OPT-*    │ │ examples each   │
     └───────────────┘ │ P1-RISK-*   │ └─────────────────┘
                       │ P1-ROCKET-* │
                       └──────┬──────┘
                              │
              ┌───────────────┼──────────────────┐
              │               │                  │
     ┌────────▼────┐ ┌───────▼──────┐ ┌────────▼──────┐
     │ FakeClock   │ │ In-memory    │ │ FakeRocket    │
     │ Injectable  │ │ Optuna Study │ │ Registry      │
     │ (B-002)     │ │ Factory      │ │ (Wave 4)      │
     │             │ │ (B-003)      │ │               │
     └─────────────┘ └──────────────┘ └───────────────┘
                              │
     ┌────────────────────────┼──────────────────────────┐
     │                        │                          │
     │                        │                          │
     ▼                        ▼                          ▼
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ CLI Subprocess   │  │ HTML Dashboard   │  │ Performance      │
│ Integration      │  │ Validation       │  │ Benchmarks       │
│                  │  │ (BeautifulSoup)  │  │                  │
│ subprocess.run() │  │                  │  │ pytest-benchmark │
│ P0-CLI-001-002   │  │ P1-DASH-001-004  │  │ P3-PERF-*        │
│ P0-OPS-001       │  │ P2-DASH-001-004  │  │ P3-MC-*          │
│ P1-OPT-005       │  │ P3-DOCS-001      │  │                  │
└──────────────────┘  └──────────────────┘  └──────────────────┘
         │
         ▼
┌──────────────────────────────────────────┐
│ Playwright (TypeScript) — PHASE 2 ONLY  │
│ NOT active in Phase 1 prep phase        │
│ Scaffold ready in zone1/               │
└──────────────────────────────────────────┘
```

---

## 4. Fixture Architecture

### 4.1 Core Fixtures (conftest.py — global)

```python
# tests/conftest.py — Shared fixtures across all test modules

import pytest
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta

# ----------------------------------------------------------------
# OHLCV Frozen Fixtures (awaiting B-001 — deterministic seed)
# ----------------------------------------------------------------

@pytest.fixture(scope="session")
def ohlcv_1m():
    """Frozen 1-minute OHLCV fixture. SHA256-validated. 1,000 bars."""
    path = Path("tests/fixtures/ohlcv/EURUSD_1m_frozen.parquet")
    assert path.exists(), f"Frozen fixture missing: {path}"
    df = pd.read_parquet(path)
    expected_hash = "sha256:abc123..."  # Will be filled when fixture committed
    assert _sha256_df(df) == expected_hash
    return df


@pytest.fixture(scope="session")
def ohlcv_all_timeframes(ohlcv_1m, ohlcv_5m, ohlcv_15m, ohlcv_1h, ohlcv_4h, ohlcv_1d):
    """All 6 TF frozen fixtures as dict."""
    return {
        "1m": ohlcv_1m, "5m": ohlcv_5m, "15m": ohlcv_15m,
        "1h": ohlcv_1h, "4h": ohlcv_4h, "1d": ohlcv_1d,
    }


# ----------------------------------------------------------------
# FakeClock (awaiting B-002 — ClockProtocol injection)
# ----------------------------------------------------------------

class FakeClock:
    """Injectable clock for deterministic time-dependent tests."""

    def __init__(self, fixed_time: datetime):
        self._time = fixed_time

    def now(self) -> datetime:
        return self._time

    def advance(self, minutes: int):
        self._time += timedelta(minutes=minutes)

    def advance_days(self, days: int):
        self._time += timedelta(days=days)


@pytest.fixture
def fake_clock_monday_03utc():
    """Monday 03:00 UTC — inside the Monday exclusion window (00:00-06:00)."""
    # Find next Monday
    now = datetime(2026, 3, 16, 3, 0, 0, tzinfo=timezone.utc)  # Monday
    return FakeClock(fixed_time=now)


@pytest.fixture
def fake_clock_fomc_pre_window():
    """T-100 minutes before FOMC event (inside 120min pre-buffer window)."""
    fomc_event = datetime(2026, 3, 20, 14, 0, 0, tzinfo=timezone.utc)
    return FakeClock(fixed_time=fomc_event - timedelta(minutes=100))


@pytest.fixture
def fake_clock_fomc_post_window():
    """T+200 minutes after FOMC event (outside any buffer)."""
    fomc_event = datetime(2026, 3, 20, 14, 0, 0, tzinfo=timezone.utc)
    return FakeClock(fixed_time=fomc_event + timedelta(minutes=200))


# ----------------------------------------------------------------
# Optuna In-Memory Study (awaiting B-003 — study isolation)
# ----------------------------------------------------------------

@pytest.fixture
def optuna_study():
    """Isolated in-memory Optuna study. Never touches shared RDB storage."""
    import optuna
    optuna.logging.set_verbosity(optuna.logging.WARNING)
    return optuna.create_study(
        storage=None,  # In-memory: no shared state between tests
        sampler=optuna.samplers.QMCSampler(seed=42),
        direction="maximize",
        study_name=f"test_study_{id(object())}",  # Unique per fixture
    )


# ----------------------------------------------------------------
# Artifact Validation Helpers
# ----------------------------------------------------------------

REQUIRED_ARTIFACTS = [
    "backtest_summary.json",
    "optimizer_summary.json",
    "signal_quality.json",
    "risk_flags.json",
    "pa_patterns.json",
    "progress.json",
]


def assert_run_artifacts_complete(run_dir: Path, schema_version: str = "1.0"):
    """Assert all required artifacts exist with correct schema_version."""
    for artifact_name in REQUIRED_ARTIFACTS:
        artifact_path = run_dir / artifact_name
        assert artifact_path.exists(), f"Missing: {artifact_name}"
        data = json.loads(artifact_path.read_text())
        # B-004: schema_version field required in all artifacts
        assert "schema_version" in data, f"schema_version missing in {artifact_name}"
        assert data["schema_version"] == schema_version
        assert "run_id" in data, f"run_id missing in {artifact_name}"


# ----------------------------------------------------------------
# FakeRocketRegistry (Wave 4 — circuit breaker tests)
# ----------------------------------------------------------------

class FakeRocketRegistry:
    """Injectable registry for circuit breaker integration tests."""

    def __init__(self):
        self.rockets = {}
        self.deaths = []

    def register_rocket(self, rocket_id: str, allocation: float):
        self.rockets[rocket_id] = {"allocation": allocation, "status": "ALIVE"}

    def kill_rocket(self, rocket_id: str, reason: str):
        self.rockets[rocket_id]["status"] = "DEAD"
        self.deaths.append({"rocket_id": rocket_id, "reason": reason,
                            "timestamp": datetime.now(timezone.utc)})

    def kill_simultaneous(self, n: int):
        """Kill n rockets simultaneously for circuit breaker trigger tests."""
        for i in range(n):
            rocket_id = f"rocket_{i:03d}"
            self.register_rocket(rocket_id, 0.01)
            self.kill_rocket(rocket_id, "TEST_KILL")

    @property
    def death_count(self) -> int:
        return len(self.deaths)


@pytest.fixture
def fake_rocket_registry():
    return FakeRocketRegistry()
```

### 4.2 Optimization Fixtures

```python
# tests/fixtures/optimization_fixtures.py

@pytest.fixture
def parameter_profile_factory():
    """Factory for generating katana parameter profiles."""
    def make_profile(**overrides):
        defaults = {
            "ma_fast": 10,
            "ma_slow": 50,
            "rsi_period": 14,
            "atr_multiplier": 1.5,
            "risk_mode": "stable",
            # ... all 115 parameters with valid defaults
        }
        return ParameterProfile(**{**defaults, **overrides})
    return make_profile


@pytest.fixture
def synthetic_backtest_results():
    """Factory for synthetic backtest results at various quality levels."""
    def make_results(pbo=0.30, dsr=0.97, wf_degradation=0.10, max_dd=0.15):
        return BacktestResults(
            pbo=pbo,
            deflated_sharpe_ratio=dsr,
            wf_degradation_pct=wf_degradation,
            max_drawdown=max_dd,
            n_trades=100,
            sharpe_is=2.5,
            sharpe_oos=2.0,
        )
    return make_results
```

---

## 5. Test Execution Tiering

### 5.1 PR/Commit Gate (Target: <15 min)

```bash
# Run on every PR — fast feedback
pytest tests/ \
    -m "unit or (integration and not slow)" \
    -n 4 \
    --n-workers 1 \
    -x \
    --timeout 60 \
    --cov=katana \
    --cov-fail-under=80 \
    -q
```

**Includes:** All P0 unit tests, P0 integration tests (FakeClock, in-memory Optuna),
selected P1 unit tests, P2 boundary tests
**Excludes:** Performance benchmarks, Monte Carlo stress, Wave 4 PostgreSQL tests

**Expected count:** ~90 tests, ~10–15 min

### 5.2 Nightly Full Integration (Target: <60 min)

```bash
# Nightly — full integration coverage
pytest tests/ \
    -m "not performance and not monte_carlo_heavy" \
    -n 2 \
    --n-workers 2 \
    --timeout 300 \
    --cov=katana \
    --cov-report=html \
    -v
```

**Includes:** All P0 + P1 + P2 tests, including PostgreSQL-backed Wave 4 tests
**Excludes:** Full 8,000-trial optimization runs, heavy Monte Carlo

**Expected count:** ~150 tests, ~45–60 min

### 5.3 Weekly Full Regression (Target: <4 hours)

```bash
# Weekly — comprehensive coverage including Wave 4 and performance
pytest tests/ \
    --n-workers 4 \
    --timeout 900 \
    --cov=katana \
    --cov-report=xml \
    -v

# Separate performance suite
pytest tests/ \
    -m "performance" \
    -n 1 \
    --timeout 3600
```

**Includes:** All 180 new tests + 350+ existing tests = 530+ total
**Includes:** Full 200-trial CI proxy for 8,000-trial throughput benchmark

### 5.4 pytest Markers Strategy

```ini
# pytest.ini or pyproject.toml
[tool.pytest.ini_options]
markers = [
    "unit: Pure unit tests (no I/O, no subprocess)",
    "integration: Integration tests (subprocess, I/O, injectable doubles)",
    "performance: Performance benchmarks (timing assertions)",
    "monte_carlo: Monte Carlo simulation tests (slow, nightly only)",
    "monte_carlo_heavy: Heavy MC tests (10,000+ simulations, weekly only)",
    "wave4: Wave 4 specific tests (requires PostgreSQL or test container)",
    "requires_postgres: Tests requiring PostgreSQL (skip if not available)",
    "slow: Tests taking >30 seconds",
    "property_based: Hypothesis property-based tests",
    "cli: CLI subprocess integration tests",
    "dashboard: HTML dashboard validation tests",
]
```

---

## 6. CI Environment Configuration

### 6.1 GitHub Actions Environment Variables

```yaml
# .github/workflows/test-automation.yml
env:
  # Core test configuration
  KATANA_N_WORKERS: "1"          # B-005: Single worker for CI (prevents OOM)
  KATANA_TEST_ENV: "ci"
  KATANA_SEED: "42"              # B-001: Deterministic seed for CI runs
  KATANA_CLOCK_SOURCE: "fake"    # B-002: Injectable clock in CI
  KATANA_OPTUNA_STORAGE: "memory"  # B-003: In-memory Optuna for CI

  # Coverage thresholds
  COVERAGE_THRESHOLD_STATEMENTS: "80"
  COVERAGE_THRESHOLD_BRANCHES: "75"

  # Database (optional — skip Wave 4 PostgreSQL tests if unavailable)
  POSTGRES_HOST: "localhost"
  POSTGRES_PORT: "5432"
  POSTGRES_DB: "katana_test"
  POSTGRES_USER: "katana_test_user"
  POSTGRES_PASSWORD: ${{ secrets.POSTGRES_TEST_PASSWORD }}

  # Timeouts
  PYTEST_TIMEOUT: "120"         # 2 min per test default
  CI_OPTIMIZATION_TIMEOUT: "600"  # 10 min max for any optimization test
```

### 6.2 Test Data Volume Requirements

For scale testing (1,000+ test case execution):

| Fixture Type | Count | Size | Location |
|---|---|---|---|
| OHLCV frozen parquet (6 TFs) | 6 files | ~50MB total | `tests/fixtures/ohlcv/` |
| Synthetic backtest results | 20 variants | ~1MB | `tests/fixtures/results/` |
| Calendar events fixtures | 12 sets | ~100KB | `tests/fixtures/calendar/` |
| Rocket state fixtures | 10 scenarios | ~200KB | `tests/fixtures/rockets/` |
| HTML dashboard fixtures | 5 templates | ~500KB | `tests/fixtures/dashboards/` |
| **Total test fixture data** | | **~52MB** | `tests/fixtures/` |

---

## 7. Blocker Impact on Automation Timeline

### 7.1 Blocker Status and Automation Dependency

| Blocker | Impacts | Tests Blocked | Workaround (Prep Phase) |
|---------|---------|---------------|------------------------|
| B-001: Deterministic Seed | All integration tests with numeric assertions | ~40 tests | Use hardcoded synthetic results; skip exact value assertions |
| B-002: ClockProtocol | All time-dependent tests | ~15 tests | Calendar Safety tests skipped; unit tests of time-agnostic logic proceed |
| B-003: Optuna Study Isolation | Optimization pipeline integration | ~25 tests | In-memory study factory pre-built; waiting for Dev to expose fixture |
| B-004: schema_version | Backward compat + artifact schema tests | ~12 tests | Schema tests skipped; artifact existence assertions proceed |
| B-005: --n-workers 1 | All CLI integration tests in CI | All CLI tests | CLI tests developed locally; marked skip_ci until B-005 resolved |

### 7.2 Automation Readiness by Phase

**Prep Phase (Now, Day 2):** 72% automation readiness
- Framework templates: COMPLETE
- Fixture architecture: DESIGNED (awaiting frozen OHLCV from Dev)
- Pure unit test automations: READY TO IMPLEMENT (no blockers)
- Integration test scaffolds: DESIGNED (awaiting B-001 through B-005)

**Post-Blockers Resolved (Day 7-10):** 95% automation readiness
- All integration tests: IMPLEMENTABLE
- CLI tests: RUNNABLE in CI
- Property-based tests: RUNNABLE
- Performance benchmarks: RUNNABLE

**Execution Phase (Day 15-25):** 100% implementation complete
- Full 155 automated tests implemented and passing
- 25 manual tests documented in manual test protocol
- Coverage report generated

---

## 8. Coverage Measurement

### 8.1 Coverage Targets by Module

| Module | Min Branch Coverage | Priority |
|--------|---------------------|----------|
| `katana.signals` (KATANA Core) | 85% | P0 |
| `katana.optimization` (Epic J) | 80% | P0 |
| `katana.risk` (Risk Suite) | 82% | P0 |
| `katana.calendar_safety` (Wave 4) | 88% | P0 |
| `katana.rockets` (Rocket Portfolio) | 80% | P0 |
| `katana.pipeline` (DFF) | 85% | P0 |
| `katana.cli` (CLI commands) | 75% | P1 |
| `katana.dashboard` (Phase 1) | 78% | P1 |
| `katana.data` (Data management) | 80% | P1 |
| **Overall** | **80%** | — |

### 8.2 Coverage Exclusions (justified)

```ini
# .coveragerc
[report]
omit =
    tests/*                # Test code itself
    */migrations/*         # DB migrations — tested via integration
    */vendor/*             # Third-party code
    katana/config/examples/* # Example configs
exclude_lines =
    # Debug-only branches
    if DEBUG:
    if __name__ == "__main__":
    # Protocol implementations (abstract)
    raise NotImplementedError
    # Type checking only
    if TYPE_CHECKING:
```

---

## 9. Automation Readiness Summary

**Prep Phase (Day 2) Deliverables:**
- automation-architecture.md (THIS DOCUMENT) — COMPLETE
- automation-setup-checklist.md — NEXT DELIVERABLE
- test-automation-coverage-plan.md — NEXT DELIVERABLE

**Day 15 Execution Phase Start Prerequisites:**
- B-001 through B-005 resolved by Dev (critical path)
- Frozen OHLCV fixtures committed to `tests/fixtures/ohlcv/`
- FakeClock class implemented (can be pre-built by QA before B-002)
- FakeRocketRegistry class implemented (pre-built by QA)
- in-memory Optuna study fixture verified working

**Automation Readiness Indicator:**
```
Day  2: ████████████████████░░░░░░░░░ 72% (framework designed, pure units ready)
Day  7: ████████████████████████████░ 95% (blockers resolved, integration ready)
Day 15: ██████████████████████████████ 100% (execution phase begins)
Day 25: ██████████████████████████████ 100% + RESULTS COMPLETE
```

---

*Generated by Agent-6 (testarch-automate), Zone 3 Prep Phase*
*Based on: zone1/test-design-qa.md (180 tests, P0-P3), zone1/test-framework-setup.md (Playwright+pytest), zone1/test-design-architecture.md (28 risks, 5 blockers)*
*Coordination: orchestration:zone:3:agent6-progress*
