# Multi-Criteria Decision Analysis (MCDA) Methodology

## Overview

This guide provides a comprehensive framework for applying MCDA to project prioritization and decision-making, integrating **AHP (Analytic Hierarchy Process)** for criterion weighting and **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** for alternative ranking.

---

## Part 1: AHP (Analytic Hierarchy Process) - Criterion Weighting

### Purpose
Determine relative importance weights for decision criteria through systematic pairwise comparisons.

### 1.1 Pairwise Comparison Scale

| Intensity | Definition | Explanation |
|-----------|------------|-------------|
| 1 | Equal importance | Two criteria contribute equally |
| 3 | Moderate importance | Experience/judgment slightly favors one |
| 5 | Strong importance | Experience/judgment strongly favors one |
| 7 | Very strong importance | One criterion is strongly favored |
| 9 | Extreme importance | Evidence favoring one is of highest order |
| 2, 4, 6, 8 | Intermediate values | When compromise is needed |

**Reciprocals**: If criterion A has intensity 5 vs criterion B, then B vs A = 1/5

### 1.2 Building the Pairwise Comparison Matrix

**Example: 4 Criteria (Impact, Effort, Risk, Timeline)**

```
Question for each pair: "How much more important is criterion A than criterion B?"

           Impact  Effort  Risk  Timeline
Impact        1      5      3       7
Effort       1/5     1     1/3      3
Risk         1/3     3      1       5
Timeline     1/7    1/3    1/5      1
```

**Matrix Properties**:
- Diagonal = 1 (criterion vs itself)
- Symmetric: a[i,j] = 1/a[j,i]
- n×n matrix for n criteria

### 1.3 Calculating Criterion Weights

**Step 1: Normalize Each Column**

Sum each column, then divide each cell by its column sum:

```
Column sums:
Impact: 1 + 1/5 + 1/3 + 1/7 = 1.676
Effort: 5 + 1 + 3 + 1/3 = 9.333
Risk: 3 + 1/3 + 1 + 1/5 = 4.533
Timeline: 7 + 3 + 5 + 1 = 16

Normalized matrix:
           Impact    Effort    Risk      Timeline
Impact     0.597     0.536     0.662     0.438
Effort     0.119     0.107     0.073     0.188
Risk       0.199     0.321     0.221     0.313
Timeline   0.085     0.036     0.044     0.063
```

**Step 2: Calculate Row Averages (Weights)**

```
Impact:   (0.597 + 0.536 + 0.662 + 0.438) / 4 = 0.558
Effort:   (0.119 + 0.107 + 0.073 + 0.188) / 4 = 0.122
Risk:     (0.199 + 0.321 + 0.221 + 0.313) / 4 = 0.264
Timeline: (0.085 + 0.036 + 0.044 + 0.063) / 4 = 0.057

Final Weights: [0.558, 0.122, 0.264, 0.057]
Sum should = 1.0
```

### 1.4 Consistency Check

**Purpose**: Ensure pairwise comparisons are logically consistent

**Step 1: Calculate λmax (maximum eigenvalue)**

```
Multiply comparison matrix by weight vector:
[1     5     3     7  ]   [0.558]   [2.404]
[1/5   1     1/3   3  ] × [0.122] = [0.521]
[1/3   3     1     5  ]   [0.264]   [1.125]
[1/7   1/3   1/5   1  ]   [0.057]   [0.241]

Divide each result by corresponding weight:
2.404/0.558 = 4.308
0.521/0.122 = 4.270
1.125/0.264 = 4.261
0.241/0.057 = 4.228

λmax = average = 4.267
```

**Step 2: Calculate Consistency Index (CI)**

```
CI = (λmax - n) / (n - 1)
   = (4.267 - 4) / (4 - 1)
   = 0.089
```

**Step 3: Calculate Consistency Ratio (CR)**

```
CR = CI / RI

Random Index (RI) values:
n:  1    2    3    4    5    6    7    8    9    10
RI: 0    0   0.58  0.90 1.12 1.24 1.32 1.41 1.45 1.49

For n=4: RI = 0.90
CR = 0.089 / 0.90 = 0.099 = 9.9%
```

**Decision Rule**:
- **CR < 0.10 (10%)**: Acceptable consistency ✓
- **CR ≥ 0.10**: Revise pairwise comparisons (inconsistent)

---

## Part 2: TOPSIS - Alternative Ranking

### Purpose
Rank alternatives by finding the one closest to the ideal solution and farthest from the worst solution.

### 2.1 Decision Matrix Setup

**Example: 3 Projects × 4 Criteria**

|          | Impact | Effort (cost) | Risk | Timeline (days) |
|----------|--------|---------------|------|-----------------|
| Project A| 9      | 5             | 3    | 30              |
| Project B| 7      | 3             | 5    | 45              |
| Project C| 8      | 7             | 2    | 20              |

**Criterion Types**:
- **Benefit** (higher is better): Impact
- **Cost** (lower is better): Effort, Risk, Timeline

### 2.2 Step-by-Step TOPSIS Algorithm

#### Step 1: Normalize Decision Matrix (Vector Normalization)

For each column, divide by the square root of sum of squares:

```
Impact column:
Sum of squares = 9² + 7² + 8² = 81 + 49 + 64 = 194
√194 = 13.928

Normalized values:
Project A: 9 / 13.928 = 0.646
Project B: 7 / 13.928 = 0.503
Project C: 8 / 13.928 = 0.574

Normalized matrix R:
           Impact  Effort  Risk   Timeline
Project A  0.646   0.546   0.445  0.545
Project B  0.503   0.328   0.741  0.817
Project C  0.574   0.765   0.297  0.364
```

#### Step 2: Apply Criterion Weights

Multiply each normalized value by its criterion weight from AHP:

```
Weights from AHP: [0.558, 0.122, 0.264, 0.057]

Weighted matrix V:
           Impact  Effort  Risk   Timeline
Project A  0.360   0.067   0.117  0.031
Project B  0.281   0.040   0.196  0.047
