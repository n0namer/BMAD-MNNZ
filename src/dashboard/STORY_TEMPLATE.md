# Dashboard Story Template

Use this template for each US-DASH-00X story implementation.

---

## Story Information

**Story ID**: US-DASH-001
**Title**: Dashboard Generation (Plotly/D3 Visualization)
**Status**: ⏳ PENDING (Blocked by Backend #2)
**Estimated Points**: 13

---

## Description

Create the main dashboard view with real-time data visualization using Plotly for basic charts and D3 for advanced visualizations.

---

## Acceptance Criteria

- [ ] Dashboard renders performance metrics from Run Journal
- [ ] Charts update when run data changes
- [ ] Plotly charts for basic visualizations
- [ ] D3 for advanced custom visualizations (optional)
- [ ] Error handling for missing data
- [ ] Loading states display correctly
- [ ] E2E tests passing

---

## Technical Specifications

### Components to Create
- `DashboardView.tsx` - Main dashboard layout
- `ChartWrapper.tsx` - Plotly chart container
- `MetricsPanel.tsx` - KPI display
- `ChartD3.tsx` - D3 chart wrapper (advanced)

### Data Requirements
- Run object from E10 Run Journal
- Metrics structure from API contract
- Trade history for equity curve

### API Endpoints Used
- `GET /api/runs/{id}` - Fetch run data
- `GET /api/runs/{id}/metrics` - Fetch metrics
- `GET /api/runs/{id}/trades` - Fetch trades for analysis

---

## Implementation Steps

### Step 1: Create Dashboard View Structure
```bash
mkdir -p src/dashboard/views
mkdir -p src/dashboard/components/charts
mkdir -p src/dashboard/components/panels
```

### Step 2: Define Types
Create `src/dashboard/types/dashboard.ts`:
```typescript
export interface DashboardProps {
  runId: string;
  mode: 'backtest' | 'paper' | 'live';
}

export interface ChartData {
  labels: string[];
  datasets: Dataset[];
}
```

### Step 3: Build Components
1. `MetricsPanel` - Display KPIs
2. `EquityCurve` - Equity curve chart
3. `Drawdown` - Drawdown visualization
4. `TradeTable` - Trade listing

### Step 4: Add Data Fetching
Use hooks from `src/frontend`:
```typescript
import { useApi } from '../frontend';

const { data: run } = useApi(`/api/runs/${runId}`);
const { data: metrics } = useApi(`/api/runs/${runId}/metrics`);
```

### Step 5: Testing
Create `tests/e2e/dashboard.test.ts`:
```typescript
describe('Dashboard', () => {
  it('should load and display metrics', () => {
    // E2E test
  });
});
```

---

## Files to Create/Modify

### New Files
- [ ] `src/dashboard/views/DashboardView.tsx`
- [ ] `src/dashboard/components/charts/EquityCurve.tsx`
- [ ] `src/dashboard/components/panels/MetricsPanel.tsx`
- [ ] `src/dashboard/types/dashboard.ts`
- [ ] `tests/e2e/dashboard.spec.ts`

### Files to Modify
- [ ] `src/dashboard/index.ts` - Export main component

---

## Dependencies

### Frontend Components
- `DataTable` from `src/frontend`
- `Card` from `src/frontend`
- `Spinner` from `src/frontend`

### Libraries
- Plotly.js: `npm install plotly.js`
- D3.js: `npm install d3` (optional)
- TypeScript types: `npm install @types/plotly.js`

---

## API Contract Reference

From `swarm:backend-dev:api-contract:e9-e10`:

```json
{
  "getRun": {
    "method": "GET",
    "path": "/api/runs/{id}",
    "response": {
      "id": "string",
      "name": "string",
      "mode": "backtest|paper|live",
      "totalReturn": "number",
      "sharpeRatio": "number",
      "maxDrawdown": "number"
    }
  },
  "getMetrics": {
    "method": "GET",
    "path": "/api/runs/{id}/metrics",
    "response": {
      "totalReturn": "number",
      "sharpeRatio": "number",
      "maxDrawdown": "number",
      "winRate": "number"
    }
  }
}
```

---

## Testing Checklist

- [ ] Component renders without errors
- [ ] Data fetches from API correctly
- [ ] Charts display with sample data
- [ ] Error state handled (missing data)
- [ ] Loading state shows spinner
- [ ] Responsive on mobile/tablet/desktop
- [ ] E2E tests passing
- [ ] No console errors or warnings

---

## Definition of Done

- [ ] Code implementation complete
- [ ] All acceptance criteria met
- [ ] E2E tests passing
- [ ] Code reviewed (peer review)
- [ ] Documentation updated
- [ ] Merged to main branch
- [ ] Memory updated: `swarm:frontend-dev:progress`

---

## Memory Updates

After implementation:

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "bmad:dashboard:us-dash-001" \
  --content "[Story completion summary]"
```

Update progress:
```bash
npx claude-flow@v3alpha memory store \
  --namespace "swarm" \
  --key "frontend-dev:progress" \
  --content "{timestamp, story_completed, percent, next_story}"
```

---

## Notes

- Start with this story after Backend #2 signals US-F1a-007 completion
- Use `/bmad-bmm-dev-story` workflow for implementation
- Follow responsive design guidelines
- Coordinate with Backend #2 on API changes

---

## Dependencies on Other Stories

This story **blocks**:
- US-DASH-002 (Mode Toggle)
- US-DASH-003 (Run List)

---

## Related Stories

- **E10**: Run Journal Infrastructure (provides data)
- **E9 Phase 1a**: Core API (provides endpoints)

---

## Success Example

When complete:
- Dashboard displays a run's performance metrics
- Charts render correctly with real data
- User can view equity curve and drawdown
- All tests passing
- Production-ready code

---

**Template Created**: 2026-02-28
**Used For**: Each US-DASH-00X story
**Launch Command**: `/bmad-bmm-dev-story` then select "US-DASH-001"
