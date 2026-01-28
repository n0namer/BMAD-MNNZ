---
description: Generate quality checklist report with pass/fail breakdown
name: step-v-01c-report
nextStepFile: ../../mode-v/mode-v-00-menu.md
type: report-generation
---

## SAVED DATA

Store report in permanent record:
```json
{
  "report_id": "quality-report-[timestamp]",
  "date_generated": "[today]",
  "posts_validated": 24,
  "summary": {
    "passed_full": 18,
    "passed_partial": 4,
    "failed": 2,
    "pass_rate": "95%",
    "average_score": 4.75
  },
  "breakdowns": { ... },
  "recommendations": [ ... ],
  "grade": "A"
}
```

Export options:
- `/outputs/quality-reports/quality-[timestamp].pdf`
- `/outputs/quality-reports/quality-[timestamp].csv`

---

## NEXT STEP

Handle user selection: save report, edit flagged posts, or return to menu

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# VALIDATE V-01C: Quality Checklist Report

## STEP GOAL:

Generate comprehensive quality report with pass rates, failed items, and recommendations.

## EXECUTION:

### 1. Display Report Header

```
═══════════════════════════════════════════════════════════════

  📊 QUALITY CHECKLIST REPORT

  Дата отчёта: [today]
  Проверено постов: 24
  Диапазон: Jan 2-15, 2024

═══════════════════════════════════════════════════════════════
```

### 2. Summary Statistics

```
OVERALL RESULTS:
  ✅ Passed (all 5 checks): 18 posts (75%)
  ⚠️  Passed with warnings (4/5): 4 posts (17%)
  ❌ Failed (<4/5): 2 posts (8%)

Average Score: 4.75 / 5.00 (95% quality)
Threshold: ≥4/5 checks passed = acceptable
```

### 3. Detailed Breakdown by Criterion

```
HOOK STRENGTH:
  ✅ Strong: 22 posts (92%)
  ❌ Weak: 2 posts (8%)

PROBLEM CLARITY:
  ✅ Clear: 23 posts (96%)
  ❌ Vague: 1 post (4%)

SOLUTION RELEVANCE:
  ✅ Relevant: 24 posts (100%)
  ❌ Irrelevant: 0 posts (0%)

CTA CLARITY:
  ✅ Explicit: 21 posts (88%)
  ❌ Weak/Missing: 3 posts (12%)

TONE CONSISTENCY:
  ✅ Consistent: 22 posts (92%)
  ❌ Inconsistent: 2 posts (8%)
```

### 4. Posts Needing Attention

```
POSTS WITH ISSUES:

❌ Post #3: "Why Most People Fail at Fitness"
   Issues: Hook weakness (generic opening) + Tone inconsistency (shifts midway)
   Recommendation: Strengthen hook, unify tone throughout
   Severity: HIGH

❌ Post #7: "The Secret to Better Sleep"
   Issues: Weak CTA (only implied)
   Recommendation: Add explicit call-to-action
   Severity: MEDIUM

⚠️  Post #12: "React Performance Tips"
   Issues: CTA clarity could be stronger
   Recommendation: Make CTA more prominent
   Severity: LOW

⚠️  Post #18: "Building Better Habits"
   Issues: Tone inconsistency (formal → casual mix)
   Recommendation: Choose and maintain single tone throughout
   Severity: MEDIUM
```

### 5. Recommendations

```
TOP RECOMMENDATIONS:

1. Improve CTA Clarity (3 posts)
   → Add explicit, action-oriented call-to-action to weak CTAs
   → Est. effort: 5-10 min per post

2. Strengthen Hooks (2 posts)
   → Rewrite opening lines to be more compelling
   → Est. effort: 10-15 min per post

3. Unify Tone (2 posts)
   → Choose dominant tone and apply throughout
   → Est. effort: 10-15 min per post
```

### 6. Quality Grade

```
QUALITY GRADE: A (90-95% pass rate)

This is excellent work. 95% of posts meet quality standards.
Focus improvements on 5 posts with specific issues.
```

### 7. Export & Actions

```
═══════════════════════════════════════════════════════════════

Что дальше?

[S] SAVE REPORT — Сохранить отчёт (PDF/CSV)
[E] EDIT POSTS — Отредактировать посты с проблемами
[V] VIEW DETAILS — Показать детали по каждому посту
[M] BACK to MENU — Вернуться в меню VALIDATE

═══════════════════════════════════════════════════════════════
```

**[S] SAVE REPORT:**
Export report as PDF/CSV to `/outputs/quality-reports/` with timestamp

**[E] EDIT POSTS:**
Load, read entire file, then execute `../../mode-c/mode-c-05/step-c-05a-select-post.md` (EDIT mode) with flagged posts pre-selected

**[V] VIEW DETAILS:**
Display detailed breakdown by post with exact issues

**[M] BACK to MENU:**
Load `../mode-v-00-menu.md`

---

## SAVED DATA

Store report in permanent record:
```json
{
  "report_id": "quality-report-[timestamp]",
  "date_generated": "[today]",
  "posts_validated": 24,
  "summary": {
    "passed_full": 18,
    "passed_partial": 4,
    "failed": 2,
    "pass_rate": "95%",
    "average_score": 4.75
  },
  "breakdowns": { ... },
  "recommendations": [ ... ],
  "grade": "A"
}
```

Export options:
- `/outputs/quality-reports/quality-[timestamp].pdf`
- `/outputs/quality-reports/quality-[timestamp].csv`

---

## NEXT STEP

Handle user selection: save report, edit flagged posts, or return to menu

