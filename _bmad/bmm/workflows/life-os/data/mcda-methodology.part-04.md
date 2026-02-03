
        if base_order != new_order:
            rank_changes.append({
                'criterion': i,
                'direction': 'increase',
                'base_ranking': base_order,
                'new_ranking': new_order
            })

    return {
        'is_stable': len(rank_changes) == 0,
        'rank_changes': rank_changes
    }
```

### 4.3 JavaScript Implementation (for web interfaces)

```javascript
class MCDA {
  constructor() {
    this.RI = {1: 0, 2: 0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24,
               7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49};
  }

  ahpWeights(pairwiseMatrix) {
    const n = pairwiseMatrix.length;

    // Normalize columns
    const colSums = Array(n).fill(0);
    for (let j = 0; j < n; j++) {
      for (let i = 0; i < n; i++) {
        colSums[j] += pairwiseMatrix[i][j];
      }
    }

    const normalized = pairwiseMatrix.map((row, i) =>
      row.map((val, j) => val / colSums[j])
    );

    // Row averages = weights
    const weights = normalized.map(row =>
      row.reduce((sum, val) => sum + val, 0) / n
    );

    // Consistency check
    const weightedSum = pairwiseMatrix.map(row =>
      row.reduce((sum, val, j) => sum + val * weights[j], 0)
    );

    const lambdaValues = weightedSum.map((val, i) => val / weights[i]);
    const lambdaMax = lambdaValues.reduce((s, v) => s + v, 0) / n;

    const ci = (lambdaMax - n) / (n - 1);
    const cr = ci / this.RI[n];

    return {
      weights,
      lambdaMax,
      ci,
      cr,
      isConsistent: cr < 0.10
    };
  }

  topsisRank(decisionMatrix, weights, criteriaTypes) {
    const m = decisionMatrix.length;
    const n = decisionMatrix[0].length;

    // Normalize (vector normalization)
    const colSumSquares = Array(n).fill(0);
    for (let j = 0; j < n; j++) {
      for (let i = 0; i < m; i++) {
        colSumSquares[j] += decisionMatrix[i][j] ** 2;
      }
    }

    const normalized = decisionMatrix.map(row =>
      row.map((val, j) => val / Math.sqrt(colSumSquares[j]))
    );

    // Apply weights
    const weighted = normalized.map(row =>
      row.map((val, j) => val * weights[j])
    );

    // Ideal solutions
    const idealBest = Array(n);
    const idealWorst = Array(n);

    for (let j = 0; j < n; j++) {
      const column = weighted.map(row => row[j]);
      if (criteriaTypes[j] === 'benefit') {
        idealBest[j] = Math.max(...column);
        idealWorst[j] = Math.min(...column);
      } else {
        idealBest[j] = Math.min(...column);
        idealWorst[j] = Math.max(...column);
      }
    }

    // Distances
    const dBest = weighted.map(row => {
      const diff = row.map((val, j) => (val - idealBest[j]) ** 2);
      return Math.sqrt(diff.reduce((s, v) => s + v, 0));
    });

    const dWorst = weighted.map(row => {
      const diff = row.map((val, j) => (val - idealWorst[j]) ** 2);
      return Math.sqrt(diff.reduce((s, v) => s + v, 0));
    });

    // Relative closeness
    const ci = dWorst.map((dw, i) => dw / (dBest[i] + dw));

    // Rankings
    const rankings = ci.map((score, i) => ({index: i, score}))
                       .sort((a, b) => b.score - a.score);

    return {
      ciScores: ci,
      rankings,
      idealBest,
      idealWorst
    };
  }
}
```

---

## Part 5: Practical Tips & Best Practices

### 5.1 Common AHP Pitfalls

1. **Over-granular comparisons**:
   - ❌ Using all 9 scale levels (1, 2, 3, ..., 9)
   - ✅ Stick to odd numbers (1, 3, 5, 7, 9)

2. **Ignoring consistency**:
   - ❌ Accepting CR > 0.10 to avoid rework
   - ✅ Revise contradictory comparisons systematically

3. **Criterion redundancy**:
   - ❌ Including highly correlated criteria (inflates weight)
   - ✅ Combine or choose the most representative

4. **Single-person bias**:
   - ❌ One person's judgments for team decision
   - ✅ Aggregate multiple stakeholder matrices (geometric mean)

### 5.2 TOPSIS Optimization

1. **Criterion type errors**:
   - ❌ Treating "time to complete" as benefit
   - ✅ Verify benefit vs cost before running algorithm

2. **Scale differences**:
   - ❌ Mixing 1-10 scale with 1-100 scale (bias)
   - ✅ Use normalized scores (vector method handles this)

3. **Missing alternatives**:
   - ❌ Comparing only 2 alternatives (trivial)
   - ✅ Need 3+ alternatives for meaningful ranking

4. **Rank reversals**:
   - ❌ Adding irrelevant alternative changes top 2 order
   - ✅ Run sensitivity analysis to detect instability

### 5.3 Integration Workflow Summary

```
Workflow: Project Prioritization with MCDA
───────────────────────────────────────────

1. Define Decision Context
   ├─ Identify sphere (D/F/V/C)
   ├─ List candidate projects (alternatives)
   └─ Define evaluation criteria (4-6 recommended)

2. Run AHP for Criterion Weights
