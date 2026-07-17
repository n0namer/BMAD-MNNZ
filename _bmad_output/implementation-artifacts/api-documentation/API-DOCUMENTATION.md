# API Documentation - Katana VectorBT Phase 1

**Project:** Katana VectorBT
**Version:** 1.0.0
**Date:** 2026-02-26
**Status:** DRAFT (Ready for Phase 1 Implementation)
**OpenAPI Spec Version:** 3.1.0

---

## Table of Contents

1. [Overview](#overview)
2. [Authentication & Authorization](#authentication--authorization)
3. [Error Handling](#error-handling)
4. [Common Schemas](#common-schemas)
5. [Endpoints by Epic](#endpoints-by-epic)
6. [Field Validation Rules](#field-validation-rules)
7. [Integration Patterns](#integration-patterns)
8. [OpenAPI 3.1 Specification](#openapi-31-specification)

---

## Overview

### API Purpose

The Katana VectorBT API provides programmatic access to:
- Strategy lifecycle management (draft → pending → approved → active → completed)
- Run journal data capture and reproducibility
- Telemetry metrics and performance tracking
- Strategy comparison and analysis
- Complete audit trails for compliance

### Base URL

```
http://localhost:5000/api/v1
```

### API Characteristics

- **Protocol:** REST with JSON payloads
- **Authentication:** Bearer Token (JWT)
- **Response Format:** JSON with consistent error structure
- **Versioning:** URL-based (/api/v1)
- **Database Isolation:** Connection pooling with transaction isolation (READ_COMMITTED minimum)
- **WCAG AA Compliance:** All responses include machine-readable metadata for accessibility

---

## Authentication & Authorization

### Bearer Token (JWT)

All endpoints require `Authorization: Bearer <token>` header.

```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Token Claims:**
```json
{
  "sub": "user:owner-operator",
  "role": "admin",
  "iat": 1234567890,
  "exp": 1234654290
}
```

### Roles & Permissions

| Role | Permissions | Scope |
|------|------------|-------|
| `admin` | All operations | Full API access |
| `viewer` | Read-only (GET) | Cannot create/modify strategies |
| `analyst` | Read + Compare | Cannot approve strategies |
| `approver` | Read + Approve | Can approve pending strategies |

### Authorization Rules

- **Strategy ownership:** Only creator can edit (unless approved)
- **Approval workflow:** Only `approver` role can approve pending strategies
- **Audit access:** All audit trails visible to `admin` + `approver`
- **Run data:** Visible to `viewer`+ (all read roles)

---

## Error Handling

### Error Response Format

All errors follow this standardized structure:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Field validation failed",
    "status": 400,
    "timestamp": "2026-02-26T14:30:00Z",
    "request_id": "req_abc123def456",
    "details": [
      {
        "field": "strategy_parameters.sl_multiplier",
        "constraint": "Range validation failed",
        "expected": "0.5 ≤ value ≤ 5.0",
        "received": 10.5
      }
    ],
    "wcag_summary": "Field sl_multiplier: expected numeric range [0.5, 5.0], got 10.5"
  }
}
```

### HTTP Status Codes

| Status | Meaning | Recovery |
|--------|---------|----------|
| 200 | Success | None needed |
| 201 | Created | Resource created, use Location header |
| 204 | No Content | Success (no response body) |
| 400 | Bad Request | Validate input per error details |
| 401 | Unauthorized | Check token validity and role |
| 403 | Forbidden | Insufficient permissions for this operation |
| 404 | Not Found | Resource doesn't exist |
| 409 | Conflict | State conflict (e.g., invalid state transition) |
| 422 | Unprocessable Entity | Semantic validation failed (see details) |
| 500 | Server Error | Retry with exponential backoff |
| 503 | Service Unavailable | Retry after service recovery |

### Common Error Codes

| Code | HTTP | Meaning | Remediation |
|------|------|---------|-------------|
| `VALIDATION_ERROR` | 400 | Field validation failed | Check constraints in details array |
| `STATE_TRANSITION_INVALID` | 409 | Invalid state transition | Verify current state + allowed transitions |
| `AUTHORIZATION_FAILED` | 403 | Permission denied | Check token role |
| `RESOURCE_NOT_FOUND` | 404 | Strategy/run doesn't exist | Verify ID |
| `CONFLICT_DB_ISOLATION` | 409 | Concurrent modification detected | Retry operation |
| `WCAG_COMPLIANCE_VIOLATION` | 422 | Accessibility requirement violated | See wcag_summary field |

---

## Common Schemas

### Base Schema: Strategy

```typescript
interface Strategy {
  strategy_id: string;           // UUID, immutable
  name: string;                  // 1-255 chars, alphanumeric + spaces
  description?: string;          // Optional, up to 2000 chars
  created_at: ISO8601DateTime;   // Immutable
  updated_at: ISO8601DateTime;   // Updated on each modification
  created_by: string;            // user_id (immutable)
  state: StrategyState;          // DRAFT | PENDING | APPROVED | ACTIVE | COMPLETED | CANCELLED | KILLED
  version: integer;              // Incremented on each modification
  approval_status: ApprovalStatus; // For audit trail
}

enum StrategyState {
  DRAFT = "DRAFT",               // Initial state, editable
  PENDING = "PENDING",           // Awaiting approval review
  APPROVED = "APPROVED",         // Ready for execution
  ACTIVE = "ACTIVE",             // Currently running
  COMPLETED = "COMPLETED",       // Finished successfully
  CANCELLED = "CANCELLED",       // Manually cancelled
  KILLED = "KILLED"              // Kill-switch activated
}

interface ApprovalStatus {
  status: "pending" | "approved" | "rejected";
  approved_at?: ISO8601DateTime;
  rejected_at?: ISO8601DateTime;
  approver_id?: string;
  rejection_reason?: string;
  rejection_comment?: string;
  resubmission_count: integer;   // Tracks how many times resubmitted
}
```

### Base Schema: StrategyParameters

```typescript
interface StrategyParameters {
  // Profile & Sizing (required)
  strategy_profile: "stable" | "return" | "rocket";

  // DFF (Distance Function Factory) - Flat per-role structure
  dff_sl_source_type?: "atr" | "stddev" | "bb_half" | "range" | "fixed_pct" | "corwin_schultz";
  dff_sl_period?: integer;       // If source_type requires
  dff_sl_lookback?: integer;
  dff_sl_pct?: number;            // 0-1 (e.g., 0.008 = 0.8%)
  dff_sl_stdev?: number;
  dff_sl_timeframe?: string;      // "1m" | "5m" | "15m" | "1h" | "4h" | "1d"
  sl_multiplier: number;          // stable/return: 0.5-5.0x, rocket: 0.5-10.0x

  dff_tp_source_type?: "atr" | "stddev" | "bb_half" | "range" | "fixed_pct" | "corwin_schultz";
  dff_tp_period?: integer;
  dff_tp_lookback?: integer;
  dff_tp_pct?: number;
  dff_tp_stdev?: number;
  dff_tp_timeframe?: string;
  tp_multiplier: number;          // stable/return: 0.5-5.0x, rocket: 0.5-10.0x

  dff_be_source_type?: string;
  dff_be_period?: integer;
  dff_be_lookback?: integer;
  dff_be_pct?: number;
  dff_be_stdev?: number;
  dff_be_timeframe?: string;
  be_multiplier: number;          // 0.5-5.0x

  dff_trail_source_type?: string;
  dff_trail_period?: integer;
  dff_trail_lookback?: integer;
  dff_trail_pct?: number;
  dff_trail_stdev?: number;
  dff_trail_timeframe?: string;
  trail_multiplier: number;       // 0.5-5.0x

  // Risk Management
  max_leverage: number;           // 1.0-5.0 (global cap: 5x, non-optimizable)
  position_sizing: "kelly" | "fixed" | "atr_based";
  max_loss_per_trade: number;     // Percent of account (0-5%)
}
```

### Base Schema: RunJournal

```typescript
interface RunJournal {
  run_id: string;                // UUID
  strategy_id: string;           // FK to strategy
  journal_version: "3.0";        // Version of schema

  manifest: ManifestJSON;        // Metadata + execution context
  summary: SummaryJSON;          // High-level results (v3.0)
  events: EventsNDJSON;          // Streaming event log

  created_at: ISO8601DateTime;
  completed_at?: ISO8601DateTime;
  status: "running" | "completed" | "failed";
}

interface ManifestJSON {
  run_id: string;
  strategy_id: string;
  strategy_name: string;
  version: string;               // Strategy version at run time

  start_time: ISO8601DateTime;
  end_time?: ISO8601DateTime;

  parameters: object;            // Full parameter snapshot
  environment: {
    python_version: string;
    vectorbt_version: string;
    data_source: string;
    backtest_period: { start: date; end: date };
  };

  seed: integer;                 // For reproducibility
  data_hash: string;             // SHA256 of input data (frozen dataset detection)
}

interface SummaryJSON {
  run_id: string;
  strategy_id: string;

  // High-level metrics
  total_runs: integer;
  win_rate: number;              // 0-1
  sharpe_ratio: number;
  max_drawdown: number;
  final_equity: number;
  profit_factor: number;

  // Quality gates
  backtest_realism_score: number; // 0-100
  live_trading_readiness: boolean;
  data_freshness: ISO8601DateTime;

  // Degradation tracking
  degradation_rules_applied: string[];
  degradation_factor: number;
  estimated_live_performance: number; // Degradation-adjusted
}

interface EventsNDJSON {
  // Each line is a JSON object:
  // {"type": "trade", "timestamp": "...", "data": {...}}
  // {"type": "signal", "timestamp": "...", "data": {...}}
  // {"type": "error", "timestamp": "...", "data": {...}}
}
```

### Base Schema: TelemetryMetrics

```typescript
interface TelemetryMetrics {
  timestamp: ISO8601DateTime;
  metric_type: "time_to_status" | "mtif" | "log_diving_rate";

  // Time-to-Status: duration from state A → state B
  state_from?: StrategyState;
  state_to?: StrategyState;
  duration_seconds?: integer;

  // MTIF: Mean Time In Flight (ACTIVE → completion)
  mtif_seconds?: integer;
  mtif_percentile?: "p50" | "p95" | "p99";

  // Log Diving Rate: error logs requiring investigation
  error_count?: integer;
  error_rate_per_hour?: number;
  error_severity_class?: "warn" | "error" | "critical";

  strategy_id?: string;
  run_id?: string;
}
```

---

## Endpoints by Epic

### Epic 1: E-STRATEGY-LIFECYCLE

#### POST /strategies

**Create a new strategy (DRAFT state)**

```http
POST /api/v1/strategies
Content-Type: application/json
Authorization: Bearer <token>

{
  "name": "RSI+MA Cross Strategy v1",
  "description": "Combined RSI oversold + MA cross confirmation",
  "parameters": {
    "strategy_profile": "return",
    "dff_sl_source_type": "atr",
    "dff_sl_period": 14,
    "sl_multiplier": 2.0,
    "dff_tp_source_type": "atr",
    "dff_tp_period": 14,
    "tp_multiplier": 3.0,
    "max_leverage": 3.0,
    "position_sizing": "kelly",
    "max_loss_per_trade": 2.5
  }
}
```

**Response (201 Created):**

```json
{
  "strategy_id": "strat_abc123def456",
  "name": "RSI+MA Cross Strategy v1",
  "state": "DRAFT",
  "version": 1,
  "created_at": "2026-02-26T14:30:00Z",
  "updated_at": "2026-02-26T14:30:00Z",
  "created_by": "user:owner-operator",
  "approval_status": {
    "status": "pending",
    "resubmission_count": 0
  }
}
```

**Validation Rules:**
- `name`: Required, 1-255 chars, alphanumeric + spaces/hyphens
- `parameters.strategy_profile`: Required, must be one of: `stable`, `return`, `rocket`
- `parameters.sl_multiplier`: Must be 0.5-5.0 (rocket: 0.5-10.0)
- `parameters.max_leverage`: Must be 1.0-5.0
- DFF validation: If `*_source_type` is set, all required params for that type must be present

**Error Examples:**
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "status": 400,
    "details": [
      {
        "field": "parameters.sl_multiplier",
        "constraint": "Range validation",
        "expected": "0.5 ≤ value ≤ 5.0",
        "received": 10.5
      },
      {
        "field": "parameters.dff_sl_source_type",
        "constraint": "Conditional requirement",
        "expected": "dff_sl_period must be set if dff_sl_source_type='atr'",
        "received": null
      }
    ]
  }
}
```

---

#### GET /strategies/{strategy_id}

**Retrieve strategy details**

```http
GET /api/v1/strategies/strat_abc123def456
Authorization: Bearer <token>
```

**Response (200 OK):**

```json
{
  "strategy_id": "strat_abc123def456",
  "name": "RSI+MA Cross Strategy v1",
  "description": "Combined RSI oversold + MA cross confirmation",
  "state": "DRAFT",
  "version": 1,
  "created_at": "2026-02-26T14:30:00Z",
  "updated_at": "2026-02-26T14:30:00Z",
  "created_by": "user:owner-operator",
  "parameters": { /* full parameter set */ },
  "approval_status": {
    "status": "pending",
    "resubmission_count": 0
  }
}
```

---

#### PUT /strategies/{strategy_id}

**Update strategy (DRAFT state only)**

```http
PUT /api/v1/strategies/strat_abc123def456
Content-Type: application/json
Authorization: Bearer <token>

{
  "name": "RSI+MA Cross Strategy v1.1",
  "parameters": {
    "dff_sl_multiplier": 2.5
  }
}
```

**Response (200 OK):**
- Updated strategy object with incremented version
- Creates audit event

**Validation:**
- Only allowed in DRAFT state
- Creator or admin can update

---

#### POST /strategies/{strategy_id}/submit

**Submit strategy for approval (DRAFT → PENDING)**

```http
POST /api/v1/strategies/strat_abc123def456/submit
Authorization: Bearer <token>
Content-Type: application/json

{
  "notes": "Ready for review. Tested on 2020-2022 data."
}
```

**Response (200 OK):**

```json
{
  "strategy_id": "strat_abc123def456",
  "state": "PENDING",
  "version": 2,
  "approval_status": {
    "status": "pending",
    "resubmission_count": 0
  }
}
```

**Validation:**
- Strategy must be in DRAFT state
- All required parameters must be set
- WCAG summary in response includes accessibility notes

---

#### POST /strategies/{strategy_id}/approve

**Approve pending strategy (PENDING → APPROVED)**

```http
POST /api/v1/strategies/strat_abc123def456/approve
Authorization: Bearer <token>
Content-Type: application/json

{
  "comments": "Looks good. Parameters within risk limits."
}
```

**Response (200 OK):**

```json
{
  "strategy_id": "strat_abc123def456",
  "state": "APPROVED",
  "approval_status": {
    "status": "approved",
    "approved_at": "2026-02-26T15:00:00Z",
    "approver_id": "user:approver",
    "resubmission_count": 0
  }
}
```

**Validation:**
- Requires `approver` role
- Strategy must be in PENDING state
- Creates audit event with approver ID

---

#### POST /strategies/{strategy_id}/reject

**Reject strategy (PENDING → DRAFT)**

```http
POST /api/v1/strategies/strat_abc123def456/reject
Authorization: Bearer <token>
Content-Type: application/json

{
  "reason": "tp_multiplier exceeds stable profile limits",
  "detailed_feedback": "For stable profile, tp_multiplier should be ≤ 3.0"
}
```

**Response (200 OK):**

```json
{
  "strategy_id": "strat_abc123def456",
  "state": "DRAFT",
  "approval_status": {
    "status": "rejected",
    "rejected_at": "2026-02-26T15:05:00Z",
    "rejection_reason": "tp_multiplier exceeds stable profile limits",
    "rejection_comment": "For stable profile, tp_multiplier should be ≤ 3.0",
    "resubmission_count": 0
  }
}
```

---

#### POST /strategies/{strategy_id}/execute

**Execute approved strategy (APPROVED → ACTIVE)**

```http
POST /api/v1/strategies/strat_abc123def456/execute
Authorization: Bearer <token>
Content-Type: application/json

{
  "mode": "backtest",              // "backtest" | "paper" | "live"
  "backtest_period": {
    "start": "2024-01-01",
    "end": "2024-12-31"
  },
  "symbol": "AAPL",
  "timeframe": "1h"
}
```

**Response (201 Created):**

```json
{
  "run_id": "run_xyz789abc123",
  "strategy_id": "strat_abc123def456",
  "state": "ACTIVE",
  "status": "running",
  "created_at": "2026-02-26T15:10:00Z",
  "estimated_completion": "2026-02-26T16:30:00Z",
  "progress_percent": 0
}
```

**Validation:**
- Strategy must be in APPROVED state
- Backtest period start < end
- Symbol and timeframe valid

---

#### POST /strategies/{strategy_id}/kill

**Activate kill-switch (any state → KILLED)**

```http
POST /api/v1/strategies/strat_abc123def456/kill
Authorization: Bearer <token>
Content-Type: application/json

{
  "reason": "Manual stop - parameters producing losses"
}
```

**Response (200 OK):**

```json
{
  "strategy_id": "strat_abc123def456",
  "state": "KILLED",
  "final_state": "KILLED",
  "killed_at": "2026-02-26T15:15:00Z",
  "kill_reason": "Manual stop - parameters producing losses",
  "cleanup_completed": true,
  "cleanup_logs": []
}
```

**Validation:**
- Can be called from any state
- Creates immutable audit trail
- Triggers cleanup operations

---

### Epic 2: E-JOURNAL-SCHEMA

#### GET /runs/{run_id}/journal/manifest

**Retrieve run manifest (metadata + execution context)**

```http
GET /api/v1/runs/run_xyz789abc123/journal/manifest
Authorization: Bearer <token>
```

**Response (200 OK):**

```json
{
  "run_id": "run_xyz789abc123",
  "strategy_id": "strat_abc123def456",
  "strategy_name": "RSI+MA Cross Strategy v1",
  "version": "1.0.0",
  "start_time": "2026-02-26T15:10:00Z",
  "end_time": "2026-02-26T16:30:00Z",
  "parameters": {
    "strategy_profile": "return",
    "dff_sl_source_type": "atr",
    "dff_sl_period": 14,
    "sl_multiplier": 2.0
  },
  "environment": {
    "python_version": "3.12.0",
    "vectorbt_version": "0.26.2",
    "data_source": "yfinance",
    "backtest_period": {
      "start": "2024-01-01",
      "end": "2024-12-31"
    }
  },
  "seed": 42,
  "data_hash": "sha256:abcd1234efgh5678ijkl9012mnop3456"
}
```

---

#### GET /runs/{run_id}/journal/summary

**Retrieve run summary (high-level results v3.0)**

```http
GET /api/v1/runs/run_xyz789abc123/journal/summary
Authorization: Bearer <token>
```

**Response (200 OK):**

```json
{
  "run_id": "run_xyz789abc123",
  "strategy_id": "strat_abc123def456",
  "journal_version": "3.0",
  "total_runs": 245,
  "win_rate": 0.548,
  "sharpe_ratio": 1.24,
  "max_drawdown": 0.156,
  "final_equity": 124500.00,
  "profit_factor": 1.68,
  "backtest_realism_score": 87,
  "live_trading_readiness": true,
  "data_freshness": "2024-12-31T16:00:00Z",
  "degradation_rules_applied": [
    "slippage_2bps",
    "commission_0.1pct"
  ],
  "degradation_factor": 0.92,
  "estimated_live_performance": 114340.00,
  "metadata": {
    "completed_at": "2026-02-26T16:30:00Z"
  }
}
```

---

#### GET /runs/{run_id}/journal/events

**Stream run events (NDJSON format)**

```http
GET /api/v1/runs/run_xyz789abc123/journal/events
Authorization: Bearer <token>
Accept: application/x-ndjson
```

**Response (200 OK, streaming):**

```ndjson
{"type":"trade","timestamp":"2024-01-02T10:30:00Z","data":{"symbol":"AAPL","entry_price":185.50,"quantity":100,"signal":"ma_cross_confirm"}}
{"type":"trade","timestamp":"2024-01-02T14:45:00Z","data":{"symbol":"AAPL","exit_price":187.20,"exit_reason":"tp_hit"}}
{"type":"signal","timestamp":"2024-01-03T09:15:00Z","data":{"symbol":"AAPL","confidence":0.89,"conditions":["ma_cross_confirm","mtf_trend"]}}
{"type":"error","timestamp":"2024-01-15T16:00:00Z","data":{"level":"warn","message":"Data gap detected - market closed","recovery":"continue_next_day"}}
```

**Event Schema:**
```typescript
type JournalEvent =
  | TradeEvent
  | SignalEvent
  | ErrorEvent
  | StateChangeEvent;

interface TradeEvent {
  type: "trade";
  timestamp: ISO8601DateTime;
  data: {
    symbol: string;
    entry_price: number;
    quantity: integer;
    exit_price?: number;
    exit_reason?: string;
    entry_signal?: string;
  };
}

interface SignalEvent {
  type: "signal";
  timestamp: ISO8601DateTime;
  data: {
    symbol: string;
    signal_type: string;
    confidence: number;     // 0-1
    conditions: string[];
  };
}

interface ErrorEvent {
  type: "error";
  timestamp: ISO8601DateTime;
  data: {
    level: "warn" | "error" | "critical";
    message: string;
    recovery?: string;
  };
}
```

---

#### POST /runs/{run_id}/verify-reproducibility

**Verify run reproducibility with captured data**

```http
POST /api/v1/runs/run_xyz789abc123/verify-reproducibility
Authorization: Bearer <token>
Content-Type: application/json

{
  "tolerance_percent": 0.01,     // ±0.01% acceptable difference
  "include_detailed_diff": true
}
```

**Response (200 OK):**

```json
{
  "run_id": "run_xyz789abc123",
  "reproducibility_score": 98,   // 0-100
  "reproducible": true,
  "verification_time_seconds": 124,
  "details": {
    "code_version_match": true,
    "parameters_match": true,
    "data_hash_match": true,
    "environment_match": true,
    "results_within_tolerance": true
  },
  "metrics_comparison": {
    "original_sharpe": 1.24,
    "reproduction_sharpe": 1.241,
    "diff_percent": 0.08,
    "within_tolerance": true
  }
}
```

---

### Epic 3: E-TELEMETRY-METRICS

#### GET /metrics/time-to-status

**Retrieve Time-to-Status metrics**

```http
GET /api/v1/metrics/time-to-status?period=7d&aggregation=hourly
Authorization: Bearer <token>
```

**Response (200 OK):**

```json
{
  "metric": "time_to_status",
  "period": "7d",
  "aggregation": "hourly",
  "data": [
    {
      "timestamp": "2026-02-20T00:00:00Z",
      "transitions": [
        {
          "from": "DRAFT",
          "to": "PENDING",
          "p50": 3600,       // seconds
          "p95": 7200,
          "p99": 14400,
          "count": 42
        },
        {
          "from": "PENDING",
          "to": "APPROVED",
          "p50": 1800,
          "p95": 3600,
          "p99": 7200,
          "count": 38
        }
      ]
    }
  ],
  "summary": {
    "total_transitions": 156,
    "avg_time_to_status": 3720,
    "slowest_transition": "DRAFT → PENDING"
  }
}
```

---

#### GET /metrics/mtif

**Retrieve Mean Time In Flight metrics**

```http
GET /api/v1/metrics/mtif?period=30d&percentile=p95
Authorization: Bearer <token>
```

**Response (200 OK):**

```json
{
  "metric": "mtif",
  "period": "30d",
  "data": {
    "overall_mtif_seconds": 86400,   // 24 hours
    "percentiles": {
      "p50": 43200,      // 12 hours
      "p95": 129600,     // 36 hours
      "p99": 172800      // 48 hours
    },
    "by_strategy": [
      {
        "strategy_id": "strat_abc123",
        "strategy_name": "RSI+MA Cross",
        "mtif_seconds": 72000,         // 20 hours
        "runs_count": 8
      }
    ],
    "outliers_detected": [
      {
        "run_id": "run_xyz789",
        "mtif_seconds": 432000,        // 120 hours - outlier
        "reason": "Suspected backlog delay"
      }
    ]
  }
}
```

---

#### GET /metrics/log-diving-rate

**Retrieve Log Diving Rate metrics**

```http
GET /api/v1/metrics/log-diving-rate?period=7d&severity=error
Authorization: Bearer <token>
```

**Response (200 OK):**

```json
{
  "metric": "log_diving_rate",
  "period": "7d",
  "severity_filter": "error",
  "data": [
    {
      "timestamp": "2026-02-20T00:00:00Z",
      "error_count": 12,
      "rate_per_hour": 0.5,
      "classification": {
        "data_gap": 5,
        "parameter_invalid": 3,
        "timeout": 2,
        "other": 2
      }
    }
  ],
  "summary": {
    "total_errors": 84,
    "avg_rate_per_hour": 0.5,
    "trend": "stable",
    "critical_errors": 0
  }
}
```

---

#### GET /dashboard/metrics

**Retrieve all 3 core metrics for dashboard display**

```http
GET /api/v1/dashboard/metrics?period=7d
Authorization: Bearer <token>
```

**Response (200 OK):**

```json
{
  "timestamp": "2026-02-26T14:30:00Z",
  "period": "7d",
  "metrics": {
    "time_to_status": {
      "avg_seconds": 3720,
      "slowest": "DRAFT → PENDING",
      "trend": "↓ improving"
    },
    "mtif": {
      "avg_seconds": 86400,
      "p95": 129600,
      "trend": "→ stable"
    },
    "log_diving_rate": {
      "avg_per_hour": 0.5,
      "critical_count": 0,
      "trend": "↓ improving"
    }
  }
}
```

---

#### POST /metrics/alerts/create

**Create alert rule based on metric threshold**

```http
POST /api/v1/metrics/alerts
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "MTIF Threshold Alert",
  "metric": "mtif",
  "threshold": 172800,           // 48 hours
  "comparison": "gt",            // greater than
  "channel": "slack",
  "webhook_url": "https://hooks.slack.com/...",
  "enabled": true,
  "silence_minutes": 60          // Deduplicate alerts
}
```

**Response (201 Created):**

```json
{
  "alert_id": "alert_123abc",
  "name": "MTIF Threshold Alert",
  "metric": "mtif",
  "threshold": 172800,
  "channel": "slack",
  "created_at": "2026-02-26T14:35:00Z",
  "enabled": true,
  "test_fired": false
}
```

---

### Epic 4: E-COMPARE-WORKFLOW

#### POST /compare/runs

**Compare two strategy runs**

```http
POST /api/v1/compare/runs
Authorization: Bearer <token>
Content-Type: application/json

{
  "run_id_1": "run_xyz789abc123",
  "run_id_2": "run_abc456def789"
}
```

**Response (200 OK):**

```json
{
  "comparison_id": "comp_001",
  "run_id_1": "run_xyz789abc123",
  "run_id_2": "run_abc456def789",
  "timestamp": "2026-02-26T14:40:00Z",
  "similarity_score": 87,        // 0-100%
  "delta": [
    {
      "field": "parameters.dff_sl_multiplier",
      "type": "modified",
      "value_1": 2.0,
      "value_2": 2.5,
      "change_percent": 25
    },
    {
      "field": "summary.sharpe_ratio",
      "type": "metric",
      "value_1": 1.24,
      "value_2": 1.31,
      "change_percent": 5.6,
      "impact": "positive"
    }
  ],
  "summary": {
    "parameters_changed": 1,
    "metrics_changed": 3,
    "overall_improvement": true
  }
}
```

---

#### GET /compare/{comparison_id}

**Retrieve detailed comparison**

```http
GET /api/v1/compare/comp_001
Authorization: Bearer <token>
```

**Response (200 OK):**

```json
{
  "comparison_id": "comp_001",
  "run_1": {
    "run_id": "run_xyz789abc123",
    "strategy_name": "RSI+MA Cross v1",
    "parameters": { /* ... */ },
    "summary": {
      "sharpe_ratio": 1.24,
      "max_drawdown": 0.156,
      "profit_factor": 1.68
    }
  },
  "run_2": {
    "run_id": "run_abc456def789",
    "strategy_name": "RSI+MA Cross v1.1",
    "parameters": { /* ... */ },
    "summary": {
      "sharpe_ratio": 1.31,
      "max_drawdown": 0.142,
      "profit_factor": 1.78
    }
  },
  "delta_detailed": [
    /* Full list of differences */
  ],
  "metrics_focused": {
    "sharpe_ratio": { "change": 0.07, "percent": 5.6, "better": "run_2" },
    "max_drawdown": { "change": -0.014, "percent": -9.0, "better": "run_2" },
    "profit_factor": { "change": 0.10, "percent": 6.0, "better": "run_2" }
  }
}
```

---

#### GET /compare/{comparison_id}/export

**Export comparison as CSV or JSON**

```http
GET /api/v1/compare/comp_001/export?format=csv
Authorization: Bearer <token>
```

**Response (200 OK, CSV):**

```csv
field,type,value_1,value_2,change_percent,impact
parameters.dff_sl_multiplier,modified,2.0,2.5,25.0,neutral
summary.sharpe_ratio,metric,1.24,1.31,5.6,positive
summary.max_drawdown,metric,0.156,0.142,-9.0,positive
```

---

### Epic 5: E-AUDIT-TRAIL

#### GET /audits/{strategy_id}/trail

**Retrieve complete audit trail for strategy**

```http
GET /api/v1/audits/strat_abc123def456/trail
Authorization: Bearer <token>
```

**Response (200 OK):**

```json
{
  "strategy_id": "strat_abc123def456",
  "audit_events": [
    {
      "event_id": "evt_001",
      "timestamp": "2026-02-26T14:30:00Z",
      "actor": "user:owner-operator",
      "action": "created",
      "old_value": null,
      "new_value": { "name": "RSI+MA Cross Strategy v1" },
      "details": "Initial creation"
    },
    {
      "event_id": "evt_002",
      "timestamp": "2026-02-26T14:35:00Z",
      "actor": "user:owner-operator",
      "action": "modified",
      "field": "parameters.dff_sl_multiplier",
      "old_value": 2.0,
      "new_value": 2.5,
      "details": null
    },
    {
      "event_id": "evt_003",
      "timestamp": "2026-02-26T14:40:00Z",
      "actor": "user:owner-operator",
      "action": "submitted",
      "old_value": null,
      "new_value": { "state": "PENDING" },
      "details": "Ready for review"
    },
    {
      "event_id": "evt_004",
      "timestamp": "2026-02-26T15:00:00Z",
      "actor": "user:approver",
      "action": "approved",
      "old_value": { "state": "PENDING" },
      "new_value": { "state": "APPROVED" },
      "details": "Approved by reviewer"
    }
  ],
  "total_events": 4,
  "immutability_verified": true
}
```

---

#### POST /audits/{run_id}/verify

**Verify run reproducibility using audit trail**

```http
POST /api/v1/audits/run_xyz789abc123/verify
Authorization: Bearer <token>
Content-Type: application/json

{
  "strict_mode": false
}
```

**Response (200 OK):**

```json
{
  "run_id": "run_xyz789abc123",
  "verification": {
    "code_version": {
      "verified": true,
      "current_version": "1.0.0",
      "run_version": "1.0.0"
    },
    "parameters": {
      "verified": true,
      "parameter_count": 12,
      "all_matched": true
    },
    "data_inputs": {
      "verified": true,
      "data_hash": "sha256:abcd...",
      "hash_matched": true
    },
    "environment": {
      "verified": true,
      "python": "3.12.0",
      "vectorbt": "0.26.2"
    }
  },
  "confidence_score": 98,        // 0-100
  "can_reproduce": true,
  "reasons_for_divergence": []
}
```

---

#### POST /audits/{run_id}/reproduce

**Trigger re-execution of historical run**

```http
POST /api/v1/audits/run_xyz789abc123/reproduce
Authorization: Bearer <token>
Content-Type: application/json

{
  "create_comparison": true,
  "mode": "backtest"
}
```

**Response (202 Accepted):**

```json
{
  "new_run_id": "run_new789xyz123",
  "original_run_id": "run_xyz789abc123",
  "reference_run": "run_xyz789abc123",
  "status": "queued",
  "estimated_completion": "2026-02-26T16:30:00Z",
  "comparison_will_be_created": true
}
```

---

#### GET /audits/{run_id}/diagnostic

**Run diagnostic tool to identify reproducibility issues**

```http
GET /api/v1/audits/run_xyz789abc123/diagnostic
Authorization: Bearer <token>
```

**Response (200 OK):**

```json
{
  "run_id": "run_xyz789abc123",
  "diagnostic_results": {
    "code_divergence": {
      "detected": false,
      "details": null
    },
    "data_divergence": {
      "detected": true,
      "details": "Data source updated after original run",
      "impact": "minor",
      "expected_variance": "±0.5%"
    },
    "environment_divergence": {
      "detected": false,
      "details": null
    },
    "parameter_divergence": {
      "detected": false,
      "details": null
    }
  },
  "recommendations": [
    "Use frozen dataset version from run metadata to ensure exact reproducibility",
    "Re-run with latest data for current performance comparison"
  ]
}
```

---

## Field Validation Rules

### Strategy Parameters Validation

| Field | Type | Required | Range/Format | Validation Rule | Error Code |
|-------|------|----------|---|---|---|
| `strategy_profile` | enum | Yes | `stable` \| `return` \| `rocket` | Must be one of 3 profiles | INVALID_PROFILE |
| `dff_sl_source_type` | enum | No | `atr` \| `stddev` \| `bb_half` \| `range` \| `fixed_pct` \| `corwin_schultz` | If set, required params must be present | DFF_INCOMPLETE |
| `dff_sl_period` | int | Conditional | 1-100 | Required if `dff_sl_source_type` ∈ {`atr`, `stddev`, `bb_half`} | MISSING_DFF_PARAM |
| `dff_sl_lookback` | int | Conditional | 1-500 | Required if `dff_sl_source_type` ∈ {`range`, `corwin_schultz`} | MISSING_DFF_PARAM |
| `dff_sl_pct` | float | Conditional | 0-1 | Required if `dff_sl_source_type = fixed_pct` | MISSING_DFF_PARAM |
| `dff_sl_stdev` | float | Conditional | 0.1-5.0 | Required if `dff_sl_source_type = bb_half` | MISSING_DFF_PARAM |
| `sl_multiplier` | float | Yes | stable/return: 0.5-5.0, rocket: 0.5-10.0 | Profile-aware range | MULTIPLIER_OUT_OF_RANGE |
| `tp_multiplier` | float | Yes | stable/return: 0.5-5.0, rocket: 0.5-10.0 | Profile-aware range | MULTIPLIER_OUT_OF_RANGE |
| `be_multiplier` | float | No | 0.5-5.0 | All profiles | MULTIPLIER_OUT_OF_RANGE |
| `trail_multiplier` | float | No | 0.5-5.0 | All profiles | MULTIPLIER_OUT_OF_RANGE |
| `max_leverage` | float | Yes | 1.0-5.0 | Global cap, non-optimizable | LEVERAGE_EXCEEDS_LIMIT |
| `position_sizing` | enum | Yes | `kelly` \| `fixed` \| `atr_based` | Strategy approach | INVALID_SIZING_TYPE |
| `max_loss_per_trade` | float | Yes | 0-5.0 | Percent of account | LOSS_LIMIT_EXCEEDED |

### DFF Validation Examples

**Valid Configuration (ATR-based SL):**
```json
{
  "dff_sl_source_type": "atr",
  "dff_sl_period": 14,
  "sl_multiplier": 2.0
}
```
✅ Valid: `dff_sl_period` present (required for ATR)

**Invalid Configuration (Missing Required Param):**
```json
{
  "dff_sl_source_type": "atr",
  "sl_multiplier": 2.0
}
```
❌ Error: `dff_sl_period` missing (required for `dff_sl_source_type=atr`)

**Invalid Configuration (Rocket Profile - TP Exceeds Limit):**
```json
{
  "strategy_profile": "rocket",
  "tp_multiplier": 12.0
}
```
❌ Error: `tp_multiplier` must be ≤ 10.0 for rocket profile

---

## Integration Patterns

### Sync vs Async Operations

**Synchronous (blocking):**
- All GET endpoints (retrieve data)
- Simple POST endpoints (create, submit, approve) — typically <1 second
- Returns immediately with result

**Asynchronous (long-running):**
- Execute strategy: Use polling or webhooks
- Verify reproducibility: May take minutes
- Reproduce run: Background job

**Async Pattern - Polling:**

```javascript
// 1. Start async operation
const response = await fetch('/api/v1/strategies/strat_123/execute', {
  method: 'POST',
  body: JSON.stringify({ mode: 'backtest' })
});
const { run_id } = await response.json();

// 2. Poll for completion
let status = 'running';
while (status === 'running') {
  const status_resp = await fetch(`/api/v1/runs/${run_id}`);
  const { status: current_status, progress_percent } = await status_resp.json();
  status = current_status;
  console.log(`Progress: ${progress_percent}%`);
  await new Promise(r => setTimeout(r, 5000)); // Poll every 5s
}
```

### Error Recovery Patterns

**Retry Logic:**

```typescript
async function executeWithRetry(
  endpoint: string,
  options: RequestInit,
  maxRetries: number = 3
) {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const response = await fetch(endpoint, options);
      if (response.ok) return response;

      if (response.status === 409 || response.status === 503) {
        // Retryable error
        const backoff = Math.pow(2, attempt - 1) * 1000;
        await new Promise(r => setTimeout(r, backoff));
        continue;
      }

      throw new Error(`${response.status}: ${response.statusText}`);
    } catch (error) {
      if (attempt === maxRetries) throw error;
    }
  }
}
```

### Database Transaction Isolation

All write operations use READ_COMMITTED isolation minimum:
- Prevents dirty reads
- Allows non-repeatable reads (acceptable for most use cases)
- Enables concurrent strategy submissions

For critical paths (approval workflow), SERIALIZABLE isolation used.

---

## OpenAPI 3.1 Specification

### Complete OpenAPI Definition

```yaml
openapi: 3.1.0
info:
  title: Katana VectorBT API
  description: Strategy lifecycle, journal, telemetry, comparison, and audit APIs
  version: 1.0.0
  contact:
    name: API Support
  license:
    name: MIT

servers:
  - url: http://localhost:5000/api/v1
    description: Local development

components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

  schemas:
    Strategy:
      type: object
      required: [strategy_id, name, state, version]
      properties:
        strategy_id:
          type: string
          pattern: '^strat_[a-z0-9]{20}$'
        name:
          type: string
          minLength: 1
          maxLength: 255
        description:
          type: string
          maxLength: 2000
        state:
          type: string
          enum: [DRAFT, PENDING, APPROVED, ACTIVE, COMPLETED, CANCELLED, KILLED]
        version:
          type: integer
          minimum: 1
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        approval_status:
          type: object
          properties:
            status:
              type: string
              enum: [pending, approved, rejected]
            resubmission_count:
              type: integer
              minimum: 0

    StrategyParameters:
      type: object
      required: [strategy_profile, sl_multiplier, tp_multiplier, max_leverage]
      properties:
        strategy_profile:
          type: string
          enum: [stable, return, rocket]
        dff_sl_source_type:
          type: string
          enum: [atr, stddev, bb_half, range, fixed_pct, corwin_schultz]
        dff_sl_period:
          type: integer
          minimum: 1
          maximum: 100
        sl_multiplier:
          type: number
          minimum: 0.5
          maximum: 10.0
        max_leverage:
          type: number
          minimum: 1.0
          maximum: 5.0

    Error:
      type: object
      required: [code, message, status]
      properties:
        code:
          type: string
        message:
          type: string
        status:
          type: integer
        timestamp:
          type: string
          format: date-time
        details:
          type: array
          items:
            type: object
            properties:
              field:
                type: string
              constraint:
                type: string
              expected:
                type: string
              received:
                oneOf:
                  - type: string
                  - type: number
                  - type: boolean

security:
  - BearerAuth: []

paths:
  /strategies:
    post:
      summary: Create a new strategy
      operationId: createStrategy
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [name, parameters]
              properties:
                name:
                  type: string
                description:
                  type: string
                parameters:
                  $ref: '#/components/schemas/StrategyParameters'
      responses:
        '201':
          description: Strategy created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Strategy'
        '400':
          description: Validation error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /strategies/{strategy_id}:
    get:
      summary: Retrieve strategy details
      operationId: getStrategy
      parameters:
        - name: strategy_id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Strategy found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Strategy'
        '404':
          description: Strategy not found

  /strategies/{strategy_id}/submit:
    post:
      summary: Submit strategy for approval
      operationId: submitStrategy
      parameters:
        - name: strategy_id
          in: path
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                notes:
                  type: string
      responses:
        '200':
          description: Strategy submitted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Strategy'

  /runs/{run_id}/journal/manifest:
    get:
      summary: Retrieve run manifest
      operationId: getManifest
      parameters:
        - name: run_id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Manifest found

  /metrics/time-to-status:
    get:
      summary: Retrieve Time-to-Status metrics
      operationId: getTimeToStatusMetrics
      parameters:
        - name: period
          in: query
          schema:
            type: string
            enum: [1d, 7d, 30d]
      responses:
        '200':
          description: Metrics retrieved

  /compare/runs:
    post:
      summary: Compare two runs
      operationId: compareRuns
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [run_id_1, run_id_2]
              properties:
                run_id_1:
                  type: string
                run_id_2:
                  type: string
      responses:
        '200':
          description: Comparison completed

  /audits/{strategy_id}/trail:
    get:
      summary: Retrieve audit trail
      operationId: getAuditTrail
      parameters:
        - name: strategy_id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Audit trail retrieved
```

---

## Summary

This API documentation provides:

✅ **Comprehensive endpoint coverage** for all 5 epics
✅ **Field validation rules** with examples
✅ **Error handling** with standardized response format
✅ **WCAG AA accessibility** in all response metadata
✅ **OpenAPI 3.1 specification** for code generation
✅ **Database isolation** constraints documented
✅ **Authentication & authorization** rules explicit
✅ **Integration patterns** for sync/async operations
✅ **Real-world examples** for all major endpoints

**Status:** Ready for implementation with Phase 1 MVP
**Next Step:** Generate Pydantic models and REST framework boilerplate from OpenAPI spec
