# Quarterly Calibration Review Protocol

## Estimate Accuracy Analysis

Based on {N} completed ideas this quarter:

```
📊 **Estimate Accuracy Analysis**

Retrospectives completed: {count}/{total_completed} ideas

**Accuracy Distribution:**
- ⭐⭐⭐⭐⭐ Excellent (±20%): {X} ideas ({Y}%)
- ⭐⭐⭐⭐ Good (±20-50%): {A} ideas ({B}%)
- ⭐⭐ Poor (>50%): {C} ideas ({D}%)

**Average Variance:** {avg_variance}%
**Target:** 80%+ ideas within ±30% variance
```

## Load Retrospectives

```bash
npx claude-flow@v3alpha memory search \
  --namespace "retrospective" \
  --query "Q{N} 2026" \
  --limit 50
```

## Speed Multiplier Adjustments

For each domain with completed ideas:
```
Domain: {domain}
  Original Multiplier: {X}x
  Actual Performance: {Y}x
  Sample Size: {N} ideas

  Recommended Adjustment: {X}x → {Z}x
  Confidence: {High/Medium/Low}

  ❓ Apply this adjustment? [Y/N]
```

**If [Y]:**
Update data/speed-multipliers.yaml:
```yaml
adjusted_multipliers:
  {domain}: {new_multiplier}x  # Was {old}x, adjusted Q{N} based on {sample_size} ideas
```

Store in memory:
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "calibration:speed-multiplier:{domain}:Q{N}" \
  --content "{adjustment details + confidence + sample size}"
```

## Common Patterns Identified

```
🔍 **Learned Patterns Q{N}:**

Pattern 1: {pattern_name}
  Observation: {what_happened}
  Sample Size: {N} ideas
  Adjustment: {what_changed}
  Confidence: {High/Medium/Low}

  ❓ Apply this pattern to future estimates? [Y/N]
```

**If [Y]:**
Update data/mcda-methodology.yaml complexity_calibration section.

## Calibration Summary

```
📈 **System Learning Q{N}:**

Adjustments Made:
- {Domain}: Speed Multiplier {X}x → {Y}x
- {Factor}: Complexity weight {A} → {B}
- {Pattern}: New warning for {issue}

Confidence Trend: {improving/stable/declining}
Sample Size: {total_retrospectives} ideas

Next calibration: Q{N+1} Review
Target: Reduce variance from {current}% to {target}%
```

## Options

```
[A] - Apply all calibration adjustments
[R] - Review individual retrospectives
[S] - Skip calibration this quarter
```
