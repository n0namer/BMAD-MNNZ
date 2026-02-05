# Retrospective Protocol

## Purpose
Learn from completed ideas to calibrate future estimates and improve recommendations.

## When to Run
- ✅ After idea reaches COMPLETED status (via step-x tracking)
- ✅ After idea reaches KILLED status (via step-x-04)
- ✅ Quarterly review of all completed ideas
- ✅ Manual: `/retrospective {idea-id}`

## Data Collection

### Planned Data (from Deep Plan)
- Estimated duration (weeks/months)
- Estimated complexity (1-10 score)
- Speed Multiplier applied (e.g., 10x)
- Resource assumptions (solo/team, LLM/manual)
- Key assumptions documented

### Actual Data (from Execution Tracking)
- Actual duration (start date → completion date)
- Actual complexity encountered (1-10 score)
- Actual resources used
- Blockers encountered (count, severity)
- Pivot decisions made (if any)

### Calculated Metrics

```
Accuracy Ratio = Actual Duration / Planned Duration

- 0.8-1.2: Excellent (±20% variance)
- 0.6-0.8 or 1.2-1.5: Good (±20-50% variance)
- <0.6 or >1.5: Poor (>50% variance)

Speed Multiplier Validation = Actual Speed / Assumed Speed

- If 1.0: Multiplier accurate
- If <1.0: Overestimated speed (slower than expected)
- If >1.0: Underestimated speed (faster than expected)
```

## Retrospective Questions

### 1. Timeline Accuracy
**Q:** Was the timeline estimate accurate?
- ✅ Yes, within ±20% (excellent)
- ⚠️ Somewhat, ±20-50% variance (good)
- ❌ No, >50% variance (poor)

**If poor, why?**
- [ ] Underestimated complexity
- [ ] Overestimated resources (Speed Multiplier too high)
- [ ] Unexpected blockers
- [ ] Scope creep
- [ ] Other: ___

### 2. Complexity Assessment
**Q:** Was the complexity score accurate?
[Original: {X}/10 → Actual: {Y}/10]

**If different, what changed?**
- Technical challenges
- Integration complexity
- Domain expertise gaps
- Dependency issues

### 3. Speed Multiplier Validation
**Q:** Was the Speed Multiplier realistic?
[Assumed: {X}x → Actual: {Y}x]

**If lower than expected:**
- LLM less effective than assumed (specific areas?)
- More manual work required (what tasks?)
- Learning curve steeper (which technologies?)

**If higher than expected:**
- LLM more effective (which tasks automated well?)
- Better tools discovered (which ones?)
- Existing knowledge leveraged (what areas?)

### 4. What Went Well
- Technical decisions that worked
- Tools/approaches that accelerated progress
- Assumptions that proved correct
- Unexpected wins

### 5. What Could Improve
- Overestimated areas (where we were too optimistic)
- Underestimated areas (where we missed complexity)
- Blockers that could have been foreseen
- Better approaches discovered mid-project

### 6. Recommendations for Future Similar Ideas
- Adjust Speed Multiplier: {X}x → {Y}x for {domain}
- Adjust complexity scoring: Add {factor} consideration
- Common pitfalls: Watch out for {issue}
- Suggested approach: Use {tool/pattern} from start

## Calibration Learning

### Update Speed Multiplier Database

```yaml
# data/speed-multipliers.yaml

calibration_history:
  - date: 2026-02-05
    domain: saas_web_app
    assumed_multiplier: 10x
    actual_multiplier: 8x
    adjustment: -20%
    reason: "Frontend complexity underestimated, UI polish took longer"
    sample_size: 3 ideas

  - date: 2026-02-06
    domain: api_backend
    assumed_multiplier: 15x
    actual_multiplier: 18x
    adjustment: +20%
    reason: "LLM excellent at API boilerplate, faster than expected"
    sample_size: 2 ideas

# Use running average for future estimates
adjusted_multipliers:
  saas_web_app: 9x  # Was 10x, adjusted based on 3 completed ideas
  api_backend: 16x  # Was 15x, adjusted based on 2 completed ideas
```

### Update Complexity Scoring Weights

```yaml
# data/mcda-methodology.yaml

complexity_calibration:
  - factor: technical_complexity
    original_weight: 0.25
    adjusted_weight: 0.30
    reason: "Consistently underestimated, increase importance"
    confidence: high (10 ideas)

  - factor: integration_points
    original_weight: 0.15
    adjusted_weight: 0.20
    reason: "Integration always more complex than assumed"
    confidence: medium (5 ideas)
```

### Common Patterns Learned

```markdown
## Learned Patterns (Updated {date})

### Pattern 1: Frontend Polish Always Takes Longer
- **Observation:** 8/10 web apps took 30-50% longer on UI polish
- **Adjustment:** Add 1.4x multiplier to frontend complexity scores
- **Confidence:** High (10 ideas)

### Pattern 2: LLM Excellent for API/Backend
- **Observation:** Backend APIs 20% faster than estimated
- **Adjustment:** Increase Speed Multiplier for API work: 15x → 18x
- **Confidence:** High (8 ideas)

### Pattern 3: First-Time Tech Has Learning Curve
- **Observation:** New technologies add 50-100% to estimates
- **Adjustment:** Flag novelty in complexity scoring, add learning time
- **Confidence:** Medium (4 ideas)
```

## Retrospective Report Template

```markdown
# Retrospective: {Idea Name}

**Date:** {Completion date}
**Status:** {COMPLETED / KILLED}
**Duration:** {Actual} (Planned: {Planned})
**Accuracy:** {Excellent / Good / Poor} (±{X}%)

## Timeline Comparison

| Metric | Planned | Actual | Variance |
|--------|---------|--------|----------|
| Duration | {X} weeks | {Y} weeks | {±Z%} |
| Complexity | {A}/10 | {B}/10 | {±C} |
| Speed Multiplier | {M}x | {N}x | {±P%} |

## What Went Well
1. {Success 1}
2. {Success 2}
3. {Success 3}

## What Could Improve
1. {Issue 1} - Impact: {High/Medium/Low}
2. {Issue 2} - Impact: {High/Medium/Low}
3. {Issue 3} - Impact: {High/Medium/Low}

## Key Learnings
- {Learning 1}
- {Learning 2}
- {Learning 3}

## Calibration Adjustments
- Speed Multiplier: {Before}x → {After}x ({domain})
- Complexity Factor: Increase weight on {factor}
- Common Pitfall: Watch for {issue} in similar projects

## Recommendations
For future similar ideas:
1. {Recommendation 1}
2. {Recommendation 2}
3. {Recommendation 3}

**Confidence in Estimates:** {High / Medium / Low}
**Sample Size:** {N} similar ideas completed

---
**Stored in memory:** `retrospective:{idea-id}:{date}`
```

## Integration Points

### With Step X-02 (Weekly Pulse)
- Track actual progress vs planned milestones
- Document blockers and delays
- Feed into retrospective

### With Step X-04 (Pivot-or-Kill)
- Document why killed or pivoted
- What assumptions were wrong
- Learn for future filtering

### With Step 09 (Complete)
- Trigger retrospective prompt
- Compare Deep Plan (step-08) vs Execution Tracking (step-x-01 → completion)

### With Quarterly Review (step-v-04)
- Aggregate retrospectives for all completed ideas
- Identify systemic patterns
- Update calibration multipliers

## Memory Storage

**Per-Idea Retrospective:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "retrospective" \
  --key "idea-{id}:{date}" \
  --content "{
    idea_id: '001',
    idea_name: 'Katana',
    planned_duration: '2 weeks',
    actual_duration: '2.5 weeks',
    accuracy: 'good',
    variance: '+25%',
    learnings: [...],
    adjustments: [...]
  }"
```

**Calibration Updates:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "calibration:speed-multiplier:saas-web" \
  --content "{
    original: 10x,
    adjusted: 9x,
    reason: 'Frontend polish underestimated',
    confidence: 'high',
    sample_size: 3
  }"
```

## Success Metrics

**System Improvement Over Time:**
- Estimate accuracy trend (are we getting better?)
- Calibration confidence (more data = higher confidence)
- Repeated mistake detection (same issues appearing?)

**Target:**
- 80%+ ideas within ±30% variance
- Speed Multiplier accuracy ±20%
- Complexity score accuracy ±2 points

---

**Last Updated:** 2026-02-05
**Ideas Retrospected:** 0
**Average Accuracy:** N/A (insufficient data)
**Confidence Level:** Low (baseline)
