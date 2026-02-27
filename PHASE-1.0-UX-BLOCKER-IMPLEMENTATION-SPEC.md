---
title: "Phase 1.0 UX Blocker Implementation Specification"
date: "2026-02-27T01:45:00Z"
status: "READY_FOR_IMPLEMENTATION"
priority: "CRITICAL_PATH"
blockers: ["Mandatory_Baseline_Badge", "Kill_Switch_Visualization"]
effort_hours: 12-16
timeline_days: "2-3 days (parallel track with Zone 2 code)"
phase: "Phase 1.0"
go_live_dependent: true
---

# Phase 1.0 UX Blocker Specification

**CRITICAL:** These 2 features MUST be implemented before go-live. Without them:
- ❌ Non-Katana strategies deployable (risk: invalid baseline)
- ❌ Kill-switch thresholds invisible to users (risk: margin calls without warning)
- ❌ Cannot claim "100% north star baseline coverage"

---

## 1. Mandatory Baseline Badge (6-8 hours)

### Purpose
Enforce that every strategy template MUST have KatanaTransformer baseline configured. Display this status prominently so users cannot accidentally use un-validated strategies.

### User Story
```
AS A trader
I WANT TO see a "Baseline Validated" badge on every strategy
SO THAT I know the strategy has been tested against KatanaTransformer baseline
```

### Requirements

#### R1.1: Badge Display Location
- **Where**: Top-right of Strategy Card (next to existing tags)
- **Visual**: Green checkmark + "Baseline ✓" text
- **Size**: 24px height, fits inline with other badges
- **Hover**: Tooltip "Strategy validated against KatanaTransformer baseline"

#### R1.2: Badge Visibility Rules
- ✅ Show badge when: `strategy.metadata.baseline_validator === "KatanaTransformer" && validation_timestamp != null`
- ❌ Hide/gray badge when: `strategy.metadata.baseline_validator === null || is_custom_strategy`
- ⚠️ Yellow variant when: `baseline_validation_timestamp < (now - 30_days)` (refreshed recently)

#### R1.3: Validation Data Model
```typescript
interface StrategyBaseline {
  // Added to strategy.metadata
  baseline_validator: "KatanaTransformer" | "Custom" | null;
  validation_timestamp: ISO8601 | null;
  validation_params: {
    timeframe: "1H" | "4H" | "D";
    sample_size: number; // rows tested
    pass_rate: number; // % of samples profitable
    min_dd: number; // minimum drawdown observed
  };
  validation_status: "PASS" | "NEEDS_RECHECK" | "FAILED";
}
```

#### R1.4: Loading State
- While validating: Badge shows spinner, text "Validating..."
- On validation failure: Badge shows red X, text "Validation Failed", tooltip shows error

#### R1.5: Edit Flow
- When user edits strategy parameters:
  1. Mark baseline badge as "NEEDS_RECHECK" (yellow)
  2. Show alert: "Strategy parameters changed. Re-run baseline validation."
  3. Provide "Validate Now" button → triggers background validation job
  4. Once passed, badge returns to green ✓

### Data Flow Diagram
```
User selects strategy
      ↓
Load strategy.metadata.baseline_validator
      ↓
IF "KatanaTransformer" and validation_timestamp exists
    → Render GREEN badge with ✓
ELSE IF null or custom
    → Render GRAY badge or hide
ELSE IF timestamp > 30 days old
    → Render YELLOW badge with warning icon
      ↓
User hovers badge
    → Show tooltip with validation date, sample size, pass rate
```

### Acceptance Criteria
- [ ] Badge renders in correct location (top-right of card)
- [ ] Green ✓ shows for KatanaTransformer-validated strategies
- [ ] Gray/hidden for custom or non-validated strategies
- [ ] Yellow warning for stale validations (>30 days)
- [ ] Hover tooltip displays validation metadata
- [ ] Badge updates to "NEEDS_RECHECK" when strategy params change
- [ ] "Validate Now" button triggers background job
- [ ] Performance: Badge renders in <50ms
- [ ] Mobile: Badge still visible on <480px screens (scales to 20px)

### Implementation Checklist
- [ ] Add `StrategyBaseline` interface to type definitions
- [ ] Add badge component (`StrategyBaselineBadge.tsx`)
- [ ] Add tooltip with validation details
- [ ] Integrate with strategy loading (fetch validation_timestamp)
- [ ] Add listener for strategy param changes → mark NEEDS_RECHECK
- [ ] Add "Validate Now" button + handler
- [ ] Add tests for all badge states (green, gray, yellow, spinner, error)
- [ ] Update strategy card component to render badge
- [ ] Add Cypress E2E test for badge visibility

### Effort Breakdown
| Task | Hours | Notes |
|------|-------|-------|
| Component creation (badge + tooltip) | 1 | Reuse existing badge patterns |
| Data model update | 0.5 | Add StrategyBaseline interface |
| Integration with strategy loader | 1 | Fetch validation_timestamp |
| Change detection listener | 1 | Mark NEEDS_RECHECK on edit |
| "Validate Now" button | 1 | Trigger background job |
| Testing (unit + E2E) | 2 | All badge state combinations |
| UI refinement + mobile | 1 | Ensure visibility on all screens |
| **Total** | **6.5-7 hours** | **Ready for Day 1 implementation** |

### Success Criteria
✅ Every strategy template shows Baseline Badge
✅ Users cannot mistake validated vs. unvalidated strategies
✅ Stale validations flagged with yellow warning
✅ Validation state updates when strategy params change
✅ Component renders in <50ms (no perf regression)

---

## 2. Kill-Switch Visualization (6-8 hours)

### Purpose
Display the kill-switch thresholds prominently so users understand:
- Individual strategy max drawdown limit (40% standard)
- Portfolio max drawdown limit (50% standard)
- When these will trigger (e.g., "Active — triggers at -42.3% DD")
- What happens when triggered (pause all signals, maintain positions)

### User Story
```
AS A risk manager
I WANT TO see kill-switch thresholds on the dashboard
SO THAT I understand when trading will pause due to drawdown limits
```

### Requirements

#### R2.1: Kill-Switch Status Widget
- **Location**: Dashboard top-right, next to portfolio stats
- **Size**: Compact card (280px × 140px)
- **Update Frequency**: Real-time (every tick for current DD)
- **Visual Style**: Orange/red alert style to emphasize risk management

#### R2.2: Display Information
```
┌─────────────────────────────┐
│ ⚠️  KILL-SWITCH LIMITS       │
├─────────────────────────────┤
│ Individual Strategy:         │
│ Max Drawdown: -40%          │
│ Current: -18.5%  ▓░░░░░░░░  │ (46% of limit)
│                              │
│ Portfolio:                   │
│ Max Drawdown: -50%          │
│ Current: -8.2%   ▓░░░░░░░░░ │ (16% of limit)
│                              │
│ STATUS: ✅ Active            │
│ Triggers at -40.0% (indiv)   │
│ Triggers at -50.0% (portfolio)
└─────────────────────────────┘
```

#### R2.3: Data Model
```typescript
interface KillSwitchConfig {
  individual_max_dd: number; // e.g., -0.40 for -40%
  portfolio_max_dd: number;  // e.g., -0.50 for -50%
}

interface KillSwitchStatus {
  config: KillSwitchConfig;
  current_individual_dd: number; // real-time from performance metrics
  current_portfolio_dd: number;  // real-time from portfolio aggregate
  is_active: boolean;
  triggered_at: ISO8601 | null;
  triggered_reason: "individual_max_dd" | "portfolio_max_dd" | null;
}
```

#### R2.4: Color Coding
| Threshold Breach | Color | Status |
|------------------|-------|--------|
| < 30% of limit | 🟢 Green | Safe |
| 30-60% of limit | 🟡 Yellow | Caution |
| 60-90% of limit | 🟠 Orange | Warning |
| > 90% of limit | 🔴 Red | Critical |
| Triggered | ⚫ Black | HALTED |

#### R2.5: Progress Bars
- Individual DD bar: Shows visual representation of how close to -40% limit
- Portfolio DD bar: Shows visual representation of how close to -50% limit
- Dynamic coloring based on thresholds (green → yellow → orange → red)
- Smooth animation when DD updates (0.5s ease-in-out)

#### R2.6: Real-Time Updates
- Subscribe to `portfolio:metrics` pubsub channel
- Update individual_dd every tick (100ms granularity)
- Update portfolio_dd every 5 seconds (aggregate)
- Show timestamp of last update: "Updated: 2min ago"

#### R2.7: Kill-Switch Trigger Flow
When individual DD < -40% OR portfolio DD < -50%:
1. ❌ Set `is_active = false`
2. 🔴 Change widget color to red/black
3. 📱 Show banner at top: "KILL-SWITCH TRIGGERED: All trading paused at [time]"
4. 📊 Update status text: "❌ HALTED - triggered at -42.3% DD"
5. 💾 Log event: `{timestamp, reason, individual_dd, portfolio_dd}`
6. 🔔 Show toast: "Kill-switch triggered to prevent further losses"
7. 🔐 Disable all signal execution until manual reset

#### R2.8: Manual Reset (After Trigger)
- Add "Reset Kill-Switch" button (visible only when triggered)
- Click button → confirmation modal: "Reset to active? This will resume trading."
- On confirm:
  1. Verify human authorized reset (check user role = manager)
  2. Set `is_active = true`
  3. Reset `triggered_at = null`
  4. Resume signal execution
  5. Log reset event with user ID

### Data Flow Diagram
```
Real-time portfolio metrics
        ↓
┌─────────────────────────────┐
│ Calculate current DD values  │
│ individual_dd, portfolio_dd  │
└─────────────────────────────┘
        ↓
IF individual_dd < -40% OR portfolio_dd < -50%
    → is_active = false
    → Render RED/BLACK state
    → Show "HALTED" status
    → Disable signal execution
ELSE
    → Render normal state (green/yellow/orange)
    → Calculate % of limit: (current_dd / max_dd)
    → Update progress bars
    → Continue signal execution
```

### Acceptance Criteria
- [ ] Widget renders on dashboard top-right
- [ ] Displays current individual DD with -40% threshold and progress bar
- [ ] Displays current portfolio DD with -50% threshold and progress bar
- [ ] Color coding correct: green (safe) → yellow (30-60%) → orange (60-90%) → red (>90%)
- [ ] Progress bars update in real-time (<100ms latency)
- [ ] Text displays exact values: "Current: -18.5% | Max: -40%"
- [ ] Status shows ✅ Active or ❌ Halted
- [ ] On trigger: widget turns red, status shows "HALTED", banner appears
- [ ] "Reset Kill-Switch" button appears after trigger
- [ ] Reset button requires confirmation modal
- [ ] Reset only available to user with "manager" role
- [ ] Performance: Widget updates in <50ms
- [ ] Mobile: Widget responsive (280px on desktop, 240px on tablet, 200px on mobile)
- [ ] E2E test: Simulate DD reaching -39%, -40% (trigger), reset

### Implementation Checklist
- [ ] Create `KillSwitchStatus` interface
- [ ] Create `KillSwitchWidget.tsx` component
- [ ] Add real-time subscription to `portfolio:metrics` pubsub
- [ ] Implement progress bar component with color mapping
- [ ] Add tooltip showing exact trigger thresholds
- [ ] Implement trigger detection logic
- [ ] Add "KILL-SWITCH TRIGGERED" banner component
- [ ] Add "Reset Kill-Switch" button with confirmation modal
- [ ] Add permission check for reset (role = manager)
- [ ] Add tests for all DD threshold states
- [ ] Add E2E test for trigger + reset flow
- [ ] Add performance monitoring (render time, subscription latency)

### Effort Breakdown
| Task | Hours | Notes |
|------|-------|-------|
| KillSwitchWidget component | 2 | Progress bars, color mapping |
| Real-time pubsub integration | 1.5 | Subscribe to metrics channel |
| Trigger detection logic | 1 | DD < -40% / -50% checks |
| Triggered state UI (banner, button) | 1.5 | Red state, reset button, modal |
| Reset flow + permission check | 1 | Confirmation, role check, log |
| Testing (unit + E2E) | 1.5 | All DD thresholds, trigger/reset |
| Mobile responsiveness | 0.5 | Scale for <480px screens |
| **Total** | **8.5-9 hours** | **Parallel with Baseline Badge** |

### Success Criteria
✅ Kill-switch limits always visible to users
✅ Real-time DD tracking with <100ms latency
✅ Visual progress bars show % of limit used
✅ Trigger immediately stops all trading
✅ Manual reset available with proper authorization
✅ All events logged for audit trail

---

## 3. Phase 1.0 Implementation Timeline

### Critical Path (Must Complete Before Go-Live)
```
Day 1 (2026-02-28):
  ├─ 09:00 - Baseline Badge component creation
  ├─ 11:00 - Kill-Switch Widget real-time integration
  └─ 17:00 - Initial testing + responsive design

Day 2 (2026-03-01):
  ├─ 09:00 - Complete unit tests (all badge states, DD thresholds)
  ├─ 12:00 - E2E tests (badge visibility, kill-switch trigger/reset)
  └─ 17:00 - Code review + performance profiling

Day 3 (2026-03-02):
  ├─ 09:00 - Fix review feedback + optimize rendering
  └─ 12:00 - READY FOR PRODUCTION
```

### Parallel Execution (with Zone 2 Dev)
- **Track A (UX)**: Days 1-3, 12-16 hours total, 2 engineers
- **Track B (Code/ATDD)**: Days 2-14, 154 story points, Agent-4 + Agent-5
- **Integration**: Code ready on Day 7, UX widgets ready on Day 3 → merge on Day 7

### Merge Point (Day 3 Evening → Day 7 Integration)
```
Day 7 Checkpoint:
  ├─ Track A complete: ✅ Baseline Badge + Kill-Switch Widget
  ├─ Track B progress: 50+ story points code, 50+ tests passing
  └─ Integration: Merge UX widgets into codebase, all tests passing
```

---

## 4. Integration with Zone 2 Development

### Code API Expectations
The UX widgets expect these APIs from Track B (Agent-4):

**1. Strategy Baseline Endpoint**
```typescript
GET /api/strategies/{strategy_id}/baseline
Response: {
  baseline_validator: "KatanaTransformer" | null;
  validation_timestamp: ISO8601 | null;
  validation_params: { timeframe, sample_size, pass_rate, min_dd };
  validation_status: "PASS" | "NEEDS_RECHECK" | "FAILED";
}

POST /api/strategies/{strategy_id}/validate-baseline
Response: { job_id, status: "queued" }

GET /api/jobs/{job_id}/status
Response: { status, result }
```

**2. Kill-Switch Status Endpoint**
```typescript
GET /api/risk/kill-switch-status
Response: {
  config: { individual_max_dd: -0.40, portfolio_max_dd: -0.50 };
  current_individual_dd: number;
  current_portfolio_dd: number;
  is_active: boolean;
  triggered_at: ISO8601 | null;
  triggered_reason: string | null;
}

POST /api/risk/kill-switch/reset
Headers: { Authorization: "Bearer {token}" }
Response: { success: boolean, reset_at: ISO8601 }
```

**3. Real-Time Pubsub Channel**
```
Channel: portfolio:metrics
Message: {
  portfolio_dd: number;
  individual_dd: number;
  timestamp: ISO8601;
}
```

### Responsibility Handoff
| Component | Owner | Deadline |
|-----------|-------|----------|
| Baseline Badge UI | Track A (UX) | Day 3 |
| Kill-Switch Widget UI | Track A (UX) | Day 3 |
| Strategy baseline API | Track B (Code S-BASELINE-001) | Day 5 |
| Kill-switch logic | Track B (Code S-KILLSWITCH-001) | Day 6 |
| Pubsub real-time integration | Track B (Code) | Day 6 |
| E2E integration test | Track A (QA) | Day 7 |

---

## 5. Risk Mitigation

### Risk 1: Real-Time Update Latency
**Risk**: Widget lag causes misleading DD display
**Mitigation**:
- Poll pubsub every 100ms (5 updates/sec minimum)
- Cache last known DD if subscription drops
- Show "Updated: 5min ago" when stale (threshold: 5min)
- Fallback: Use REST endpoint every 1s if pubsub unavailable

### Risk 2: Race Condition in Kill-Switch Trigger
**Risk**: Concurrent signal execution + kill-switch trigger → signals still execute after trigger
**Mitigation**:
- Use atomic flag: `signal_execution_enabled` (managed by kill-switch logic)
- Check flag BEFORE executing each signal (microsecond latency)
- Log all signals attempted after trigger (audit trail)
- Strict ordering: detect DD breach → set flag false → pause signals

### Risk 3: Kill-Switch Reset Unauthorized
**Risk**: Non-manager user resets kill-switch, resumes risky trading
**Mitigation**:
- Role check: `user.role === "manager"` before reset
- Confirmation modal: explicit user action required
- Log user ID + timestamp of reset
- Optionally: notify team leads via Slack

### Risk 4: Stale Validation Badge
**Risk**: Strategy params changed but badge still shows ✓ (stale)
**Mitigation**:
- Add listener to strategy param changes
- Immediately mark badge NEEDS_RECHECK (yellow)
- Show alert: "Parameters changed. Re-validate strategy."
- Prevent deployment until validation passed

---

## 6. Success Definition

This feature is DONE when:

✅ **Phase 1.0 Ready for Go-Live**
- Mandatory Baseline Badge on every strategy card
- Kill-Switch Limits prominently visible with real-time updates
- Can clearly see if strategy is KatanaTransformer-validated
- Can clearly see when kill-switch will trigger
- Users understand "100% north star baseline coverage" means these features are present

✅ **Testing Complete**
- Unit tests for all badge states (green, gray, yellow, spinner, error)
- Unit tests for all DD threshold ranges (green, yellow, orange, red, triggered)
- E2E test for kill-switch trigger + reset flow
- E2E test for badge update on strategy param change
- Performance test: widgets render in <50ms

✅ **Integration Verified**
- Code APIs match UX expectations (by Day 5-6)
- Real-time pubsub delivering DD updates (<100ms latency)
- Kill-switch reset works with role check
- All events logged for audit trail
- Mobile responsive (tested on <480px, 768px, 1024px breakpoints)

✅ **Go-Live Criteria Met**
- Day 7 checkpoint: UX widgets merged with code, all tests passing
- Day 8-10: Staging deployment + final validation
- Day 11+: Production deployment

---

## 7. Files to Create/Update

| File | Status | Owner | Deadline |
|------|--------|-------|----------|
| `src/components/StrategyBaselineBadge.tsx` | NEW | Track A (UX) | Day 2 |
| `src/components/KillSwitchWidget.tsx` | NEW | Track A (UX) | Day 2 |
| `src/types/strategy.ts` | UPDATE | Track A (UX) | Day 1 |
| `src/types/risk.ts` | UPDATE | Track A (UX) | Day 1 |
| `src/api/strategies.ts` | UPDATE | Track B (Code) | Day 5 |
| `src/api/risk.ts` | UPDATE | Track B (Code) | Day 6 |
| `src/hooks/useKillSwitchStatus.ts` | NEW | Track B (Code) | Day 6 |
| `tests/components/*.test.tsx` | NEW | Track A (QA) | Day 3 |
| `tests/e2e/kill-switch.spec.ts` | NEW | Track A (QA) | Day 7 |

---

## 8. Dependencies & Blockers

### No External Blockers ✅
- Baseline Badge: Needs only strategy.metadata extension (Day 1)
- Kill-Switch Widget: Needs kill-switch logic from Code (Day 6) + pubsub channel (Day 6)

### Internal Dependencies
1. Strategy baseline API must be ready before E2E test (Day 5 blocker)
2. Kill-switch reset API must be ready before E2E test (Day 6 blocker)
3. Real-time pubsub must be working before production (Day 6 blocker)

### Contingency
If Code track delays:
- **Option A**: Mock APIs in UI for Day 3 testing, swap with real APIs on Day 7
- **Option B**: Pre-deploy UI to staging Day 3, wait for APIs, integrate Day 5
- **No Option C**: Delay go-live if either component incomplete

---

## Conclusion

**Phase 1.0 UX Blockers are READY FOR IMPLEMENTATION**

Total effort: **12-16 hours** (2-3 days, parallel with Zone 2)
Critical path: **Day 1-3** (before Day 7 Zone 2 checkpoint)
Go-live dependent: **YES** (cannot launch without these features)
North star baseline coverage: **Increases from 70-75% to 85-90%** with these components

Next step: Assign these specs to Track A implementation team on Day 1.

