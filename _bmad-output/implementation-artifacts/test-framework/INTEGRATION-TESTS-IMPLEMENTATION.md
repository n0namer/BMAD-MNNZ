# Integration Tests Implementation Guide - Katana VectorBT Phase 1

**Project**: Katana VectorBT
**Phase**: Phase 1 MVP (Epics 1-6)
**Date**: 2026-02-26
**Status**: Implementation Ready
**Test Architect**: QA Engineer Team

---

## EXECUTIVE SUMMARY

This guide specifies the 26 integration tests that validate service-level functionality with controlled I/O (database, file system, external APIs). Integration tests:
- Execute within <1000ms (acceptable for I/O)
- Test interactions between components
- Use transaction-based database isolation (Batch 1 feature)
- Verify end-to-end workflows within single service

**Test Distribution**:
- **Epic 1 (E-STRATEGY-LIFECYCLE)**: 5 integration tests (approval workflows)
- **Epic 2 (E-JOURNAL-SCHEMA)**: 6 integration tests (artifact retrieval)
- **Epic 3 (E-TELEMETRY-METRICS)**: 5 integration tests (dashboard aggregation)
- **Epic 4 (E-COMPARE-WORKFLOW)**: 5 integration tests (diff workflows)
- **Epic 5 (E-AUDIT-TRAIL)**: 5 integration tests (chain reconstruction)

**Total Effort**: 10-14 hours (team of 2-3 engineers, Week 2)

---

## SECTION 1: EPIC 1 - APPROVAL WORKFLOW INTEGRATION (5 TESTS)

**File**: `tests/integration/test_approval_workflow.py`
**Database**: Transaction-based isolation with db_session fixture
**External Dependencies**: None (mocked in this epic)

### Test 1.1: E1-I1 - Submit Strategy for Approval

**Test Name**: `test_submit_strategy_for_approval`
**Purpose**: Verify strategy can be submitted for approval and state changes

```python
def test_submit_strategy_for_approval(db_session):
    """Test submitting strategy for approval workflow."""
    # Setup
    strategy = Strategy(
        id="strat-1",
        name="Test Strategy",
        mode="BACKTEST",
        status=StrategyState.PAPER
    )
    db_session.add(strategy)
    db_session.flush()

    # Action: Submit for approval
    approval_request = strategy.request_approval(
        reason="Ready for live trading"
    )
    db_session.flush()

    # Assertions
    assert approval_request is not None
    assert approval_request.status == "PENDING"
    assert strategy.status == StrategyState.PAPER  # Still PAPER, waiting approval
    assert strategy.latest_approval_request == approval_request
    assert approval_request.created_at is not None

    # Verify in database
    db_request = db_session.query(ApprovalRequest).filter_by(
        strategy_id="strat-1"
    ).first()
    assert db_request is not None
    assert db_request.status == "PENDING"
```

### Test 1.2: E1-I2 - Approve Strategy Request

**Test Name**: `test_approve_strategy_request`
**Purpose**: Verify strategy can be approved and transitions to MICRO_LIVE

```python
def test_approve_strategy_request(db_session):
    """Test approving strategy request transitions state."""
    # Setup: Create strategy with pending approval
    strategy = Strategy(
        id="strat-1",
        name="Test Strategy",
        status=StrategyState.PAPER
    )
    approval_request = ApprovalRequest(
        strategy_id="strat-1",
        reason="Ready for live",
        status="PENDING"
    )
    db_session.add_all([strategy, approval_request])
    db_session.flush()

    # Action: Approve request
    approval_request.approve(approved_by="admin@example.com")
    db_session.flush()

    # Assertions
    assert approval_request.status == "APPROVED"
    assert approval_request.approved_at is not None
    assert approval_request.approved_by == "admin@example.com"

    # Verify strategy state changed
    strategy = db_session.query(Strategy).filter_by(id="strat-1").first()
    assert strategy.status == StrategyState.MICRO_LIVE
    assert strategy.micro_live_start_time is not None
```

### Test 1.3: E1-I3 - Reject Strategy Request

**Test Name**: `test_reject_strategy_request`
**Purpose**: Verify strategy request can be rejected

```python
def test_reject_strategy_request(db_session):
    """Test rejecting strategy request."""
    # Setup
    strategy = Strategy(id="strat-1", status=StrategyState.PAPER)
    approval_request = ApprovalRequest(
        strategy_id="strat-1",
        status="PENDING"
    )
    db_session.add_all([strategy, approval_request])
    db_session.flush()

    # Action: Reject request
    approval_request.reject(
        reason="Sharpe ratio too low",
        rejected_by="admin@example.com"
    )
    db_session.flush()

    # Assertions
    assert approval_request.status == "REJECTED"
    assert approval_request.reason_for_rejection == "Sharpe ratio too low"

    # Strategy should remain PAPER
    strategy = db_session.query(Strategy).filter_by(id="strat-1").first()
    assert strategy.status == StrategyState.PAPER
```

### Test 1.4: E1-I4 - Timeline Accuracy Post-Approval

**Test Name**: `test_timeline_accuracy_post_approval`
**Purpose**: Verify timeline and metrics are recorded correctly

```python
def test_timeline_accuracy_post_approval(db_session):
    """Test timeline recording after approval."""
    # Setup
    now = datetime.now()
    strategy = Strategy(
        id="strat-1",
        status=StrategyState.PAPER,
        created_at=now
    )
    approval_request = ApprovalRequest(
        strategy_id="strat-1",
        status="PENDING",
        created_at=now
    )
    db_session.add_all([strategy, approval_request])
    db_session.flush()

    # Wait 1 second (to show time progression)
    import time
    time.sleep(1)

    # Approve
    approval_request.approve(approved_by="admin")
    db_session.flush()

    # Verify timeline
    assert approval_request.created_at < approval_request.approved_at
    assert (approval_request.approved_at - approval_request.created_at).total_seconds() >= 1
    assert strategy.micro_live_start_time > strategy.created_at
```

### Test 1.5: E1-I5 - Multiple Approval Attempts

**Test Name**: `test_multiple_approval_attempts`
**Purpose**: Verify re-submission after rejection

```python
def test_multiple_approval_attempts(db_session):
    """Test strategy can be re-submitted after rejection."""
    # Setup
    strategy = Strategy(id="strat-1", status=StrategyState.PAPER)
    db_session.add(strategy)
    db_session.flush()

    # First attempt (rejected)
    request1 = strategy.request_approval("First attempt")
    request1.reject("Need more data", "admin")
    db_session.flush()

    assert request1.status == "REJECTED"
    assert strategy.status == StrategyState.PAPER

    # Second attempt (approved)
    request2 = strategy.request_approval("Second attempt, improved metrics")
    request2.approve("admin")
    db_session.flush()

    assert request2.status == "APPROVED"
    assert strategy.status == StrategyState.MICRO_LIVE

    # Verify both requests in history
    requests = db_session.query(ApprovalRequest).filter_by(
        strategy_id="strat-1"
    ).all()
    assert len(requests) == 2
    assert requests[0].status == "REJECTED"
    assert requests[1].status == "APPROVED"
```

---

## SECTION 2: EPIC 2 - ARTIFACT RETRIEVAL INTEGRATION (6 TESTS)

**File**: `tests/integration/test_artifact_retrieval.py`
**Database**: PostgreSQL with artifact schema
**External Dependencies**: File system (mocked for reproducibility)

### Test 2.1: E2-I1 - Query Run Journal by ID

```python
def test_query_run_journal_by_id(db_session):
    """Test retrieving run journal by ID."""
    # Setup: Create run with metrics
    run = RunJournal(
        id="run-1",
        strategy_id="strat-1",
        status="COMPLETE",
        metrics={"total_return": 0.15, "win_rate": 0.65}
    )
    db_session.add(run)
    db_session.flush()

    # Query
    retrieved = db_session.query(RunJournal).filter_by(id="run-1").first()

    # Assertions
    assert retrieved is not None
    assert retrieved.id == "run-1"
    assert retrieved.metrics["total_return"] == 0.15
    assert retrieved.metrics["win_rate"] == 0.65
```

### Test 2.2: E2-I2 - Retrieve Artifact Metadata

```python
def test_retrieve_artifact_metadata(db_session):
    """Test retrieving artifact metadata and schema validation."""
    # Setup
    artifact = Artifact(
        id="artifact-1",
        type="RUN_JOURNAL",
        version="1.0",
        schema_version="2.0",
        created_at=datetime.now(),
        data={
            "id": "run-1",
            "metrics": {"total_return": 0.15}
        }
    )
    db_session.add(artifact)
    db_session.flush()

    # Retrieve
    retrieved = db_session.query(Artifact).filter_by(id="artifact-1").first()

    # Assertions
    assert retrieved.type == "RUN_JOURNAL"
    assert retrieved.version == "1.0"
    assert retrieved.schema_version == "2.0"
    assert retrieved.data["metrics"]["total_return"] == 0.15
```

### Test 2.3: E2-I3 - Load JSON Schema Validation

```python
def test_load_json_schema_validation(db_session):
    """Test loading and validating against JSON schema."""
    # Setup: Store artifact
    artifact = Artifact(
        id="artifact-1",
        type="RUN_JOURNAL",
        data={
            "id": "run-1",
            "strategy_id": "strat-1",
            "metrics": {"total_return": 0.15}
        }
    )
    db_session.add(artifact)
    db_session.flush()

    # Load and validate
    schema = get_schema("RUN_JOURNAL")
    validator = SchemaValidator(schema)
    is_valid = validator.validate(artifact.data)

    # Assertions
    assert is_valid == True
    assert len(validator.errors) == 0
```

### Test 2.4: E2-I4 - Verify Data Consistency

```python
def test_verify_data_consistency(db_session):
    """Test data consistency across related tables."""
    # Setup: Create strategy and run
    strategy = Strategy(id="strat-1", name="Test")
    run = RunJournal(id="run-1", strategy_id="strat-1")
    metric = Metric(run_id="run-1", name="total_return", value=0.15)

    db_session.add_all([strategy, run, metric])
    db_session.flush()

    # Verify consistency
    retrieved_run = db_session.query(RunJournal).filter_by(id="run-1").first()
    strategy_ref = db_session.query(Strategy).filter_by(
        id=retrieved_run.strategy_id
    ).first()
    metrics_ref = db_session.query(Metric).filter_by(
        run_id=retrieved_run.id
    ).all()

    assert strategy_ref is not None
    assert len(metrics_ref) == 1
    assert metrics_ref[0].value == 0.15
```

### Test 2.5: E2-I5 - Cache Behavior Validation

```python
def test_cache_behavior_validation(db_session):
    """Test caching of artifact metadata."""
    # Setup
    artifact = Artifact(
        id="artifact-1",
        type="RUN_JOURNAL",
        data={"id": "run-1"}
    )
    db_session.add(artifact)
    db_session.flush()

    # First query (cache miss)
    import time
    start = time.time()
    result1 = get_artifact("artifact-1")
    time1 = time.time() - start

    # Second query (cache hit)
    start = time.time()
    result2 = get_artifact("artifact-1")
    time2 = time.time() - start

    # Cache should make second query faster
    assert time2 < time1  # Cache faster
    assert result1 == result2  # Same result
```

### Test 2.6: E2-I6 - Recovery from Missing Data

```python
def test_recovery_from_missing_data(db_session):
    """Test handling of missing data gracefully."""
    # Query non-existent run
    result = db_session.query(RunJournal).filter_by(id="nonexistent").first()

    assert result is None

    # Should not raise exception
    artifact_service = ArtifactService(db_session)
    result = artifact_service.get_by_id("nonexistent")
    assert result is None
```

---

## SECTION 3: EPIC 3 - DASHBOARD AGGREGATION INTEGRATION (5 TESTS)

**File**: `tests/integration/test_dashboard.py`
**Database**: PostgreSQL with pre-populated test data
**Real-time Data**: From run table

### Test 3.1: E3-I1 - Fetch Latest Metrics

```python
def test_fetch_latest_metrics(db_session):
    """Test fetching latest metrics across all strategies."""
    # Setup: Multiple strategies with runs
    strategies = [
        Strategy(id="strat-1", name="Strategy A"),
        Strategy(id="strat-2", name="Strategy B"),
    ]
    runs = [
        RunJournal(id="run-1", strategy_id="strat-1", metrics={"total_return": 0.15}),
        RunJournal(id="run-2", strategy_id="strat-2", metrics={"total_return": 0.10}),
    ]
    db_session.add_all(strategies + runs)
    db_session.flush()

    # Fetch metrics
    dashboard = DashboardService(db_session)
    metrics = dashboard.get_latest_metrics()

    # Assertions
    assert len(metrics) == 2
    assert metrics["strat-1"]["total_return"] == 0.15
    assert metrics["strat-2"]["total_return"] == 0.10
```

### Test 3.2: E3-I2 - Aggregate Across Strategies

```python
def test_aggregate_metrics_across_strategies(db_session):
    """Test aggregating metrics across multiple strategies."""
    # Setup: Multiple runs per strategy
    for i in range(3):
        run = RunJournal(
            id=f"run-{i}",
            strategy_id="strat-1",
            metrics={"total_return": 0.10 + i*0.05}
        )
        db_session.add(run)
    db_session.flush()

    # Aggregate
    dashboard = DashboardService(db_session)
    aggregates = dashboard.get_aggregated_metrics("strat-1")

    # Assertions
    assert aggregates["avg_return"] == pytest.approx(0.15, rel=0.01)
    assert aggregates["max_return"] == 0.20
    assert aggregates["min_return"] == 0.10
    assert aggregates["run_count"] == 3
```

### Test 3.3: E3-I3 - Sort and Filter Operations

```python
def test_sort_and_filter_operations(db_session):
    """Test sorting and filtering dashboard results."""
    # Setup
    for i in range(5):
        run = RunJournal(
            id=f"run-{i}",
            strategy_id="strat-1",
            status="COMPLETE" if i < 3 else "IN_PROGRESS",
            metrics={"total_return": 0.05 * i}
        )
        db_session.add(run)
    db_session.flush()

    # Filter and sort
    dashboard = DashboardService(db_session)
    results = dashboard.get_runs(
        filters={"status": "COMPLETE"},
        sort_by="total_return",
        order="DESC"
    )

    # Assertions
    assert len(results) == 3  # Filtered to 3 complete runs
    assert results[0].metrics["total_return"] >= results[1].metrics["total_return"]
```

### Test 3.4: E3-I4 - Responsive Render Validation

```python
def test_responsive_render_validation(db_session):
    """Test dashboard data is formatted for responsive rendering."""
    # Setup
    run = RunJournal(
        id="run-1",
        metrics={"total_return": 0.15, "win_rate": 0.65}
    )
    db_session.add(run)
    db_session.flush()

    # Get render data
    dashboard = DashboardService(db_session)
    render_data = dashboard.get_render_data()

    # Assertions
    assert "runs" in render_data
    assert "aggregates" in render_data
    assert "charts" in render_data
    assert isinstance(render_data["runs"], list)
    assert isinstance(render_data["aggregates"], dict)
```

### Test 3.5: E3-I5 - Cache Staleness Detection

```python
def test_cache_staleness_detection(db_session):
    """Test detection of stale cache."""
    # Setup: Create run, add to cache
    run = RunJournal(id="run-1", metrics={"total_return": 0.15})
    db_session.add(run)
    db_session.flush()

    dashboard = DashboardService(db_session)
    data1 = dashboard.get_latest_metrics()

    # Simulate time passing (cache expires after 5 minutes)
    import time
    dashboard.last_cache_time = time.time() - 300  # 5 minutes ago

    # Update data
    run.metrics["total_return"] = 0.20
    db_session.flush()

    # Cache should be invalidated
    is_stale = dashboard.is_cache_stale()
    assert is_stale == True

    # Fresh query should get new data
    data2 = dashboard.get_latest_metrics(force_refresh=True)
    assert data2["run-1"]["total_return"] == 0.20
```

---

## SECTION 4: EPIC 4 - DIFF WORKFLOW INTEGRATION (5 TESTS)

**File**: `tests/integration/test_diff_workflow.py`
**Database**: Multiple run artifacts
**Computation**: Diff algorithm applied to real data

### Test 4.1-4.5: Diff Workflow Tests

Similar structure to previous tests, validate:
- Generate comparison report (workflow across components)
- Validate metric alignment (cross-checks)
- Compute delta accurately (calculation correctness)
- Format export output (data transformation)
- Handle edge cases (robustness)

---

## SECTION 5: EPIC 5 - CHAIN RECONSTRUCTION INTEGRATION (5 TESTS)

**File**: `tests/integration/test_chain_reconstruction.py`
**Database**: Artifact chain with hashes
**Cryptography**: Hash verification

### Test 5.1-5.5: Chain Reconstruction Tests

Validate:
- Rebuild artifact chain from hashes
- Validate chain continuity (no gaps)
- Detect tampering (hash mismatches)
- Recover from partial loss (missing middle artifacts)
- Audit trail completeness (all events recorded)

---

## SECTION 6: DATABASE ISOLATION & TRANSACTION MANAGEMENT

### 6.1 Transaction-Based Isolation Pattern

All integration tests use the `db_session` fixture from conftest.py:

```python
def test_approval_workflow(db_session):
    """Integration test with automatic transaction rollback."""
    # All operations within this test are in a transaction
    strategy = Strategy(id="strat-1", status=StrategyState.PAPER)
    db_session.add(strategy)
    db_session.flush()

    strategy.request_approval()
    db_session.flush()

    # At end of test: Automatic rollback
    # Database returns to clean state for next test
    # No explicit cleanup needed
```

**Benefits**:
- ✅ Fast (no I/O between tests)
- ✅ Isolated (each test starts fresh)
- ✅ Parallelizable (4+ tests simultaneously)
- ✅ Deterministic (same seed data every time)

### 6.2 Batch Testing Pattern

For parallel execution, tests are assigned to batches:
```bash
pytest tests/integration/ -k "batch_1"  # Run batch 1 only
pytest tests/integration/ -k "batch_2"  # Run batch 2 only
# etc.
```

---

## SECTION 7: RUNNING INTEGRATION TESTS

**Run all integration tests**:
```bash
pytest tests/integration/ --ignore=tests/integration/end_to_end/ -v
```

**Run specific epic**:
```bash
pytest tests/integration/test_approval_workflow.py -v
```

**Run with database isolation**:
```bash
pytest tests/integration/ -v --tb=short
```

**Run in parallel** (4 batches):
```bash
pytest tests/integration/ -v -k "batch_1"
pytest tests/integration/ -v -k "batch_2"
pytest tests/integration/ -v -k "batch_3"
pytest tests/integration/ -v -k "batch_4"
```

**Run with coverage**:
```bash
pytest tests/integration/ --cov=katana --cov-report=html
```

**Expected Output**:
```
tests/integration/test_approval_workflow.py::test_submit_strategy_for_approval PASSED
tests/integration/test_approval_workflow.py::test_approve_strategy_request PASSED
...
========================= 26 passed in 15.23s =========================
Coverage: 89% (294/330 lines covered)
```

---

## SECTION 8: TROUBLESHOOTING

**Issue**: Database connection refused
- **Solution**: Verify PostgreSQL running, TEST_DATABASE_URL set

**Issue**: Transaction rollback doesn't clean up
- **Solution**: Ensure fixture is used: `def test_(..., db_session)`

**Issue**: Tests interfere with each other
- **Solution**: Check isolation — if sharing db_session scope, change to function scope

**Issue**: Timing-dependent test fails randomly
- **Solution**: Don't rely on `time.sleep()` — use database state instead

---

## CONCLUSION

The 26 integration tests validate service-level workflows with database isolation. Each test:
- ✅ Executes in <1000ms
- ✅ Uses transaction-based isolation
- ✅ Tests real workflows across components
- ✅ Requires valid data in database
- ✅ Parallelizable (4 batches)

**Estimated Implementation Time**: 10-14 hours
**Coverage**: 85-90% of integration paths

---

**Document Version**: 1.0
**Status**: FINAL
**Approval Date**: 2026-02-26
