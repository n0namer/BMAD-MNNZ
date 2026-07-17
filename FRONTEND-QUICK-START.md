# Frontend Developer - Quick Start Guide

**Status**: 🟠 INITIALIZED & WAITING FOR BACKEND #2 SIGNAL

---

## What Happened

Frontend Developer has been **fully initialized** for the E11 Dashboard epic (9 stories).

✅ **All systems ready**. Waiting only for Backend #2 to complete `US-F1a-007: Run Journal Infrastructure`.

---

## Key Files to Know

| File | Purpose |
|------|---------|
| `.claude/frontend-dashboard-init.md` | Initialization record |
| `.claude/frontend-status.md` | Daily status & monitoring |
| `.claude/coordination-frontend-backend.md` | Detailed sync protocol |
| `src/dashboard/README.md` | Dashboard overview |
| `src/frontend/README.md` | UI components guide |
| `src/dashboard/STORY_TEMPLATE.md` | Story implementation template |

---

## The Plan

### Phase 0: Waiting (Now)
- Monitor: `swarm:backend-dev:status` in memory
- When Backend #2 completes US-F1a-007 → Signal sent
- **Trigger**: `swarm:backend-dev:status` = `"COMPLETED"`

### Phase 1: Implementation Begins (Post-Signal)
**Week 1** (US-DASH-001, 002, 003)
- Dashboard Generation (Plotly/D3 charts)
- Mode Toggle (Backtest/Paper/Live switching)
- Run List & Filtering

**Week 2** (US-DASH-004, 005)
- Equity Curve visualization
- Trade-by-Trade analysis

**Week 3** (US-DASH-006, 007)
- Signal Diagnostics panel
- Gates & Quality checklist

**Week 4** (US-DASH-008, 009)
- Export to JSON/CSV/HTML
- Responsive design & accessibility

---

## Directory Structure

```
BMAD-MNNZ/
├── src/
│   ├── dashboard/               ← Main dashboard app (E11)
│   │   ├── components/          ← React components
│   │   ├── views/               ← Page views
│   │   ├── types/               ← TypeScript definitions
│   │   ├── utils/               ← Helper functions
│   │   └── README.md            ← Dashboard guide
│   │
│   └── frontend/                ← Shared UI components
│       ├── components/          ← Reusable components
│       ├── hooks/               ← Custom hooks
│       ├── styles/              ← CSS/SCSS
│       ├── types/               ← Shared types
│       └── README.md            ← UI guide
│
├── static/                      ← Assets (HTML, CSS, images)
├── tests/
│   └── e2e/                     ← End-to-end tests
│
└── .claude/
    ├── frontend-dashboard-init.md
    ├── frontend-status.md
    └── coordination-frontend-backend.md
```

---

## How to Start (When Signal Received)

### Step 1: Verify Signal
```bash
# Check for signal in memory
npx claude-flow@v3alpha memory search -q "US-F1a-007 COMPLETED"
```

### Step 2: Get API Contract
```bash
# Retrieve from Backend #2
npx claude-flow@v3alpha memory search -q "api-contract:e9-e10"
```

### Step 3: Initialize First Story
```bash
# Run the BMAD dev-story workflow
/bmad-bmm-dev-story

# When prompted, enter: US-DASH-001
# Or copy the story template and start from STORY_TEMPLATE.md
```

### Step 4: Begin Implementation
1. Follow the template for story structure
2. Create components in src/dashboard/
3. Write E2E tests in tests/e2e/
4. Commit and update memory hourly

### Step 5: Track Progress
```bash
# Update progress every hour
npx claude-flow@v3alpha memory store \
  --namespace "swarm" \
  --key "frontend-dev:progress" \
  --content "{...progress data...}"
```

---

## Memory Keys to Monitor & Update

### Monitor These (Pre-Signal)
```
swarm:backend-dev:status
  → Waiting for: "US-F1a-007": "COMPLETED"
  → Check daily
```

### Update These (Post-Signal)
```
swarm:frontend-dev:progress
  → Update hourly
  → Include: current story, %, blockers, API sync status

swarm:frontend-dev:component-contract
  → Define component interfaces
  → Share with Backend #2 for validation
```

### Receive These
```
swarm:backend-dev:api-contract:e9-e10
  → Endpoints, types, auth
  → Needed to start implementation
```

---

## The 9 Stories (In Order)

1. **US-DASH-001**: Dashboard Generation
   - Plotly & D3 visualizations
   - Real-time data rendering
   - Estimated: 2 days

2. **US-DASH-002**: Mode Toggle
   - Backtest/Paper/Live switching
   - Data filtering by mode
   - Estimated: 1 day

3. **US-DASH-003**: Run List & Filtering
   - Display list of runs
   - Search and filter
   - Estimated: 2 days

4. **US-DASH-004**: Equity Curve & Drawdown
   - Performance visualization
   - Drawdown analysis
   - Estimated: 2 days

5. **US-DASH-005**: Trade-by-Trade Analysis
   - Individual trade display
   - Trade metrics
   - Estimated: 2 days

6. **US-DASH-006**: Signal Diagnostics Panel
   - Signal history and analysis
   - Confidence scores
   - Estimated: 2 days

7. **US-DASH-007**: Gates & Quality Checklist
   - Quality validation
   - Gate checks
   - Estimated: 1 day

8. **US-DASH-008**: Export Artifacts
   - JSON/CSV/HTML export
   - Report generation
   - Estimated: 2 days

9. **US-DASH-009**: Responsive Design & Accessibility
   - Mobile optimization
   - WCAG 2.1 AA compliance
   - Estimated: 2 days

---

## Dependencies & API

### From Backend #2 (E9 Phase 1a + E10)
- `GET /api/runs` - List all runs
- `GET /api/runs/{id}` - Get run details
- `GET /api/runs/{id}/trades` - Get trades
- `GET /api/runs/{id}/signals` - Get signals
- `GET /api/runs/{id}/metrics` - Get metrics

### From Shared UI (src/frontend/)
- `DataTable` - Sortable table
- `Card` - Card component
- `Button` - Button
- `Chart` - Generic chart wrapper
- `Spinner` - Loading indicator
- `Alert` - Notifications

---

## Testing & Quality

### E2E Tests
- Location: `tests/e2e/`
- Framework: Playwright or Cypress (TBD)
- Coverage: Every story has E2E tests
- Run: `npm run test:e2e`

### Unit Tests
- Location: Component __tests__ folders
- Framework: Jest + Testing Library
- Coverage: >80% target
- Run: `npm run test`

### Checklist Before Commit
```
✓ Code implements acceptance criteria
✓ E2E tests passing
✓ No console errors
✓ Responsive on mobile/tablet/desktop
✓ Accessibility check (axe or similar)
✓ Memory updated with progress
✓ Coordination sync verified
```

---

## Tools & Commands

### Development
```bash
npm install                 # Install dependencies
npm run dev                 # Start dev server
npm run build              # Build for production
npm run test               # Run unit tests
npm run test:e2e           # Run E2E tests
```

### Memory & Coordination
```bash
# Check Backend #2 signal
npx claude-flow@v3alpha memory search -q "US-F1a-007"

# Update frontend progress
npx claude-flow@v3alpha memory store \
  --namespace "swarm" \
  --key "frontend-dev:progress" \
  --content "..."

# View frontend status
cat .claude/frontend-status.md
```

### Git
```bash
git add src/dashboard/      # Stage dashboard changes
git commit -m "feat: US-DASH-001 complete"
git push origin main
```

---

## Coordination Protocol

### Hourly Updates (Post-Signal)
Every 60 minutes, update memory:
```json
{
  "timestamp": "2026-03-01T10:00:00Z",
  "current_story": "US-DASH-001",
  "completion_percent": 45,
  "recent_changes": ["Added EquityCurve component"],
  "api_contract_status": "synchronized",
  "blockers": [],
  "next_review": "2026-03-01T11:00:00Z"
}
```

### Signal Reception (Critical)
When Backend #2 completes US-F1a-007:
1. You'll be notified automatically
2. Retrieve API contract from memory
3. Start US-DASH-001 immediately
4. Begin hourly tracking

### If Issues Arise
```
API Contract Mismatch → Log to memory, Backend responds
Feature Blocked → Check Backend #2 status, escalate if needed
Performance Issues → Update status, request architectural review
```

---

## Success Indicators

✅ **Week 1**: US-DASH-001, 002, 003 complete
✅ **Week 2**: US-DASH-004, 005 complete
✅ **Week 3**: US-DASH-006, 007 complete
✅ **Week 4**: US-DASH-008, 009 complete + E2E tests passing

**Final Goal**:
- All 9 stories implemented
- 100% responsive design
- WCAG 2.1 AA accessibility
- Production-ready code
- Deployed to live environment

---

## Quick Reference

| Item | Location | Purpose |
|------|----------|---------|
| Roadmap | src/dashboard/README.md | 9 stories overview |
| Template | src/dashboard/STORY_TEMPLATE.md | Implementation guide |
| Status | .claude/frontend-status.md | Daily tracking |
| Protocol | .claude/coordination-frontend-backend.md | Sync details |
| UI Components | src/frontend/README.md | Shared components |

---

## FAQ

**Q: When do I start?**
A: When Backend #2 signals `US-F1a-007` completion. Until then, monitor memory key `swarm:backend-dev:status`.

**Q: What if Backend #2 is delayed?**
A: Start building UI components in parallel. They don't depend on API contracts.

**Q: How do I know the API contract?**
A: Backend #2 provides it in memory key `swarm:backend-dev:api-contract:e9-e10` when signaling completion.

**Q: What if API changes mid-implementation?**
A: Log issue to memory, sync with Backend #2 hourly. Version the contract.

**Q: Where do I put test files?**
A: End-to-end: `tests/e2e/`. Unit tests: next to component in `__tests__/` folder.

---

## Contacts & Escalation

### Daily Operations
- Use memory for all coordination
- Update progress hourly
- Check Backend #2 status daily

### Escalations
- **API Contract Mismatch**: Log to memory, Backend #2 responds
- **Feature Blocked**: Check Backend #2 status, escalate if >4 hours
- **Performance Issues**: Request architectural review
- **Timeline Slip**: Notify coordination team

---

## Next Steps

### Right Now
1. ✅ Review this document
2. ✅ Check `.claude/frontend-status.md`
3. ✅ Understand coordination protocol
4. ⏳ **Monitor `swarm:backend-dev:status` daily**

### When Signal Received
1. ✅ Get API contract from memory
2. ✅ Run `/bmad-bmm-dev-story` for US-DASH-001
3. ✅ Begin hourly progress updates
4. ✅ Implement first 3 stories in Week 1

---

**Created**: 2026-02-28
**Status**: 🟠 READY & WAITING
**Next Action**: Wait for Backend #2 signal on US-F1a-007
**Contact**: Frontend Developer Agent
