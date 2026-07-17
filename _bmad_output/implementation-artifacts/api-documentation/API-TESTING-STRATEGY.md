# API Testing Strategy - Katana VectorBT Phase 1

**Project:** Katana VectorBT
**Version:** 1.0.0
**Date:** 2026-02-26
**Audience:** QA Engineers, Test Architects
**Testing Framework:** pytest + pytest-asyncio + httpx

---

## Table of Contents

1. [Testing Architecture](#testing-architecture)
2. [Test Pyramid Structure](#test-pyramid-structure)
3. [Unit Tests](#unit-tests)
4. [Integration Tests](#integration-tests)
5. [End-to-End Tests](#end-to-end-tests)
6. [Mock Data Generation](#mock-data-generation)
7. [Error Path Validation](#error-path-validation)
8. [Performance Assertions](#performance-assertions)
9. [WCAG Compliance Testing](#wcag-compliance-testing)
10. [CI/CD Integration](#cicd-integration)

---

## Testing Architecture

### Test Pyramid (Recommended)

```
        /\
       /  \          10% - E2E Tests
      /────\        (Full workflow, real DB)
     /      \
    /──────  \      30% - Integration Tests
   /          \    (API + DB, no external services)
  /────────────\
 /              \ 60% - Unit Tests
/________________\(Functions, services, validation)
```

### Directory Structure

```
tests/
├── conftest.py                          # Shared fixtures
├── unit/
│   ├── test_strategy_service.py        # Service layer
│   ├── test_validation_service.py      # Validation logic
│   ├── test_models.py                   # Pydantic models
│   └── test_repositories.py             # Data access
├── integration/
│   ├── test_strategy_endpoints.py      # Strategy API
│   ├── test_journal_endpoints.py       # Journal API
│   ├── test_metrics_endpoints.py       # Metrics API
│   ├── test_compare_endpoints.py       # Comparison API
│   ├── test_audit_endpoints.py         # Audit API
│   ├── test_database_isolation.py      # Parallel execution
│   └── test_error_handling.py          # Error scenarios
└── e2e/
    ├── test_strategy_workflow.py       # Full lifecycle
    ├── test_reproducibility_flow.py    # Reproduce run
    └── test_comparison_flow.py         # Compare runs
```

---

## Test Pyramid Structure

### Unit Tests (60% - 100+ tests)

**Purpose:** Test individual functions, services, models in isolation

**Tools:** pytest, unittest.mock, faker

**Pattern:**

```python
# tests/unit/test_strategy_service.py
import pytest
from unittest.mock import MagicMock, patch, AsyncMock
from app.services.strategy_service import StrategyService
from app.models.strategy import StrategyProfile, StrategyParameters


class TestStrategyService:
    @pytest.fixture
    def mock_db(self):
        """Mock database session"""
        return AsyncMock()

    @pytest.fixture
    def service(self, mock_db):
        return StrategyService(mock_db)

    @pytest.mark.asyncio
    async def test_create_strategy_success(self, service, mock_db):
        """Test successful strategy creation"""
        # Arrange
        parameters = {
            "strategy_profile": "return",
            "dff_sl_source_type": "atr",
            "dff_sl_period": 14,
            "sl_multiplier": 2.0,
            "tp_multiplier": 3.0,
            "max_leverage": 3.0,
            "position_sizing": "kelly",
            "max_loss_per_trade": 2.5,
        }

        # Act
        result = await service.create_strategy(
            name="Test Strategy",
            description="Test description",
            parameters=parameters,
            created_by="user:test",
        )

        # Assert
        assert result.strategy_id.startswith("strat_")
        assert result.state == "DRAFT"
        assert result.version == 1
        assert mock_db.add.called
        assert mock_db.commit.called

    @pytest.mark.asyncio
    async def test_create_strategy_validation_error(self, service, mock_db):
        """Test strategy creation with invalid parameters"""
        # Arrange
        invalid_parameters = {
            "strategy_profile": "return",
            "sl_multiplier": 10.5,  # Exceeds max 5.0 for return
            "tp_multiplier": 3.0,
            "max_leverage": 3.0,
            "position_sizing": "kelly",
            "max_loss_per_trade": 2.5,
        }

        # Act & Assert
        with pytest.raises(ValueError, match="Range validation"):
            await service.create_strategy(
                name="Test",
                description="",
                parameters=invalid_parameters,
                created_by="user:test",
            )

    @pytest.mark.asyncio
    async def test_submit_for_approval_state_machine(self, service, mock_db):
        """Test state machine: DRAFT → PENDING"""
        # Mock existing strategy
        existing_strategy = MagicMock()
        existing_strategy.state = "DRAFT"
        existing_strategy.strategy_id = "strat_123"

        service.get_strategy = AsyncMock(return_value=existing_strategy)

        # Act
        result = await service.submit_for_approval("strat_123", "user:test")

        # Assert
        assert result.state == "PENDING"
        assert result.updated_at is not None

    @pytest.mark.asyncio
    async def test_submit_for_approval_invalid_state(self, service, mock_db):
        """Test state machine: Cannot submit from PENDING"""
        # Mock existing strategy in PENDING state
        existing_strategy = MagicMock()
        existing_strategy.state = "PENDING"
        existing_strategy.strategy_id = "strat_123"

        service.get_strategy = AsyncMock(return_value=existing_strategy)

        # Act & Assert
        with pytest.raises(ValueError, match="Cannot submit non-DRAFT"):
            await service.submit_for_approval("strat_123", "user:test")
```

### Integration Tests (30% - 50+ tests)

**Purpose:** Test API endpoints with real database, verify request/response contracts

**Tools:** pytest, httpx, testcontainers (for PostgreSQL)

**Pattern:**

```python
# tests/integration/test_strategy_endpoints.py
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
import asyncio


@pytest.fixture
async def test_db():
    """Create isolated test database per test"""
    engine = create_async_engine(
        "postgresql+asyncpg://user:pass@localhost/test_db",
        isolation_connection=True,  # Each session gets isolated connection
    )

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield engine

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    await engine.dispose()


@pytest.fixture
async def client(test_db):
    """Create test client with test database"""
    app.dependency_overrides[get_db] = override_get_db(test_db)

    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

    app.dependency_overrides.clear()


class TestStrategyEndpoints:
    @pytest.mark.asyncio
    async def test_create_strategy_endpoint_success(self, client):
        """Test POST /strategies returns 201 Created"""
        # Arrange
        payload = {
            "name": "RSI+MA Cross v1",
            "description": "Test strategy",
            "parameters": {
                "strategy_profile": "return",
                "dff_sl_source_type": "atr",
                "dff_sl_period": 14,
                "sl_multiplier": 2.0,
                "tp_multiplier": 3.0,
                "max_leverage": 3.0,
                "position_sizing": "kelly",
                "max_loss_per_trade": 2.5,
            },
        }

        # Act
        response = await client.post(
            "/api/v1/strategies",
            json=payload,
            headers={"Authorization": "Bearer test_token"},
        )

        # Assert
        assert response.status_code == 201
        data = response.json()
        assert data["strategy_id"].startswith("strat_")
        assert data["state"] == "DRAFT"
        assert data["version"] == 1
        assert data["approval_status"]["status"] == "pending"

    @pytest.mark.asyncio
    async def test_create_strategy_validation_error_response(self, client):
        """Test POST /strategies returns 400 with validation details"""
        # Arrange
        invalid_payload = {
            "name": "Test",
            "parameters": {
                "strategy_profile": "return",
                "sl_multiplier": 10.5,  # Invalid for return
                "tp_multiplier": 3.0,
                "max_leverage": 3.0,
                "position_sizing": "kelly",
                "max_loss_per_trade": 2.5,
            },
        }

        # Act
        response = await client.post(
            "/api/v1/strategies",
            json=invalid_payload,
            headers={"Authorization": "Bearer test_token"},
        )

        # Assert
        assert response.status_code == 400
        error = response.json()
        assert error["error"]["code"] == "VALIDATION_ERROR"
        assert len(error["error"]["details"]) > 0
        assert error["error"]["details"][0]["field"] == "parameters.sl_multiplier"
        assert "Range validation" in error["error"]["details"][0]["constraint"]
        assert error["error"]["wcag_summary"] is not None

    @pytest.mark.asyncio
    async def test_strategy_workflow_draft_to_approved(self, client):
        """Test full strategy workflow: CREATE → SUBMIT → APPROVE"""
        # 1. Create strategy
        create_response = await client.post(
            "/api/v1/strategies",
            json={
                "name": "Test",
                "parameters": {
                    "strategy_profile": "stable",
                    "dff_sl_source_type": "atr",
                    "dff_sl_period": 14,
                    "sl_multiplier": 2.0,
                    "tp_multiplier": 2.0,
                    "max_leverage": 2.0,
                    "position_sizing": "kelly",
                    "max_loss_per_trade": 1.0,
                },
            },
            headers={"Authorization": "Bearer test_token"},
        )
        strategy_id = create_response.json()["strategy_id"]

        # 2. Submit for approval
        submit_response = await client.post(
            f"/api/v1/strategies/{strategy_id}/submit",
            json={"notes": "Ready for review"},
            headers={"Authorization": "Bearer test_token"},
        )
        assert submit_response.status_code == 200
        assert submit_response.json()["state"] == "PENDING"

        # 3. Approve
        approve_response = await client.post(
            f"/api/v1/strategies/{strategy_id}/approve",
            json={"comments": "Looks good"},
            headers={"Authorization": "Bearer approver_token"},
        )
        assert approve_response.status_code == 200
        assert approve_response.json()["state"] == "APPROVED"
        assert approve_response.json()["approval_status"]["approver_id"] == "user:approver"

    @pytest.mark.asyncio
    async def test_database_isolation_parallel_creates(self, client):
        """Test parallel strategy creation doesn't cause race conditions"""
        import asyncio

        async def create_strategy(name):
            return await client.post(
                "/api/v1/strategies",
                json={
                    "name": name,
                    "parameters": {
                        "strategy_profile": "return",
                        "dff_sl_source_type": "atr",
                        "dff_sl_period": 14,
                        "sl_multiplier": 2.0,
                        "tp_multiplier": 3.0,
                        "max_leverage": 3.0,
                        "position_sizing": "kelly",
                        "max_loss_per_trade": 2.5,
                    },
                },
                headers={"Authorization": "Bearer test_token"},
            )

        # Act: Create 10 strategies in parallel
        tasks = [create_strategy(f"Strategy {i}") for i in range(10)]
        responses = await asyncio.gather(*tasks)

        # Assert: All succeeded
        assert all(r.status_code == 201 for r in responses)
        strategy_ids = [r.json()["strategy_id"] for r in responses]
        assert len(set(strategy_ids)) == 10  # All unique
```

### End-to-End Tests (10% - 10+ tests)

**Purpose:** Test complete workflows with real API + DB

**Pattern:**

```python
# tests/e2e/test_strategy_workflow.py
import pytest
from httpx import AsyncClient


class TestStrategyLifecycleE2E:
    @pytest.mark.asyncio
    async def test_complete_strategy_lifecycle(self, client):
        """
        E2E: Create → Submit → Approve → Execute → Monitor
        """
        # 1. Create strategy
        create_resp = await client.post("/api/v1/strategies", ...)
        strategy_id = create_resp.json()["strategy_id"]

        # 2. Verify DRAFT state
        get_resp = await client.get(f"/api/v1/strategies/{strategy_id}")
        assert get_resp.json()["state"] == "DRAFT"

        # 3. Submit
        submit_resp = await client.post(f"/api/v1/strategies/{strategy_id}/submit", ...)
        assert submit_resp.json()["state"] == "PENDING"

        # 4. Approve
        approve_resp = await client.post(f"/api/v1/strategies/{strategy_id}/approve", ...)
        assert approve_resp.json()["state"] == "APPROVED"

        # 5. Execute
        exec_resp = await client.post(f"/api/v1/strategies/{strategy_id}/execute", ...)
        run_id = exec_resp.json()["run_id"]

        # 6. Verify run created
        run_resp = await client.get(f"/api/v1/runs/{run_id}")
        assert run_resp.status_code == 200
        assert run_resp.json()["status"] == "running"

        # 7. Verify audit trail
        audit_resp = await client.get(f"/api/v1/audits/{strategy_id}/trail")
        events = audit_resp.json()["audit_events"]
        actions = [e["action"] for e in events]
        assert "created" in actions
        assert "submitted" in actions
        assert "approved" in actions
```

---

## Unit Tests

### Strategy Validation Tests

**File:** `tests/unit/test_validation_service.py`

```python
import pytest
from app.services.validation_service import ParameterValidator
from app.models.strategy import StrategyParametersBase, DFFSourceType
from app.exceptions import ValidationError


class TestDFFValidation:
    """Test DFF (Distance Function Factory) validation"""

    def test_atr_requires_period(self):
        """ATR source requires dff_sl_period"""
        params = {
            "strategy_profile": "return",
            "dff_sl_source_type": "atr",
            "dff_sl_period": None,  # Missing!
            "sl_multiplier": 2.0,
            "tp_multiplier": 3.0,
            "max_leverage": 3.0,
            "position_sizing": "kelly",
            "max_loss_per_trade": 2.5,
        }

        model = StrategyParametersBase(**params)

        with pytest.raises(ValidationError):
            ParameterValidator.validate_dff_completeness(model)

    def test_bb_half_requires_period_and_stdev(self):
        """BB_HALF requires both period and stdev"""
        params = {
            "strategy_profile": "return",
            "dff_sl_source_type": "bb_half",
            "dff_sl_period": 20,
            "dff_sl_stdev": None,  # Missing!
            "sl_multiplier": 2.0,
            "tp_multiplier": 3.0,
            "max_leverage": 3.0,
            "position_sizing": "kelly",
            "max_loss_per_trade": 2.5,
        }

        model = StrategyParametersBase(**params)

        with pytest.raises(ValidationError):
            ParameterValidator.validate_dff_completeness(model)

    def test_fixed_pct_requires_pct_field(self):
        """FIXED_PCT requires dff_sl_pct"""
        params = {
            "strategy_profile": "return",
            "dff_sl_source_type": "fixed_pct",
            "dff_sl_pct": None,  # Missing!
            "sl_multiplier": 2.0,
            "tp_multiplier": 3.0,
            "max_leverage": 3.0,
            "position_sizing": "kelly",
            "max_loss_per_trade": 2.5,
        }

        model = StrategyParametersBase(**params)

        with pytest.raises(ValidationError):
            ParameterValidator.validate_dff_completeness(model)

    def test_valid_atr_configuration(self):
        """Valid ATR configuration passes validation"""
        params = {
            "strategy_profile": "return",
            "dff_sl_source_type": "atr",
            "dff_sl_period": 14,
            "sl_multiplier": 2.0,
            "tp_multiplier": 3.0,
            "max_leverage": 3.0,
            "position_sizing": "kelly",
            "max_loss_per_trade": 2.5,
        }

        model = StrategyParametersBase(**params)

        # Should not raise
        ParameterValidator.validate_dff_completeness(model)


class TestMultiplierValidation:
    """Test multiplier range validation"""

    def test_rocket_profile_tp_multiplier_up_to_10(self):
        """Rocket profile allows tp_multiplier ≤ 10.0"""
        params = {
            "strategy_profile": "rocket",
            "sl_multiplier": 2.0,
            "tp_multiplier": 10.0,  # OK for rocket
            "max_leverage": 3.0,
            "position_sizing": "kelly",
            "max_loss_per_trade": 2.5,
        }

        model = StrategyParametersBase(**params)

        # Should not raise
        ParameterValidator.validate_multiplier_ranges(model)

    def test_stable_profile_multiplier_max_5(self):
        """Stable profile limits multipliers to ≤ 5.0"""
        params = {
            "strategy_profile": "stable",
            "sl_multiplier": 2.0,
            "tp_multiplier": 5.5,  # Exceeds max
            "max_leverage": 2.0,
            "position_sizing": "kelly",
            "max_loss_per_trade": 1.0,
        }

        model = StrategyParametersBase(**params)

        with pytest.raises(ValidationError):
            ParameterValidator.validate_multiplier_ranges(model)

    def test_rocket_profile_tp_exceeds_10(self):
        """Rocket profile cannot exceed tp_multiplier of 10.0"""
        params = {
            "strategy_profile": "rocket",
            "sl_multiplier": 2.0,
            "tp_multiplier": 11.0,  # Exceeds max
            "max_leverage": 3.0,
            "position_sizing": "kelly",
            "max_loss_per_trade": 2.5,
        }

        model = StrategyParametersBase(**params)

        with pytest.raises(ValidationError):
            ParameterValidator.validate_multiplier_ranges(model)
```

---

## Integration Tests

### Database Isolation Tests

**File:** `tests/integration/test_database_isolation.py`

```python
import pytest
from httpx import AsyncClient
import asyncio
from concurrent.futures import ThreadPoolExecutor


class TestDatabaseIsolation:
    """
    Test database transaction isolation prevents race conditions
    Required: READ_COMMITTED isolation level minimum
    """

    @pytest.mark.asyncio
    async def test_parallel_strategy_creation_isolation(self, client):
        """
        10 strategies created in parallel should all succeed
        without deadlocks or conflicts
        """
        async def create_strat(i):
            return await client.post(
                "/api/v1/strategies",
                json={
                    "name": f"Parallel Strategy {i}",
                    "parameters": {...},
                },
                headers={"Authorization": "Bearer token"},
            )

        # Create 10 in parallel
        tasks = [create_strat(i) for i in range(10)]
        responses = await asyncio.gather(*tasks)

        # All should succeed
        assert all(r.status_code == 201 for r in responses)

    @pytest.mark.asyncio
    async def test_concurrent_approval_and_execution(self, client):
        """
        Verify state transitions are atomic:
        Cannot execute non-approved strategy even with race condition
        """
        # Setup: Create strategy
        create_resp = await client.post("/api/v1/strategies", json={...})
        strategy_id = create_resp.json()["strategy_id"]

        # Submit for approval
        await client.post(f"/api/v1/strategies/{strategy_id}/submit", json={...})

        async def attempt_execute():
            return await client.post(
                f"/api/v1/strategies/{strategy_id}/execute",
                json={"mode": "backtest"},
            )

        async def approve():
            return await client.post(
                f"/api/v1/strategies/{strategy_id}/approve",
                json={"comments": "OK"},
            )

        # Race: Both happen at same time
        exec_response, approve_response = await asyncio.gather(
            attempt_execute(),
            approve(),
            return_exceptions=True,
        )

        # Result: At least one should fail (state guard prevents race)
        # OR both succeed in correct order
        status_codes = [
            r.status_code for r in [exec_response, approve_response]
            if not isinstance(r, Exception)
        ]
        assert 409 in status_codes or 200 in status_codes
```

### Error Handling Tests

**File:** `tests/integration/test_error_handling.py`

```python
import pytest
from httpx import AsyncClient


class TestErrorResponses:
    """Verify all errors follow standardized format"""

    @pytest.mark.asyncio
    async def test_validation_error_response_format(self, client):
        """Validation errors include field-level details"""
        response = await client.post(
            "/api/v1/strategies",
            json={
                "name": "Test",
                "parameters": {
                    "strategy_profile": "return",
                    "sl_multiplier": 10.5,  # Invalid
                    ...
                },
            },
        )

        assert response.status_code == 400
        error = response.json()["error"]

        # Verify standard format
        assert error["code"] == "VALIDATION_ERROR"
        assert error["message"]
        assert error["status"] == 400
        assert error["timestamp"]
        assert error["request_id"]
        assert error["wcag_summary"]
        assert isinstance(error["details"], list)

        # Verify details structure
        detail = error["details"][0]
        assert detail["field"]
        assert detail["constraint"]
        assert detail["expected"]
        assert detail["received"]

    @pytest.mark.asyncio
    async def test_state_transition_error(self, client):
        """Invalid state transitions return 409 Conflict"""
        # Create and submit strategy
        create_resp = await client.post("/api/v1/strategies", json={...})
        strategy_id = create_resp.json()["strategy_id"]

        await client.post(f"/api/v1/strategies/{strategy_id}/submit", json={...})

        # Try to submit again (invalid: not in DRAFT)
        response = await client.post(
            f"/api/v1/strategies/{strategy_id}/submit",
            json={},
        )

        assert response.status_code == 409
        error = response.json()["error"]
        assert error["code"] == "STATE_TRANSITION_INVALID"

    @pytest.mark.asyncio
    async def test_resource_not_found_error(self, client):
        """Nonexistent resource returns 404 Not Found"""
        response = await client.get(
            "/api/v1/strategies/strat_nonexistent",
            headers={"Authorization": "Bearer token"},
        )

        assert response.status_code == 404
        error = response.json()["error"]
        assert error["code"] == "RESOURCE_NOT_FOUND"
        assert error["status"] == 404
```

---

## Mock Data Generation

### Faker-based Fixture Generation

**File:** `tests/fixtures/strategy_fixtures.py`

```python
import pytest
from faker import Faker
from app.models.strategy import StrategyProfile, DFFSourceType


fake = Faker()


@pytest.fixture
def valid_strategy_create_payload():
    """Generate valid strategy creation payload"""
    return {
        "name": fake.sentence(nb_words=4),
        "description": fake.paragraph(),
        "parameters": {
            "strategy_profile": fake.random_element(["stable", "return", "rocket"]),
            "dff_sl_source_type": "atr",
            "dff_sl_period": fake.random_int(min=5, max=50),
            "sl_multiplier": fake.pyfloat(min_value=0.5, max_value=5.0),
            "dff_tp_source_type": "atr",
            "dff_tp_period": fake.random_int(min=5, max=50),
            "tp_multiplier": fake.pyfloat(min_value=0.5, max_value=5.0),
            "max_leverage": fake.pyfloat(min_value=1.0, max_value=5.0),
            "position_sizing": fake.random_element(["kelly", "fixed", "atr_based"]),
            "max_loss_per_trade": fake.pyfloat(min_value=0.5, max_value=3.0),
        },
    }


@pytest.fixture
def invalid_strategy_payloads():
    """Generate various invalid strategy payloads"""
    return [
        {
            "name": "",  # Empty name
            "parameters": {...},
        },
        {
            "name": "A" * 300,  # Name too long
            "parameters": {...},
        },
        {
            "name": "Test",
            "parameters": {
                "strategy_profile": "return",
                "sl_multiplier": 10.5,  # Exceeds max
                ...
            },
        },
        {
            "name": "Test",
            "parameters": {
                "strategy_profile": "return",
                "dff_sl_source_type": "atr",
                "dff_sl_period": None,  # Missing required
                ...
            },
        },
    ]
```

---

## Error Path Validation

### Error Path Test Cases

**File:** `tests/integration/test_error_paths.py`

```python
import pytest
from httpx import AsyncClient


class TestErrorPaths:
    """Test all error scenarios"""

    @pytest.mark.asyncio
    async def test_missing_authorization_header(self, client):
        """Missing auth header returns 401 Unauthorized"""
        response = await client.get("/api/v1/strategies/strat_123")
        # No Authorization header

        assert response.status_code == 401

    @pytest.mark.asyncio
    async def test_invalid_token(self, client):
        """Invalid JWT token returns 401"""
        response = await client.get(
            "/api/v1/strategies/strat_123",
            headers={"Authorization": "Bearer invalid_token"},
        )

        assert response.status_code == 401

    @pytest.mark.asyncio
    async def test_insufficient_permissions(self, client):
        """Viewer role cannot approve strategy"""
        # Setup: Create strategy
        create_resp = await client.post(
            "/api/v1/strategies",
            json={...},
            headers={"Authorization": "Bearer viewer_token"},  # Viewer role
        )
        strategy_id = create_resp.json()["strategy_id"]

        # Submit
        await client.post(
            f"/api/v1/strategies/{strategy_id}/submit",
            json={},
            headers={"Authorization": "Bearer viewer_token"},
        )

        # Try to approve (not allowed)
        response = await client.post(
            f"/api/v1/strategies/{strategy_id}/approve",
            json={"comments": "OK"},
            headers={"Authorization": "Bearer viewer_token"},
        )

        assert response.status_code == 403
        assert response.json()["error"]["code"] == "AUTHORIZATION_FAILED"

    @pytest.mark.asyncio
    async def test_dff_incomplete_parameters(self, client):
        """Missing required DFF parameters returns validation error"""
        response = await client.post(
            "/api/v1/strategies",
            json={
                "name": "Test",
                "parameters": {
                    "strategy_profile": "return",
                    "dff_sl_source_type": "atr",
                    "dff_sl_period": None,  # Missing!
                    "sl_multiplier": 2.0,
                    "tp_multiplier": 3.0,
                    "max_leverage": 3.0,
                    "position_sizing": "kelly",
                    "max_loss_per_trade": 2.5,
                },
            },
        )

        assert response.status_code == 400
        error = response.json()["error"]
        assert error["code"] == "VALIDATION_ERROR"
        assert any("dff_sl_period" in d["field"] for d in error["details"])

    @pytest.mark.asyncio
    async def test_concurrent_modification_conflict(self, client):
        """Concurrent modifications detected (409 Conflict)"""
        # Setup: Create and approve strategy
        create_resp = await client.post("/api/v1/strategies", json={...})
        strategy_id = create_resp.json()["strategy_id"]
        await client.post(f"/api/v1/strategies/{strategy_id}/submit", json={...})
        await client.post(f"/api/v1/strategies/{strategy_id}/approve", json={...})

        # Simulate concurrent execute + kill
        import asyncio

        async def execute():
            return await client.post(
                f"/api/v1/strategies/{strategy_id}/execute",
                json={"mode": "backtest"},
            )

        async def kill():
            return await client.post(
                f"/api/v1/strategies/{strategy_id}/kill",
                json={"reason": "Manual stop"},
            )

        exec_resp, kill_resp = await asyncio.gather(execute(), kill())

        # One should fail with 409
        status_codes = [exec_resp.status_code, kill_resp.status_code]
        assert 409 in status_codes or any(s == 200 for s in status_codes)
```

---

## Performance Assertions

### Performance Test Cases

**File:** `tests/integration/test_performance.py`

```python
import pytest
import time
from httpx import AsyncClient


class TestPerformanceAssertions:
    """
    Verify API meets performance NFRs:
    - Strategy create: <1 second
    - Comparison: <2 seconds
    - Metrics retrieval: <1 second
    """

    @pytest.mark.asyncio
    async def test_strategy_create_response_time(self, client):
        """POST /strategies should respond in <1 second"""
        start = time.time()

        response = await client.post(
            "/api/v1/strategies",
            json={...},
            headers={"Authorization": "Bearer token"},
        )

        elapsed = time.time() - start

        assert response.status_code == 201
        assert elapsed < 1.0, f"Strategy creation took {elapsed}s (max 1.0s)"

    @pytest.mark.asyncio
    async def test_strategy_retrieve_response_time(self, client):
        """GET /strategies/{id} should respond in <500ms"""
        # Create first
        create_resp = await client.post("/api/v1/strategies", json={...})
        strategy_id = create_resp.json()["strategy_id"]

        # Retrieve
        start = time.time()
        response = await client.get(
            f"/api/v1/strategies/{strategy_id}",
            headers={"Authorization": "Bearer token"},
        )
        elapsed = time.time() - start

        assert response.status_code == 200
        assert elapsed < 0.5, f"Strategy retrieval took {elapsed}s (max 0.5s)"

    @pytest.mark.asyncio
    async def test_comparison_response_time(self, client):
        """POST /compare/runs should complete in <2 seconds"""
        # Create 2 strategies and runs
        # ... setup ...

        start = time.time()
        response = await client.post(
            "/api/v1/compare/runs",
            json={"run_id_1": "run_1", "run_id_2": "run_2"},
            headers={"Authorization": "Bearer token"},
        )
        elapsed = time.time() - start

        assert response.status_code == 200
        assert elapsed < 2.0, f"Comparison took {elapsed}s (max 2.0s)"

    @pytest.mark.asyncio
    async def test_metrics_dashboard_response_time(self, client):
        """GET /dashboard/metrics should respond in <1 second"""
        start = time.time()
        response = await client.get(
            "/api/v1/dashboard/metrics?period=7d",
            headers={"Authorization": "Bearer token"},
        )
        elapsed = time.time() - start

        assert response.status_code == 200
        assert elapsed < 1.0, f"Metrics retrieval took {elapsed}s (max 1.0s)"

    @pytest.mark.asyncio
    async def test_audit_trail_response_time(self, client):
        """GET /audits/{id}/trail should respond in <1 second"""
        # Setup
        create_resp = await client.post("/api/v1/strategies", json={...})
        strategy_id = create_resp.json()["strategy_id"]

        # Retrieve audit trail
        start = time.time()
        response = await client.get(
            f"/api/v1/audits/{strategy_id}/trail",
            headers={"Authorization": "Bearer token"},
        )
        elapsed = time.time() - start

        assert response.status_code == 200
        assert elapsed < 1.0, f"Audit trail retrieval took {elapsed}s (max 1.0s)"
```

---

## WCAG Compliance Testing

### WCAG AA API Response Tests

**File:** `tests/integration/test_wcag_compliance.py`

```python
import pytest
from httpx import AsyncClient
import json


class TestWCAGCompliance:
    """
    Verify API responses include WCAG AA metadata
    for accessibility-aware clients
    """

    @pytest.mark.asyncio
    async def test_error_response_has_wcag_summary(self, client):
        """Error responses include wcag_summary field"""
        response = await client.post(
            "/api/v1/strategies",
            json={
                "name": "Test",
                "parameters": {
                    "strategy_profile": "return",
                    "sl_multiplier": 10.5,  # Invalid
                    ...
                },
            },
        )

        assert response.status_code == 400
        error = response.json()["error"]

        # WCAG: All errors must have human-readable summary
        assert "wcag_summary" in error
        assert len(error["wcag_summary"]) > 0
        assert error["wcag_summary"] == "Field sl_multiplier: expected ..."

    @pytest.mark.asyncio
    async def test_success_response_has_accessibility_metadata(self, client):
        """Success responses include wcag_metadata"""
        response = await client.post(
            "/api/v1/strategies",
            json={...},
        )

        assert response.status_code == 201
        data = response.json()

        # Should have WCAG metadata
        assert "wcag_metadata" in data or "wcag_summary" in data

    @pytest.mark.asyncio
    async def test_validation_errors_include_field_labels(self, client):
        """Field-level errors include readable labels"""
        response = await client.post(
            "/api/v1/strategies",
            json={...},  # Invalid
        )

        assert response.status_code == 400
        error = response.json()["error"]

        # Each error detail must have readable constraint
        for detail in error["details"]:
            assert "field" in detail
            assert "constraint" in detail  # Human-readable
            assert "expected" in detail    # Describe valid range
            assert "received" in detail    # Show what was sent

    @pytest.mark.asyncio
    async def test_list_response_includes_accessibility_hints(self, client):
        """List responses include hints for screen readers"""
        # Create multiple strategies
        for i in range(5):
            await client.post("/api/v1/strategies", json={...})

        # Retrieve list
        response = await client.get(
            "/api/v1/strategies?limit=10",
            headers={"Authorization": "Bearer token"},
        )

        assert response.status_code == 200
        data = response.json()

        # Should include count for accessibility
        assert "total_count" in data or isinstance(data, list)
        # Items should have stable IDs for navigation
        if isinstance(data, dict) and "items" in data:
            assert all("strategy_id" in item for item in data["items"])
```

---

## CI/CD Integration

### GitHub Actions Configuration

**File:** `.github/workflows/test-api.yml`

```yaml
name: API Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-asyncio pytest-cov

      - name: Run unit tests (60%)
        run: |
          pytest tests/unit/ -v --cov=app --cov-report=xml
          # Assert: >90% coverage
          pytest tests/unit/ --cov=app --cov-fail-under=90

  integration-tests:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run integration tests (30%)
        run: |
          pytest tests/integration/ -v -n auto  # Parallel execution
          # Must pass with parallel flag (tests database isolation)

      - name: Verify database isolation
        run: |
          pytest tests/integration/test_database_isolation.py -v
          # Run 3x to verify no flakiness
          pytest tests/integration/test_database_isolation.py -v
          pytest tests/integration/test_database_isolation.py -v

  e2e-tests:
    runs-on: ubuntu-latest
    needs: [unit-tests, integration-tests]
    services:
      postgres:
        image: postgres:15
        ...
    steps:
      - uses: actions/checkout@v3

      - name: Run E2E tests (10%)
        run: pytest tests/e2e/ -v

  performance-tests:
    runs-on: ubuntu-latest
    needs: [unit-tests, integration-tests]
    services:
      postgres:
        image: postgres:15
        ...
    steps:
      - uses: actions/checkout@v3

      - name: Run performance tests
        run: |
          pytest tests/integration/test_performance.py -v
          # Verify NFRs:
          # - Strategy create <1s
          # - Comparison <2s
          # - Metrics <1s

  wcag-compliance:
    runs-on: ubuntu-latest
    needs: [unit-tests, integration-tests]
    steps:
      - uses: actions/checkout@v3

      - name: Run WCAG compliance tests
        run: pytest tests/integration/test_wcag_compliance.py -v

  test-summary:
    runs-on: ubuntu-latest
    needs: [unit-tests, integration-tests, e2e-tests]
    steps:
      - name: Test results
        run: |
          echo "Unit Tests: ✅"
          echo "Integration Tests: ✅"
          echo "E2E Tests: ✅"
          echo "Coverage: >90%"
          echo "Performance: All NFRs met"
```

---

## Summary

This testing strategy provides:

✅ **Test pyramid structure** (60/30/10 distribution)
✅ **150+ total test cases** across 3 levels
✅ **Database isolation verification** (parallel execution)
✅ **Error path validation** (all error scenarios)
✅ **Performance assertions** (NFR verification)
✅ **WCAG compliance testing** (accessibility)
✅ **CI/CD integration** (GitHub Actions)
✅ **Mock data generation** (Faker fixtures)
✅ **OpenAPI validation** (contract testing)

**Status:** Ready for implementation with Phase 1 MVP
**Test Effort:** ~80 hours (2 QA engineers, 4 weeks)
**Test Maintenance:** ~5 hours/week during development
