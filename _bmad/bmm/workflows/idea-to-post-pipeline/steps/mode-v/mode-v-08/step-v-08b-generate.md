---
description: Generate comprehensive validation report with all data, trends, and action plan
name: step-v-08b-generate
nextStepFile: ../../mode-v/mode-v-00-menu.md
type: report-generation
---

## SAVED DATA

Store comprehensive report:
```json
{
  "report_id": "comprehensive-validation-[timestamp]",
  "date_generated": "[today]",
  "period": "[date_range]",
  "total_items_validated": 203,
  "posts_validated": 156,
  "ideas_validated": 47,
  "overall_health_score": 81,
  "grade": "B+",
  "dimensional_scores": {
    "v01_quality": 81,
    "v02_performance": 60,
    "v03_consistency": 78,
    "v04_copy": 82,
    "v05_engagement": 87,
    "v06_batch": 78,
    "v07_ideas": 81
  },
  "critical_posts": [3, 7, 24],
  "high_priority_posts": [8, 12, 15, 18, 19, 22, 23, 28, 31, 35],
  "90day_plan": { ... },
  "success_metrics": { ... }
}
```

---

## NEXT STEP

Handle user selection: save report, print, view action plan, or return to menu

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# VALIDATE V-08B: Generate Comprehensive Validation Report

## STEP GOAL:

Generate complete validation report with all validation dimensions, trends, issues, recommendations, and 90-day action plan.

## EXECUTION:

### 1. Display Report Generation

```
═══════════════════════════════════════════════════════════════

  📊 GENERATING COMPREHENSIVE VALIDATION REPORT

  Creating complete quality dashboard with all validations...

═══════════════════════════════════════════════════════════════
```

### 2. Generate Report Sections

```
REPORT GENERATION IN PROGRESS:

Step 1/5: Executive Summary
  └─ Overall health score: 81% (B+)
  └─ Pass rate across all dimensions: 82%
  └─ Items requiring action: 35 posts, 6 ideas
  └─ Time to completion: ████████░░░░░░░░░░░░░░ 40%

Step 2/5: Dimensional Analysis
  ├─ Quality Checklist (V-01): 81% ✅
  ├─ Performance Audit (V-02): 60% ⚠️
  ├─ Consistency Check (V-03): 78% ✅
  ├─ Copy Audit (V-04): 82% ✅
  ├─ Engagement Check (V-05): 87% ✅
  ├─ Batch Results (V-06): 78% ✅
  └─ Idea Viability (V-07): 81% ✅
  └─ Time to completion: ████████████░░░░░░░░░░░░ 60%

Step 3/5: Issue Analysis
  ├─ Critical issues (8 posts): 5% of content
  ├─ High priority (12 posts): 8% of content
  ├─ Medium priority (15 posts): 10% of content
  └─ Low priority/monitoring (35 posts): 22% of content
  └─ Time to completion: ██████████████░░░░░░░░░░░░ 75%

Step 4/5: Trends & Patterns
  ├─ Engagement potential: STRONG (87%)
  ├─ Copy quality: GOOD (82%)
  ├─ Cross-post consistency: NEEDS WORK (78%)
  ├─ Performance metrics: VARIABLE (60%)
  └─ Overall trend: IMPROVING
  └─ Time to completion: ██████████████████░░░░░░░░ 90%

Step 5/5: Recommendations & Action Plan
  ├─ Immediate actions: 3-5 hours
  ├─ 30-day sprint: 8-10 hours
  ├─ 90-day plan: 20-25 hours
  └─ Ongoing optimization: Monthly reviews
  └─ Time to completion: █████████████████████░░░░░░ 100%

GENERATION COMPLETE ✅
Report ready for display.
```

### 3. Full Report Display

Load comprehensive report template from: `../../data/report-templates/comprehensive-validation-report-template.md`

Populate template sections with actual validation data from V-01 through V-07:
- Executive summary with dimensional scores
- Dimensional breakdown for each validation
- Critical issues with fix times
- Key findings and trends
- 90-day action plan phases
- Monthly monitoring plan
- Success metrics and targets

Display report with menu options:
```
═══════════════════════════════════════════════════════════════

Что дальше?

[S] SAVE REPORT — Сохранить полный отчёт (PDF/word)
[P] PRINT REPORT — Распечатать отчёт
[A] ACTION PLAN — Показать 90-day план действий
[D] DETAILS — Показать детальные данные по каждому посту
[M] BACK to MENU — Вернуться в меню VALIDATE

═══════════════════════════════════════════════════════════════
```

**[S] SAVE REPORT:**
Export comprehensive report to `/outputs/comprehensive-reports/comprehensive-validation-[timestamp].pdf`

**[P] PRINT REPORT:**
Format for printing and display

**[A] ACTION PLAN:**
Display detailed 90-day action plan with specific tasks

**[D] DETAILS:**
Show detailed metrics for each post and idea

**[M] BACK to MENU:**
Load `../mode-v-00-menu.md`

---

## SAVED DATA

Store comprehensive report:
```json
{
  "report_id": "comprehensive-validation-[timestamp]",
  "date_generated": "[today]",
  "period": "[date_range]",
  "total_items_validated": 203,
  "posts_validated": 156,
  "ideas_validated": 47,
  "overall_health_score": 81,
  "grade": "B+",
  "dimensional_scores": {
    "v01_quality": 81,
    "v02_performance": 60,
    "v03_consistency": 78,
    "v04_copy": 82,
    "v05_engagement": 87,
    "v06_batch": 78,
    "v07_ideas": 81
  },
  "critical_posts": [3, 7, 24],
  "high_priority_posts": [8, 12, 15, 18, 19, 22, 23, 28, 31, 35],
  "90day_plan": { ... },
  "success_metrics": { ... }
}
```

---

## NEXT STEP

Handle user selection: save report, print, view action plan, or return to menu

