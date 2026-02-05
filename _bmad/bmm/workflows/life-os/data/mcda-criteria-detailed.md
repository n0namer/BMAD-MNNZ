# MCDA Scoring Criteria - Detailed Definitions

## Base Criteria (Always Applied)

### 1. Impact (0.25 weight default)
**Definition:** Potential magnitude of positive change if successful

**Scoring Anchors:**
- **1 (Low):** Minimal improvement, affects small subset of users/processes
- **3 (Medium):** Noticeable improvement, moderate scope
- **5 (High):** Transformational change, broad positive impact

**Evidence Required:**
- Quantified metrics (revenue, time saved, users affected)
- Competitor analysis or market data
- User research or customer interviews

**Quality Question:** "Why not higher?" - What limits the impact ceiling?

---

### 2. Confidence (0.15 weight default)
**Definition:** Certainty about successfully executing and achieving stated impact

**Scoring Anchors:**
- **1 (Low):** High uncertainty, many unknowns, unproven approach
- **3 (Medium):** Moderate confidence, some risks, validated approach
- **5 (High):** High certainty, proven method, minimal unknowns

**Evidence Required:**
- Past similar project outcomes
- Team expertise assessment
- Technical feasibility validation

**Quality Question:** "Why not higher?" - What creates uncertainty?

---

### 3. Effort (0.20 weight default, negative)
**Definition:** Resources required (time, people, budget, complexity)

**Scoring Anchors:**
- **1 (Low Effort):** Quick win, minimal resources, simple execution
- **3 (Medium Effort):** Moderate investment, standard complexity
- **5 (High Effort):** Major investment, complex execution, long timeline

**Evidence Required:**
- T-shirt sizing (S/M/L/XL)
- Resource allocation estimate
- Dependency mapping

**Quality Question:** "Why not higher?" - What reduces required effort?

**Note:** Effort is weighted negatively (higher effort = lower priority)

---

### 4. Risk (0.15 weight default, negative)
**Definition:** Likelihood and severity of negative outcomes

**Scoring Anchors:**
- **1 (Low Risk):** Minimal downside, reversible, safe to fail
- **3 (Medium Risk):** Moderate downside, some irreversibility
- **5 (High Risk):** Significant downside, irreversible, critical failure mode

**Evidence Required:**
- Risk register (top 3-5 risks identified)
- Mitigation strategies outlined
- Blast radius assessment

**Quality Question:** "Why not higher?" - What mitigates the risk?

**Note:** Risk is weighted negatively (higher risk = lower priority)

---

### 5. Strategic Alignment (0.25 weight default, requires goals.yaml)
**Definition:** Fit with defined long-term goals and direction

**Scoring Anchors:**
- **1 (Low Alignment):** Tangential to goals, no clear connection
- **3 (Medium Alignment):** Supports goals indirectly, partial fit
- **5 (High Alignment):** Direct contribution to primary goals, strong fit

**Evidence Required:**
- Explicit mapping to goals.yaml objectives
- Theory of change explaining connection
- Success metrics linked to goal KPIs

**Quality Question:** "Why not higher?" - What prevents full alignment?

**Note:** Skipped if goals not defined (GOALS_AVAILABLE = false)

---

## Domain-Specific Criteria (Auto-Added Based on Frameworks)

### Business Domain

**Market Opportunity (0.10 weight)**
- **Definition:** Size and growth potential of addressable market
- **Evidence:** Market size data, growth rates, competitive landscape

**Competitive Advantage (0.10 weight)**
- **Definition:** Unique value proposition vs competitors
- **Evidence:** Differentiation analysis, moat assessment

---

### Finance Domain

**Expected Value (0.15 weight)**
- **Definition:** Probabilistic financial return (revenue, savings, ROI)
- **Evidence:** Revenue projections, cost-benefit analysis, NPV calculation

**Option Value (0.10 weight)**
- **Definition:** Future opportunities unlocked by this initiative
- **Evidence:** Follow-on projects enabled, strategic options created

---

### Health Domain

**Readiness (HBM) (0.10 weight)**
- **Definition:** Preparedness to change based on Health Belief Model
- **Evidence:** Self-efficacy assessment, perceived barriers, motivations

**Sustainability (0.10 weight)**
- **Definition:** Long-term maintainability of habit or behavior
- **Evidence:** Habit formation plan, relapse prevention strategy

---

### Personal Development Domain

**Skill Impact (0.10 weight)**
- **Definition:** Competency gained or improved through project
- **Evidence:** Skill gap analysis, learning objectives, mastery criteria

**Time Commitment (0.10 weight, negative)**
- **Definition:** Ongoing time investment required post-launch
- **Evidence:** Maintenance schedule, recurring tasks identified

---

## Weight Normalization Rules

**Total weights MUST sum to 1.0:**
- When domain criteria added, base criteria weights reduced proportionally
- User can manually adjust weights (must re-normalize)
- Negative criteria (Effort, Risk) retain negative sign

**Example Calculation:**
```
Base: Impact (0.25) + Confidence (0.15) + Effort (-0.20) + Strategic (0.25) + Risk (-0.15) = 0.30
+ Domain: Market Opportunity (0.10) + Competitive Advantage (0.10) = 0.20
= Total positive weights: 0.50

Normalized:
Impact: 0.25 * (0.80/0.50) = 0.40
Confidence: 0.15 * (0.80/0.50) = 0.24
Strategic: 0.25 * (0.80/0.50) = 0.40
Effort: -0.20 (unchanged)
Risk: -0.15 (unchanged)
Market Opportunity: 0.10
Competitive Advantage: 0.10
Total = 1.00
```

---

## Quality Standards for Scoring Output

**Minimum Requirements (600-800 words total):**
- ✅ Every score justified with reasoning (not just numbers)
- ✅ Evidence provided (data, competitor analysis, interviews)
- ✅ "Why not higher?" ceiling explained for each criterion
- ✅ Weighted calculation shown (MCDA)
- ✅ Sensitivity analysis included (what-if scenarios)
- ✅ Clear decision with rationale

**Reference:** See `validation-examples.md` for WRONG vs RIGHT scoring examples
