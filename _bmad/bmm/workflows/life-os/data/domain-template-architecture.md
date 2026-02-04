# Domain Template Architecture for Life OS

## Overview

This document defines the unified template system for all 24 domain-specific frameworks integrated with Life OS. Each framework provides structured thinking tools that feed into Step 5 (scoring) and Step 8 (deep planning).

## Template Design Principles

### 1. Consistency Across All Frameworks
- **Uniform YAML frontmatter**: Every template uses identical metadata structure
- **Standardized sections**: Framework Input → Life OS Integration → Next Actions
- **Common integration hooks**: All templates expose scoring impact and deep plan contributions
- **Predictable file naming**: `[domain]-[framework-slug].template.md`

### 2. Framework-Specific Flexibility
- **Domain-appropriate sections**: Business templates differ from Health templates
- **Variable complexity**: Simple frameworks (SMART) vs. complex (DCF)
- **Optional sections**: Advanced features available but not required
- **Extensibility**: Custom sections can be added per framework

### 3. Life OS Integration Points
- **Step 5 Scoring**: Frameworks provide criteria, weights, or trade-off analysis
- **Step 8 Deep Planning**: Frameworks generate L2/L3 headings and action items
- **Workflow Plan Sync**: Project metadata auto-populated from workflow-plan.md
- **Decision Tracking**: Key choices recorded for project-decisions.md

### 4. Auto-Population Strategy
- **From workflow-plan.md**: project_id, project_name, dates, roles
- **From consilium output**: Specialist recommendations mapped to framework inputs
- **From scoring step**: MCDA criteria pre-filled into relevant frameworks
- **From calendar sync**: Time estimates for Pomodoro/GTD templates

---

## Universal Template Structure

Every framework template follows this base structure:

```yaml
---
# === METADATA (Auto-populated from workflow plan) ===
framework: "[Framework Name]"
framework_slug: "[kebab-case-name]"
domain: "[business|finance|health|personal|universal]"
applied_to_project: "[project_id from workflow-plan.md]"
project_name: "[Auto-filled]"
created_date: "[YYYY-MM-DD]"
completed_date: "[YYYY-MM-DD or null]"

# === INTEGRATION HOOKS ===
integration_step: "[1-consilium|4-pre-scoring|5-scoring|8-deep-plan]"
time_invested_minutes: 0
consilium_specialist: "[Matched from step-04-consilium.md if applicable]"

# === SCORING IMPACT ===
scoring_contribution:
  provides_criteria: [true|false]
  provides_weights: [true|false]
  provides_scenarios: [true|false]
  mcda_dimensions: ["Dimension 1", "Dimension 2", ...]

# === DEEP PLAN IMPACT ===
deep_plan_contribution:
  generates_l2_headings: [true|false]
  generates_l3_tasks: [true|false]
  generates_milestones: [true|false]

# === COMPOSITION ===
linked_frameworks: []  # Auto-populated based on composition patterns
prerequisite_frameworks: []
follows_frameworks: []
---

# [Framework Name] - {{project_name}}

> **Applied to Project**: {{project_name}}
> **Domain**: {{domain}}
> **Completed**: {{completed_date}}
> **Time Invested**: {{time_invested_minutes}} minutes

---

## Framework Input

[Framework-specific sections here - varies by template]

---

## Life OS Integration

### Scoring Impact (Step 5)

**How this framework affects MCDA scoring:**
- [Specific criteria or weights generated]
- [Trade-offs identified]
- [Scenarios defined]

**Auto-population for scoring step:**
```yaml
# This data feeds into step-05-scoring.md
criteria_from_framework:
  - name: "[Criterion 1]"
    weight: [0.0-1.0]
    rationale: "[Why this matters]"
```

### Deep Plan Contribution (Step 8)

**L2 Headings Generated:**
- [Major phase/section from framework]
- [Another major section]

**L3 Tasks Generated:**
- [Specific action item 1]
- [Specific action item 2]

**Milestones Identified:**
- [Key checkpoint 1]
- [Key checkpoint 2]

### Decision Tracking

**Key decisions made using this framework:**
1. **Decision**: [What was decided]
   - **Rationale**: [Why, based on framework analysis]
   - **Trade-offs**: [What was sacrificed]
   - **Confidence**: [High|Medium|Low]

---

## Next Actions

- [ ] [Action item 1 from framework analysis]
- [ ] [Action item 2]
- [ ] [Action item 3]

---

## Notes

[Free-form notes, observations, or context]

---

## Metadata

**Framework Version**: 1.0
**Life OS Version**: 2.0
**Template Last Updated**: 2026-02-04
```

---

## Framework-Specific Templates Specification

### Business Domain (6 Frameworks)

#### 1. Business Model Canvas (`templates/business-model-canvas.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### 1. Customer Segments
[Who are we creating value for? Who are our most important customers?]

### 2. Value Propositions
[What value do we deliver to customers? Which problems are we solving?]

### 3. Channels
[How do we reach and communicate with customer segments?]

### 4. Customer Relationships
[What relationships do we establish and maintain with each segment?]

### 5. Revenue Streams
[For what value are customers willing to pay? How are they paying now?]

### 6. Key Resources
[What key resources do our value propositions require?]

### 7. Key Activities
[What key activities do our value propositions require?]

### 8. Key Partnerships
[Who are our key partners and suppliers?]

### 9. Cost Structure
[What are the most important costs in our business model?]
```

**Scoring Contribution:**
- Generates criteria: Revenue Potential, Customer Reach, Resource Efficiency
- Provides weights: Based on which canvas blocks are most critical

**Deep Plan Contribution:**
- L2 headings: "Customer Acquisition", "Value Delivery", "Revenue Generation", "Cost Management"
- L3 tasks: Specific actions from each of 9 blocks

**Auto-linking:**
- Links to: Value Proposition Canvas (VPC), SWOT Analysis
- VPC "Customer Jobs" ← BMC "Customer Segments"
- SWOT "Opportunities" ← BMC "Customer Segments" + "Channels"

---

#### 2. OKR Framework (`templates/okr-framework.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### Objective
[Qualitative, inspiring goal - What do we want to achieve?]

**Time Horizon**: [Quarter|Year|Multi-year]
**Aligned With**: [Higher-level OKR or strategic goal]

### Key Results (3-5 measurable outcomes)

#### Key Result 1
- **Metric**: [What we're measuring]
- **Baseline**: [Current state: X]
- **Target**: [Desired state: Y]
- **Measurement Frequency**: [Daily|Weekly|Monthly]
- **Owner**: [Person/role responsible]

#### Key Result 2
[Same structure]

#### Key Result 3
[Same structure]

### Initiatives (Actions to achieve KRs)
- [ ] Initiative 1 → Contributes to KR1
- [ ] Initiative 2 → Contributes to KR2, KR3
- [ ] Initiative 3 → Contributes to KR1, KR3
```

**Scoring Contribution:**
- Generates criteria: KR achievement likelihood, resource requirements
- Provides weights: Equal weight per KR (or custom if strategic priority differs)

**Deep Plan Contribution:**
- L2 headings: Each Key Result becomes a major phase
- L3 tasks: Initiatives mapped to specific weeks/sprints
- Milestones: 25%, 50%, 75%, 100% achievement points per KR

**Auto-linking:**
- Links to: SMART Goals, GTD (initiatives → Next Actions)
- GTD "Projects" ← OKR "Initiatives"

---

#### 3. SWOT Analysis (`templates/swot-analysis.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### Strengths (Internal, Positive)
1. [Strength 1]
   - Evidence: [Why this is true]
   - Leverage: [How to capitalize on this]
2. [Strength 2]

### Weaknesses (Internal, Negative)
1. [Weakness 1]
   - Evidence: [Why this is a problem]
   - Mitigation: [How to address this]
2. [Weakness 2]

### Opportunities (External, Positive)
1. [Opportunity 1]
   - Timeframe: [When is this window open?]
   - Requirements: [What's needed to seize this?]
2. [Opportunity 2]

### Threats (External, Negative)
1. [Threat 1]
   - Probability: [High|Medium|Low]
   - Impact: [High|Medium|Low]
   - Response: [How to mitigate]
2. [Threat 2]

### SWOT Matrix (SO, ST, WO, WT Strategies)

#### SO Strategies (Leverage Strengths to Capture Opportunities)
- [Strategy 1]

#### ST Strategies (Use Strengths to Mitigate Threats)
- [Strategy 1]

#### WO Strategies (Overcome Weaknesses to Pursue Opportunities)
- [Strategy 1]

#### WT Strategies (Minimize Weaknesses and Avoid Threats)
- [Strategy 1]
```

**Scoring Contribution:**
- Generates scenarios: Best case (SO), Worst case (WT), Mixed (ST, WO)
- Provides risk weights: Threat probability × impact

**Deep Plan Contribution:**
- L2 headings: "Capitalize on Strengths", "Address Weaknesses", "Seize Opportunities", "Mitigate Threats"
- L3 tasks: Each strategy becomes action items

**Auto-linking:**
- Links to: Business Model Canvas, Porter's Five Forces
- BMC "Key Resources" ← SWOT "Strengths"
- Porter's "Threat of New Entrants" ← SWOT "Threats"

---

#### 4. Lean Canvas (`templates/lean-canvas.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### 1. Problem (Top 3)
1. [Problem 1]
2. [Problem 2]
3. [Problem 3]

**Existing Alternatives**: [How do customers solve this today?]

### 2. Customer Segments
- **Early Adopters**: [Who will try this first?]
- **Target Segment**: [Who is the ideal customer?]

### 3. Unique Value Proposition
[Single, clear, compelling message - Why are you different and worth buying?]

**High-Level Concept**: [X for Y analogy]

### 4. Solution (Top 3)
1. [Solution to Problem 1]
2. [Solution to Problem 2]
3. [Solution to Problem 3]

### 5. Channels
- **Path to Customers**: [How will you reach them?]
- **Inbound**: [How they find you]
- **Outbound**: [How you reach them]

### 6. Revenue Streams
- **Revenue Model**: [Subscription|Transaction|Advertising|Licensing|etc.]
- **Lifetime Value**: [Estimate]

### 7. Cost Structure
- **Customer Acquisition Cost**: [Estimate]
- **Distribution Costs**: [Estimate]
- **Hosting/Infrastructure**: [Estimate]
- **People**: [Estimate]

### 8. Key Metrics
- [Metric 1 that measures progress]
- [Metric 2]
- [Metric 3]

### 9. Unfair Advantage
[What can't be easily copied or bought?]
```

**Scoring Contribution:**
- Generates criteria: Problem-Solution Fit, UVP Clarity, Cost Efficiency
- Provides weights: Higher weight to UVP and Unfair Advantage

**Deep Plan Contribution:**
- L2 headings: "MVP Development", "Customer Discovery", "Channel Testing"
- L3 tasks: Validation experiments per section

**Auto-linking:**
- Links to: Business Model Canvas, Value Proposition Canvas
- BMC "Customer Segments" ↔ Lean Canvas "Customer Segments"
- VPC "Pains" ← Lean Canvas "Problem"

---

#### 5. Value Proposition Canvas (`templates/value-proposition-canvas.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### Customer Profile (Right Side)

#### Customer Jobs
1. [Functional job - What tasks are they trying to complete?]
2. [Social job - How do they want to be perceived?]
3. [Emotional job - How do they want to feel?]

#### Pains (Things that annoy customers)
1. [Pain 1] - **Severity**: [Extreme|High|Moderate|Low]
2. [Pain 2]
3. [Pain 3]

#### Gains (Outcomes and benefits customers want)
1. [Gain 1] - **Importance**: [Critical|High|Nice-to-have]
2. [Gain 2]
3. [Gain 3]

### Value Map (Left Side)

#### Products & Services
1. [Product/service 1]
2. [Product/service 2]

#### Pain Relievers (How products alleviate pains)
1. [Reliever 1] → Addresses [Pain X]
2. [Reliever 2] → Addresses [Pain Y]

#### Gain Creators (How products create gains)
1. [Creator 1] → Delivers [Gain X]
2. [Creator 2] → Delivers [Gain Y]

### Fit Analysis

**Pain-Reliever Fit**:
- ✓ [Well-matched pain-reliever pair]
- ⚠ [Weak match that needs work]

**Gain-Creator Fit**:
- ✓ [Well-matched gain-creator pair]
- ⚠ [Weak match that needs work]

**Gaps**:
- [Unaddressed pain]
- [Undelivered gain]
```

**Scoring Contribution:**
- Generates criteria: Pain-Relief Effectiveness, Gain Creation Strength, Customer Job Alignment
- Provides weights: Based on pain severity and gain importance

**Deep Plan Contribution:**
- L2 headings: "Address Critical Pains", "Deliver Key Gains", "Validate Customer Jobs"
- L3 tasks: Specific pain relievers and gain creators to build

**Auto-linking:**
- Links to: Business Model Canvas, Lean Canvas
- Lean Canvas "Problem" ← VPC "Pains"
- BMC "Value Propositions" ← VPC "Pain Relievers" + "Gain Creators"

---

#### 6. Porter's Five Forces (`templates/porters-five-forces.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### 1. Threat of New Entrants
**Overall Threat Level**: [High|Medium|Low]

**Barriers to Entry**:
- Capital requirements: [Assessment]
- Economies of scale: [Assessment]
- Brand loyalty: [Assessment]
- Regulatory barriers: [Assessment]
- Access to distribution: [Assessment]

**Analysis**: [Why this threat level?]

### 2. Bargaining Power of Suppliers
**Overall Power Level**: [High|Medium|Low]

**Factors**:
- Supplier concentration: [Assessment]
- Switching costs: [Assessment]
- Substitute inputs available: [Assessment]
- Forward integration threat: [Assessment]

**Analysis**: [Why this power level?]

### 3. Bargaining Power of Buyers
**Overall Power Level**: [High|Medium|Low]

**Factors**:
- Buyer concentration: [Assessment]
- Switching costs: [Assessment]
- Price sensitivity: [Assessment]
- Backward integration threat: [Assessment]

**Analysis**: [Why this power level?]

### 4. Threat of Substitute Products
**Overall Threat Level**: [High|Medium|Low]

**Substitutes Identified**:
1. [Substitute 1] - Performance vs. price: [Assessment]
2. [Substitute 2]

**Analysis**: [Why this threat level?]

### 5. Competitive Rivalry
**Overall Intensity**: [High|Medium|Low]

**Factors**:
- Number of competitors: [Assessment]
- Industry growth rate: [Assessment]
- Product differentiation: [Assessment]
- Exit barriers: [Assessment]

**Analysis**: [Why this intensity?]

### Strategic Implications

**Most Significant Force**: [Which of the 5 is most important?]

**Defensive Strategies**:
- [Strategy to address force 1]
- [Strategy to address force 2]

**Offensive Opportunities**:
- [How to exploit weak forces]
```

**Scoring Contribution:**
- Generates criteria: Competitive Advantage Sustainability, Market Entry Risk
- Provides weights: Highest weight to most significant force

**Deep Plan Contribution:**
- L2 headings: "Build Entry Barriers", "Reduce Supplier Dependence", "Differentiate from Rivals"
- L3 tasks: Defensive and offensive strategies

**Auto-linking:**
- Links to: SWOT Analysis, Business Model Canvas
- SWOT "Threats" ← Porter's "Threat of New Entrants" + "Competitive Rivalry"
- BMC "Key Partnerships" → Response to "Bargaining Power of Suppliers"

---

### Finance Domain (6 Frameworks)

#### 7. Net Present Value (NPV) (`templates/npv-analysis.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### Investment Details
- **Initial Investment (Year 0)**: $[amount]
- **Project Lifespan**: [N years]
- **Discount Rate**: [X]% (WACC or required rate of return)

### Cash Flow Projections

| Year | Cash Inflow | Cash Outflow | Net Cash Flow |
|------|-------------|--------------|---------------|
| 0    | $0          | $[initial]   | -$[initial]   |
| 1    | $[amount]   | $[amount]    | $[net]        |
| 2    | $[amount]   | $[amount]    | $[net]        |
| ...  | ...         | ...          | ...           |
| N    | $[amount]   | $[amount]    | $[net]        |

### Discount Factor Calculation

| Year | Net Cash Flow | Discount Factor (1/(1+r)^n) | Present Value |
|------|---------------|------------------------------|---------------|
| 0    | -$[initial]   | 1.000                        | -$[initial]   |
| 1    | $[net]        | [factor]                     | $[pv]         |
| 2    | $[net]        | [factor]                     | $[pv]         |
| ...  | ...           | ...                          | ...           |
| N    | $[net]        | [factor]                     | $[pv]         |

**Total NPV**: $[sum of PV column]

### Decision Criteria
- **NPV > 0**: Accept project (creates value)
- **NPV < 0**: Reject project (destroys value)
- **NPV = 0**: Indifferent

**Decision**: [Accept|Reject|Indifferent]

### Sensitivity Analysis

**What if discount rate changes?**
- At [r-2]%: NPV = $[amount]
- At [r]%: NPV = $[amount]
- At [r+2]%: NPV = $[amount]

**What if cash flows are 20% lower?**
- NPV = $[amount]
```

**Scoring Contribution:**
- Generates criteria: Financial Return, Payback Period, Risk-Adjusted Value
- Provides weights: NPV magnitude relative to investment

**Deep Plan Contribution:**
- L2 headings: "Year 1 Milestones", "Year 2 Milestones", ...
- L3 tasks: Actions needed to achieve projected cash flows
- Milestones: Breakeven point, positive NPV confirmation

**Auto-linking:**
- Links to: DCF Model, Monte Carlo Simulation
- DCF "Terminal Value" → NPV final year projections
- Monte Carlo "Scenarios" → NPV sensitivity analysis

---

#### 8. Discounted Cash Flow (DCF) (`templates/dcf-model.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### Company/Project Overview
- **Name**: [Company or project name]
- **Industry**: [Industry]
- **Forecast Period**: [5-10 years typical]

### Revenue Projections

| Year | Revenue | Growth Rate | Notes |
|------|---------|-------------|-------|
| 1    | $[amt]  | [%]         | [Assumptions] |
| 2    | $[amt]  | [%]         | |
| ...  | ...     | ...         | |

### Operating Expenses & Margins

| Year | COGS | Operating Expenses | EBIT | EBIT Margin |
|------|------|--------------------|------|-------------|
| 1    | $[amt] | $[amt]           | $[amt] | [%] |
| ...  | ...  | ...                | ...  | ... |

### Free Cash Flow Calculation

| Year | EBIT | Tax | NOPAT | + D&A | - CapEx | - Δ NWC | FCF |
|------|------|-----|-------|-------|---------|---------|-----|
| 1    | $[amt] | $[amt] | $[amt] | $[amt] | $[amt] | $[amt] | $[amt] |
| ...  | ...  | ... | ...   | ...   | ...     | ...     | ... |

### Terminal Value
- **Method**: [Gordon Growth|Exit Multiple]
- **Perpetual Growth Rate**: [%] (if Gordon Growth)
- **Exit Multiple**: [X]x EBITDA (if Exit Multiple)
- **Terminal Value (Year N)**: $[amount]

### Discount Rate (WACC)
- **Cost of Equity**: [%]
- **Cost of Debt**: [%]
- **Tax Rate**: [%]
- **Debt/Equity Ratio**: [%]
- **WACC**: [%]

### Valuation

| Year | FCF | Discount Factor | PV of FCF |
|------|-----|-----------------|-----------|
| 1    | $[amt] | [factor]     | $[pv]     |
| ...  | ...  | ...            | ...       |
| N    | $[amt] | [factor]     | $[pv]     |
| Terminal | $[tv] | [factor] | $[pv_tv]  |

**Enterprise Value**: $[sum of PV column]
**Less: Net Debt**: $[amount]
**Equity Value**: $[EV - Net Debt]
**Shares Outstanding**: [number]
**Value per Share**: $[Equity Value / Shares]
```

**Scoring Contribution:**
- Generates criteria: Valuation Upside, Margin Stability, Terminal Value Sensitivity
- Provides weights: Higher weight if DCF is primary valuation method

**Deep Plan Contribution:**
- L2 headings: "Revenue Growth Phase", "Margin Expansion Phase", "FCF Optimization"
- L3 tasks: Operational initiatives to hit projections
- Milestones: Revenue targets, margin targets, FCF breakeven

**Auto-linking:**
- Links to: NPV Analysis, Monte Carlo Simulation
- NPV cash flows ← DCF Free Cash Flows
- Monte Carlo inputs ← DCF assumptions (revenue growth, margins)

---

#### 9. Monte Carlo Simulation (`templates/monte-carlo-simulation.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### Variables to Simulate
1. **Variable 1**: [e.g., Revenue Growth Rate]
   - Distribution: [Normal|Lognormal|Uniform|Triangular]
   - Mean: [value]
   - Std Dev / Range: [value]
   - Rationale: [Why this distribution?]

2. **Variable 2**: [e.g., Operating Margin]
   - Distribution: [type]
   - Parameters: [...]
   - Rationale: [...]

[Add all uncertain variables]

### Correlations
- **Variable 1 ↔ Variable 2**: Correlation = [value]
  - Rationale: [Why are these correlated?]

### Output Metric
- **Metric**: [e.g., NPV, ROI, Payback Period]
- **Calculated as**: [Formula]

### Simulation Parameters
- **Number of Iterations**: [10,000 typical]
- **Random Seed**: [value for reproducibility]

### Results

#### Distribution of [Output Metric]
- **Mean**: $[value]
- **Median**: $[value]
- **Std Deviation**: $[value]
- **Min**: $[value]
- **Max**: $[value]

#### Percentiles
- **10th percentile**: $[value] (Pessimistic)
- **50th percentile**: $[value] (Expected)
- **90th percentile**: $[value] (Optimistic)

#### Probability of Success
- **P([Metric] > $[threshold])**: [%]
- **P([Metric] < $0)**: [%] (Risk of loss)

### Sensitivity Analysis
**Which variables drive the most uncertainty?**
- [Variable X]: Explains [%]% of output variance
- [Variable Y]: Explains [%]% of output variance

### Scenario Planning
- **Base Case (50th percentile)**: [Outcome]
- **Bear Case (10th percentile)**: [Outcome]
- **Bull Case (90th percentile)**: [Outcome]
```

**Scoring Contribution:**
- Generates scenarios: Bear, Base, Bull cases with probabilities
- Provides risk weights: Probability of failure, downside risk

**Deep Plan Contribution:**
- L2 headings: "Risk Mitigation for [Top Risk Variable]", "Upside Capture for [Top Opportunity Variable]"
- L3 tasks: Actions to reduce variance in key variables
- Milestones: Checkpoints to validate assumptions

**Auto-linking:**
- Links to: NPV, DCF, Real Options
- NPV "Sensitivity Analysis" ← Monte Carlo distributions
- DCF assumptions → Monte Carlo variables

---

#### 10. Real Options Analysis (`templates/real-options.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### Investment Opportunity
- **Description**: [What is the investment?]
- **Traditional NPV (now or never)**: $[amount]
- **Decision**: [Accept if NPV > 0, but...]

### Option to Delay
- **Wait Period**: [X months/years]
- **Information Gained**: [What will we learn by waiting?]
- **Cost of Waiting**: [Opportunity cost, competitive risk]
- **Value of Delay Option**: $[calculated using option pricing model]

### Option to Expand
- **Initial Investment**: $[amount]
- **Expansion Investment**: $[additional amount later]
- **Trigger**: [Conditions that justify expansion]
- **Expansion NPV (if triggered)**: $[amount]
- **Value of Expansion Option**: $[amount]

### Option to Abandon
- **Salvage Value**: $[amount] (if we exit early)
- **Trigger**: [Conditions that justify exit]
- **Loss Avoided**: $[amount]
- **Value of Abandonment Option**: $[amount]

### Option to Switch
- **Alternative Use**: [What else could we do with these assets?]
- **Switching Cost**: $[amount]
- **Value if Switched**: $[amount]
- **Value of Switching Option**: $[amount]

### Option Tree
```
[Decision Tree Diagram - ASCII or link to visual]

Year 0: Invest $[X] or Wait
  ├─ Invest Now
  │   ├─ Success (P=[%]): NPV = $[Y]
  │   └─ Failure (P=[%]): NPV = -$[Z]
  └─ Wait 1 Year
      ├─ Information Positive: Invest then (NPV = $[Y2])
      └─ Information Negative: Don't invest (NPV = $0)
```

### Total Value with Options
- **Traditional NPV**: $[amount]
- **+ Value of Delay**: $[amount]
- **+ Value of Expansion**: $[amount]
- **+ Value of Abandonment**: $[amount]
- **+ Value of Switching**: $[amount]
- **= Expanded NPV**: $[total]

**Decision with Real Options**: [Accept|Reject|Wait]
```

**Scoring Contribution:**
- Generates criteria: Flexibility Value, Irreversibility Risk, Learning Value
- Provides weights: Higher weight if uncertainty is high

**Deep Plan Contribution:**
- L2 headings: "Phase 1 (Initial Investment)", "Decision Point (Expand/Abandon/Switch)"
- L3 tasks: Information-gathering activities to inform option exercise
- Milestones: Option decision dates

**Auto-linking:**
- Links to: NPV, Monte Carlo, DCF
- Monte Carlo scenarios → Real Options triggers
- NPV "Sensitivity" → Real Options value drivers

---

#### 11. Capital Asset Pricing Model (CAPM) (`templates/capm-analysis.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### Required Inputs
- **Risk-Free Rate (Rf)**: [%] (e.g., 10-year Treasury yield)
- **Market Return (Rm)**: [%] (e.g., S&P 500 historical average)
- **Beta (β)**: [value] (Asset's systematic risk)

### Beta Calculation (if not provided)
- **Covariance(Asset, Market)**: [value]
- **Variance(Market)**: [value]
- **Beta = Cov / Var**: [calculated]

### Expected Return Calculation
**Formula**: E(R) = Rf + β × (Rm - Rf)

- **Risk-Free Rate**: [%]
- **Market Risk Premium (Rm - Rf)**: [%]
- **Beta**: [value]
- **Expected Return**: [%]

### Interpretation
- **If β > 1**: Asset is [%]% more volatile than market (aggressive)
- **If β = 1**: Asset moves with market (neutral)
- **If β < 1**: Asset is [%]% less volatile than market (defensive)

**This asset's beta ([value]) means**: [Interpretation]

### Application to Project
- **Project/Investment**: [Name]
- **Required Return (from CAPM)**: [%]
- **Actual Expected Return**: [%]
- **Decision**: [Invest if Actual > Required]
```

**Scoring Contribution:**
- Generates criteria: Risk-Adjusted Return, Volatility Tolerance
- Provides weights: Beta influences risk dimension weight

**Deep Plan Contribution:**
- L2 headings: "Risk Monitoring", "Return Tracking"
- L3 tasks: Hedge strategies if beta too high
- Milestones: Quarterly return reviews vs. CAPM expectation

**Auto-linking:**
- Links to: NPV (provides discount rate), DCF (cost of equity input)
- DCF "Cost of Equity" ← CAPM Expected Return
- NPV "Discount Rate" ← CAPM Expected Return (for equity projects)

---

#### 12. Kelly Criterion (`templates/kelly-criterion.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### Bet/Investment Details
- **Win Probability (p)**: [%] (e.g., 55%)
- **Loss Probability (q)**: [%] (= 1 - p)
- **Win Payoff (b)**: [ratio] (e.g., win $2 for every $1 bet)
- **Loss Amount**: $1 (standard)

### Kelly Formula
**f* = (bp - q) / b**

Where:
- f* = Optimal fraction of capital to bet
- b = Odds received on the bet
- p = Probability of winning
- q = Probability of losing (1-p)

### Calculation
- **Numerator (bp - q)**: [value]
- **Denominator (b)**: [value]
- **Kelly %**: [result]%

### Interpretation
- **If Kelly % > 0**: Favorable bet, allocate [%]% of capital
- **If Kelly % = 0**: Break-even, don't bet
- **If Kelly % < 0**: Unfavorable bet, avoid (or bet against)

**Recommendation**: Allocate [X]% of capital to this opportunity

### Fractional Kelly (Conservative Approach)
- **Half Kelly**: [Kelly%/2]% (reduces risk of overbetting)
- **Quarter Kelly**: [Kelly%/4]% (very conservative)

**Conservative Recommendation**: Allocate [X]% (Half Kelly)

### Portfolio Application
If applied to project portfolio:
- **Total Budget**: $[amount]
- **Kelly Allocation**: $[Kelly% × Budget]
- **Fractional Kelly Allocation**: $[Fractional% × Budget]
```

**Scoring Contribution:**
- Generates criteria: Optimal Allocation, Risk of Ruin
- Provides weights: Kelly% influences resource allocation

**Deep Plan Contribution:**
- L2 headings: "Staged Investment", "Risk Management"
- L3 tasks: Incremental funding decisions
- Milestones: Review points to recalculate Kelly% as probabilities update

**Auto-linking:**
- Links to: Monte Carlo (probability estimates), Real Options (staged investment)
- Monte Carlo "P(Success)" → Kelly "Win Probability"
- Real Options "Option to Expand" ← Kelly "Fractional allocation then reassess"

---

### Health Domain (6 Frameworks)

#### 13. Health Belief Model (HBM) (`templates/health-belief-model.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### 1. Perceived Susceptibility
**How likely am I to experience this health issue?**
- [Assessment of personal risk]
- Evidence: [Why I believe this]

**Rating**: [Low|Medium|High]

### 2. Perceived Severity
**How serious would the consequences be?**
- [Impact on health, life, work, relationships]
- Evidence: [Why I believe this]

**Rating**: [Low|Medium|High]

### 3. Perceived Benefits
**What are the benefits of taking action?**
- Benefit 1: [Specific outcome]
- Benefit 2: [Specific outcome]
- Evidence: [Research, testimonials, logic]

**Rating**: [Low|Medium|High]

### 4. Perceived Barriers
**What obstacles prevent me from taking action?**
- Barrier 1: [e.g., Cost, time, discomfort]
- Barrier 2: [e.g., Lack of knowledge, access]
- Evidence: [Why these are real barriers]

**Rating**: [Low|Medium|High]

### 5. Cues to Action
**What triggers will prompt me to act?**
- Internal cue: [e.g., Pain, symptoms, fear]
- External cue: [e.g., Doctor recommendation, friend's experience]
- Environmental cue: [e.g., Reminder, app notification]

### 6. Self-Efficacy
**Do I believe I can successfully take this action?**
- Past success: [Have I done this before?]
- Support available: [Who/what will help?]
- Skills/resources: [Do I have what I need?]

**Rating**: [Low|Medium|High]

### HBM Decision Matrix

| Factor | Rating | Weight | Score |
|--------|--------|--------|-------|
| Susceptibility | [H/M/L] | [%] | [W×R] |
| Severity | [H/M/L] | [%] | [W×R] |
| Benefits | [H/M/L] | [%] | [W×R] |
| Barriers (inverse) | [H/M/L] | [%] | [W×R] |
| Cues | [H/M/L] | [%] | [W×R] |
| Self-Efficacy | [H/M/L] | [%] | [W×R] |
| **Total** | | | [Sum] |

**Decision**:
- Score > [threshold]: High likelihood of action
- Score < [threshold]: Need to increase benefits, reduce barriers, or boost self-efficacy
```

**Scoring Contribution:**
- Generates criteria: Health Impact, Feasibility, Self-Efficacy
- Provides weights: Based on HBM construct ratings

**Deep Plan Contribution:**
- L2 headings: "Increase Awareness (Susceptibility/Severity)", "Reduce Barriers", "Build Self-Efficacy"
- L3 tasks: Specific actions per construct (e.g., "Find affordable gym" → Reduce barrier)
- Milestones: Construct rating improvements

**Auto-linking:**
- Links to: SMART Goals, Habit Loop
- SMART "Achievable" ← HBM "Self-Efficacy"
- Habit Loop "Cue" ← HBM "Cues to Action"

---

#### 14. SMART Goals (`templates/smart-goals.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### Goal Statement
[Original goal in free-form]

### SMART Criteria

#### S - Specific
**What exactly will I accomplish?**
- Who: [Who is involved?]
- What: [What do I want to accomplish?]
- Where: [Where will this happen?]
- Why: [Why is this important?]

**Specific Goal**: [Rewritten specific version]

#### M - Measurable
**How will I know when it's accomplished?**
- Metric 1: [Quantifiable measure]
- Metric 2: [Quantifiable measure]
- Tracking method: [How will I measure?]

**Measurable Target**: [X by Y date]

#### A - Achievable
**Is this goal realistic given my resources and constraints?**
- Resources available: [Time, money, skills, support]
- Obstacles: [What might prevent this?]
- Plan to overcome: [How to address obstacles]

**Achievability Assessment**: [High|Medium|Low] - [Rationale]

#### R - Relevant
**Why does this goal matter?**
- Aligns with: [Larger objective, value, or project]
- Impact: [What difference will this make?]
- Priority: [High|Medium|Low]

**Relevance Statement**: [Why this goal is worth pursuing]

#### T - Time-bound
**When will I achieve this?**
- Start date: [YYYY-MM-DD]
- End date: [YYYY-MM-DD]
- Milestones:
  - [Date]: [Milestone 1]
  - [Date]: [Milestone 2]

**Deadline**: [Final date with consequence if missed]

### Final SMART Goal
[Rewritten goal incorporating all 5 criteria in one sentence]

**Example**: "I will [Measurable target] by [Time-bound date] by [Specific actions] to [Relevant outcome]."

### Action Plan
- [ ] Step 1: [First action] - Due: [Date]
- [ ] Step 2: [Second action] - Due: [Date]
- [ ] Step 3: [Third action] - Due: [Date]
```

**Scoring Contribution:**
- Generates criteria: Goal Clarity, Achievability, Timeline Feasibility
- Provides weights: Higher weight if goal is critical to project success

**Deep Plan Contribution:**
- L2 headings: Each major milestone becomes L2
- L3 tasks: Action plan steps
- Milestones: Time-bound checkpoints

**Auto-linking:**
- Links to: OKRs (SMART goals as Key Results), GTD (Action plan → Next Actions)
- OKR "Key Results" ← SMART "Measurable + Time-bound"
- GTD "Projects" ← SMART "Action Plan"

---

#### 15. Habit Loop (`templates/habit-loop.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### Desired Habit
**What habit do I want to build?**
- [Clear description]

**Frequency**: [Daily|Weekly|Specific schedule]

### Habit Loop Components

#### 1. Cue (Trigger)
**What will remind me to do this habit?**
- **Type**: [Time|Location|Preceding event|Emotional state|Other people]
- **Specific Cue**: [Exact trigger description]
- **Examples**:
  - Time: "Every day at 7:00 AM"
  - Location: "When I enter my home office"
  - Event: "Right after I finish breakfast"

**My Cue**: [Chosen trigger]

#### 2. Routine (Behavior)
**What is the actual behavior?**
- **Action**: [Step-by-step description]
- **Duration**: [How long?]
- **Environment**: [Where does this happen?]

**My Routine**: [Detailed behavior]

#### 3. Reward (Benefit)
**What benefit do I get immediately after?**
- **Type**: [Intrinsic (internal satisfaction)|Extrinsic (external reward)]
- **Specific Reward**: [What feels good?]
- **Examples**:
  - Intrinsic: "Sense of accomplishment"
  - Extrinsic: "Check off my tracker"

**My Reward**: [Chosen reward]

### Habit Stacking (Optional)
**Can I attach this to an existing habit?**
- Existing habit: [Something I already do consistently]
- New habit: [Habit I'm building]
- Formula: "After I [existing habit], I will [new habit]."

**My Stack**: After I [X], I will [Y].

### Habit Tracking
- **Start Date**: [YYYY-MM-DD]
- **Tracking Method**: [App|Paper calendar|Streak counter]
- **Minimum Viable Habit**: [Smallest version if I'm struggling]

| Date | Cue Present? | Routine Done? | Reward Given? | Notes |
|------|--------------|---------------|---------------|-------|
| [Date] | ✓/✗ | ✓/✗ | ✓/✗ | [Any observations] |

### Troubleshooting
**If the habit isn't sticking:**
- Is the cue obvious enough? [Yes|No] - [Adjust how?]
- Is the routine too hard? [Yes|No] - [Simplify how?]
- Is the reward satisfying? [Yes|No] - [Change to what?]
```

**Scoring Contribution:**
- Generates criteria: Habit Sustainability, Cue Reliability, Reward Effectiveness
- Provides weights: Higher weight if habit is foundational to project execution

**Deep Plan Contribution:**
- L2 headings: "Establish Habit", "Track Consistency", "Optimize Loop"
- L3 tasks: Weekly habit reviews, cue/reward adjustments
- Milestones: 7-day streak, 30-day streak, 90-day streak

**Auto-linking:**
- Links to: Atomic Habits, Pomodoro Technique
- Atomic Habits "Implementation Intention" ← Habit Loop "Cue"
- Pomodoro "Daily Plan" → Can include habit routine

---

#### 16. Progressive Overload (`templates/progressive-overload.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### Training Goal
**What am I trying to improve?**
- [Strength|Endurance|Skill|Hypertrophy|Power]

**Target**: [Specific outcome, e.g., "Bench press 225 lbs"]

### Baseline Assessment
- **Current Performance**: [Measurement]
- **Assessment Date**: [YYYY-MM-DD]
- **Method**: [How measured]

### Progressive Overload Variables

#### 1. Volume (Sets × Reps × Weight)
- **Current**: [X sets] × [Y reps] × [Z weight]
- **Progression Plan**: [Increase by X% per week/cycle]

#### 2. Intensity (% of 1-Rep Max or Effort Level)
- **Current**: [%1RM or RPE]
- **Progression Plan**: [Increase intensity every X weeks]

#### 3. Frequency (Sessions per Week)
- **Current**: [X sessions/week]
- **Progression Plan**: [Add sessions when?]

#### 4. Density (Rest Between Sets)
- **Current**: [X seconds/minutes rest]
- **Progression Plan**: [Reduce rest by X seconds per cycle]

### Progression Schedule

| Week | Volume | Intensity | Frequency | Density | Notes |
|------|--------|-----------|-----------|---------|-------|
| 1    | [Sets×Reps×Weight] | [%1RM] | [X/week] | [Rest] | Baseline |
| 2    | [Increased] | [Same] | [Same] | [Same] | Volume up |
| 3    | [Same] | [Increased] | [Same] | [Same] | Intensity up |
| 4    | [Same] | [Same] | [Same] | [Reduced] | Density up |
| 5    | [Deload] | [Reduced] | [Reduced] | [Increased] | Recovery |
| 6    | [New baseline] | ... | ... | ... | Start next cycle |

### Deload Protocol
**Every [X] weeks**: Reduce volume/intensity by [Y]% for recovery

### Tracking Metrics
- **Primary Metric**: [What's most important?]
- **Secondary Metrics**: [Supporting measures]

| Date | Primary Metric | Secondary Metric | RPE | Notes |
|------|----------------|------------------|-----|-------|
| [Date] | [Value] | [Value] | [1-10] | [Observations] |

### Plateau Protocol
**If no progress for [X] weeks:**
- [ ] Deload for 1 week
- [ ] Change exercise variation
- [ ] Adjust volume/intensity ratio
- [ ] Check recovery (sleep, nutrition)
```

**Scoring Contribution:**
- Generates criteria: Progression Rate, Recovery Adequacy, Injury Risk
- Provides weights: Higher weight if physical capability is project-critical

**Deep Plan Contribution:**
- L2 headings: "Foundation Phase", "Progressive Phase", "Peak Phase", "Deload Phase"
- L3 tasks: Weekly training sessions, nutrition adjustments
- Milestones: Each progression cycle completion

**Auto-linking:**
- Links to: SMART Goals (training target), Habit Loop (training consistency)
- SMART "Measurable" ← Progressive Overload "Primary Metric"
- Habit Loop "Routine" ← Progressive Overload "Training sessions"

---

#### 17. Macro Tracking (`templates/macro-tracking.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### Goal
**What am I trying to achieve?**
- [ ] Weight loss
- [ ] Muscle gain
- [ ] Maintenance
- [ ] Performance (athletic)
- [ ] Health optimization

### Body Metrics
- **Current Weight**: [lbs/kg]
- **Height**: [in/cm]
- **Age**: [years]
- **Sex**: [M/F]
- **Activity Level**: [Sedentary|Lightly active|Moderately active|Very active|Extremely active]

### Macro Calculations

#### Total Daily Energy Expenditure (TDEE)
- **Basal Metabolic Rate (BMR)**: [Calculated using Mifflin-St Jeor]
  - Men: (10 × weight_kg) + (6.25 × height_cm) - (5 × age) + 5
  - Women: (10 × weight_kg) + (6.25 × height_cm) - (5 × age) - 161
- **Activity Multiplier**: [1.2 - 1.9 based on activity level]
- **TDEE**: [BMR × Activity Multiplier] = [X] calories/day

#### Calorie Target
- **Goal**: [Deficit|Surplus|Maintenance]
- **Adjustment**: [±X]% from TDEE
- **Target Calories**: [Y] calories/day

#### Macro Split
**Protein**:
- **Target**: [X] g/kg body weight (typically 1.6-2.2 g/kg for muscle gain)
- **Total**: [grams] = [calories] (4 cal/g)

**Fats**:
- **Target**: [%]% of total calories (typically 20-35%)
- **Total**: [grams] = [calories] (9 cal/g)

**Carbohydrates**:
- **Total**: [Remaining calories] = [grams] (4 cal/g)

**Summary**:
- Protein: [X]g ([Y]%)
- Fats: [X]g ([Y]%)
- Carbs: [X]g ([Y]%)
- Total: [Z] calories

### Meal Plan Template

| Meal | Time | Protein | Fats | Carbs | Calories | Foods |
|------|------|---------|------|-------|----------|-------|
| Breakfast | [Time] | [g] | [g] | [g] | [cal] | [Examples] |
| Snack 1 | [Time] | [g] | [g] | [g] | [cal] | [Examples] |
| Lunch | [Time] | [g] | [g] | [g] | [cal] | [Examples] |
| Snack 2 | [Time] | [g] | [g] | [g] | [cal] | [Examples] |
| Dinner | [Time] | [g] | [g] | [g] | [cal] | [Examples] |
| **Total** | | [g] | [g] | [g] | [cal] | |

### Tracking Log

| Date | Weight | Protein | Fats | Carbs | Calories | Notes |
|------|--------|---------|------|-------|----------|-------|
| [Date] | [lbs] | [g] | [g] | [g] | [cal] | [How I felt] |

### Adjustment Protocol
**Review every [X] weeks:**
- Weight change: [lbs/kg]
- If not progressing → Adjust calories by [±Y]%
- Recalculate macros
```

**Scoring Contribution:**
- Generates criteria: Nutritional Adherence, Energy Balance, Body Composition
- Provides weights: Higher if nutrition directly impacts project execution

**Deep Plan Contribution:**
- L2 headings: "Meal Prep", "Macro Tracking", "Progress Review"
- L3 tasks: Weekly meal planning, grocery shopping, macro logging
- Milestones: 2-week adherence, 4-week progress check

**Auto-linking:**
- Links to: Progressive Overload (nutrition supports training), SMART Goals (weight/body comp targets)
- Progressive Overload "Recovery" → Macro Tracking "Protein target"
- SMART "Measurable" ← Macro Tracking "Weight change"

---

#### 18. Recovery Protocol (`templates/recovery-protocol.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### Recovery Goal
**What am I recovering from?**
- [ ] Intense training cycle
- [ ] Injury/illness
- [ ] Burnout/overtraining
- [ ] Competition/event
- [ ] General optimization

### Current Recovery Status
- **Fatigue Level**: [1-10]
- **Sleep Quality**: [1-10]
- **Muscle Soreness**: [1-10]
- **Mental Clarity**: [1-10]
- **Motivation**: [1-10]

**Overall Recovery Score**: [Average or weighted]

### Recovery Modalities

#### 1. Sleep
- **Target**: [7-9 hours/night]
- **Current Average**: [X hours]
- **Sleep Hygiene Tactics**:
  - [ ] Consistent bedtime ([Time])
  - [ ] Dark, cool room
  - [ ] No screens 1 hour before bed
  - [ ] Caffeine cutoff ([Time])

#### 2. Nutrition
- **Protein Intake**: [X g/day] (for muscle repair)
- **Hydration**: [X liters/day]
- **Anti-inflammatory Foods**: [List]
- **Supplements**: [If any]

#### 3. Active Recovery
- **Type**: [Light cardio|Yoga|Stretching|Walking]
- **Frequency**: [X times/week]
- **Duration**: [X minutes]

#### 4. Passive Recovery
- **Massage**: [Frequency]
- **Sauna/Ice Bath**: [Frequency]
- **Foam Rolling**: [Daily|Weekly]
- **Meditation/Breathing**: [X min/day]

#### 5. Load Management
- **Training Volume**: [Reduced by X%]
- **Intensity**: [Reduced by Y%]
- **Deload Duration**: [X weeks]

### Recovery Schedule

| Day | Sleep | Nutrition | Active | Passive | Training Load | Notes |
|-----|-------|-----------|--------|---------|---------------|-------|
| Mon | [hrs] | ✓/✗ | [Type] | [Type] | [Low/Med/High] | [Observations] |
| Tue | [hrs] | ✓/✗ | [Type] | [Type] | [Low/Med/High] | |
| ... | ... | ... | ... | ... | ... | |

### Metrics to Track
- **Resting Heart Rate (RHR)**: [Measure daily before getting out of bed]
- **Heart Rate Variability (HRV)**: [If available]
- **Body Weight**: [Daily weigh-ins]
- **Perceived Recovery**: [1-10 scale daily]

| Date | RHR | HRV | Weight | Perceived Recovery | Notes |
|------|-----|-----|--------|---------------------|-------|
| [Date] | [bpm] | [ms] | [lbs] | [1-10] | [Observations] |

### Red Flags (Stop and Reassess)
- [ ] RHR elevated >10% for 3+ days
- [ ] HRV decreased >10% for 3+ days
- [ ] Sleep <6 hours for 3+ nights
- [ ] Persistent muscle soreness >5 days
- [ ] Loss of appetite
- [ ] Declining performance despite rest
```

**Scoring Contribution:**
- Generates criteria: Recovery Completeness, Injury Risk, Readiness
- Provides weights: Higher if project has physical demands

**Deep Plan Contribution:**
- L2 headings: "Sleep Optimization", "Nutrition Support", "Active Recovery"
- L3 tasks: Daily recovery activities, weekly metrics review
- Milestones: Recovery score >7/10, RHR normalized

**Auto-linking:**
- Links to: Progressive Overload (deload cycles), Macro Tracking (nutrition for recovery)
- Progressive Overload "Deload Protocol" ← Recovery Protocol "Load Management"
- Macro Tracking "Protein" → Recovery Protocol "Nutrition"

---

### Personal Domain (6 Frameworks)

#### 19. Pomodoro Technique (`templates/pomodoro-technique.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### Daily Work Plan
**Date**: [YYYY-MM-DD]
**Total Available Pomodoros**: [Calculated: Work hours × 2]

### Task List with Pomodoro Estimates

| Task | Priority | Estimated Pomodoros | Actual Pomodoros | Status |
|------|----------|---------------------|------------------|--------|
| [Task 1] | [H/M/L] | [X] | | ⬜ |
| [Task 2] | [H/M/L] | [Y] | | ⬜ |
| [Task 3] | [H/M/L] | [Z] | | ⬜ |

**Pomodoro Definition**:
- **Focus Time**: 25 minutes
- **Short Break**: 5 minutes (after each Pomodoro)
- **Long Break**: 15-30 minutes (after 4 Pomodoros)

### Pomodoro Session Log

#### Session 1 (Pomodoro 1-4)
| Pom # | Start Time | Task | Distractions | Completed? | Notes |
|-------|------------|------|--------------|------------|-------|
| 1 | [Time] | [Task name] | [Count] | ✓/✗ | [Observations] |
| 2 | [Time] | [Task name] | [Count] | ✓/✗ | |
| 3 | [Time] | [Task name] | [Count] | ✓/✗ | |
| 4 | [Time] | [Task name] | [Count] | ✓/✗ | |

**Long Break**: [Time] - [Duration]

#### Session 2 (Pomodoro 5-8)
[Same structure]

### Daily Summary
- **Planned Pomodoros**: [X]
- **Completed Pomodoros**: [Y]
- **Completion Rate**: [Y/X × 100]%
- **Tasks Finished**: [Count]
- **Total Distractions**: [Count]

### Improvement Actions
- [ ] Reduce distractions by: [Action]
- [ ] Improve estimates by: [Action]
- [ ] Optimize break activities: [Action]
```

**Scoring Contribution:**
- Generates criteria: Task Completion Rate, Focus Quality, Time Efficiency
- Provides weights: Higher if deep work is critical to project

**Deep Plan Contribution:**
- L2 headings: Each major task becomes L2
- L3 tasks: Broken down into Pomodoro-sized chunks
- Milestones: Daily completion targets

**Auto-linking:**
- Links to: GTD (task list source), OKRs (initiatives → tasks)
- GTD "Next Actions" → Pomodoro "Task List"
- OKR "Initiatives" → Pomodoro "Task List"

---

#### 20. Atomic Habits (4 Laws) (`templates/atomic-habits.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### Habit to Build/Break
**Desired Habit**: [What habit?]
**Type**: [Build new|Break old]
**Frequency**: [Daily|Weekly|Other]

### 4 Laws of Behavior Change

#### Law 1: Make It Obvious (for good habits) / Make It Invisible (for bad habits)

**For Building Good Habits:**
- **Implementation Intention**: "I will [BEHAVIOR] at [TIME] in [LOCATION]."
  - Example: "I will meditate for 10 minutes at 7:00 AM in my bedroom."
- **Habit Stacking**: "After I [CURRENT HABIT], I will [NEW HABIT]."
  - Example: "After I pour my morning coffee, I will journal for 5 minutes."
- **Environment Design**: [How to make cues visible]
  - Example: "Put running shoes by bed so I see them immediately."

**For Breaking Bad Habits:**
- **Remove Cues**: [How to make triggers invisible]
  - Example: "Hide phone in drawer during work hours."

**My Application**: [Specific tactic]

#### Law 2: Make It Attractive (for good habits) / Make It Unattractive (for bad habits)

**For Building Good Habits:**
- **Temptation Bundling**: Pair habit with something I enjoy
  - "Only watch [favorite show] while [doing habit]."
- **Social Environment**: Join group where desired behavior is normal
  - Example: "Join running club where everyone runs daily."

**For Breaking Bad Habits:**
- **Reframe Mindset**: Highlight benefits of avoidance
  - Example: "I don't smoke → I'm free from nicotine dependence."

**My Application**: [Specific tactic]

#### Law 3: Make It Easy (for good habits) / Make It Difficult (for bad habits)

**For Building Good Habits:**
- **2-Minute Rule**: Scale down habit to 2-minute version
  - "Read 30 pages" → "Read 1 page"
- **Reduce Friction**: Decrease steps between you and habit
  - Example: "Prep gym bag night before."
- **Prime Environment**: Set up space in advance
  - Example: "Lay out yoga mat before bed."

**For Breaking Bad Habits:**
- **Increase Friction**: Add steps between you and habit
  - Example: "Delete social media apps from phone."

**My Application**: [Specific tactic]

#### Law 4: Make It Satisfying (for good habits) / Make It Unsatisfying (for bad habits)

**For Building Good Habits:**
- **Immediate Reward**: Give yourself pleasure right after
  - Example: "After workout, enjoy favorite smoothie."
- **Habit Tracking**: Visual satisfaction of marking completion
  - Method: [App|Paper calendar|Streak counter]
- **Never Miss Twice**: If I slip, get back on track immediately

**For Breaking Bad Habits:**
- **Accountability Partner**: Someone who costs me if I slip
  - Example: "$50 to friend if I smoke."
- **Habit Contract**: Written commitment with consequences

**My Application**: [Specific tactic]

### Habit Scorecard

| Date | Law 1 Applied? | Law 2 Applied? | Law 3 Applied? | Law 4 Applied? | Habit Done? | Notes |
|------|----------------|----------------|----------------|----------------|-------------|-------|
| [Date] | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | [Observations] |

### Identity-Based Habit
**Who do I want to become?**
- "I am a [type of person who does this habit]."
- Example: "I am a runner" (not "I want to run").

**Evidence of Identity**:
- Small win 1: [Example of acting as this identity]
- Small win 2: [Example]
```

**Scoring Contribution:**
- Generates criteria: Habit Sustainability, 4 Laws Coverage, Identity Alignment
- Provides weights: Higher if habit is foundational to project success

**Deep Plan Contribution:**
- L2 headings: "Make Obvious", "Make Attractive", "Make Easy", "Make Satisfying"
- L3 tasks: Specific implementations per law
- Milestones: 7-day streak (2-minute version), 30-day streak (full version)

**Auto-linking:**
- Links to: Habit Loop, Pomodoro Technique
- Habit Loop "Cue" ← Atomic Habits "Law 1 (Make Obvious)"
- Habit Loop "Reward" ← Atomic Habits "Law 4 (Make Satisfying)"

---

#### 21. Eisenhower Matrix (`templates/eisenhower-matrix.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### Task List Classification

| Task | Urgent? | Important? | Quadrant | Action |
|------|---------|------------|----------|--------|
| [Task 1] | ✓/✗ | ✓/✗ | [Q1-Q4] | [Do/Schedule/Delegate/Delete] |
| [Task 2] | ✓/✗ | ✓/✗ | [Q1-Q4] | |
| [Task 3] | ✓/✗ | ✓/✗ | [Q1-Q4] | |

### Quadrant 1: Urgent & Important (DO NOW - Crisis Mode)
**Tasks**:
- [ ] [Task with deadline or crisis]
- [ ] [Task with deadline or crisis]

**Time Allocated**: [X]% of week
**Goal**: Minimize time here (reactive)

### Quadrant 2: Not Urgent but Important (SCHEDULE - Strategic Mode)
**Tasks**:
- [ ] [Planning, prevention, relationship-building]
- [ ] [Learning, skill development]
- [ ] [Exercise, health, recovery]

**Time Allocated**: [Y]% of week
**Goal**: Maximize time here (proactive)

### Quadrant 3: Urgent but Not Important (DELEGATE - Distraction Mode)
**Tasks**:
- [ ] [Interruptions, some emails/calls]
- [ ] [Other people's priorities]

**Time Allocated**: [Z]% of week
**Goal**: Minimize or delegate

### Quadrant 4: Not Urgent & Not Important (DELETE - Waste Mode)
**Tasks**:
- [ ] [Time wasters, busy work]
- [ ] [Trivial activities]

**Time Allocated**: [W]% of week
**Goal**: Eliminate completely

### Weekly Analysis

| Quadrant | Hours Spent | % of Time | Target % | Gap |
|----------|-------------|-----------|----------|-----|
| Q1 (Urgent & Important) | [X] | [%] | 20-25% | [±%] |
| Q2 (Not Urgent, Important) | [Y] | [%] | 60-70% | [±%] |
| Q3 (Urgent, Not Important) | [Z] | [%] | 5-10% | [±%] |
| Q4 (Not Urgent/Important) | [W] | [%] | 0-5% | [±%] |

### Improvement Actions
- [ ] Move from Q1 to Q2 by: [Prevention strategy]
- [ ] Delegate Q3 tasks to: [Person/system]
- [ ] Eliminate Q4 tasks by: [Boundary/habit]
```

**Scoring Contribution:**
- Generates criteria: Strategic Focus, Urgency Balance, Waste Elimination
- Provides weights: Higher weight to Q2 (important, not urgent) tasks

**Deep Plan Contribution:**
- L2 headings: "Q1 Crisis Management", "Q2 Strategic Work", "Q3 Delegation Plan"
- L3 tasks: Specific Q2 activities to schedule
- Milestones: Achieve 60%+ time in Q2

**Auto-linking:**
- Links to: GTD (task classification), OKRs (Q2 should contain KR initiatives)
- GTD "Projects" → Eisenhower "Q2" (important strategic work)
- OKR "Initiatives" → Eisenhower "Q2"

---

#### 22. Getting Things Done (GTD) (`templates/gtd-system.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### GTD Workflow (5 Steps)

#### 1. Capture
**Inboxes** (where stuff lands):
- [ ] Physical inbox (desk)
- [ ] Email inbox
- [ ] Notes app
- [ ] Voice memos
- [ ] [Other]

**Capture Triggers**:
- Mind dump: [List all open loops]

#### 2. Clarify
**For each item in inbox, ask**:
- **Is it actionable?**
  - **No** → Trash, Someday/Maybe, or Reference
  - **Yes** → Continue...
- **What's the next action?**
  - [Specific physical action]
- **Will it take <2 minutes?**
  - **Yes** → Do it now
  - **No** → Continue...
- **Am I the best person?**
  - **No** → Delegate (Waiting For list)
  - **Yes** → Continue...
- **Is it one action or multiple?**
  - **One action** → Next Actions list
  - **Multiple** → Project (with next action defined)

#### 3. Organize

**GTD Lists**:

##### Next Actions (by context)
- **@Computer**:
  - [ ] [Action 1]
  - [ ] [Action 2]
- **@Phone**:
  - [ ] [Action 1]
- **@Errands**:
  - [ ] [Action 1]
- **@Home**:
  - [ ] [Action 1]
- **@Office**:
  - [ ] [Action 1]

##### Projects (outcomes requiring >1 action)
- [ ] [Project 1] - Next Action: [Specific action]
- [ ] [Project 2] - Next Action: [Specific action]

##### Waiting For (delegated/blocked)
- [ ] [Item 1] - Waiting on: [Person] - Date delegated: [Date]

##### Someday/Maybe (not committed yet)
- [ ] [Idea 1]
- [ ] [Idea 2]

##### Calendar (time-specific commitments)
- [Date/Time]: [Appointment]
- [Date]: [Deadline]

##### Reference (non-actionable info)
- [Document/link storage]

#### 4. Reflect

**Weekly Review Checklist**:
- [ ] Collect loose papers/materials
- [ ] Process all inboxes to zero
- [ ] Review Next Actions lists
- [ ] Review Projects list (ensure each has next action)
- [ ] Review Waiting For list (follow up as needed)
- [ ] Review Someday/Maybe (promote any to active?)
- [ ] Review upcoming calendar
- [ ] Brain dump any new items

**Weekly Review Date**: [Every Friday at 4 PM]

#### 5. Engage

**Decision Criteria** (when choosing what to do):
1. **Context**: Where am I? What tools available?
2. **Time Available**: How long until next commitment?
3. **Energy**: Mental/physical capacity right now?
4. **Priority**: What's most important given above?

### Current State Snapshot

| List | Items | Status |
|------|-------|--------|
| Inbox | [X] | [Last processed: Date] |
| Next Actions | [Y] | [Contexts: X] |
| Projects | [Z] | [Active: X, Stalled: Y] |
| Waiting For | [W] | [Oldest: Date] |
| Someday/Maybe | [V] | [Last reviewed: Date] |
| Calendar | [U items next 2 weeks] | |
```

**Scoring Contribution:**
- Generates criteria: Inbox Zero Achievement, Next Action Clarity, Project Momentum
- Provides weights: Higher if GTD is primary productivity system

**Deep Plan Contribution:**
- L2 headings: Each active GTD project becomes L2 heading
- L3 tasks: Next Actions per project
- Milestones: Weekly review completion, inbox zero

**Auto-linking:**
- Links to: Eisenhower Matrix (contexts prioritized by urgency/importance), OKRs (projects aligned to KRs)
- Eisenhower "Q2" ← GTD "Projects"
- OKR "Initiatives" → GTD "Projects"

---

#### 23. Growth Mindset Reflection (`templates/growth-mindset.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### Fixed vs. Growth Mindset Assessment

#### Recent Challenge/Setback
**Describe the situation**:
- [What happened?]

**Fixed Mindset Response** (what I initially thought):
- [ ] "I'm not good at this."
- [ ] "I'll never be able to do this."
- [ ] "I'm just not talented in this area."
- [ ] "This is too hard."
- [ ] "I give up."

**Growth Mindset Reframe**:
- [ ] "I'm not good at this yet."
- [ ] "What can I learn from this?"
- [ ] "What strategy can I try?"
- [ ] "This will take time and effort."
- [ ] "Mistakes help me learn."

### Reflection Questions

#### 1. Effort vs. Outcome
**What I learned from the process** (regardless of result):
- [Lesson 1]
- [Lesson 2]

**How effort contributed**:
- [Connection between effort and outcome]

#### 2. Challenges as Opportunities
**How this challenge is helping me grow**:
- Skill being developed: [Skill]
- Resilience being built: [How]

#### 3. Criticism as Feedback
**Feedback received**:
- [Criticism or feedback]

**Growth Mindset Interpretation**:
- What's true/useful in this feedback? [Analysis]
- How can I improve? [Action plan]

#### 4. Success of Others as Inspiration
**Someone I admire in this area**:
- [Person]

**What can I learn from their journey?**
- [Lessons from their path]
- [Strategies to adopt]

### Growth Plan

**Current Ability Level**: [1-10]
**Target Ability Level**: [1-10]

**Strategies to Bridge Gap**:
1. [Strategy 1] - [Why this will help]
2. [Strategy 2]
3. [Strategy 3]

**Evidence of Progress** (small wins):
- [ ] [Win 1] - Date achieved: [Date]
- [ ] [Win 2] - Date achieved: [Date]

### Weekly Reflection

| Week | Challenge Faced | Fixed Response | Growth Reframe | Action Taken | Outcome |
|------|-----------------|----------------|----------------|--------------|---------|
| [Date] | [Description] | [What I thought] | [Reframe] | [What I did] | [Result] |
```

**Scoring Contribution:**
- Generates criteria: Learning Agility, Resilience, Feedback Integration
- Provides weights: Higher if mindset is critical to project success

**Deep Plan Contribution:**
- L2 headings: "Develop Skill X", "Build Resilience", "Integrate Feedback"
- L3 tasks: Specific growth strategies
- Milestones: Evidence of progress checkpoints

**Auto-linking:**
- Links to: Deliberate Practice (growth mindset enables deliberate practice), SMART Goals (growth plan → SMART goal)
- Deliberate Practice "Micro-Skills" ← Growth Mindset "Strategies to Bridge Gap"
- SMART "Achievable" ← Growth Mindset "Belief in growth potential"

---

#### 24. Deliberate Practice (`templates/deliberate-practice.template.md`)

**Framework Input Sections:**
```markdown
## Framework Input

### Skill to Develop
**Skill**: [Specific skill]
**Current Level**: [Beginner|Intermediate|Advanced]
**Target Level**: [Description of mastery]

### Skill Decomposition (Break into Micro-Skills)

**Core Skill**: [Main skill]
**Sub-Skills**:
1. [Sub-skill 1]
   - Current proficiency: [1-10]
   - Target proficiency: [1-10]
2. [Sub-skill 2]
   - Current proficiency: [1-10]
   - Target proficiency: [1-10]
3. [Sub-skill 3]
   - Current proficiency: [1-10]
   - Target proficiency: [1-10]

### Deliberate Practice Principles

#### 1. Focused Practice (Not Mindless Repetition)
**Specific Focus for Each Session**:
- Session 1: [Sub-skill 1] - [Specific aspect]
- Session 2: [Sub-skill 2] - [Specific aspect]

**Avoid**: General, unfocused practice

#### 2. Immediate Feedback
**How I'll get feedback**:
- [ ] Coach/mentor review
- [ ] Video recording and self-review
- [ ] Metrics/data tracking
- [ ] Peer feedback

**Feedback Loop**: [Frequency]

#### 3. Push Beyond Comfort Zone
**Sweet Spot**: Tasks just beyond current ability (not too easy, not impossible)

**Challenge Level for Each Sub-Skill**:
- [Sub-skill 1]: [How to make it 10% harder]
- [Sub-skill 2]: [How to make it 10% harder]

#### 4. Mental Representation
**Expert Performance Looks Like**:
- [Characteristic 1 of expert performance]
- [Characteristic 2]

**My Current Mental Model**:
- [How I currently think about this skill]

**Gap to Close**:
- [Difference between expert and my model]

### Practice Schedule

| Date | Sub-Skill Focus | Duration | Challenge Level | Feedback Received | Progress |
|------|-----------------|----------|-----------------|-------------------|----------|
| [Date] | [Sub-skill] | [X min] | [Description] | [What I learned] | [1-10] |

### Performance Metrics

**Baseline Assessment** (Date: [YYYY-MM-DD]):
- [Metric 1]: [Value]
- [Metric 2]: [Value]

**Progress Tracking**:
| Date | Metric 1 | Metric 2 | Notes |
|------|----------|----------|-------|
| [Date] | [Value] | [Value] | [Observations] |

### Plateaus and Breakthroughs

**If Progress Stalls**:
- [ ] Increase difficulty
- [ ] Change practice method
- [ ] Seek expert feedback
- [ ] Work on different sub-skill
- [ ] Study expert performance more closely

**Breakthrough Moments**:
- [Date]: [What clicked? What changed?]
```

**Scoring Contribution:**
- Generates criteria: Skill Progression Rate, Feedback Quality, Practice Consistency
- Provides weights: Higher if skill is critical to project success

**Deep Plan Contribution:**
- L2 headings: Each sub-skill becomes L2 phase
- L3 tasks: Daily/weekly practice sessions
- Milestones: Sub-skill proficiency targets

**Auto-linking:**
- Links to: Growth Mindset (belief enables practice), Pomodoro (practice sessions → Pomodoros)
- Growth Mindset "Effort" ← Deliberate Practice "Focused Practice"
- Pomodoro "Task List" ← Deliberate Practice "Practice Schedule"

---

## Template Composition Patterns

### Pattern 1: Startup Launch (Business Domain)
**Sequence**: Lean Canvas → Value Proposition Canvas → OKRs → Business Model Canvas → GTD

**Auto-Linking Logic**:
1. **Lean Canvas "Problem"** → VPC "Pains"
   - Action: Copy top 3 problems to VPC pain section
2. **Lean Canvas "Solution"** → VPC "Pain Relievers"
   - Action: Copy solutions to VPC pain reliever section
3. **Lean Canvas "Key Metrics"** → OKR "Key Results"
   - Action: Transform metrics into measurable KRs
4. **VPC "Customer Jobs"** → BMC "Customer Segments"
   - Action: Sync customer profile data
5. **OKR "Initiatives"** → GTD "Projects"
   - Action: Create GTD project for each initiative with next action

**Expected Outcome**: Complete business strategy from problem validation to daily execution

---

### Pattern 2: Skill Acquisition (Personal Domain)
**Sequence**: Growth Mindset Reflection → Deliberate Practice → Pomodoro Technique → Atomic Habits

**Auto-Linking Logic**:
1. **Growth Mindset "Strategies to Bridge Gap"** → Deliberate Practice "Practice Schedule"
   - Action: Convert growth strategies into practice sessions
2. **Deliberate Practice "Sub-Skills"** → Pomodoro "Task List"
   - Action: Each practice session becomes Pomodoro task
3. **Deliberate Practice "Practice Schedule"** → Atomic Habits "Implementation Intention"
   - Action: Daily practice time becomes habit cue
4. **Pomodoro "Daily Completion Rate"** → Atomic Habits "Habit Tracking"
   - Action: Practice consistency tracked visually

**Expected Outcome**: Structured skill development with daily accountability

---

### Pattern 3: Health Transformation (Health Domain)
**Sequence**: Health Belief Model → SMART Goals → Progressive Overload → Macro Tracking → Habit Loop

**Auto-Linking Logic**:
1. **HBM "Perceived Benefits"** → SMART "Relevant (Why)"
   - Action: Benefits become goal rationale
2. **HBM "Cues to Action"** → Habit Loop "Cue"
   - Action: External cues from HBM inform habit triggers
3. **SMART "Measurable Target"** → Progressive Overload "Target"
   - Action: Fitness goal becomes training target
4. **Progressive Overload "Training Sessions"** → Macro Tracking "Meal Plan"
   - Action: Nutrition timing aligned with training
5. **Macro Tracking "Daily Target"** → Habit Loop "Routine"
   - Action: Meal prep becomes daily habit

**Expected Outcome**: Behavior change supported by belief, structure, and habit

---

### Pattern 4: Financial Decision (Finance Domain)
**Sequence**: NPV Analysis → DCF Model → Monte Carlo Simulation → Real Options → Kelly Criterion

**Auto-Linking Logic**:
1. **NPV "Cash Flow Projections"** → DCF "Free Cash Flow"
   - Action: NPV cash flows become DCF input
2. **DCF "Revenue Growth Rate"** → Monte Carlo "Variable 1"
   - Action: DCF assumptions become Monte Carlo variables
3. **DCF "Operating Margin"** → Monte Carlo "Variable 2"
   - Action: Margin assumptions tested in simulation
4. **Monte Carlo "10th/50th/90th Percentile"** → Real Options "Decision Tree Scenarios"
   - Action: Probabilistic outcomes inform option valuation
5. **Real Options "Expanded NPV"** → Kelly Criterion "Win Probability"
   - Action: Option value influences capital allocation

**Expected Outcome**: Risk-adjusted investment decision with optimal sizing

---

### Pattern 5: Product Development (Business + Personal)
**Sequence**: Business Model Canvas → OKRs → GTD → Pomodoro → Growth Mindset

**Auto-Linking Logic**:
1. **BMC "Key Activities"** → OKR "Initiatives"
   - Action: Key activities become OKR initiatives
2. **OKR "Key Results"** → GTD "Projects"
   - Action: Each KR becomes GTD project
3. **GTD "Next Actions"** → Pomodoro "Task List"
   - Action: Next actions scheduled as Pomodoros
4. **Pomodoro "Daily Summary"** → OKR "Progress Tracking"
   - Action: Completed Pomodoros update KR progress
5. **OKR "Setbacks"** → Growth Mindset "Reflection"
   - Action: KR failures analyzed for learnings

**Expected Outcome**: Strategic product goals executed daily with continuous learning

---

### Pattern 6: Competitive Analysis (Business Domain)
**Sequence**: SWOT Analysis → Porter's Five Forces → Business Model Canvas

**Auto-Linking Logic**:
1. **SWOT "Threats"** → Porter's "Competitive Rivalry"
   - Action: External threats feed into rivalry assessment
2. **SWOT "Opportunities"** → Porter's "Threat of New Entrants"
   - Action: Market opportunities influence entry barrier analysis
3. **Porter's "Bargaining Power of Suppliers"** → BMC "Key Partnerships"
   - Action: Supplier power insights drive partnership strategy
4. **Porter's "Strategic Implications"** → SWOT "SO/ST/WO/WT Strategies"
   - Action: Porter's insights refine SWOT strategies
5. **BMC "Cost Structure"** → SWOT "Weaknesses (if high cost)"
   - Action: Cost insights inform weakness analysis

**Expected Outcome**: Comprehensive competitive positioning with actionable strategies

---

### Pattern 7: Athletic Performance (Health Domain)
**Sequence**: SMART Goals → Progressive Overload → Macro Tracking → Recovery Protocol → Habit Loop

**Auto-Linking Logic**:
1. **SMART "Measurable Target"** → Progressive Overload "Target Performance"
   - Action: Performance goal becomes training target
2. **Progressive Overload "Volume/Intensity Schedule"** → Macro Tracking "Calorie Target"
   - Action: Training load determines calorie needs
3. **Progressive Overload "Deload Protocol"** → Recovery Protocol "Load Management"
   - Action: Deload weeks sync with recovery plan
4. **Macro Tracking "Meal Plan"** → Habit Loop "Routine"
   - Action: Meal timing becomes daily habit
5. **Recovery Protocol "Sleep Target"** → Habit Loop "Cue (Bedtime)"
   - Action: Sleep hygiene becomes habit

**Expected Outcome**: Peak performance through training, nutrition, and recovery integration

---

### Pattern 8: Time Management Overhaul (Personal Domain)
**Sequence**: Eisenhower Matrix → GTD → Pomodoro → Atomic Habits

**Auto-Linking Logic**:
1. **Eisenhower "Q2 (Important, Not Urgent)"** → GTD "Projects"
   - Action: Strategic tasks become GTD projects
2. **Eisenhower "Q3 (Urgent, Not Important)"** → GTD "Waiting For (Delegate)"
   - Action: Delegation tasks tracked in Waiting For
3. **GTD "Next Actions"** → Pomodoro "Task List"
   - Action: Next actions scheduled as Pomodoros
4. **Pomodoro "Daily Plan"** → Eisenhower "Weekly Analysis"
   - Action: Time spent per quadrant calculated from Pomodoros
5. **Eisenhower "Q2 Time Target"** → Atomic Habits "Make It Obvious"
   - Action: Block Q2 time on calendar (habit)

**Expected Outcome**: Shift from reactive (Q1/Q3) to proactive (Q2) work

---

### Pattern 9: Investment Portfolio (Finance Domain)
**Sequence**: CAPM → Kelly Criterion → Monte Carlo → Real Options

**Auto-Linking Logic**:
1. **CAPM "Expected Return"** → Kelly "Win Payoff (b)"
   - Action: Expected return becomes Kelly payoff ratio
2. **CAPM "Beta"** → Monte Carlo "Variable (Volatility)"
   - Action: Beta informs return distribution in simulation
3. **Monte Carlo "P(Success)"** → Kelly "Win Probability (p)"
   - Action: Simulation probability feeds Kelly formula
4. **Kelly "Optimal %"** → Real Options "Initial Investment Size"
   - Action: Kelly allocation determines option investment
5. **Real Options "Expansion NPV"** → Kelly "Recalculate after new info"
   - Action: Option outcomes update Kelly probabilities

**Expected Outcome**: Optimal portfolio allocation with staged investment strategy

---

### Pattern 10: Habit Formation (Personal + Health)
**Sequence**: Health Belief Model → Habit Loop → Atomic Habits → Pomodoro

**Auto-Linking Logic**:
1. **HBM "Cues to Action"** → Habit Loop "Cue"
   - Action: HBM cues become habit triggers
2. **HBM "Perceived Benefits"** → Habit Loop "Reward"
   - Action: Benefits become immediate rewards
3. **Habit Loop "Cue-Routine-Reward"** → Atomic Habits "4 Laws"
   - Action: Loop mapped to Laws (Cue=Obvious, Reward=Satisfying)
4. **Atomic Habits "2-Minute Rule"** → Pomodoro "Task Estimate"
   - Action: Minimum viable habit = 1 Pomodoro
5. **Pomodoro "Daily Completion"** → Atomic Habits "Habit Tracker"
   - Action: Pomodoro log = habit tracker

**Expected Outcome**: Sustainable behavior change with daily execution

---

## Auto-Population Rules

### Rule 1: Project Metadata from Workflow Plan
**Source**: `_bmad/bmm/workflows/life-os/workflow-plan.md`

**Auto-Populated Fields**:
```yaml
applied_to_project: "{{frontmatter.project_id}}"
project_name: "{{frontmatter.project_name}}"
created_date: "{{TODAY}}"
```

**Logic**:
- Read `workflow-plan.md` frontmatter
- Extract `project_id` and `project_name`
- Inject into every framework template when created

---

### Rule 2: Consilium Specialists → Framework Recommendation
**Source**: `_bmad/bmm/workflows/life-os/steps-c/step-04-consilium.md`

**Mapping Table**:
| Consilium Specialist | Recommended Frameworks | Why |
|----------------------|------------------------|-----|
| Business Strategist | Business Model Canvas, OKRs, SWOT | Strategic thinking required |
| Financial Analyst | NPV, DCF, Monte Carlo, CAPM | Financial evaluation needed |
| UX Designer | Value Proposition Canvas, Lean Canvas | Customer-centric design |
| Data Scientist | Monte Carlo, Kelly Criterion | Probabilistic reasoning |
| Product Manager | Lean Canvas, OKRs, GTD | Product delivery focus |
| Health Coach | HBM, SMART, Progressive Overload | Wellness optimization |
| Productivity Expert | GTD, Pomodoro, Eisenhower | Time/task management |

**Auto-Population Logic**:
- Parse consilium specialist recommendations
- Pre-fill `consilium_specialist` field
- Suggest 1-3 frameworks based on specialist type

---

### Rule 3: Scoring Criteria → Framework Pre-Fill
**Source**: `_bmad/bmm/workflows/life-os/steps-c/step-05-scoring.md`

**Auto-Population Logic**:
- If MCDA criteria defined → Pre-fill relevant framework sections
  - Example: MCDA criterion "Financial Return" → NPV template "Decision Criteria"
  - Example: MCDA criterion "Customer Impact" → VPC template "Gain Creators"

**Mapping**:
| MCDA Criterion | Framework | Pre-Fill Section |
|----------------|-----------|------------------|
| Financial Return | NPV, DCF | Decision threshold, discount rate |
| Customer Satisfaction | VPC, Lean Canvas | Customer jobs, gains, pains |
| Strategic Fit | SWOT, Porter's | SO strategies, competitive analysis |
| Technical Feasibility | Deliberate Practice | Skill decomposition, practice plan |
| Time Efficiency | Pomodoro, GTD | Task estimates, context lists |

---

### Rule 4: Deep Plan L2 Headings → Framework Outputs
**Source**: `_bmad/bmm/workflows/life-os/steps-c/step-08-deep-plan.md`

**Auto-Population Logic**:
- After framework completed → Extract L2 headings
- Inject into deep plan template structure

**Example**:
```markdown
# From Business Model Canvas
L2 Headings Generated:
- Customer Acquisition
- Value Delivery
- Revenue Generation
- Cost Management

# Injected into Deep Plan
## Customer Acquisition
[Actions from BMC "Customer Segments" + "Channels"]

## Value Delivery
[Actions from BMC "Value Propositions" + "Key Activities"]
```

---

### Rule 5: Framework Dates → Timeline Sync
**Source**: Framework `completed_date` fields

**Auto-Population Logic**:
- When framework completed → Update project timeline
- Calculate time invested → Inform future estimates

**Example**:
```yaml
# Framework completed
framework: "Business Model Canvas"
completed_date: "2026-02-10"
time_invested_minutes: 90

# Auto-update workflow plan
timeline:
  - phase: "Design"
    start: "2026-02-05"
    end: "2026-02-10"  # Auto-updated from BMC completion
    actual_time: 90min  # Auto-calculated
```

---

## Implementation Guidelines

### For Claude Code

**When user says**: "Create [Framework Name] for this project"

**Claude Code MUST**:
1. Check if `workflow-plan.md` exists
2. Extract `project_id`, `project_name` from frontmatter
3. Read consilium recommendations (if Step 4 completed)
4. Read MCDA criteria (if Step 5 completed)
5. Create framework file with:
   - Auto-populated metadata
   - Pre-filled sections (where applicable)
   - Links to related frameworks
6. Save to: `_bmad/bmm/workflows/life-os/frameworks/[domain]-[framework-slug].md`

**Example Command**:
```
User: "Create a Business Model Canvas for this project"

Claude:
1. Reads workflow-plan.md → project_id="PROJ-001", project_name="Life OS"
2. Reads step-04-consilium.md → Specialist="Business Strategist"
3. Reads step-05-scoring.md → Criteria=["Financial Return", "Customer Impact"]
4. Creates: `_bmad/bmm/workflows/life-os/frameworks/business-business-model-canvas.md`
5. Pre-fills:
   - frontmatter.applied_to_project = "PROJ-001"
   - frontmatter.project_name = "Life OS"
   - frontmatter.consilium_specialist = "Business Strategist"
   - BMC "Value Propositions" section hint: "Consider 'Customer Impact' from scoring"
6. Notifies user: "Business Model Canvas created. 9 blocks ready to fill."
```

---

### For Template Files (Next Phase)

**After this architecture is approved**, create 24 template files:
- Location: `_bmad/bmm/workflows/life-os/templates/`
- File naming: `[domain]-[framework-slug].template.md`
- Each template includes:
  - YAML frontmatter (as defined in Universal Template Structure)
  - Framework-specific sections (as defined in Framework Specifications)
  - Auto-linking placeholders (for composition patterns)
  - Integration hooks (for Life OS Steps 5 & 8)

**Template Creation Order** (suggested):
1. Business domain (6 templates) - Most commonly used
2. Personal domain (6 templates) - High user demand
3. Finance domain (6 templates) - Complex but valuable
4. Health domain (6 templates) - Emerging interest

---

## Validation & Testing

### Template Validation Checklist

For each template, verify:
- [ ] YAML frontmatter complete and valid
- [ ] All framework-specific sections present
- [ ] Scoring contribution logic defined
- [ ] Deep plan contribution logic defined
- [ ] Auto-linking fields identified
- [ ] At least 1 composition pattern includes this framework
- [ ] Time estimate realistic (based on framework complexity)

### Composition Pattern Testing

For each pattern, verify:
- [ ] Auto-linking logic is clear and implementable
- [ ] Frameworks in sequence are logically connected
- [ ] Expected outcome is achievable
- [ ] Pattern covers common use case

### Auto-Population Testing

For each rule, verify:
- [ ] Source data location is correct
- [ ] Mapping logic is unambiguous
- [ ] Edge cases handled (e.g., missing source data)
- [ ] User override allowed (don't force auto-fill if user wants custom)

---

## Future Enhancements

### Phase 2: AI-Powered Suggestions
- Analyze project description → Suggest top 3 frameworks
- Detect framework dependencies → Auto-suggest composition pattern
- Predict time investment based on user history

### Phase 3: Cross-Framework Analytics
- Compare scenarios across frameworks (e.g., NPV vs. Real Options)
- Identify contradictions (e.g., SWOT says "high threat" but Porter's says "low rivalry")
- Generate unified dashboard from multiple frameworks

### Phase 4: Community Templates
- User-submitted framework variations
- Industry-specific adaptations (e.g., "SaaS-specific BMC")
- Version control and template evolution tracking

---

## Appendix: Framework Complexity Matrix

| Framework | Complexity | Est. Time | Recommended For | Prerequisites |
|-----------|------------|-----------|-----------------|---------------|
| **Business** |
| Business Model Canvas | Medium | 60-90 min | Startup, new product | None |
| OKR Framework | Low | 30-45 min | Goal setting, alignment | None |
| SWOT Analysis | Low | 30-60 min | Strategic planning | None |
| Lean Canvas | Medium | 45-75 min | Lean startup, MVP | None |
| Value Proposition Canvas | Medium | 45-60 min | Product-market fit | Lean Canvas (optional) |
| Porter's Five Forces | High | 90-120 min | Competitive analysis | Industry research |
| **Finance** |
| NPV Analysis | Medium | 60-90 min | Investment decision | Cash flow projections |
| DCF Model | High | 120-180 min | Valuation | Financial modeling skills |
| Monte Carlo Simulation | High | 90-150 min | Risk analysis | NPV or DCF |
| Real Options | High | 120-180 min | Flexibility valuation | NPV, probability theory |
| CAPM | Low | 30-45 min | Required return | Basic finance |
| Kelly Criterion | Medium | 45-60 min | Position sizing | Probability estimates |
| **Health** |
| Health Belief Model | Low | 30-45 min | Behavior change | None |
| SMART Goals | Low | 15-30 min | Goal setting | None |
| Habit Loop | Low | 20-30 min | Habit formation | None |
| Progressive Overload | Medium | 45-60 min | Training plan | Fitness baseline |
| Macro Tracking | Medium | 60-90 min | Nutrition plan | Body metrics |
| Recovery Protocol | Medium | 45-60 min | Recovery optimization | Training program |
| **Personal** |
| Pomodoro Technique | Low | 15-20 min | Daily planning | Task list |
| Atomic Habits | Low | 30-45 min | Habit building | None |
| Eisenhower Matrix | Low | 20-30 min | Prioritization | Task list |
| GTD System | High | 90-120 min | Productivity system | Commitment to process |
| Growth Mindset | Low | 20-30 min | Reflection, learning | Recent challenge |
| Deliberate Practice | Medium | 45-60 min | Skill development | Skill baseline |

---

**End of Domain Template Architecture Document**

**Next Steps**:
1. Review and approve this architecture
2. Create 24 individual template files based on specifications
3. Implement auto-population rules in Life OS workflow
4. Test composition patterns with real projects
5. Iterate based on user feedback

**Metadata**:
- **Document Version**: 1.0
- **Created**: 2026-02-04
- **Author**: Claude (Sonnet 4.5)
- **Status**: Draft for Review
- **Dependencies**: Life OS workflow, step-05-scoring.md, step-08-deep-plan.md
