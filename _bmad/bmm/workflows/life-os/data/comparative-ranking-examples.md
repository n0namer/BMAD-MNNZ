# Comparative Ranking Protocol & Examples

## Overview

Comparative ranking forces differentiation between projects by explicitly ranking them against each other for each criterion. This prevents grade inflation and reveals true relative priorities.

**When to use:**
- Evaluating 2-5 projects simultaneously
- Portfolio review sessions
- When absolute scoring risks grade inflation ("everything is a 4 or 5")

**Key Difference from Absolute:**
- Absolute: Each project scored independently (1-5 scale)
- Comparative: Projects ranked relative to each other, then converted to 1-5 scale

---

## Step-by-Step Protocol

### Step 1: Present All Projects

List all projects being compared with brief descriptions:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 COMPARATIVE RANKING: 3 PROJECTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Project A: Launch SaaS dashboard for productivity tracking
- Domain: Business/SaaS
- Timeframe: 3-6 months
- Key deliverable: MVP with 100 users

Project B: Write technical book on React patterns
- Domain: Personal/Business
- Timeframe: 6-12 months
- Key deliverable: Published book (200+ pages)

Project C: Build personal fitness habit (run 5K)
- Domain: Health
- Timeframe: 3 months
- Key deliverable: 5K run under 25 minutes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### Step 2: Rank Each Criterion (Forced Differentiation)

For EACH criterion, ask user to rank projects from **best to worst** (no ties allowed).

#### Example: Impact Ranking

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CRITERION: IMPACT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Which project has the HIGHEST potential impact if successful?
Rank from 1 (highest impact) to 3 (lowest impact):

Rank 1 (highest): ___
Rank 2 (middle): ___
Rank 3 (lowest): ___

Brief reasoning for ranking:
___
```

**User Response:**
```
Rank 1 (highest): Project A (SaaS dashboard)
Reasoning: Revenue-generating, affects multiple users daily, scalable business

Rank 2 (middle): Project B (React book)
Reasoning: Career impact + passive income, but limited to tech audience

Rank 3 (lowest): Project C (Fitness habit)
Reasoning: Personal benefit only, no broader impact
```

---

### Step 3: Convert Ranks to Scores

**Conversion Formula:**

For N projects ranked on a criterion:
- Best (Rank 1): 5.0 / 5
- Worst (Rank N): 1.0 / 5
- Middle ranks: Linear interpolation

**Formula:**
```
Score = 5.0 - ((Rank - 1) / (N - 1)) × 4.0
```

**Example (N=3):**
- Rank 1: 5.0 - (0 / 2) × 4.0 = 5.0
- Rank 2: 5.0 - (1 / 2) × 4.0 = 3.0
- Rank 3: 5.0 - (2 / 2) × 4.0 = 1.0

**Result:**
```
Impact Scores:
- Project A: 5.0 (Rank 1)
- Project B: 3.0 (Rank 2)
- Project C: 1.0 (Rank 3)
```

---

### Step 4: Repeat for All Criteria

Execute Step 2-3 for each criterion:

#### Confidence Ranking

```
CRITERION: CONFIDENCE (likelihood of success)

Rank 1 (highest): Project C (Fitness)
Reasoning: Proven approach, clear path, minimal dependencies

Rank 2 (middle): Project B (Book)
Reasoning: Have writing experience but book market uncertain

Rank 3 (lowest): Project A (SaaS)
Reasoning: Unvalidated market, technical complexity, competitive space

Converted Scores:
- Project C: 5.0
- Project B: 3.0
- Project A: 1.0
```

#### Effort Ranking (Negative - Lower is Better)

```
CRITERION: EFFORT (time/resources required)

Rank 1 (LEAST effort): Project C (Fitness)
Reasoning: 3 months part-time, no budget, solo

Rank 2 (middle): Project A (SaaS)
Reasoning: 3-6 months, $1-2K tools, solo but intense

Rank 3 (MOST effort): Project B (Book)
Reasoning: 6-12 months, high time commitment, ongoing

Converted Scores (remember: effort is negative):
- Project C: 5.0 (least effort)
- Project A: 3.0
- Project B: 1.0 (most effort)
```

#### Strategic Alignment Ranking

```
CRITERION: STRATEGIC ALIGNMENT (with defined goals)

Rank 1 (highest): Project A (SaaS)
Reasoning: Directly achieves Business 1yr goal ($10K MRR) + Finance 3yr goal (passive income)

Rank 2 (middle): Project C (Fitness)
Reasoning: Perfectly aligned with Health 1yr goal, but no Business/Finance impact

Rank 3 (lowest): Project B (Book)
Reasoning: Weak alignment across all domains (moderate Business, weak others)

Converted Scores:
- Project A: 5.0
- Project C: 3.0
- Project B: 1.0
```

#### Risk Ranking (Negative - Lower is Better)

```
CRITERION: RISK (probability × severity of failure)

Rank 1 (LOWEST risk): Project C (Fitness)
Reasoning: Worst case is status quo, no financial loss, only opportunity cost

Rank 2 (middle): Project B (Book)
Reasoning: Time investment but learning experience, reputation upside even if doesn't sell

Rank 3 (HIGHEST risk): Project A (SaaS)
Reasoning: Financial investment, market uncertainty, high failure rate in SaaS

Converted Scores (remember: risk is negative):
- Project C: 5.0 (lowest risk)
- Project B: 3.0
- Project A: 1.0 (highest risk)
```

---

### Step 5: Summary Matrix

Present all comparative scores in a matrix:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 COMPARATIVE SCORES MATRIX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Project | Impact | Confidence | Effort | Strategic | Risk | Overall |
|---------|--------|------------|--------|-----------|------|---------|
| A (SaaS)| 5.0    | 1.0        | 3.0    | 5.0       | 1.0  | ?       |
| B (Book)| 3.0    | 3.0        | 1.0    | 1.0       | 3.0  | ?       |
| C (Fitness)| 1.0 | 5.0        | 5.0    | 3.0       | 5.0  | ?       |

Legend:
- Positive criteria (higher is better): Impact, Confidence, Strategic
- Negative criteria (higher is better for score): Effort, Risk
```

---

### Step 6: Calculate Weighted Overall Scores

Apply standard MCDA weights to comparative scores.

**Weights (with goals available):**
```
- Impact: 0.269 (positive)
- Confidence: 0.162 (positive)
- Strategic Alignment: 0.269 (positive)
- Effort: -0.171 (negative)
- Risk: -0.129 (negative)
```

**Calculations:**

**Project A (SaaS):**
```
Impact: 5.0 × 0.269 = 1.345
Confidence: 1.0 × 0.162 = 0.162
Strategic: 5.0 × 0.269 = 1.345
Effort: 3.0 × -0.171 = -0.513
Risk: 1.0 × -0.129 = -0.129
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall: 2.210/10 raw → 6.2/10 normalized
```

**Project B (Book):**
```
Impact: 3.0 × 0.269 = 0.807
Confidence: 3.0 × 0.162 = 0.486
Strategic: 1.0 × 0.269 = 0.269
Effort: 1.0 × -0.171 = -0.171
Risk: 3.0 × -0.129 = -0.387
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall: 1.004/10 raw → 5.0/10 normalized
```

**Project C (Fitness):**
```
Impact: 1.0 × 0.269 = 0.269
Confidence: 5.0 × 0.162 = 0.810
Strategic: 3.0 × 0.269 = 0.807
Effort: 5.0 × -0.171 = -0.855
Risk: 5.0 × -0.129 = -0.645
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall: 0.386/10 raw → 4.4/10 normalized
```

---

### Step 7: Present Final Ranking with Interpretation

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏆 FINAL RANKING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**1. Project A: Launch SaaS Dashboard (6.2/10)**

Strengths:
✅ Highest Impact (5.0) - Revenue-generating, scalable
✅ Perfect Strategic Alignment (5.0) - Directly achieves goals
✅ Moderate Effort (3.0) - Manageable with part-time work

Weaknesses:
❌ Lowest Confidence (1.0) - Unvalidated market
❌ Highest Risk (1.0) - Financial investment, competitive

Recommendation: **Prioritize IF** you can validate market demand quickly (landing page + waitlist). Otherwise, consider validating via smaller MVP first.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**2. Project B: Write React Book (5.0/10)**

Strengths:
✅ Moderate Impact (3.0) - Career + passive income potential
✅ Moderate Confidence (3.0) - Have experience
✅ Low Risk (3.0) - Learning outcome even if doesn't sell

Weaknesses:
❌ Highest Effort (1.0) - 6-12 months ongoing commitment
❌ Lowest Strategic Alignment (1.0) - Weak fit with defined goals

Recommendation: **Consider IF** you have spare time and writing is a passion project. Otherwise, deprioritize in favor of higher-aligned projects.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**3. Project C: Build Fitness Habit (4.4/10)**

Strengths:
✅ Highest Confidence (5.0) - Clear proven path
✅ Lowest Effort (5.0) - Part-time, 3 months
✅ Lowest Risk (5.0) - No downside except opportunity cost

Weaknesses:
❌ Lowest Impact (1.0) - Personal benefit only, no business value
❌ Moderate Strategic Alignment (3.0) - Only Health domain covered

Recommendation: **Execute alongside** other projects. Low effort means no conflict with higher-priority work. Good for maintaining life balance.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### Step 8: Trade-off Analysis

Highlight key portfolio-level insights:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 PORTFOLIO INSIGHTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Key Trade-off: Impact vs. Confidence**
- Highest impact (SaaS) has lowest confidence
- Highest confidence (Fitness) has lowest impact
- Classic risk/reward trade-off visible

**Strategic Alignment Matters:**
- SaaS perfectly aligned → highest score despite low confidence
- Book poorly aligned → middle score despite balanced profile
- Demonstrates importance of goal definition

**Recommended Portfolio Approach:**
1. **Primary focus:** Project A (SaaS) - 70% time
   - Validate quickly before full commitment
   - Set kill criteria: if no interest after 100 waitlist signups, pivot

2. **Parallel maintenance:** Project C (Fitness) - 20% time
   - Low effort allows simultaneous execution
   - Maintains health while building business

3. **Defer:** Project B (Book) - 10% time (research only)
   - Weak alignment suggests waiting
   - Consider after SaaS achieves traction or validated as dead-end

**Resource Allocation:**
- Total effort: SaaS (3.0) + Fitness (5.0 effort but low intensity) = manageable
- Book (1.0 effort = 6-12 months) deferred saves ~15 hours/week for SaaS validation
```

---

## Example 2: 5 Projects (Larger Portfolio)

### Input: 5 Projects

```
Project A: Launch SaaS dashboard
Project B: Write React book
Project C: Build fitness habit
Project D: Freelance consulting (increase to $10K/month)
Project E: Learn machine learning (online course)
```

### Ranking: Impact

```
Rank 1 (highest): Project A (SaaS) - scalable revenue
Rank 2: Project D (Consulting) - immediate revenue increase
Rank 3: Project B (Book) - career + passive income
Rank 4: Project E (ML) - skill acquisition
Rank 5 (lowest): Project C (Fitness) - personal only

Converted Scores (N=5):
- Project A: 5.0
- Project D: 4.0
- Project B: 3.0
- Project E: 2.0
- Project C: 1.0
```

**Formula for 5 projects:**
```
Score = 5.0 - ((Rank - 1) / (5 - 1)) × 4.0
      = 5.0 - ((Rank - 1) / 4) × 4.0
```

**Rank → Score mapping:**
- Rank 1: 5.0 - (0/4) × 4.0 = 5.0
- Rank 2: 5.0 - (1/4) × 4.0 = 4.0
- Rank 3: 5.0 - (2/4) × 4.0 = 3.0
- Rank 4: 5.0 - (3/4) × 4.0 = 2.0
- Rank 5: 5.0 - (4/4) × 4.0 = 1.0

---

## Handling Ties (Not Recommended)

**Rule:** Comparative ranking should **force differentiation** (no ties).

**IF user insists on tie:**

```
⚠️ Warning: Ties reduce differentiation benefit of comparative ranking.

If Projects X and Y truly equal on this criterion:
- Both get average of their rank scores

Example: 3 projects, X and Y tied for Rank 1:
- Rank 1 (tie): X = 4.5, Y = 4.5 (average of Rank 1 [5.0] and Rank 2 [3.0])
- Rank 3: Z = 1.0
```

**Better approach:** Force tie-breaking by asking:
```
"If you HAD to choose one as slightly better on {criterion}, which would it be?
Even 1% better counts - there are no perfect ties in real decisions."
```

---

## When NOT to Use Comparative Ranking

**Avoid if:**
- Only 1 project (no comparison possible)
- Projects in completely different domains with no overlap (e.g., career vs. health vs. hobby)
- User needs absolute benchmark ("Is this idea objectively good?")
- Projects at vastly different stages (comparing MVP to mature product)

**Alternative:** Use absolute scoring with strict anchoring to prevent grade inflation.

---

## Differentiation Metrics

**After scoring, calculate differentiation metrics:**

### Spread (Range)

```
Spread = Max_Score - Min_Score

High spread (>3 points) = Clear differentiation
Low spread (<1 point) = Projects similar in quality
```

### Standard Deviation

```
StdDev = sqrt(Σ(Score - Mean)² / N)

High StdDev (>1.5) = Diverse portfolio
Low StdDev (<0.5) = Homogeneous portfolio
```

### Example:

```
Final Scores: 6.2, 5.0, 4.4

Spread: 6.2 - 4.4 = 1.8 (moderate differentiation)
Mean: 5.2
StdDev: 0.74 (moderate diversity)

Interpretation: Projects have meaningful differences but no extreme outliers.
Suggests balanced portfolio with clear top choice.
```

---

## Integration with Absolute Scores

**Can you mix approaches?**

Yes - use hybrid:
- **Comparative ranking** for relative prioritization
- **Absolute scoring** for absolute quality gates

**Example:**
```
Comparative ranking reveals:
1. Project A (6.2/10)
2. Project B (5.0/10)
3. Project C (4.4/10)

Absolute gate: "Proceed only if score ≥6.0"
→ Only Project A passes gate
→ Projects B and C deferred regardless of relative ranking
```

---

## References

- **Methodology:** `mcda-methodology.md`
- **Criteria Definitions:** `dfvc-criteria-rubric.md`
- **Calculator:** `scoring-calculator.md`
- **SaaS Rubric:** `saas-autonomy-rubric.md`
