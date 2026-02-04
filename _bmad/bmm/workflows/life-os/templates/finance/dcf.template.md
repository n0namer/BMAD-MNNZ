---
framework: "Discounted Cash Flow (DCF)"
framework_slug: "dcf"
domain: finance
tier: 1
score: "19/25"
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
    - "Valuation Upside"
    - "Margin Stability"
    - "Terminal Value Sensitivity"

deep_plan_contribution:
  generates_l2_headings: true
  generates_l3_tasks: true
  generates_milestones: true

linked_frameworks:
  - npv
  - capm
  - monte-carlo
prerequisite_frameworks:
  - capm  # CAPM provides cost of equity for WACC
follows_frameworks: []
---

# DCF Model - {project_name}

> **Applied to Project**: {project_name}
> **Domain**: Finance
> **Tier**: 1 (19/25 - core valuation method)
> **Completed**: {completed_date}
> **Time Invested**: {time_invested_minutes} minutes

---

## Overview

DCF (Discounted Cash Flow) - the standard valuation method for calculating intrinsic value
of a business, project, or asset based on projected future free cash flows.

**Formula:**
```
Enterprise Value = Sum [ FCF_t / (1 + WACC)^t ] + TV / (1 + WACC)^n

Where:
  FCF_t  = Free Cash Flow in period t
  WACC   = Weighted Average Cost of Capital
  TV     = Terminal Value (Gordon Growth or Exit Multiple)
  n      = Forecast period (typically 5-10 years)

Terminal Value (Gordon Growth):
  TV = FCF_n * (1 + g) / (WACC - g)

Terminal Value (Exit Multiple):
  TV = EBITDA_n * Exit_Multiple
```

**When to Use:**
- Business acquisition or investment valuation
- Real estate investment (rental properties, commercial)
- Stock valuation (fundamental analysis)
- Large capital projects (5-10+ year horizon)
- Education/certification ROI assessment

**When NOT to Use:**
- Short-term investments (<2 years)
- Speculative assets without predictable cash flows
- Early-stage startups with negative/no cash flows (use other methods)

---

## Framework Input

### 1. Company/Project Overview

- **Name**: {Company or project name}
- **Industry**: {Industry/sector}
- **Forecast Period**: {5-10 years}
- **Valuation Date**: {YYYY-MM-DD}
- **Purpose**: {M&A / Investment decision / Portfolio evaluation}

### 2. Revenue Projections

**Growth Assumptions:**
- Historical revenue CAGR (3-5 years): {X}%
- Projected growth Year 1-3: {Y}%
- Projected growth Year 4-7: {Z}% (maturation slowdown)
- Terminal growth rate: {g}% (should not exceed GDP growth, typically 2-3%)

| Year | Revenue | Growth Rate | Rationale |
|------|---------|-------------|-----------|
| Historical Avg | ${amt} | {X}% | Baseline |
| 1 | ${amt} | {Y}% | {reason} |
| 2 | ${amt} | {Y}% | {reason} |
| 3 | ${amt} | {Y}% | {reason} |
| 4 | ${amt} | {Z}% | {reason} |
| 5 | ${amt} | {Z}% | {reason} |
| 6 | ${amt} | {Z}% | {reason} |
| 7 | ${amt} | {Z}% | {reason} |

### 3. Operating Expenses & Margins

| Year | Revenue | COGS | Gross Margin | OpEx | EBIT | EBIT Margin |
|------|---------|------|-------------|------|------|-------------|
| 1 | ${amt} | ${amt} | {X}% | ${amt} | ${amt} | {Y}% |
| 2 | ${amt} | ${amt} | {X}% | ${amt} | ${amt} | {Y}% |
| 3 | ${amt} | ${amt} | {X}% | ${amt} | ${amt} | {Y}% |
| ... | ... | ... | ... | ... | ... | ... |

**Margin Assumptions:**
- Gross margin trend: {Expanding / Stable / Contracting} -- Reason: {why}
- EBIT margin target: {X}% by Year {N}
- Key cost drivers: {list}

### 4. Free Cash Flow Calculation

```
FCF = EBIT * (1 - Tax Rate) + D&A - CapEx - Change in NWC

Where:
  EBIT         = Earnings Before Interest and Taxes
  Tax Rate     = Effective tax rate
  D&A          = Depreciation & Amortization (non-cash add-back)
  CapEx        = Capital Expenditures
  Change in NWC = Change in Net Working Capital
```

| Year | EBIT | Tax ({t}%) | NOPAT | + D&A | - CapEx | - Delta NWC | **FCF** |
|------|------|------------|-------|-------|---------|-------------|---------|
| 1 | ${amt} | ${amt} | ${amt} | ${amt} | ${amt} | ${amt} | **${fcf}** |
| 2 | ${amt} | ${amt} | ${amt} | ${amt} | ${amt} | ${amt} | **${fcf}** |
| 3 | ${amt} | ${amt} | ${amt} | ${amt} | ${amt} | ${amt} | **${fcf}** |
| 4 | ${amt} | ${amt} | ${amt} | ${amt} | ${amt} | ${amt} | **${fcf}** |
| 5 | ${amt} | ${amt} | ${amt} | ${amt} | ${amt} | ${amt} | **${fcf}** |
| ... | ... | ... | ... | ... | ... | ... | ... |

**Key ratios:**
- CapEx as % of Revenue: {X}%
- D&A as % of Revenue: {Y}%
- NWC as % of Revenue: {Z}%

### 5. Discount Rate (WACC)

```
WACC = E/(E+D) * Re + D/(E+D) * Rd * (1 - Tax)

Where:
  E  = Market value of equity
  D  = Market value of debt
  Re = Cost of equity (from CAPM)
  Rd = Cost of debt (interest rate on debt)
```

| Component | Value | Source |
|-----------|-------|--------|
| Cost of Equity (Re) | {X}% | CAPM: Rf + Beta * (Rm - Rf) |
| Cost of Debt (Rd) | {Y}% | Current borrowing rate |
| Tax Rate | {Z}% | Effective rate |
| Debt / (Debt + Equity) | {D}% | Capital structure |
| Equity / (Debt + Equity) | {E}% | Capital structure |
| **WACC** | **{W}%** | **Calculated** |

**CAPM Inputs (for Cost of Equity):**
- Risk-Free Rate (Rf): {X}% (10-year Treasury)
- Market Return (Rm): {Y}% (S&P 500 historical)
- Beta: {beta} (comparable companies)
- Size premium: {Z}% (if small-cap)

### 6. Terminal Value

**Method**: {Gordon Growth / Exit Multiple}

**Gordon Growth Method:**
```
TV = FCF_n * (1 + g) / (WACC - g)
TV = ${fcf_n} * (1 + {g}%) / ({wacc}% - {g}%) = ${TV}
```

**Exit Multiple Method:**
```
TV = EBITDA_n * Exit_Multiple
TV = ${ebitda_n} * {X}x = ${TV}
```

| Method | Terminal Value | % of Enterprise Value |
|--------|--------------|----------------------|
| Gordon Growth | ${TV_gordon} | {X}% |
| Exit Multiple | ${TV_exit} | {Y}% |
| **Selected** | **${TV_selected}** | **{Z}%** |

**Warning:** If TV > 60% of Enterprise Value, result is highly sensitive to terminal assumptions.

---

## DCF Valuation

### Present Value Calculation

| Year | FCF | Discount Factor 1/(1+WACC)^t | PV of FCF |
|------|-----|------------------------------|-----------|
| 1 | ${fcf_1} | {factor} | ${pv_1} |
| 2 | ${fcf_2} | {factor} | ${pv_2} |
| 3 | ${fcf_3} | {factor} | ${pv_3} |
| 4 | ${fcf_4} | {factor} | ${pv_4} |
| 5 | ${fcf_5} | {factor} | ${pv_5} |
| ... | ... | ... | ... |
| Terminal | ${TV} | {factor} | ${pv_tv} |

### Valuation Summary

| Metric | Value |
|--------|-------|
| PV of Forecast Period FCFs | ${sum_pv_fcf} |
| PV of Terminal Value | ${pv_tv} |
| **Enterprise Value (EV)** | **${EV}** |
| Less: Net Debt | -${net_debt} |
| Plus: Non-operating assets | +${non_op} |
| **Equity Value** | **${equity_value}** |
| Shares Outstanding | {shares} |
| **Value per Share** | **${value_per_share}** |
| Current Market Price | ${current_price} |
| **Upside / Downside** | **{X}%** |

### Decision

| Criterion | Result | Interpretation |
|-----------|--------|----------------|
| DCF Value vs Price | {Above / Below / Fair} | {Undervalued / Overvalued / Fairly valued} |
| Implied IRR | {X}% | {Above / Below required return} |
| Margin of Safety | {Y}% | {Sufficient / Insufficient} |
| **Recommendation** | **{BUY / HOLD / SELL / APPROVE / REJECT}** | |

---

## Sensitivity Analysis

### WACC vs Terminal Growth Rate

| | g = 1.5% | g = 2.0% | g = 2.5% | g = 3.0% |
|---|---|---|---|---|
| **WACC = {w-2}%** | ${} | ${} | ${} | ${} |
| **WACC = {w-1}%** | ${} | ${} | ${} | ${} |
| **WACC = {w}%** | ${} | **${base}** | ${} | ${} |
| **WACC = {w+1}%** | ${} | ${} | ${} | ${} |
| **WACC = {w+2}%** | ${} | ${} | ${} | ${} |

### Revenue Growth Sensitivity

| Revenue Growth | Enterprise Value | Change from Base |
|----------------|-----------------|------------------|
| {base - 4}% | ${EV} | {X}% |
| {base - 2}% | ${EV} | {X}% |
| **{base}% (Base)** | **${EV_base}** | **0%** |
| {base + 2}% | ${EV} | {X}% |
| {base + 4}% | ${EV} | {X}% |

### EBIT Margin Sensitivity

| EBIT Margin | Enterprise Value | Change from Base |
|-------------|-----------------|------------------|
| {base - 5pp}% | ${EV} | {X}% |
| **{base}% (Base)** | **${EV_base}** | **0%** |
| {base + 5pp}% | ${EV} | {X}% |

---

## Risk Considerations

### Assumptions Log

| Assumption | Value | Confidence | Risk if Wrong |
|------------|-------|------------|---------------|
| Revenue growth | {X}% | {H/M/L} | {Impact description} |
| EBIT margin | {Y}% | {H/M/L} | {Impact description} |
| WACC | {Z}% | {H/M/L} | {Impact description} |
| Terminal growth | {g}% | {H/M/L} | {Impact description} |
| CapEx intensity | {W}% | {H/M/L} | {Impact description} |

### Risk Flags

- [ ] Terminal value > 60% of Enterprise Value (high TV dependence)
- [ ] Revenue growth exceeds industry average by >5pp
- [ ] EBIT margin assumed to expand >5pp over forecast period
- [ ] WACC below 8% (may underestimate risk)
- [ ] No comparable transactions to validate exit multiple
- [ ] Negative FCF in forecast period without clear path to positive

---

## Life OS Integration

### Scoring Impact (Step 5)

**How DCF feeds into MCDA scoring (Expected Value criterion):**

```yaml
criteria_from_framework:
  - name: "Valuation Upside"
    weight: 0.25
    score_formula: "(DCF_Value - Current_Price) / Current_Price * 10"
    rationale: "Potential return based on intrinsic value"
  - name: "Margin Stability"
    weight: 0.15
    score_formula: "EBIT_Margin_Stability_Score"
    rationale: "Predictability of cash generation"
  - name: "Terminal Value Risk"
    weight: 0.10
    score_formula: "10 - (TV_Percentage / 10)"
    rationale: "Lower TV dependence = more reliable valuation"
```

### Deep Plan Contribution (Step 8)

**L2 Headings Generated (Year-based phases):**
- Phase 1: Revenue Growth Execution (Year 1-3)
- Phase 2: Margin Expansion (Year 3-5)
- Phase 3: FCF Optimization (Year 5-N)
- Phase 4: Terminal Value Realization

**L3 Tasks Generated:**
- [ ] Build full financial model with 3 scenarios
- [ ] Validate revenue assumptions with market research
- [ ] Track quarterly actuals vs. DCF projections
- [ ] Review and update WACC annually
- [ ] Set decision gates at Year 2 and Year 5
- [ ] Plan exit strategy aligned with terminal value method

**Milestones:**
- Revenue target achieved for Year 1
- Positive FCF achieved by Year {X}
- EBIT margin reaches target {Y}% by Year {Z}
- Terminal value event (exit, IPO, refinance)

### Decision Tracking

**Key decisions made using DCF:**
1. **Decision**: {What was decided}
   - **DCF Value**: ${amount}
   - **Rationale**: {Based on valuation analysis}
   - **Trade-offs**: {What was sacrificed}
   - **Confidence**: {High / Medium / Low}

---

## Synergies with Other Finance Frameworks

### DCF + CAPM
- CAPM provides Cost of Equity -> DCF uses it in WACC
- Workflow: Calculate CAPM Re -> Calculate WACC -> Use in DCF
- Without CAPM, discount rate selection is arbitrary

### DCF + NPV
- DCF Free Cash Flows become NPV cash flow inputs
- DCF is the detailed model; NPV is the summary metric
- DCF Enterprise Value = NPV of all cash flows + terminal value

### DCF + Monte Carlo
- DCF assumptions (growth, margins, WACC) become Monte Carlo variables
- Each variable gets probability distribution instead of point estimate
- Output: Distribution of Enterprise Values instead of single number
- Decision upgrade: "P(Undervalued) = 75%" instead of "Undervalued by 15%"

### DCF + Real Options
- If DCF NPV is negative but close to zero, Real Options may reveal hidden value
- Flexibility to expand/defer/abandon adds value not captured by DCF alone
- Expanded NPV = DCF NPV + Option Value

---

## Next Actions

- [ ] Gather 3-5 years of historical financials
- [ ] Research comparable company margins and growth rates
- [ ] Calculate WACC (use CAPM template if needed)
- [ ] Build cash flow projections (3 scenarios)
- [ ] Select terminal value method and validate assumptions
- [ ] Run sensitivity analysis on WACC, growth, margins
- [ ] Compare DCF valuation to market price / asking price
- [ ] Update workflow-plan.md with valuation conclusion

---

## Notes

{Free-form notes, data sources, comparable company data, industry reports}

---

## Metadata

**Framework Version**: 1.0
**Life OS Version**: 2.0
**Template Last Updated**: 2026-02-04
**Research Source**: finance-investment-frameworks.md
**Rankings Source**: method-rankings.yaml (DCF: 19/25, Tier 1)
