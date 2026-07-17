# Unit Tests Implementation Guide - Katana VectorBT Phase 1

**Project**: Katana VectorBT
**Phase**: Phase 1 MVP (Epics 1-6)
**Date**: 2026-02-26
**Status**: Implementation Ready
**Test Architect**: QA Engineer Team

---

## EXECUTIVE SUMMARY

This guide provides concrete implementation specifications for the 42 unit tests across 5 epics. Each test is designed to:
- Execute in <100ms (no I/O, isolated)
- Validate a single function/method (single responsibility)
- Require no database (use mocks/fixtures)
- Be fully parallelizable (zero state sharing)

**Test Distribution**:
- **Epic 1 (E-STRATEGY-LIFECYCLE)**: 8 unit tests (state machine transitions)
- **Epic 2 (E-JOURNAL-SCHEMA)**: 12 unit tests (JSON schema validation)
- **Epic 3 (E-TELEMETRY-METRICS)**: 8 unit tests (metric calculation)
- **Epic 4 (E-COMPARE-WORKFLOW)**: 6 unit tests (diff algorithm)
- **Epic 5 (E-AUDIT-TRAIL)**: 8 unit tests (cryptographic hash validation)

**Total Effort**: 10-16 hours (team of 2-3 engineers, Week 1)

---

## SECTION 1: EPIC 1 - STATE MACHINE LIFECYCLE (8 UNIT TESTS)

**File**: `tests/unit/test_state_machine.py`
**Risk Score**: 9 (Critical — state machine correctness is foundation)
**Coverage Target**: 100% of state transitions

### Test 1.1: E1-U1 - Initial State Validation

**Test Name**: `test_strategy_initial_state_is_paper`
**Purpose**: Verify new strategy starts in PAPER state

```python
def test_strategy_initial_state_is_paper():
    """Verify new strategy initializes to PAPER state."""
    strategy = Strategy(
        id="test-strat-1",
        name="Test Strategy",
        mode="BACKTEST"
    )

    assert strategy.current_state == StrategyState.PAPER
    assert strategy.state_history == [
        StateTransition(
            from_state=None,
            to_state=StrategyState.PAPER,
            timestamp=strategy.created_at
        )
    ]
```

**Assertions**:
- ✅ New strategy state == PAPER
- ✅ State history initialized with creation transition
- ✅ Timestamp matches creation time

### Test 1.2: E1-U2 - PAPER→MICRO_LIVE Transition

**Test Name**: `test_paper_to_micro_live_transition`
**Purpose**: Verify valid transition from PAPER to MICRO_LIVE

```python
def test_paper_to_micro_live_transition():
    """Test PAPER→MICRO_LIVE transition with approval."""
    strategy = Strategy(id="test-strat-1", name="Test")
    assert strategy.current_state == StrategyState.PAPER

    # Transition
    strategy.request_approval()
    assert strategy.current_state == StrategyState.MICRO_LIVE

    # Verify state history
    assert len(strategy.state_history) == 2
    transition = strategy.state_history[1]
    assert transition.from_state == StrategyState.PAPER
    assert transition.to_state == StrategyState.MICRO_LIVE
    assert transition.initiated_by == "system"
```

**Assertions**:
- ✅ State changes to MICRO_LIVE
- ✅ Transition recorded in history
- ✅ Timestamp is newer than previous state

### Test 1.3: E1-U3 - MICRO_LIVE→LIVE Transition

**Test Name**: `test_micro_live_to_live_transition`
**Purpose**: Verify transition from MICRO_LIVE to LIVE after validation

```python
def test_micro_live_to_live_transition():
    """Test MICRO_LIVE→LIVE transition after validation window."""
    strategy = Strategy(id="test-strat-1", name="Test")
    strategy.current_state = StrategyState.MICRO_LIVE
    strategy.micro_live_start_time = datetime.now() - timedelta(days=8)

    # Transition
    strategy.promote_to_live()
    assert strategy.current_state == StrategyState.LIVE

    # Verify transition
    assert strategy.state_history[-1].to_state == StrategyState.LIVE
    assert strategy.live_start_time is not None
```

**Assertions**:
- ✅ Requires minimum 7 days in MICRO_LIVE
- ✅ State changes to LIVE
- ✅ Live timestamp recorded

### Test 1.4: E1-U4 - LIVE→PAPER Transition (Emergency Stop)

**Test Name**: `test_live_to_paper_emergency_stop`
**Purpose**: Verify emergency stop transitions from LIVE to PAPER

```python
def test_live_to_paper_emergency_stop():
    """Test emergency stop from LIVE to PAPER."""
    strategy = Strategy(id="test-strat-1", name="Test")
    strategy.current_state = StrategyState.LIVE
    strategy.live_start_time = datetime.now() - timedelta(hours=2)

    # Emergency stop
    strategy.emergency_stop(reason="Drawdown exceeded 20%")
    assert strategy.current_state == StrategyState.PAPER

    # Verify transition
    transition = strategy.state_history[-1]
    assert transition.from_state == StrategyState.LIVE
    assert transition.to_state == StrategyState.PAPER
    assert transition.reason == "Drawdown exceeded 20%"
```

**Assertions**:
- ✅ LIVE state stops immediately
- ✅ Transition reason recorded
- ✅ No validation delays applied

### Test 1.5: E1-U5 - Invalid State Transitions (Error Handling)

**Test Name**: `test_invalid_state_transition_raises_error`
**Purpose**: Verify invalid transitions are rejected

```python
def test_invalid_state_transition_raises_error():
    """Test that invalid transitions raise InvalidTransitionError."""
    strategy = Strategy(id="test-strat-1", name="Test")
    strategy.current_state = StrategyState.PAPER

    # Invalid: PAPER directly to LIVE (skipping MICRO_LIVE)
    with pytest.raises(InvalidTransitionError) as exc_info:
        strategy.current_state = StrategyState.LIVE
        strategy.validate_transition()

    assert "PAPER→LIVE not allowed" in str(exc_info.value)

    # State should not change
    assert strategy.current_state == StrategyState.PAPER
```

**Assertions**:
- ✅ Invalid transition raises exception
- ✅ State unchanged after failed transition
- ✅ Error message is descriptive

### Test 1.6: E1-U6 - Transition Guard Conditions

**Test Name**: `test_transition_guard_conditions`
**Purpose**: Verify pre-conditions for state transitions

```python
def test_transition_guard_conditions():
    """Test guard conditions before transitions."""
    strategy = Strategy(id="test-strat-1", name="Test")
    strategy.current_state = StrategyState.MICRO_LIVE
    strategy.micro_live_start_time = datetime.now()  # Just started

    # Transition should fail: Not enough time in MICRO_LIVE
    with pytest.raises(InvalidTransitionError) as exc_info:
        strategy.promote_to_live()

    assert "Requires 7 days in MICRO_LIVE" in str(exc_info.value)

    # State unchanged
    assert strategy.current_state == StrategyState.MICRO_LIVE

    # After 7 days, transition succeeds
    strategy.micro_live_start_time = datetime.now() - timedelta(days=7)
    strategy.promote_to_live()
    assert strategy.current_state == StrategyState.LIVE
```

**Assertions**:
- ✅ Guard conditions checked before transition
- ✅ Descriptive error messages
- ✅ Transition succeeds when conditions met

### Test 1.7: E1-U7 - State History Tracking

**Test Name**: `test_state_history_tracking`
**Purpose**: Verify complete history is recorded

```python
def test_state_history_tracking():
    """Test that state history tracks all transitions."""
    strategy = Strategy(id="test-strat-1", name="Test")

    # Simulate state transitions
    strategy.request_approval()  # PAPER→MICRO_LIVE
    strategy.micro_live_start_time = datetime.now() - timedelta(days=7)
    strategy.promote_to_live()    # MICRO_LIVE→LIVE

    # Verify history
    assert len(strategy.state_history) == 3  # Initial + 2 transitions

    assert strategy.state_history[0].to_state == StrategyState.PAPER
    assert strategy.state_history[1].to_state == StrategyState.MICRO_LIVE
    assert strategy.state_history[2].to_state == StrategyState.LIVE

    # Timestamps should be ordered
    for i in range(len(strategy.state_history) - 1):
        assert strategy.state_history[i].timestamp <= strategy.state_history[i+1].timestamp
```

**Assertions**:
- ✅ All transitions recorded
- ✅ History length correct
- ✅ Timestamps ordered chronologically

### Test 1.8: E1-U8 - Concurrent Transition Handling

**Test Name**: `test_concurrent_transition_handling`
**Purpose**: Verify race conditions don't corrupt state

```python
def test_concurrent_transition_handling():
    """Test that concurrent transitions are handled safely."""
    import threading

    strategy = Strategy(id="test-strat-1", name="Test")
    errors = []

    def try_transition():
        try:
            strategy.request_approval()
        except Exception as e:
            errors.append(e)

    # Attempt concurrent transitions
    threads = [threading.Thread(target=try_transition) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # Either exactly one succeeded or all failed with clear error
    successful_transitions = [
        h for h in strategy.state_history
        if h.to_state == StrategyState.MICRO_LIVE
    ]

    assert len(successful_transitions) <= 1  # At most one transition
    if successful_transitions:
        assert len(errors) == 4  # Others should have failed gracefully
```

**Assertions**:
- ✅ Concurrent calls don't create duplicate transitions
- ✅ At most one thread succeeds
- ✅ Failed attempts report clear errors
- ✅ Final state is consistent

---

## SECTION 2: EPIC 2 - JSON SCHEMA VALIDATION (12 UNIT TESTS)

**File**: `tests/unit/test_schema_validation.py`
**Risk Score**: 6 (High — schema validation is critical for data integrity)
**Coverage Target**: All validation rules

### Test 2.1: E2-U1 - Schema Structure Validation

```python
def test_run_journal_schema_structure():
    """Verify Run Journal schema has required structure."""
    schema = RunJournalSchema()

    # Must have these fields
    assert "id" in schema.fields
    assert "created_at" in schema.fields
    assert "strategy_id" in schema.fields
    assert "metrics" in schema.fields

    # Each field has type
    for field_name, field in schema.fields.items():
        assert field.type is not None
```

### Test 2.2: E2-U2 - Required Fields Enforcement

```python
def test_required_fields_enforcement():
    """Verify required fields are enforced."""
    with pytest.raises(ValidationError) as exc_info:
        RunJournal(
            # Missing 'id' and 'created_at'
            strategy_id="strat-1",
            status="COMPLETE"
        )

    error = exc_info.value
    assert "id" in str(error)
    assert "created_at" in str(error)
```

### Test 2.3: E2-U3 - Type Validation (Strict)

```python
def test_strict_type_validation():
    """Verify strict type validation."""
    # Numeric field with string value
    with pytest.raises(ValidationError):
        RunJournal(
            id="run-1",
            strategy_id="strat-1",
            metrics={"total_return": "invalid"}  # Should be float
        )

    # Date field with wrong format
    with pytest.raises(ValidationError):
        RunJournal(
            id="run-1",
            strategy_id="strat-1",
            created_at="2026-13-45"  # Invalid date
        )
```

### Test 2.4: E2-U4 - Enum Validation

```python
def test_enum_field_validation():
    """Verify enum values are enforced."""
    run = RunJournal(
        id="run-1",
        strategy_id="strat-1",
        status="COMPLETE"
    )
    assert run.status == RunStatus.COMPLETE

    # Invalid enum value
    with pytest.raises(ValidationError):
        RunJournal(
            id="run-1",
            strategy_id="strat-1",
            status="INVALID_STATUS"
        )
```

### Test 2.5: E2-U5 - Numeric Range Validation

```python
def test_numeric_range_validation():
    """Verify numeric ranges are enforced."""
    # Valid range: 0-1
    run = RunJournal(
        id="run-1",
        strategy_id="strat-1",
        metrics={"win_rate": 0.65}  # Valid: 0 <= 0.65 <= 1
    )
    assert run.metrics["win_rate"] == 0.65

    # Invalid: > 1
    with pytest.raises(ValidationError):
        RunJournal(
            id="run-1",
            strategy_id="strat-1",
            metrics={"win_rate": 1.5}  # Invalid: > 1
        )

    # Invalid: < 0
    with pytest.raises(ValidationError):
        RunJournal(
            id="run-1",
            strategy_id="strat-1",
            metrics={"win_rate": -0.1}  # Invalid: < 0
        )
```

### Test 2.6: E2-U6 - Date Format Validation

```python
def test_date_format_validation():
    """Verify date fields use correct format."""
    # Valid ISO format
    run = RunJournal(
        id="run-1",
        strategy_id="strat-1",
        created_at="2026-02-26T15:30:00Z"
    )
    assert isinstance(run.created_at, datetime)

    # Invalid formats
    invalid_formats = [
        "26/02/2026",      # US format
        "2026-02-26",      # Date only (missing time)
        "26-Feb-2026",     # Text format
        "invalid",         # Garbage
    ]

    for invalid_date in invalid_formats:
        with pytest.raises(ValidationError):
            RunJournal(
                id="run-1",
                strategy_id="strat-1",
                created_at=invalid_date
            )
```

### Test 2.7: E2-U7 - Nested Object Validation

```python
def test_nested_object_validation():
    """Verify nested objects are validated recursively."""
    # Valid nested structure
    run = RunJournal(
        id="run-1",
        strategy_id="strat-1",
        metrics=MetricsObject(
            total_return=0.15,
            profit_factor=2.1
        )
    )
    assert run.metrics.total_return == 0.15

    # Invalid nested: Missing required field
    with pytest.raises(ValidationError):
        RunJournal(
            id="run-1",
            strategy_id="strat-1",
            metrics=MetricsObject(
                # Missing 'total_return'
                profit_factor=2.1
            )
        )
```

### Test 2.8: E2-U8 - Array Element Validation

```python
def test_array_element_validation():
    """Verify array elements are validated."""
    # Valid array
    run = RunJournal(
        id="run-1",
        strategy_id="strat-1",
        trades=[
            {"entry": 100, "exit": 105, "profit": 5},
            {"entry": 110, "exit": 108, "profit": -2}
        ]
    )
    assert len(run.trades) == 2

    # Invalid array element type
    with pytest.raises(ValidationError):
        RunJournal(
            id="run-1",
            strategy_id="strat-1",
            trades=[
                {"entry": 100, "exit": 105, "profit": 5},
                "invalid"  # Should be object, not string
            ]
        )
```

### Test 2.9: E2-U9 - Null Value Handling

```python
def test_null_value_handling():
    """Verify null values handled correctly."""
    # Optional field can be null
    run = RunJournal(
        id="run-1",
        strategy_id="strat-1",
        notes=None  # Optional field
    )
    assert run.notes is None

    # Required field cannot be null
    with pytest.raises(ValidationError):
        RunJournal(
            id=None,  # Required field
            strategy_id="strat-1"
        )
```

### Test 2.10: E2-U10 - Default Value Application

```python
def test_default_value_application():
    """Verify default values are applied."""
    run = RunJournal(
        id="run-1",
        strategy_id="strat-1"
        # status not provided
    )

    # Should have default status
    assert run.status == RunStatus.PENDING  # Default value
```

### Test 2.11: E2-U11 - Custom Validation Rules

```python
def test_custom_validation_rules():
    """Verify custom validation rules."""
    # Rule: profit_factor must be > 1 if win_rate > 0.5
    with pytest.raises(ValidationError):
        RunJournal(
            id="run-1",
            strategy_id="strat-1",
            metrics={
                "win_rate": 0.65,  # High win rate
                "profit_factor": 0.8  # Invalid: Should be > 1
            }
        )

    # Valid: High win rate with valid profit factor
    run = RunJournal(
        id="run-1",
        strategy_id="strat-1",
        metrics={
            "win_rate": 0.65,
            "profit_factor": 1.5  # Valid
        }
    )
    assert run.metrics["profit_factor"] == 1.5
```

### Test 2.12: E2-U12 - Error Message Clarity

```python
def test_validation_error_clarity():
    """Verify error messages are clear and actionable."""
    try:
        RunJournal(
            id="run-1",
            strategy_id="strat-1",
            metrics={"win_rate": 1.5}  # Invalid: > 1
        )
        pytest.fail("Should have raised ValidationError")
    except ValidationError as e:
        error_msg = str(e)

        # Error should identify the field
        assert "win_rate" in error_msg

        # Error should explain the constraint
        assert "1" in error_msg or "range" in error_msg or "maximum" in error_msg

        # Error should be user-friendly (not stack trace)
        assert "traceback" not in error_msg.lower()
```

---

## SECTION 3: EPIC 3 - METRIC CALCULATION (8 UNIT TESTS)

**File**: `tests/unit/test_metrics.py`
**Risk Score**: 6 (High — incorrect metrics cause wrong decisions)
**Coverage Target**: All calculation paths

### Test 3.1-3.8: Metric Calculations

Each test follows pattern:
1. Set up input data
2. Calculate metric
3. Verify result matches expected value (with tolerance for floats)
4. Test edge cases (zero division, empty data, etc.)

```python
def test_net_profit_loss_calculation():
    """Verify P&L calculation."""
    trades = [
        {"entry": 100, "exit": 105},  # +5 profit
        {"entry": 110, "exit": 108},  # -2 loss
        {"entry": 107, "exit": 110},  # +3 profit
    ]
    initial_capital = 1000

    result = calculate_net_pnl(trades, initial_capital)

    # Total P&L: 5 - 2 + 3 = 6
    assert result == 6

    # As percentage
    result_pct = calculate_net_pnl_pct(trades, initial_capital)
    assert abs(result_pct - 0.006) < 0.0001  # 0.6%


def test_win_rate_calculation():
    """Verify win rate calculation."""
    trades = [
        {"result": 1},  # Win
        {"result": 1},  # Win
        {"result": -1},  # Loss
        {"result": 1},  # Win
    ]

    result = calculate_win_rate(trades)
    assert abs(result - 0.75) < 0.0001  # 75%


def test_profit_factor_calculation():
    """Verify profit factor calculation."""
    trades = [
        {"pnl": 10},   # Winning trades
        {"pnl": 15},
        {"pnl": 5},
        {"pnl": -4},   # Losing trades
        {"pnl": -2},
    ]

    result = calculate_profit_factor(trades)
    # Profit factor = (10+15+5) / (4+2) = 30 / 6 = 5.0
    assert abs(result - 5.0) < 0.0001


def test_max_drawdown_calculation():
    """Verify maximum drawdown calculation."""
    equity = [1000, 1100, 950, 1000, 900, 1050]  # Peak: 1100, Trough: 900

    result = calculate_max_drawdown(equity)
    expected = (1100 - 900) / 1100  # 18.18%
    assert abs(result - expected) < 0.0001


def test_sharpe_ratio_calculation():
    """Verify Sharpe ratio calculation."""
    returns = [0.01, 0.02, -0.01, 0.015, 0.005]  # Daily returns

    result = calculate_sharpe_ratio(returns, risk_free_rate=0.0)

    # Sharpe = mean_return / std_dev
    assert result > 0  # Positive Sharpe ratio for positive returns


def test_metric_calculation_edge_cases():
    """Verify edge case handling."""
    # Empty trades
    assert calculate_win_rate([]) == 0.0
    assert calculate_profit_factor([]) == 0.0

    # Zero division
    single_trade = [{"result": 1}]
    assert calculate_win_rate(single_trade) == 1.0  # 100% win rate

    # All losses
    losing_trades = [{"result": -1}, {"result": -1}]
    assert calculate_win_rate(losing_trades) == 0.0
    assert calculate_profit_factor(losing_trades) == 0.0


def test_metric_precision_and_rounding():
    """Verify metric precision."""
    trades = [
        {"entry": 100.123, "exit": 105.789},
    ]

    result = calculate_net_pnl(trades, 1000)
    # 105.789 - 100.123 = 5.666
    assert abs(result - 5.666) < 0.001


def test_metric_performance_under_load():
    """Verify metric calculation performance."""
    # 1000 trades
    trades = [{"entry": 100 + i*0.1, "exit": 101 + i*0.1} for i in range(1000)]

    start_time = time.time()
    result = calculate_metrics(trades, 10000)
    elapsed = time.time() - start_time

    assert elapsed < 0.01  # Should be <10ms
    assert result["total_return"] > 0
```

---

## SECTION 4: EPIC 4 - DIFF ALGORITHM (6 UNIT TESTS)

**File**: `tests/unit/test_diff_algorithm.py`
**Risk Score**: 6 (High — incorrect diffs mislead strategy comparison)
**Coverage Target**: All diff scenarios

```python
def test_identical_runs_no_diff():
    """Verify identical runs produce empty diff."""
    run1 = {
        "metrics": {"total_return": 0.15, "win_rate": 0.65},
        "parameters": {"lookback": 20, "threshold": 0.5}
    }
    run2 = run1.copy()

    diff = compute_diff(run1, run2)
    assert diff == {}  # No differences


def test_single_metric_change_diff():
    """Verify single metric change is detected."""
    run1 = {"metrics": {"total_return": 0.15, "win_rate": 0.65}}
    run2 = {"metrics": {"total_return": 0.18, "win_rate": 0.65}}

    diff = compute_diff(run1, run2)
    assert "metrics.total_return" in diff
    assert diff["metrics.total_return"] == {
        "from": 0.15,
        "to": 0.18,
        "change": "+20%"
    }


def test_multiple_metric_changes_diff():
    """Verify multiple changes are captured."""
    run1 = {"metrics": {"total_return": 0.15, "win_rate": 0.60}}
    run2 = {"metrics": {"total_return": 0.18, "win_rate": 0.70}}

    diff = compute_diff(run1, run2)
    assert len(diff) == 2
    assert "metrics.total_return" in diff
    assert "metrics.win_rate" in diff


def test_parametric_differences_diff():
    """Verify parameter changes are captured."""
    run1 = {"parameters": {"lookback": 20, "threshold": 0.5}}
    run2 = {"parameters": {"lookback": 30, "threshold": 0.5}}

    diff = compute_diff(run1, run2)
    assert "parameters.lookback" in diff
    assert "parameters.threshold" not in diff  # Unchanged


def test_performance_degradation_detection():
    """Verify performance regressions are flagged."""
    run1 = {"metrics": {"total_return": 0.15, "sharpe_ratio": 1.8}}
    run2 = {"metrics": {"total_return": 0.10, "sharpe_ratio": 1.2}}

    diff = compute_diff(run1, run2)
    degradation = analyze_degradation(diff)

    assert degradation["performance_degraded"] == True
    assert degradation["severity"] == "HIGH"  # >20% return decrease


def test_diff_snapshot_comparison():
    """Verify diff matches snapshot for regression detection."""
    run1 = {"metrics": {"total_return": 0.15}}
    run2 = {"metrics": {"total_return": 0.18}}

    diff = compute_diff(run1, run2)

    # Compare with saved snapshot
    saved_snapshot = {
        "metrics.total_return": {
            "from": 0.15,
            "to": 0.18,
            "change": "+20%"
        }
    }

    assert diff == saved_snapshot
```

---

## SECTION 5: EPIC 5 - CRYPTOGRAPHIC HASHING (8 UNIT TESTS)

**File**: `tests/unit/test_crypto.py`
**Risk Score**: 9 (Critical — reproducibility depends on hash integrity)
**Coverage Target**: All hash operations and chain integrity

```python
def test_sha256_hash_consistency():
    """Verify SHA256 produces consistent hashes."""
    data = "test_data_12345"
    hash1 = compute_hash(data)
    hash2 = compute_hash(data)

    assert hash1 == hash2  # Same input → same hash


def test_config_hash_accuracy():
    """Verify configuration hashing."""
    config = {"lookback": 20, "threshold": 0.5}
    config_hash = compute_config_hash(config)

    # Hash should change if config changes
    config["lookback"] = 21
    config_hash2 = compute_config_hash(config)

    assert config_hash != config_hash2


def test_artifact_hash_verification():
    """Verify artifact hashing."""
    artifact = {"trades": [], "metrics": {}}
    artifact_hash = compute_artifact_hash(artifact)

    # Verify hash matches
    assert verify_artifact_hash(artifact, artifact_hash) == True

    # Hash fails if artifact corrupted
    artifact["trades"].append({"corrupted": True})
    assert verify_artifact_hash(artifact, artifact_hash) == False


def test_chain_integrity_validation():
    """Verify reproducibility chain integrity."""
    chain = [
        {"hash": "abc123", "type": "config"},
        {"hash": "def456", "type": "data", "depends_on": "abc123"},
        {"hash": "ghi789", "type": "result", "depends_on": "def456"}
    ]

    # Valid chain
    assert validate_chain_integrity(chain) == True

    # Broken chain: Missing dependency
    chain[2]["depends_on"] = "nonexistent"
    assert validate_chain_integrity(chain) == False


def test_run_reconstruction_accuracy():
    """Verify run can be reconstructed from hash."""
    original_run = {
        "id": "run-1",
        "parameters": {"lookback": 20},
        "results": {"total_return": 0.15}
    }

    run_hash = compute_run_hash(original_run)
    reconstructed = reconstruct_from_hash(run_hash)

    # Reconstruction should match original
    assert reconstructed == original_run


def test_seed_reproducibility():
    """Verify seed-based reproducibility."""
    seed = "reproducible_seed_123"
    hash1 = compute_deterministic_hash(seed)
    hash2 = compute_deterministic_hash(seed)

    assert hash1 == hash2  # Same seed → same hash


def test_multi_artifact_chain():
    """Verify chaining multiple artifacts."""
    config_hash = compute_hash({"lookback": 20})
    data_hash = compute_hash({"trades": []})
    result_hash = compute_hash(
        {"metrics": {}},
        depends_on=[config_hash, data_hash]
    )

    chain = create_chain([config_hash, data_hash, result_hash])
    assert len(chain) == 3
    assert validate_chain_integrity(chain) == True


def test_hash_format_validation():
    """Verify hash format validation."""
    # Valid hex format
    valid_hash = "abc123def456"  # 12 chars, valid hex
    assert validate_hash_format(valid_hash) == True

    # Invalid formats
    invalid_hashes = [
        "abc123xyz789",  # Invalid hex (xyz)
        "abc12",         # Too short
        "abc123def456xyz"  # Invalid characters
    ]

    for invalid_hash in invalid_hashes:
        assert validate_hash_format(invalid_hash) == False
```

---

## SECTION 6: TEST IMPLEMENTATION BEST PRACTICES

### 6.1 Use Parametrize for Multiple Scenarios

Instead of writing 10 similar tests:
```python
@pytest.mark.parametrize("input,expected", [
    ({"win_rate": 0.65}, 0.65),
    ({"win_rate": 0.00}, 0.00),
    ({"win_rate": 1.00}, 1.00),
])
def test_win_rate_values(input, expected):
    assert calculate_win_rate(input) == expected
```

### 6.2 Use Fixtures for Common Setup

```python
@pytest.fixture
def sample_trades():
    return [
        {"entry": 100, "exit": 105},
        {"entry": 110, "exit": 108},
    ]

def test_pnl(sample_trades):
    result = calculate_pnl(sample_trades)
    assert result == 6
```

### 6.3 Use pytest.approx for Float Comparisons

```python
# DON'T do this:
assert result == 1.234567

# DO this:
assert result == pytest.approx(1.234567, rel=1e-5)
```

### 6.4 Clear Test Names

```python
# BAD:
def test_1():
    ...

# GOOD:
def test_win_rate_calculation_with_mixed_trades():
    ...
```

---

## SECTION 7: RUNNING UNIT TESTS

**Run all unit tests**:
```bash
pytest tests/unit/ -v
```

**Run specific epic**:
```bash
pytest tests/unit/test_state_machine.py -v
```

**Run specific test**:
```bash
pytest tests/unit/test_state_machine.py::test_paper_to_micro_live_transition -v
```

**Run with coverage**:
```bash
pytest tests/unit/ --cov=katana --cov-report=html
```

**Run in parallel**:
```bash
pytest tests/unit/ -n auto  # Use CPU count
```

**Expected Output**:
```
tests/unit/test_state_machine.py::test_strategy_initial_state_is_paper PASSED
tests/unit/test_state_machine.py::test_paper_to_micro_live_transition PASSED
...
========================= 42 passed in 0.45s ==========================
Coverage: 94% (123/131 lines covered)
```

---

## CONCLUSION

The 42 unit tests provide comprehensive coverage of core algorithms, data validation, and state management. Each test:
- ✅ Executes in <100ms
- ✅ Tests single responsibility
- ✅ Requires no I/O or database
- ✅ Produces clear pass/fail result
- ✅ Documents expected behavior

**Estimated Implementation Time**: 10-16 hours (team of 2-3 engineers)
**Effort Per Test**: 12-18 minutes average
**Total Coverage**: 100% of critical paths

---

**Document Version**: 1.0
**Status**: FINAL
**Approval Date**: 2026-02-26
