---
description: Generate comprehensive batch validation report with all validation results
name: step-v-06c-report
nextStepFile: ./v-00-menu.md
type: report-generation
---

## SAVED DATA

Store batch validation report in permanent record:
```json
{
  "report_id": "batch-validation-[timestamp]",
  "date_generated": "[today]",
  "total_items": 203,
  "composite_score": 78,
  "grade": "B+",
  "validation_results": {
    "v01_quality": { score: 81, pass_rate: 82 },
    "v02_performance": { score: 60, underperformers: 33 },
    "v03_consistency": { score: 78, poor_consistency: 13 },
    "v04_copy": { score: 82, poor_copy: 6 },
    "v05_engagement": { score: 87, below_threshold: 10 }
  },
  "critical_posts": [3, 7, 24],
  "high_priority_posts": [8, 12, 15, 18, 19, 22, 23, 28, 31, 35],
  "action_items": [ ... ]
}
```

---

## NEXT STEP

Handle user selection: save report, edit critical posts, or show detailed analysis

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# VALIDATE V-06C: Batch Validation Summary Report

## STEP GOAL:

Generate comprehensive report summarizing all validation results, problem areas, and recommendations.

## EXECUTION:

### 1. Display Report Header

```
═══════════════════════════════════════════════════════════════

  📊 COMPREHENSIVE BATCH VALIDATION REPORT

  Дата отчёта: [today]
  Проверено: 203 элемента (156 постов + 47 идей)
  Время: 5 минут 23 секунды

═══════════════════════════════════════════════════════════════
```

### 2. Executive Summary

```
CONTENT HEALTH SCORE: B+ (78%)

Validation Results Across All Criteria:

✅ Quality: 81% (High quality content)
✅ Copy: 82% (Strong copywriting)
✅ Engagement: 87% (Excellent engagement potential)
✅ Consistency: 78% (Good cross-post alignment)
⚠️  Performance: 60% (Some underperformers in analytics)

Overall Recommendation: CONTENT QUALITY IS GOOD
                        Focus improvements on performance metrics

Posts Requiring Action: 35 posts (22%)
Critical Issues: 8 posts (5%)
```

### 3. Detailed Validation Results

```
V-01: QUALITY CHECKLIST
  Total: 156 posts
  Passed (5/5): 128 (82%) ✅
  Passed with warnings (4/5): 20 (13%) ⚠️
  Failed (<4/5): 8 (5%) ❌
  Average: 4.77/5 (Excellent)

V-02: PERFORMANCE AUDIT
  Total: 124 published posts
  Top performers (>6%): 35 (28%) ✅
  Acceptable (4-6%): 56 (45%) ✅
  Underperformers (<4%): 33 (27%) ⚠️
  Avg CTR: 2.4% | Avg engagement: 5.1%

V-03: CONSISTENCY CHECK
  Total: 156 posts
  Excellent (85%+): 95 (61%) ✅
  Acceptable (70-84%): 48 (31%) ✅
  Poor (<70%): 13 (8%) ⚠️
  Overall consistency: 78%

V-04: COPY AUDIT
  Total: 156 posts
  Excellent (5/5): 58 (37%) ✅
  Good (4/5): 72 (46%) ✅
  Acceptable (3/5): 20 (13%) ⚠️
  Poor (<3/5): 6 (4%) ❌
  Average: 4.2/5 (Good)

V-05: ENGAGEMENT CHECK
  Total: 156 posts
  4+ stars (High): 94 (60%) ✅
  3 stars (Marginal): 52 (33%) ⚠️
  <3 stars (Poor): 10 (7%) ❌
  Average: 3.5 stars
```

### 4. Problem Areas Summary

```
TOP 5 ISSUE CATEGORIES:

1. UNDERPERFORMING POSTS (Performance <4% engagement)
   Posts affected: 33
   Impact: Low CTR and engagement metrics
   Root cause: Often weak copy or inconsistent messaging
   Fix: Rewrite copy, improve specificity

2. ENGAGEMENT POTENTIAL BELOW THRESHOLD (<3 stars)
   Posts affected: 10
   Impact: Lower predicted social sharing
   Root cause: Weak curiosity hooks, low urgency
   Fix: Strengthen hook and add data/social proof

3. INCONSISTENCY ACROSS POSTS (<70% consistency)
   Posts affected: 13
   Impact: Confusing brand voice
   Root cause: Tone shifts, audience confusion
   Fix: Standardize voice and target audience

4. WEAK COPY (<3/5 copy score)
   Posts affected: 6
   Impact: Poor copywriting quality
   Root cause: Weak action verbs, vague benefits
   Fix: Strengthen language and clarify benefits

5. QUALITY ISSUES (Quality <4/5)
   Posts affected: 28
   Impact: Various quality gaps
   Root cause: Weak hooks, unclear CTAs, tone issues
   Fix: Refer to quality checklist recommendations
```

### 5. Critical Posts Requiring Immediate Action

```
🔴 CRITICAL (Fix This Week):

Post #3: "Why Most People Fail at Fitness"
  Issues: Quality 3/5 | Copy 1/5 | Engagement 2 stars
  Action: Rewrite post completely
  Est. time: 30 min

Post #7: "The Secret to Better Sleep"
  Issues: Quality 2/5 | Copy 2/5 | Engagement 2.3 stars
  Action: Rewrite post completely
  Est. time: 30 min

Post #24: "This is Important"
  Issues: Quality 2/5 | Engagement 1.8 stars
  Action: Rewrite post completely
  Est. time: 30 min

CRITICAL ACTION ITEMS: 3 posts | Est. 1.5 hours total

🟡 HIGH PRIORITY (Fix This Month):

Posts with multiple issues: 5 posts
  • Copy score <3: Posts #8, #12, #18, #22, #28
  • Performance issue + consistency: Posts #15, #19, #23
  • Engagement + quality: Posts #31, #35

HIGH PRIORITY: 12 posts | Est. 2-3 hours total
```

### 6. Strengths to Maintain

```
✅ WHAT'S WORKING WELL:

Excellent Quality (82% pass rate)
  → Keep using clear structure: Hook → Problem → Solution
  → Maintain 4+ criteria in all future posts

Strong Copy Writing (82% pass rate)
  → Continue using strong action verbs
  → Keep using specific numbers and data
  → Maintain explicit CTAs

Excellent Engagement Potential (87% pass rate)
  → Strong specificity in content
  → Good emotional appeal
  → Curiosity elements working well

Consistency in Style (78% overall)
  → Writing style very consistent
  → Maintain this going forward
  → Just need minor tone adjustments
```

### 7. Recommendations & Action Plan

```
IMMEDIATE (THIS WEEK - 2-3 hours):
  1. Fix 3 critical posts (complete rewrite)
  2. Improve weak CTAs (3 posts, 5 min each)
  3. Add missing data (5 posts, 10 min each)

SHORT-TERM (THIS MONTH - 8-10 hours):
  4. Fix 12 high-priority posts
  5. Improve performance metrics (optimize for social sharing)
  6. Strengthen consistency in recent posts

ONGOING:
  7. Use batch validation monthly (track progress)
  8. Create quality checklist for all new posts
  9. Model future content on top performers (#1, #5, #8)
  10. Track metrics: target B+ grade (78%+) every month
```

### 8. Export & Actions

```
═══════════════════════════════════════════════════════════════

Что дальше?

[S] SAVE REPORT — Сохранить полный отчёт (PDF)
[E] EDIT CRITICAL — Отредактировать критичные посты
[D] DETAILED — Показать детальный анализ каждого критерия
[M] BACK to MENU — Вернуться в меню VALIDATE

═══════════════════════════════════════════════════════════════
```

**[S] SAVE REPORT:**
Export comprehensive report to `/outputs/batch-reports/batch-[timestamp].pdf`

**[E] EDIT CRITICAL:**
Load mode-c EDIT with Posts #3, #7, #24 pre-selected

**[D] DETAILED:**
Display detailed breakdowns for each validation type

**[M] BACK to MENU:**
Load `./v-00-menu.md`

---

## SAVED DATA

Store batch validation report in permanent record:
```json
{
  "report_id": "batch-validation-[timestamp]",
  "date_generated": "[today]",
  "total_items": 203,
  "composite_score": 78,
  "grade": "B+",
  "validation_results": {
    "v01_quality": { score: 81, pass_rate: 82 },
    "v02_performance": { score: 60, underperformers: 33 },
    "v03_consistency": { score: 78, poor_consistency: 13 },
    "v04_copy": { score: 82, poor_copy: 6 },
    "v05_engagement": { score: 87, below_threshold: 10 }
  },
  "critical_posts": [3, 7, 24],
  "high_priority_posts": [8, 12, 15, 18, 19, 22, 23, 28, 31, 35],
  "action_items": [ ... ]
}
```

---

## NEXT STEP

Handle user selection: save report, edit critical posts, or show detailed analysis

