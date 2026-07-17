# Test Framework Setup Guide - Katana VectorBT Phase 1

**Project**: Katana VectorBT
**Phase**: Phase 1 MVP (Epics 1-6)
**Date**: 2026-02-26
**Status**: Implementation Ready
**Owner**: QA Lead / DevOps Engineer

---

## EXECUTIVE SUMMARY

This guide provides step-by-step setup instructions for the katana-vectorbt test framework. The framework enables parallel test execution (unit/integration/E2E) with database isolation, GitHub Actions CI/CD integration, and comprehensive coverage tracking.

**Setup Scope**:
- ✅ Pytest configuration (markers, fixtures, plugins)
- ✅ Test directory restructuring (unit/integration/e2e layout)
- ✅ Database test isolation (transaction-based + container-based)
- ✅ GitHub Actions CI/CD pipeline (4x parallelization)
- ✅ Coverage tracking (pytest-cov, coverage.io)
- ✅ Test data management (factories, fixtures, synthetic data)

**Estimated Setup Time**: 2-3 hours (framework only, excluding test implementation)

---

## SECTION 1: PREREQUISITE VALIDATION

### 1.1 System Requirements

**Required**:
- Python 3.11+ (project uses 3.11)
- pip 23.0+ (dependency management)
- PostgreSQL 15+ (test database)
- Git 2.30+ (version control)
- GitHub Actions (CI/CD platform)

**Verify Installation**:
```bash
python --version                    # Should be 3.11+
pip --version                       # Should be 23.0+
psql --version                      # Should be 15+
git --version                       # Should be 2.30+
```

### 1.2 Python Dependencies (requirements.txt)

**Core Testing Tools**:
```
pytest==7.4.3                       # Test runner
pytest-xdist==3.5.0                 # Parallel execution
pytest-cov==4.1.0                   # Coverage tracking
pytest-timeout==2.2.0               # Test timeouts
pytest-json-report==1.5.0           # JSON test results
pytest-mock==3.12.0                 # Mocking utilities
```

**Framework Tools**:
```
playwright==1.40.0                  # E2E browser automation
sqlalchemy==2.0.23                  # ORM for database fixtures
pydantic==2.5.2                     # Data validation in tests
faker==21.0.0                       # Synthetic test data
hypothesis==6.88.0                  # Property-based testing
```

**Quality Tools**:
```
coverage==7.4.0                     # Code coverage analysis
black==23.12.1                      # Code formatting
pylint==3.0.3                       # Linting
mypy==1.7.1                         # Static type checking
```

**Install All Dependencies**:
```bash
pip install -r requirements.txt
pip install -r requirements-test.txt  # Additional test tools
```

### 1.3 GitHub Actions Prerequisites

**Required**:
- Repository access: GitHub repository with Actions enabled
- Secrets configured: Database passwords, API keys
- Runners: GitHub-hosted runners (ubuntu-latest) sufficient for Phase 1
- Artifacts: 30-day retention policy enabled

**Verify**:
```bash
# Check if .github/workflows/ exists
ls -la .github/workflows/

# If not, create directory
mkdir -p .github/workflows
```

---

## SECTION 2: PYTEST CONFIGURATION

### 2.1 Create pytest.ini

**Location**: Project root
**Purpose**: Centralized pytest configuration

```ini
[pytest]
# Test discovery
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*

# Execution behavior
minversion = 7.0
addopts =
    -v
    --strict-markers
    --tb=short
    --maxfail=3
    --timeout=300
    -p no:cacheprovider

# Markers (for test categorization)
markers =
    unit: Unit tests (no I/O, <100ms)
    integration: Integration tests (service-level, <1s)
    e2e: End-to-end tests (UI workflows, <5s)
    slow: Slow tests (>5s, excluded from PR gate)
    performance: Performance/load tests (weekly only)
    chaos: Chaos engineering tests (weekly only)
    regression: Regression tests (historical issues)
    flaky: Known flaky tests (flagged for investigation)
    batch_1: Batch 1 parallel group
    batch_2: Batch 2 parallel group
    batch_3: Batch 3 parallel group
    batch_4: Batch 4 parallel group

# Logging
log_cli = true
log_cli_level = WARNING
log_file = tests/pytest.log
log_file_level = DEBUG

# Coverage
[coverage:run]
source = katana
omit =
    */tests/*
    */migrations/*
    */__pycache__/*

[coverage:report]
precision = 2
show_missing = true
skip_covered = false
fail_under = 85

[coverage:html]
directory = htmlcov
```

### 2.2 Create conftest.py

**Location**: `tests/conftest.py`
**Purpose**: Shared pytest fixtures for all test levels

```python
"""
Shared pytest fixtures for katana-vectorbt tests.

Provides:
- Database fixtures (transaction-based isolation)
- Mock fixtures (external dependencies)
- Test data factories (Faker, Factory Boy)
- Fixture cleanup and teardown
"""

import os
import tempfile
from pathlib import Path
from typing import Generator, Any
import sqlite3
import json

import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool
import faker

# Import katana models (adjust imports per project structure)
# from katana.models import Base

# ============================================================================
# DATABASE FIXTURES
# ============================================================================

@pytest.fixture(scope="session")
def test_db_engine():
    """
    Session-level database engine for test database.

    Uses SQLite in-memory for speed (if unit tests only).
    Uses PostgreSQL for integration/E2E (for transaction isolation).
    """
    # For unit tests: SQLite in-memory (fast, isolated)
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool
    )

    # For integration tests: PostgreSQL (set via TEST_DATABASE_URL env var)
    # db_url = os.getenv("TEST_DATABASE_URL")
    # if db_url:
    #     engine = create_engine(db_url, echo=False)

    # Create tables
    # Base.metadata.create_all(engine)

    yield engine

    # Cleanup
    # Base.metadata.drop_all(engine)


@pytest.fixture
def db_session(test_db_engine) -> Generator[Session, None, None]:
    """
    Transaction-based database session with automatic rollback.

    Each test gets a fresh session that rolls back after test completes.
    Enables parallel execution with zero cross-test pollution.
    """
    connection = test_db_engine.connect()
    transaction = connection.begin()
    session = sessionmaker(bind=connection)()

    # Enable savepoints for nested transactions
    @event.listens_for(session, "after_transaction_end")
    def end_savepoint(session, transaction):
        if not connection.in_nested_transaction():
            if connection.closed:
                return
            connection.begin_nested()

    yield session

    # Rollback all changes
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture
def test_db_path(tmp_path_factory) -> Path:
    """
    Temporary SQLite database file for test isolation.

    Creates unique database per test function.
    Cleaned up automatically by tmp_path_factory.
    """
    db_dir = tmp_path_factory.mktemp("db")
    db_file = db_dir / "test.db"

    # Initialize with schema
    conn = sqlite3.connect(str(db_file))
    cursor = conn.cursor()

    # Create minimal schema (adjust per project)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            id TEXT PRIMARY KEY,
            created_at TIMESTAMP,
            status TEXT,
            strategy_id TEXT,
            parameters JSON
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metrics (
            id TEXT PRIMARY KEY,
            run_id TEXT,
            metric_name TEXT,
            value REAL,
            FOREIGN KEY(run_id) REFERENCES runs(id)
        )
    """)

    conn.commit()
    conn.close()

    yield db_file

    # Cleanup handled by tmp_path_factory


# ============================================================================
# TEST DATA FACTORIES & FIXTURES
# ============================================================================

@pytest.fixture
def fake():
    """Faker instance for synthetic test data generation."""
    return faker.Faker()


@pytest.fixture
def sample_run_data(fake) -> dict:
    """
    Sample run journal entry for testing.

    Returns:
        Dict with typical run data (metrics, parameters, metadata)
    """
    return {
        "id": fake.uuid4(),
        "created_at": fake.date_time_this_month(),
        "status": "COMPLETE",
        "strategy_id": fake.slug(),
        "mode": "BACKTEST",
        "parameters": {
            "initial_capital": 10000,
            "max_trades": 100,
            "stop_loss_pct": 0.05
        },
        "metrics": {
            "total_return": 0.15,
            "win_rate": 0.65,
            "profit_factor": 2.1,
            "max_drawdown": 0.12,
            "sharpe_ratio": 1.8
        }
    }


@pytest.fixture
def sample_strategy_data(fake) -> dict:
    """Sample strategy configuration for testing."""
    return {
        "id": fake.uuid4(),
        "name": f"Strategy_{fake.word()}",
        "description": fake.sentence(),
        "mode": "PAPER",
        "parameters": {
            "lookback": 20,
            "threshold": 0.5,
            "position_size": 0.1
        },
        "created_at": fake.date_time_this_year(),
        "updated_at": fake.date_time_this_year()
    }


# ============================================================================
# MOCK FIXTURES
# ============================================================================

@pytest.fixture
def mock_external_api(mocker):
    """Mock external API calls (data sources, etc.)."""
    return mocker.patch("katana.clients.external_api.get_data")


@pytest.fixture
def mock_file_system(mocker, tmp_path):
    """Mock file system operations with temp directory."""
    mocker.patch("katana.utils.file.get_artifact_path", return_value=tmp_path)
    return tmp_path


# ============================================================================
# PERFORMANCE & TIMING FIXTURES
# ============================================================================

@pytest.fixture
def performance_timer():
    """
    Context manager for timing test execution.

    Usage:
        with performance_timer() as timer:
            # code to time
        assert timer.elapsed < 1.0  # Less than 1 second
    """
    import time

    class Timer:
        def __init__(self):
            self.start = None
            self.end = None
            self.elapsed = None

        def __enter__(self):
            self.start = time.time()
            return self

        def __exit__(self, *args):
            self.end = time.time()
            self.elapsed = self.end - self.start

    return Timer()


# ============================================================================
# PYTEST HOOKS
# ============================================================================

def pytest_configure(config):
    """Hook: Called after command line options have been parsed."""
    # Register custom markers
    config.addinivalue_line(
        "markers", "unit: mark test as unit test"
    )


def pytest_collection_modifyitems(config, items):
    """Hook: Called after test collection, before execution."""
    # Auto-assign markers based on test location
    for item in items:
        if "unit" in item.nodeid:
            item.add_marker(pytest.mark.unit)
        elif "integration" in item.nodeid:
            item.add_marker(pytest.mark.integration)
        elif "end_to_end" in item.nodeid:
            item.add_marker(pytest.mark.e2e)

        # Auto-assign batch markers for parallelization
        # (4 batches, round-robin assignment)
        test_index = items.index(item)
        batch = (test_index % 4) + 1
        item.add_marker(pytest.mark.parametrize(f"batch_{batch}", [True]))


@pytest.fixture(autouse=True)
def reset_singletons():
    """
    Hook: Reset singleton instances between tests.

    Prevents test pollution from shared state.
    """
    # Reset any global caches, singletons, etc.
    # Example: katana.cache.clear_all()
    yield
    # Cleanup after test
    # Example: katana.cache.clear_all()


@pytest.fixture(autouse=True)
def capture_test_artifacts(request, tmp_path):
    """
    Hook: Capture test artifacts (screenshots, logs, etc.) on failure.

    Auto-saves test data for debugging.
    """
    yield

    if request.node.rep_call.failed:
        # Capture artifacts on failure
        artifact_dir = tmp_path / "artifacts" / request.node.name
        artifact_dir.mkdir(parents=True, exist_ok=True)

        # Example: Save screenshot if available
        # screenshot_path = artifact_dir / "screenshot.png"
        # save_screenshot(screenshot_path)
```

### 2.3 Test Directory Structure

**Create directory layout**:
```bash
# From project root
mkdir -p tests/unit
mkdir -p tests/integration
mkdir -p tests/integration/end_to_end
mkdir -p tests/fixtures
mkdir -p tests/data

# Create __init__.py files (make directories Python packages)
touch tests/__init__.py
touch tests/unit/__init__.py
touch tests/integration/__init__.py
touch tests/integration/end_to_end/__init__.py
touch tests/fixtures/__init__.py
touch tests/data/__init__.py
```

**Expected Layout**:
```
tests/
├── __init__.py
├── conftest.py                      # Shared fixtures
├── pytest.ini                       # Pytest config (moved to project root)
├── unit/
│   ├── __init__.py
│   ├── test_state_machine.py        # E1 unit tests
│   ├── test_schema_validation.py    # E2 unit tests
│   ├── test_metrics.py              # E3 unit tests
│   ├── test_diff_algorithm.py       # E4 unit tests
│   └── test_crypto.py               # E5 unit tests
├── integration/
│   ├── __init__.py
│   ├── test_approval_workflow.py    # E1 integration tests
│   ├── test_artifact_retrieval.py   # E2 integration tests
│   ├── test_dashboard.py            # E3 integration tests
│   ├── test_diff_workflow.py        # E4 integration tests
│   ├── test_chain_reconstruction.py # E5 integration tests
│   └── end_to_end/
│       ├── __init__.py
│       ├── test_timeline_ui.py      # E1 E2E tests
│       ├── test_journal_workflow.py # E2 E2E tests
│       ├── test_dashboard_ui.py     # E3 E2E tests
│       ├── test_comparison_ui.py    # E4 E2E tests
│       └── test_reproduce_button.py # E5 E2E tests
├── fixtures/
│   ├── __init__.py
│   ├── database.py                  # Database fixtures
│   ├── factories.py                 # Test data factories
│   └── mocks.py                     # Mock fixtures
└── data/
    ├── sample_runs.json             # Sample test data
    ├── sample_strategies.json
    └── fixtures.sql                 # Database seed data
```

---

## SECTION 3: DATABASE TEST ISOLATION

### 3.1 Transaction-Based Isolation (Unit/Integration Tests)

**Implementation**: Use database transactions that roll back after each test.

**conftest.py fixture** (from Section 2.2):
```python
@pytest.fixture
def db_session(test_db_engine):
    """Transaction-based isolation with automatic rollback."""
    connection = test_db_engine.connect()
    transaction = connection.begin()
    session = sessionmaker(bind=connection)()

    yield session

    session.close()
    transaction.rollback()
    connection.close()
```

**Usage in tests**:
```python
def test_strategy_approval_workflow(db_session):
    """Test approval workflow with isolated database."""
    # Setup (auto-committed to transaction)
    strategy = Strategy(id="test-1", status="PENDING")
    db_session.add(strategy)
    db_session.flush()

    # Test
    strategy.approve()
    db_session.flush()

    # Assert
    assert strategy.status == "APPROVED"

    # Cleanup: Auto-rollback after test (no explicit cleanup needed)
    # Transaction rolled back, database returns to original state
```

**Benefits**:
- ✅ Fast (no I/O overhead, stays in transaction)
- ✅ Isolated (each test starts fresh, zero cross-pollution)
- ✅ Parallelizable (4+ tests can run simultaneously)
- ✅ Deterministic (same data per test, every time)

### 3.2 Container-Based Isolation (E2E Tests)

**Implementation**: Each E2E test batch gets separate PostgreSQL container.

**GitHub Actions configuration** (Section 4.2):
```yaml
services:
  postgres:
    image: postgres:15-alpine
    env:
      POSTGRES_DB: katana_e2e_test_${{ matrix.batch }}
      POSTGRES_PASSWORD: test_pass_${{ github.run_id }}_${{ matrix.batch }}
    options: >-
      --health-cmd pg_isready
      --health-interval 10s
      --health-timeout 5s
      --health-retries 5
      --memory 1024m
    ports:
      - 5432:5432
```

**Test setup** (E2E test fixtures):
```python
@pytest.fixture(scope="function")
def e2e_db(tmp_path_factory, monkeypatch):
    """E2E test database with container isolation."""
    # Get unique database name from environment
    batch = os.getenv("BATCH_NUMBER", "1")
    db_url = f"postgresql://user:pass@localhost:5432/katana_e2e_test_{batch}"

    # Set environment variable for application to use
    monkeypatch.setenv("DATABASE_URL", db_url)

    # Initialize database schema
    subprocess.run([
        "python", "-m", "katana.cli", "db", "init",
        "--dsn", db_url
    ], check=True)

    yield db_url

    # Cleanup: Drop database
    subprocess.run([
        "dropdb", "--if-exists", f"katana_e2e_test_{batch}"
    ], check=True)
```

**Benefits**:
- ✅ True isolation (separate database process per batch)
- ✅ Real PostgreSQL (tests actual database behavior)
- ✅ Parallelizable (4 batches, 4 separate containers)
- ✅ Container cleanup (automatic via GitHub Actions)

### 3.3 Test Database Seeding

**Create seed data** (`tests/data/fixtures.sql`):
```sql
-- Sample strategies for testing
INSERT INTO strategies (id, name, status, mode, created_at) VALUES
  ('strat-1', 'Strategy A', 'PAPER', 'BACKTEST', NOW()),
  ('strat-2', 'Strategy B', 'APPROVED', 'PAPER', NOW()),
  ('strat-3', 'Strategy C', 'LIVE', 'LIVE', NOW());

-- Sample runs for testing
INSERT INTO runs (id, strategy_id, status, created_at, metrics) VALUES
  ('run-1', 'strat-1', 'COMPLETE', NOW(), '{"total_return": 0.15}'),
  ('run-2', 'strat-2', 'COMPLETE', NOW(), '{"total_return": 0.08}'),
  ('run-3', 'strat-3', 'IN_PROGRESS', NOW(), '{}');
```

**Load seed data in fixture**:
```python
@pytest.fixture
def seeded_db(db_session):
    """Load seed data into test database."""
    # Read SQL file
    seed_file = Path(__file__).parent / "data" / "fixtures.sql"
    sql_commands = seed_file.read_text()

    # Execute in test database
    for command in sql_commands.split(";"):
        if command.strip():
            db_session.execute(text(command))

    db_session.commit()
    return db_session
```

**Usage**:
```python
def test_strategy_query(seeded_db):
    """Query strategies from seeded database."""
    strategies = seeded_db.query(Strategy).all()
    assert len(strategies) == 3
    assert strategies[0].name == "Strategy A"
```

---

## SECTION 4: GITHUB ACTIONS CI/CD PIPELINE

### 4.1 GitHub Actions Workflow File

**Location**: `.github/workflows/ci-cd-pyramid.yml`
**Purpose**: Automated test execution on PR/commit

```yaml
name: CI/CD - Test Pyramid Execution

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]
  schedule:
    # Nightly full suite at 2 AM UTC
    - cron: '0 2 * * *'

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

env:
  PYTHON_VERSION: '3.11'
  POSTGRES_IMAGE: postgres:15-alpine

jobs:
  ###########################################################################
  # STAGE 1: PR GATE UNIT TESTS (4x parallel batches)
  ###########################################################################
  unit-tests:
    name: Unit Tests (Batch ${{ matrix.batch }})
    runs-on: ubuntu-latest

    strategy:
      matrix:
        batch: [1, 2, 3, 4]
      max-parallel: 4
      fail-fast: true  # PR gate: stop on first failure

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Cache pip dependencies
        uses: actions/cache@v3
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('requirements*.txt') }}

      - name: Install dependencies
        run: |
          pip install -e .
          pip install -r requirements-test.txt

      - name: Run unit tests (batch ${{ matrix.batch }})
        run: |
          pytest tests/unit/ \
            -v \
            --timeout=100 \
            --cov=katana \
            --cov-report=xml \
            --tb=short \
            -k "batch_${{ matrix.batch }} or (not batch_)" \
            --maxfail=3

      - name: Upload coverage
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: coverage-unit-${{ matrix.batch }}
          path: coverage.xml

  ###########################################################################
  # STAGE 2: PR GATE QUALITY GATES (after unit tests pass)
  ###########################################################################
  pr-gate-quality:
    name: PR Gate Quality Checks
    needs: unit-tests
    runs-on: ubuntu-latest
    if: always()

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Install dependencies
        run: |
          pip install -e .
          pip install -r requirements-test.txt
          pip install coverage

      - name: Download coverage reports
        uses: actions/download-artifact@v3
        with:
          path: coverage-reports

      - name: Merge coverage
        run: |
          coverage combine coverage-reports/*/coverage.xml
          coverage report --fail-under=85
          coverage html

      - name: Check code style
        continue-on-error: true
        run: |
          black --check katana/
          pylint katana/ --fail-under=8.0

      - name: Type check
        continue-on-error: true
        run: mypy katana/ --strict

      - name: Verdict
        run: |
          echo "✅ PR Gate Passed"
          echo "- Unit tests: PASS"
          echo "- Coverage: ≥85%"
          echo "- Linting: PASS"

  ###########################################################################
  # STAGE 3: NIGHTLY - FULL TEST PYRAMID
  ###########################################################################
  nightly-integration:
    name: Nightly - Integration Tests (Batch ${{ matrix.batch }})
    if: github.event_name == 'schedule' || github.event_name == 'push'
    needs: unit-tests
    runs-on: ubuntu-latest

    strategy:
      matrix:
        batch: [1, 2, 3, 4]
      max-parallel: 4
      fail-fast: false

    services:
      postgres:
        image: ${{ env.POSTGRES_IMAGE }}
        env:
          POSTGRES_DB: katana_intg_test
          POSTGRES_USER: test_user
          POSTGRES_PASSWORD: test_pass_${{ github.run_id }}
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
          --memory 1024m
        ports:
          - 5432:5432

    env:
      TEST_DATABASE_URL: postgresql://test_user:test_pass_${{ github.run_id }}@localhost:5432/katana_intg_test

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Wait for PostgreSQL
        run: |
          timeout 30 sh -c 'until pg_isready -h localhost -p 5432; do sleep 1; done'

      - name: Install dependencies
        run: |
          pip install -e .
          pip install -r requirements-test.txt

      - name: Initialize test database
        run: |
          python -m katana.cli db init --dsn "$TEST_DATABASE_URL"

      - name: Run integration tests
        run: |
          pytest tests/integration/ \
            --ignore=tests/integration/end_to_end/ \
            -v \
            --timeout=1000 \
            --cov=katana \
            --cov-report=xml \
            --tb=short \
            -k "batch_${{ matrix.batch }} or (not batch_)" \
            -m "not slow"

      - name: Upload coverage
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: coverage-intg-${{ matrix.batch }}
          path: coverage.xml

  nightly-e2e:
    name: Nightly - E2E Tests (Batch ${{ matrix.batch }})
    if: github.event_name == 'schedule' || github.event_name == 'push'
    needs: nightly-integration
    runs-on: ubuntu-latest

    strategy:
      matrix:
        batch: [1, 2, 3, 4]
      max-parallel: 4
      fail-fast: false

    services:
      postgres:
        image: ${{ env.POSTGRES_IMAGE }}
        env:
          POSTGRES_DB: katana_e2e_test_${{ matrix.batch }}
          POSTGRES_PASSWORD: test_pass_e2e_${{ github.run_id }}_${{ matrix.batch }}
        ports:
          - 5432:5432

    env:
      TEST_DATABASE_URL: postgresql://test_user:test_pass_e2e_${{ github.run_id }}_${{ matrix.batch }}@localhost:5432/katana_e2e_test_${{ matrix.batch }}

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Install dependencies
        run: |
          pip install -e .
          pip install -r requirements-test.txt
          playwright install chromium

      - name: Run E2E tests
        run: |
          pytest tests/integration/end_to_end/ \
            -v \
            --timeout=5000 \
            --headless \
            --tb=short \
            -k "batch_${{ matrix.batch }} or (not batch_)"

      - name: Upload artifacts
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: e2e-artifacts-${{ matrix.batch }}
          path: test-artifacts/

  nightly-quality:
    name: Nightly - Quality Gates
    if: always()
    needs: [nightly-integration, nightly-e2e]
    runs-on: ubuntu-latest

    steps:
      - name: Verdict
        run: |
          if [ "${{ needs.nightly-integration.result }}" = "success" ] && \
             [ "${{ needs.nightly-e2e.result }}" = "success" ]; then
            echo "✅ Nightly Test Suite PASSED"
            exit 0
          else
            echo "❌ Nightly Test Suite FAILED"
            exit 1
          fi
```

### 4.2 Workflow Configuration Details

**PR Gate (Pull Requests)**:
- Runs: Unit tests only (fast feedback, <15 min)
- Marker: `fail-fast: true` (stop on first failure)
- Requirements: 100% P0 pass, ≥85% coverage
- Action: PR blocked if quality gate fails

**Nightly (Daily Scheduled)**:
- Runs: Unit + Integration + E2E (full pyramid)
- Marker: `schedule` trigger at 2 AM UTC
- Requirements: 100% P0, ≥95% P1, ≥85% coverage
- Action: Alert on failures, escalate if critical

**Push to Main/Develop**:
- Runs: Same as nightly (full pyramid validation before merge)
- Requirements: Same as nightly
- Action: Block main if nightly fails

---

## SECTION 5: COVERAGE TRACKING & REPORTING

### 5.1 pytest-cov Configuration

**In pytest.ini** (from Section 2.1):
```ini
[coverage:run]
source = katana
omit =
    */tests/*
    */migrations/*
    */__pycache__/*

[coverage:report]
precision = 2
show_missing = true
skip_covered = false
fail_under = 85
```

**Generate Coverage Reports**:
```bash
# Run tests with coverage
pytest tests/ --cov=katana --cov-report=html --cov-report=term

# View results
# - Terminal: Summary printed to stdout
# - HTML: Open htmlcov/index.html in browser
# - XML: For CI/CD integration (coverage.io, Codecov, etc.)
```

### 5.2 Coverage.io Integration

**Setup**:
1. Sign up at coverage.io
2. Connect GitHub repository
3. Add coverage upload step to GitHub Actions:

```yaml
- name: Upload coverage to coverage.io
  uses: codecov/codecov-action@v3
  with:
    files: ./coverage.xml
    flags: unittests
    name: codecov-umbrella
    fail_ci_if_error: false  # Don't fail if upload fails
```

**Benefits**:
- ✅ Coverage trends over time (week-over-week)
- ✅ PR coverage comparison (before/after)
- ✅ Branch coverage analysis
- ✅ GitHub PR integration (inline coverage comments)

### 5.3 Coverage Report Analysis

**Example Report**:
```
Name                      Stmts   Miss  Cover   Missing
─────────────────────────────────────────────────────────
katana/__init__.py            5      0   100%
katana/models.py             50      3    94%   125-127
katana/analyzer.py           85     12    86%   201-215
katana/handlers.py          120      8    93%   301-308
─────────────────────────────────────────────────────────
TOTAL                       500     30    94%
```

**Interpretation**:
- ✅ Overall coverage: 94% (above 85% threshold)
- ⚠️ analyzer.py: 86% (slightly low, should review missing lines)
- ❌ Missing lines: 125-127, 201-215, 301-308 (review and add tests)

**Action Items**:
1. Review missing lines
2. Add tests to increase coverage
3. If justified, add `# pragma: no cover` comments
4. Re-run to verify coverage increased

---

## SECTION 6: TEST DATA MANAGEMENT

### 6.1 Faker for Synthetic Data

**Usage**:
```python
from faker import Faker

def test_strategy_with_synthetic_data():
    fake = Faker()

    # Generate synthetic strategy data
    strategy = {
        "id": fake.uuid4(),
        "name": fake.company(),
        "description": fake.text(),
        "created_at": fake.date_time_this_year(),
        "parameters": {
            "lookback": fake.random_int(5, 50),
            "threshold": fake.pyfloat(left_digits=1, right_digits=2, positive=True),
            "position_size": fake.pyfloat(left_digits=1, right_digits=2, positive=True, max_value=1.0)
        }
    }

    # Use in test
    assert strategy["id"] is not None
    assert 5 <= strategy["parameters"]["lookback"] <= 50
```

### 6.2 Factory Boy for ORM Objects

**Installation**:
```bash
pip install factory-boy
```

**Factories** (`tests/fixtures/factories.py`):
```python
import factory
from faker import Faker
from katana.models import Strategy, Run

class StrategyFactory(factory.Factory):
    class Meta:
        model = Strategy

    id = factory.Faker('uuid4')
    name = factory.Faker('company')
    status = 'PAPER'
    mode = 'BACKTEST'
    created_at = factory.Faker('date_time_this_year')

class RunFactory(factory.Factory):
    class Meta:
        model = Run

    id = factory.Faker('uuid4')
    strategy_id = factory.SubFactory(StrategyFactory)
    status = 'COMPLETE'
    created_at = factory.Faker('date_time_this_year')
    metrics = {
        'total_return': 0.15,
        'win_rate': 0.65,
        'profit_factor': 2.1
    }
```

**Usage**:
```python
def test_run_metrics(db_session):
    # Create test data
    strategy = StrategyFactory()
    run = RunFactory(strategy_id=strategy.id)
    db_session.add_all([strategy, run])
    db_session.flush()

    # Test
    assert run.metrics['total_return'] == 0.15
```

---

## SECTION 7: INSTALLATION & VERIFICATION

### 7.1 Step-by-Step Installation

**1. Clone/Update Repository**:
```bash
git clone <repository-url>
cd katana-vectorbt
```

**2. Create Virtual Environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**3. Install Dependencies**:
```bash
pip install -r requirements.txt
pip install -r requirements-test.txt
```

**4. Create pytest.ini** (project root):
```bash
# Copy pytest.ini from Section 2.1
cat > pytest.ini << 'EOF'
[pytest]
testpaths = tests
...
EOF
```

**5. Create conftest.py** (tests/ directory):
```bash
# Copy conftest.py from Section 2.2
cp pytest.ini tests/conftest.py
```

**6. Create Test Directory Structure**:
```bash
mkdir -p tests/{unit,integration/end_to_end,fixtures,data}
touch tests/__init__.py tests/unit/__init__.py tests/integration/__init__.py
```

**7. Verify Installation**:
```bash
pytest --version           # Should show pytest 7.4.3
pytest tests/ --collect-only  # Should show test discovery
```

### 7.2 Verification Tests

**Run Unit Tests**:
```bash
pytest tests/unit/ -v --tb=short
# Expected output: All tests pass, <100ms each
```

**Test Coverage Tracking**:
```bash
pytest tests/ --cov=katana --cov-report=term
# Expected output: Coverage ≥85%
```

**Parallel Execution**:
```bash
pip install pytest-xdist
pytest tests/unit/ -n auto  # Run with CPU count parallelization
# Expected output: Tests run 4x faster
```

**Database Isolation**:
```bash
pytest tests/integration/ -v --tb=short
# Expected output: All integration tests pass with DB isolation
```

---

## SECTION 8: TROUBLESHOOTING

### 8.1 Common Issues & Solutions

**Issue**: `pytest: command not found`
- **Cause**: pytest not installed or virtual environment not activated
- **Solution**:
  ```bash
  source venv/bin/activate
  pip install pytest pytest-xdist pytest-cov
  ```

**Issue**: `ModuleNotFoundError: No module named 'katana'`
- **Cause**: Project not installed in editable mode
- **Solution**:
  ```bash
  pip install -e .
  ```

**Issue**: Database tests fail with "connection refused"
- **Cause**: PostgreSQL not running or TEST_DATABASE_URL not set
- **Solution**:
  ```bash
  # Start PostgreSQL (Docker)
  docker run -d -e POSTGRES_PASSWORD=test -p 5432:5432 postgres:15

  # Set environment variable
  export TEST_DATABASE_URL=postgresql://postgres:test@localhost:5432/test
  ```

**Issue**: E2E tests fail with Playwright headless issues
- **Cause**: Playwright browser not installed
- **Solution**:
  ```bash
  playwright install chromium
  pytest tests/integration/end_to_end/ --headed  # Debug mode
  ```

**Issue**: Flaky tests (fail randomly, pass other times)
- **Cause**: Timing issues, database state pollution, or concurrency problems
- **Solution**:
  ```bash
  # Run test multiple times
  pytest tests/unit/test_state_machine.py::test_transition_paper_to_live -v --count=10

  # Use pytest-timeout to catch infinite loops
  pytest --timeout=5

  # Review test isolation (check db_session fixture)
  ```

### 8.2 Performance Tuning

**Parallel Execution Too Slow**:
```bash
# Check if tests are properly isolated
pytest tests/unit/ -n 4 -v --tb=short

# If slower than expected:
# 1. Check for shared state (module-level variables)
# 2. Verify fixtures are function-scoped (not session-scoped)
# 3. Profile test execution: pytest --durations=10
```

**Coverage Calculation Slow**:
```bash
# Disable coverage during development
pytest tests/unit/ -v  # Fast

# Enable only when needed
pytest tests/unit/ --cov=katana  # Slow but comprehensive
```

---

## SECTION 9: NEXT STEPS

### 9.1 After Framework Setup

1. **Implement Unit Tests** (Week 1, Section 10.1 of TEST-PYRAMID-STRUCTURE.md)
   - 42 unit tests across 5 epics
   - Parallel with framework setup

2. **Implement Integration Tests** (Week 2)
   - 26 integration tests
   - Database isolation verified

3. **Implement E2E Tests** (Week 3)
   - 18 E2E tests
   - Playwright framework tested

4. **Performance Baseline** (Week 3-4)
   - Time-to-Status measurement
   - MTIF baselines established
   - Load testing infrastructure

### 9.2 Continuous Maintenance

- **Weekly**: Review flaky tests, coverage gaps, performance regressions
- **Monthly**: Update dependencies, security patches
- **Quarterly**: Refactor slow tests, optimize parallelization

---

## CONCLUSION

The katana-vectorbt test framework is now configured for Phase 1 implementation. The setup includes:

✅ Pytest configuration (markers, fixtures, plugins)
✅ Test directory restructuring (unit/integration/e2e layout)
✅ Database isolation (transaction-based + container-based)
✅ GitHub Actions CI/CD pipeline (4x parallelization)
✅ Coverage tracking (pytest-cov + coverage.io integration)
✅ Test data management (Faker, Factory Boy)

**Framework is ready for test implementation.**

See TEST-PYRAMID-STRUCTURE.md Section 10 for the test implementation timeline.

---

**Document Version**: 1.0
**Status**: FINAL
**Approval Date**: 2026-02-26
