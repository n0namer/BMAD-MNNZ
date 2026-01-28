# Comprehensive Validation Report Template

## REPORT STRUCTURE

Report to be generated with the following sections:

### Section 1: Report Header
```
═══════════════════════════════════════════════════════════════

  COMPREHENSIVE VALIDATION REPORT

  Generated: [today]
  Period: [date_range]
  Total Items Validated: {total_items} ({posts_count} posts + {ideas_count} ideas)
  Validation Dimensions: 7 (V-01 through V-07)
  Overall Health Score: {overall_health_score}% ({grade})

═══════════════════════════════════════════════════════════════
```

### Section 2: Executive Summary
```
Your content is in {health_status} overall ({overall_health_score}% / {grade}).

Performance by Dimension:
  ✅ Engagement Potential: {eng_score}% {eng_status}
  ✅ Copy Quality: {copy_score}% {copy_status}
  ✅ Quality Checklist: {quality_score}% {quality_status}
  ✅ Idea Viability: {idea_score}% {idea_status}
  ✅ Consistency: {consistency_score}% {consistency_status}
  {perf_indicator} Performance Metrics: {perf_score}% {perf_status}

Next Steps: {action_summary}
```

### Section 3: Dimensional Breakdown

Each dimension formatted as:
```
V-XX: {DIMENSION_NAME} ({items_count} items)
  Score: {score}% | Average: {average}/5 {indicator}
  Pass rate: {pass_rate}% of items meet standards
  Issues: {issue_count} items with gaps ({issue_percent}%)
  Critical: {critical_count} items failing checks ({critical_percent}%)
  Recommendation: {recommendation_text}
```

### Section 4: Critical Issues
```
Posts failing multiple validations:

🔴 Post #{number}: "{title}"
   Failures: {failure_list}
   Severity: CRITICAL
   Fix time: {est_time}
   Status: {status}
```

### Section 5: Key Findings & Trends

**STRENGTHS:**
  ✅ {strength_1}
  ✅ {strength_2}
  ...

**WEAKNESSES:**
  ❌ {weakness_1}
  ❌ {weakness_2}
  ...

**TRENDS:**
  📈 {trend_1}
  📉 {trend_2}
  ➡️  {trend_3}

### Section 6: Recommendations & Action Plan

**PHASE 1: IMMEDIATE** (Week 1 - {est_hours} hours)
  1. {action_1}
     → {details}
     → Est. {time}

**PHASE 2: SHORT-TERM** (Week 2-4 - {est_hours} hours)
  4. {action_2}
     → {details}
     → Est. {time}

**PHASE 3: ONGOING** (Month 2-3 - {est_hours} hours)
  6. {action_3}
     → {details}
     → Est. {time}

### Section 7: Monthly Monitoring Plan

Week 1: Run batch validation (V-06)
Week 2: Performance review
Week 3: Content optimization
Week 4: Planning & strategy

### Section 8: Success Metrics & Targets

Current State → Target State (90 days):
- Overall Health: {current}% → {target}%
- Quality Score: {current}% → {target}%
- Performance: {current}% → {target}%
- {metric_n}: {current}% → {target}%

### Section 9: Export Menu

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

## JSON DATA STRUCTURE

Store report data in this structure:
```json
{
  "report_id": "comprehensive-validation-[timestamp]",
  "date_generated": "[today]",
  "period": "[date_range]",
  "total_items_validated": {total_items},
  "posts_validated": {posts_count},
  "ideas_validated": {ideas_count},
  "overall_health_score": {score},
  "grade": "{grade}",
  "dimensional_scores": {
    "v01_quality": {score},
    "v02_performance": {score},
    "v03_consistency": {score},
    "v04_copy": {score},
    "v05_engagement": {score},
    "v06_batch": {score},
    "v07_ideas": {score}
  },
  "critical_posts": [{post_ids}],
  "high_priority_posts": [{post_ids}],
  "90day_plan": { ... },
  "success_metrics": { ... }
}
```

## USAGE IN STEP FILE

In step file, reference this template:
```markdown
### Generate Report Sections

Load template from: {REPORT_TEMPLATE_URL}

Then populate with actual data from validations (V-01 through V-07)
and display to user with menu options.
```
