# Comparative Ranking Protocol

## Overview

**Purpose:** Prevent grade inflation by forcing relative ranking across multiple ideas

**When to Use:**
- 2+ ideas need prioritization (Comparative mode)
- 3+ ideas in portfolio intake (Batch mode)

**Benefits:**
- Clear differentiation (no ties)
- Forces trade-off thinking
- More accurate prioritization than absolute scoring

---

## Scoring Modes

### [A] Absolute Mode
**When:** Single idea, or ideas are very different
**Process:** Score each idea independently (0-5 scale)
**Risk:** Grade inflation (all ideas score 3.5-4.0)
**Use case:** First idea in portfolio, or radically different domains

---

### [C] Comparative Mode (Recommended for 2+ ideas)
**When:** 2+ ideas need prioritization
**Process:** Rank ideas against each other per criterion
**Benefit:** Forced differentiation, clear winner

**Step-by-Step:**

1. **Load All PLANNED Ideas**
   ```bash
   # Retrieve from memory/workflow plans
   Ideas to compare:
   1. {Idea A Name} (current idea)
   2. {Idea B Name} (from memory)
   3. {Idea C Name} (from memory)
   ```

2. **Rank Per Criterion**
   For EACH criterion below, ask:
   **"Which idea ranks highest for [Criterion]?"**

   **Criteria (reference: `data/comparative-scoring-criteria.yaml`):**
   - **Impact Magnitude** - Which has bigger potential impact?
   - **Strategic Fit** - Which aligns better with long-term direction?
   - **Execution Confidence** - Which are you more confident executing?
   - **Time-to-Value** - Which delivers value faster?
   - **Resource Efficiency** - Which uses resources more efficiently?
   - **Risk Level** - Which has lower risk? (lower = better)

   **User Response Format:**
   ```
   Impact Magnitude: [A] Idea A | [B] Idea B | [C] Idea C
   Strategic Fit: [A] Idea A | [B] Idea B | [C] Idea C
   Execution Confidence: [A] Idea A | [B] Idea B | [C] Idea C
   Time-to-Value: [A] Idea A | [B] Idea B | [C] Idea C
   Resource Efficiency: [A] Idea A | [B] Idea B | [C] Idea C
   Risk Level: [A] Idea A | [B] Idea B | [C] Idea C
   ```

3. **Calculate Aggregate Ranking**
   - Count "wins" per idea across all criteria
   - Idea with most wins = Rank 1
   - Break ties with forced differentiation (see below)

4. **Normalize to Scores**
   ```
   Rank 1: 5.0
   Rank 2: 4.5
   Rank 3: 4.0
   Rank 4: 3.5
   Rank 5+: 3.0
   ```

5. **Present Results**
   ```
   🎯 Scoring Results (Comparative)

   Rank | Idea Name | Normalized Score | Your Ranking Reason
   -----|-----------|------------------|---------------------
     1  | Idea A    | 5.0              | Highest impact, strategic fit
     2  | Idea B    | 4.5              | Fast execution, lower risk
     3  | Idea C    | 4.0              | Good idea but lower priority

   ✅ Clear differentiation: Δ(1-2) = 0.5, Δ(2-3) = 0.5
   ```

---

### [B] Batch Mode (3+ ideas, side-by-side)
**When:** Portfolio intake with multiple ideas
**Process:** Show comparison matrix, score all at once
**Benefit:** Fastest for multiple ideas, visual comparison

**Step-by-Step:**

1. **Present Comparison Matrix**
   ```
   📊 Batch Scoring Matrix

   Idea | Impact | Strategic Fit | Execution | Time-to-Value | Resources | Risk | Total
   -----|--------|---------------|-----------|---------------|-----------|------|------
   A    | ___    | ___           | ___       | ___           | ___       | ___  | ___
   B    | ___    | ___           | ___       | ___           | ___       | ___  | ___
   C    | ___    | ___           | ___       | ___           | ___       | ___  | ___

   Rank each idea 1-5 for each criterion.
   ```

2. **Collect Scores**
   User fills in matrix with values 1-5

3. **Calculate Totals**
   Sum weighted scores per idea

4. **Apply Forced Differentiation**
   If any two ideas score within 0.3 points → Force ranking (see below)

---

## Forced Differentiation Logic

**When to Trigger:**
- Multiple ideas score identically (within 0.3 points)
- Prevents artificial ties

**Process:**

1. **Detect Tie**
   ```
   ⚠️ Multiple ideas scored identically:
   - Idea A: 3.8
   - Idea B: 3.8
   - Idea C: 3.8
   ```

2. **Force User to Differentiate**
   ```
   Please differentiate - which is slightly better?
   Rank order: 1st → 2nd → 3rd
   (Even small differences help prioritization)

   Your ranking: ___ → ___ → ___
   ```

3. **Apply Micro-Adjustments**
   ```
   Rank 1: Original score + 0.2 (3.8 → 4.0)
   Rank 2: Original score (3.8 → 3.8)
   Rank 3: Original score - 0.2 (3.8 → 3.6)
   ```

4. **Confirm with User**
   ```
   Adjusted scores:
   - Idea A: 4.0 (ranked 1st - you prioritized this)
   - Idea B: 3.8 (ranked 2nd)
   - Idea C: 3.6 (ranked 3rd)

   Accept? [Y/N]
   ```

---

## Integration with MCDA Criteria

**Comparative ranking criteria map to base MCDA criteria:**

| Comparative Criterion | MCDA Base Criterion | Weight Reference |
|-----------------------|---------------------|------------------|
| Impact Magnitude      | Impact              | 0.25 (default)   |
| Strategic Fit         | Strategic Alignment | 0.25 (default)   |
| Execution Confidence  | Confidence          | 0.15 (default)   |
| Time-to-Value         | Effort (inverse)    | 0.20 (negative)  |
| Resource Efficiency   | Effort (inverse)    | 0.20 (negative)  |
| Risk Level            | Risk (inverse)      | 0.15 (negative)  |

**Note:** See `data/mcda-criteria-detailed.md` for full MCDA methodology

---

## Example Comparative Ranking Session

**Setup:**
- 3 ideas: "Mobile App", "API Platform", "Data Pipeline"
- User selects Comparative mode [C]

**Step 1: Load Ideas**
```
Ideas to compare:
1. Mobile App (current)
2. API Platform (from memory)
3. Data Pipeline (from memory)
```

**Step 2: Rank Per Criterion**
```
Impact Magnitude: [C] Data Pipeline (biggest impact)
Strategic Fit: [A] Mobile App (aligns with customer-first strategy)
Execution Confidence: [B] API Platform (team has API experience)
Time-to-Value: [A] Mobile App (quickest to launch)
Resource Efficiency: [B] API Platform (least resources)
Risk Level: [A] Mobile App (lowest risk)
```

**Step 3: Count Wins**
```
Mobile App: 3 wins (Strategic Fit, Time-to-Value, Risk)
API Platform: 2 wins (Execution, Resources)
Data Pipeline: 1 win (Impact)
```

**Step 4: Normalize**
```
Rank 1: Mobile App → 5.0
Rank 2: API Platform → 4.5
Rank 3: Data Pipeline → 4.0
```

**Step 5: Present**
```
🎯 Scoring Results (Comparative)

Rank | Idea         | Score | Reasoning
-----|--------------|-------|----------
  1  | Mobile App   | 5.0   | Best strategic fit, fastest, safest
  2  | API Platform | 4.5   | High confidence, efficient
  3  | Data Pipeline| 4.0   | High impact but slower/riskier

✅ Clear differentiation achieved
```

---

## Quality Validation for Comparative Scoring

**Checklist:**
- ☐ All ideas ranked for ALL criteria (no skipped criteria)
- ☐ Forced differentiation applied if ties detected
- ☐ Reasoning provided for each ranking decision
- ☐ Final scores confirmed with user
- ☐ Clear winner identified (Rank 1 = highest priority)

**Reference:** See `data/comparative-scoring-criteria.yaml` for detailed criteria definitions
