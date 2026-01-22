# Confidence Calibration Framework

## Overview

Confidence scores in EMBER Consilium should reflect actual probability of recommendation success. This guide ensures confidence thresholds are well-calibrated through empirical testing and post-decision learning.

## Why Calibration Matters

**Overconfidence Example:**
```
You report 85% confidence in Option A
In reality, Option A succeeds only 65% of the time
Result: Stakeholder expects higher success rate than actual
Decision appears worse than analysis predicted
Trust in framework decreases
```

**Underconfidence Example:**
```
You report 65% confidence in Option A
In reality, Option A succeeds 82% of the time
Result: Stakeholder hesitates despite strong evidence
Valuable opportunity missed
Framework appears overly cautious
```

**Well-Calibrated:**
```
You report 80% confidence in Option A
In reality, Option A succeeds ~80% of the time
Result: Stakeholder expectations align with reality
Decision assessment aligns with outcomes
Trust in framework increases
Framework trustworthy
```

---

## Calibration Formula

### Step 1: Calculate Point Confidence (from Step-05c)

```
Base_Confidence = (Evidence_Strength × 0.4) + (Analytical_Rigor × 0.3) + (Perspective_Balance × 0.3)
```

**Example:**
```
Evidence_Strength = 0.82 (good sources, some gaps)
Analytical_Rigor = 0.75 (systematic methodology, some assumptions)
Perspective_Balance = 0.88 (stakeholders represented, one dissenting)

Base_Confidence = (0.82 × 0.4) + (0.75 × 0.3) + (0.88 × 0.3)
                = 0.328 + 0.225 + 0.264
                = 0.817
```

### Step 2: Adjust for Uncertainty Propagation

```
σ_Evidence = std dev across evidence sources (how much variation?)
σ_Rigor = std dev across methodology steps (how consistent?)
σ_Perspective = std dev across stakeholder views (how much disagreement?)

Uncertainty = sqrt((σ_Evidence/5)² + (σ_Rigor/5)² + (σ_Perspective/5)²)
```

**Example:**
```
σ_Evidence = 0.8 (sources vary 2 points on 5-scale: 3,4,5,3,4)
σ_Rigor = 0.6 (methodology fairly consistent)
σ_Perspective = 1.2 (significant stakeholder disagreement: 2,4,5,3)

Uncertainty = sqrt((0.8/5)² + (0.6/5)² + (1.2/5)²)
            = sqrt(0.0256 + 0.0144 + 0.0576)
            = sqrt(0.0976)
            = 0.0988 ≈ 0.10
```

### Step 3: Apply Penalty Factors

**Evidence Gap Penalty** (per missing evidence category):
```
Evidence_Gap_Penalty = 0.05 per category (Tech, Business, Ops, Risk)
Example: 1 category gap = -0.05
         2 categories = -0.10
```

**MCP Conflict Penalty** (per unresolved conflict):
```
MCP_Conflict_Penalty = 0.03 per unresolved conflict
Example: 2 unresolved conflicts = -0.06
```

**Stakeholder Misalignment Penalty** (if alignment <70%):
```
Misalignment_Penalty = 0.05 × (1 - alignment_percentage)
Example: 60% alignment = 0.05 × 0.40 = -0.02
```

**Near-Tie Penalty** (if top options within 0.3 points):
```
Near_Tie_Penalty = 0.20 (major uncertainty)
Example: Option A 4.2, Option B 3.95 → Indiscriminable
```

**Overconfidence Correction** (for suspicious perfect scores):
```
IF (confidence > 0.90 AND evidence_sources < 5) THEN
  Overconfidence_Correction = -0.10
ELSE
  Overconfidence_Correction = 0
```

**Total Penalties:**
```
Total_Penalty = Evidence_Gap + MCP_Conflict + Misalignment + Near_Tie + Overconfidence
```

### Step 4: Calculate Final Confidence

```
Final_Confidence_Point = Base_Confidence × (1 - Total_Penalty)

Confidence_Range:
  Lower_Bound = Final_Confidence_Point - Uncertainty
  Upper_Bound = Final_Confidence_Point + Uncertainty

Report: [Lower_Bound] - [Upper_Bound] (point: [Final_Confidence_Point])
```

**Complete Example:**
```
Base_Confidence = 0.817

Uncertainties:
  σ_Evidence = 0.08
  σ_Rigor = 0.06
  σ_Perspective = 0.12
  Combined Uncertainty = 0.10

Penalties:
  Evidence Gap (1 category): -0.05
  MCP Conflicts (0): 0.00
  Stakeholder Misalignment (75%): -0.0125
  Near-tie: 0.00 (clear difference)
  Overconfidence correction: 0.00 (8 sources)
  Total Penalty = -0.0625

Final_Confidence_Point = 0.817 × (1 - 0.0625) = 0.766

Confidence_Range = 0.766 ± 0.10 = 0.666 - 0.866

REPORT: "Confidence 0.67 - 0.87 (point estimate: 0.77)"
```

---

## Calibration Validation (Post-Decision)

### Track Confidence vs. Actual Outcome

After decision implementation, record:
```
Decision: [Name]
Reported Confidence: 0.77 (point)
Reported Range: 0.67 - 0.87
Actual Outcome: [Success / Partial / Failure]
```

### Calibration Accuracy Assessment

```
If using 75-80% confidence threshold:
  - 100+ decisions with 75-80% confidence
  - What % actually succeeded?

CALIBRATION CHECK:
Success Rate    | Assessment        | Action
>85%           | UNDERCONFIDENT   | Increase thresholds next time
80-85%         | WELL-CALIBRATED  | Maintain current formula
70-80%         | SLIGHT OVERCONFIDENT | Minor adjustment
<70%           | OVERCONFIDENT    | Significant formula revision
```

### Confidence Threshold Adjustment

If data shows overconfidence:

```
ADJUSTMENT FORMULA:
New_Threshold = Current_Threshold × (Actual_Success_Rate / Expected_Success_Rate)

Example:
Current threshold: 80% confidence
Actual success rate for 80% confidence: 70%
Expected success rate: 80%

New_Threshold = 0.80 × (0.70 / 0.80) = 0.70 (lower to 70%)
Interpretation: Only count decisions as high-confidence if they meet 70% threshold
```

---

## Psychological Bias Corrections in Calibration

### 1. Overconfidence Bias

**Problem:** People naturally report 75% confidence even for 50/50 choices

**Correction:**
```
IF (confidence > 0.85 AND evidence_base_small) THEN
  Apply penalty of -0.10

Rationale: Extremely high confidence requires extensive evidence
```

### 2. Disconfirmatory Evidence Bias

**Problem:** Late-arriving contradictory evidence disproportionately reduces confidence

**Correction:**
```
IF (major_conflict_found_in_final_20%_of_analysis) THEN
  Re-assess entire evidence base rather than anchoring on conflict
  Explicitly ask: "Would this conflict have changed my analysis if found earlier?"
```

### 3. Anchoring Bias

**Problem:** Early confidence estimates persist despite new evidence

**Correction:**
```
Explicit recomputation required if:
  - Major unexpected evidence discovered
  - Key assumption invalidated
  - New stakeholder perspective adds
```

---

## Confidence Range Interpretation

### What the Range Means

```
Reported: 0.68 - 0.82 (point: 0.75)

MEANS:
- Point estimate of success probability: 75%
- With our measurement uncertainty: 68-82%
- Real probability likely falls in that range
- But don't over-interpret: 0.75 vs 0.74 are equivalent
```

### What the Range Does NOT Mean

```
❌ "68% chance of failure" - NO, 0.68-0.82 is confidence in analysis, not failure probability
❌ "Exactly 75% will succeed" - NO, it's a range reflecting uncertainty
❌ "We're 95% sure it's in this range" - NO, this range is ~±1 std dev (~68% confidence interval)
```

---

## Updating Confidence Over Time

As evidence accumulates during analysis:

```
Phase 1 (Evidence gathering): Confidence low (0.40-0.60)
Phase 2 (Evidence validation): Confidence increases (0.60-0.75)
Phase 3 (Matrix evaluation): Confidence stable (0.65-0.85)
Phase 4 (Validation): Confidence final (0.60-0.90)

IMPORTANT: Don't let confidence artificially increase just because
you've done more analysis. If underlying evidence didn't improve,
confidence shouldn't improve.
```

---

## Building Confidence Calibration Database

Over time, create organizational database:

```
Decision 1: Reported 0.82 confidence → Actual: SUCCESS
Decision 2: Reported 0.75 confidence → Actual: PARTIAL
Decision 3: Reported 0.68 confidence → Actual: FAILURE
Decision 4: Reported 0.78 confidence → Actual: SUCCESS
...

After 50+ decisions:
Confidence 0.75-0.80 has X% actual success rate
Calibration accuracy: [assessment]
```

This allows continuous improvement of the framework.

---

## Summary: Calibration Checklist

- [ ] Base confidence calculated from evidence/rigor/perspective
- [ ] Uncertainty propagation computed from standard deviations
- [ ] All penalty factors identified and calculated
- [ ] Final confidence computed (not just averaged)
- [ ] Confidence range generated (not just point estimate)
- [ ] Psychological bias corrections applied
- [ ] Range interpretation provided (with caveats)
- [ ] Confidence vs. success tracked post-decision
- [ ] Calibration accuracy reviewed quarterly
- [ ] Framework adjusted based on calibration findings
