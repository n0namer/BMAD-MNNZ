---
title: "Architecture Critical Decisions Resolution Plan"
date: "2026-02-27T01:50:00Z"
status: "READY_FOR_DECISION"
priority: "CRITICAL_PATH"
blocking_items: 5
effort_weeks: 2-3
timeline: "2026-02-27 to 2026-03-20"
phase: "Phase 1a"
implementation_blocker: true
---

# Architecture Critical Decisions Resolution Plan

**CRITICAL:** These 5 architecture decisions MUST be resolved before Phase 1 development can proceed with confidence. Without them:
- ❌ Signal validation framework unclear (which conditions to use?)
- ❌ Performance bounds unmeasured (what's acceptable DD recovery time?)
- ❌ Anti-overfitting strategy undefined (how to prevent system gaming?)
- ❌ Price action integration scope ambiguous (core feature or Phase 2?)
- ❌ AUX signal conditions not spec'd (where does feature X go?)

---

## Overview: 5 Critical Architecture Decisions

| Priority | Decision | Effort | Timeline | Blocker For |
|----------|----------|--------|----------|-------------|
| 1️⃣ | Signal Framework CORE Conditions | 3-5 days | 2026-02-28 to 2026-03-04 | Signal research + implementation |
| 2️⃣ | Anti-Overfitting Degradation Rules | 3-5 days | 2026-02-28 to 2026-03-04 | Rocket bucket research |
| 3️⃣ | Performance Validation Plan | 2-3 days | 2026-03-05 to 2026-03-07 | Benchmarking infrastructure |
| 4️⃣ | Signal AUX Conditions Framework | 2-3 days | 2026-03-08 to 2026-03-10 | Signal module architecture |
| 5️⃣ | Price Action Module Scope Decision | 1 day | 2026-03-11 | Phase 1 vs Phase 2 epics |

**Total Timeline:** 2-3 weeks (Feb 28 - Mar 20)
**Parallel with Zone 2:** Days 2-14 development can proceed, but final validation blocked until decisions made
**Integration Point:** Day 14 (Zone 2 end) - must have all decisions resolved for Phase 2 planning

---

## Decision 1: Signal Framework CORE Conditions (3-5 days)

### Problem Statement
**Current State**: We know signal types exist (MA, RSI, MACD, Bollinger, etc.) but lack:
- Which conditions are "CORE" vs "AUX"
- CORE thresholds (e.g., when does RSI overbought = SELL condition?)
- How many CORE conditions minimum for valid signal?
- What prevents signal misconfiguration (validation rules)?

### Key Questions to Answer

**Q1.1: What defines CORE vs AUX?**
- CORE: Always evaluated, directly affects entry/exit decisions
- AUX: Optional enhancements, modify signal confidence but not decision

**Proposed Answer:**
```
CORE Conditions (must evaluate):
  • Moving Average crossover (fast < slow = BUY when crossing)
  • RSI Extreme (RSI < 30 = BUY, RSI > 70 = SELL)
  • Trend confirmation (price > MA(200) = uptrend)

AUX Conditions (enhance but don't block):
  • Volume confirmation (volume > 20-day avg)
  • MACD histogram (positive = bullish confirmation)
  • Bollinger Band squeeze (entry on breakout)
```

**Q1.2: What are specific thresholds per condition?**

Example for RSI (CORE):
```
RSI(14) threshold matrix:
  Oversold (BUY signal):
    • Severe: RSI < 20 (high confidence entry, risk: false positive)
    • Moderate: RSI < 30 (balanced entry)
    • Mild: RSI < 40 (early signal, higher false positive)

  Overbought (SELL signal):
    • Severe: RSI > 80 (high confidence exit)
    • Moderate: RSI > 70 (balanced exit)
    • Mild: RSI > 60 (early exit, may miss gains)

Recommendation: Use Moderate threshold (RSI < 30 / > 70) for Phase 1
```

**Q1.3: Minimum CORE conditions for valid signal?**

Options:
- **Option A (Strict)**: All 3 CORE conditions must agree (high precision, low recall)
- **Option B (Moderate)**: 2 of 3 CORE conditions must agree (balanced)
- **Option C (Loose)**: Any 1 CORE condition triggers signal (high recall, low precision)

**Recommendation: Option B (2 of 3)** - balanced risk/reward, prevents false signals from single indicator

**Q1.4: Validation rules to prevent misconfiguration?**

```typescript
interface SignalValidation {
  rules: [
    { rule: "at_least_2_core_conditions", error: "Need minimum 2 core conditions" },
    { rule: "rsi_threshold_30_70", error: "RSI threshold must be 30±5 for oversold, 70±5 for overbought" },
    { rule: "ma_periods_valid", error: "MA fast < MA slow (e.g., 9 < 20)" },
    { rule: "no_contradictions", error: "Cannot have RSI overbought AND price below MA200" }
  ];

  warn_if: [
    { condition: "only_1_core", message: "Only 1 core condition - consider adding another for robustness" },
    { condition: "all_aux_no_core", message: "Only AUX conditions - add at least 2 core conditions" }
  ];
}
```

### Deliverable Format

**Document: SIGNAL-FRAMEWORK-CORE-CONDITIONS-V1.md**

```markdown
# Signal Framework CORE Conditions Specification (v1.0)

## 1. CORE Conditions Definition
- Moving Average Crossover (fast < slow = trend start)
- RSI Extreme (RSI < 30 / > 70 = momentum extreme)
- Trend Confirmation (price > MA(200) = uptrend, < MA(200) = downtrend)

## 2. Threshold Matrix (per condition)
### RSI (CORE)
- Oversold (BUY): RSI(14) < 30 (recommended: 28-32 range)
- Overbought (SELL): RSI(14) > 70 (recommended: 68-72 range)
- Lookback: 14 periods (standard)

### MA Crossover (CORE)
- Fast MA: EMA(9) or SMA(9)
- Slow MA: EMA(20) or SMA(20)
- Signal: BUY when fast > slow, SELL when fast < slow
- Confirmation: Price must close above fast MA (no reversal within 1 bar)

### Trend (CORE)
- Uptrend: Close > MA(200)
- Downtrend: Close < MA(200)
- Purpose: Filter signals against major trend (avoid counter-trend trades)

## 3. Minimum Conditions Rule
- Minimum 2 of 3 CORE conditions must agree for valid signal
- Prevents false signals from single indicator
- Example: RSI oversold + MA crossover = BUY (MA trend can be any direction)

## 4. Validation Rules (Implemented in Signal Validator)
- [ ] At least 2 CORE conditions configured
- [ ] RSI threshold in range [25-35] for oversold, [65-75] for overbought
- [ ] MA fast < MA slow (e.g., 9 < 20)
- [ ] No contradictions (e.g., can't require RSI overbought AND price > MA200 uptrend)
- [ ] Warn if only 1 CORE condition used
- [ ] Warn if no CORE conditions configured (only AUX)

## 5. AUX Conditions (Enhance signal confidence, don't block)
- Volume confirmation: Volume > 20-day MA
- MACD histogram: Positive histogram = bullish
- Bollinger Band squeeze: Entry on band breakout
- Others as strategy-specific enhancements

## 6. Implementation Examples

### Example 1: Conservative Signal
```
CORE:
  ✓ RSI(14) < 30 (Oversold)
  ✓ EMA(9) > EMA(20) (Fast > Slow)
  ? Price > MA(200) (Uptrend - not required)

AUX:
  ✓ Volume > 20-day MA (Confirm)

Validation: ✅ PASS (2 CORE conditions met)
Signal: BUY when all triggered
```

### Example 2: Aggressive Signal
```
CORE:
  ✓ RSI(14) < 30 (Oversold)
  ? EMA(9) > EMA(20) (Not configured)
  ? Price > MA(200) (Not configured)

AUX:
  ✓ Volume > 20-day MA
  ✓ MACD histogram positive

Validation: ⚠️ WARN (only 1 CORE condition)
Signal: May fire too frequently, consider adding 2nd CORE condition
```

## 7. Performance Impact
- Each CORE condition evaluation: <5ms (vectorized)
- Total signal evaluation: <15ms per bar (3 CORE + 3 AUX)
- Memory: ~2KB per signal configuration
- Scalability: 100+ signals evaluable in parallel

## 8. Phase 1 Implementation Status
- [x] CORE conditions defined
- [x] Threshold matrix finalized
- [ ] Signal validator implemented (code)
- [ ] Unit tests (code)
- [ ] Integration with signal broker (code)

Target: Ready for code implementation by Day 5
```

### Decision Timeline

| Date | Action | Owner | Deliverable |
|------|--------|-------|-------------|
| Feb 28 | Identify which indicators are CORE | Architect | Initial list (3-4 indicators) |
| Mar 1 | Define thresholds for each CORE | Analyst + Researcher | Threshold matrix |
| Mar 2 | Validate thresholds against historical data | Performance Engineer | Performance report |
| Mar 3 | Finalize validation rules (contradictions, warnings) | Architect | Validation rule spec |
| Mar 4 | **DECISION GATE: Approve v1.0** | Leadership | Sign-off on SIGNAL-FRAMEWORK-CORE-CONDITIONS-V1.md |

### Success Criteria
✅ All 5 CORE conditions (or agreed alternative) have specific thresholds
✅ "Minimum 2 of 3" rule decided (or alternative minimum defined)
✅ Validation rules prevent misconfiguration
✅ Performance impact acceptable (<15ms per signal)
✅ Architect + leadership agree on approach

---

## Decision 2: Anti-Overfitting Degradation Rules (3-5 days)

### Problem Statement
**Current State**: Rocket bucket optimizes parameters (K, lookback, leverage) but:
- What prevents system from overfitting to historical data?
- How to detect when model is "too optimized"?
- What happens if parameters degrade in live trading (e.g., K=0.6 works in backtest but fails live)?

### Key Questions to Answer

**Q2.1: What is the anti-overfitting metric?**

Options:
- **Walk-Forward Analysis**: Split data into train (60%) + test (40%), measure degradation from train→test
- **Sharpe Ratio Stability**: Monitor if Sharpe ratio changes >20% between train/test
- **Max Drawdown Buffer**: Require historical MaxDD < 30% as headroom for live trading (expecting >40% possible)
- **Parameter Stability**: Require optimal parameters to be stable (e.g., K value consistent across different market regimes)

**Recommendation: Walk-Forward Analysis + Sharpe Ratio Stability**
```
Anti-Overfitting Rule:
  IF (Sharpe_train - Sharpe_test) / Sharpe_train > 20%
    THEN system_degraded = true
    AND flag_for_review = true
    AND recommendation = "Parameters may be overfit, consider simplifying model"
```

**Q2.2: What's the degradation acceptance threshold?**

Example matrix:
```
Sharpe Train vs Test Degradation:
  • 0-10%: ✅ Excellent (model generalizes well)
  • 10-20%: ✅ Good (acceptable degradation)
  • 20-30%: ⚠️ Caution (potential overfit, review parameters)
  • 30-50%: 🔴 Flag for review (likely overfit)
  • >50%: ❌ Reject (severe overfit, reoptimize)
```

**Recommendation: Accept up to 20% degradation, warn 20-30%, reject >30%**

**Q2.3: How to detect overfitting in live trading?**

Monitoring rules:
```typescript
interface OverfitDetection {
  metrics: {
    live_sharpe: number;
    backtest_sharpe: number;
    degradation: number; // (backtest - live) / backtest

    live_win_rate: number;
    backtest_win_rate: number;
    win_rate_degradation: number;

    live_max_dd: number;
    backtest_max_dd: number;
    // Note: Live MaxDD EXPECTED to be worse (no look-ahead bias)
  };

  alerts: [
    { condition: "degradation > 30%", severity: "CRITICAL", action: "Pause trading, reoptimize" },
    { condition: "win_rate_degradation > 25%", severity: "HIGH", action: "Reduce position size" },
    { condition: "live_max_dd > backtest_max_dd * 1.5", severity: "INFO", action: "Monitor closely" }
  ];
}
```

**Q2.4: What parameter stabilization rules?**

Stability check:
```
Regime 1: Bear market (2020-2021)
  Optimal K = 0.62, lookback = 14

Regime 2: Bull market (2021-2022)
  Optimal K = 0.58, lookback = 12

Regime 3: Sideways (2022-2023)
  Optimal K = 0.60, lookback = 15

Parameter Stability Score:
  • K variation: std([0.62, 0.58, 0.60]) = 0.02 (2% variation) ✅ Stable
  • Lookback variation: std([14, 12, 15]) = 1.4 periods ✅ Stable

Recommendation: Use average parameters (K=0.60, lookback=14)
            Or: Use regime-adaptive parameters (select by current market condition)
```

### Deliverable Format

**Document: ANTI-OVERFITTING-DEGRADATION-RULES-V1.md**

```markdown
# Anti-Overfitting Degradation Rules Specification (v1.0)

## 1. Overfitting Definition
System is overfit if trained parameters fail to generalize to unseen data (walk-forward test set).

## 2. Metrics for Overfitting Detection

### Primary Metric: Sharpe Ratio Degradation
```
sharpe_degradation = (sharpe_train - sharpe_test) / sharpe_train * 100%

Thresholds:
  • 0-10%: ✅ Excellent
  • 10-20%: ✅ Good (accept)
  • 20-30%: ⚠️ Caution (review)
  • 30-50%: 🔴 High risk (flag for reoptimization)
  • >50%: ❌ Reject (severe overfit)

Action:
  IF degradation > 30%:
    THEN recommend_reoptimization()
    AND reduce_position_size()
    AND increase_monitoring_frequency()
```

### Secondary Metric: Win Rate Stability
```
win_rate_degradation = (win_rate_train - win_rate_test) / win_rate_train * 100%

Threshold:
  • Degradation > 25%: Monitor closely, reduce position size
  • Degradation > 40%: Flag for review
```

### Tertiary Metric: MaxDD Divergence (Live vs Backtest)
```
max_dd_divergence = (live_max_dd - backtest_max_dd) / abs(backtest_max_dd)

Expected:
  • Live MaxDD WORSE than backtest (no look-ahead bias)
  • Acceptable divergence: <50% worse (e.g., backtest -30% → live -45%)

Threshold:
  • Divergence > 100%: Critical, pause trading
  • Divergence 50-100%: High alert, reduce leverage
  • Divergence 0-50%: Normal, monitor
```

## 3. Walk-Forward Analysis Setup

```
Training Data: 60% of historical
Test Data: 40% of historical
Granularity: 6-month rolling windows

For each window:
  1. Optimize parameters on training 60%
  2. Evaluate on test 40%
  3. Record sharpe_train, sharpe_test
  4. Calculate degradation
  5. If degradation acceptable: use parameters
     Else: flag for review or simplify model

Result: Array of [sharpe_train, sharpe_test] pairs
        showing degradation across time periods
```

## 4. Parameter Stability Rules

```
IF std(optimal_K_across_regimes) > 0.05 (5% variation):
  THEN parameters unstable
  AND recommendation = "Use simpler model or regime-adaptive approach"

IF std(optimal_lookback_across_regimes) > 2 (2 period variation):
  THEN lookback unstable
  AND recommendation = "Fix lookback to most stable value"
```

## 5. Live Trading Overfitting Detection

Monitor live vs. backtest metrics continuously:

```python
daily_check():
  sharpe_live = calculate_sharpe(live_pnl, lookback=252)
  sharpe_backtest = historical_sharpe_value
  degradation = (sharpe_backtest - sharpe_live) / sharpe_backtest

  IF degradation > 0.30:
    alert(CRITICAL, "Live trading degraded >30%, potential overfit")
    action: pause_trading() or reduce_position_size(0.5)

  IF live_max_dd > backtest_max_dd * 1.5:
    alert(HIGH, "Live MaxDD 50% worse than backtest")
    action: reduce_leverage(0.75)

  IF win_rate_live < win_rate_backtest * 0.75:
    alert(MEDIUM, "Win rate degradation >25%")
    action: increase_monitoring()
```

## 6. Reoptimization Trigger

```
Reoptimize IF:
  • Degradation > 30% (parameters failed to generalize)
  • Market regime changed significantly (new bull/bear cycle)
  • Strategy performance degraded >25% in live trading
  • New data accumulated (>3 months of new history)

Reoptimization Process:
  1. Gather data (last 2 years or last major regime)
  2. Walk-forward analysis (6-month rolling windows)
  3. Find parameters with <20% degradation
  4. If found: deploy new parameters
  5. If not found: simplify model (fewer parameters) or archive strategy
```

## 7. Phase 1 Implementation
- [x] Walk-forward analysis methodology defined
- [x] Sharpe degradation threshold set (20-30% warning, >30% reject)
- [x] Live monitoring rules specified
- [ ] Walk-forward backtest code (implementation)
- [ ] Live monitoring dashboard (implementation)
- [ ] Reoptimization automation (implementation)

Target: Ready for implementation by Day 5
```

### Decision Timeline

| Date | Action | Owner | Deliverable |
|------|--------|-------|-------------|
| Feb 28 | Define what "overfit" means for Rocket | Architect | Definition + metrics |
| Mar 1 | Design walk-forward analysis methodology | Performance Engineer | Walk-forward spec |
| Mar 2 | Run walk-forward on historical Rocket data | Researcher | Sample degradation report |
| Mar 3 | Determine acceptance thresholds (% degradation OK?) | Leadership + Analyst | Threshold approval |
| Mar 4 | **DECISION GATE: Approve v1.0** | Leadership | Sign-off on ANTI-OVERFITTING-DEGRADATION-RULES-V1.md |

### Success Criteria
✅ Walk-forward analysis methodology clear
✅ Sharpe ratio degradation <20% for production parameters
✅ Live monitoring dashboard spec'd
✅ Reoptimization trigger conditions defined
✅ Architect + leadership approve approach

---

## Decision 3: Performance Validation Plan (2-3 days)

### Problem Statement
**Current State**: We measure Sharpe ratio and MaxDD, but lack:
- Acceptable performance bounds (what Sharpe is "good enough"?)
- Acceptable latency bounds (when is signal too slow?)
- Acceptable slippage bounds (how much slippage before strategy breaks?)
- How to validate before go-live (backtest minimum confidence?)

### Key Questions to Answer

**Q3.1: What Sharpe ratio target for Phase 1?**

```
Sharpe Ratio Targets:
  • Sharpe > 2.0: Excellent (>90% annual return with moderate volatility)
  • Sharpe 1.5-2.0: Good (profitable with managed risk)
  • Sharpe 1.0-1.5: Acceptable (profitable but higher volatility)
  • Sharpe < 1.0: Unacceptable (too much volatility per unit return)

Phase 1 Target: Sharpe > 1.0 (minimum acceptable)
               Sharpe > 1.5 (preferred target)

Note: Rocket historical ~1.8-2.2 Sharpe, so 1.5+ is realistic
```

**Q3.2: What latency bounds?**

```
Signal latency SLA:
  • Ideal: <100ms (signal generated to order submitted)
  • Acceptable: 100-500ms
  • Caution: 500ms-1s
  • Unacceptable: >1s (slippage too high)

Validation:
  [ ] Measure signal latency in sandbox (paper trading)
  [ ] Ensure <500ms for 99th percentile
  [ ] If higher: optimize bottleneck (signal calc, broker API, network)
```

**Q3.3: What slippage assumptions?**

```
Slippage Models:
  • Limit order assumption: 0 slippage (price exactly filled)
  • Market order assumption: 1-3 bps slippage (typical for liquid pairs)
  • Stress scenario: 10 bps slippage (volatile market)

Validation:
  [ ] Backtest with 2 bps slippage assumption (realistic)
  [ ] If strategy still Sharpe > 1.5: ✅ Robust
  [ ] If Sharpe < 1.0 with 2 bps: ⚠️ Too fragile, simplify strategy
```

**Q3.4: Backtest confidence requirements?**

```
Pre-launch Validation:
  1. Walk-forward analysis: <20% Sharpe degradation ✓
  2. Out-of-sample performance: >1.0 Sharpe
  3. Stress test: Sharpe > 1.0 with 10 bps slippage
  4. Regime performance: Positive return in 3/3 market regimes
  5. Maximum correlation: <0.3 correlation to benchmark (unique strategy)
  6. Drawdown recovery: Recover to new high within 6 months average

Pass all 6 → Ready for live deployment
Fail any 1 → Adjust parameters or defer to Phase 2
```

### Deliverable Format

**Document: PERFORMANCE-VALIDATION-PLAN-V1.md**

```markdown
# Performance Validation Plan Specification (v1.0)

## 1. Performance Targets

### Sharpe Ratio
- Target: > 1.5 (preferred)
- Minimum acceptable: > 1.0
- Below 1.0: Do not deploy

### Maximum Drawdown
- Target: < 30% (seasonal headroom before kill-switch at 40%)
- Maximum acceptable: < 40%
- Above 40%: Triggers kill-switch, trading halted

### Win Rate
- Target: > 55% (more winners than losers)
- Acceptable: 45-55% (higher average win size compensates)
- Below 45%: Strategy logic questionable, review

### Return Metrics
- Annual Return: > 10% (modest baseline in low-volatility environment)
- Risk-adjusted Return (Sharpe): > 1.5
- Information Ratio (vs benchmark): > 0.5

## 2. Latency Validation

### Signal Latency Budget
```
Signal generation:    <50ms  (calculate conditions)
Order submission:     <100ms (place order)
Network round-trip:   <50ms  (broker acknowledgment)
---
Total P99 latency:    <200ms (target)
Acceptable max:       <500ms
```

### Measurement
- [ ] Instrument signal pipeline with timing
- [ ] Log latency for every signal in sandbox
- [ ] Calculate P50, P99 latency
- [ ] Monitor during live paper trading
- [ ] Alert if P99 > 500ms (indicates performance issue)

## 3. Slippage Assumptions

### Conservative Model (Use for Validation)
- Limit orders: 0 bps slippage (no execution risk)
- Market orders: 2 bps slippage (typical for liquid pairs)
- Stress scenario: 10 bps slippage (volatile market/large order)

### Validation Step
- Backtest with 2 bps slippage
- If Sharpe > 1.5 with slippage: ✅ Strategy robust
- If Sharpe < 1.0 with slippage: ⚠️ Adjust parameters

## 4. Pre-Launch Validation Checklist

### [ ] 1. Walk-Forward Analysis
- Run 6-month rolling windows
- Verify Sharpe degradation < 20%
- If passed: Proceed to next check

### [ ] 2. Out-of-Sample Performance
- Test on final 20% of data (held out from training)
- Verify Sharpe > 1.0
- Verify Win Rate > 40%
- If passed: Proceed

### [ ] 3. Stress Testing
- Apply 10 bps slippage
- Verify Sharpe still > 1.0
- Verify MaxDD < 50%
- If passed: Proceed

### [ ] 4. Regime Performance
- Bull market 2021-2022: Positive return ✓
- Bear market 2022-2023: Positive return or limited loss ✓
- Sideways market 2020-2021: Positive return ✓
- If all 3 regimes: Proceed

### [ ] 5. Correlation Test
- Measure correlation to benchmark (BTC/ETH/SPY)
- Verify correlation < 0.3 (unique strategy)
- If passed: Proceed

### [ ] 6. Recovery Speed
- Calculate average time to recover from drawdown
- Verify recovers within 6 months average
- If passed: Ready to deploy

**Result: All 6 checks must PASS before live deployment**

## 5. Go-Live Validation Report

Document required pre-launch:

```yaml
Go-Live Validation Report:
  Date: 2026-03-15
  Strategy: Rocket

  Walk-Forward:
    avg_sharpe_train: 1.85
    avg_sharpe_test: 1.68
    degradation: 9.2%  ✅ PASS (< 20%)

  Out-of-Sample:
    sharpe: 1.52  ✅ PASS (> 1.0)
    win_rate: 58%  ✅ PASS (> 40%)

  Stress Test:
    sharpe_with_10bps: 1.21  ✅ PASS (> 1.0)
    max_dd_with_10bps: 34%  ✅ PASS (< 50%)

  Regime Performance:
    bull_market: +22% annual  ✅ PASS
    bear_market: -5% loss  ✅ PASS (limited)
    sideways_market: +8% annual  ✅ PASS

  Correlation Test:
    correlation_to_btc: 0.18  ✅ PASS (< 0.3)

  Recovery Speed:
    avg_recovery_days: 127  ✅ PASS (< 180)

  Overall Result: ✅ APPROVED FOR PRODUCTION
```

## 6. Post-Launch Monitoring

Monitor live deployment:

```
Daily:
  [ ] Check Sharpe ratio (rolling 30-day)
  [ ] Check MaxDD (rolling)
  [ ] Check win rate
  [ ] Check latency P99

Weekly:
  [ ] Compare live vs backtest Sharpe
  [ ] Monitor correlation to market
  [ ] Check for regime change

Monthly:
  [ ] Full performance report
  [ ] Walk-forward revalidation (if data >3 months new)
  [ ] User feedback on strategy
```

## 7. Phase 1 Implementation
- [x] Performance targets defined
- [x] Validation checklist created
- [ ] Walk-forward analysis code (implementation)
- [ ] Performance monitoring dashboard (implementation)
- [ ] Go-live validation report automation (implementation)

Target: Ready for implementation by Day 5
```

### Decision Timeline

| Date | Action | Owner | Deliverable |
|------|--------|-------|-------------|
| Mar 5 | Run walk-forward on historical Rocket | Performance Engineer | Walk-forward report |
| Mar 6 | Run stress test (2 bps, 10 bps slippage) | Performance Engineer | Stress test report |
| Mar 7 | **DECISION GATE: Approve v1.0** | Leadership | Sign-off on PERFORMANCE-VALIDATION-PLAN-V1.md |

### Success Criteria
✅ Sharpe > 1.5 in out-of-sample testing
✅ All 6 pre-launch checks defined
✅ Go-live validation report template ready
✅ Post-launch monitoring defined
✅ Leadership approves performance targets

---

## Decision 4: Signal AUX Conditions Framework (2-3 days)

### Problem Statement
**Current State**: CORE conditions defined, but:
- AUX conditions not categorized (how to organize optional enhancements?)
- No framework for adding new AUX conditions
- No priority/weighting for AUX conditions (how to combine multiple AUX?)

### Key Questions to Answer

**Q4.1: What are AUX condition categories?**

Proposed framework:
```
AUX Categories:
  1. Volume Confirmation
     ├─ Volume > 20-day MA (most common)
     ├─ Volume > 50-day MA (stricter)
     └─ Volume spike > 150% of average

  2. Momentum Confirmation
     ├─ MACD histogram positive
     ├─ Stochastic overbought/oversold
     └─ ROC (Rate of Change) positive

  3. Volatility Filters
     ├─ Bollinger Band position (above/below)
     ├─ ATR expansion (volatility low enough for trade)
     └─ Keltner Channel squeeze detection

  4. Trend Filters (already in CORE, but can enhance)
     ├─ ADX > 25 (strong trend)
     ├─ Supertrend breakout
     └─ Ichimoku cloud position

  5. Support/Resistance
     ├─ Price bouncing off known support
     ├─ Fibonacci level proximity
     └─ Previous day high/low
```

**Q4.2: How to weight/combine AUX conditions?**

Options:
- **Simple OR**: Any AUX condition triggered = increase confidence slightly
- **Voting**: Count AUX conditions triggered, increase confidence per count
- **Weighted**: Assign weights per AUX condition (volume = 30%, MACD = 20%, etc)

**Recommendation: Weighted voting**
```
AUX Confidence Calculation:
  confidence = sum(weight_i * triggered_i) for all AUX conditions

  Example weights:
    Volume confirmation: 40% (most reliable)
    MACD histogram: 25% (momentum confirmation)
    Bollinger Band: 20% (volatility confirmation)
    Trend filter: 15% (already covered by CORE)

  Result: confidence in 0-100% range

  Signal execution:
    IF core_signal_valid AND confidence > 50%:
      EXECUTE_TRADE()
    ELIF core_signal_valid AND confidence 25-50%:
      REDUCE_POSITION_SIZE(0.5)
    ELIF core_signal_valid AND confidence < 25%:
      SKIP_TRADE()
```

**Q4.3: How to add new AUX conditions in future?**

Framework for extensibility:
```typescript
interface AUXCondition {
  id: string; // "aux_volume_ma20"
  category: "volume" | "momentum" | "volatility" | "trend" | "support";
  weight: number; // 0-100, total should not exceed 100
  description: string;
  calculation: (bar: OHLCV, history: OHLCV[]) => boolean;
  enabled: boolean;
}

// Adding new AUX condition (Phase 2 example):
const new_aux = AUXCondition(
  id: "aux_renko_breakout",
  category: "volatility",
  weight: 15,
  description: "Price breaks above Renko brick high",
  calculation: (bar, history) => {
    return bar.close > calculate_renko_high(history);
  },
  enabled: true
);

// System validates:
// 1. Total weight <= 100%
// 2. Calculation returns boolean
// 3. No duplicate IDs
// 4. Category is valid
// Then AUX condition is available for signal configuration
```

### Deliverable Format

**Document: SIGNAL-AUX-CONDITIONS-FRAMEWORK-V1.md** (shorter, framework-focused)

### Decision Timeline

| Date | Action | Owner | Deliverable |
|------|--------|-------|-------------|
| Mar 8 | Define AUX categories | Architect | Category list |
| Mar 9 | Design weighted voting system | Engineer | Weighting spec + code template |
| Mar 10 | **DECISION GATE: Approve v1.0** | Leadership | Sign-off on framework |

### Success Criteria
✅ AUX categories defined (5+ categories)
✅ Weighted voting system clear
✅ Extension framework documented
✅ Usable by engineers for Phase 2

---

## Decision 5: Price Action Module Scope Decision (1 day)

### Problem Statement
**Current State**: Is Price Action a Phase 1 feature or Phase 2?
- Expected effort: 40-60 hours (medium complexity)
- Value: Medium (useful but not foundational)
- Risk: High (new signal type, less tested)

### Key Questions to Answer

**Q5.1: What does "Price Action Module" include?**

Scope options:
- **Option A (Minimal)**: Basic support/resistance detection + breakout signals (~20 hours)
- **Option B (Standard)**: Support/resistance + chart pattern recognition (pin bars, engulfing) (~40 hours)
- **Option C (Advanced)**: Market profile, volume profile, smart money accumulation analysis (~60+ hours)

**Q5.2: How does it integrate with Signal Framework?**

```
IF include_in_phase1:
  → Price Action = new AUX condition category
  → Breakout signal: additional trigger for CORE signal entry
  → Recovery time: uses price action patterns

IF defer_to_phase2:
  → Keep support/resistance as manual indicator
  → Add price action signals in Phase 2 research
  → Use Rocket (momentum-based) as primary in Phase 1
```

**Q5.3: Go/No-go decision?**

Recommendation factors:
- ✅ Fits framework as AUX condition category
- ❌ Requires new pattern recognition algorithm
- ❌ Limited historical validation (new strategy type)
- ⚠️ Phase 1 timeline already tight (Zone 2: 2 weeks)

**Recommendation: DEFER to Phase 2** (post-launch enhancement)

### Deliverable Format

**Simple Decision Document: PRICE-ACTION-SCOPE-DECISION-V1.md**

```markdown
# Price Action Module Scope Decision (v1.0)

## Decision
**Defer Price Action signal module to Phase 2 (post-launch enhancement)**

## Rationale
1. **Timeline**: Phase 1 deadline tight (2 weeks remaining)
2. **Validation**: Limited historical backtest data for price action patterns
3. **Complexity**: Pattern recognition algorithm requires new research
4. **Architecture Ready**: Framework supports adding as AUX condition in Phase 2

## What's in Phase 1
- Rocket (momentum-based) signal system ✅
- Support/resistance levels (display only, not signals) ✅
- Price action as manual indicator (traders read patterns manually) ✅

## What's in Phase 2 (Planned)
- Automated price action signal generation (40-60 hours)
- Integration as AUX condition category
- Backtesting framework for pattern-based signals
- User-configurable pattern rules

## Timeline Impact
- Phase 1 unaffected (keep current scope)
- Phase 2 +2 weeks (add price action module)
- Go-live date: Unchanged (2026-03-25)
- Phase 2 start: 2026-03-25

## Approval
- [ ] Product: Agree to defer
- [ ] Engineering: Confirm resource impact
- [ ] Trading: OK with momentum-based Phase 1
- **Decision Made**: 2026-03-11 (deferred to Phase 2)
```

### Decision Timeline

| Date | Action | Owner | Decision |
|------|--------|-------|----------|
| Mar 11 | Evaluate effort/timeline impact | Architect + PM | Go/No-go assessment |
| Mar 11 | **DECISION: Defer to Phase 2** | Leadership | Update epics + timeline |

### Success Criteria
✅ Clear: Phase 1 uses Rocket momentum-based signals
✅ Clear: Phase 2 will add price action signals
✅ Epics updated to reflect Phase 2 scope
✅ Phase 2 roadmap includes price action research

---

## Summary: 5 Decisions Timeline

```
Week 1 (Feb 28 - Mar 4):
  ├─ MON 28: Signal CORE conditions decision ✓
  ├─ MON 28: Anti-overfitting degradation decision ✓
  ├─ WED 3: Final approval on both
  └─ THU 4: Code can begin (S-SIGNAL-001, S-ROCKET-001)

Week 2 (Mar 5 - Mar 11):
  ├─ MON 5: Performance validation plan decision ✓
  ├─ WED 7: Final approval + go-live criteria
  ├─ THU 8: Signal AUX framework decision ✓
  ├─ FRI 10: Final approval on framework
  └─ FRI 11: Price action scope decision + Phase 2 planning

Week 3 (Mar 12 - Mar 20):
  └─ Code implementation with clear architecture
```

**Total timeline: 2-3 weeks (Feb 28 - Mar 20)**
**Parallel with Zone 2: Days 2-14 code development unblocked, final validation gated on decisions**
**Integration point: Day 14 (Zone 2 end) → All decisions resolved → Ready for Phase 2 planning**

---

## Next Steps (Immediate)

1. **Review this plan** → Add any missing questions
2. **Schedule decision meetings** → 30-min each for Qs 1-5
3. **Assign research** → Performance engineer runs walk-forward analysis (Days 1-2)
4. **Continue Zone 2** → Code development proceeds in parallel (Days 2-14)
5. **Integration** → By Day 7 checkpoint, have answers to Q1-Q2

These 5 decisions unlock the full Phase 1 implementation path.

---

**READY FOR EXECUTION**
Document created: 2026-02-27 01:50:00Z
Status: READY_FOR_DECISION_MEETINGS
Next action: Schedule 5 decision meetings (Q1-Q5), start research on Day 1

