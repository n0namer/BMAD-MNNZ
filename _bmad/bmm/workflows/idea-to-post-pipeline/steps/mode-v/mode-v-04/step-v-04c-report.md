---
description: Generate copy audit report with scores and improvement suggestions
name: step-v-04c-report
nextStepFile: ../../mode-v/mode-v-00-menu.md
type: report-generation
---

## SAVED DATA

Store copy audit in permanent record:
```json
{
  "report_id": "copy-audit-[timestamp]",
  "date_generated": "[today]",
  "summary": {
    "posts_audited": 22,
    "average_score": 4.1,
    "grade": "B+"
  },
  "distribution": {
    "excellent": 8,
    "good": 10,
    "acceptable": 3,
    "poor": 1
  },
  "weak_posts": [3, 7, 12],
  "dimension_analysis": { ... }
}
```

---

## NEXT STEP

Handle user selection: save report, edit weak copy, or generate copy guidelines

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# VALIDATE V-04C: Copy Audit Report

## STEP GOAL:

Generate comprehensive copy audit report with quality scores and specific improvement suggestions.

## EXECUTION:

### 1. Display Report Header

```
═══════════════════════════════════════════════════════════════

  📊 COPY AUDIT REPORT

  Дата отчёта: [today]
  Проверено постов: 22
  Диапазон: Jan 1-28, 2024

═══════════════════════════════════════════════════════════════
```

### 2. Overall Results

```
COPY QUALITY SUMMARY:

Average Score: 4.1 / 5.0 (82% quality) ✅ GOOD

Distribution:
  Excellent (5/5): 8 posts (36%) 🏆
  Good (4/5): 10 posts (45%) ✅
  Acceptable (3/5): 3 posts (14%) ⚠️
  Poor (<3/5): 1 post (5%) ❌

Grade: B+ (Very Good)
Threshold: ≥3.5/5 = acceptable writing quality
```

### 3. Top-Scoring Posts (Examples to Follow)

```
🏆 BEST COPY (Score 5/5):

Post #1: "5 Ways to Transform Your Productivity"
  Why it works:
  ✅ Strong action verbs: "Transform", "Unlock", "Master"
  ✅ Specific numbers: "5 Ways", "3x faster", "2,340 users"
  ✅ Clear benefits: "Save 10 hours/week", "Achieve more"
  ✅ Compelling: "Game-changing", "Breakthrough approach"
  ✅ Explicit CTA: "Save this post and implement today"

Post #5: "The Hidden Cost of Procrastination"
  Why it works:
  ✅ Strong verbs: "Eliminate", "Reclaim", "Maximize"
  ✅ Data: "47% productivity loss", "$15k annual cost"
  ✅ Clear benefits: "Recover focus", "Gain 5+ hours/week"
  ✅ Compelling: "Lost potential", "Missed opportunities"
  ✅ Explicit CTA: "Start tracking today"

Post #8: "Complete Guide to Building Better Habits"
  Why it works:
  ✅ Action verbs: "Build", "Create", "Establish"
  ✅ Specific: "66-day cycle", "3 key components"
  ✅ Benefits: Clear & measurable outcomes
  ✅ Language: "Transformation", "Breakthrough"
  ✅ CTA: "Download your habit tracker"
```

### 4. Posts Needing Improvement

```
⚠️ NEEDS IMPROVEMENT (Score <4):

Post #3: "Why Most People Fail at Fitness"
  Current Score: 1/5 ❌ POOR
  Issues:
    ❌ Weak verbs: "Talk about", "Discuss"
    ❌ No specific data
    ❌ Benefits unclear
    ⚠️ Generic language
    ❌ No CTA

  How to Fix:
    1. Replace "Why Most People Fail" with action-focused headline
       → "How to Avoid the #1 Fitness Mistake (Costs Most People 3+ Years)"

    2. Add strong action verbs throughout
       → Instead: "discuss common problems"
       → Use: "eliminate these 3 critical mistakes"

    3. Add specific data
       → "87% of people quit within 30 days"
       → "Those who use this method have 3x better retention"

    4. State clear benefits
       → "You'll finally achieve sustainable results"
       → "Stop wasting time on ineffective approaches"

    5. Add explicit CTA
       → "Start with these proven methods today"
       → "Get your free fitness roadmap"

  Estimated Fix Time: 20-30 min

Post #7: "The Secret to Better Sleep"
  Current Score: 2/5 ⚠️ POOR
  Issues:
    ⚠️ Okay verbs (could be stronger)
    ⚠️ Generic references (no data)
    ⚠️ Benefits implied, not stated
    ⚠️ Forgettable language
    ⚠️ Weak CTA

  How to Fix:
    → Add research data: "Study shows X% improvement"
    → Use strong verbs: "Unlock", "Transform", "Master"
    → State specific benefits: "Fall asleep in 10 minutes"
    → Use compelling language: "Rest like never before"
    → Add explicit CTA: "Get your sleep optimization guide"

  Estimated Fix Time: 15-20 min

Post #12: "React Performance Tips"
  Current Score: 3/5 ⚠️ ACCEPTABLE
  Issues:
    ✅ Verbs okay, could be stronger
    ⚠️ Some data but could be more specific
    ⚠️ Benefits stated but could be clearer
    ✅ Language decent
    ✅ CTA present but could be stronger

  How to Fix:
    → Use stronger opening verb: "Master React Performance"
    → Add benchmarks: "5x faster rendering", "60% less code"
    → Make benefits explicit: "Build lightning-fast apps"
    → Strengthen CTA: "Implement these 7 tips today"

  Estimated Fix Time: 10-15 min
```

### 5. Dimension Analysis

```
ACTION VERBS (82% quality):

Top Performers Using:
  "Transform" (5 posts) - most effective
  "Unlock" (4 posts) - compelling
  "Master" (3 posts) - aspirational
  "Eliminate" (3 posts) - problem-focused

Avoid These Weak Verbs:
  "Learn", "Know", "See", "Get" (weak)
  "Talk about", "Discuss" (passive)

Recommendation: Replace weak verbs in 3 posts


SPECIFICITY (73% quality):

Posts Using Strong Data:
  "5 ways", "3x faster", "2,340 users", "47% increase" ✅

Posts Missing Data:
  "Many people", "Recently", "Some studies" ⚠️

Recommendation: Add numbers to 6 posts


CLEAR BENEFITS (86% quality):

Excellent Examples:
  "Save 10 hours/week"
  "Achieve sustainable results"
  "Build 2x faster"

Weak Examples:
  "Learn new things"
  "Improve your skills"
  "Be better at coding"

Recommendation: Quantify benefits in 3 posts


COMPELLING LANGUAGE (77% quality):

Effective Words:
  "Game-changing", "Breakthrough", "Transform"
  "Eliminate", "Unlock", "Reclaim"

Generic Words:
  "Good", "Nice", "Cool", "Better", "Interesting"

Recommendation: Replace generic adjectives in 5 posts


CTA CLARITY (91% quality - excellent!):

Strong CTAs:
  "Save this post and implement today"
  "Get your guide now"
  "Start tracking today"

Weak CTAs:
  "Let me know your thoughts"
  "Feel free to try"
  (none missing - this is strength!)

Recommendation: Strengthen 2 weak CTAs
```

### 6. Improvement Action Plan

```
QUICK WINS (1-2 hours):
  1. Strengthen CTAs in Posts #2, #7 (5 min each)
  2. Add data to Posts #6, #10, #15 (10 min each)
  3. Replace weak verbs in Post #3, #7, #12 (5 min each)

SHORT-TERM (2-3 hours):
  4. Rewrite poor-scoring posts (#3, #7)
     → Follow top-performer formulas
     → Est. 20-30 min per post

  5. Add compelling language to 4-5 posts
     → Replace generic adjectives
     → Est. 10 min per post

ONGOING:
  6. Create "Copy Guidelines" template
     → Based on top 5 performers
     → Reference for future posts
```

### 7. Before/After Examples

```
BEFORE (Weak Copy):

"Why Most People Fail at Fitness"
Talk about why most people don't achieve fitness goals.
Learn the common mistakes and improve your fitness.
Let me know what you think.

Score: 1/5 ❌


AFTER (Strong Copy):

"Eliminate the #1 Fitness Mistake (That Costs Most 3+ Years)"
Discover why 87% of people quit fitness routines.
This one mistake sabotages results for millions annually.
Master the proven system used by top athletes.
Get your free fitness roadmap now.

Score: 5/5 ✅

[Strong verbs + specific data + clear benefits + CTA]
```

### 8. Export & Actions

```
═══════════════════════════════════════════════════════════════

Что дальше?

[S] SAVE REPORT — Сохранить отчёт (PDF/CSV)
[E] EDIT WEAK COPY — Отредактировать слабые посты
[G] COPY GUIDELINES — Создать руководство копирайтинга
[M] BACK to MENU — Вернуться в меню VALIDATE

═══════════════════════════════════════════════════════════════
```

**[S] SAVE REPORT:**
Export as PDF/CSV to `/outputs/copy-audit-reports/`

**[E] EDIT WEAK COPY:**
Load mode-c EDIT with Posts #3, #7, #12 pre-selected

**[G] COPY GUIDELINES:**
Create template based on top 5 performers

**[M] BACK to MENU:**
Load `../mode-v-00-menu.md`

---

## SAVED DATA

Store copy audit in permanent record:
```json
{
  "report_id": "copy-audit-[timestamp]",
  "date_generated": "[today]",
  "summary": {
    "posts_audited": 22,
    "average_score": 4.1,
    "grade": "B+"
  },
  "distribution": {
    "excellent": 8,
    "good": 10,
    "acceptable": 3,
    "poor": 1
  },
  "weak_posts": [3, 7, 12],
  "dimension_analysis": { ... }
}
```

---

## NEXT STEP

Handle user selection: save report, edit weak copy, or generate copy guidelines

