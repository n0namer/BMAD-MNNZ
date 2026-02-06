---
description: Run quality checks on posts (hook, problem, solution, CTA, tone)
name: step-v-01b-checks
nextStepFile: ./v-01c-report.md
type: automated-validation
---

# VALIDATE V-01B: Quality Checklist Validation

## STEP GOAL:

Run automated quality checks on loaded posts: hook strength, problem clarity, solution relevance, CTA clarity, tone consistency.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Check Start

```
═══════════════════════════════════════════════════════════════

  🔍 RUNNING QUALITY CHECKS

  Проверяю 24 поста по критериям качества...

═══════════════════════════════════════════════════════════════
```

### 2. Run Quality Checks

For each post, validate against criteria:

#### CHECK 1: Hook Strength
- ✅ Strong: Opening line captures attention immediately
- ❌ Weak: Generic or unclear opening

#### CHECK 2: Problem Clarity
- ✅ Clear: Specific problem articulated in first 2 lines
- ❌ Vague: Problem not clearly stated

#### CHECK 3: Solution Relevance
- ✅ Relevant: Solution directly addresses stated problem
- ❌ Irrelevant: Solution seems disconnected

#### CHECK 4: CTA Clarity
- ✅ Explicit: Clear call-to-action (save, share, comment, click)
- ❌ Weak: No CTA or vague

#### CHECK 5: Tone Consistency
- ✅ Consistent: Tone matches throughout (not switching)
- ❌ Inconsistent: Tone changes abruptly

### 3. Generate Check Results

```
Validating posts...

Post #1: "5 Ways to Increase Productivity"
├─ Hook strength: ✅ Strong
├─ Problem clarity: ✅ Clear
├─ Solution relevance: ✅ Relevant
├─ CTA clarity: ✅ Explicit (Save this post)
└─ Tone consistency: ✅ Consistent
STATUS: ✅ PASS (5/5 checks)

Post #2: "Common Mistake When Learning React"
├─ Hook strength: ✅ Strong
├─ Problem clarity: ✅ Clear
├─ Solution relevance: ✅ Relevant
├─ CTA clarity: ❌ Weak (implied)
└─ Tone consistency: ✅ Consistent
STATUS: ⚠️  PASS (4/5 checks) — Improve CTA clarity

Post #3: "Why Most People Fail at Fitness"
├─ Hook strength: ❌ Weak (generic opening)
├─ Problem clarity: ✅ Clear
├─ Solution relevance: ✅ Relevant
├─ CTA clarity: ✅ Explicit (Start with this method)
└─ Tone consistency: ❌ Inconsistent (shifts midway)
STATUS: ❌ FAIL (3/5 checks) — Fix hook and tone

...Processing 21 more posts...
```

### 4. Auto-Analysis

```
Quality Check Summary:
├─ Total posts validated: 24
├─ Passed (5/5): 18 posts (75%)
├─ Passed with warnings (4/5): 4 posts (17%)
├─ Failed (<4/5): 2 posts (8%)
└─ Average score: 4.75/5

Common issues detected:
  1. CTA clarity (3 posts need improvement)
  2. Tone consistency (2 posts)
  3. Hook strength (1 post)

Ready to generate detailed report.
```

### 5. Progress Indicator

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Quality Checks: 100% Complete (24/24 posts)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## SAVED DATA

Store validation results in session:
```json
{
  "validation_type": "quality_checklist",
  "posts_validated": 24,
  "passed_full": 18,
  "passed_partial": 4,
  "failed": 2,
  "average_score": 4.75,
  "results": [
    {"post_id": 1, "hook": true, "problem": true, "solution": true, "cta": true, "tone": true, "status": "pass"},
    ...
  ]
}
```

---

## NEXT STEP

Generate detailed quality report with issues and recommendations

