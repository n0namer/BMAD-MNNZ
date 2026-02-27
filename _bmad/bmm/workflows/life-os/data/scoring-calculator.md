# Scoring Calculator Protocol

## Overview

This document provides step-by-step calculation protocols for all scoring modes (Absolute, Comparative, Batch).

---

## Mode 1: Absolute Scoring

### Step 1: Collect Individual Criterion Scores

For each criterion, ask user:
```
{Criterion Name} (1-5 scale):
{Anchor description from rubric}

Your score: ___ /5
Brief reasoning: ___
```

**Example:**
```
Impact (1-5 scale):
1 = Negligible benefit
3 = Noticeable improvement
5 = Transformative, life-changing

Your score: 4 /5
Brief reasoning: Solves daily bottleneck affecting 500+ users, 40% time savings expected
```

### Step 2: Verify Score Justification

For each score, ensure:
- ✅ Reasoning provided (not just number)
- ✅ Evidence mentioned (data, examples, comparisons)
- ✅ "Why not higher?" explained for scores <5

**If missing:** Prompt user:
```
⚠️ Score needs justification. Please explain:
- Why {score} instead of {score-1}?
- Why NOT {score+1}?
- What evidence supports this score?
```

### Step 3: Load Weights

**IF goals.yaml exists AND domain = 'saas'/'software':**
```
Normalized weights (6 criteria):
- Impact: 0.219
- Confidence: 0.131
- Strategic Alignment: 0.219
- SaaS Autonomy: 0.131
- Effort: -0.171
- Risk: -0.129
```

**IF goals.yaml exists AND domain ≠ 'saas'/'software':**
```
Normalized weights (5 criteria):
- Impact: 0.269
- Confidence: 0.162
- Strategic Alignment: 0.269
- Effort: -0.171
- Risk: -0.129
```

**IF goals.yaml NOT exists:**
```
Simplified weights (4-5 criteria):
- Impact: 0.500 (or 0.438 if SaaS Autonomy added)
- Confidence: 0.200 (or 0.175 if SaaS Autonomy added)
- SaaS Autonomy: 0.087 (if SaaS domain)
- Effort: -0.214 (or -0.188 if SaaS Autonomy added)
- Risk: -0.086 (or -0.075 if SaaS Autonomy added)
```

**Confirm with user:**
```
📊 Scoring weights:
{list weights}

Adjust weights? [Y/n]
```

**IF user selects [Y]:** Allow custom weight entry, then re-normalize to 70/30 split.

### Step 4: Calculate Overall Score

**Formula:**
```
Overall_Score = Σ(Criterion_Score × Normalized_Weight)
```

**Example (with goals, non-SaaS):**
```
Impact: 4 × 0.269 = 1.076
Confidence: 4 × 0.162 = 0.648
Strategic Alignment: 5 × 0.269 = 1.345
Effort: 3 × -0.171 = -0.513
Risk: 2 × -0.129 = -0.258
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall Score: 2.298 (raw)

Normalized to 10-point scale:
(2.298 + 3) / 10 × 10 = 5.3/10
```

### Step 5: Present Results

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 SCORING RESULTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Overall Score:** {score}/10

**Weighted Breakdown:**
- Impact: {score} × {weight} = {contribution}
- Confidence: {score} × {weight} = {contribution}
- Strategic Alignment: {score} × {weight} = {contribution}
- Effort: {score} × {weight} = {contribution}
- Risk: {score} × {weight} = {contribution}

**Decision Rationale:**
{2-3 bullets summarizing key drivers}

**Key Risks:**
{1-2 bullets on main concerns}

**Confidence in Score:** {interpretation}
```

---

## Mode 2: Comparative Ranking

**See:** `comparative-ranking-examples.md` for full protocol

### Quick Overview

**Step 1:** Present all projects side-by-side
**Step 2:** For EACH criterion, force-rank projects (no ties)
**Step 3:** Convert ranks to normalized scores:
- Best: 5/5
- Worst: 1/5
- Middle: Linear interpolation

**Step 4:** Apply weights and calculate as in Absolute mode

**Key Difference:** Scores determined by relative ranking, not absolute assessment.

---

## Mode 3: Batch Scoring (Matrix)

### Step 1: Create Comparison Matrix

Present all projects and criteria in table format:

```
| Project | Impact | Confidence | Effort | Strategic | Risk | Overall |
|---------|--------|------------|--------|-----------|------|---------|
| Idea A  |   ?    |     ?      |   ?    |     ?     |  ?   |    ?    |
| Idea B  |   ?    |     ?      |   ?    |     ?     |  ?   |    ?    |
| Idea C  |   ?    |     ?      |   ?    |     ?     |  ?   |    ?    |
```

### Step 2: Score Column-by-Column

For each criterion:
```
Let's score all projects on {Criterion Name}.

Idea A ({brief description}): ___ /5
Idea B ({brief description}): ___ /5
Idea C ({brief description}): ___ /5

Brief comparison: Why these differences?
```

### Step 3: Calculate Overall Scores

Apply standard weighted formula for each project independently.

### Step 4: Rank and Highlight Trade-offs

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 PORTFOLIO COMPARISON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Ranking:**
1. {Project Name} - {score}/10
   Strengths: {key strengths}
   Weaknesses: {key weaknesses}

2. {Project Name} - {score}/10
   Strengths: {key strengths}
   Weaknesses: {key weaknesses}

3. {Project Name} - {score}/10
   Strengths: {key strengths}
   Weaknesses: {key weaknesses}

**Trade-off Analysis:**
- {Observation about portfolio balance}
- {Observation about resource allocation}
```

---

## Special Calculations

### Strategic Alignment Score (Conditional)

**Trigger:** Only if `goals.yaml` exists

**Step 1: Load Goals**
```yaml
goals:
  finance:
    1_year: "{goal_text}"
    3_years: "{goal_text}"
    5_10_years: "{goal_text}"
  business: {...}
  health: {...}
  personal: {...}

alignmentWeights:
  1_year: 0.5
  3_years: 0.3
  5_10_years: 0.2
```

**Step 2: Score Each Goal (12 total)**

For each domain and timeframe:
```
{Domain} - {Timeframe} Goal: "{goal_text}"
How does this idea align? (1-5 scale)

Your score: ___ /5
Reasoning: ___
```

**Step 3: Calculate Domain Averages**
```
Finance_Alignment = (1yr_score × 0.5) + (3yr_score × 0.3) + (5_10yr_score × 0.2)
Business_Alignment = (1yr_score × 0.5) + (3yr_score × 0.3) + (5_10yr_score × 0.2)
Health_Alignment = (1yr_score × 0.5) + (3yr_score × 0.3) + (5_10yr_score × 0.2)
Personal_Alignment = (1yr_score × 0.5) + (3yr_score × 0.3) + (5_10yr_score × 0.2)
```

**Step 4: Calculate Overall Strategic Alignment**
```
Strategic_Alignment_Score = (Finance + Business + Health + Personal) / 4
```

**Step 5: Present Domain Breakdown**
```
**Strategic Alignment: {score}/5.0**

Domain Breakdown:
- Finance: {score}/5 (1yr:{1yr}, 3yr:{3yr}, 5-10yr:{5_10yr})
- Business: {score}/5 (1yr:{1yr}, 3yr:{3yr}, 5-10yr:{5_10yr})
- Health: {score}/5 (1yr:{1yr}, 3yr:{3yr}, 5-10yr:{5_10yr})
- Personal: {score}/5 (1yr:{1yr}, 3yr:{3yr}, 5-10yr:{5_10yr})

Strongest Alignment: {domain} domain, {timeframe} goals
Weakest Alignment: {domain} domain, {timeframe} goals
```

---

### SaaS Autonomy Score (Conditional)

**Trigger:** Only if `domain = 'saas'` OR `domain = 'software'`

**Step 1: Score 4 Sub-Pillars**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 SaaS Autonomy Assessment
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Pillar 1: Self-Signup (0.25 weight)
How easy is signup for new users?
1 = Enterprise sales (weeks), 5 = 1-click OAuth (<5 seconds)

Your score: ___ /5
Reasoning: ___

Pillar 2: Self-Billing (0.30 weight)
How automated is payment management?
1 = Manual invoicing, 5 = Usage-based + smart dunning

Your score: ___ /5
Reasoning: ___

Pillar 3: Self-Service Support (0.30 weight)
How self-sufficient are users?
1 = Dedicated CSM (50%+ contact), 5 = AI support (<1% contact)

Your score: ___ /5
Reasoning: ___

Pillar 4: Autonomous Operation (0.15 weight)
How much manual infrastructure work?
1 = Daily manual work, 5 = Fully autonomous (99.9% uptime)

Your score: ___ /5
Reasoning: ___
```

**Step 2: Calculate SaaS Autonomy Score**

```
SaaS_Autonomy_Score = (Self_Signup × 0.25) + (Self_Billing × 0.30) +
                      (Self_Service_Support × 0.30) + (Autonomous_Operation × 0.15)
```

**Example:**
```
Self-Signup: 4 × 0.25 = 1.00
Self-Billing: 3 × 0.30 = 0.90
Self-Service Support: 3 × 0.30 = 0.90
Autonomous Operation: 4 × 0.15 = 0.60
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SaaS Autonomy Score: 3.40/5.0
```

**Step 3: Classify and Interpret**

| Score Range | Classification | Team Size | Business Model | Passive Income |
|-------------|---------------|-----------|----------------|----------------|
| 4.5-5.0 | Highly Autonomous | Solo feasible | Product-led growth | ✅ High |
| 3.5-4.4 | Moderately Autonomous | 2-5 team | Hybrid PLG + light touch | ⚠️ Medium |
| 2.5-3.4 | Limited Autonomy | 5-10 team | Sales-assisted | ❌ Low |
| 1.0-2.4 | Low Autonomy | 10+ team | High-touch enterprise | ❌ None |

**Step 4: Check Risk Flags**

**⚠️ Flag 1: High Support Load Risk**
- Trigger: `SaaS_Autonomy < 3.0`
- Warning: Significant ongoing support team needed, operational costs may exceed revenue for 6-12 months
- Recommendation: Improve self-service capabilities before launch

**⚠️ Flag 2: Manual Operations Bottleneck**
- Trigger: `Autonomous_Operation < 2.5`
- Warning: Manual operations limit scaling, solo founder not feasible
- Recommendation: Invest in infrastructure automation (CI/CD, auto-scaling, monitoring)

**⚠️ Flag 3: Consider Enterprise Model Instead**
- Trigger: `SaaS_Autonomy < 2.0`
- Warning: Closer to managed service than true SaaS, passive income unlikely
- Recommendation: Either (1) redesign for more automation, OR (2) pivot to B2B enterprise with higher pricing

---

## Sensitivity Analysis (Deep Track Only)

**Purpose:** Test how overall score changes if key assumptions vary.

**Step 1: Identify Key Variables**

From scoring rationale, identify 2-3 most uncertain assumptions.

**Example:**
- Impact score assumes 40% time savings (based on competitor data)
- Effort score assumes solo development feasible (unvalidated)
- Confidence score assumes technology is proven (minimal unknowns)

**Step 2: Define Scenarios**

For each variable, define optimistic/pessimistic scenarios:

```
Base Case: Impact = 4, Effort = 3, Overall = 6.4/10

Scenario 1: Impact Lower (4 → 3)
- Assumption: Time savings only 20% instead of 40%
- New Overall Score: ?

Scenario 2: Effort Higher (3 → 4)
- Assumption: Need part-time designer, adds 2 months
- New Overall Score: ?

Scenario 3: Combined Pessimistic (Impact 3, Effort 4)
- Both assumptions wrong
- New Overall Score: ?
```

**Step 3: Recalculate Scores**

Use same weights, update only changed criterion scores.

**Step 4: Calculate % Change**

```
% Change = (New_Score - Base_Score) / Base_Score × 100
```

**Step 5: Present Sensitivity Results**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 SENSITIVITY ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Base Case: 6.4/10

Scenario 1: Impact Lower (4→3)
New Score: 5.3/10 (-17% change)
Interpretation: Score highly sensitive to Impact

Scenario 2: Effort Higher (3→4)
New Score: 6.0/10 (-6% change)
Interpretation: Score moderately sensitive to Effort

Scenario 3: Combined Pessimistic
New Score: 4.9/10 (-23% change)
Interpretation: Combined effect worse than sum of parts

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 RECOMMENDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Score most sensitive to: Impact assumption
Action: Validate time savings claim before proceeding
Method: User testing with prototype (5 users, 2 weeks)
```

---

## Output Format Templates

### Standard Output (Absolute Mode)

```markdown
## Scoring Summary

**Criteria Scores (1–5):**
- Impact: {score} — {rationale + evidence + ceiling}
- Confidence: {score} — {rationale + evidence + ceiling}
- Effort: {score} — {rationale + evidence + ceiling}
- Strategic Alignment: {score} — {rationale + evidence + ceiling}
- Risk: {score} — {rationale + evidence + ceiling}
{If SaaS domain}
- SaaS Autonomy: {score} — {classification + breakdown}

**Overall Score:** {score}/10 (method: {weighted/comparative/batch})

**Decision Rationale:**
- {key driver 1}
- {key driver 2}
- {key driver 3}

{If strategic alignment scored}
**Strategic Insights:**
- Strongest Alignment: {domain} domain, {timeframe} goals
- Weakest Alignment: {domain} domain, {timeframe} goals
- {insight}

{If SaaS autonomy scored}
**SaaS Business Implications:**
- Team Size: {solo / 2-5 / 5-10 / 10+}
- Model Fit: {PLG / Hybrid / Sales-assisted / High-touch}
- Passive Income: {High / Medium / Low / None}

{If risk flags triggered}
⚠️ **Risk Flags:**
- {flag description}
- Recommendation: {recommendation}
```

---

## Validation Checklist

Before finalizing scores, verify:

- ✅ Every score has reasoning (not just numbers)
- ✅ Evidence provided (data, examples, comparisons)
- ✅ "Why not higher?" explained for scores <5
- ✅ Weighted calculation shown with formula
- ✅ Total output 600-800 words minimum
- ✅ Clear decision recommendation
- ✅ Key risks acknowledged
- ✅ Strategic implications considered (if goals available)

---

## References

- **Methodology:** `mcda-methodology.md`
- **Criteria Definitions:** `dfvc-criteria-rubric.md`
- **Comparative Examples:** `comparative-ranking-examples.md`
- **SaaS Rubric:** `saas-autonomy-rubric.md`
