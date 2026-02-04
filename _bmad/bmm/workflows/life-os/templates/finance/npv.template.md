---
framework: "Net Present Value (NPV)"
framework_slug: "npv"
domain: finance
tier: 1
score: "24/25"
applied_to_project: "{project_id}"
project_name: "{project_name}"
created_date: "{YYYY-MM-DD}"
completed_date: null

integration_step: "5-scoring"
time_invested_minutes: 0
consilium_specialist: "Financial Analyst"

scoring_contribution:
  provides_criteria: true
  provides_weights: true
  provides_scenarios: true
  mcda_dimensions:
    - "Financial Return"
    - "Payback Period"
    - "Risk-Adjusted Value"

deep_plan_contribution:
  generates_l2_headings: true
  generates_l3_tasks: true
  generates_milestones: true

linked_frameworks:
  - dcf
  - monte-carlo
  - real-options
prerequisite_frameworks: []
follows_frameworks: []
---

# NPV Analysis - {project_name}

> **Applied to Project**: {project_name}
> **Domain**: Finance
> **Tier**: 1 (24/25 - most universal finance framework)
> **Completed**: {completed_date}
> **Time Invested**: {time_invested_minutes} minutes

---

## Overview

NPV (Net Present Value) - gold standard for capital allocation decisions.
Calculates the present value of all future cash flows minus initial investment.

**Formula:**
```
NPV = Sum [ CF_t / (1 + r)^t ] - I_0

Where:
  CF_t  = Net Cash Flow in period t
  r     = Discount rate (WACC or required return)
  t     = Period number (1, 2, ..., N)
  I_0   = Initial Investment (Year 0 outflow)
```

**Decision Rule:**
- **NPV > 0** -> Accept (project creates value)
- **NPV < 0** -> Reject (project destroys value)
- **NPV = 0** -> Indifferent (project breaks even at required return)

---

## Framework Input

### 1. Investment Details

- **Project/Investment Name**: {name}
- **Initial Investment (Year 0)**: ${amount}
- **Project Lifespan**: {N} years
- **Currency**: {currency}

### 2. Discount Rate Selection

**Method**: {WACC / Required Return / CAPM-derived / Rule of Thumb}

| Parameter | Value | Source |
|-----------|-------|--------|
| Risk-Free Rate (Rf) | {X}% | 10-year Treasury |
| Equity Risk Premium | {Y}% | Market data |
| Project Beta | {beta} | Comparable analysis |
| **Discount Rate (r)** | **{r}%** | **Calculated/Selected** |

**Rationale for discount rate:**
{Why this rate is appropriate for the risk level of this project}

**2026 Reference Rates:**
- Conservative (low risk): 6-8%
- Moderate (market-level risk): 8-12%
- Aggressive (high risk/startup): 12-20%

### 3. Cash Flow Projections

**Assumptions:**
- Revenue growth rate: {X}% per year
- Operating expense ratio: {Y}%
- Tax rate: {Z}%
- Other: {assumptions}

| Year | Cash Inflow | Cash Outflow | Net Cash Flow (CF_t) |
|------|-------------|--------------|----------------------|
| 0    | $0          | ${initial}   | -${initial}          |
| 1    | ${amount}   | ${amount}    | ${net}               |
| 2    | ${amount}   | ${amount}    | ${net}               |
| 3    | ${amount}   | ${amount}    | ${net}               |
| 4    | ${amount}   | ${amount}    | ${net}               |
| 5    | ${amount}   | ${amount}    | ${net}               |
| ...  | ...         | ...          | ...                  |
| N    | ${amount}   | ${amount}    | ${net}               |

### 4. Terminal / Residual Value

**Method**: {None / Salvage Value / Gordon Growth / Exit Multiple}

- **Terminal Value (if applicable)**: ${TV}
- **Growth rate for perpetuity (g)**: {g}%
- **Exit multiple**: {X}x {metric}

---

## NPV Calculation

### Discount Factor Table

| Year | Net Cash Flow | Discount Factor 1/(1+r)^t | Present Value |
|------|---------------|---------------------------|---------------|
| 0    | -${initial}   | 1.000                     | -${initial}   |
| 1    | ${CF_1}       | {factor}                  | ${PV_1}       |
| 2    | ${CF_2}       | {factor}                  | ${PV_2}       |
| 3    | ${CF_3}       | {factor}                  | ${PV_3}       |
| 4    | ${CF_4}       | {factor}                  | ${PV_4}       |
| 5    | ${CF_5}       | {factor}                  | ${PV_5}       |
| TV   | ${TV}         | {factor}                  | ${PV_TV}      |

### Result

| Metric | Value |
|--------|-------|
| **NPV** | **${NPV}** |
| IRR (Internal Rate of Return) | {IRR}% |
| Payback Period | {X.X} years |
| Profitability Index (NPV/I_0) | {PI} |
| **Decision** | **{Accept / Reject / Indifferent}** |

---

## Sensitivity Analysis

### Discount Rate Sensitivity

| Discount Rate | NPV | Decision |
|---------------|-----|----------|
| {r - 4}% | ${NPV_low_r} | {Accept/Reject} |
| {r - 2}% | ${NPV_mid_low_r} | {Accept/Reject} |
| **{r}% (Base)** | **${NPV_base}** | **{Accept/Reject}** |
| {r + 2}% | ${NPV_mid_high_r} | {Accept/Reject} |
| {r + 4}% | ${NPV_high_r} | {Accept/Reject} |

**Breakeven discount rate** (NPV = 0): {X}%

### Cash Flow Sensitivity

| Scenario | CF Adjustment | NPV | Decision |
|----------|---------------|-----|----------|
| Pessimistic | -30% | ${NPV_pessimistic} | {Accept/Reject} |
| Conservative | -15% | ${NPV_conservative} | {Accept/Reject} |
| **Base Case** | **0%** | **${NPV_base}** | **{Accept/Reject}** |
| Optimistic | +15% | ${NPV_optimistic} | {Accept/Reject} |
| Best Case | +30% | ${NPV_best} | {Accept/Reject} |

### Scenario Matrix

| | Low CF (-20%) | Base CF | High CF (+20%) |
|---|---|---|---|
| **Low r ({r-2}%)** | ${} | ${} | ${} |
| **Base r ({r}%)** | ${} | **${NPV_base}** | ${} |
| **High r ({r+2}%)** | ${} | ${} | ${} |

---

## Risk Considerations

### Key Assumptions & Limitations

1. **Cash flow predictability**: {High / Medium / Low}
   - Rationale: {why}
2. **Discount rate confidence**: {High / Medium / Low}
   - Rationale: {why}
3. **Terminal value dependence**: {X}% of total NPV from TV
   - Warning: if >50%, result is highly sensitive to terminal assumptions
4. **Inflation treatment**: {Real / Nominal cash flows}
5. **Currency risk**: {Applicable / Not applicable}

### Risk Flags

- [ ] Terminal value accounts for >{50}% of total NPV
- [ ] NPV turns negative with +2% discount rate increase
- [ ] Cash flow projections based on unvalidated assumptions
- [ ] Single customer/revenue source dependency
- [ ] High initial investment relative to annual cash flows

---

## Life OS Integration

### Scoring Impact (Step 5)

**How NPV feeds into MCDA scoring:**

```yaml
criteria_from_framework:
  - name: "Financial Return (NPV)"
    weight: 0.30
    score_formula: "(Project_NPV / Highest_NPV_in_Portfolio) * 10"
    rationale: "Absolute value creation measure"
  - name: "Payback Period"
    weight: 0.15
    score_formula: "10 - (Payback_Years / Max_Acceptable_Payback) * 10"
    rationale: "Liquidity and time-to-value"
  - name: "Risk-Adjusted Value"
    weight: 0.20
    score_formula: "Profitability_Index * 10"
    rationale: "Value created per dollar invested"
```

**NPV-based project ranking:**
- NPV > 0 and PI > 1.5 -> High priority
- NPV > 0 and PI 1.0-1.5 -> Medium priority
- NPV > 0 and PI < 1.0 -> Low priority (marginal)
- NPV < 0 -> Reject unless strong non-financial rationale

### Deep Plan Contribution (Step 8)

**L2 Headings Generated (NPV-based phases):**
- Phase 1: Initial Investment & Setup (Year 0)
- Phase 2: Cash Flow Ramp-Up (Year 1-2)
- Phase 3: Steady State Operations (Year 3-N)
- Phase 4: Exit / Terminal Value Realization

**L3 Tasks Generated:**
- [ ] Validate cash flow assumptions with market data
- [ ] Secure financing at or below assumed discount rate
- [ ] Establish monthly cash flow tracking vs. projections
- [ ] Set trigger points for re-evaluation (if actual CF < 80% projected)
- [ ] Plan terminal value realization (sale, refinance, perpetuity)

**Milestones:**
- Breakeven point (cumulative CF > initial investment)
- Positive NPV confirmation (Year {X} actuals vs. projections)
- Terminal value realization event

### Decision Tracking

**Key decisions made using NPV:**
1. **Decision**: {What was decided}
   - **NPV Result**: ${amount}
   - **Rationale**: {Based on NPV analysis}
   - **Trade-offs**: {What was sacrificed}
   - **Confidence**: {High / Medium / Low}

---

## Synergies with Other Finance Frameworks

### NPV + DCF
- DCF provides detailed Free Cash Flow projections -> NPV uses them as inputs
- DCF terminal value -> NPV terminal period
- Use DCF when you need full financial model; use NPV for simpler project evaluation

### NPV + Monte Carlo
- Monte Carlo converts deterministic NPV to probabilistic NPV
- Instead of single NPV number, get distribution: P10, P50, P90
- Decision rule upgrade: "P(NPV > 0) >= 70%" instead of just "NPV > 0"

### NPV + Real Options
- Traditional NPV = "now or never" decision
- Real Options = NPV + value of flexibility (delay, expand, abandon)
- Expanded NPV = Traditional NPV + Option Value
- Use Real Options when uncertainty is high and decisions can be staged

### NPV + CAPM
- CAPM provides risk-adjusted discount rate for NPV calculation
- Beta-based discount rate replaces arbitrary rate selection
- Workflow: CAPM -> discount rate -> NPV calculation

---

## Next Actions

- [ ] Gather cash flow projection data
- [ ] Select and validate discount rate
- [ ] Calculate base case NPV
- [ ] Run sensitivity analysis on 2-3 key variables
- [ ] Compare with portfolio alternatives
- [ ] Update workflow-plan.md with NPV decision
- [ ] If NPV < 0: escalate to Consilium for qualitative review

---

## Notes

{Free-form notes, data sources, comparable transactions, market research}

---

## Metadata

**Framework Version**: 1.0
**Life OS Version**: 2.0
**Template Last Updated**: 2026-02-04
**Research Source**: finance-investment-frameworks.md
**Rankings Source**: method-rankings.yaml (NPV: 24/25, Tier 1)
