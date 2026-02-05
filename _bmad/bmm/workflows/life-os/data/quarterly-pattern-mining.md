# Quarterly Pattern Mining Protocol

## Pattern Discovery Process

**Load archived ideas from this quarter:**
```bash
# Search archived completed ideas
npx claude-flow@v3alpha memory search -q "archive completed Q{N}"

# Search archived killed ideas
npx claude-flow@v3alpha memory search -q "archive killed Q{N}"
```

```
🔍 **Archive Pattern Mining - Q{N}**

Archived this quarter:
- ✅ Completed: {count} ideas
- ❌ Killed: {count} ideas

Analyzing for patterns...
```

## A. Success Pattern Detection

For completed ideas, analyze:
1. Common technologies/approaches that worked well
2. Domains with better-than-expected speed
3. Complexity factors that were accurate vs underestimated
4. Frontend/backend split patterns

```
💡 **Success Pattern Candidate Detected**

Pattern: {pattern_name}
Source: {N} completed ideas ({idea_ids})
Observation: {what_pattern_observed}

Evidence:
- Idea {ID}: {specific_evidence}
- Idea {ID}: {specific_evidence}

Confidence: {HIGH/MEDIUM/LOW} based on {N} data points

Recommendation: {actionable_recommendation}

❓ Save this as pattern? [Y]es / [N]o / [Tell me more]
```

**If [Y]:** Update `output/archive/patterns/success-patterns.md`

## B. Failure Pattern Detection

For killed ideas, analyze:
1. Common kill reasons (market validation, complexity, ROI)
2. Warning signs that appeared early
3. Domain-specific challenges
4. Estimate accuracy for killed ideas

```
⚠️ **Failure Pattern Candidate Detected**

Pattern: {pattern_name}
Source: {N} killed ideas ({idea_ids})
Observation: {what_led_to_kill}

Evidence:
- Idea {ID}: Killed because {reason}
- Idea {ID}: Killed because {reason}

Confidence: {HIGH/MEDIUM/LOW} based on {N} data points

Prevention: {how_to_avoid}
Warning triggers: {early_warning_signs}

❓ Save this as warning pattern? [Y]es / [N]o / [Tell me more]
```

**If [Y]:** Update `output/archive/patterns/failure-patterns.md`

## C. Domain Insights Update

```
📊 **Domain Performance Analysis - Q{N}**

Finance Domain:
  Completed: {X} ideas
  Avg Speed: {Y}x (vs planned {Z}x)
  Avg Complexity: {A}/10 (vs estimated {B}/10)
  Success Rate: {C}%

  Recommendation: {adjustment}
  Confidence: {level}

  ❓ Apply domain calibration? [Y/N]
```

**If [Y]:** Update `output/archive/patterns/domain-insights.md`

## D. Pattern Application to Future Ideas

Store patterns in memory for auto-detection:
```bash
# Save success pattern
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "patterns:success:p{NNN}-{name}" \
  --content "{pattern definition + evidence + recommendation}"

# Save failure pattern
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "patterns:failure:f{NNN}-{name}" \
  --content "{pattern definition + warning triggers + prevention}"
```

## Pattern Summary

```
✅ Patterns Discovered Q{N}:

Success Patterns: {count}
  - {pattern_1_name}: {brief_description}
  - {pattern_2_name}: {brief_description}

Failure Patterns: {count}
  - {pattern_1_name}: {brief_description}
  - {pattern_2_name}: {brief_description}

Domain Calibrations: {count}
  - {domain}: Speed Multiplier {old}x → {new}x
  - {domain}: Complexity Factor +{adjustment}

All patterns saved to:
- output/archive/patterns/success-patterns.md
- output/archive/patterns/failure-patterns.md
- output/archive/patterns/domain-insights.md
- Global memory (shared-knowledge namespace)

Next quarter, these patterns will auto-suggest during:
- Step 02: Scoring (complexity adjustments)
- Step 03: Planning (timeline adjustments)
- Step 08: Deep Plan (architecture recommendations)
```
