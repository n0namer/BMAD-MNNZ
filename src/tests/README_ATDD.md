# ATDD Test Suite - Quick Start Guide

## What Is This?

This is an **ATDD (Acceptance Test Driven Development)** test suite for two major features:
- **FR-001**: Position Sizing Integration with Kelly Criterion & Optuna
- **UX-001**: Live Monitoring Dashboard

All **78 tests are currently FAILING** (red). They serve as specifications before implementation (green).

---

## Test Files Overview

| File | Tests | Story | Coverage |
|------|-------|-------|----------|
| `test_fr001_position_sizing_integration.py` | 13 | FR-001 AC1-AC13 | Integration tests |
| `test_kelly_sizing.py` | 16 | FR-001 AC1-AC4 | Kelly formula math |
| `test_optuna_with_sizing.py` | 13 | FR-001 AC5-AC7 | Optimization tuning |
| `test_dashboard_panels.py` | 18 | UX-001 AC1-AC18 | Panel components |
| `test_dashboard_callbacks.py` | 18 | UX-001 AC13-AC18 | Event system |
| **TOTAL** | **78** | FR-001 + UX-001 | 31 Acceptance Criteria |

---

## Quick Start

### 1. View Test Summary
```bash
# Read the full test mapping
cat src/tests/ATDD_TEST_SUMMARY.md

# Quick statistics
grep -c "def test_" src/tests/test_*.py
```

### 2. Run Tests (All Failing - Expected)

```bash
# Run ALL tests (expect 78 failures)
pytest src/tests/test_fr001*.py src/tests/test_kelly*.py \
        src/tests/test_optuna*.py src/tests/test_dashboard*.py -v

# Run by story
pytest src/tests/ -m "fr001" -v           # 42 FR-001 tests
pytest src/tests/ -m "ux001" -v           # 36 UX-001 tests

# Run by component
pytest src/tests/test_kelly_sizing.py -v          # Kelly math (16)
pytest src/tests/test_optuna_with_sizing.py -v    # Optuna (13)
pytest src/tests/test_fr001_position_sizing_integration.py -v  # Integration (13)
pytest src/tests/test_dashboard_panels.py -v      # Panels (18)
pytest src/tests/test_dashboard_callbacks.py -v   # Events (18)
```

### 3. View Test Details

```bash
# Show test names only
pytest src/tests/test_kelly_sizing.py --collect-only -q

# Show detailed docstrings
grep -A 5 "def test_" src/tests/test_kelly_sizing.py | head -30
```

---

## Test Organization

### FR-001: Position Sizing Integration

#### AC1-AC4: Kelly Criterion (in `test_kelly_sizing.py` + integration)
```
test_kelly_formula_basic_calculation()          ← Core formula
test_kelly_breakeven_win_rate()                  ← Math validation
test_kelly_increasing_with_win_rate()            ← Monotonicity
test_kelly_fractional_kelly_*()                  ← Risk reduction
test_kelly_position_constraints()                ← Limits enforcement
```

**What to implement**: `katana/live/kelly.py::KellyCriterion`
- Formula: `f* = (bp - q) / b`
- Methods: `calculate(win_rate, avg_win, avg_loss)`
- Features: Fractional Kelly, constraint enforcement

#### AC5-AC7: Optuna Optimization (in `test_optuna_with_sizing.py`)
```
test_optuna_basic_optimization()                 ← Parameter search
test_optuna_parameter_bounds()                   ← Range enforcement
test_optuna_convergence()                        ← Improvement over trials
test_optuna_*_constraints()                      ← Hard constraint handling
test_optuna_with_backtest_objective()            ← Real backtest integration
```

**What to implement**: `katana/live/optuna_optimizer.py::OptunaOptimizer`
- Method: `optimize(objective_func, param_space)`
- Features: TPE sampler, pruning, constraint support
- Integration: Works with backtest functions

#### AC8-AC13: Portfolio Constraints (in `test_fr001_position_sizing_integration.py`)
```
test_portfolio_constraint_max_allocation()       ← Per-symbol limits
test_portfolio_constraint_sector_limits()        ← Sector diversification
test_portfolio_constraint_leverage_limit()       ← Leverage cap
test_portfolio_constraint_correlation()          ← Correlation limits
test_portfolio_risk_management_vix()             ← Volatility adjustment
test_integration_kelly_optuna_constraints()      ← Full pipeline
```

**What to implement**: `katana/live/position_sizer.py::PositionSizer`
- Classes: `PortfolioConstraints`, `VIXAdjustment`
- Method: `calculate_positions(backtest_result, portfolio, vix_level, account_size)`
- Features: Multi-constraint enforcement, risk management

---

### UX-001: Live Monitoring Dashboard

#### AC1-AC4: Position Panel (in `test_dashboard_panels.py`)
```
test_position_panel_renders()                    ← Component rendering
test_position_panel_displays_symbols()           ← Symbol display
test_position_panel_shows_size_and_pnl()         ← Metrics display
test_position_panel_color_coding()               ← Green/red indicators
```

**What to implement**: `katana/dashboard/components/panels/PositionPanel`
- Displays: Symbol, quantity, entry/current price, P&L, return %, allocation
- Features: Real-time updates, color coding, responsive layout

#### AC5-AC8: Risk Metrics Panel (in `test_dashboard_panels.py`)
```
test_risk_panel_renders()                        ← Rendering
test_risk_panel_shows_metrics()                  ← Sharpe, DD, leverage
test_risk_panel_updates_on_data_change()         ← Live updates
test_risk_panel_alerts_on_threshold()            ← Alert generation
```

**What to implement**: `katana/dashboard/components/panels/RiskPanel`
- Metrics: Sharpe ratio, max drawdown, leverage, win rate, profit factor
- Features: Threshold monitoring, alert generation

#### AC9-AC12: Performance Analytics (in `test_dashboard_panels.py`)
```
test_performance_panel_renders()                 ← Chart rendering
test_performance_panel_equity_curve()            ← Line chart
test_performance_panel_period_returns()          ← Time period returns
test_performance_panel_drawdown_chart()          ← Drawdown visualization
```

**What to implement**: `katana/dashboard/components/panels/PerformancePanel`
- Charts: Equity curve, drawdown, period returns
- Features: Interactive tooltips, multiple timeframes

#### AC13-AC18: Real-time Callbacks (in `test_dashboard_callbacks.py`)
```
test_callbacks_on_position_update()              ← Position change events
test_callbacks_on_trade_executed()               ← Trade execution events
test_callbacks_on_risk_alert()                   ← Risk threshold events
test_callbacks_data_consistency()                ← Multi-callback safety
test_callbacks_error_handling()                  ← Exception isolation
test_callbacks_performance_monitoring()          ← Latency tracking
```

**What to implement**: `katana/dashboard/callbacks/CallbackManager` + async support
- Features: Event registration, listener management, error isolation
- Performance: < 50ms latency, > 10K events/sec throughput
- Async: Mixed sync/async callback support

---

## Test Execution Workflow

### Phase 1: Watch Tests Fail (RED)
```bash
pytest src/tests/test_kelly_sizing.py -v
# Output: 16 FAILED tests ❌
```

### Phase 2: Implement & Watch Pass (GREEN)
```bash
# Implement katana/live/kelly.py
# Then run tests again
pytest src/tests/test_kelly_sizing.py -v
# Output: 16 PASSED tests ✅
```

### Phase 3: Refactor & Maintain Quality
```bash
# Add coverage checks
pytest src/tests/test_kelly_sizing.py --cov=katana/live/kelly --cov-report=term-missing
# Target: 100% coverage on kelly.py
```

---

## Implementation Order (Recommended)

1. **Kelly Criterion** (1-2 days)
   - Implement pure formula in `katana/live/kelly.py`
   - Get `test_kelly_sizing.py` fully passing (16 tests)

2. **Position Sizing Integration** (2-3 days)
   - Integrate Kelly + constraints
   - Get `test_fr001_position_sizing_integration.py` passing (13 tests)

3. **Optuna Optimizer** (1-2 days)
   - Wrapper around Optuna library
   - Get `test_optuna_with_sizing.py` passing (13 tests)

4. **Dashboard Components** (3-4 days)
   - Panels for positions, risk, performance
   - Get `test_dashboard_panels.py` passing (18 tests)

5. **Callback System** (2-3 days)
   - Event registration, emission, async support
   - Get `test_dashboard_callbacks.py` passing (18 tests)

---

## Coverage Targets

```bash
# Position Sizing (FR-001)
pytest src/tests/test_fr001*.py src/tests/test_kelly*.py src/tests/test_optuna*.py \
  --cov=katana/live --cov-report=term-missing
# Target: 95%+ coverage

# Dashboard (UX-001)
pytest src/tests/test_dashboard*.py \
  --cov=katana/dashboard --cov-report=term-missing
# Target: 95%+ coverage
```

---

## Key Test Patterns

### Acceptance Criteria Mapping
Each test clearly states its AC:
```python
@pytest.mark.fr001
@pytest.mark.acceptance
@pytest.mark.kelly_criterion
def test_kelly_criterion_basic(self):
    """AC1: Calculate basic Kelly Criterion position size."""
```

### Test Structure (BDD Style)
```python
def test_something(self):
    """Description of AC being tested.

    GIVEN: Initial state
    WHEN: Action performed
    THEN: Expected outcome
    """
    # WHEN: ...
    # THEN: assert ...
```

### Fixtures for Isolation
```python
@pytest.fixture
def sample_trade_history(self) -> List[MockTrade]:
    """Fixture: Sample trade history."""
    return [...]  # Mock data
```

---

## Expected Test Output

### Before Implementation
```
======================== 78 failed in 2.34s ========================
FAILED test_kelly_criterion_basic - AssertionError
FAILED test_kelly_with_win_rate - AttributeError: module...
FAILED test_optuna_optimization_basic - ModuleNotFoundError...
FAILED test_position_panel_renders - ImportError...
```

### After Full Implementation
```
======================== 78 passed in 8.52s =========================
✅ test_kelly_criterion_basic PASSED
✅ test_kelly_with_win_rate PASSED
✅ test_position_panel_renders PASSED
... (all 78 tests passing)
```

---

## Troubleshooting

### Import Errors
```
ModuleNotFoundError: No module named 'katana.live.position_sizer'
→ Need to create the module being tested
```

### Assertion Failures
```
AssertionError: Kelly fraction must be between 0 and 1
→ Implementation logic doesn't match test expectations
→ Review test docstring (GIVEN/WHEN/THEN) for requirements
```

### Performance Timeouts
```
test_callbacks_performance_monitoring FAILED - latency exceeded
→ Callback execution taking > 50ms per event
→ Optimize callback handling logic
```

---

## Test Metadata

| Metric | Value |
|--------|-------|
| Total Tests | 78 |
| Total Lines of Code | ~2,500 |
| Stories Covered | 2 (FR-001, UX-001) |
| Acceptance Criteria | 31 |
| Modules to Implement | 5+ |
| Coverage Target | 95%+ |
| Performance Targets | < 50ms latency, > 10K events/sec |

---

## Success Definition

✅ **Complete when:**
- [ ] All 78 tests passing
- [ ] 95%+ code coverage on all modules
- [ ] All 13 FR-001 ACs verified passing
- [ ] All 18 UX-001 ACs verified passing
- [ ] Performance benchmarks met
- [ ] Integration tests validate full workflows

---

## Resources

- **Test Summary**: `ATDD_TEST_SUMMARY.md` (full AC mapping)
- **Test Framework**: pytest with fixtures and mocking
- **BDD Pattern**: Arrange-Act-Assert (Given-When-Then)
- **Markers**: `@pytest.mark.fr001`, `@pytest.mark.ux001`, `@pytest.mark.acceptance`

---

**Status**: ❌ RED (78 tests failing - expected)
**Next Step**: Implement modules to make tests pass (GREEN)
**Timeline**: 2-3 weeks for full implementation

---

Generated: 2026-02-28
ATDD Phase: Specification (RED) → Implementation (GREEN) → Refinement
