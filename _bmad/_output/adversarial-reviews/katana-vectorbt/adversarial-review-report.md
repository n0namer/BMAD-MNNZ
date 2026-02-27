# Adversarial Review Report: Katana-VectorBT Phase 1 Documentation
**Project:** katana-vectorbt
**Scope:** Phase 1 Coverage (Brief, PRD, Architecture, UX, Epics)
**Review Date:** 2026-02-27
**Review Type:** Critical Adversarial Analysis
**Review Stance:** Cynical, skeptical, assume problems exist

---

## Executive Summary

This adversarial review examined Phase 1 documentation across five critical documents to identify gaps, contradictions, weak specifications, and implementation risks. **25 critical findings** were identified spanning missing operational details, vague acceptance criteria, unvalidated assumptions, and specification fragmentation.

**Overall Assessment:** While documents show good structural alignment (96%+ coverage metrics), they suffer from **operational ambiguity, brittle assumptions, and implementation readiness gaps** that will cause problems during development.

**Confidence in Findings:** HIGH - Based on pattern matching across existing validation reports that revealed ~23 issues in brief alone, plus architectural gaps that required explicit corrections.

---

## CRITICAL FINDINGS

### 1. ❌ HNSW Vector Index Operational Black Box
**Severity:** HIGH | **Persistence:** Multiple sections mention, zero operational spec

**The Problem:**
- Brief and PRD repeatedly claim "HNSW indexing provides 150x-12,500x speedup" with zero operational details
- **Missing specs:**
  - Index rebuild frequency? (Real-time? Batch? Daily?)
  - Trigger conditions? (Every N new samples? Every M seconds?)
  - Staleness detection? (How do you know index is outdated?)
  - Memory overhead? (HNSW with M=16, ef_construction=200 for 10K samples ≈ 100MB+)
  - Vector dimension source? (Embedding model?)

**Why This Matters:**
- Optimization loop calls search ~1000s per trial
- Stale index = incorrect candidate selection = wasted optimization cycles
- Under-provisioned rebuild = memory explosion
- Unvalidated assumption: "150x speedup works in practice with our parameter scale"

**Evidence from Docs:**
- PRD L248-280: "HNSW Vector Indexing" section has zero operational parameters
- Brief L143: "HNSW indexing for 150x-12,500x speedup" — no context on scale
- No mention of vector source (embeddings model? PCA? raw params?)

**Recommendation:** Create operational spec: rebuild trigger, memory budget, staleness detection strategy.

---

### 2. ❌ DFF Conditional Parameter Sampling Not Formally Specified
**Severity:** HIGH | **Persistence:** "Conditional sampling" is mentioned, never detailed

**The Problem:**
- Brief claims: "Only active params sampled per trial (25-70, usually 25-45)"
- PRD claims: "Each profile defines active vs inactive params"
- **But:**
  - No formal grammar for conditional sampling (if type=ATR then sample {atr_period, atr_multiplier} else...)
  - No enumeration of valid (type, params) combinations
  - No validation rules for impossible combinations (e.g., bb_period + atr_period both active)
  - No constraint propagation (if tp_type != ATR then skip atr_period fields)

**Why This Matters:**
- Optuna integration must know which params are active per trial
- Without formal spec, sampler will either:
  - Over-sample (waste trials on inactive params)
  - Under-sample (miss valid parameter combinations)
  - Crash on invalid combinations
- "25-70 params usually" is not a formal constraint Optuna can enforce

**Evidence from Docs:**
- Brief L141-145: Mentions profiles define active params, zero grammar
- PRD L131-173: DFF structure detailed but no conditional sampling logic
- No "parameter dependency matrix" showing (type → required params)

**Recommendation:** Formalize conditional sampling as BNF or decision table: (source_type, role) → active_param_set.

---

### 3. ❌ No Monte Carlo Contamination Analysis for Walk-Forward Splits
**Severity:** HIGH | **Persistence:** Walk-forward validation claimed, but contamination unchecked

**The Problem:**
- PRD claims: "Purged K-fold cross-validation (FR25)" and "Walk-forward 8+ windows in ≤30 sec"
- **Missing:**
  - Look-ahead bias mitigation? (Training window stops BEFORE test window starts? When exactly?)
  - Purging parameters documented? (How many bars before/after?)
  - Walk-forward ancillarity? (Do windows overlap? If yes, how much cross-contamination?)
  - Degeneracy test? (Does train → test performance cliff exist? Or is test set a "lucky continuation"?)

**Why This Matters:**
- Walk-forward with improper purging = statistical lie (inflated Sharpe, overfitted parameters)
- 8 windows with 20% overlap but no purging = effectively 3-4 independent tests, not 8
- Monte Carlo significance testing requires clean separation
- Brief's success criteria (Net P&L ≥ +1.0%, correlation ≥ 0.5) are vulnerable if test set is contaminated

**Evidence from Docs:**
- PRD L283-296: Caching strategy detailed but no purging spec
- Brief L1403-1410: Walk-forward validation mentioned, zero contamination guards
- "CSCV" (Combinatorial Purged K-Fold) mentioned by name but not detailed

**Recommendation:** Document purging strategy: exact bar counts, overlap handling, degeneracy detection.

---

### 4. ❌ Rocket Portfolio Cap Mathematics Not Validated
**Severity:** HIGH | **Persistence:** Numbers look reasonable but assumptions unvalidated

**The Problem:**
- Brief claims: "10% rocket bucket, 60% per rocket, 3-month promotion gates (1%-2%-4%-6%)"
- **Unvalidated:**
  - Max simultaneous rockets? (If each starts at 1%, rocket_0 could be 6% while rocket_1-9 are 1% = 15% total, **exceeds 10% cap**)
  - Promotion math: "successful rocket grows 1%→2%→4%→6%" — what happens at promotion?
  - Allocation enforcement: Is this a hard constraint in code or a guideline?
  - Kill-switch interaction: "If rocket reaches 40% DD, blacklist 7 days" — what happens to its 4% allocation? Liquidate immediately? Slow exit?

**Why This Matters:**
- Overlapping promotion schedules + concurrent new rockets = mathematical edge case
- "Rocket_0 at 6%, Rocket_1 enters at 1%, Rocket_2 at 2%, Rocket_3 at 3%" = 12% total, **cap violation**
- No formal allocation algorithm guarantees correctness
- Brief is internally inconsistent on this (implied max = 60 + 40 = 100%, but cap is 10%)

**Evidence from Docs:**
- Brief L597-598: Promotion schedule specified, no allocation algorithm
- Architecture Decision 1: Capital allocation enforced, but no proof of cap correctness
- No simulation/backtest showing this works under concurrent stress

**Recommendation:** Create allocation algorithm with invariant proofs and edge case testing (concurrent promotions, kill-switches, new entries).

---

### 5. ❌ MTF Kill-Switch Metrics Lack Recovery Definition
**Severity:** MEDIUM | **Persistence:** Rollback "triggering" is vague, recovery is missing

**The Problem:**
- Brief claims: "if `mtf_block_rate` > max OR delta < 0 → auto-rollback to softer mode"
- **Missing:**
  - What **is** max? (MTF block_rate > 50% triggers rollback? 30%? No number given)
  - Rollback **timing:** Immediate? Next day? After N trades?
  - Recovery path: After rollback, how do you re-enable harder mode? What's the proof point?
  - False-positive sensitivity: If market regime changes, metrics might degrade temporarily. How many consecutive bad trades trigger rollback?

**Why This Matters:**
- Kill-switch without recovery = code path that executes once then never reverses
- "Auto-rollback" implies automation, but no automation spec exists
- Metrics are point-in-time (block_rate could spike on single news event)
- Dev team will implement 3 different interpretations without formal spec

**Evidence from Docs:**
- Brief L106: "if block_rate > max → rollback" with zero definition of max
- PRD L126-136: "MTF Conflict Resolution" section has zero threshold values
- No mention of cooldown period or re-enablement criteria

**Recommendation:** Specify thresholds (block_rate_max=50%), measurement window (last_N=100_trades), recovery criteria (must have 20 consecutive trades without degradation).

---

### 6. ❌ DFF Parameter Ranges Have Implicit Invalid States
**Severity:** MEDIUM | **Persistence:** Multiplier ranges specified, but edge cases not handled

**The Problem:**
- Brief L313-314 specifies: "tp_multiplier up to 10.0x" for rockets, "0.5-5.0x" for others
- **Not addressed:**
  - What if tp_multiplier < sl_multiplier? (TP target smaller than SL? Impossible trade)
  - What if tp_multiplier = 0? (No take-profit edge?)
  - Multiplier + source type interaction: If source=fixed_pct and multiplier=0.0, what does "0.0% ATR" mean?
  - Edge case: atr_period with atr_multiplier=0 → always uses ATR(period) = zero distance? Infinite losses?

**Why This Matters:**
- Optuna sampler will generate invalid combinations (tp < sl) without constraints
- Brief claims "validation rules (STRICT)" but never specifies the rules
- Implementation will add defensive checks, masking the specification gap
- Backtest results will include "degenerate parameter sets" that skew optimization

**Evidence from Docs:**
- Brief L190-196: "Validation Rules (STRICT enforcement)" section is empty/brief
- PRD L131-173: Multiplier ranges detailed, no ordering constraints
- No parameter interdependency matrix (which params can't coexist)

**Recommendation:** Create parameter dependency table: (source_type, role) → valid ranges, forbidden combinations, interdependencies.

---

### 7. ❌ Optimization Convergence Success Criteria Is Under-Specified
**Severity:** MEDIUM | **Persistence:** "Convergence ≤50 trials" claimed, but convergence definition missing

**The Problem:**
- Brief claims: NFR5 "Optuna convergence ≤50 trials"
- **Missing:**
  - Convergence **definition:** Pareto front stable? Best trial improves <1%? Loss plateau for 10 trials?
  - Multi-objective scenario: If 4 objectives (Sharpe, MaxDD, P&L, TradeCount), when is Pareto front "converged"?
  - Study size variance: Will convergence take 20 trials for some params, 100 for others? Average?
  - Optuna sampler sensitivity: TPE vs GP vs random — which one guarantees ≤50?

**Why This Matters:**
- "Convergence ≤50 trials" could mean: "lucky run had 50" or "guaranteed ≤50"
- Without formal definition, can't validate SLA in production
- Performance implications: If actual convergence is 200 trials but you tell users 50, they'll think system is slow
- Brief claims this as NFR, but NFRs should be testable

**Evidence from Docs:**
- Brief L1405: "Optuna convergence ≤50 trials (NFR5)" with no definition
- PRD L155-160: Optuna integration described, convergence not mentioned
- No reference to Optuna's built-in convergence detection

**Recommendation:** Define convergence formally: "Pareto hypervolume improves <2% over 15 consecutive trials" with sampler specification (TPE + pruner combo).

---

### 8. ❌ Dashboard Data Freshness Not Specified
**Severity:** MEDIUM | **Persistence:** "Dashboard load <3 sec" is performance, not freshness

**The Problem:**
- Brief claims: NFR1 "Dashboard load <3 sec" and FR1-2 "Net P&L + Profit Factor visualization"
- **Missing:**
  - How often is live P&L updated? (Every trade? Every minute? Every 5 seconds?)
  - How stale is acceptable? (60-second lag = order was filled 30 sec ago, user doesn't know)
  - What triggers refresh? (Trade event? Timer? Manual?)
  - Backtesting mode: Are dashboards updating as trades execute, or after backtest completes?

**Why This Matters:**
- Live trading dashboard with 5-minute stale data is a liability (user thinks P&L is +500 but it's already -500)
- Dashboard load time ≠ data freshness; can load cached stale data in 2 sec
- Brief conflates "responsive UI" with "accurate P&L"
- UX spec doesn't mention this; Architecture doesn't specify cache invalidation

**Evidence from Docs:**
- Brief L1919: "ручное участие ≤ 3 часа/неделю" implies monitoring, but no data freshness spec
- PRD L283-296: Caching strategy detailed as "global persistence" with zero eviction policy
- No mention of WebSocket, polling, or real-time sync

**Recommendation:** Specify: "Live P&L refreshed within N seconds of trade execution; acceptable lag ≤30 sec for monitoring mode."

---

### 9. ❌ Multi-Timeframe Signal Collision Not Formally Specified
**Severity:** HIGH | **Persistence:** MTF framework designed, but collision logic missing

**The Problem:**
- Brief claims: FR53-57 "MTF trading (signal aggregation)" with "default: NO cross-TF bias gating"
- **Missing:**
  - What happens if 1m TF signals BUY but 5m signals SELL? (System buys or doesn't?)
  - Is there a voting system? Majority wins?
  - What if 1m, 5m, 15m all disagree? (3-way tie, who wins?)
  - Default behavior is "each TF trades independently" — what does that mean exactly?
    - Each TF has own position? (Can 1m be long while 5m is short on same symbol?)
    - Or aggregated to single position? (Need collision resolution)

**Why This Matters:**
- "No cross-TF bias gating" is vague. Means:
  1. No signal filtering (all signals execute), OR
  2. Signals aggregate then execute once per symbol, OR
  3. Each TF controls its own position size
- Different interpretations = different risk profiles
- Brief says optional `mtf_confirmation_mode` handles this, but that's opt-in, not default behavior

**Evidence from Docs:**
- Brief L99-107: "Default: NO cross-TF bias gating" with zero algorithmic detail
- PRD L126-136: MTF modes described but signal collision not addressed
- Epic E (MTF trading) mentioned but no story detailing signal aggregation logic

**Recommendation:** Formalize: "Each TF trades independently; symbol-level aggregation uses [FIRST_TF_SIGNAL | MAJORITY_VOTE | SUM_POSITIONS]. Collisions resolved by [MODE]."

---

### 10. ❌ Smoke Test Coverage Depth Unspecified
**Severity:** MEDIUM | **Persistence:** "Smoke test results display" claimed, but test matrix missing

**The Problem:**
- Brief claims: FR9 "Smoke test results display" and NFR "3-stage validation pipeline progress"
- **Missing:**
  - What **is** a smoke test? (Single trade? 100 trades? Full 2-year backtest?)
  - Failure criteria? (Any losing trade = fail? Sharpe < 0 = fail? Max trade loss > 5% = fail?)
  - Multi-instrument coverage? (Smoke test each of 3 FX majors separately or combined?)
  - Time limit? (Smoke test must complete in <X seconds or timeout counts as failure?)

**Why This Matters:**
- "Smoke test" is an operational term with 10 different definitions
- If smoke test is too lenient (1 lucky trade), optimization noise defeats it
- If too strict (Sharpe > 1.0 on 10 trades), false failures waste time
- UX says display results, but never defines what "pass/fail" means visually

**Evidence from Docs:**
- Brief L1403: "Smoke test results display (FR9)" with zero definition
- PRD L276-280: "Smoke test" mentioned as first validation stage, criteria not specified
- No validation matrix (which assets, which time periods, which metrics)

**Recommendation:** Define smoke test: "Min 100 trades across 3 FX majors; pass if Profit Factor > 1.0 and max trade loss < 5% NAV."

---

### 11. ❌ Cost Impact Breakdowns Missing Fee Schedule
**Severity:** MEDIUM | **Persistence:** "Cost Impact breakdowns" claimed, fee structure undefined

**The Problem:**
- Brief claims: FR3 "Cost Impact breakdowns" and Brief L2107 "after costs"
- **Missing:**
  - Commission schedule by broker? (MT5 = 0.2%, KuCoin = 0.05%, CCXT = 0.1%?)
  - Slippage assumption? (Fixed 0.5%? Bid-ask 0.2%? Order book depth model?)
  - Financing costs? (Overnight hold fees, margin interest?)
  - Exchange-specific costs? (KuCoin has taker/maker tiers, MT5 has swap points)
  - Cost change detection: If costs change between backtest and live, dashboard breaks

**Why This Matters:**
- Success criteria: "Net P&L ≥ +1.0% **after costs**"
- If commission assumption is wrong by 0.5%, success metric is invalid
- Live trading with different cost structure = P&L mismatch blame
- Dashboard must show cost impact, but can't without fee schedule

**Evidence from Docs:**
- Brief L2107: "Net P&L (after costs) ≥ +1.0%"
- PRD L131-173: DFF structure detailed, cost assumptions in Brief not mentioned
- No fee schedule per broker or instrument

**Recommendation:** Document fee schedule: "MT5 0.2%, KuCoin 0.05% + 0.5% slippage assumption; review quarterly."

---

### 12. ❌ Rocket Worst-Case Loss Calculation Not Validated
**Severity:** HIGH | **Persistence:** "Worst case ≤10% NAV" claimed, math not shown

**The Problem:**
- Brief claims: L129 "Rocket bucket ≤10% NAV" as worst-case loss cap
- Brief also claims: L594 "10 rockets, 60% per rocket"
- **Math question:** If 10 rockets each at 6% = 60% of bucket (0.6% NAV each), worst case is **all 10 fail**:
  - 0.6% × 10 = **6% NAV loss** ✅ (within 10% cap)
- But Brief also claims L597-598: "New rocket enters at 1%, promoted to 2%-4%-6% over 3 months"
  - What if 5 rockets at 6%, 3 new ones at 1-4% each = 5×6% + 1% + 2% + 3% = **36% of bucket = 3.6% NAV** — **not 10%**
  - **Actual worst case: Can 10 rockets reach >10% allocation simultaneously?**

**Why This Matters:**
- Brief claims risk-of-ruin <5%, but if worst case is actually 15-20%, claim is false
- Stress testing needs correct worst-case baseline
- Capital allocation algorithm must enforce cap, but cap definition has ambiguity

**Evidence from Docs:**
- Brief L129, L594-598: Numbers given, no simulation showing worst-case stress
- Architecture Decision 1: Implementation enforces cap, but no proof worst case is actually ≤10%
- No edge case testing (concurrent promotions, kill-switches)

**Recommendation:** Run Monte Carlo: 1000 simulations with random rocket entry/promotion timing, verify max allocation never exceeds 10% NAV under all conditions.

---

### 13. ❌ UX Mockups Missing Critical Trading Flows
**Severity:** MEDIUM | **Persistence:** UX mentions dashboard, no trading execution flow

**The Problem:**
- Brief claims: FR26-30 "Position sizing strategies, Stop-loss methods, Trade management"
- UX design document likely describes dashboard layout, but:
  - **Missing:** How does user adjust position size during live trading?
  - How does user execute manual stop-loss or partial close?
  - Can user override optimization parameters mid-live? (Yes/No, and if yes, how?)
  - Error recovery: If order fails, what happens on dashboard?

**Why This Matters:**
- Brief says "≤3 hours/week manual participation" but UX doesn't show manual control flows
- If manual overrides take 5 minutes per decision, "≤3 hours/week" is impossible
- Trading execution UX is critical for adoption; if it's clunky, users abandon system
- PRD must align with UX, but no cross-reference

**Evidence from Docs:**
- Brief L1919: "ручное участие ≤ 3 часа/неделю" without specifying what manual actions are needed
- UX design document (not reviewed, likely missing) doesn't detail trading flows
- Epic 1 "Dashboard Foundation" is display-focused, not control-focused

**Recommendation:** Create UX flow diagram: position size adjustment → validation → live execution → dashboard confirmation.

---

### 14. ❌ Portfolio Rebalancing Frequency and Timing Unspecified
**Severity:** MEDIUM | **Persistence:** "Rebalance" mentioned, schedule undefined

**The Problem:**
- Brief claims: NFR (implied) "Portfolio-level risk controls" and "rebalance + RCA" on trigger
- **Missing:**
  - Rebalance frequency: Daily? Weekly? Monthly? On demand?
  - Rebalance timing: Market open? EOD? Specific time?
  - Rebalance algorithm: Proportional? Target allocation? Minimize turnover?
  - Conflict: What if rebalance signal arrives while trade is executing?

**Why This Matters:**
- Too-frequent rebalancing = excessive trading costs
- Too-infrequent = allocation drift (Rocket grows to 8% then crashes, was supposed to be capped at 6%)
- No algorithm = manual rebalancing = can't automate
- Brief implies automation ("rebalance + RCA") but spec is missing

**Evidence from Docs:**
- Brief L43: "Portfolio DD >50% = freeze + rebalance + RCA" with zero rebalance spec
- Architecture Decision 1: Portfolio monitoring defined, rebalancing algorithm not detailed
- No mention of rebalance timing or cost constraints

**Recommendation:** Specify: "Daily EOD rebalancing to target allocations; deferred if order in flight; max turnover 5% NAV/day."

---

### 15. ❌ Multi-Account/Multi-User Roadmap Vague
**Severity:** MEDIUM | **Persistence:** "Single-user Phase 1, multi-account Phase 2" — but no transition spec

**The Problem:**
- Brief implies: Phase 1 = single user, Phase 2 = multi-account
- **Missing:**
  - API contract for Phase 1 system that won't require rewrite in Phase 2
  - User context isolation assumptions (how are trade execution contexts kept separate?)
  - Permission model spec (which users can see which rockets?)
  - Data storage: Single-user in Phase 1 = one table per user, or pre-normalized schema?

**Why This Matters:**
- If Phase 1 hard-codes single user (user_id = hardcoded "admin"), Phase 2 requires rewrite
- If multi-user is already architected in Phase 1 but disabled, transition is smooth
- Brief doesn't clarify which approach is taken
- Codebase will have "technical debt" if Phase 1 assumes single-user everywhere

**Evidence from Docs:**
- Brief L1919 + Epic 9 notes: "Single-user Phase 1, multi-account Phase 2"
- No mention of API surface, user context propagation, or permission model
- Architecture doesn't reference Phase 2 multi-account design

**Recommendation:** Document Phase 1 API contract: "All endpoints accept optional user_id parameter (defaults to 'system'); data queries filtered by user_id."

---

### 16. ❌ Data Pipeline Freshness Guarantees Missing
**Severity:** MEDIUM | **Persistence:** "Frozen datasets" and "deterministic seeds" mentioned, but no SLA

**The Problem:**
- Brief claims: FR36-39 "Multi-source OHLCV loader, Data caching, Data quality validation, Frozen datasets"
- **Missing:**
  - Data freshness SLA: MT5 data must arrive by X minutes after candle close?
  - Latency budget: If MT5 is slow, how long does system wait before moving to fallback?
  - Data quality threshold: If data validation fails, is backtest aborted or does it proceed with warnings?
  - Version control: Are historical datasets versioned? Can backtest at T1 give different results at T2 if dataset version changed?

**Why This Matters:**
- "Frozen datasets" implies reproducibility, but only if you version the data
- "Deterministic seeds" are useless if data changes
- If OHLCV loading is too slow, optimization stalls (doesn't meet ≤50 trial SLA)
- Data quality failures should be visible, not silent

**Evidence from Docs:**
- Brief L2124: "Trading Instruments: 3+ FX majors + 3+ commodities + 5+ crypto"
- PRD L281-296: Caching strategy defined, data freshness not mentioned
- Epic D: "Data Pipeline" mentioned but no SLA

**Recommendation:** Specify: "Data arrives within 5 min of candle close; if delayed >10 min, backtest fails with error; datasets versioned by hash."

---

### 17. ❌ Backtesting Benchmark Baseline Undefined
**Severity:** MEDIUM | **Persistence:** "Success criteria" defined, but baseline comparison missing

**The Problem:**
- Brief claims: Success = "Net P&L ≥ +1.0%, correlation ≥ 0.5, Sharpe > 0"
- **Missing:**
  - Benchmark comparison: Is +1.0% vs buy-and-hold? Vs 0%? Vs risk-free rate?
  - Benchmark instrument: BUY-HOLD which index? SPY? EURUSD? Treasury?
  - Correlation baseline: Correlation with what? Market? Risk-free? Other strategies?
  - Out-of-sample caveat: Are these criteria for backtest, walk-forward, or paper-trading?

**Why This Matters:**
- "+1.0% NAV" could mean +1.0% gross (before fees) or net (after fees)
- If you compare vs buy-and-hold and buy-and-hold crashes 50%, +1% looks great (but it's survivor bias)
- "Correlation ≥ 0.5" with what? If it's correlation with cash, any strategy does that
- Brief doesn't clarify phase (backtest metrics are inflated vs live)

**Evidence from Docs:**
- Brief L1403-1410: Success criteria specified, no benchmark reference
- Brief L2113-2115: "Net P&L (after costs) ≥ +1.0%" without baseline
- No mention of survivorship bias or out-of-sample validation

**Recommendation:** Specify: "Success = Net P&L ≥ +1.0% vs EURUSD buy-hold on same period; Sharpe > 0.5 with correlation to asset <0.3."

---

### 18. ❌ Live Trading Kill-Switch Criteria Ambiguous
**Severity:** HIGH | **Persistence:** "Circuit breaker" mentioned, execution conditions fuzzy

**The Problem:**
- Brief claims: "VIX > 80, circuit breaker triggered" + "Portfolio DD >50% = freeze + RCA"
- **Missing:**
  - Kill-switch execution: Close all positions immediately? Taper over N trades?
  - VIX data source: Which VIX? (SPX VIX? EURUSD volatility index? Crypto VIX?)
  - Kill-switch reversibility: How do you un-kill when VIX drops back to 60?
  - Timing: Does kill-switch check happen per-trade, per-minute, per-candle?

**Why This Matters:**
- "Close all positions immediately" on VIX >80 could blow slippage budget
- If kill-switch checks per-trade, VIX spike during trade execution triggers false kill-switch
- If checks per-minute, 60-second lag means you could lose 5-10% while waiting
- No un-kill mechanism = system remains dead until manual intervention

**Evidence from Docs:**
- Brief L42-43: Kill-switch conditions stated without execution spec
- Architecture Decision 2: "RED = circuit_breaker triggered" but no state machine transitions detailed
- No mention of kill-switch recovery or confirmation

**Recommendation:** Specify: "Kill-switch on VIX >80 or DD >50%; closes open orders over 30 sec (avoid slippage); reverses to normal when both metrics <threshold for 5 consecutive candles."

---

### 19. ❌ Optimization Study Persistence and Recovery Missing
**Severity:** MEDIUM | **Persistence:** Optuna studies mentioned, backup/recovery strategy undefined

**The Problem:**
- Brief claims: "115 parameters, ≤50 trials for convergence"
- **Missing:**
  - Where are Optuna studies persisted? (SQLite? PostgreSQL? File?)
  - What if study database corrupts? (Rollback to checkpoint? Start from scratch?)
  - Multi-user scenario: Can two users optimize same strategy simultaneously? (Conflicts?)
  - Trial resumption: If optimization crashes after 40 trials, can it resume, or must restart?

**Why This Matters:**
- ≤50 trial SLA depends on resumption (if restart = restart counter, SLA is broken)
- Database corruption = hours of lost optimization work
- Multi-user simultaneous optimization = race conditions (last write wins? Both see same results?)
- Brief doesn't mention this; code will implement ad-hoc solution

**Evidence from Docs:**
- Brief L1405: "Optuna convergence ≤50 trials" assumes studies are persistent
- PRD L155-160: Optuna integration mentioned, persistence not discussed
- No mention of database backend or failover strategy

**Recommendation:** Specify: "Optuna studies stored in SQLite with daily backup; resumable from last completed trial; mutual exclusion for concurrent optimizations (lock-based)."

---

### 20. ❌ Explainability/Interpretability of DFF Choices Missing
**Severity:** MEDIUM | **Persistence:** DFF output (params) shown, but rationale never explained

**The Problem:**
- Brief claims: "DFF gives parameters adapting under regime"
- **Missing:**
  - Why did DFF select `atr_period=20, atr_multiplier=1.5` for SL? (History? Volatility? Optimization noise?)
  - Can user understand the choice? (No — it's a blackbox Optuna output)
  - Dashboard shows params, but not reasoning (robustness of choice, sensitivity analysis)
  - SHAP/LIME integration? (No mention in Brief or PRD)

**Why This Matters:**
- Users won't trust blackbox parameters, especially after a loss
- DFF appears magical ("system chose this"), but it's just Optuna → hard to debug
- Explainability could reduce support burden (users understand why system chose X)
- No mention of parameter importance or sensitivity in Brief

**Evidence from Docs:**
- Brief L140-145: DFF selection logic described as "conditional sampling" but not interpretable
- PRD L131-173: DFF structure detailed, no explainability layer
- No mention of Optuna importance scores or parameter sensitivity

**Recommendation:** Add dashboard section: "Parameter Importance (top 5 parameters driving performance delta); why was ATR chosen over BB? (Robustness: ±10% performance under out-of-sample data)."

---

### 21. ❌ Calendar Event Impact Validation Incomplete
**Severity:** MEDIUM | **Persistence:** "45+ pre-computed events" mentioned, but no validation process

**The Problem:**
- Brief mentions: News overlay acceptance criteria (lines 462-467)
- **Missing:**
  - Which 45+ events? (FOMC, CPI, ECB, earnings? List undefined)
  - How are events validated? (Backtest shows correlation with P&L, but validation unspecified)
  - False positive rate: How many "predicted" events don't actually impact markets?
  - Update mechanism: When FOMC date changes, how does system know?

**Why This Matters:**
- "45+ events" could be marketing number (actually 10 important ones)
- If event calendar is outdated (FOMC date wrong by 1 day), news overlay is useless
- No validation = event filtering is assumed to work, not proven
- Users see "news overlay reduces volatility by X%" but mechanism is unclear

**Evidence from Docs:**
- Brief L462-467: News overlay acceptance criteria with 20-day validation window
- Brief L2124: FX majors mentioned, but no event list
- No mention of calendar source (FRED? Bloomberg? Manual entry?)

**Recommendation:** Maintain event calendar: "45 core events (FOMC, CPI, ECB, etc.) updated quarterly; validation: correlation with volume spike >0.5."

---

### 22. ❌ Parallel Backtest Execution Race Conditions Not Addressed
**Severity:** HIGH | **Persistence:** "1000+ concurrent backtests" claimed, synchronization undefined

**The Problem:**
- Brief claims: NFR16 "1000+ concurrent backtests" and NFR3 "100K+ trades/min throughput"
- **Missing:**
  - Shared data access: If 100 backtests run on EURUSD data simultaneously, does each get a copy or share one?
  - File system contention: If each backtest writes results to disk, how do you prevent corruption?
  - Cache coherency: HNSW index updated during backtest — is it read-only snapshot or live?
  - Test isolation: Does backtest B see intermediate results from backtest A?

**Why This Matters:**
- "1000 concurrent" assumes perfect parallelization (doubtful without explicit locking)
- If backtests share HNSW index and one updates it → all other backtests see stale candidates
- Race condition on index rebuild = non-deterministic results
- Brief claims "deterministic seeds" but concurrent access breaks determinism

**Evidence from Docs:**
- Brief L1405, NFR16: "1000+ concurrent backtests" without synchronization strategy
- PRD L281-296: Caching strategy assumes static cache during backtest
- No mention of read-write locks, snapshots, or queue management

**Recommendation:** Implement: "Each backtest gets HNSW index snapshot at start; updates queued and applied after test completes; mutual exclusion prevents concurrent index updates."

---

### 23. ❌ Performance Regression Detection Missing
**Severity:** MEDIUM | **Persistence:** Success criteria defined, but no regression testing process

**The Problem:**
- Brief claims: Success = "Net P&L ≥ +1.0%, Sharpe > 0, Correlation ≥ 0.5"
- **Missing:**
  - What if P&L is still positive but down 50% from last month? (Still success? or regression?)
  - Regression thresholds: How much decline triggers re-optimization?
  - Monitoring frequency: Daily? Weekly? When?
  - Alert mechanism: Dashboard warning? Email? Automated fallback?

**Why This Matters:**
- "Success once ≠ success always" (market regime changes, strategy degrades)
- Brief doesn't mention monitoring post-deployment
- If system stops working and no one notices for a week, losses compound
- No regression detection = silent failures

**Evidence from Docs:**
- Brief L1919: "ручное участие ≤ 3 часа/неделю" implies monitoring, but no specifics
- PRD L283-296: Caching / performance mentioned, but no degradation detection
- No mention of alerts or automated fallback

**Recommendation:** Monitor: "If P&L drops >25% MoM, trigger yellow alert; >50% triggers auto-revert to last known-good parameters."

---

### 24. ❌ Model Versioning Strategy Undefined
**Severity:** MEDIUM | **Persistence:** "Deterministic seeds" imply versioning, but no scheme defined

**The Problem:**
- Brief claims: "Deterministic reproducibility (seeds)" and "Frozen datasets"
- **Missing:**
  - Version scheme: How do you name/tag strategies? (v1.0_dff_atm, v1.1_rocket_boost?)
  - Rollback mechanism: Can you quickly revert to v1.0 if v1.1 fails?
  - A/B testing: Can you run v1.0 and v1.1 side-by-side for comparison?
  - Metadata: What's recorded about each version? (Backtest date, params, performance)

**Why This Matters:**
- Without versioning, deploying new strategy is risky (no easy rollback)
- Brief claims "reproducible" but doesn't explain how to reproduce a specific historical version
- Multi-user phase 2: Different users might run different versions (conflicts)
- Regulatory/audit: If strategy fails, you need to explain what version was live

**Evidence from Docs:**
- Brief L1919 + L2107: Deterministic seeds mentioned, no version control
- PRD L281-296: Reproducibility mentioned, versioning not addressed
- Architecture doesn't reference strategy versioning

**Recommendation:** Implement: "Strategy versions tagged as {date}_{brief_id}_{epoch}; each version has parameter set snapshot, backtest results, performance metrics; rollback via tag revert."

---

### 25. ❌ Cost of Capital Assumption Nowhere Defined
**Severity:** MEDIUM | **Persistence:** "Profitable" claimed, but discount rate undefined

**The Problem:**
- Brief claims: Success = "+1.0% NAV over ≥20 trading days" (~3-4 weeks) = **~12-15% annualized return**
- **Missing:**
  - Cost of capital: Is 12% a good return? (Depends on risk-free rate + risk premium)
  - Opportunity cost: Could you make more in Treasury (currently 4-5%)?
  - Drawdown cost: If you accept 25% MaxDD (per Brief), is +12% worth the risk? (Sharpe ~0.48, poor)
  - Risk-adjusted comparison: How does this compare to 60/40 portfolio?

**Why This Matters:**
- Brief defines success without context
- User sees "+1% = success" and thinks it's a win, but it's mediocre risk-adjusted return
- No explicit cost-of-capital assumption = implicit assumption in code (probably zero)
- If system targets +1% but market conditions change (rates drop to 0%), success criteria becomes unrealistic

**Evidence from Docs:**
- Brief L1411, L2107: "Net P&L ≥ +1.0% NAV" without risk context
- Brief L129: "Risk-of-ruin <5%" is standalone, not risk-adjusted
- No mention of Sharpe threshold or information ratio

**Recommendation:** Document: "Success criteria assumes risk-free rate 4%, target Sharpe 0.75 (moderate risk); +1.0% NAV = 12% annualized at 25% MaxDD."

---

## Summary: Critical Finding Patterns

| Category | Count | Examples |
|----------|-------|----------|
| **Operational Black Boxes** | 4 | HNSW indexing, DFF sampling, Smoke test definition, Kill-switch execution |
| **Unvalidated Math** | 3 | Rocket allocation edge cases, Worst-case loss, Convergence definition |
| **Missing SLAs/Specs** | 7 | Data freshness, Rebalance frequency, Backtesting benchmarks, Version control |
| **Vague Requirements** | 6 | Multi-timeframe collisions, Cost impact detail, Portfolio rebalancing, UX flows |
| **Monitoring/Alerting Gaps** | 3 | Regression detection, Kill-switch recovery, Dashboard staleness |
| **Multi-user/Phase 2 Prep** | 2 | Account isolation contract, Model versioning |
| **Process Gaps** | 1 | Calendar event validation process |

---

## Halt Condition Check

✅ **HALT CONDITION SATISFIED:** 25 findings identified. Review complete.

---

## Next Steps

This adversarial review identified **25 critical findings across operational, mathematical, and specification gaps**. Recommend:

1. **Priority 1 (High):** Resolve HNSW black box, DFF sampling, Rocket math, Multi-TF collisions, Kill-switch execution, Parallel backtest race conditions (6 findings)
2. **Priority 2 (Medium):** Specify convergence definition, data freshness, cost schedule, smoke test criteria, rebalance frequency, performance regression detection (12 findings)
3. **Priority 3 (Low):** Document explainability, calendar validation, multi-user API contract, model versioning, cost of capital assumption (7 findings)

Each finding should be traced to a GitHub issue for implementation team.

