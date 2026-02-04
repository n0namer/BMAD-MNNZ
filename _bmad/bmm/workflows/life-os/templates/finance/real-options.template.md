---
framework: "Real Options Analysis"
framework_slug: "real-options"
domain: finance
tier: 2
score: "18/25"
applied_to_project: "{project_id}"
project_name: "{project_name}"
created_date: "{YYYY-MM-DD}"
completed_date: null

integration_step: "5-scoring"
time_invested_minutes: 0
consilium_specialist: "Financial Analyst / Strategic Planner"

scoring_contribution:
  provides_criteria: true
  provides_weights: true
  provides_scenarios: true
  mcda_dimensions:
    - "Flexibility Value"
    - "Irreversibility Risk"
    - "Learning Value"

deep_plan_contribution:
  generates_l2_headings: true
  generates_l3_tasks: true
  generates_milestones: true

linked_frameworks:
  - npv
  - monte-carlo
  - dcf
prerequisite_frameworks:
  - npv  # Traditional NPV needed as baseline
follows_frameworks:
  - npv
  - dcf
---

# Real Options Analysis - {project_name}

> **Applied to Project**: {project_name}
> **Domain**: Finance
> **Tier**: 2 (18/25 - values strategic flexibility)
> **Completed**: {completed_date}
> **Time Invested**: {time_invested_minutes} minutes

---

## Overview

Real Options Analysis applies financial option pricing theory to real-world investment
decisions. It captures the value of managerial flexibility -- the ability to defer,
expand, contract, abandon, or switch an investment based on new information.

**Core Insight:**
```
Expanded NPV = Traditional NPV + Option Value

Traditional NPV assumes "now or never" -- invest fully today or not at all.
Real Options recognizes that decisions can be staged, reversed, or modified.
The value of this flexibility is the Option Value.
```

**Option Types:**
- **Option to Defer** -- Wait for more information before investing
- **Option to Expand** -- Scale up if initial results are positive
- **Option to Contract** -- Scale down if market deteriorates
- **Option to Abandon** -- Exit and recover salvage value
- **Option to Switch** -- Change inputs, outputs, or strategy

**When to Use Real Options:**
- High uncertainty about future outcomes
- Decisions can be staged (not all-or-nothing)
- New information will become available over time
- Traditional NPV is negative or marginally positive
- Significant sunk costs if wrong decision is made

**When NOT to Use:**
- Simple go/no-go with no flexibility
- Very low uncertainty
- Time-critical decisions that cannot be deferred
- Low-cost, easily reversible decisions

---

## Framework Input

### 1. Investment Opportunity Description

- **Project/Investment**: {name}
- **Description**: {What is the investment?}
- **Total potential investment**: ${total_amount}
- **Traditional NPV (now or never)**: ${npv_traditional}
- **Traditional NPV decision**: {Accept / Reject / Marginal}

### 2. Uncertainty Assessment

| Factor | Current Estimate | Range of Outcomes | Uncertainty Level |
|--------|-----------------|-------------------|-------------------|
| Market demand | {value} | {low} - {high} | {H/M/L} |
| Revenue potential | ${value} | ${low} - ${high} | {H/M/L} |
| Technology risk | {value} | {low} - {high} | {H/M/L} |
| Competitive response | {value} | {low} - {high} | {H/M/L} |
| Regulatory environment | {value} | {low} - {high} | {H/M/L} |

**Overall uncertainty**: {High / Medium / Low}
**Will uncertainty reduce over time?** {Yes -- how / No}
**Time needed for uncertainty to resolve**: {X months/years}

### 3. Option to Defer

**Can we wait before investing?**

| Parameter | Value |
|-----------|-------|
| Maximum wait period | {X months/years} |
| Information gained by waiting | {What will we learn?} |
| Cost of waiting | {Opportunity cost, competitive risk} |
| Probability of positive signal | {X}% |
| Probability of negative signal | {Y}% |
| Value if invest after positive signal | ${NPV_positive} |
| Value if invest after negative signal | ${NPV_negative} |
| Value of not investing (wait & negative) | $0 |

**Option Value Calculation (simplified):**
```
Expected Value (wait) = P(positive) * NPV_positive + P(negative) * max(NPV_negative, 0)
Expected Value (now) = NPV_traditional
Option Value (defer) = E(wait) - E(now)
```

**Result:**
- Expected Value if invest now: ${ev_now}
- Expected Value if wait: ${ev_wait}
- **Option Value (Defer)**: **${option_defer}**

### 4. Option to Expand

**Can we scale up if things go well?**

| Parameter | Value |
|-----------|-------|
| Initial investment (Phase 1) | ${phase_1} |
| Expansion investment (Phase 2) | ${phase_2} |
| Trigger for expansion | {Conditions that justify it} |
| Probability of expansion trigger | {X}% |
| NPV of expanded project | ${npv_expanded} |
| NPV of Phase 1 only | ${npv_phase_1} |
| Time to expansion decision | {X months/years} |

**Option Value Calculation:**
```
Option Value (expand) = P(trigger) * max(NPV_expansion_incremental, 0)
                      = {X}% * max(${npv_expanded} - ${npv_phase_1} - ${phase_2}, 0)
```

**Result:**
- **Option Value (Expand)**: **${option_expand}**

### 5. Option to Contract

**Can we scale down if things go poorly?**

| Parameter | Value |
|-----------|-------|
| Full-scale operating cost | ${full_cost}/year |
| Reduced-scale operating cost | ${reduced_cost}/year |
| Cost savings from contraction | ${savings}/year |
| Trigger for contraction | {Conditions that justify it} |
| Probability of contraction trigger | {X}% |
| PV of cost savings | ${pv_savings} |
| Cost to restructure/downsize | ${restructure_cost} |

**Option Value Calculation:**
```
Option Value (contract) = P(trigger) * max(PV_savings - Restructure_cost, 0)
```

**Result:**
- **Option Value (Contract)**: **${option_contract}**

### 6. Option to Abandon

**Can we exit and recover value?**

| Parameter | Value |
|-----------|-------|
| Salvage/liquidation value | ${salvage} |
| Trigger for abandonment | {Conditions that justify exit} |
| Probability of abandonment trigger | {X}% |
| PV of continuing (if bad outcome) | ${pv_continue_bad} |
| Benefit of abandoning | ${salvage} - ${pv_continue_bad} |

**Option Value Calculation:**
```
Option Value (abandon) = P(trigger) * max(Salvage - PV_continue_bad, 0)
```

**Result:**
- **Option Value (Abandon)**: **${option_abandon}**

### 7. Option to Switch

**Can we change use, inputs, or strategy?**

| Parameter | Value |
|-----------|-------|
| Alternative use description | {What else could we do?} |
| Switching cost | ${switch_cost} |
| NPV of alternative use | ${npv_alternative} |
| Trigger for switching | {Conditions} |
| Probability of switching trigger | {X}% |

**Option Value Calculation:**
```
Option Value (switch) = P(trigger) * max(NPV_alternative - NPV_current - Switch_cost, 0)
```

**Result:**
- **Option Value (Switch)**: **${option_switch}**

---

## Option Tree (Decision Map)

```
Year 0: Initial Decision
  |
  +-- [INVEST NOW] -- ${phase_1}
  |     |
  |     +-- Year 1-2: Observe results
  |           |
  |           +-- [SUCCESS] (P = {X}%)
  |           |     |
  |           |     +-- [EXPAND] -- additional ${phase_2}
  |           |     |     NPV = ${npv_expanded}
  |           |     |
  |           |     +-- [CONTINUE] -- no extra investment
  |           |           NPV = ${npv_phase_1}
  |           |
  |           +-- [MEDIOCRE] (P = {Y}%)
  |           |     |
  |           |     +-- [CONTRACT] -- reduce scale
  |           |     |     NPV = ${npv_contracted}
  |           |     |
  |           |     +-- [CONTINUE] -- maintain course
  |           |           NPV = ${npv_mediocre}
  |           |
  |           +-- [FAILURE] (P = {Z}%)
  |                 |
  |                 +-- [ABANDON] -- recover ${salvage}
  |                 |     NPV = ${salvage} - ${phase_1}
  |                 |
  |                 +-- [SWITCH] -- alternative use
  |                       NPV = ${npv_alternative} - ${switch_cost}
  |
  +-- [WAIT] -- $0 now, decide in {X} months
        |
        +-- [POSITIVE INFO] (P = {A}%)
        |     +-- [INVEST] -- NPV = ${npv_positive}
        |
        +-- [NEGATIVE INFO] (P = {B}%)
              +-- [DON'T INVEST] -- NPV = $0
```

---

## Total Value with Real Options

### Expanded NPV Calculation

| Component | Value | % of Total |
|-----------|-------|-----------|
| Traditional NPV (base case) | ${npv_traditional} | {X}% |
| + Option to Defer | +${option_defer} | {Y}% |
| + Option to Expand | +${option_expand} | {Z}% |
| + Option to Contract | +${option_contract} | {W}% |
| + Option to Abandon | +${option_abandon} | {V}% |
| + Option to Switch | +${option_switch} | {U}% |
| **= Expanded NPV** | **${expanded_npv}** | **100%** |

### Decision Comparison

| Approach | Value | Decision |
|----------|-------|----------|
| Traditional NPV (now or never) | ${npv_traditional} | {Accept/Reject} |
| **Expanded NPV (with options)** | **${expanded_npv}** | **{Accept/Reject/Wait}** |
| Difference (Option Value) | +${total_option_value} | {Options add value} |

### Final Recommendation

**Decision**: {Accept with staged approach / Wait for information / Reject even with options}

**Rationale**: {Why, based on option analysis}

**Optimal strategy**: {Description of staged investment approach}

---

## Sensitivity Analysis

### Option Value Sensitivity to Uncertainty

| Uncertainty Level (Volatility) | Traditional NPV | Option Value | Expanded NPV |
|-------------------------------|-----------------|-------------|-------------|
| Low (sigma = {low}) | ${npv} | ${opt_low} | ${exp_low} |
| **Medium (sigma = {med})** | **${npv}** | **${opt_med}** | **${exp_med}** |
| High (sigma = {high}) | ${npv} | ${opt_high} | ${exp_high} |

**Key insight:** Higher uncertainty INCREASES option value (more potential for favorable information).

### Sensitivity to Wait Period

| Wait Period | Info Quality | Option Value (Defer) | Opportunity Cost |
|-------------|-------------|---------------------|-----------------|
| 3 months | Low | ${opt_3m} | ${cost_3m} |
| 6 months | Medium | ${opt_6m} | ${cost_6m} |
| 12 months | High | ${opt_12m} | ${cost_12m} |
| **Optimal** | **{quality}** | **${opt_best}** | **${cost_best}** |

---

## Risk Considerations

### Model Limitations

1. **Option pricing models assume**: Market completeness, no arbitrage, continuous trading
   - Reality: Real options are illiquid, markets incomplete
   - Mitigation: Use simplified decision tree instead of Black-Scholes for real assets
2. **Probability estimates**: Subjective for most real investments
   - Mitigation: Use Monte Carlo to generate probability distributions
3. **Interaction effects**: Multiple options may not be additive
   - Mitigation: Model options sequentially, not in isolation
4. **Execution risk**: Having the option is worthless if you cannot exercise it
   - Mitigation: Build organizational capability to react quickly

### Checklist

- [ ] All relevant option types identified (defer, expand, contract, abandon, switch)
- [ ] Probability estimates based on data or expert judgment
- [ ] Traditional NPV calculated first as baseline
- [ ] Option interactions considered (not just additive)
- [ ] Execution capability to exercise options confirmed
- [ ] Time decay of options considered (information window)

---

## Life OS Integration

### Scoring Impact (Step 5)

**How Real Options enhance MCDA scoring (Option Value as new criterion):**

```yaml
criteria_from_framework:
  - name: "Flexibility Value"
    weight: 0.15
    score_formula: "Option_Value / Total_Investment * 10"
    rationale: "Value of strategic flexibility relative to commitment"
  - name: "Irreversibility Risk"
    weight: 0.15
    score_formula: "10 - (Sunk_Cost_Percentage * 10)"
    rationale: "Lower sunk costs = more flexibility = better"
  - name: "Learning Value"
    weight: 0.10
    score_formula: "Info_Gained_by_Staging * 10"
    rationale: "Staged approach reveals information, reducing future risk"
```

### Deep Plan Contribution (Step 8)

**L2 Headings Generated (Stage-gate with real options):**
- Gate 0: Initial Assessment & Option Identification
- Gate 1: Phase 1 Investment (Limited Commitment)
- Gate 2: Information Review & Option Exercise Decision
- Gate 3: Full Commitment / Expand / Contract / Abandon

**L3 Tasks Generated:**
- [ ] Calculate traditional NPV as baseline
- [ ] Identify all available real options
- [ ] Estimate probabilities for each scenario branch
- [ ] Design Phase 1 as minimum viable investment
- [ ] Define clear triggers for each option exercise
- [ ] Schedule Gate review meetings at decision points
- [ ] Build information-gathering plan (what to learn before Gate 2)

**Milestones:**
- Gate 1: Phase 1 investment decision (Date: {X})
- Gate 2: Option exercise decision (Date: {Y})
- Gate 3: Full commitment or exit decision (Date: {Z})
- Information milestone: {What we must learn by when}

### Decision Tracking

**Key decisions made using Real Options:**
1. **Decision**: {What was decided}
   - **Expanded NPV**: ${amount}
   - **Option exercised**: {Defer / Expand / Abandon / None}
   - **Rationale**: {Based on information revealed}
   - **Confidence**: {High / Medium / Low}

---

## Synergies with Other Finance Frameworks

### Real Options + NPV
- NPV = baseline "now or never" value
- Real Options add flexibility value on top of NPV
- Expanded NPV = NPV + Option Value
- Projects rejected by NPV may be accepted with Real Options

### Real Options + Monte Carlo
- Monte Carlo scenarios define WHEN options get exercised
- "In 35% of simulations, expansion option triggered"
- "In 12% of simulations, abandon option optimal"
- Probabilistic option exercise -> more realistic Expanded NPV

### Real Options + DCF
- DCF provides detailed cash flow model for each scenario branch
- Real Options provide decision framework for when to shift between scenarios
- Combined: Dynamic DCF with embedded decision gates

### Real Options + Kelly Criterion
- Real Options "Phase 1" = Kelly fractional bet (limited initial commitment)
- If Phase 1 succeeds -> Kelly recalculates with updated probabilities
- Staged investment = fractional Kelly applied over time

---

## Valuation Methods Reference

### Simplified Decision Tree (Recommended for Most Cases)

Best for personal/business decisions with discrete outcomes.
Use probability-weighted expected values at each node.

### Binomial Lattice

For options with time-varying uncertainty over multiple periods.
```
u = e^(sigma * sqrt(dt))    -- up factor
d = 1/u                      -- down factor
p = (e^(r*dt) - d) / (u - d) -- risk-neutral probability
```

### Black-Scholes (Reference Only)

For European-style options with continuous uncertainty.
```
C = S * N(d1) - K * e^(-rT) * N(d2)
d1 = [ln(S/K) + (r + sigma^2/2) * T] / (sigma * sqrt(T))
d2 = d1 - sigma * sqrt(T)
```
*Note: Black-Scholes assumptions rarely hold for real options.
Use with caution -- decision tree approach is preferred.*

---

## Next Actions

- [ ] Calculate traditional NPV as baseline
- [ ] List all available real options (defer, expand, contract, abandon, switch)
- [ ] Estimate probabilities and payoffs for each option
- [ ] Build decision tree with option nodes
- [ ] Calculate Expanded NPV
- [ ] Design staged investment approach
- [ ] Define clear triggers for option exercise
- [ ] Update workflow-plan.md with staged decision plan

---

## Notes

{Free-form notes, comparable staged investments, industry examples, advisor input}

---

## Metadata

**Framework Version**: 1.0
**Life OS Version**: 2.0
**Template Last Updated**: 2026-02-04
**Research Source**: finance-investment-frameworks.md
**Rankings Source**: method-rankings.yaml (Real Options: 18/25, Tier 2)
