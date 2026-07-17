# Frontend & Backend Coordination (E11 Dashboard + E9/E10)

**Setup Date**: 2026-02-28
**Frontend Agent**: Dashboard & UI Developer
**Backend Agent**: API & Infrastructure Developer

---

## Signal Synchronization Protocol

### 🟠 Current State: INITIALIZATION

**Frontend Status**:
- ✅ Directory structure created
- ✅ Story roadmap defined (US-DASH-001 through US-DASH-009)
- ⏳ **WAITING** for Backend #2 signal

**Backend #2 Status**:
- 🟠 **US-F1a-007: Run Journal Infrastructure** (PENDING)
- This is the **blocking dependency** for Frontend

---

## Blocking Signal

**Memory Key**: `swarm:backend-dev:status`

Frontend will monitor this key for completion of:
```json
{
  "epic": "E9 Phase 1a Core",
  "story": "US-F1a-007",
  "title": "Run Journal Infrastructure",
  "status": "PENDING|IN_PROGRESS|COMPLETED",
  "api_contract_url": "memory:key:...",
  "completion_date": "YYYY-MM-DD"
}
```

**When status = "COMPLETED"**:
1. Frontend begins US-DASH-001 implementation
2. Frontend retrieves API contract
3. Synchronization becomes hourly

---

## API Contract Exchange

### Backend Provides (via Memory)
**Key**: `swarm:backend-dev:api-contract:e9-e10`

Frontend expects:
```typescript
{
  // Run Journal endpoints
  "endpoints": {
    "listRuns": {
      "method": "GET",
      "path": "/api/runs",
      "query": { "filter": "string", "limit": "number", "offset": "number" },
      "response": { "type": "Run[]" }
    },
    "getRun": {
      "method": "GET",
      "path": "/api/runs/{id}",
      "response": { "type": "Run" }
    },
    "getTrades": {
      "method": "GET",
      "path": "/api/runs/{id}/trades",
      "query": { "filter": "string" },
      "response": { "type": "Trade[]" }
    },
    "getSignals": {
      "method": "GET",
      "path": "/api/runs/{id}/signals",
      "response": { "type": "Signal[]" }
    },
    "getMetrics": {
      "method": "GET",
      "path": "/api/runs/{id}/metrics",
      "response": { "type": "Metrics" }
    }
  },

  // Data structures
  "types": {
    "Run": {
      "id": "string",
      "name": "string",
      "mode": "backtest|paper|live",
      "startDate": "ISO8601",
      "endDate": "ISO8601",
      "initialCapital": "number",
      "totalReturn": "number",
      "sharpeRatio": "number",
      "maxDrawdown": "number",
      "winRate": "number",
      "status": "running|completed|failed"
    },
    "Trade": {
      "id": "string",
      "runId": "string",
      "timestamp": "ISO8601",
      "symbol": "string",
      "entryPrice": "number",
      "exitPrice": "number",
      "quantity": "number",
      "pnl": "number",
      "pnlPercent": "number",
      "duration": "string",
      "reason": "string"
    },
    "Signal": {
      "id": "string",
      "runId": "string",
      "timestamp": "ISO8601",
      "symbol": "string",
      "signal": "buy|sell|hold",
      "confidence": "number",
      "reason": "string"
    },
    "Metrics": {
      "totalReturn": "number",
      "annualizedReturn": "number",
      "sharpeRatio": "number",
      "sortino Ratio": "number",
      "maxDrawdown": "number",
      "winRate": "number",
      "profitFactor": "number",
      "avgWin": "number",
      "avgLoss": "number"
    }
  },

  // Authentication
  "auth": {
    "type": "bearer|apikey",
    "location": "header|query",
    "key_name": "Authorization|X-API-Key"
  }
}
```

### Frontend Provides (via Memory)
**Key**: `swarm:frontend-dev:component-contract`

Backend uses this for:
- UI component props
- Expected data format validation
- Response structure confirmation

```typescript
{
  "components": {
    "DashboardView": {
      "props": {
        "runId": "string (required)",
        "mode": "backtest|paper|live",
        "onModeChange": "function"
      }
    },
    "TradeTable": {
      "props": {
        "trades": "Trade[]",
        "onRowClick": "function"
      }
    },
    "EquityCurve": {
      "props": {
        "data": "number[]",
        "timestamps": "ISO8601[]"
      }
    }
  }
}
```

---

## Hourly Sync Protocol (After Blocking Signal)

**Frontend Updates** (every 60 minutes):

Key: `swarm:frontend-dev:progress`

```json
{
  "timestamp": "2026-02-28T14:00:00Z",
  "current_story": "US-DASH-001 or null if waiting",
  "story_title": "Dashboard Generation",
  "completion_percent": 0,
  "recent_commits": [],
  "api_contract_status": "synchronized|pending|mismatch",
  "blockers": [],
  "dependencies_ready": true|false,
  "next_story": "US-DASH-002"
}
```

**Backend Updates** (every 60 minutes):

Key: `swarm:backend-dev:progress`

```json
{
  "timestamp": "2026-02-28T14:00:00Z",
  "current_story": "US-F1a-007 or next",
  "story_title": "Run Journal Infrastructure",
  "completion_percent": 0,
  "api_endpoints_ready": ["listRuns", "getRun"],
  "blockers": [],
  "frontend_blocked": true|false,
  "next_story": "US-F2-001 or next backend feature"
}
```

---

## Integration Checkpoints

### Checkpoint 1: US-DASH-001 + API Ready
- Dashboard Generation implementation
- Basic data fetching from E9/E10
- Plotly charts rendering

### Checkpoint 2: US-DASH-002 + Mode Toggle
- Run mode switching (Backtest/Paper/Live)
- Data filtering by mode

### Checkpoint 3: US-DASH-003-005
- Run list display
- Trade analysis
- Equity curve visualization

### Checkpoint 4: US-DASH-006-007
- Signal diagnostics
- Quality gates validation

### Checkpoint 5: US-DASH-008-009
- Export functionality
- Responsive design

---

## Communication Channels

### Primary (Memory-Based)
- `swarm:frontend-dev:progress` - Frontend status
- `swarm:backend-dev:status` - Backend blocking signal
- `swarm:backend-dev:progress` - Backend hourly updates
- `swarm:backend-dev:api-contract:e9-e10` - API specification
- `swarm:frontend-dev:component-contract` - Component contracts

### Secondary (Code-Based)
- API integration tests (tests/e2e/)
- Shared type definitions (shared-types.ts)
- Integration documentation (this file)

---

## Escalation Protocol

If mismatch detected in API contract:
1. Frontend logs issue in memory: `issues:frontend-api-mismatch`
2. Backend acknowledges and provides explanation
3. Contract updated and both agents sync
4. Resume work

If Frontend blocked >2 hours:
1. Frontend escalates to coordination agent
2. Review current Backend #2 status
3. If not progressing, re-prioritize tasks

---

## Success Criteria

✅ **Blocking Signal Received**
- Backend #2 completes US-F1a-007
- API contract provided in memory

✅ **US-DASH-001 Complete**
- Dashboard renders with live data
- Data fetching working correctly
- E2E tests passing

✅ **Full E11 Dashboard Complete**
- All 9 stories implemented
- 100% responsive design
- Accessibility compliance (WCAG 2.1 AA)
- Export functionality working

---

## Timeline Estimate

**Post-Signal Timeline**:
- Week 1: US-DASH-001 & 002 (Dashboard Gen + Mode Toggle)
- Week 2: US-DASH-003 to 005 (Run List + Analysis)
- Week 3: US-DASH-006 to 007 (Diagnostics + Gates)
- Week 4: US-DASH-008 to 009 (Export + Responsive)

---

## Notes

- This is a **blocking dependency** - Frontend cannot proceed until Backend #2 signals completion
- All coordination happens via shared memory (no external communication needed)
- Regular hourly syncs ensure alignment
- API contract is source of truth for integration

---

**Established**: 2026-02-28
**Status**: ⏳ WAITING FOR US-F1a-007 SIGNAL
**Next Review**: When Backend #2 signals completion
