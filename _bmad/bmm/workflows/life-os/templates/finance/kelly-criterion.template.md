---
framework: "Kelly Criterion"
framework_slug: "kelly-criterion"
domain: finance
tier: 3
score: "17/25"
applied_to_project: "{project_id}"
project_name: "{project_name}"
created_date: "{YYYY-MM-DD}"
completed_date: null

integration_step: "6-integration"
time_invested_minutes: 0
consilium_specialist: "Financial Analyst / Data Scientist"

scoring_contribution:
  provides_criteria: true
  provides_weights: true
  provides_scenarios: false
  mcda_dimensions:
    - "Optimal Allocation"
    - "Risk of Ruin"
    - "Portfolio Sizing"

deep_plan_contribution:
  generates_l2_headings: true
  generates_l3_tasks: true
  generates_milestones: true

linked_frameworks:
  - monte-carlo
  - real-options
  - capm
prerequisite_frameworks:
  - monte-carlo  # Provides probability estimates
follows_frameworks:
  - monte-carlo
  - npv
---

# Kelly Criterion - {project_name}

> **Applied to Project**: {project_name}
> **Domain**: Finance
> **Tier**: 3 (17/25 - optimal position sizing)
> **Completed**: {completed_date}
> **Time Invested**: {time_invested_minutes} minutes

---

## Overview

Kelly Criterion determines the mathematically optimal fraction of capital to allocate
to an investment or bet. It maximizes long-term growth rate while avoiding ruin.

**Formula:**
```
f* = (b * p - q) / b

Where:
  f* = Optimal fraction of capital to bet/invest
  b  = Net odds (profit per $1 wagered, i.e., win/loss ratio)
  p  = Probability of winning
  q  = Probability of losing (1 - p)
```

**Interpretation:**
- f* > 0: Favorable bet, invest f* fraction of capital
- f* = 0: Break-even, no allocation justified
- f* < 0: Unfavorable bet, do not invest (or bet against)

**WARNING:** Full Kelly is mathematically optimal but extremely aggressive.
Practitioners use Fractional Kelly (typically 0.25-0.50 of full Kelly) to:
- Reduce volatility of portfolio
- Account for estimation errors in p and b
- Avoid psychological discomfort of large drawdowns

**Origin:** Developed by John Kelly (Bell Labs, 1956) for information theory.
Adopted by professional gamblers (Ed Thorp) and hedge funds.

---

## Framework Input

### 1. Investment/Bet Description

- **Investment opportunity**: {name/description}
- **Type**: {Single bet / Repeated bet / Portfolio allocation}
- **Total available capital**: ${total_capital}
- **Time horizon**: {one-time / recurring frequency}

### 2. Probability Estimation

#### Win Probability (p)

| Source | Probability | Confidence |
|--------|-------------|------------|
| Historical data ({N} samples) | {X}% | {H/M/L} |
| Monte Carlo simulation | {Y}% | {H/M/L} |
| Expert/subjective estimate | {Z}% | {H/M/L} |
| **Selected p** | **{p}%** | **{overall confidence}** |

**Rationale for selected probability:**
{Why this probability estimate is reliable}

**Loss Probability (q):** {q}% = 100% - {p}% = {q}%

#### Win/Loss Ratio (b)

| Outcome | Value | How Calculated |
|---------|-------|----------------|
| Win payoff (per $1 invested) | ${b} | {Expected profit if success / Amount at risk} |
| Loss amount (per $1 invested) | $1.00 | {Amount lost if failure} |
| **Net odds (b)** | **{b}** | **Win payoff / Loss amount** |

**Alternative calculation from NPV/DCF:**
```
b = Expected Positive NPV / Initial Investment (if success)
    Example: $150K profit / $100K invested = 1.5

Or from scenarios:
b = P90_outcome / Investment_at_risk
```

### 3. Asymmetric Payoffs (Advanced)

If win and loss amounts are not symmetric:

| Outcome | Probability | Payoff | Expected Value |
|---------|-------------|--------|----------------|
| Big Win | {X}% | +${amount} | ${ev} |
| Small Win | {Y}% | +${amount} | ${ev} |
| Small Loss | {Z}% | -${amount} | ${ev} |
| Big Loss | {W}% | -${amount} | ${ev} |
| **Total EV** | 100% | | **${total_ev}** |

**For asymmetric payoffs, use generalized Kelly:**
```
f* = (Expected Value) / (Expected Loss if Lose)
   = Sum(p_i * payoff_i) / abs(Expected Loss)
```

---

## Kelly Calculation

### Basic Kelly

```
f* = (b * p - q) / b

f* = ({b} * {p} - {q}) / {b}
f* = ({b*p} - {q}) / {b}
f* = {numerator} / {b}
f* = {kelly_percent}%
```

### Fractional Kelly (Recommended)

| Fraction | Allocation (% of capital) | Dollar Amount | Risk Level |
|----------|--------------------------|---------------|------------|
| Full Kelly (1.0x) | {kelly}% | ${full_kelly_amount} | AGGRESSIVE |
| 3/4 Kelly (0.75x) | {kelly*0.75}% | ${three_quarter_amount} | High |
| **Half Kelly (0.50x)** | **{kelly*0.5}%** | **${half_kelly_amount}** | **RECOMMENDED** |
| Quarter Kelly (0.25x) | {kelly*0.25}% | ${quarter_kelly_amount} | Conservative |

### Result Summary

| Metric | Value |
|--------|-------|
| Win Probability (p) | {p}% |
| Loss Probability (q) | {q}% |
| Win/Loss Ratio (b) | {b}:1 |
| **Full Kelly (f*)** | **{kelly}%** |
| **Recommended Allocation (Half Kelly)** | **{kelly*0.5}%** |
| **Dollar Amount** | **${half_kelly_amount}** |
| Expected Growth Rate (full Kelly) | {growth}% per period |
| Expected Growth Rate (half Kelly) | {growth_half}% per period |

### Decision

| Criterion | Result | Action |
|-----------|--------|--------|
| f* > 0? | {YES/NO} | {Favorable / Unfavorable bet} |
| f* > 5%? | {YES/NO} | {Meaningful allocation / Too small to bother} |
| f* < 25%? | {YES/NO} | {Reasonable / Dangerously large - check assumptions} |
| Probability confidence | {H/M/L} | {Full Kelly / Half Kelly / Quarter Kelly} |
| **Recommendation** | | **Allocate {X}% (${amount}) using {fraction} Kelly** |

---

## Sensitivity Analysis

### Probability Sensitivity

| Win Probability (p) | Full Kelly f* | Half Kelly | Decision |
|---------------------|--------------|------------|----------|
| {p - 15}% | {kelly}% | {half}% | {Invest/Pass} |
| {p - 10}% | {kelly}% | {half}% | {Invest/Pass} |
| {p - 5}% | {kelly}% | {half}% | {Invest/Pass} |
| **{p}% (Base)** | **{kelly}%** | **{half}%** | **{Invest}** |
| {p + 5}% | {kelly}% | {half}% | {Invest} |
| {p + 10}% | {kelly}% | {half}% | {Invest} |

**Breakeven probability** (f* = 0): p = q/b = {breakeven_p}%

### Odds Sensitivity

| Win/Loss Ratio (b) | Full Kelly f* | Half Kelly | Decision |
|--------------------|--------------|------------|----------|
| {b * 0.5} | {kelly}% | {half}% | {Invest/Pass} |
| {b * 0.75} | {kelly}% | {half}% | {Invest/Pass} |
| **{b} (Base)** | **{kelly}%** | **{half}%** | **{Invest}** |
| {b * 1.25} | {kelly}% | {half}% | {Invest} |
| {b * 1.5} | {kelly}% | {half}% | {Invest} |

### Combined Sensitivity Matrix

| | b = {b*0.75} | b = {b} | b = {b*1.25} |
|---|---|---|---|
| **p = {p-10}%** | f* = {X}% | f* = {X}% | f* = {X}% |
| **p = {p}%** | f* = {X}% | **f* = {base}%** | f* = {X}% |
| **p = {p+10}%** | f* = {X}% | f* = {X}% | f* = {X}% |

---

## Portfolio Application

### Multi-Bet Kelly (Multiple Investments)

If applying Kelly across multiple independent investments:

| Investment | p | b | Kelly f* | Half Kelly | Amount |
|------------|---|---|----------|------------|--------|
| {Investment A} | {p}% | {b} | {kelly}% | {half}% | ${amount} |
| {Investment B} | {p}% | {b} | {kelly}% | {half}% | ${amount} |
| {Investment C} | {p}% | {b} | {kelly}% | {half}% | ${amount} |
| **Total Allocated** | | | | **{total}%** | **${total_amount}** |
| **Cash Reserve** | | | | **{100-total}%** | **${reserve}** |

**WARNING:** Sum of Kelly allocations should not exceed 100%.
If total > 100%, scale down proportionally.

### Budget Allocation (Step 6 Integration)

**Total Project Portfolio Budget:** ${total_budget}

| Project | Kelly Allocation % | Budget Allocated | Rationale |
|---------|-------------------|------------------|-----------|
| {Project 1} | {X}% | ${amount} | {Highest conviction, best odds} |
| {Project 2} | {Y}% | ${amount} | {Moderate conviction} |
| {Project 3} | {Z}% | ${amount} | {Lower conviction but diversifying} |
| Cash/Reserve | {R}% | ${amount} | Safety buffer |
| **Total** | **100%** | **${total_budget}** | |

---

## Risk Considerations

### Kelly Criterion Dangers

1. **Probability estimation error**: Small errors in p dramatically change f*
   - If true p = 50% but you estimate 55%, Kelly says invest; reality says don't
   - **Mitigation**: ALWAYS use fractional Kelly (0.25-0.50)
   - **Rule of thumb**: If confidence in p is Low, use Quarter Kelly

2. **Full Kelly volatility**: Full Kelly has enormous drawdowns
   - Expected maximum drawdown ~ 50% before recovering
   - Psychologically devastating even if mathematically optimal
   - **Mitigation**: Half Kelly has 75% of growth rate with much lower drawdowns

3. **Non-independent bets**: Kelly assumes independent outcomes
   - If investments are correlated, total allocation should be lower
   - **Mitigation**: Reduce Kelly by correlation factor

4. **Finite horizon**: Kelly optimizes for infinite repetitions
   - Single bets may not have time to recover from adverse outcomes
   - **Mitigation**: For one-time decisions, use more conservative fraction

5. **Unknown unknowns**: Edge (b*p - q) may be an illusion
   - Overfitting to historical data, survivorship bias
   - **Mitigation**: Stress-test with worst-case p and b values

### When Kelly Is Most Useful

- Repeated decisions with known probabilities (trading, gambling)
- Portfolio allocation across multiple opportunities
- Sizing an investment when you have a quantified edge
- Budget allocation across multiple projects

### When Kelly Is Least Useful

- Unknown probabilities (use Monte Carlo first to estimate)
- Correlated investments (need multivariate Kelly)
- One-time decisions (not enough repetitions for Kelly to work)
- When loss = ruin (cannot recover, Kelly requires ability to repeat)

---

## Life OS Integration

### Scoring Impact (Step 5)

**How Kelly Criterion informs MCDA scoring:**

```yaml
criteria_from_framework:
  - name: "Optimal Allocation"
    weight: 0.10
    score_formula: "Kelly_f_star * 10 (capped at 10)"
    rationale: "Higher Kelly = stronger edge = better investment"
  - name: "Risk of Ruin"
    weight: 0.10
    score_formula: "10 - (Probability_of_Total_Loss * 10)"
    rationale: "Penalizes investments that can wipe out capital"
```

### Portfolio Allocation (Step 6)

**Kelly directly informs resource/budget allocation decisions:**
- High-Kelly projects get proportionally more budget
- Low-Kelly projects get minimal or no allocation
- Cash reserve = 100% - sum(Kelly allocations)

### Deep Plan Contribution (Step 8)

**L2 Headings Generated (Budget allocation phases):**
- Phase 1: Initial Allocation (Quarter Kelly - conservative entry)
- Phase 2: Validate Assumptions (track actual win rate)
- Phase 3: Scale Up (increase to Half Kelly if assumptions confirmed)
- Phase 4: Review & Rebalance (recalculate with updated probabilities)

**L3 Tasks Generated:**
- [ ] Estimate win probability from available data
- [ ] Calculate win/loss ratio from expected outcomes
- [ ] Compute full Kelly and select fractional Kelly level
- [ ] Allocate capital according to Kelly recommendation
- [ ] Track actual outcomes to validate probability estimates
- [ ] Recalculate Kelly after {N} observations/periods
- [ ] Rebalance portfolio based on updated Kelly fractions

**Milestones:**
- Initial Kelly calculation complete
- First {N} outcomes tracked (validate p estimate)
- Kelly recalculation with actual data (update allocation)
- Portfolio rebalancing event

### Decision Tracking

**Key decisions made using Kelly Criterion:**
1. **Decision**: {How much to allocate}
   - **Kelly Fraction Used**: {1.0 / 0.5 / 0.25}
   - **Amount Allocated**: ${amount} ({X}% of capital)
   - **Rationale**: {Edge identified with confidence level}
   - **Review Date**: {When to recalculate}

---

## Synergies with Other Finance Frameworks

### Kelly + Monte Carlo
- Monte Carlo provides P(success) -> Kelly's win probability (p)
- Monte Carlo P10/P90 ratio informs Kelly's win/loss odds (b)
- Workflow: Run Monte Carlo -> Extract p and b -> Calculate Kelly allocation
- This is the STRONGEST synergy in the finance toolkit

### Kelly + Real Options
- Real Options Phase 1 = Quarter Kelly (limited initial commitment)
- If Phase 1 validates assumptions, update p and increase to Half Kelly
- Staged investment via real options = iterative Kelly recalculation

### Kelly + CAPM
- CAPM Alpha identifies the "edge" (excess return above risk-adjusted benchmark)
- If Alpha > 0, Kelly determines HOW MUCH to invest
- CAPM answers "Should I invest?", Kelly answers "How much?"

### Kelly + NPV
- NPV provides expected profit (numerator for b calculation)
- b = Expected NPV / Initial Investment (if success)
- Combined with p from Monte Carlo, gives complete Kelly inputs

---

## Worked Example

### Example: SaaS Business Investment

**Setup:**
- Investment opportunity: acquire SaaS product for $200,000
- If successful (grow to $50K MRR): worth $600,000 (3x return) -> profit = $400K
- If unsuccessful (churn kills it): worth $50,000 (salvage) -> loss = $150K
- Win probability (from Monte Carlo): 60%

**Kelly Calculation:**
```
b = Win payoff / Loss amount = $400,000 / $150,000 = 2.67
p = 0.60
q = 0.40

f* = (b * p - q) / b
f* = (2.67 * 0.60 - 0.40) / 2.67
f* = (1.60 - 0.40) / 2.67
f* = 1.20 / 2.67
f* = 0.449 = 44.9%

Half Kelly = 22.5%
```

**If total capital = $500,000:**
- Full Kelly allocation: $224,500 (44.9% - very aggressive)
- Half Kelly allocation: $112,500 (22.5% - recommended)
- Quarter Kelly allocation: $56,250 (11.2% - conservative)

**Recommendation:** Allocate $112,500 (Half Kelly) given moderate confidence in 60% win rate.

---

## Next Actions

- [ ] Estimate win probability (p) using data, Monte Carlo, or expert judgment
- [ ] Calculate win/loss ratio (b) from expected outcomes
- [ ] Compute Kelly fraction f*
- [ ] Select fractional Kelly level based on confidence
- [ ] Allocate capital accordingly
- [ ] Define tracking plan to validate probability estimates
- [ ] Schedule recalculation date ({N} observations or {X} months)
- [ ] Update workflow-plan.md with allocation decision

---

## Notes

{Free-form notes, probability estimation details, comparable bet outcomes, historical edge data}

---

## Metadata

**Framework Version**: 1.0
**Life OS Version**: 2.0
**Template Last Updated**: 2026-02-04
**Research Source**: finance-investment-frameworks.md
**Rankings Source**: method-rankings.yaml (Kelly Criterion: 17/25, Tier 3)
