
2. **Alternative Scores Change** (TOPSIS):
   - New project proposals added
   - Existing project status updates
   - Risk/effort estimates revised
   - **Frequency**: Monthly or on project updates

3. **Consistency Violations**:
   - CR > 0.10 detected
   - Pairwise comparisons become contradictory
   - **Action**: Immediate recalibration

4. **Sensitivity Alerts**:
   - Rankings change dramatically with small weight shifts
   - Multiple alternatives have near-identical Ci scores
   - **Action**: Add discriminating criteria or split decisions

---

## Part 4: Pseudocode Implementation

### 4.1 AHP Weight Calculation

```python
def ahp_calculate_weights(pairwise_matrix):
    """
    Calculate criterion weights from pairwise comparison matrix

    Args:
        pairwise_matrix: n×n array of pairwise comparisons

    Returns:
        weights: Array of normalized weights (sum = 1)
        cr: Consistency Ratio
        is_consistent: Boolean (CR < 0.10)
    """
    n = len(pairwise_matrix)

    # Step 1: Normalize columns
    col_sums = pairwise_matrix.sum(axis=0)
    normalized = pairwise_matrix / col_sums

    # Step 2: Calculate row averages (weights)
    weights = normalized.mean(axis=1)

    # Step 3: Consistency check
    weighted_sum = pairwise_matrix @ weights
    lambda_values = weighted_sum / weights
    lambda_max = lambda_values.mean()

    ci = (lambda_max - n) / (n - 1)
    ri = {1: 0, 2: 0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24,
          7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
    cr = ci / ri[n] if n in ri and ri[n] > 0 else 0

    return {
        'weights': weights,
        'lambda_max': lambda_max,
        'ci': ci,
        'cr': cr,
        'is_consistent': cr < 0.10
    }


def ahp_pairwise_matrix(criteria, comparisons):
    """
    Build pairwise comparison matrix from comparison dict

    Args:
        criteria: List of criterion names
        comparisons: Dict {(crit_i, crit_j): value}

    Returns:
        matrix: n×n pairwise comparison matrix
    """
    n = len(criteria)
    matrix = np.ones((n, n))

    for i in range(n):
        for j in range(i+1, n):
            key = (criteria[i], criteria[j])
            if key in comparisons:
                value = comparisons[key]
                matrix[i, j] = value
                matrix[j, i] = 1 / value
            else:
                # Default to equal importance if not specified
                matrix[i, j] = 1
                matrix[j, i] = 1

    return matrix
```

### 4.2 TOPSIS Ranking

```python
def topsis_rank(decision_matrix, weights, criteria_types):
    """
    Rank alternatives using TOPSIS

    Args:
        decision_matrix: m×n array (alternatives × criteria)
        weights: Array of criterion weights from AHP
        criteria_types: Array of 'benefit' or 'cost' for each criterion

    Returns:
        rankings: Array of (alternative_index, Ci_score)
    """
    # Step 1: Normalize (vector normalization)
    col_squares = (decision_matrix ** 2).sum(axis=0)
    normalized = decision_matrix / np.sqrt(col_squares)

    # Step 2: Apply weights
    weighted = normalized * weights

    # Step 3: Identify ideal solutions
    ideal_best = np.zeros(len(weights))
    ideal_worst = np.zeros(len(weights))

    for j in range(len(weights)):
        if criteria_types[j] == 'benefit':
            ideal_best[j] = weighted[:, j].max()
            ideal_worst[j] = weighted[:, j].min()
        else:  # cost
            ideal_best[j] = weighted[:, j].min()
            ideal_worst[j] = weighted[:, j].max()

    # Step 4: Calculate distances
    m = len(decision_matrix)
    d_best = np.zeros(m)
    d_worst = np.zeros(m)

    for i in range(m):
        d_best[i] = np.sqrt(((weighted[i] - ideal_best) ** 2).sum())
        d_worst[i] = np.sqrt(((weighted[i] - ideal_worst) ** 2).sum())

    # Step 5: Calculate relative closeness
    ci = d_worst / (d_best + d_worst)

    # Step 6: Rank (descending by Ci)
    rankings = sorted(enumerate(ci), key=lambda x: x[1], reverse=True)

    return {
        'ci_scores': ci,
        'rankings': rankings,
        'ideal_best': ideal_best,
        'ideal_worst': ideal_worst
    }


def topsis_sensitivity_analysis(decision_matrix, base_weights,
                                  criteria_types, perturbation=0.1):
    """
    Test ranking stability under weight variations

    Args:
        decision_matrix: m×n array (alternatives × criteria)
        base_weights: Original AHP weights
        criteria_types: Array of 'benefit' or 'cost'
        perturbation: Weight variation (default ±10%)

    Returns:
        stability_report: Dict with rank changes under perturbations
    """
    base_ranking = topsis_rank(decision_matrix, base_weights, criteria_types)
    rank_changes = []

    # Perturb each weight individually
    for i in range(len(base_weights)):
        # Increase weight i
        perturbed_weights = base_weights.copy()
        delta = perturbation * base_weights[i]
        perturbed_weights[i] += delta
        perturbed_weights /= perturbed_weights.sum()  # Re-normalize

        new_ranking = topsis_rank(decision_matrix, perturbed_weights, criteria_types)

        # Compare rankings
        base_order = [x[0] for x in base_ranking['rankings']]
        new_order = [x[0] for x in new_ranking['rankings']]
