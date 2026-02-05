# Retrospective Calibration Methods

## Accuracy Metrics

### Accuracy Ratio
```
Actual Duration / Planned Duration

- 0.8-1.2: Excellent (±20% variance) ⭐⭐⭐⭐⭐
- 0.6-0.8 or 1.2-1.5: Good (±20-50% variance) ⭐⭐⭐⭐
- <0.6 or >1.5: Poor (>50% variance) ⭐⭐
```

### Speed Multiplier Validation
```
Actual Speed / Assumed Speed

- 1.0: Multiplier accurate ✅
- <1.0: Overestimated speed (slower than expected) ⚠️
- >1.0: Underestimated speed (faster than expected) 🚀
```

### Complexity Delta
```
Actual Complexity - Planned Complexity

- ±2 points: Accurate ✅
- ±3-5 points: Significant variance ⚠️
- >±5 points: Major mismatch ❌
```

---

## Memory Storage Patterns

### Store Retrospective Data
```bash
npx claude-flow@v3alpha memory store \
  --namespace "retrospective" \
  --key "idea-{id}:{date}" \
  --content "{full retrospective JSON}"
```

### Store Calibration Updates
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "calibration:speed-multiplier:{domain}" \
  --content "{adjusted multiplier + reason + confidence}"
```

### Store Learned Patterns
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "patterns:retrospective:{pattern-name}" \
  --content "{pattern description + confidence + sample size}"
```

---

## Calibration File Updates

### Update data/speed-multipliers.yaml
Add new `calibration_history` entry with:
- date
- domain
- assumed_multiplier
- actual_multiplier
- adjustment
- reason
- sample_size

**Update adjusted_multipliers section:**
Recalculate running average for this domain.

### Update data/mcda-methodology.yaml
If complexity scoring needs adjustment, add to `complexity_calibration` section.

---

## Confidence Levels

| Sample Size | Confidence | Recommendation |
|-------------|------------|----------------|
| 1-2 ideas | Low | Use with caution |
| 3-5 ideas | Medium | Reliable for domain |
| 6+ ideas | High | Strongly reliable |
