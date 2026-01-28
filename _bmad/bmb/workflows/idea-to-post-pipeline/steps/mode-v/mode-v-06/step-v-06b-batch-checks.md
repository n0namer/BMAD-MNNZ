---
description: Run all quality checks (V-01 through V-05) on all posts in parallel
name: step-v-06b-batch-checks
nextStepFile: ./step-v-06c-report.md
type: parallel-validation
---

# VALIDATE V-06B: Batch Quality Checks (All Validations in Parallel)

## STEP GOAL:

Run all 5 validation types (quality, performance, consistency, copy, engagement) on all 203 content items in parallel.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Batch Start

```
═══════════════════════════════════════════════════════════════

  🔄 RUNNING BATCH VALIDATIONS (Parallel Processing)

  Запускаю все проверки на 203 элементах контента...

═══════════════════════════════════════════════════════════════
```

### 2. Run Validations in Parallel

```
BATCH VALIDATION PROGRESS:

Starting parallel validation streams...

┌─ V-01: QUALITY CHECKLIST (156 posts)
│  Processing... ████████████░░░░░░░░░░ 50% Complete
│  ETA: 2 minutes

├─ V-02: PERFORMANCE AUDIT (124 published posts only)
│  Processing... ██████████████░░░░░░░░░░░ 60% Complete
│  ETA: 2 minutes

├─ V-03: CONSISTENCY CHECK (156 posts)
│  Processing... ████████░░░░░░░░░░░░░░░░░░ 30% Complete
│  ETA: 3 minutes

├─ V-04: COPY AUDIT (156 posts)
│  Processing... ██████████████████░░░░░░░░ 70% Complete
│  ETA: 1.5 minutes

└─ V-05: ENGAGEMENT CHECK (156 posts + 47 ideas)
   Processing... ████████████░░░░░░░░░░░░░░░ 50% Complete
   ETA: 2 minutes

Overall Progress: 52% (107/203 items)
Time elapsed: 3 minutes
Estimated completion: 5 minutes total

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 3. Batch Results Summary (After Completion)

```
BATCH VALIDATION COMPLETE ✅

All validations finished in 5 minutes 23 seconds.

════════════════════════════════════════════════════════════════

V-01: QUALITY CHECKLIST RESULTS (156 posts)
  ✅ Passed (5/5): 128 posts (82%)
  ⚠️  Passed with warnings (4/5): 20 posts (13%)
  ❌ Failed (<4/5): 8 posts (5%)
  Average score: 4.77/5

V-02: PERFORMANCE AUDIT RESULTS (124 published posts)
  ✅ Top performers (>6% engagement): 35 posts (28%)
  ✅ Acceptable (4-6% engagement): 56 posts (45%)
  ❌ Underperformers (<4% engagement): 33 posts (27%)
  Average CTR: 2.4%
  Average engagement: 5.1%

V-03: CONSISTENCY CHECK RESULTS (156 posts)
  ✅ Excellent consistency (85%+): 95 posts (61%)
  ⚠️  Acceptable consistency (70-84%): 48 posts (31%)
  ❌ Poor consistency (<70%): 13 posts (8%)
  Overall consistency score: 78%

V-04: COPY AUDIT RESULTS (156 posts)
  ✅ Excellent (5/5): 58 posts (37%)
  ✅ Good (4/5): 72 posts (46%)
  ⚠️  Acceptable (3/5): 20 posts (13%)
  ❌ Poor (<3/5): 6 posts (4%)
  Average copy score: 4.2/5

V-05: ENGAGEMENT CHECK RESULTS (156 posts)
  ✅ 4+ stars (high engagement): 94 posts (60%)
  ⚠️  3 stars (marginal): 52 posts (33%)
  ❌ <3 stars (poor engagement): 10 posts (7%)
  Average engagement score: 3.5 stars

════════════════════════════════════════════════════════════════

OVERALL CONTENT HEALTH:

Quality Score: 81% ✅ GOOD
Performance Score: 60% (published posts) ⚠️ ACCEPTABLE
Consistency Score: 78% ✅ GOOD
Copy Score: 82% ✅ GOOD
Engagement Score: 87% ✅ EXCELLENT

COMPOSITE SCORE: 78% (B+ Overall)
```

### 4. Top Issues Across All Content

```
TOP 10 POSTS NEEDING ATTENTION:

1. Post #3: "Why Most People Fail at Fitness"
   Issues: Quality 3/5 | Copy 1/5 | Engagement 2 stars
   Severity: CRITICAL

2. Post #7: "The Secret to Better Sleep"
   Issues: Quality 2/5 | Copy 2/5 | Engagement 2.3 stars
   Severity: CRITICAL

3. Post #14: "3 Things You Should Know"
   Issues: Copy 2/5 | Engagement 3 stars
   Severity: HIGH

4-10: [8 more posts with specific issues flagged]
```

### 5. Ideas Validation Results

```
IDEA VALIDATION (47 ideas):

For Ideas Inbox (V-07: VALIDATE IDEAS):
  ✅ Valid ideas: 38 (81%)
  ⚠️  Needs clarification: 6 (13%)
  ❌ Not viable: 3 (6%)

Summary: 81% of ideas are ready for research/writing
```

### 6. Progress Display

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Batch Validation: 100% Complete (203/203 items)
Total issues detected: 47
Posts requiring action: 35 posts
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## SAVED DATA

Store comprehensive batch validation results:
```json
{
  "validation_type": "batch_validation",
  "items_validated": 203,
  "posts_validated": 156,
  "ideas_validated": 47,
  "completion_time_seconds": 323,
  "v01_results": { ... },
  "v02_results": { ... },
  "v03_results": { ... },
  "v04_results": { ... },
  "v05_results": { ... },
  "flagged_items": [3, 7, 14, ...],
  "composite_score": 78
}
```

---

## NEXT STEP

Generate comprehensive batch validation report

