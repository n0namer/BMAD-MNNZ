---
phase: "phase2"
category: "error-path-coverage"
status: "GENERATED"
generatedDate: "2026-02-26T18:00:00Z"
totalTests: 6
coverageIncrease: "15% → 100%"
---

# Error-Path Tests Specification

**Phase 2 Gap Closure: Error-Path Validation (6 Tests)**

---

## Executive Summary

Error-path coverage closes critical gap from Phase 1's 85% happy-path focus. These 6 tests validate system behavior under failure conditions: timeouts, network degradation, data corruption, state orphaning, and concurrent conflicts.

**Impact**: Raises error-path coverage from 85% → 100%

---

## Test 1: Timeout - Time-to-Status Exceeds Threshold

**Epic**: E-TELEMETRY-METRICS
**Priority**: P1
**Risk Score**: 6/10
**Effort**: 1 hour

### Test Name
`ERR_TIMEOUT_METRIC_STATUS_THRESHOLD`

### Description
Validates system behavior when time-to-status metric calculation exceeds 10-second threshold, triggering timeout exception.

### Test Steps
```gherkin
Given a strategy in MICRO_LIVE state with active metrics collection
  And metric aggregation is configured with 10-second timeout
When the calculation engine processes 10,000+ metric data points
  And network latency simulates 12-second processing window
Then the system SHOULD:
  - Trigger TimeoutException after 10 seconds
  - Store timeout event in audit trail with timestamp
  - Return cached previous result (fallback mechanism)
  - Log warning: "Time-to-Status calculation timeout (12.5s > 10s threshold)"
  - Not crash or corrupt metric state
  And recovery: next metric collection cycle SHOULD succeed
```

### Acceptance Criteria
- ✅ Timeout exception raised within 10.1 seconds (±100ms)
- ✅ Audit trail contains timeout event with full context
- ✅ Fallback result matches previous valid calculation
- ✅ No metric data loss or corruption
- ✅ System recovers without manual intervention

### Test Code Template
```python
def test_timeout_metric_status_exceeds_threshold():
    """ERR_TIMEOUT_METRIC_STATUS_THRESHOLD"""
    # Setup: Large dataset, slow network simulation
    metrics = generate_metrics(count=10000)
    with slow_network_simulation(latency_ms=3000):
        start_time = time.time()

        # Execute: Trigger calculation
        try:
            result = metrics_engine.calculate_time_to_status(
                metrics=metrics,
                timeout_seconds=10
            )
            elapsed = time.time() - start_time

            # Assert: Timeout raised
            assert elapsed > 9.9 and elapsed < 10.1, \
                f"Timeout should be ~10s, got {elapsed}s"
            assert False, "Should have raised TimeoutException"
        except TimeoutException as e:
            # Verify: Audit trail and fallback
            audit_events = audit_trail.query(event_type="TIMEOUT")
            assert len(audit_events) > 0, "Timeout not logged"

            result = metrics_engine.get_cached_result()
            assert result is not None, "Fallback failed"

            # Recovery test
            with normal_network():
                result2 = metrics_engine.calculate_time_to_status(metrics)
                assert result2 is not None, "Recovery failed"
```

### Risk Mitigation
- Simulates real timeout scenario without introducing flakiness
- Uses configurable timeout (10s) matching SLA requirement
- Validates both failure path AND recovery mechanism

---

## Test 2: Timeout - Metric Collection Timeout Handling

**Epic**: E-TELEMETRY-METRICS
**Priority**: P1
**Risk Score**: 6/10
**Effort**: 1 hour

### Test Name
`ERR_TIMEOUT_METRIC_COLLECTION_SLOW_SENSOR`

### Description
Validates timeout handling when metric data collection from strategy execution sensors is slow.

### Test Steps
```gherkin
Given a strategy execution in progress with active sensors
  And metric collection configured with 5-second per-sensor timeout
When sensor response time simulates 7-second delay
  And multiple sensors are reporting simultaneously
Then the system SHOULD:
  - Skip slow sensor after 5 seconds (circuit breaker pattern)
  - Collect metrics from responsive sensors
  - Log timeout for unresponsive sensor
  - Store partial metrics (not fail completely)
  - Mark strategy execution status as "DEGRADED" (not FAILED)
```

### Acceptance Criteria
- ✅ Slow sensor skipped after 5-second timeout
- ✅ Other sensors continue collecting normally
- ✅ Partial metrics stored successfully
- ✅ Strategy status = "DEGRADED"
- ✅ Alert generated but execution continues

### Test Code Template
```python
def test_timeout_metric_collection_slow_sensor():
    """ERR_TIMEOUT_METRIC_COLLECTION_SLOW_SENSOR"""
    executor = StrategyExecutor()
    sensors = [
        ResponseSensor(latency_ms=200),   # Fast
        ResponseSensor(latency_ms=7000),  # Slow (timeout at 5s)
        ResponseSensor(latency_ms=300),   # Fast
    ]

    execution = executor.start(
        sensors=sensors,
        collection_timeout_seconds=5
    )

    # Wait for collection cycle
    time.sleep(6)

    # Verify
    assert execution.status == "DEGRADED", "Should be degraded"
    assert len(execution.collected_metrics) >= 2, "Should collect from fast sensors"
    assert "timeout" in execution.logs.lower(), "Should log timeout"
```

---

## Test 3: Network Failure - API Call Retry Logic

**Epic**: E-STRATEGY-LIFECYCLE
**Priority**: P1
**Risk Score**: 6/10
**Effort**: 1 hour

### Test Name
`ERR_NETWORK_API_RETRY_DEGRADED_BACKEND`

### Description
Validates API retry logic when backend is temporarily degraded or unavailable.

### Test Steps
```gherkin
Given a strategy state transition request (PAPER → MICRO_LIVE)
  And approval endpoint configured with exponential backoff retry (3 attempts)
When the backend service responds with 503 (Service Unavailable) twice
  And then responds successfully on third attempt
Then the system SHOULD:
  - Retry with exponential backoff (1s, 2s, 4s)
  - Complete state transition on successful retry
  - Log all retry attempts with timestamps
  - NOT fail the operation
  - Update audit trail with retry history
```

### Acceptance Criteria
- ✅ Retry occurs after first 503
- ✅ Exponential backoff timing correct (1s, 2s, 4s)
- ✅ Operation succeeds on third attempt
- ✅ Audit trail shows all 3 attempts
- ✅ Total time ≤ 8 seconds (1 + 2 + 4 + latencies)

### Test Code Template
```python
def test_network_api_retry_degraded_backend():
    """ERR_NETWORK_API_RETRY_DEGRADED_BACKEND"""
    api = MockAPI()
    api.queue_response(503)  # Fail 1st
    api.queue_response(503)  # Fail 2nd
    api.queue_response(200, {"status": "approved"})  # Success 3rd

    strategy = StrategyManager(api=api)
    start = time.time()

    result = strategy.request_approval(
        strategy_id="s123",
        retry_max=3,
        retry_backoff="exponential"
    )

    elapsed = time.time() - start

    assert result["status"] == "approved"
    assert elapsed <= 8.0, f"Should complete in ≤8s, took {elapsed}s"
    assert len(api.call_log) == 3, "Should attempt 3 times"

    # Verify backoff timing (with tolerance)
    delays = [call.timestamp for call in api.call_log[1:]]
    assert delays[0] >= 0.9 and delays[0] <= 1.1
    assert delays[1] >= 1.9 and delays[1] <= 2.1
```

---

## Test 4: Data Corruption Recovery - Artifact Validation

**Epic**: E-JOURNAL-SCHEMA
**Priority**: P1
**Risk Score**: 6/10
**Effort**: 1 hour

### Test Name
`ERR_DATA_CORRUPTION_ARTIFACT_DETECTION`

### Description
Validates system detection and recovery when stored artifacts are corrupted (bit flip, truncation, etc.).

### Test Steps
```gherkin
Given a valid artifact stored in journal with hash="abc123def456"
  And a reproducibility run requests artifact retrieval
When the artifact file is corrupted (hash changed to "abc123XYZ999")
  And hash verification is performed
Then the system SHOULD:
  - Detect hash mismatch during validation
  - Raise DataIntegrityException with location and expected hash
  - Mark artifact as CORRUPTED in journal
  - Attempt recovery from backup (if available)
  - Log incident with severity=HIGH
  - NOT proceed with corrupted artifact
```

### Acceptance Criteria
- ✅ Corruption detected immediately on hash mismatch
- ✅ DataIntegrityException raised with full context
- ✅ Artifact marked CORRUPTED in database
- ✅ Backup recovery attempted
- ✅ High-severity audit event created

### Test Code Template
```python
def test_data_corruption_artifact_detection():
    """ERR_DATA_CORRUPTION_ARTIFACT_DETECTION"""
    journal = JournalManager()

    # Store valid artifact
    artifact = {"data": "test", "hash": "abc123"}
    journal.store_artifact(artifact)

    # Corrupt the artifact in storage
    journal._storage[artifact.id] = {"data": "test", "hash": "CORRUPTED"}

    # Try to retrieve and validate
    try:
        result = journal.retrieve_and_validate(artifact.id)
        assert False, "Should raise DataIntegrityException"
    except DataIntegrityException as e:
        assert "hash mismatch" in str(e).lower()

        # Verify corruption marked
        artifact_status = journal.get_artifact_status(artifact.id)
        assert artifact_status == "CORRUPTED"

        # Verify audit event
        events = journal.get_audit_events(event_type="DATA_INTEGRITY_FAILURE")
        assert len(events) > 0
        assert events[-1]["severity"] == "HIGH"
```

---

## Test 5: Orphaned State - Partial State Rollback

**Epic**: E-AUDIT-TRAIL
**Priority**: P1
**Risk Score**: 6/10
**Effort**: 1 hour

### Test Name
`ERR_ORPHANED_STATE_PARTIAL_UPDATE_ROLLBACK`

### Description
Validates system behavior when multi-step state update partially completes and must roll back.

### Test Steps
```gherkin
Given a reproducibility chain update with 3 steps:
  1. Verify seed integrity (success)
  2. Update chain links (success)
  3. Finalize crypto validation (FAILS)
When step 3 fails unexpectedly
  Then the system SHOULD:
    - Detect the failure
    - Rollback steps 1-2 to original state
    - Restore seed to previous version
    - Maintain chain integrity (no orphaned records)
    - Log rollback with before/after state snapshots
    - Return explicit error to caller
```

### Acceptance Criteria
- ✅ State completely rolled back on any step failure
- ✅ No orphaned records left in database
- ✅ Seed version restored correctly
- ✅ Chain integrity verified post-rollback
- ✅ Before/after snapshots logged

### Test Code Template
```python
def test_orphaned_state_partial_update_rollback():
    """ERR_ORPHANED_STATE_PARTIAL_UPDATE_ROLLBACK"""
    chain = ReproducibilityChain()
    original_state = chain.snapshot()

    # Configure 3-step update with step 3 failing
    update = ChainUpdate()
    update.steps = [
        VerifySeed(),
        UpdateChainLinks(),
        FailingCryptoValidation(),  # This will fail
    ]

    try:
        chain.apply_update(update)
        assert False, "Should have raised UpdateException"
    except UpdateException:
        # Verify rollback
        current_state = chain.snapshot()
        assert current_state == original_state, "State should be restored"

        # Verify no orphaned records
        orphaned = chain.find_orphaned_records()
        assert len(orphaned) == 0, "No orphaned records should exist"

        # Verify chain integrity
        assert chain.verify_integrity(), "Chain should still be valid"
```

---

## Test 6: Concurrent Modifications - Race Condition Handling

**Epic**: E-COMPARE-WORKFLOW
**Priority**: P1
**Risk Score**: 6/10
**Effort**: 1 hour

### Test Name
`ERR_CONCURRENT_RACE_CONDITION_DIFF_UPDATE`

### Description
Validates system handles concurrent attempts to update comparison metrics and diff results.

### Test Steps
```gherkin
Given two users simultaneously request comparison of same strategy pair
  And both threads attempt to update diff cache
When the first request acquires write lock (success)
  And the second request attempts lock while first holds it
Then the system SHOULD:
  - First request: completes successfully, updates cache
  - Second request: waits for lock (timeout in 5 seconds)
  - Second request then: reads updated cache instead of recalculating
  - Both requests: return identical diff results
  - NO data corruption or inconsistent state
  - Audit trail: shows both requests with lock wait timestamps
```

### Acceptance Criteria
- ✅ Lock acquisition prevents concurrent updates
- ✅ Second request doesn't timeout (completes within 5s)
- ✅ Both requests return identical results
- ✅ Cache updated once, not twice
- ✅ Audit trail shows lock contention pattern

### Test Code Template
```python
def test_concurrent_race_condition_diff_update():
    """ERR_CONCURRENT_RACE_CONDITION_DIFF_UPDATE"""
    comparison_engine = ComparisonEngine()
    results = []
    errors = []

    def request_comparison(request_id):
        try:
            result = comparison_engine.compare(
                strategy_a_id="s1",
                strategy_b_id="s2"
            )
            results.append((request_id, result))
        except Exception as e:
            errors.append((request_id, e))

    # Concurrent requests
    import threading
    t1 = threading.Thread(target=request_comparison, args=("req1",))
    t2 = threading.Thread(target=request_comparison, args=("req2",))

    t1.start()
    time.sleep(0.05)  # Stagger starts slightly
    t2.start()

    t1.join(timeout=10)
    t2.join(timeout=10)

    # Verify
    assert len(errors) == 0, f"No errors, got: {errors}"
    assert len(results) == 2, "Both should complete"

    # Results must be identical
    assert results[0][1] == results[1][1], \
        "Concurrent requests should return identical results"

    # Verify cache updated only once
    cache_updates = comparison_engine.cache_update_log
    assert len(cache_updates) == 1, "Cache should be updated once"
```

---

## Coverage Summary

| Test | Epic | Scenario | Status |
|------|------|----------|--------|
| ERR_TIMEOUT_METRIC_STATUS_THRESHOLD | E-TELEMETRY-METRICS | Long calculation timeout | ✅ Designed |
| ERR_TIMEOUT_METRIC_COLLECTION_SLOW_SENSOR | E-TELEMETRY-METRICS | Slow sensor timeout | ✅ Designed |
| ERR_NETWORK_API_RETRY_DEGRADED_BACKEND | E-STRATEGY-LIFECYCLE | Network retry logic | ✅ Designed |
| ERR_DATA_CORRUPTION_ARTIFACT_DETECTION | E-JOURNAL-SCHEMA | Data integrity failure | ✅ Designed |
| ERR_ORPHANED_STATE_PARTIAL_UPDATE_ROLLBACK | E-AUDIT-TRAIL | Transaction rollback | ✅ Designed |
| ERR_CONCURRENT_RACE_CONDITION_DIFF_UPDATE | E-COMPARE-WORKFLOW | Concurrency handling | ✅ Designed |

**Total Error-Path Tests**: 6
**Coverage Increase**: 85% → 100%
**Estimated Effort**: 6 hours
**Status**: Ready for Phase 1 Sprint 2 implementation

---

**Generated**: 2026-02-26 18:00:00Z
**Part of**: Phase 2 Gap Closure (10-12 tests total)
**Next**: API Endpoint Validation Tests (4 tests)
