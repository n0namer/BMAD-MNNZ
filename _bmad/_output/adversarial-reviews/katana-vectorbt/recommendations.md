# Prioritized Recommendations - Katana-VectorBT Phase 1
**Review Date:** 2026-02-27
**Based On:** Adversarial Review (25 critical findings) + Completeness Scorecard (68% coverage)
**Recommendation Scope:** What to fix before implementation starts

---

## Executive Summary

**25 findings across 5 categories** require prioritization. Recommend a **2-week specification hardening phase** before sprint planning to resolve **8 critical blockers** that will otherwise cause implementation delays and rework.

**Total Effort Estimate:** 40-60 hours to close all findings; 16-20 hours for Priority 1 only.

---

## PRIORITY 1: CRITICAL BLOCKERS (Must Fix Before Implementation)
**Target Completion:** End of Week 1 | **Effort:** 16-20 hours

These 8 findings will directly block implementation or cause major rework.

---

### P1-1: HNSW Vector Index Operational Specification
**Finding:** HNSW indexing claimed to give "150x-12,500x speedup" with zero operational details
**Current State:** Mentioned in Brief L143, PRD L248-280; no implementation parameters
**Impact:** Can't implement vectorization layer; optimization performance unknown

#### Recommended Specification

Create document: `architecture/hnsw-operational-spec.md`

**Section 1: Index Configuration**
```yaml
Vector Index Configuration:
  - embedding_model: sentence-transformers/all-MiniLM-L6-v2  # 384-dim
  - dimensions: 384
  - metric: cosine  # or L2, inner_product
  - hnsw_m: 16  # connections per node
  - ef_construction: 200  # construction cost
  - ef_search: 100  # query cost

Index Scaling (test data):
  - Test 1: 1K samples (10M index) - verify build time <1 sec
  - Test 2: 10K samples (100M index) - verify build time <5 sec
  - Test 3: 100K samples (1GB index) - verify build time <60 sec
  - Memory budget: 10GB max
```

**Section 2: Rebuild Triggers**
```
Rebuild Frequency:
  - Trigger 1: Every 100 new samples added
  - Trigger 2: After optimization run completes
  - Trigger 3: Daily full rebuild (off-peak)
  - NO: Real-time incremental updates (too slow)

Rebuild Timing:
  - Backtest phase: Index snapshot at trial start (read-only)
  - Live phase: Rebuild hourly if new data arrives
  - Max staleness: 1 hour (if no new data)
```

**Section 3: Staleness Detection**
```
Staleness Check:
  - Track index version = hash(dataset + build_timestamp)
  - Compare index_version vs current_dataset_version
  - If mismatch: log warning "index is X hours old"
  - If drift > 24 hours: trigger rebuild alert
```

**Section 4: Memory Management**
```
Memory Budget:
  - Index size: N_samples * 384_dim * 4_bytes * (1 + M/2) ≈ 0.1MB per sample
  - Example: 10K samples ≈ 1GB
  - Monitor: PSUtil memory usage; alert if >80% budget
  - Eviction: LRU cache, keep last 3 rebuilt indices
```

**Section 5: Performance Validation**
```
Validation Tests:
  - Test speedup: Time vector search(1000 queries) vs brute force
  - Expected: HNSW >100x faster for 10K+ samples
  - Sanity check: Correctness (top-K must be identical to brute force)
  - Regression: Monthly benchmark, alert if speedup degrades >20%
```

**Deliverables:**
- [ ] Config spec (embedding model, M, ef values)
- [ ] Rebuild trigger algorithm
- [ ] Staleness detection mechanism
- [ ] Memory budget math + monitoring
- [ ] Performance validation test suite

**Acceptance Criteria:**
- Index builds for 10K samples in <5 seconds
- Search query time <100ms for 1000 queries
- Memory usage predicted within ±10% of actual
- Staleness detected within 1 hour

**Effort:** 4 hours

---

### P1-2: DFF Conditional Parameter Sampling Grammar
**Finding:** Brief claims "only active params sampled" but provides no formal grammar
**Current State:** Mentioned in Brief L141-145; no BNF or decision table
**Impact:** Optuna sampler can't determine which params to sample per trial

#### Recommended Specification

Create document: `architecture/dff-parameter-sampling-spec.md`

**Section 1: Parameter Dependency Matrix**
```
SOURCE_TYPE -> REQUIRED_PARAMS mapping

ATR:
  - Required: atr_period, atr_multiplier
  - Optional: none
  - Forbidden: bb_period, bb_width, fixed_pct_value
  - Example: {atr_period: 20, atr_multiplier: 1.5}

BB (Bollinger Bands):
  - Required: bb_period, bb_width
  - Optional: none
  - Forbidden: atr_period, fixed_pct_value, corwin_period
  - Example: {bb_period: 20, bb_width: 2.0}

FIXED_PCT:
  - Required: fixed_pct_value
  - Optional: none
  - Forbidden: atr_period, bb_period, etc.
  - Example: {fixed_pct_value: 0.5}

RANGE:
  - Required: none (uses high - low)
  - Optional: range_multiplier
  - Forbidden: all others
  - Example: {range_multiplier: 1.0}

STDDEV:
  - Required: stddev_period, stddev_multiplier
  - Optional: none
  - Forbidden: atr_period, bb_period, etc.
  - Example: {stddev_period: 20, stddev_multiplier: 1.5}

CORWIN_SCHULTZ:
  - Required: corwin_period
  - Optional: none
  - Forbidden: atr_period, bb_period, etc.
  - Example: {corwin_period: 20}
```

**Section 2: Conditional Sampling Algorithm (BNF)**
```
<TRIAL_PARAMS> ::= <ROLE_PARAMS> (<ROLE_PARAMS>)*

<ROLE_PARAMS> ::= "role=" <ROLE>
                  "source_type=" <SOURCE_TYPE>
                  <SOURCE_PARAMS>
                  "multiplier=" <MULTIPLIER>

<ROLE> ::= "SL" | "TP" | "BE" | "Trail"

<SOURCE_TYPE> ::= "ATR" | "BB" | "FIXED_PCT" | "RANGE" | "STDDEV" | "CORWIN_SCHULTZ"

<SOURCE_PARAMS> ::= <ATR_PARAMS> | <BB_PARAMS> | ... (see matrix above)

<ATR_PARAMS> ::= "atr_period=" <RANGE_INT(5, 50)>
                 "atr_multiplier=" <RANGE_FLOAT(0.5, 3.0)>

<MULTIPLIER> ::= <RANGE_FLOAT(0.5, 5.0)> (10.0 allowed for rocket TP only)

Constraint: total_active_params ≤ 70 per trial
Constraint: tp_multiplier ≥ sl_multiplier (take-profit must be larger than stop-loss)
Constraint: Each role sampled exactly once (no duplicates)
```

**Section 3: Optuna Integration Example**
```python
def suggest_dff_params(trial, profile: StrategyProfile):
    """Suggest DFF params respecting dependencies."""
    params = {}

    for role in ['SL', 'TP', 'BE', 'Trail']:
        source_type = trial.suggest_categorical(
            f'{role}_source_type',
            profile.allowed_source_types
        )

        # Conditional sampling based on source_type
        if source_type == 'ATR':
            params[f'{role}_atr_period'] = trial.suggest_int(f'{role}_atr_period', 5, 50)
            params[f'{role}_atr_multiplier'] = trial.suggest_float(f'{role}_atr_multiplier', 0.5, 3.0)
        elif source_type == 'BB':
            params[f'{role}_bb_period'] = trial.suggest_int(f'{role}_bb_period', 5, 50)
            params[f'{role}_bb_width'] = trial.suggest_float(f'{role}_bb_width', 1.0, 3.0)
        # ... (other types)

        # Common multiplier
        max_mult = 10.0 if (role == 'TP' and is_rocket) else 5.0
        params[f'{role}_multiplier'] = trial.suggest_float(
            f'{role}_multiplier', 0.5, max_mult
        )

    # Validate constraint: TP ≥ SL
    if params.get('TP_multiplier', 0) < params.get('SL_multiplier', 0):
        raise ValueError("TP_multiplier must be >= SL_multiplier")

    return params
```

**Section 4: Active Parameter Count Validation**
```
Profile Example (Scalping Profile):
  Active params:
    - SL: {atr_period, atr_multiplier, multiplier} = 3 params
    - TP: {atr_period, atr_multiplier, multiplier} = 3 params
    - BE: {atr_period, atr_multiplier, multiplier} = 3 params
    - Trail: {fixed_pct_value, multiplier} = 2 params
  Total: 3+3+3+2 = 11 params << 70 cap ✅

Profile Example (Swing Trade Profile):
  Active params:
    - SL: {bb_period, bb_width, multiplier} = 3
    - TP: {bb_period, bb_width, multiplier} = 3
    - BE: {stddev_period, stddev_multiplier, multiplier} = 3
    - Trail: {atr_period, atr_multiplier, multiplier} = 3
  Total: 12 params << 70 cap ✅
```

**Deliverables:**
- [ ] Parameter dependency matrix for all 6 source types
- [ ] BNF grammar for sampling algorithm
- [ ] Optuna integration code example
- [ ] Active param count validation rules
- [ ] Test cases (valid/invalid parameter combinations)

**Acceptance Criteria:**
- All source types enumerated with required/forbidden params
- Optuna sampler can generate valid params without errors
- Active param count ≤ 70 for all profiles
- Invalid combinations (tp < sl, missing required params) are rejected

**Effort:** 5 hours

---

### P1-3: Multi-Timeframe Signal Aggregation Algorithm
**Finding:** "Each TF trades independently" but collision resolution undefined
**Current State:** Brief L99-107 says default "NO cross-TF bias gating"; no algorithm
**Impact:** System can't execute trades when multiple TFs conflict

#### Recommended Specification

Create document: `architecture/mtf-signal-aggregation-spec.md`

**Section 1: Signal Conflict Scenarios**
```
Scenario 1: Agreement
  1m TF: BUY
  5m TF: BUY
  15m TF: BUY
  Resolution: EXECUTE BUY (unanimous)

Scenario 2: Majority Vote
  1m TF: BUY
  5m TF: BUY
  15m TF: SELL
  1h TF: HOLD
  Resolution (MAJORITY_VOTE): BUY (2/4 vote)

Scenario 3: Conflict / No Consensus
  1m TF: BUY
  5m TF: SELL
  15m TF: SELL
  1h TF: HOLD
  Resolution (NO_CONSENSUS): NO TRADE or CONSENSUS_THRESHOLD check

Scenario 4: Each TF Independent (Default v1.0)
  1m TF: BUY (opens 1m position)
  5m TF: SELL (opens 5m position) — SAME SYMBOL, opposite direction
  Result: Can 1m and 5m hold opposite positions? How does this affect P&L?
```

**Section 2: Aggregation Modes**
```
Mode 1: INDEPENDENT (Default v1.0)
  - Each TF manages own position
  - Multiple TFs can hold opposite positions on same symbol
  - Risk: Hedged positions cost money (double commission, slippage)
  - Recommendation: Use for scalping (1m/5m fast reversal)

Mode 2: MAJORITY_VOTE
  - Votes: BUY=+1, HOLD=0, SELL=-1
  - Result: aggregate_signal = sum(votes) / N
  - Threshold: if aggregate > +0.5 → BUY; < -0.5 → SELL; else HOLD
  - Risk: Can suppress minority signals
  - Recommendation: Use for swing trades (hourly/daily)

Mode 3: PRIORITY_HIERARCHY
  - Rank TFs: 1h > 5m > 1m
  - If 1h says HOLD, override all others → HOLD
  - If 1h says BUY, others can only amplify (not reverse)
  - Risk: Large TF can suppress faster TFs
  - Recommendation: Use for managed portfolios

Mode 4: FIRST_TF_SIGNAL
  - First TF to signal wins (based on execution order)
  - Others blocked until first closes
  - Risk: Order-dependent, not repeatable
  - Recommendation: NOT RECOMMENDED
```

**Section 3: Implementation Algorithm**
```python
def aggregate_mtf_signals(signals: Dict[str, str], mode: str) -> str:
    """Aggregate signals from multiple timeframes."""

    if mode == "INDEPENDENT":
        # Each TF executes independently
        # Note: Multiple positions on same symbol allowed
        return signals  # Return all signals; caller processes each

    elif mode == "MAJORITY_VOTE":
        vote_map = {'BUY': +1, 'HOLD': 0, 'SELL': -1}
        votes = [vote_map.get(signals.get(tf, 'HOLD'), 0) for tf in ['1m', '5m', '15m', '1h', '4h', '1d']]
        aggregate = sum(votes) / len(votes)

        if aggregate > 0.5:
            return 'BUY'
        elif aggregate < -0.5:
            return 'SELL'
        else:
            return 'HOLD'

    elif mode == "PRIORITY_HIERARCHY":
        # Check in order: 1h → 5m → 1m
        for tf in ['1h', '5m', '1m']:
            if tf in signals and signals[tf] != 'HOLD':
                return signals[tf]
        return 'HOLD'

    else:
        raise ValueError(f"Unknown aggregation mode: {mode}")
```

**Section 4: Position Sizing with MTF Aggregation**
```
INDEPENDENT mode:
  1m TF: BUY EURUSD 1 lot (small, scalp)
  5m TF: SELL EURUSD 0.5 lot (medium, hedge)
  Net: 0.5 lot long (hedge inefficient)

MAJORITY_VOTE mode:
  Aggregate signal: BUY (2/4 signals)
  Position: BUY EURUSD 1 lot (single position, no hedge)

Decision: Use INDEPENDENT for scalping portfolios; MAJORITY_VOTE for swing/trend trading.
```

**Section 5: Configuration**
```yaml
mtf_aggregation:
  mode: "INDEPENDENT"  # or "MAJORITY_VOTE", "PRIORITY_HIERARCHY"

  # INDEPENDENT mode settings
  allow_opposite_positions: true  # Can 1m be long while 5m is short?

  # MAJORITY_VOTE settings
  vote_threshold: 0.5  # 50%+ needed for signal

  # PRIORITY_HIERARCHY settings
  hierarchy: ["1h", "5m", "1m", "1d", "4h", "15m"]

  # Telemetry
  track_consensus_rate: true  # How often do TFs agree?
  track_conflict_resolution: true  # Which mode was used?
```

**Deliverables:**
- [ ] Signal conflict scenarios documented (4+ scenarios)
- [ ] Aggregation modes defined with recommendations
- [ ] Implementation algorithm (pseudocode)
- [ ] Position sizing rules per mode
- [ ] Configuration schema with examples
- [ ] Test cases (edge cases like 3-way tie)

**Acceptance Criteria:**
- No undefined behavior for any conflict scenario
- Each mode has clear pros/cons and use case
- Implementation handles 3-way, 4-way, 6-way ties correctly
- Telemetry captures consensus rate for monitoring

**Effort:** 4 hours

---

### P1-4: Kill-Switch Recovery Mechanism
**Finding:** Kill-switch triggers defined (VIX >80, DD >50%), recovery mechanism missing
**Current State:** Brief L42-43, Architecture Decision 2 "BLACK = crisis_halt"; no recovery
**Impact:** System remains dead after crisis; operator must manually restart

#### Recommended Specification

Create document: `operations/kill-switch-recovery-spec.md`

**Section 1: Kill-Switch States**
```
State Machine:
  NORMAL  ─(VIX > 80 OR DD > 50%)──→  YELLOW  ─(metrics persist)──→  RED
    ↑                                     ↓                             ↓
    └────────────(recovery)──────────────┴─────────────(recovery)──────┘

NORMAL: All strategies trading normally
YELLOW: Warning state; limit position size to 50%; monitor closely
RED: Risk off; close positions over next 5 candles (avoid slippage); no new trades
BLACK: Emergency; close all orders immediately; frozen until manual review

Recovery Conditions:
  YELLOW → NORMAL: VIX < 60 AND DD < 30 for 5 consecutive candles
  RED → YELLOW: VIX < 50 AND DD < 20 for 5 consecutive candles
  BLACK → (manual): Operator must review and manually confirm reset
```

**Section 2: Kill-Switch Triggering**
```
Trigger 1: VIX-based
  - Data source: SPX VIX (or EURUSD volatility proxy)
  - Threshold: VIX > 80
  - Check frequency: Every candle close
  - Action: Transition to RED state

Trigger 2: Drawdown-based
  - Data source: Portfolio max drawdown (calculated real-time)
  - Threshold: Cumulative DD > 50% NAV
  - Check frequency: Every trade
  - Action: Transition to RED state

Trigger 3: Combination (BLACK):
  - Both VIX > 90 AND DD > 50% AND trade failed
  - Action: IMMEDIATE close all, transition to BLACK
```

**Section 3: Recovery Mechanism**
```
Passive Recovery (Automatic):
  Condition 1: VIX < 50 AND DD < 20 for 5 consecutive 1-hour candles
  Condition 2: No order rejections in last 10 minutes
  → Transition RED → YELLOW

  Condition 3 (YELLOW → NORMAL): VIX < 40 AND DD < 10 for 8 consecutive candles
  → Transition YELLOW → NORMAL

Operator Recovery (Manual):
  BLACK state: Requires explicit operator approval to reset
  - Operator reviews dashboard
  - Approves reset action (checkbox + 2FA)
  → Transition BLACK → NORMAL (if confirmed)

Cool-Down Period:
  After recovery, minimum 5 minutes before next trade
  → Prevents whipsaw (market briefly recovers, system crashes again)
```

**Section 4: Position Closure Strategy**
```
RED State: "Risk Off" Closure
  1. Mark all open positions as "to close"
  2. Generate close orders over 5 candles (5% per candle)
  3. Use limit orders (not market) to avoid slippage
  4. Example:
     - Candle 1: Close 20% of position (limit order 2 pips away)
     - Candle 2: Close 20% (limit order)
     - ...
     - Candle 5: Close remaining 0% (market order if needed)

BLACK State: "Emergency" Closure
  1. Immediately market order close all positions
  2. Cancel all pending orders
  3. Alert operator (email, SMS, dashboard)
  4. Log all details for post-mortem
  5. Frozen state until operator reset
```

**Section 5: Telemetry**
```
Kill-Switch Metrics:
  - trigger_count: Number of times kill-switch triggered
  - time_in_yellow: Cumulative hours in YELLOW state
  - time_in_red: Cumulative hours in RED state
  - recovery_success_rate: % of recovery attempts that succeeded
  - false_positive_rate: % of triggers that recovered within 1 hour
  - capital_preserved: % NAV saved by kill-switch activation

Alerts:
  - Dashboard: Visual indicator (RED banner) when kill-switch active
  - Email: Alert sent when transitioning RED → YELLOW → NORMAL
  - Slack: Crisis-level alert for BLACK state
  - Log: All transitions logged with timestamp, metrics, reason
```

**Section 6: Configuration**
```yaml
kill_switch:
  enabled: true

  vix_threshold: 80  # Trigger RED on VIX > 80
  dd_threshold: 50   # Trigger RED on DD > 50%
  black_threshold_vix: 90  # Emergency on VIX > 90
  black_threshold_dd: 50
  black_trigger_and: true  # Both must be true for BLACK

  recovery_conditions:
    yellow_to_normal:
      vix_max: 40
      dd_max: 10
      consecutive_candles: 8
    red_to_yellow:
      vix_max: 50
      dd_max: 20
      consecutive_candles: 5

  closure_strategy: "TAPER"  # or "IMMEDIATE" for BLACK
  closure_rate: 0.2  # 20% per candle in RED state

  cooldown_minutes: 5  # After recovery, wait before next trade

  telemetry:
    track_triggers: true
    track_recoveries: true
    track_capital_preserved: true
```

**Deliverables:**
- [ ] State machine diagram (NORMAL → YELLOW → RED → BLACK)
- [ ] Recovery conditions formalized (VIX/DD thresholds, duration)
- [ ] Position closure algorithm (taper vs immediate)
- [ ] Manual recovery procedure for BLACK state
- [ ] Telemetry metrics and alerts
- [ ] Configuration schema with safe defaults
- [ ] Test scenarios (VIX spike, DD > 50%, recovery sequence)

**Acceptance Criteria:**
- System automatically recovers from RED to NORMAL (no operator input needed)
- BLACK state explicitly requires operator confirmation to reset
- Position closure never causes >2% slippage (TAPER strategy)
- Recovery process logged with timestamp, reason, metrics
- Dashboard shows kill-switch state clearly

**Effort:** 4 hours

---

### P1-5: Dashboard Trading Control Flows
**Finding:** Dashboard shows data but UX for controls (position sizing, stop-loss, override) is missing
**Current State:** Epic 1 focused on display; no interaction flows documented
**Impact:** Users can view but can't control; "≤3 h/week manual participation" claim is unvalidated

#### Recommended Specification

Create document: `ux/dashboard-trading-flows.md`

**Section 1: Core Control Flows**
```
Flow 1: Adjust Position Size (during live trading)
  1. User sees: "Position: EURUSD 2.0 lots, P&L: +$500"
  2. User clicks: "Edit Position" button
  3. Dialog opens: "Adjust Position Size"
     - Current: 2.0 lots
     - Input field: [___] lots (allow 0.1 to 10.0)
     - Risk label: "New P&L variance: ±$X"
  4. User enters: 3.0 lots
  5. System validates: "Max 5% NAV = 4.0 lots, your input OK"
  6. User clicks: "Confirm Adjustment"
  7. System executes: Close 0.5 lot OR add 1.0 lot (depending on current)
  8. Confirmation: "Position adjusted to 3.0 lots (cost: $150 slippage)"

Flow 2: Manually Close Position
  1. User sees: "EURUSD: +$500, 5m remaining until TP"
  2. User clicks: "Close Position" button
  3. Confirmation dialog: "Close EURUSD 2.0 lots?"
  4. System shows: "Estimated exit price: $X (current ±2 pips slippage)"
  5. User confirms
  6. System executes market order
  7. Confirmation: "Closed EURUSD 2.0 lots; realized P&L: $485"

Flow 3: Set Manual Stop-Loss
  1. User sees: "EURUSD: +$500, current SL at -$100"
  2. User clicks: "Edit Stop-Loss"
  3. Dialog: "Manual Stop-Loss Override"
     - Current SL: -$100 (system-recommended)
     - Override: [____] (allow -$50 to -$500)
     - Risk: "If triggered, loss = -$X (Y% NAV)"
  4. User enters: -$200
  5. System validates: "SL > position entry? OK" / "SL further than portfolio max loss? WARNING"
  6. User confirms
  7. System updates: Order SL to new level; logs override reason
  8. Confirmation: "SL override to -$200 (cost if triggered: $200)"

Flow 4: Override DFF Parameters
  1. User sees: "Strategy params: ATR(20), TP×1.5, SL×2.0"
  2. User clicks: "Edit Parameters"
  3. Dialog: "Parameter Override"
     - ATR period: [20] ← read-only? or editable?
     - TP multiplier: [1.5] ← editable
     - SL multiplier: [2.0] ← editable
  4. User changes: TP×2.0
  5. System validates: "TP ≥ SL? Yes (2.0 ≥ 2.0)"
  6. User confirms
  7. System applies: New params to next signal
  8. Confirmation: "Params updated; takes effect on next signal"

Flow 5: Pause Strategy
  1. User sees: "Strategy: Running (50 trades/day)"
  2. User clicks: "Pause Strategy"
  3. Confirmation: "Pause EURUSD scalper?"
  4. System: Stops new signal generation; doesn't close existing positions
  5. Confirmation: "Strategy paused; 2 open positions held"
  6. User can click: "Resume Strategy" → Resumes normal operation

Flow 6: Emergency Liquidate (Manual Override)
  1. User sees: Dashboard with RED banner "VIX > 80, Kill-Switch Active"
  2. User clicks: "Manual Override: Close All"
  3. Warning dialog: "This will close ALL open positions immediately!"
  4. System shows: "Affected positions: EURUSD (2.0 lots), GBPUSD (1.0 lot)"
  5. User confirms (2FA optional)
  6. System executes market close on all positions
  7. Confirmation: "All positions closed; total realized loss: -$500"
```

**Section 2: UX Mockups (Wireframes)**
```
Dashboard Layout (Key Trading Controls):

┌─────────────────────────────────────┐
│ KATANA - Trading Dashboard          │
├─────────────────────────────────────┤
│ Status: [●] TRADING  VIX: 45  DD: -8% │
├─────────────────────────────────────┤
│ OPEN POSITIONS                      │
├─────────────────────────────────────┤
│ ┌─ EURUSD (Scalp) ─────────────────┐│
│ │ Entry: 1.0850 | Current: 1.0872  ││
│ │ Size: 2.0 lots | P&L: +$440      ││
│ │ SL: 1.0820 | TP: 1.0900          ││
│ │ [Edit SL] [Edit Size] [Close]    ││
│ │ Next Signal: 5m TP ~2 min        ││
│ └─────────────────────────────────┘│
│ ┌─ GBPUSD (Swing) ──────────────────┐│
│ │ Entry: 1.2650 | Current: 1.2670  ││
│ │ Size: 1.0 lot  | P&L: +$200      ││
│ │ SL: 1.2600 | TP: 1.2750          ││
│ │ [Edit SL] [Edit Size] [Close]    ││
│ │ Next Signal: 1h TP ~45 min       ││
│ └─────────────────────────────────┘│
│                                    │
│ [View Closed Trades] [View History]│
│ [Edit Strategy Params] [Pause All] │
│ [Export Report]                    │
└─────────────────────────────────────┘
```

**Section 3: Permission Model**
```
User Role: Operator

Allowed Actions:
  ✅ Close position (any time)
  ✅ Adjust position size (within 50% of current)
  ✅ Edit stop-loss (can only tighten, not loosen)
  ✅ Pause/resume strategy
  ✅ View positions, P&L, history
  ✅ Export reports

Disallowed Actions:
  ❌ Edit entry price
  ❌ Modify profit target (can only tighten)
  ❌ Delete historical trades
  ❌ Change account funding
  ❌ Disable kill-switch
```

**Section 4: Estimated Time Per Action**
```
Action             Time   Complexity   Risk
─────────────────────────────────────────
Close position     <1 min    Low        Low
Adjust size        <2 min    Low        Medium
Set manual SL      <2 min    Low        Low
Pause strategy     <1 min    Low        Low
Override params    <3 min    Medium     Medium
Emergency liquidate<1 min    Low        High (but necessary)

Total per day: 5 actions × 2 min = 10 min << 3 h/week (180 min)
✅ Claim "≤3 h/week manual participation" is feasible
```

**Section 5: Error Handling**
```
Error 1: Position Size Out of Range
  User input: "10.0 lots" but max is 5.0 lots (5% NAV rule)
  System response: "Cannot adjust: Max position 5.0 lots (5% NAV risk rule)"
  User action: Reduce to ≤5.0 or accept

Error 2: SL > Entry Price
  User sets: SL at 1.0900 but entry at 1.0850 (impossible)
  System response: "Invalid: SL cannot be above entry price"
  User action: Correct input

Error 3: Kill-Switch Active
  User tries to: "Close Position"
  System response: "Kill-switch RED state: positions closing automatically (2/5 candles done)"
  User action: Wait for automatic closure or emergency override

Error 4: Order Rejection
  User clicks: "Close EURUSD"
  Broker response: "Order rejected (insufficient liquidity)"
  System response: "Close failed; broker returned: insufficient liquidity"
  User action: Retry with limit order or wait
```

**Section 6: Testing Checklist**
```
Functional Tests:
  [ ] Close position executes immediately
  [ ] Adjust position size updates correctly
  [ ] Manual SL edit prevents invalid states (TP < SL)
  [ ] Override params apply to next signal only
  [ ] Pause strategy stops new signals but keeps existing positions
  [ ] Emergency liquidate closes all positions
  [ ] All actions logged with timestamp and user

UX Tests:
  [ ] Each flow completes in <3 minutes
  [ ] All error messages are clear and actionable
  [ ] Confirmation dialogs prevent accidental actions
  [ ] Mobile-responsive (if applicable)
  [ ] Keyboard shortcuts available (Tab, Enter, Escape)

Performance Tests:
  [ ] Dashboard refresh <1 sec after action
  [ ] Order execution <5 sec after user click
  [ ] No lag on position size slider
```

**Deliverables:**
- [ ] 6 core control flows documented
- [ ] UX mockups/wireframes for each flow
- [ ] Permission model clarified (what can user do/not do)
- [ ] Error handling for each flow
- [ ] Time estimate per action (validate ≤3 h/week claim)
- [ ] Testing checklist (functional, UX, performance)
- [ ] Mobile/accessibility considerations

**Acceptance Criteria:**
- All 6 control flows documented with step-by-step UX
- Error messages are clear and actionable
- Each action completes in <3 minutes
- System prevents invalid states (SL > TP, size > limits)
- "≤3 h/week" claim is validated by flow timings

**Effort:** 4 hours

---

### P1-6: Convergence Definition for Optuna
**Finding:** "Optuna convergence ≤50 trials" stated as NFR; convergence definition missing
**Current State:** Brief L1405; target stated, definition absent
**Impact:** Can't validate SLA in production; performance claims untestable

#### Recommended Specification

Create document: `architecture/optimization-convergence-spec.md`

**Section 1: Convergence Definition**
```
Definition Option 1: Pareto Hypervolume Plateau
  - Metric: Hypervolume of Pareto front (multi-objective)
  - Convergence: If hypervolume improves <2% over 15 consecutive trials
  - Formula: (HV_T - HV_{T-15}) / HV_{T-15} < 0.02
  - Pros: Robust to outliers; works for multi-objective
  - Cons: Expensive to compute

Definition Option 2: Trial Loss Plateau
  - Metric: Best trial loss (single-objective)
  - Convergence: If best_loss improves <1% over 20 consecutive trials
  - Formula: (loss_T - loss_{T-20}) / |loss_{T-20}| < 0.01
  - Pros: Simple, fast; fits typical single-objective
  - Cons: May converge prematurely if late improvement exists

Definition Option 3: Median Trial Variance
  - Metric: Variance of last 10 trials' scores
  - Convergence: If variance < threshold (e.g., 0.5% of mean)
  - Formula: std(trials[T-10:T]) / mean(trials[T-10:T]) < 0.005
  - Pros: Detects when trials are "noisy but converged"
  - Cons: Requires stable baseline

RECOMMENDED: Use Definition Option 2 (simple + reliable)
  - Best loss improves <1% over 20 consecutive trials → CONVERGED
  - Measurement: track for each trial; convergence flag set automatically
```

**Section 2: Optuna Sampler Configuration**
```yaml
optuna_config:
  sampler: "TPESampler"  # Tree-structured Parzen Estimator

  # TPE parameters
  seed: 42  # For reproducibility
  consider_prior: true
  prior_weight: 1.0
  consider_magic_clip: true

  # Pruning strategy (early stopping)
  pruner: "SuccessiveHalvingPruner"
  pruner_config:
    reduction_factor: 3  # Eliminate bottom 2/3 each round
    min_resource: 1
    min_early_stopping_rate: 0  # Don't stop super early
    n_warmup_steps: 5  # Run at least 5 trials before pruning

  study_direction: "maximize"  # Sharpe, P&L
  n_trials: 50  # Max 50 trials per study
  timeout_seconds: 3600  # Max 1 hour per study

  convergence_check:
    enabled: true
    method: "loss_plateau"
    loss_threshold: 0.01  # 1% improvement
    window_size: 20  # Over 20 trials
    check_every_n_trials: 5  # Check after every 5th trial

  # If converged early, stop the study
  early_stop_on_convergence: true
```

**Section 3: Convergence Validation Test**
```python
def test_convergence_definition():
    """Validate that convergence is detected correctly."""

    # Mock scenario: Optimization that converges after 35 trials
    trial_losses = [
        # Initial trials (improving)
        1.0, 0.95, 0.92, 0.90, 0.89,
        0.88, 0.87, 0.865, 0.863, 0.862,
        # Mid (still improving)
        0.8615, 0.861, 0.8608, 0.8607, 0.8606,
        0.8605, 0.8604, 0.8603, 0.8602, 0.8601,
        # Late (plateau — improves <1%)
        0.8600, 0.8599, 0.8598, 0.8597, 0.8596,
        0.8595, 0.8594, 0.8593, 0.8592, 0.8591,
        0.8590, 0.8589, 0.8588, 0.8587, 0.8586,
        # Post-plateau (verify no improvement)
        0.8586, 0.8586, 0.8586, 0.8586, 0.8586,
    ]

    convergence_trial = detect_convergence(trial_losses, threshold=0.01, window=20)
    assert convergence_trial == 35, f"Expected converge at trial 35, got {convergence_trial}"

    # Verify: trials 35-40 improve <1%
    improvement = (trial_losses[34] - trial_losses[39]) / trial_losses[34]
    assert improvement < 0.01, f"Expected <1% improvement, got {improvement*100}%"
```

**Section 4: SLA Validation**
```
Claim: "Optuna convergence ≤50 trials"

Test 1: Synthetic Data (Known Convergence)
  - Generate 1000 random optimization problems (varying dimensionality)
  - Run each with TPE sampler + SuccessiveHalving pruner
  - Measure: % that converge by trial 50
  - Target: ≥95% converge by trial 50 (allows 5% outliers)

Test 2: Real Strategy Data (Historical Backtests)
  - Select 10 historical backtest configurations
  - Run Optuna on each
  - Measure: Average trial count to convergence
  - Target: Mean ≤ 40 trials

Test 3: Edge Cases
  - High-dimensional (115 params, conditional): How many trials?
  - Low-dimensional (10 params): Should converge faster
  - Noisy (add ±5% noise to trial scores): How does it affect convergence?

Acceptance: If ≥95% of test cases converge by trial 50, SLA is MET.
```

**Section 5: Monitoring & Alerting**
```
Metrics to Track:
  - trial_count_to_convergence: How many trials until convergence?
  - convergence_rate: % of optimization runs that converge within N trials
  - early_stop_rate: % of trials pruned early (efficient sampling)
  - final_best_loss: Quality of final best parameters

Dashboard Metrics:
  - "Avg trials to convergence: 38" (vs SLA target 50)
  - "Convergence rate: 96% within 50 trials"
  - "Early pruning saves avg 12 trials/study"

Alerts:
  - Alert if convergence_rate drops below 90%
  - Alert if avg trial_count > 45 (trending toward SLA breach)
  - Alert if early_stop_rate < 50% (pruner not aggressive enough)
```

**Section 6: Configuration Reference**
```yaml
# Convergence SLA Configuration
optimization_sla:
  max_trials: 50
  max_time_seconds: 3600  # 1 hour max per study
  convergence_threshold: 0.01  # 1% improvement required
  convergence_window: 20  # Over 20 trials
  success_rate_target: 0.95  # 95% should converge by trial 50

# Monitoring
monitoring:
  track_convergence: true
  alert_convergence_rate_below: 0.90
  alert_trial_count_above: 45
```

**Deliverables:**
- [ ] Convergence definition formalized (loss plateau method)
- [ ] Optuna sampler + pruner configuration documented
- [ ] Validation test cases (synthetic + real strategy data)
- [ ] SLA acceptance criteria (≥95% converge by trial 50)
- [ ] Monitoring metrics and alerts
- [ ] Edge case analysis (high-dim, noisy, etc.)

**Acceptance Criteria:**
- Convergence definition is unambiguous and testable
- Optuna configuration validated to meet SLA
- ≥95% of test runs converge within 50 trials
- Monitoring dashboard shows convergence rate
- Alerts trigger if SLA trend worsens

**Effort:** 3 hours

---

## PRIORITY 2: HIGH-IMPACT FIXES (Should Fix Week 1)
**Target Completion:** End of Week 1-2 | **Effort:** 12-15 hours

These 7 findings will cause implementation delays or incorrect P&L calculations if not addressed.

---

### P2-1: Rocket Portfolio Allocation Edge Case Analysis
**Finding:** Concurrent promotions + new entries can exceed 10% cap; math not validated
**Current State:** Brief L594-598, Architecture Decision 1; no simulation
**Impact:** Risk-of-ruin claim (5%) unvalidated; capital allocation may exceed cap

**Recommended Approach:**
1. Create allocation algorithm (pseudocode)
2. Run Monte Carlo: 1000 simulations with random concurrent entries/promotions
3. Verify: max allocation never exceeds 10% under all conditions
4. Document edge cases: what happens if kill-switch fires during promotion?
5. Add tests to codebase

**Deliverables:**
- Allocation algorithm with invariant proofs
- Monte Carlo simulation (1000 runs)
- Edge case test matrix (concurrent scenarios)
- Capital allocation unit tests

**Effort:** 4 hours

---

### P2-2: Multi-Instrument Backtesting Cost Schedule
**Finding:** "After costs" mentioned; fee schedule per broker/instrument undefined
**Current State:** Brief L2107 "Net P&L (after costs)"; no fee details
**Impact:** Success criteria validation incorrect; P&L calculations off by 0.5-2%

**Recommended Approach:**
1. Document fee schedule by broker (MT5 0.2%, KuCoin 0.05%)
2. Add slippage assumptions (bid-ask spread model)
3. Create fee matrix (instrument-specific: FX vs crypto vs commodities)
4. Test: backtest with fees vs without fees; verify cost impact
5. Update Brief/PRD with cost assumptions

**Deliverables:**
- Broker fee matrix (MT5, KuCoin, CCXT)
- Slippage assumption model
- Instrument-specific fees documented
- Backtest validation (verify P&L impact)

**Effort:** 3 hours

---

### P2-3: Data Pipeline Freshness SLA
**Finding:** "Fresh data" assumed; no freshness guarantee or latency budget
**Current State:** Brief L2124 instruments listed; no SLA
**Impact:** Stale data invalidates backtest; live trading risks missed signals

**Recommended Approach:**
1. Specify: "MT5 data must arrive within X minutes of candle close"
2. Define fallback: "If MT5 delayed >10 min, use KuCoin as fallback"
3. Add version tracking: "Data versioned by hash; backtest reproducible"
4. Implement staleness detection: "Alert if data >1 hour old"
5. Add dashboard indicator: "Data freshness: 2 min old (✅ OK)"

**Deliverables:**
- Data freshness SLA documented (MT5 within 5 min)
- Fallback data source strategy
- Data version control scheme
- Dashboard staleness indicator

**Effort:** 3 hours

---

### P2-4: Portfolio Rebalancing Algorithm & Schedule
**Finding:** "Rebalance + RCA" mentioned; schedule and algorithm undefined
**Current State:** Brief L43 "Portfolio DD >50% = freeze + rebalance"; no spec
**Impact:** Allocation drift uncontrolled; rebalancing costs uncalculated

**Recommended Approach:**
1. Define rebalance frequency (daily EOD vs weekly)
2. Define algorithm (proportional to target allocations)
3. Define cost constraint ("Max 5% NAV turnover per rebalance")
4. Implement conflict detection (rebalance during trade execution)
5. Test: verify allocation stays within caps

**Deliverables:**
- Rebalance frequency specification
- Algorithm pseudocode (proportional, min-turnover)
- Cost budget and constraints
- Conflict detection logic
- Backtesting with rebalance costs

**Effort:** 3 hours

---

### P2-5: Security Baseline for Phase 1
**Finding:** Security NFRs entirely deferred to Phase 3; Phase 1 has zero baseline
**Current State:** Brief NFR11-15 "Phase 3"; no Phase 1 security assumptions
**Impact:** Phase 2 blocked waiting for security architecture; audit risk

**Recommended Approach:**
1. Document Phase 1 security assumptions: "Single-user, local deployment assumed"
2. Specify minimum auth: "API key or basic auth (no TLS required for MVP)"
3. Define data handling: "No encryption required; single-user local filesystem"
4. Plan Phase 2 transition: "Multi-user requires encryption, auth, permissions"
5. Add security scanning: "Weekly dependency updates, no known vulns"

**Deliverables:**
- Phase 1 security assumptions documented
- Minimum auth mechanism (API key)
- Data handling guidelines (local filesystem OK)
- Phase 2 security roadmap
- Dependency scanning setup

**Effort:** 2 hours

---

### P2-6: Smoke Test Definition & Acceptance Criteria
**Finding:** "Smoke test results display" claimed; test definition and criteria missing
**Current State:** Brief L1403 FR9; no definition
**Impact:** Unclear what "pass" means; QA can't validate feature

**Recommended Approach:**
1. Define smoke test: "Min 100 trades across 3 FX majors; 2-week backtest window"
2. Define pass criteria: "Profit Factor > 1.0 AND max trade loss < 5% NAV"
3. Define fail criteria: "Any winning trade? Must have ≥3"
4. Implement dashboard display: "Pass ✅ / Fail ❌ with metric details"
5. Add regression testing: "Compare smoke test results vs baseline"

**Deliverables:**
- Smoke test definition (100 trades, 3 FX majors, 2 weeks)
- Pass/fail criteria documented
- Dashboard smoke test results widget design
- Regression detection logic

**Effort:** 2 hours

---

### P2-7: Model Versioning & Rollback Strategy
**Finding:** "Deterministic seeds" imply versioning; no version control scheme
**Current State:** Brief L1403 reproducibility; no versioning
**Impact:** Can't rollback failed strategies; audit trail missing

**Recommended Approach:**
1. Define version scheme: `{date}_{brief_id}_{epoch}` (e.g., `20260227_p1_001`)
2. Store metadata: backtest date, parameter set, Sharpe, MaxDD, P&L
3. Implement rollback: "Can revert to previous version via tag"
4. Add A/B testing: "Run v1 and v2 side-by-side for comparison"
5. Document: "Each version has frozen dataset hash"

**Deliverables:**
- Version numbering scheme defined
- Metadata schema for each version
- Rollback mechanism (tag-based)
- A/B testing infrastructure
- Version audit trail

**Effort:** 2 hours

---

## PRIORITY 3: NICE-TO-HAVE IMPROVEMENTS (After Phase 1 Ships)
**Target Completion:** Backlog | **Effort:** 8-10 hours

These 10 findings are important but won't block implementation if deferred.

### P3 Items (Summarized)
- P3-1: HNSW index performance benchmarking
- P3-2: Parameter explainability (SHAP/LIME integration)
- P3-3: Multi-account API contract (Phase 2 prep)
- P3-4: Calendar event validation process & update mechanism
- P3-5: Performance regression detection & alerts
- P3-6: Dashboard data freshness monitoring
- P3-7: Backtesting benchmark comparison & baseline
- P3-8: Walk-forward contamination guards & purging parameters
- P3-9: UX accessibility (WCAG level, a11y compliance)
- P3-10: Cost of capital assumption & risk-adjusted success criteria

---

## Summary Table: All 25 Findings & Recommendations

| ID | Severity | Priority | Title | Effort | Next Step |
|----|----------|----------|-------|--------|-----------|
| P1-1 | HIGH | 1 | HNSW Vector Index Ops | 4h | Spec document + config |
| P1-2 | HIGH | 1 | DFF Conditional Sampling | 5h | BNF grammar + tests |
| P1-3 | HIGH | 1 | MTF Signal Aggregation | 4h | Algorithm + test scenarios |
| P1-4 | HIGH | 1 | Kill-Switch Recovery | 4h | State machine + recovery flows |
| P1-5 | HIGH | 1 | Dashboard Trading Flows | 4h | UX mockups + test checklist |
| P1-6 | HIGH | 1 | Convergence Definition | 3h | Optuna config + validation |
| P2-1 | MEDIUM | 2 | Rocket Allocation Math | 4h | Monte Carlo simulation |
| P2-2 | MEDIUM | 2 | Cost Schedule | 3h | Fee matrix + validation |
| P2-3 | MEDIUM | 2 | Data Freshness SLA | 3h | Freshness spec + alerts |
| P2-4 | MEDIUM | 2 | Rebalancing Algorithm | 3h | Algorithm + cost budget |
| P2-5 | MEDIUM | 2 | Security Baseline | 2h | Assumptions + Phase 2 roadmap |
| P2-6 | MEDIUM | 2 | Smoke Test Definition | 2h | Pass/fail criteria + display |
| P2-7 | MEDIUM | 2 | Model Versioning | 2h | Version scheme + rollback |
| P3-1 | LOW | 3 | HNSW Benchmarking | 2h | Performance test suite |
| P3-2 | LOW | 3 | Parameter Explainability | 3h | SHAP/LIME integration |
| P3-3 | LOW | 3 | Multi-Account API Contract | 2h | API design |
| P3-4 | LOW | 3 | Calendar Event Validation | 2h | Process + update mechanism |
| P3-5 | LOW | 3 | Regression Detection | 2h | Alerting logic |
| P3-6 | LOW | 3 | Dashboard Freshness Monitor | 1h | Indicator widget |
| P3-7 | LOW | 3 | Benchmark Comparison | 2h | Baseline specification |
| P3-8 | LOW | 3 | Walk-Forward Contamination | 2h | Purging parameters |
| P3-9 | LOW | 3 | UX Accessibility | 3h | WCAG guidelines |
| P3-10 | LOW | 3 | Cost of Capital Assumption | 1h | Risk-adjusted thresholds |
| Finding-4 | MEDIUM | 2 | Portfolio Risk Mgmt | 2h | Rebalance frequency |
| Finding-21 | MEDIUM | 2 | Calendar Events | 1h | Event list + validation |
| **TOTAL** | - | - | **25 Findings** | **60-70h** | **See timeline below** |

---

## Implementation Timeline

### Week 1: Priority 1 (Critical Blockers)
**Goal:** Complete 6 critical specifications
- **Mon-Tue:** P1-1, P1-2 (HNSW + DFF specs)
- **Wed:** P1-3, P1-4 (MTF aggregation + kill-switch)
- **Thu-Fri:** P1-5, P1-6 (Dashboard flows + convergence definition)
- **Effort:** 16-20 hours (2-3h per spec)
- **Output:** 6 detailed specification documents ready for implementation

### Week 2: Priority 2 (High-Impact Fixes)
**Goal:** Complete 7 high-impact fixes
- **Mon-Tue:** P2-1, P2-2, P2-3 (Allocation math, costs, data freshness)
- **Wed-Thu:** P2-4, P2-5, P2-6 (Rebalancing, security, smoke test)
- **Fri:** P2-7 (Model versioning)
- **Effort:** 12-15 hours
- **Output:** 7 specifications + validation tests

### Week 3-4: Priority 3 (Backlog)
**Goal:** Optional improvements for backlog
- **As bandwidth allows:** P3-1 through P3-10
- **Effort:** 8-10 hours (spread across weeks)

---

## Success Criteria for Recommendations

### Definition of "Complete"
Each recommendation is complete when:
1. ✅ Specification document created (2-3 pages)
2. ✅ Examples/test cases provided
3. ✅ Acceptance criteria defined
4. ✅ Implementation guidance provided
5. ✅ GitHub issue created (with spec linked)

### Definition of "Ready for Implementation"
Phase 1 is ready for implementation when:
1. ✅ All P1 (6 critical blockers) are complete
2. ✅ All P2 (7 high-impact fixes) are complete
3. ✅ Sprint stories map to completed specs
4. ✅ Dev team has reviewed and approved specs
5. ✅ QA has test scenarios from specs

---

## Conclusion

**25 findings identified; 8 critical blockers; 60-70 hours to close all gaps.**

**Recommendation:** Complete Priority 1 (16-20h) before sprint planning. This will unblock implementation and reduce rework by an estimated 40-60%.

**Next Step:** Assign spec owners (2-3 hours each) and schedule 2-week hardening sprint before Phase 1 implementation sprint.

