---
agent: testarch-automate
zone: 3
phase: prep
generatedDate: '2026-02-26'
status: READY_FOR_USE
type: checklist
---

# Automation Setup Checklist: katana-vectorbt

**Agent:** Agent-6 (testarch-automate), Zone 3 Prep Phase
**Date:** 2026-02-26
**Purpose:** Environment verification before automation execution begins (Day 15)
**Format:** Execute sequentially; check each item before proceeding to next group

---

## Group 1: Python Environment Verification

Complete this group FIRST. No automation work proceeds without Python environment confirmed.

- [ ] **1.1** Python version: `python --version` outputs `3.9.x` or higher
  - Required: Python 3.9+
  - Recommended: Python 3.11 (matches CI)
  - Fix: `pyenv install 3.11` or `conda create -n katana python=3.11`

- [ ] **1.2** pytest installed and functional: `python -m pytest --version` returns `7.x.x`
  - Fix: `pip install "pytest>=7.0.0"`

- [ ] **1.3** Core test dependencies installed:
  ```bash
  pip install \
    "pytest>=7.0.0" \
    "pytest-cov>=4.0.0" \
    "pytest-timeout>=2.1.0" \
    "pytest-xdist>=3.0.0" \
    "hypothesis>=6.0.0" \
    "pytest-mock>=3.0.0" \
    "beautifulsoup4>=4.12.0" \
    "lxml>=4.9.0"
  ```
  - Verify: `pip list | grep pytest` shows all packages

- [ ] **1.4** katana project dependencies installed: `pip install -r requirements.txt`
  - Verify: `python -c "import katana"` succeeds (no ImportError)

- [ ] **1.5** vectorbt Pro license active: `python -c "import vectorbt as vbt; print(vbt.__version__)"`
  - CRITICAL: 350+ existing tests require vectorbt Pro
  - Fix: Check license environment variables; contact vectorbt Pro support

- [ ] **1.6** Optuna installed: `python -c "import optuna; print(optuna.__version__)"` outputs `3.x.x`
  - Fix: `pip install "optuna>=3.0.0"`

- [ ] **1.7** hypothesis installed: `python -c "from hypothesis import given; print('OK')"`
  - Fix: `pip install "hypothesis>=6.0.0"`

---

## Group 2: Test Collection Verification

- [ ] **2.1** Run test discovery (no execution): `python -m pytest --collect-only tests/ -q`
  - Verify: Collects existing 350+ tests without errors
  - Any `ImportError` or `ModuleNotFoundError` must be resolved before proceeding

- [ ] **2.2** Verify existing suite passes: `python -m pytest tests/ -m "unit" -q --timeout 60`
  - Target: All existing unit tests pass (0 failures)
  - Expected: ~350+ tests collected and passing
  - STOP if more than 5% failure rate — resolve existing failures first

- [ ] **2.3** Verify pytest markers work: `python -m pytest tests/ -m "not slow" --collect-only -q`
  - Should collect tests without warnings about unknown markers
  - If unknown marker warnings: add markers to `pytest.ini` or `pyproject.toml`

---

## Group 3: Fixture Infrastructure Setup

### Frozen OHLCV Test Data (requires Dev — B-001)

- [ ] **3.1** OHLCV fixture directory exists: `tests/fixtures/ohlcv/`
  - Create if missing: `mkdir -p tests/fixtures/ohlcv/`

- [ ] **3.2** Frozen parquet fixtures committed (from Dev, after B-001):
  - [ ] `tests/fixtures/ohlcv/EURUSD_1m_frozen.parquet` (1,000+ bars, SHA256 recorded)
  - [ ] `tests/fixtures/ohlcv/EURUSD_5m_frozen.parquet` (1,000+ bars)
  - [ ] `tests/fixtures/ohlcv/EURUSD_15m_frozen.parquet` (1,000+ bars)
  - [ ] `tests/fixtures/ohlcv/EURUSD_1h_frozen.parquet` (1,000+ bars)
  - [ ] `tests/fixtures/ohlcv/EURUSD_4h_frozen.parquet` (1,000+ bars)
  - [ ] `tests/fixtures/ohlcv/EURUSD_1d_frozen.parquet` (1,000+ bars)
  - STATUS: BLOCKED on B-001. Proceed with synthetic generators in interim.

- [ ] **3.3** Synthetic OHLCV generator available (interim before B-001):
  ```python
  # tests/fixtures/generators/synthetic_ohlcv.py
  # Verify this file exists and imports correctly
  from tests.fixtures.generators.synthetic_ohlcv import generate_synthetic_ohlcv
  df = generate_synthetic_ohlcv(n_bars=1000, seed=42)
  assert len(df) == 1000
  assert set(["open", "high", "low", "close", "volume"]).issubset(df.columns)
  ```

### FakeClock Infrastructure

- [ ] **3.4** FakeClock class created in `tests/conftest.py`:
  - Class implements: `now()`, `advance(minutes)`, `advance_days(days)`
  - Verify: `from tests.conftest import FakeClock; c = FakeClock(datetime.now()); c.advance(60)`

- [ ] **3.5** FakeClock injectable into CalendarSafety (requires Dev — B-002):
  - STATUS: BLOCKED on B-002.
  - When B-002 resolved: verify `CalendarSafety(clock=fake_clock)` accepts injectable
  - Workaround until B-002: unit-test time-agnostic CalendarSafety logic only

### Optuna Study Factory

- [ ] **3.6** In-memory Optuna study fixture created in `tests/conftest.py`:
  ```python
  @pytest.fixture
  def optuna_study():
      import optuna
      return optuna.create_study(
          storage=None,
          sampler=optuna.samplers.QMCSampler(seed=42),
          direction="maximize",
      )
  ```
  - Verify: `python -m pytest tests/ -k "optuna_study" --collect-only` finds fixture

- [ ] **3.7** Study isolation verified: Two parallel pytest-xdist workers do not share study state
  - Test: Run `python -m pytest tests/test_optuna_isolation.py -n 2` (test to be created)
  - STATUS: BLOCKED on B-003 for full validation; fixture design complete.

### FakeRocketRegistry

- [ ] **3.8** FakeRocketRegistry class created in `tests/fixtures/rocket_fixtures.py`:
  - Class implements: `register_rocket()`, `kill_rocket()`, `kill_simultaneous(n)`
  - Verify: `from tests.fixtures.rocket_fixtures import FakeRocketRegistry; r = FakeRocketRegistry(); r.kill_simultaneous(6); assert r.death_count == 6`

### Artifact Validation Helpers

- [ ] **3.9** Artifact validation helper created in `tests/helpers/artifact_helpers.py`:
  - Function: `assert_run_artifacts_complete(run_dir, schema_version="1.0")`
  - Verify: Import succeeds; function callable with mock path argument

- [ ] **3.10** Schema version validation waits on B-004:
  - STATUS: BLOCKED on B-004.
  - Workaround: Assert artifacts exist; skip schema_version assertion until B-004 resolved.

---

## Group 4: CI Environment Configuration

### GitHub Actions / Local CI Environment

- [ ] **4.1** `.env.test` file created (local) with:
  ```bash
  KATANA_N_WORKERS=1
  KATANA_TEST_ENV=ci
  KATANA_SEED=42
  KATANA_CLOCK_SOURCE=fake
  KATANA_OPTUNA_STORAGE=memory
  COVERAGE_THRESHOLD_STATEMENTS=80
  COVERAGE_THRESHOLD_BRANCHES=75
  PYTEST_TIMEOUT=120
  ```
  - Verify: `cat .env.test` shows all variables

- [ ] **4.2** `pytest.ini` or `pyproject.toml` configured with all markers:
  ```ini
  [tool.pytest.ini_options]
  markers = [
      "unit: Pure unit tests",
      "integration: Integration tests",
      "performance: Performance benchmarks",
      "monte_carlo: Monte Carlo simulation tests",
      "monte_carlo_heavy: Heavy Monte Carlo (weekly only)",
      "wave4: Wave 4 specific tests",
      "requires_postgres: Tests requiring PostgreSQL",
      "slow: Tests taking >30 seconds",
      "property_based: Hypothesis property-based tests",
      "cli: CLI subprocess integration tests",
      "dashboard: HTML dashboard validation tests",
  ]
  ```
  - Verify: `python -m pytest --markers` lists all markers without warnings

- [ ] **4.3** Coverage configuration in `.coveragerc`:
  ```ini
  [run]
  source = katana
  [report]
  fail_under = 80
  omit = tests/*, */vendor/*
  exclude_lines =
      if DEBUG:
      if __name__ == "__main__":
      raise NotImplementedError
  ```
  - Verify: `python -m pytest tests/ -m unit --cov=katana --cov-report=term-missing -q`

- [ ] **4.4** `--n-workers 1` flag works on CLI (requires B-005):
  - STATUS: BLOCKED on B-005.
  - Verify once B-005 resolved: `python -m katana backtest --n-workers 1 --help` shows flag
  - Workaround: CLI integration tests skip in CI until B-005; run locally only.

- [ ] **4.5** GitHub Actions workflow file created: `.github/workflows/test-automation.yml`
  - Base template from `zone1/test-framework-setup.md` (Section 11: CI/CD Integration)
  - Extended with Python pytest job from this prep phase
  - Verify: `gh workflow run test-automation.yml` triggers without errors

---

## Group 5: Blocker Tracking

### Pre-conditions Dependent on Dev (B-001 through B-005)

Track each blocker status. Do not attempt blocked tests until resolved.

- [ ] **5.1 B-001: Deterministic Seed Contract**
  - Status: [ ] OPEN [ ] IN PROGRESS [ ] RESOLVED
  - Resolved when: `seed` parameter accepted by `backtest()`, `optimize()`, `monte_carlo()`
  - Verification test: Run same config twice with seed=42; assert all metric values identical
  - Estimated resolution: Sprint 1 Epic J (Week 1-2)
  - Automation tests unblocked: ~40 integration tests with numeric assertions

- [ ] **5.2 B-002: ClockProtocol Injection**
  - Status: [ ] OPEN [ ] IN PROGRESS [ ] RESOLVED
  - Resolved when: `CalendarSafety(clock=FakeClock(...))` accepted without error
  - Verification test: `calendar_safety = CalendarSafety(clock=FakeClock(fomc_pre_window_time)); result = calendar_safety.evaluate("EURUSD"); assert result.blocked`
  - Estimated resolution: Pre-Wave 4 Sprint 1
  - Automation tests unblocked: All 15 Calendar Safety integration tests (P0-CAL-*, P1-WAVE4-007)

- [ ] **5.3 B-003: Optuna Study Isolation**
  - Status: [ ] OPEN [ ] IN PROGRESS [ ] RESOLVED
  - Resolved when: `optuna.create_study(storage=None)` usable as pytest fixture without RDB
  - Verification test: Two parallel pytest workers with `optuna_study` fixture run without state corruption
  - Estimated resolution: Sprint 1 Epic J (Week 1-2)
  - Automation tests unblocked: ~25 optimization pipeline integration tests

- [ ] **5.4 B-004: Artifact Schema Versioning**
  - Status: [ ] OPEN [ ] IN PROGRESS [ ] RESOLVED
  - Resolved when: All JSON artifacts contain `schema_version` field
  - Verification test: `data = json.loads((run_dir / "progress.json").read_text()); assert data["schema_version"] == "1.0"`
  - Estimated resolution: Pre-Epic J Sprint 1
  - Automation tests unblocked: ~12 backward compatibility tests

- [ ] **5.5 B-005: --n-workers 1 CLI Override**
  - Status: [ ] OPEN [ ] IN PROGRESS [ ] RESOLVED
  - Resolved when: `python -m katana mass_optimize --n-workers 1` runs with single worker
  - Verification test: `assert os.environ.get("KATANA_N_WORKERS", "1") == "1"` in CI
  - Estimated resolution: Pre-Epic J Sprint 1
  - Automation tests unblocked: All CLI subprocess integration tests (P0-CLI-*, P0-OPS-*)

---

## Group 6: Zone 2 Output Monitoring

When Agent-4 (dev-story) produces implementation code, begin mapping automation:

- [ ] **6.1** Monitor orchestration memory key: `orchestration:zone:2:dev-story-outputs`
  - Check daily after Day 5
  - When available: Extract list of implemented modules; map to test IDs

- [ ] **6.2** Monitor orchestration memory key: `orchestration:zone:2:atdd-failure-analysis`
  - When available: Review ATDD failure patterns
  - Identify any tests needing automation approach adjustment

- [ ] **6.3** When Agent-4 code available, verify automation prerequisites:
  - [ ] `import katana.signals` succeeds
  - [ ] `import katana.optimization` succeeds
  - [ ] `import katana.risk` succeeds
  - [ ] `import katana.rockets` succeeds
  - [ ] `python -m katana --help` shows all CLI commands

---

## Group 7: Automation Template Verification

- [ ] **7.1** Verify automation-architecture.md is complete and approved:
  - File: `_bmad-output/zone3/automation-architecture.md`
  - Status: COMPLETE (this document's companion)

- [ ] **7.2** Verify test-automation-coverage-plan.md is complete:
  - File: `_bmad-output/zone3/test-automation-coverage-plan.md`
  - Status: COMPLETE (companion document)

- [ ] **7.3** Create `tests/` directory structure (can do now, before code exists):
  ```bash
  mkdir -p tests/unit/signals
  mkdir -p tests/unit/optimization
  mkdir -p tests/unit/risk
  mkdir -p tests/unit/rockets
  mkdir -p tests/unit/calendar
  mkdir -p tests/unit/pipeline
  mkdir -p tests/unit/dashboard
  mkdir -p tests/integration/optimization
  mkdir -p tests/integration/cli
  mkdir -p tests/integration/wave4
  mkdir -p tests/integration/live_gates
  mkdir -p tests/performance
  mkdir -p tests/property_based
  mkdir -p tests/fixtures/ohlcv
  mkdir -p tests/fixtures/results
  mkdir -p tests/fixtures/calendar
  mkdir -p tests/fixtures/rockets
  mkdir -p tests/fixtures/dashboards
  mkdir -p tests/helpers
  mkdir -p tests/manual_protocols
  ```
  - Verify: `ls tests/` shows all directories

- [ ] **7.4** Base `conftest.py` scaffold created at `tests/conftest.py`:
  - Contains: FakeClock, FakeRocketRegistry, optuna_study fixture, assert_run_artifacts_complete
  - Verify: `python -m pytest tests/ --collect-only -q` succeeds

- [ ] **7.5** Manual test protocol template created at `tests/manual_protocols/manual-test-template.md`:
  - Template covers: P3-DOCS-001, P3-DOCS-002, P3-DOCS-003, P3-EXP-002, P3-EXP-005
  - Each manual test has: Pre-conditions, Steps, Expected Result, Pass/Fail criteria

---

## Group 8: Day-15 Execution Go/No-Go Checklist

On Day 15, before beginning full automation implementation, verify:

- [ ] **8.1** All Group 1–4 items complete
- [ ] **8.2** B-001 through B-005: at minimum B-001, B-003, B-005 RESOLVED
  - Can proceed with reduced scope if B-002 and B-004 still open (skip blocked tests)
- [ ] **8.3** Agent-4 (dev-story) code available for import
- [ ] **8.4** Agent-5 (testarch-atdd) failure analysis available
- [ ] **8.5** `python -m pytest tests/ --collect-only -q` collects all new test files without errors
- [ ] **8.6** CI pipeline runs green on base test suite (0 failures in existing 350+ tests)

**GO Decision:** If 8.1, 8.3, 8.4, 8.6 all pass AND at least 3 of 5 blockers resolved → PROCEED
**NO-GO Decision:** If 8.6 fails or Agent-4 code unavailable → ESCALATE to orchestrator

---

## Checklist Summary Dashboard

| Group | Items | Complete | Blocked | Status |
|-------|-------|----------|---------|--------|
| 1: Python Environment | 7 | TBD | 0 | Run now |
| 2: Test Collection | 3 | TBD | 0 | Run now |
| 3: Fixture Infrastructure | 10 | TBD | 5 (B-001 through B-005) | Partial |
| 4: CI Configuration | 5 | TBD | 1 (B-005) | Partial |
| 5: Blocker Tracking | 5 | 0 | 5 | Monitoring |
| 6: Zone 2 Monitoring | 3 | 0 | 0 | Async watch |
| 7: Template Verification | 5 | TBD | 0 | Run now |
| 8: Day-15 Go/No-Go | 6 | 0 | 0 | Day 15 |

**Overall Prep Phase Completion Target:** Groups 1, 2, 7 complete by Day 5; Groups 3, 4 complete once blockers resolved; Groups 5, 6 continuous monitoring.

---

*Generated by Agent-6 (testarch-automate), Zone 3 Prep Phase*
*Date: 2026-02-26*
*Next: automation-architecture.md (companion) and test-automation-coverage-plan.md*
