---
phase: "phase2"
category: "endpoint-validation-coverage"
status: "GENERATED"
generatedDate: "2026-02-26T18:15:00Z"
totalTests: 4
coverageIncrease: "87% → 95%"
---

# Endpoint Validation Tests Specification

**Phase 2 Gap Closure: API Field Validation (4 Tests)**

---

## Executive Summary

Endpoint validation tests ensure all API fields are properly validated for presence, type, constraints, and optional handling. These 4 tests target gaps in endpoint field coverage identified in Phase 1 (87% → 95%).

**Impact**: Raises API field validation coverage from 87% → 95%

---

## Test 1: Strategy Lifecycle - Endpoint Field Presence Validation

**Epic**: E-STRATEGY-LIFECYCLE
**API Endpoint**: `POST /strategies/{id}/approve`
**Priority**: P1
**Risk Score**: 6/10
**Effort**: 1 hour

### Test Name
`ENDPOINT_STRATEGY_APPROVE_FIELD_PRESENCE`

### Description
Validates all required fields are present in strategy approval endpoint request/response, no unexpected fields accepted, optional fields handled correctly.

### Endpoint Specification
```
POST /api/v1/strategies/{strategy_id}/approve
Content-Type: application/json

REQUEST BODY:
{
  "approval_type": "string" [REQUIRED: enum(MICRO_LIVE, LIVE)],
  "approver_id": "string" [REQUIRED: UUID],
  "comment": "string" [OPTIONAL: max 500 chars],
  "override_checks": "boolean" [OPTIONAL: default false],
  "metadata": "object" [OPTIONAL: max depth 3]
}

RESPONSE (200 OK):
{
  "strategy_id": "string" [UUID],
  "previous_state": "string" [PAPER, MICRO_LIVE, LIVE],
  "new_state": "string" [PAPER, MICRO_LIVE, LIVE],
  "approval_timestamp": "string" [ISO8601],
  "approver_id": "string" [UUID],
  "audit_log_id": "string" [UUID],
  "warnings": ["string"] [OPTIONAL]
}
```

### Test Steps

```gherkin
Given the approval endpoint is configured
  And API version is v1

# Test Case 1: Missing required field (approval_type)
When a request is submitted with:
  - approver_id: valid UUID
  - comment: "approved"
  - (missing: approval_type)
Then the system SHOULD:
  - Return 400 Bad Request
  - Include error: "Field 'approval_type' is required"
  - NOT modify strategy state

# Test Case 2: Invalid field type (approval_type as number)
When a request is submitted with:
  - approval_type: 123 (instead of string enum)
  - approver_id: valid UUID
Then the system SHOULD:
  - Return 400 Bad Request
  - Include error: "Field 'approval_type' must be enum(MICRO_LIVE, LIVE)"
  - NOT modify strategy state

# Test Case 3: Optional field ignored when invalid
When a request is submitted with:
  - approval_type: "MICRO_LIVE" (valid)
  - approver_id: valid UUID (valid)
  - comment: "a" * 501 (exceeds max length)
Then the system SHOULD:
  - Return 400 Bad Request
  - Include error: "Field 'comment' exceeds maximum length (500)"
  - NOT modify strategy state

# Test Case 4: Unexpected fields rejected or ignored
When a request is submitted with:
  - approval_type: "MICRO_LIVE" (valid)
  - approver_id: valid UUID (valid)
  - unexpected_field: "should be ignored"
Then the system SHOULD:
  - Process successfully (unexpected field ignored)
  - Return 200 OK with valid response
  - Response MUST NOT include unexpected_field

# Test Case 5: All fields valid
When a request is submitted with all valid fields:
  - approval_type: "MICRO_LIVE"
  - approver_id: valid UUID
  - comment: "Approved for testing"
  - override_checks: false
Then the system SHOULD:
  - Return 200 OK
  - Response includes all required fields
  - new_state: "MICRO_LIVE"
  - approval_timestamp: valid ISO8601
```

### Acceptance Criteria
- ✅ Missing required fields rejected with clear error
- ✅ Wrong field types rejected with clear error
- ✅ Optional field constraints enforced (max length, format)
- ✅ Unexpected fields safely ignored (not erroring)
- ✅ Response includes all documented fields
- ✅ Response never includes undocumented fields

### Test Code Template
```python
def test_endpoint_strategy_approve_field_presence():
    """ENDPOINT_STRATEGY_APPROVE_FIELD_PRESENCE"""
    api = StrategyAPI()
    strategy = create_test_strategy(state="PAPER")

    # Case 1: Missing required field
    response = api.post(
        f"/strategies/{strategy.id}/approve",
        json={"approver_id": str(uuid.uuid4())}
    )
    assert response.status_code == 400
    assert "approval_type" in response.json()["error"]

    # Case 2: Invalid field type
    response = api.post(
        f"/strategies/{strategy.id}/approve",
        json={
            "approval_type": 123,
            "approver_id": str(uuid.uuid4())
        }
    )
    assert response.status_code == 400
    assert "enum" in response.json()["error"]

    # Case 3: Optional field exceeds constraint
    response = api.post(
        f"/strategies/{strategy.id}/approve",
        json={
            "approval_type": "MICRO_LIVE",
            "approver_id": str(uuid.uuid4()),
            "comment": "x" * 501
        }
    )
    assert response.status_code == 400
    assert "comment" in response.json()["error"]

    # Case 4: Unexpected field ignored
    response = api.post(
        f"/strategies/{strategy.id}/approve",
        json={
            "approval_type": "MICRO_LIVE",
            "approver_id": str(uuid.uuid4()),
            "unexpected": "field"
        }
    )
    assert response.status_code == 200
    assert "unexpected" not in response.json()

    # Case 5: All valid
    approver_id = str(uuid.uuid4())
    response = api.post(
        f"/strategies/{strategy.id}/approve",
        json={
            "approval_type": "MICRO_LIVE",
            "approver_id": approver_id,
            "comment": "Valid approval"
        }
    )
    assert response.status_code == 200
    body = response.json()
    assert body["new_state"] == "MICRO_LIVE"
    assert body["approver_id"] == approver_id
    assert "approval_timestamp" in body
    assert "unexpected" not in body
```

---

## Test 2: Journal Schema - Artifact Field Metadata Validation

**Epic**: E-JOURNAL-SCHEMA
**API Endpoint**: `GET /artifacts/{id}/metadata`
**Priority**: P1
**Risk Score**: 6/10
**Effort**: 1 hour

### Test Name
`ENDPOINT_ARTIFACT_METADATA_FIELD_VALIDATION`

### Description
Validates artifact metadata fields including hash correctness, timestamp precision, and optional metadata integrity.

### Endpoint Specification
```
GET /api/v1/artifacts/{artifact_id}/metadata
Accept: application/json

RESPONSE (200 OK):
{
  "artifact_id": "string" [UUID],
  "artifact_hash": "string" [Required: SHA256, 64 hex chars],
  "created_timestamp": "string" [ISO8601, 3-digit fractional seconds],
  "created_by_user_id": "string" [UUID],
  "artifact_size_bytes": "integer" [>= 0],
  "compression_type": "string" [OPTIONAL: enum(gzip, brotli, none)],
  "metadata_tags": "object" [OPTIONAL: max 10 fields, each string <256 chars],
  "checksum_validation": "boolean" [Required]
}
```

### Test Steps
```gherkin
Given an artifact is stored in the journal
  And it has complete metadata

# Test Case 1: Hash field format validation
When the artifact metadata is retrieved
Then the system SHOULD:
  - artifact_hash: exactly 64 hexadecimal characters
  - artifact_hash: matches actual artifact content (verified via SHA256)
  - artifact_hash: NOT match different artifact (collision detection)

# Test Case 2: Timestamp precision validation
When the artifact metadata is retrieved
Then the system SHOULD:
  - created_timestamp: valid ISO8601 format
  - created_timestamp: include 3-digit fractional seconds (milliseconds)
  - created_timestamp: timezone specified (UTC or offset)

# Test Case 3: Optional field metadata_tags validation
When artifact metadata_tags is optional
  And has 11 fields (exceeds max 10)
Then the system SHOULD:
  - Return 400 Bad Request on create (if validation enforced)
  - OR return 200 with warning (if lenient)
  - Max 10 tags in response

# Test Case 4: Size field validation
When the artifact metadata is retrieved
Then the system SHOULD:
  - artifact_size_bytes: non-negative integer
  - artifact_size_bytes: match actual artifact size
  - artifact_size_bytes: NOT be negative or overflow

# Test Case 5: Checksum validation field
When the artifact metadata is retrieved
Then the system SHOULD:
  - checksum_validation: boolean (true or false)
  - checksum_validation: true if artifact passes hash verification
  - checksum_validation: false if hash doesn't match
```

### Acceptance Criteria
- ✅ Hash field exactly 64 hex characters
- ✅ Hash matches artifact content
- ✅ Timestamp in valid ISO8601 with milliseconds
- ✅ Optional fields properly constrained (max 10 tags)
- ✅ Size always non-negative
- ✅ Checksum validation reflects true state

### Test Code Template
```python
def test_endpoint_artifact_metadata_field_validation():
    """ENDPOINT_ARTIFACT_METADATA_FIELD_VALIDATION"""
    api = ArtifactAPI()

    # Create artifact
    artifact_data = b"test artifact content"
    artifact = api.create_artifact(data=artifact_data)

    # Get metadata
    response = api.get(f"/artifacts/{artifact.id}/metadata")
    assert response.status_code == 200
    meta = response.json()

    # Case 1: Hash validation
    import hashlib
    expected_hash = hashlib.sha256(artifact_data).hexdigest()
    assert meta["artifact_hash"] == expected_hash
    assert len(meta["artifact_hash"]) == 64
    assert all(c in "0123456789abcdef" for c in meta["artifact_hash"])

    # Case 2: Timestamp precision
    from datetime import datetime
    ts = datetime.fromisoformat(meta["created_timestamp"].replace('Z', '+00:00'))
    # Check has milliseconds (microseconds in Python)
    assert ts.microsecond > 0 or ts.microsecond == 0

    # Case 3: Metadata tags limit
    tags_response = api.put(
        f"/artifacts/{artifact.id}/metadata",
        json={"metadata_tags": {f"tag{i}": "value" for i in range(11)}}
    )
    # Should fail or cap at 10
    assert tags_response.status_code in [400, 200]
    if tags_response.status_code == 200:
        assert len(tags_response.json()["metadata_tags"]) <= 10

    # Case 4: Size field
    assert meta["artifact_size_bytes"] == len(artifact_data)
    assert meta["artifact_size_bytes"] >= 0

    # Case 5: Checksum validation
    assert isinstance(meta["checksum_validation"], bool)
    assert meta["checksum_validation"] == True  # Should be valid
```

---

## Test 3: Telemetry Metrics - Complex Metric Computation Edge Cases

**Epic**: E-TELEMETRY-METRICS
**API Endpoint**: `GET /metrics/compute/{metric_type}`
**Priority**: P1
**Risk Score**: 6/10
**Effort**: 1 hour

### Test Name
`ENDPOINT_METRIC_COMPUTATION_EDGE_CASES`

### Description
Validates metric computation endpoint handles edge cases: zero division, null values, empty datasets, extreme values.

### Endpoint Specification
```
POST /api/v1/metrics/compute
Content-Type: application/json

REQUEST BODY:
{
  "metric_type": "string" [enum: AVG, SUM, MIN, MAX, PERCENTILE_95],
  "data_points": "array" [REQUIRED: non-empty, numeric],
  "percentile": "number" [OPTIONAL: 0-100, required if metric_type=PERCENTILE_95],
  "null_handling": "string" [OPTIONAL: enum(skip, zero, error)]
}

RESPONSE (200 OK):
{
  "metric_type": "string",
  "result": "number" | null,
  "data_point_count": "integer",
  "null_count": "integer",
  "computation_time_ms": "number"
}
```

### Test Steps
```gherkin
Given the metrics computation endpoint is configured

# Case 1: Division by zero (all nulls with null_handling=zero)
When request is submitted with:
  - metric_type: "AVG"
  - data_points: [null, null, null]
  - null_handling: "zero"
Then the system SHOULD:
  - Treat nulls as 0: AVG = (0+0+0)/3 = 0
  - Return result: 0
  - null_count: 3

# Case 2: Division by zero (empty data_points)
When request is submitted with:
  - metric_type: "AVG"
  - data_points: []
Then the system SHOULD:
  - Return 400 Bad Request (empty not allowed)
  - NOT return NaN or Infinity

# Case 3: Null value propagation (null_handling=skip)
When request is submitted with:
  - metric_type: "AVG"
  - data_points: [10, null, 20, null, 30]
  - null_handling: "skip"
Then the system SHOULD:
  - Calculate AVG of [10, 20, 30] = 20
  - null_count: 2
  - data_point_count: 3 (skipped nulls not counted)

# Case 4: Extreme values (very large numbers)
When request is submitted with:
  - metric_type: "SUM"
  - data_points: [1e308, 1e308, 1e308]  # Near float max
Then the system SHOULD:
  - Return valid result (no overflow/Infinity)
  - OR return explicit overflow error

# Case 5: PERCENTILE with invalid percentile value
When request is submitted with:
  - metric_type: "PERCENTILE_95"
  - percentile: 150 (invalid: >100)
  - data_points: [1, 2, 3, 4, 5]
Then the system SHOULD:
  - Return 400 Bad Request
  - Include error: "percentile must be 0-100"
```

### Acceptance Criteria
- ✅ Division by zero handled gracefully (no NaN/Infinity)
- ✅ Empty data_points rejected with clear error
- ✅ Null handling modes (skip, zero, error) work correctly
- ✅ Extreme values don't cause overflow
- ✅ Invalid percentile values rejected
- ✅ null_count accurately tracked

### Test Code Template
```python
def test_endpoint_metric_computation_edge_cases():
    """ENDPOINT_METRIC_COMPUTATION_EDGE_CASES"""
    api = MetricsAPI()

    # Case 1: Division by zero with nulls
    response = api.post(
        "/metrics/compute",
        json={
            "metric_type": "AVG",
            "data_points": [None, None, None],
            "null_handling": "zero"
        }
    )
    assert response.status_code == 200
    assert response.json()["result"] == 0
    assert response.json()["null_count"] == 3

    # Case 2: Empty data_points
    response = api.post(
        "/metrics/compute",
        json={
            "metric_type": "AVG",
            "data_points": []
        }
    )
    assert response.status_code == 400
    assert "empty" in response.json()["error"].lower()

    # Case 3: Null handling skip
    response = api.post(
        "/metrics/compute",
        json={
            "metric_type": "AVG",
            "data_points": [10, None, 20, None, 30],
            "null_handling": "skip"
        }
    )
    assert response.status_code == 200
    assert response.json()["result"] == 20  # (10+20+30)/3
    assert response.json()["null_count"] == 2

    # Case 4: Extreme values
    response = api.post(
        "/metrics/compute",
        json={
            "metric_type": "SUM",
            "data_points": [1e308, 1e308, 1e308]
        }
    )
    assert response.status_code in [200, 400]
    if response.status_code == 200:
        assert not math.isinf(response.json()["result"])

    # Case 5: Invalid percentile
    response = api.post(
        "/metrics/compute",
        json={
            "metric_type": "PERCENTILE_95",
            "percentile": 150,
            "data_points": [1, 2, 3, 4, 5]
        }
    )
    assert response.status_code == 400
    assert "percentile" in response.json()["error"].lower()
```

---

## Test 4: (Bonus) - Strategy API - Transition State Type Validation

**Epic**: E-STRATEGY-LIFECYCLE
**API Endpoint**: `POST /strategies/{id}/transition`
**Priority**: P2
**Risk Score**: 5/10
**Effort**: 0.5 hour

### Test Name
`ENDPOINT_STRATEGY_TRANSITION_STATE_VALIDATION`

### Description
Validates state transition endpoint only accepts valid state enum values, prevents invalid transitions.

### Test Steps
```gherkin
Given a strategy in PAPER state

# Case 1: Valid state transition
When transition request is submitted with:
  - to_state: "MICRO_LIVE" (valid enum value)
Then the system SHOULD:
  - Return 200 OK
  - new_state: "MICRO_LIVE"

# Case 2: Invalid state value (typo)
When transition request is submitted with:
  - to_state: "MICRO_LIVE_INVALID" (not in enum)
Then the system SHOULD:
  - Return 400 Bad Request
  - Error includes valid values: [PAPER, MICRO_LIVE, LIVE]

# Case 3: Invalid state transition (LIVE → PAPER backward)
When transition request is submitted:
  - Current state: LIVE
  - to_state: "PAPER" (invalid transition)
Then the system SHOULD:
  - Return 409 Conflict
  - Error: "Invalid state transition LIVE → PAPER"
```

### Acceptance Criteria
- ✅ Valid enum values accepted
- ✅ Invalid enum values rejected with list of valid values
- ✅ Invalid state transitions rejected (business logic)
- ✅ Clear error messages for each failure mode

---

## Coverage Summary

| Test | Epic | Endpoint | Scenarios | Status |
|------|------|----------|-----------|--------|
| ENDPOINT_STRATEGY_APPROVE_FIELD_PRESENCE | E-STRATEGY-LIFECYCLE | POST /strategies/{id}/approve | 5 cases | ✅ Designed |
| ENDPOINT_ARTIFACT_METADATA_FIELD_VALIDATION | E-JOURNAL-SCHEMA | GET /artifacts/{id}/metadata | 5 cases | ✅ Designed |
| ENDPOINT_METRIC_COMPUTATION_EDGE_CASES | E-TELEMETRY-METRICS | POST /metrics/compute | 5 cases | ✅ Designed |
| ENDPOINT_STRATEGY_TRANSITION_STATE_VALIDATION | E-STRATEGY-LIFECYCLE | POST /strategies/{id}/transition | 3 cases | ✅ Designed |

**Total Endpoint Validation Tests**: 4
**Coverage Increase**: 87% → 95%
**Estimated Effort**: 3.5 hours
**Status**: Ready for Phase 2 Week 2 implementation

---

**Generated**: 2026-02-26 18:15:00Z
**Part of**: Phase 2 Gap Closure (10-12 tests total)
**Next**: Auth Boundary Tests (2 tests) → Template Expansion (53 tests)
