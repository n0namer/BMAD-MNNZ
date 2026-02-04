---
framework: "Monte Carlo Simulation"
framework_slug: "monte-carlo"
domain: finance
tier: 1
score: "19/25"
applied_to_project: "{project_id}"
project_name: "{project_name}"
created_date: "{YYYY-MM-DD}"
completed_date: null

integration_step: "5-scoring"
time_invested_minutes: 0
consilium_specialist: "Financial Analyst / Data Scientist"

scoring_contribution:
  provides_criteria: true
  provides_weights: true
  provides_scenarios: true
  mcda_dimensions:
    - "Probability of Success"
    - "Downside Risk (VaR)"
    - "Scenario Distribution"

deep_plan_contribution:
  generates_l2_headings: true
  generates_l3_tasks: true
  generates_milestones: true

linked_frameworks:
  - npv
  - dcf
  - real-options
  - kelly-criterion
prerequisite_frameworks:
  - npv  # or dcf - need base model to simulate
follows_frameworks:
  - npv
  - dcf
---

# Monte Carlo Simulation - {project_name}

> **Applied to Project**: {project_name}
> **Domain**: Finance
> **Tier**: 1 (19/25 - quantifies uncertainty)
> **Completed**: {completed_date}
> **Time Invested**: {time_invested_minutes} minutes

---

## Overview

Monte Carlo Simulation models the range of possible outcomes by running thousands of
randomized scenarios. Instead of single-point forecasts, it provides probability
distributions of results.

**Algorithm:**
```
FOR i = 1 to N (typically 10,000):
  FOR each uncertain variable:
    Sample random value from its probability distribution
  Calculate output metric (NPV, ROI, portfolio value, etc.)
  Store result[i]

OUTPUT:
  Mean, Median, Std Deviation of results
  Percentiles: P5, P10, P25, P50, P75, P90, P95
  Probability(outcome > target)
  Value at Risk (VaR) and Conditional VaR (CVaR)
```

**Key Probability Distributions:**
- **Normal** N(mu, sigma) -- Stock returns, inflation
- **Log-Normal** LN(mu, sigma) -- Asset prices (cannot go negative)
- **Triangular** T(min, mode, max) -- Expert estimates
- **Uniform** U(min, max) -- Complete uncertainty, equal probability
- **Poisson** P(lambda) -- Random event count (shocks, defaults)
- **Beta** B(alpha, beta) -- Bounded rates (conversion, churn)

---

## Framework Input

### 1. Model Description

- **What are we simulating?** {Description of decision/investment}
- **Output metric**: {NPV / Portfolio Value / Revenue / ROI}
- **Time horizon**: {N years/months}
- **Base model**: {NPV template / DCF template / Custom}

### 2. Uncertain Variables

#### Variable 1: {e.g., Revenue Growth Rate}

| Parameter | Value |
|-----------|-------|
| Distribution | {Normal / Log-Normal / Triangular / Uniform} |
| Mean (mu) | {value} |
| Std Dev (sigma) | {value} |
| Min | {value} (for Triangular/Uniform) |
| Max | {value} (for Triangular/Uniform) |
| Mode | {value} (for Triangular) |
| **Rationale** | {Why this distribution and parameters?} |
| **Data source** | {Historical data / Expert estimate / Industry benchmark} |

#### Variable 2: {e.g., Operating Margin}

| Parameter | Value |
|-----------|-------|
| Distribution | {type} |
| Parameters | {values} |
| **Rationale** | {why} |
| **Data source** | {source} |

#### Variable 3: {e.g., Discount Rate}

| Parameter | Value |
|-----------|-------|
| Distribution | {type} |
| Parameters | {values} |
| **Rationale** | {why} |
| **Data source** | {source} |

#### Variable 4: {e.g., Exit Multiple / Terminal Growth}

| Parameter | Value |
|-----------|-------|
| Distribution | {type} |
| Parameters | {values} |
| **Rationale** | {why} |
| **Data source** | {source} |

#### Variable 5: {e.g., Shock Event}

| Parameter | Value |
|-----------|-------|
| Distribution | {Poisson / Bernoulli} |
| Probability per period | {X}% |
| Impact if triggered | {-$amount or -X%} |
| **Rationale** | {why} |
| **Data source** | {source} |

*Add more variables as needed (typically 3-10 for meaningful simulation)*

### 3. Correlations Between Variables

| Variable A | Variable B | Correlation | Rationale |
|------------|------------|-------------|-----------|
| Revenue Growth | Operating Margin | {+0.3 / -0.2 / 0} | {Higher revenue may improve margins due to scale} |
| Discount Rate | Revenue Growth | {-0.4} | {Higher rates depress growth} |
| {var} | {var} | {value} | {why} |

**Note:** If no correlations specified, variables are treated as independent.

### 4. Simulation Parameters

| Parameter | Value |
|-----------|-------|
| Number of iterations (N) | {10,000} |
| Random seed (for reproducibility) | {12345 or "none"} |
| Confidence level for VaR | {95%} |
| Success threshold | {NPV > $0 / IRR > X% / Value > $Y} |

---

## Simulation Results

### Summary Statistics

| Statistic | Value |
|-----------|-------|
| **Mean** | ${mean} |
| **Median (P50)** | ${median} |
| **Std Deviation** | ${std_dev} |
| **Minimum** | ${min} |
| **Maximum** | ${max} |
| **Skewness** | {value} {right-skewed / left-skewed / symmetric} |

### Percentile Distribution

| Percentile | Value | Interpretation |
|------------|-------|----------------|
| P5 | ${value} | Worst 5% of scenarios |
| **P10** | **${value}** | **Pessimistic case** |
| P25 | ${value} | Conservative case |
| **P50** | **${value}** | **Expected (median) case** |
| P75 | ${value} | Optimistic case |
| **P90** | **${value}** | **Best realistic case** |
| P95 | ${value} | Best 5% of scenarios |

### Probability Analysis

| Question | Probability | Assessment |
|----------|-------------|------------|
| P({metric} > $0) | {X}% | {Acceptable / Risky} |
| P({metric} > ${target}) | {Y}% | {Achievable / Stretch} |
| P({metric} < -${loss_threshold}) | {Z}% | {Risk of significant loss} |
| P(success by threshold) | {W}% | {Above/Below 70% gate} |

### Risk Metrics

| Metric | Value | Interpretation |
|--------|-------|----------------|
| **Value at Risk (VaR 95%)** | -${var} | 95% confidence worst loss |
| **Conditional VaR (CVaR 95%)** | -${cvar} | Average loss in worst 5% |
| **Max Drawdown** | -${max_dd} | Worst single-scenario loss |
| **Probability of Loss** | {X}% | Chance of negative outcome |

```
VaR interpretation:
  "With 95% confidence, the loss will not exceed ${var}"
  "However, if it does exceed VaR, the average loss is ${cvar} (CVaR)"
```

### Sensitivity Analysis (Tornado Chart)

**Which variables drive the most uncertainty in the output?**

| Rank | Variable | Contribution to Variance | Correlation with Output |
|------|----------|-------------------------|------------------------|
| 1 | {Variable X} | {X}% | {+/- 0.XX} |
| 2 | {Variable Y} | {Y}% | {+/- 0.XX} |
| 3 | {Variable Z} | {Z}% | {+/- 0.XX} |
| 4 | {Variable W} | {W}% | {+/- 0.XX} |
| 5 | {Variable V} | {V}% | {+/- 0.XX} |

**Key insight:** {Variable X} explains {X}% of all output variation.
Focus risk mitigation efforts here.

---

## Scenario Planning

### Three Key Scenarios

| Scenario | Percentile | {Output Metric} | Key Conditions |
|----------|------------|------------------|----------------|
| **Bear Case** | P10 | ${value} | {What goes wrong} |
| **Base Case** | P50 | ${value} | {Expected path} |
| **Bull Case** | P90 | ${value} | {What goes right} |

### Bear Case (P10) Analysis
- **What happens:** {Description of pessimistic conditions}
- **Key drivers:** {Which variables cause this scenario}
- **Mitigation plan:** {How to protect against this}
- **Decision if realized:** {Continue / Pivot / Exit}

### Base Case (P50) Analysis
- **What happens:** {Description of expected conditions}
- **Key assumptions holding:** {Which assumptions must be true}
- **Monitoring triggers:** {KPIs to track}

### Bull Case (P90) Analysis
- **What happens:** {Description of optimistic conditions}
- **Upside capture plan:** {How to maximize if things go well}
- **Expansion triggers:** {When to accelerate investment}

---

## Risk Considerations

### Model Limitations

1. **Distribution assumptions**: Chosen distributions may not reflect reality
   - Mitigation: Use historical data where available, expert triangular estimates elsewhere
2. **Correlation assumptions**: Independence assumption may be wrong
   - Mitigation: Test with positive/negative correlation scenarios
3. **Black swan events**: Extreme events not captured by standard distributions
   - Mitigation: Add stress-test scenarios outside simulation
4. **Parameter estimation error**: Mean/sigma estimates may be inaccurate
   - Mitigation: Run "uncertainty of uncertainty" - vary parameters themselves
5. **Structural model risk**: Base model (NPV/DCF) may be flawed
   - Mitigation: Validate base model independently before Monte Carlo layer

### Confidence Assessment

| Component | Confidence | Rationale |
|-----------|------------|-----------|
| Variable distributions | {H/M/L} | {Based on X years of data / Expert estimate} |
| Correlations | {H/M/L} | {Measured / Estimated / Assumed zero} |
| Base model accuracy | {H/M/L} | {Validated / Theoretical / Untested} |
| Sample size (N iterations) | {H/M/L} | {10,000 = High / 1,000 = Medium} |

---

## Life OS Integration

### Scoring Impact (Step 5)

**How Monte Carlo enhances MCDA scoring (probabilistic upgrade):**

```yaml
criteria_from_framework:
  - name: "Probability of Positive Outcome"
    weight: 0.25
    score_formula: "P(NPV > 0) * 10"
    rationale: "Direct measure of project viability likelihood"
  - name: "Downside Risk (CVaR)"
    weight: 0.20
    score_formula: "10 - (abs(CVaR) / Initial_Investment) * 10"
    rationale: "Penalizes high potential losses"
  - name: "Expected Value (Mean NPV)"
    weight: 0.20
    score_formula: "(Mean_NPV / Highest_Mean_NPV_in_Portfolio) * 10"
    rationale: "Average outcome across all scenarios"
```

**Monte Carlo Decision Gate:**
- P(Success) >= 80% -> Auto-approve (high confidence)
- P(Success) 70-80% -> Approve with contingency plan
- P(Success) 50-70% -> Consilium review required
- P(Success) < 50% -> Reject or restructure

### Deep Plan Contribution (Step 8)

**L2 Headings Generated:**
- Risk Mitigation for {Top Risk Variable}
- Upside Capture for {Top Opportunity Variable}
- Monitoring & Trigger Framework
- Contingency Planning (Bear Case Protocol)

**L3 Tasks Generated:**
- [ ] Define monitoring KPIs for top 3 uncertain variables
- [ ] Set early warning triggers at P25 threshold
- [ ] Build contingency plan for bear case (P10) scenario
- [ ] Schedule quarterly re-simulation with updated actuals
- [ ] Reduce variance in top driver through {specific action}

**Milestones:**
- Assumption validation checkpoint (Month 3/6)
- Re-simulation with actual data (Quarter 2)
- Bear case trigger review (if any KPI hits P25 threshold)

### Scenario Integration (Step 6)

**Calendar/resource allocation by scenario:**
- Bear case budget reserve: ${X} (P10 preparation)
- Base case investment: ${Y} (standard plan)
- Bull case expansion budget: ${Z} (contingent on P75+ triggers)

---

## Synergies with Other Finance Frameworks

### Monte Carlo + NPV
- NPV provides deterministic base model
- Monte Carlo makes it probabilistic: "P(NPV > 0) = X%"
- Upgrades decision from binary (positive/negative) to probability

### Monte Carlo + DCF
- DCF assumptions (growth, margins, WACC) become simulation variables
- Each run produces different Enterprise Value
- Output: Distribution of valuations, not single point estimate

### Monte Carlo + Real Options
- Monte Carlo scenarios define when options are exercised
- "In 35% of scenarios, expansion option is triggered"
- "In 12% of scenarios, abandon option is optimal"
- Combine option value with probability of exercise

### Monte Carlo + Kelly Criterion
- Monte Carlo P(success) feeds into Kelly win probability (p)
- Monte Carlo P10/P90 ratio feeds into Kelly payoff odds (b)
- Workflow: Simulate -> Extract p and b -> Calculate Kelly allocation

---

## Tools & Implementation

### Recommended Tools

| Tool | Complexity | Cost | Best For |
|------|-----------|------|----------|
| Excel (manual RAND) | Low | Free | Simple models, 3-5 variables |
| Excel + @RISK | Medium | Paid | Professional analysis, tornado charts |
| Python (NumPy/SciPy) | High | Free | Custom models, large simulations |
| Crystal Ball | Medium | Paid | Enterprise-grade simulation |
| Portfolio Visualizer | Low | Free | Portfolio/retirement simulations |

### Python Template (Reference)

```python
import numpy as np

N = 10000  # simulations
results = []

for _ in range(N):
    growth = np.random.normal(0.06, 0.03)    # Revenue growth
    margin = np.random.triangular(0.25, 0.35, 0.45)  # EBIT margin
    wacc = np.random.uniform(0.08, 0.12)     # Discount rate

    # Calculate NPV using sampled values
    npv = calculate_npv(growth, margin, wacc)  # Your base model
    results.append(npv)

results = np.array(results)
print(f"Mean NPV: ${results.mean():,.0f}")
print(f"P(NPV > 0): {(results > 0).mean()*100:.1f}%")
print(f"VaR 95%: ${np.percentile(results, 5):,.0f}")
```

---

## Next Actions

- [ ] Build or reference base deterministic model (NPV/DCF)
- [ ] Identify 3-10 uncertain variables
- [ ] Research distributions for each variable (historical data or expert estimates)
- [ ] Define correlations between variables (if any)
- [ ] Run 10,000 simulation iterations
- [ ] Analyze results: percentiles, VaR, sensitivity rankings
- [ ] Create 3 scenarios (bear/base/bull) with action plans
- [ ] Present probabilistic results to decision-makers
- [ ] Update workflow-plan.md with Monte Carlo findings

---

## Notes

{Free-form notes, data sources, distribution fitting results, expert opinions}

---

## Metadata

**Framework Version**: 1.0
**Life OS Version**: 2.0
**Template Last Updated**: 2026-02-04
**Research Source**: finance-investment-frameworks.md
**Rankings Source**: method-rankings.yaml (Monte Carlo: 19/25, Tier 1)
