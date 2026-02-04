---
framework: "Capital Asset Pricing Model (CAPM)"
framework_slug: "capm"
domain: finance
tier: 2
score: "17/25"
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
  provides_scenarios: false
  mcda_dimensions:
    - "Risk-Adjusted Return"
    - "Alpha Generation"
    - "Volatility Tolerance"

deep_plan_contribution:
  generates_l2_headings: true
  generates_l3_tasks: true
  generates_milestones: true

linked_frameworks:
  - dcf   # CAPM provides Cost of Equity for WACC
  - npv   # CAPM provides discount rate for NPV
  - monte-carlo
prerequisite_frameworks: []
follows_frameworks: []
---

# CAPM Analysis - {project_name}

> **Applied to Project**: {project_name}
> **Domain**: Finance
> **Tier**: 2 (17/25 - risk-adjusted return benchmark)
> **Completed**: {completed_date}
> **Time Invested**: {time_invested_minutes} minutes

---

## Overview

CAPM (Capital Asset Pricing Model) determines the theoretically appropriate required
rate of return for an asset based on its systematic risk (market risk that cannot be
diversified away).

**Formula:**
```
E(R_i) = R_f + Beta_i * (E(R_m) - R_f)

Where:
  E(R_i)        = Expected return on investment i
  R_f            = Risk-free rate (10-year Treasury yield)
  Beta_i         = Beta of investment i (sensitivity to market)
  E(R_m)         = Expected return of the market
  (E(R_m) - R_f) = Equity Risk Premium (ERP)
```

**Beta Interpretation:**
- Beta = 1.0: Asset moves with market (average risk)
- Beta > 1.0: More volatile than market (aggressive)
- Beta < 1.0: Less volatile than market (defensive)
- Beta < 0: Moves inversely to market (hedge)

**Key Application:** CAPM provides the discount rate (cost of equity) for DCF and NPV models.

---

## Framework Input

### 1. Market Parameters

| Parameter | Value | Source | Date |
|-----------|-------|--------|------|
| Risk-Free Rate (R_f) | {X}% | 10-year Treasury yield | {date} |
| Expected Market Return (E(R_m)) | {Y}% | S&P 500 historical/forward | {date} |
| **Equity Risk Premium** | **{ERP}%** | **E(R_m) - R_f** | |

**2026 Reference Values:**
- Risk-Free Rate: 4.0-4.5% (10-year Treasury)
- Market Return: 9.5-10.5% (historical S&P 500 average)
- Equity Risk Premium: 5.0-6.0%

**Source of market parameters:** {Bloomberg / Federal Reserve / Damodaran / Other}

### 2. Beta Estimation

**Method**: {Comparable Companies / Pure Play / Regression / Fundamental}

#### Method A: Comparable Companies (Recommended)

| Comparable Company | Industry | Beta | Source |
|-------------------|----------|------|--------|
| {Company 1} | {industry} | {beta} | {Bloomberg/Yahoo} |
| {Company 2} | {industry} | {beta} | {Bloomberg/Yahoo} |
| {Company 3} | {industry} | {beta} | {Bloomberg/Yahoo} |
| {Company 4} | {industry} | {beta} | {Bloomberg/Yahoo} |
| **Average Beta** | | **{avg_beta}** | |
| **Median Beta** | | **{med_beta}** | |

#### Method B: Regression (if historical data available)

```
Beta = Covariance(R_asset, R_market) / Variance(R_market)

  Data period: {X years} of {monthly/weekly} returns
  R-squared: {value} (how well beta explains returns)
  Standard error: {value} (precision of beta estimate)
```

#### Adjustments

| Adjustment | Value | Rationale |
|------------|-------|-----------|
| Raw Beta | {value} | From comparable analysis or regression |
| Private Company Premium | +{X} | Illiquidity discount (if private) |
| Size Premium (small-cap) | +{Y} | Higher risk for smaller companies |
| Country Premium | +{Z} | If non-US or emerging market |
| **Adjusted Beta** | **{final_beta}** | **Used in CAPM calculation** |

**Blume Adjustment (optional):**
```
Adjusted Beta = (2/3) * Raw Beta + (1/3) * 1.0
(Mean reversion toward market beta of 1.0)
```

### 3. Project/Investment Expected Return

- **Investment/Project**: {name}
- **Expected Return (from DCF/analysis)**: {X}%
- **Basis for expected return**: {DCF IRR / Historical return / Analyst estimate}

---

## CAPM Calculation

### Required Return

```
E(R_i) = R_f + Beta * (E(R_m) - R_f)
E(R_i) = {R_f}% + {Beta} * ({E(R_m)}% - {R_f}%)
E(R_i) = {R_f}% + {Beta} * {ERP}%
E(R_i) = {required_return}%
```

### Alpha (Excess Return)

```
Alpha = Expected Return - CAPM Required Return
Alpha = {expected}% - {required}% = {alpha}%
```

### Result Summary

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Risk-Free Rate (R_f) | {X}% | Guaranteed return benchmark |
| Equity Risk Premium | {ERP}% | Market compensation for risk |
| Beta | {beta} | {Aggressive / Neutral / Defensive} |
| **CAPM Required Return** | **{required}%** | **Minimum acceptable return for this risk** |
| Expected Return | {expected}% | Projected actual return |
| **Alpha** | **{alpha}%** | **{Positive = beats risk-adjusted / Negative = underperforms}** |

### Decision

| Criterion | Test | Result |
|-----------|------|--------|
| Alpha > 0? | {expected}% > {required}% | {YES / NO} |
| Sufficient alpha? | Alpha > {minimum_threshold}% | {YES / NO} |
| Beta acceptable? | {beta} < {max_beta_tolerance} | {YES / NO} |
| **Recommendation** | | **{INVEST / PASS / REVIEW}** |

**Decision Rule:**
- Alpha > 0 AND Beta acceptable -> INVEST
- Alpha > 0 BUT Beta too high -> REVIEW (risk may be excessive)
- Alpha < 0 -> PASS (can earn same return with lower risk via market index)
- Alpha ~ 0 -> INDIFFERENT (invest in market index instead)

---

## Sensitivity Analysis

### Beta Sensitivity

| Beta | Required Return | Alpha | Decision |
|------|----------------|-------|----------|
| {beta - 0.5} | {required}% | {alpha}% | {Invest/Pass} |
| {beta - 0.25} | {required}% | {alpha}% | {Invest/Pass} |
| **{beta} (Base)** | **{required}%** | **{alpha}%** | **{Invest/Pass}** |
| {beta + 0.25} | {required}% | {alpha}% | {Invest/Pass} |
| {beta + 0.5} | {required}% | {alpha}% | {Invest/Pass} |

**Breakeven Beta** (Alpha = 0): {X}

### Market Return Sensitivity

| E(R_m) | ERP | Required Return | Alpha |
|--------|-----|----------------|-------|
| {Rm - 2}% | {erp}% | {required}% | {alpha}% |
| **{Rm}% (Base)** | **{erp}%** | **{required}%** | **{alpha}%** |
| {Rm + 2}% | {erp}% | {required}% | {alpha}% |

### Risk-Free Rate Sensitivity

| R_f | Required Return | Alpha |
|-----|----------------|-------|
| {Rf - 1}% | {required}% | {alpha}% |
| **{Rf}% (Base)** | **{required}%** | **{alpha}%** |
| {Rf + 1}% | {required}% | {alpha}% |

---

## Security Market Line (SML) Position

```
Expected Return
     ^
     |         *[Project] (above SML = positive alpha)
     |       /
     |     /  <-- SML: E(R) = Rf + Beta * ERP
     |   /
     | /
  Rf +---->  Beta
     0    0.5    1.0    1.5    2.0
```

**Project position relative to SML:**
- **Above SML** (Alpha > 0): Investment earns more than risk warrants -> Attractive
- **On SML** (Alpha = 0): Investment earns exactly what risk warrants -> Fair
- **Below SML** (Alpha < 0): Investment earns less than risk warrants -> Unattractive

**This project is**: {Above / On / Below} the SML with alpha = {X}%

---

## Applications

### Application 1: Discount Rate for DCF

**CAPM Required Return -> Cost of Equity -> WACC -> DCF Discount Rate**

```
WACC = (E/(E+D)) * R_e + (D/(E+D)) * R_d * (1 - Tax)

Where R_e = CAPM Required Return = {required}%

WACC = ({E_weight}%) * {required}% + ({D_weight}%) * {R_d}% * (1 - {tax}%)
WACC = {wacc}%
```

**Use {wacc}% as discount rate in DCF template.**

### Application 2: Investment Comparison

| Investment | Beta | Required Return | Expected Return | Alpha | Rank |
|------------|------|----------------|-----------------|-------|------|
| {Investment A} | {beta} | {required}% | {expected}% | {alpha}% | {1-N} |
| {Investment B} | {beta} | {required}% | {expected}% | {alpha}% | {1-N} |
| {Investment C} | {beta} | {required}% | {expected}% | {alpha}% | {1-N} |
| Market Index | 1.00 | {Rm}% | {Rm}% | 0% | Benchmark |

**Best risk-adjusted investment**: {Investment with highest Alpha}

### Application 3: Portfolio Beta Management

**Current portfolio beta**: {current_beta}
**Target portfolio beta**: {target_beta}

```
Required allocation change:
  W_new * Beta_new + (1 - W_new) * Beta_old = Target_Beta

  Solve for W_new (weight to shift)
```

---

## Risk Considerations

### CAPM Assumptions & Limitations

1. **Efficient markets**: CAPM assumes all information is priced in
   - Reality: Markets are not perfectly efficient, especially for private assets
   - Impact: Beta may not capture all relevant risk
2. **Single-factor model**: Only systematic (market) risk is priced
   - Reality: Size, value, momentum factors also matter (Fama-French 3/5-factor model)
   - Mitigation: Add size/value premiums to adjusted beta
3. **Beta stability**: Assumes beta is constant over time
   - Reality: Beta changes with business cycle, leverage, company stage
   - Mitigation: Use 3-5 year rolling beta, adjust for current conditions
4. **Risk-free rate**: 10-year Treasury is approximation
   - Reality: Government bonds have inflation and reinvestment risk
   - Impact: Low for most practical purposes
5. **Private assets**: No traded beta for private companies/real estate
   - Mitigation: Use comparable public companies + illiquidity premium

### When CAPM Is Most Reliable

- Publicly traded assets with 5+ years of return data
- Diversified portfolios (unsystematic risk already eliminated)
- Stable, mature businesses with consistent beta
- Standard market conditions (not crisis periods)

### When CAPM Is Least Reliable

- Early-stage startups (no beta data, non-standard risk)
- Private assets (no market pricing)
- Highly leveraged investments (beta amplified, unstable)
- During market crises (correlations spike, beta unreliable)

---

## Life OS Integration

### Scoring Impact (Step 5)

**How CAPM feeds into MCDA scoring (Risk-Adjusted Impact):**

```yaml
criteria_from_framework:
  - name: "Alpha Generation"
    weight: 0.20
    score_formula: "min(10, max(0, 5 + Alpha * 20))"
    rationale: "Positive alpha = investment beats risk-adjusted benchmark"
  - name: "Risk-Adjusted Return"
    weight: 0.15
    score_formula: "Expected_Return / Beta * scaling_factor"
    rationale: "Return per unit of systematic risk (like Treynor ratio)"
  - name: "Beta Acceptability"
    weight: 0.10
    score_formula: "10 - abs(Beta - Target_Beta) * 5"
    rationale: "Penalizes deviation from investor's target risk level"
```

### Deep Plan Contribution (Step 8)

**L2 Headings Generated:**
- Risk Monitoring Framework
- Return Tracking vs. CAPM Benchmark
- Portfolio Rebalancing Schedule

**L3 Tasks Generated:**
- [ ] Calculate CAPM required return for all portfolio positions
- [ ] Identify positions with negative alpha (underperformers)
- [ ] Set quarterly review schedule: actual return vs. CAPM expected
- [ ] Monitor beta changes as business evolves
- [ ] Rebalance portfolio if overall beta deviates >0.2 from target

**Milestones:**
- Initial CAPM analysis complete (this document)
- Q1 return review vs. CAPM benchmark
- Annual beta recalculation with updated comparables
- Portfolio rebalancing event (if triggered)

### Decision Tracking

**Key decisions made using CAPM:**
1. **Decision**: {What was decided}
   - **Alpha**: {X}%
   - **Rationale**: {Investment beats/misses risk-adjusted hurdle}
   - **Trade-offs**: {Higher return vs. higher volatility}
   - **Confidence**: {High / Medium / Low}

---

## Synergies with Other Finance Frameworks

### CAPM + DCF
- **Primary integration**: CAPM Required Return -> Cost of Equity -> WACC -> DCF discount rate
- Without CAPM, discount rate selection in DCF is arbitrary
- CAPM provides theoretical basis for risk-adjusted discounting

### CAPM + NPV
- CAPM Required Return can serve directly as NPV discount rate
- For equity-funded projects: Discount rate = CAPM E(R_i)
- For mixed funding: Use WACC (which includes CAPM-derived cost of equity)

### CAPM + Monte Carlo
- Beta informs volatility parameter in Monte Carlo simulations
- If Beta = 1.5 and market sigma = 15%, asset sigma ~ 22.5%
- Monte Carlo variable: Annual return ~ Normal(CAPM_E(R), Beta * Market_sigma)

### CAPM + Kelly Criterion
- CAPM Alpha = excess return above risk-adjusted benchmark
- If Alpha > 0, Kelly Criterion can size the position optimally
- Workflow: CAPM identifies opportunity -> Kelly sizes the bet

---

## Next Actions

- [ ] Gather current market parameters (R_f, E(R_m))
- [ ] Identify 3-5 comparable companies for beta estimation
- [ ] Calculate raw and adjusted beta
- [ ] Compute CAPM required return
- [ ] Compare with expected return to determine alpha
- [ ] If CAPM used for DCF: calculate WACC and apply to DCF template
- [ ] Update workflow-plan.md with CAPM findings
- [ ] Set up quarterly return tracking vs. CAPM benchmark

---

## Notes

{Free-form notes, comparable company data, beta calculation details, market data sources}

---

## Metadata

**Framework Version**: 1.0
**Life OS Version**: 2.0
**Template Last Updated**: 2026-02-04
**Research Source**: finance-investment-frameworks.md
**Rankings Source**: method-rankings.yaml (CAPM: 17/25, Tier 2)
