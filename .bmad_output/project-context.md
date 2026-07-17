# Katana VectorBT - Project Context for AI Agents

**Project**: katana-vectorbt
**Type**: Brownfield (Autonomous Trading Strategy Platform)
**Status**: Phase L2 → L3 (Architecture Audit Complete)
**Generated**: 2026-02-28

---

## 1. Technology Stack & Versions

### Core Technologies
- **Python**: 3.11+ (MANDATORY - requires f-string = syntax, type hints)
- **FastAPI**: 0.109.0+ (async web framework)
- **uvicorn**: 0.27.0+ (ASGI server with standard extras)
- **pandas**: 2.0+ (data processing, breaking changes from 1.x - NO .values, use .to_numpy())
- **numpy**: 1.24+ (numerical operations)
- **Optuna**: 3.0+ (hyperparameter optimization, 400+ trial budgets)
- **scipy**: 1.7.0+ (statistical functions for strategy validation)
- **ccxt**: 4.0.96+ (crypto exchange API - ASYNC ONLY in 4.x)

### Testing & Quality
- **pytest**: 7.0+ (283+ tests required, 95% coverage minimum)
- **pytest-cov**: 4.0+ (coverage enforcement)
- **Black**: 23.0+ (line-length=88, enforced by pre-commit)
- **isort**: 5.12+ (import ordering, profile="black")
- **mypy**: 1.0+ (type checking, Python 3.11 mode)
- **ruff**: 0.1+ (fast linter, E/F/W/I/N/UP/RUF rules)
- **flake8**: 6.0+ (style guide enforcement)
- **pre-commit**: 3.0+ (BLOCKS COMMITS if violations found)
- **bandit**: 1.7+ (security scanning for crypto operations)

### Data & Visualization
- **plotly**: 5.0+ (interactive backtesting charts)
- **dash**: 2.14.0+ (web UI for strategy monitoring)
- **papermill**: 2.3.0+ (notebook parameter injection)
- **nbformat/nbconvert**: 5.0+/6.0+ (Jupyter integration)

### Critical Version Constraints
⚠️ **DO NOT IGNORE:**
- pandas 2.0+ breaks `.values` accessor - use `.to_numpy()` or `.array`
- Optuna 3.x trial API changed - MUST use `trial.suggest_float()`, not `trial.suggest_uniform()`
- ccxt 4.x is async-only - ALL exchange calls require `async`/`await`
- Python 3.11 required for dict union operator `|` used in config merging
- Pre-commit WILL block commits with Black/isort/flake8 violations

---

## 2. Language-Specific Rules (Python 3.11)

### Type Hints (MANDATORY)
- All function signatures MUST have type hints (mypy enforces this)
- Use `from typing import *` for complex types
- Use `dataclasses` or `Pydantic` for config classes (NOT manual __init__)
- Return type hints MUST be present, even if `-> None`

### Import Organization
- **Order**: stdlib → third-party → local (enforced by isort, profile="black")
- **Convention**: `from katana.conditions import detect_patterns` (relative imports from src/katana/)
- **Never**: Wildcard imports (`from X import *`)
- **Known first party**: `["katana"]` (configured in pyproject.toml)

### Code Style Enforced by Black
- Line length: **88 characters** (NOT 79)
- String quotes: Double quotes preferred (`"string"`)
- f-strings: USE for all string formatting (Python 3.11+)
- No trailing commas in single-line structures

### Error Handling
- Use custom exception classes (inherit from `Exception`)
- Log errors with structured logging (dict format for JSON parsing)
- Never suppress exceptions silently (`except: pass` is FORBIDDEN)
- Optuna trials MUST catch `optuna.TrialPruned` separately

### Async/Await Rules
- CCXT calls MUST be wrapped in `async def` functions
- Use `asyncio.gather()` for parallel exchange queries (NOT threads)
- NEVER mix sync and async in same function
- Await ALL coroutines explicitly

---

## 3. Framework-Specific Rules (FastAPI)

### API Endpoint Structure
- Use Pydantic models for request/response schemas
- All endpoints MUST have docstrings (Swagger generation)
- Use path parameters for IDs, query parameters for filters
- Return HTTP 200 for success, 400 for validation errors, 500 for server errors

### Configuration Management
- Use Pydantic Settings for environment variables
- Config class hierarchy: `BaseSettings` → `TraderConfig` → `StrategyConfig`
- YAML configs loaded via `from_yaml()` method
- Dict merge with union operator: `config = {**base, **overrides}`

### Strategy Parameter Profiles
- 3 profiles ONLY: **stable**, **return**, **rocket** (NOT arbitrary)
- Each profile has fixed parameter ranges (in PRD)
- Optuna searches within profile bounds (≤70 active parameters per trial)
- Results cached in memory with profile name as key

---

## 4. Testing Rules (pytest)

### Test Organization
- **Path**: `src/tests/` (configured in pyproject.toml)
- **File naming**: `test_*.py` or `*_test.py`
- **Class naming**: `Test*` (inheritance from `unittest.TestCase` optional)
- **Function naming**: `test_*`

### Coverage Requirements
- **Minimum**: 95% coverage (enforced by pytest-cov)
- **Branches**: ALL if/else branches must be tested
- **Edge cases**: Boundary values (0, negative, max_int)
- **Errors**: Test exception paths, not just happy path

### Mock Usage (pytest-mock)
- Use `mocker.patch()` for external dependencies (ccxt, databases)
- Mock ccxt with fixture: `@pytest.fixture def mock_ccxt(mocker)`
- Never mock the code under test - only external calls
- Verify mock was called: `mock.assert_called_with(...)`

### Test Structure Pattern
```python
def test_pattern_detection_with_valid_candle(mock_exchange):
    # Arrange
    candle = Candle(open=100, high=110, low=95, close=105, volume=1000)

    # Act
    result = detect_patterns([candle])

    # Assert
    assert len(result) > 0
    assert result[0].confidence >= 0.6
```

### Integration Tests
- Separate folder: `src/tests/integration/`
- Use real (sandbox) exchange data when possible
- Timeout: 30 seconds per test (enforced by pytest-timeout)
- Mark with `@pytest.mark.integration` for selective runs

---

## 5. Code Quality & Style Rules

### Linting Enforcement (pre-commit BLOCKS commits)
- **Black**: MUST pass `black --check .`
- **isort**: MUST pass `isort --check-only .`
- **ruff**: MUST pass with rules: E/F/W/I/N/UP/RUF
- **flake8**: MUST NOT exceed complexity (McCabe 10)
- **bandit**: MUST NOT have security issues (no hardcoded secrets)

### File Organization
```
src/katana/
├── conditions/           # Pattern detection (pa_patterns.py, pa_hard_limits.py)
├── optimization/         # Optuna integration (hyperparameter search)
├── portfolio/           # Risk management (3-tier cascade, state transitions)
├── data/                # Data loading and preprocessing
├── api/                 # FastAPI endpoints
└── tests/              # Test suite (mirrors src structure)
```

### Naming Conventions
- **Variables**: `snake_case` (NEVER camelCase)
- **Constants**: `UPPER_CASE` (for final values only)
- **Classes**: `PascalCase` (with descriptive nouns)
- **Functions**: `snake_case` with verb prefix (`detect_`, `calculate_`, `validate_`)
- **Private methods**: `_prefix_method_name()` (single underscore for internal use)
- **Modules**: `snake_case.py` (lowercase, no hyphens)

### Documentation Requirements
- **Docstrings**: Triple-quoted strings for ALL classes and public functions
- **Format**: Google-style docstrings (Args, Returns, Raises)
- **Type hints**: In docstrings match function signature
- **Examples**: Include 1-2 usage examples for complex functions

---

## 6. Development Workflow Rules

### Git Conventions
- **Branches**: `feature/`, `bugfix/`, `hotfix/` prefixes
- **Commit messages**: Imperative mood ("Add feature" NOT "Added feature")
- **Format**: `[TYPE] Subject (max 50 chars)\n\nBody (wrapped at 72 chars)`
- **Types**: `feat:`, `fix:`, `test:`, `docs:`, `refactor:`, `perf:`

### Pre-commit Hooks (MANDATORY)
- Runs Black, isort, flake8, mypy, bandit
- Fixes formatting issues automatically (Black/isort)
- BLOCKS commit if errors remain
- Skip with `git commit --no-verify` (NOT RECOMMENDED)

### Pull Request Checklist
- All tests passing (pytest -v with coverage)
- Code coverage ≥95% for new code
- No security issues (bandit clean)
- Type hints present (mypy passes)
- Documentation updated (if API changed)

### Deployment Patterns
- Use FastAPI + uvicorn for production
- Environment: Docker container with Python 3.11
- Configuration: Load from `config.yaml` or environment variables
- Secrets: Use `python-dotenv` for local dev, K8s secrets for prod

---

## 7. Critical Don't-Miss Rules (Anti-Patterns & Gotchas)

### 🚫 ANTI-PATTERNS (WILL BREAK TESTS)

**1. pandas .values**
```python
# ❌ WRONG - breaks with ExtensionArray in pandas 2.0+
data = df.values
# ✅ CORRECT
data = df.to_numpy()
```

**2. Optuna old API**
```python
# ❌ WRONG - Optuna 3.x removed this
trial.suggest_uniform("param", 0, 1)
# ✅ CORRECT
trial.suggest_float("param", 0, 1)
```

**3. Sync CCXT calls**
```python
# ❌ WRONG - ccxt 4.x is async-only
exchange = ccxt.binance()
ticker = exchange.fetch_ticker('BTC/USDT')
# ✅ CORRECT
exchange = ccxt.async_binance()
ticker = await exchange.fetch_ticker('BTC/USDT')
```

**4. Missing type hints in production code**
```python
# ❌ WRONG - mypy will fail
def calculate(value):
    return value * 2
# ✅ CORRECT
def calculate(value: float) -> float:
    return value * 2
```

**5. Hardcoded secrets in code**
```python
# ❌ WRONG - bandit will fail
API_KEY = "sk-12345abc"
# ✅ CORRECT
API_KEY = os.getenv("CCXT_API_KEY")
```

### ⚡ EDGE CASES TO HANDLE

**1. Empty DataFrames**
- Always check `df.empty` before processing
- Return empty result list, don't raise error

**2. Optuna Trial Pruning**
- Catch `optuna.TrialPruned` separately (NOT in generic except)
- Log pruned trials for debugging

**3. Exchange Rate Limits**
- Implement exponential backoff for ccxt API calls
- CCXT `enable_rateLimit = True` (already configured)

**4. Missing Market Data**
- Handle `ccxt.NetworkError`, `ccxt.ExchangeNotAvailable`
- Retry 3 times before failing

**5. Parameter Profile Boundaries**
- All Optuna suggestions MUST be within profile bounds
- Raise `ValueError` if bounds violated

### 🔒 SECURITY RULES

**1. API Keys**
- NEVER hardcode in code or commit to git
- Use `python-dotenv` for local dev (`.env` in .gitignore)
- Use K8s secrets or AWS Secrets Manager for production

**2. Data Validation**
- Validate CCXT tickers format: `"BTC/USDT"` (always uppercase pair)
- Validate candle data: price > 0, volume ≥ 0
- Reject NaN or infinity values in optimization

**3. Exchange Connections**
- Use sandbox endpoints for testing (CCXT supports this)
- NEVER test with real money in development
- Log all API calls for audit trail

### ⚡ PERFORMANCE GOTCHAS

**1. DataFrame copies**
- `.copy()` is expensive on large datasets
- Use views when possible: `df.loc[start:end]`

**2. Optuna parallelization**
- DO NOT parallelize Optuna trials manually
- Optuna handles distribution internally
- Parallel CCXT calls OK inside single trial

**3. Memory management**
- Clear trial cache after optimization: `study.trials.clear()` (if needed)
- Use generators for large data streams

---

## 8. Project-Specific Implementation Rules

### Pattern Detection Module (pa_patterns.py)
- 8 candlestick patterns: PinBar, Engulfing, InsideBar, BreakoutRetest, Hammer, ShootingStar, MorningStar, EveningStar
- Confidence scoring: float 0.0-1.0 based on pattern characteristics
- All patterns inherit from `PatternDetector` base class

### Hard Limits Module (pa_hard_limits.py)
- Confidence threshold: minimum 0.6 for signal generation (US-PA-003)
- Occurrence limits per session: PinBar≤5, Engulfing≤4, Hammer≤3, Other≤2
- Filter before signal generation (confidence THEN occurrence)

### Risk Management (3-Tier Cascade)
- **Tier 1 (Rockets)**: 10% of capital, scalping 1-5min
- **Tier 2 (Intraday)**: 70-80% of capital, 1-4hour
- **Tier 3 (Medium-term)**: 10-20% of capital, 4hour-1day
- **Transfer trigger**: When Tier N equity > initial +50%, weekly transfer to next tier

### Risk Tier States (GREEN/YELLOW/RED/BLACK)
- **GREEN**: Normal operations, 10 rockets active
- **YELLOW**: Win rate 30-40%, reduce to 7 rockets, daily review
- **RED**: Win rate <30%, reduce to 3 rockets, real-time review
- **BLACK**: Drawdown >20%, 0% allocation, all rockets halted

---

## Next Steps for AI Agents

When implementing in this project:
1. **ALWAYS** run `pytest -v --cov=src/katana --cov-report=term-missing` before committing
2. **VERIFY** all type hints with `mypy src/katana`
3. **FORMAT** with `black src/katana && isort src/katana`
4. **LINT** with `flake8 src/katana` and `ruff check src/katana`
5. **SECURITY** scan with `bandit -r src/katana`
6. **DOCUMENT** all public APIs with docstrings

---

**Last Updated**: 2026-02-28
**Version**: 1.0 (Project Context Discovery Complete)
**Status**: ✅ READY FOR AGENT IMPLEMENTATION
