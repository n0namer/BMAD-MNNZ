---
description: Generate performance audit report with top/bottom performers and trends
name: step-v-02c-report
nextStepFile: ../../mode-v/mode-v-00-menu.md
type: report-generation
---

## SAVED DATA

Store performance audit in permanent record:
```json
{
  "report_id": "performance-[timestamp]",
  "date_generated": "[today]",
  "summary": {
    "posts_analyzed": 18,
    "avg_ctr": 2.4,
    "avg_engagement": 5.1,
    "grade": "B+"
  },
  "top_performers": [1, 5, 8, 12, 15],
  "underperformers": [3, 7, 2, 6, 14],
  "insights": { ... }
}
```

---

## NEXT STEP

Handle user selection: save report, edit weak posts, or return to menu

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# VALIDATE V-02C: Performance Audit Report

## STEP GOAL:

Generate comprehensive performance audit with top/bottom performers, engagement trends, and actionable insights.

## EXECUTION:

### 1. Display Report Header

```
═══════════════════════════════════════════════════════════════

  📊 PERFORMANCE AUDIT REPORT

  Дата отчёта: [today]
  Проверено постов: 18
  Диапазон: Dec 1 - Jan 28, 2024

═══════════════════════════════════════════════════════════════
```

### 2. Executive Summary

```
OVERALL PERFORMANCE:

Average CTR: 2.4% (ACCEPTABLE)
Average Engagement: 5.1% (GOOD)
Total Views: 26,208
Total Interactions: 1,335

Performance Grade: B+ (Good overall)
Trend: STABLE with minor improvement
```

### 3. Top Performers (Spotlight)

```
🏆 TOP 5 HIGHEST ENGAGEMENT:

1. Post #1: "5 Ways to Increase Productivity"
   Views: 2,340 | CTR: 3.2% | Engagement: 7.9%
   Why it works: Strong hook, clear benefits, specific tactics

2. Post #5: "The Hidden Cost of..."
   Views: 2,100 | CTR: 3.8% | Engagement: 7.1%
   Why it works: Curiosity-driven headline, strong CTA

3. Post #8: "Complete Guide to..."
   Views: 1,980 | CTR: 3.5% | Engagement: 6.8%
   Why it works: Comprehensive content, high value-add

4. Post #12: "React Performance Tips"
   Views: 1,850 | CTR: 2.9% | Engagement: 6.4%
   Why it works: Solves specific problem, technical value

5. Post #15: "Why I Changed My Mind"
   Views: 1,720 | CTR: 2.7% | Engagement: 6.1%
   Why it works: Personal angle, relatability factor
```

### 4. Bottom Performers (Needs Attention)

```
📉 BOTTOM 5 LOWEST ENGAGEMENT:

1. Post #3: "Why Most People Fail at Fitness"
   Views: 980 | CTR: 1.8% | Engagement: 4.3%
   Issues: Weak hook, poor share rate
   Recommendation: Rewrite headline, improve specificity

2. Post #7: "The Secret to Better Sleep"
   Views: 1,140 | CTR: 2.0% | Engagement: 3.9%
   Issues: Generic content, weak CTA
   Recommendation: Add data/research, strengthen CTA

3. Post #2: "Common Mistake When Learning React"
   Views: 1,890 | CTR: 2.1% | Engagement: 4.9%
   Issues: Low comment engagement, sharing
   Recommendation: Add discussion-prompting question

4. Post #6: "What Nobody Talks About"
   Views: 1,260 | CTR: 1.9% | Engagement: 4.2%
   Issues: Unclear value prop, weak opening
   Recommendation: Clarify promise in first line

5. Post #14: "3 Things You Should Know"
   Views: 1,150 | CTR: 1.7% | Engagement: 3.5%
   Issues: Too generic, no differentiation
   Recommendation: Make more specific and unique
```

### 5. Performance Metrics Breakdown

```
BY CTR:
  >3%: 7 posts (39%) ✅ EXCELLENT
  2-3%: 8 posts (44%) ⚠️ ACCEPTABLE
  <2%: 3 posts (17%) ❌ POOR

BY ENGAGEMENT RATE:
  >6%: 5 posts (28%) ✅ EXCELLENT
  4-6%: 8 posts (44%) ⚠️ ACCEPTABLE
  <4%: 5 posts (28%) ❌ POOR

BY COMMENTS:
  >10: 5 posts (28%) ✅ GOOD
  5-10: 8 posts (44%) ⚠️ ACCEPTABLE
  <5: 5 posts (28%) ❌ POOR

BY SHARE RATE:
  >1%: 2 posts (11%) ✅ EXCELLENT
  0.5-1%: 7 posts (39%) ⚠️ ACCEPTABLE
  <0.5%: 9 posts (50%) ❌ POOR
```

### 6. Key Insights & Trends

```
📈 WHAT'S WORKING:

1. List-based headlines (5-7 items)
   → Avg engagement: 7.2%

2. "Why" and "How" angles
   → Avg engagement: 6.8%

3. Personal stories + data combination
   → Avg engagement: 6.5%

4. Strong CTAs (explicit action words)
   → Avg engagement: 6.2%

📉 WHAT'S NOT WORKING:

1. Generic "should know" angles
   → Avg engagement: 3.8%

2. Weak/missing CTAs
   → Avg engagement: 4.1%

3. Non-specific benefits
   → Avg engagement: 4.3%

4. Single-dimension content (no story)
   → Avg engagement: 4.0%
```

### 7. Recommendations

```
ACTION PLAN:

IMMEDIATE (This Week):
  1. Rewrite bottom 5 posts (focus on hook + CTA)
  2. Add discussion questions to weak performers
  3. Increase share-ability (make data citable)

SHORT-TERM (This Month):
  1. Model top 5 performers for future posts
  2. A/B test headline variations for weak posts
  3. Analyze comment content (what questions arise?)

ONGOING:
  1. Track CTR weekly (benchmark: 2.5%+)
  2. Monitor engagement rate (target: 6%+)
  3. Test new angles based on top performers
```

### 8. Export & Actions

```
═══════════════════════════════════════════════════════════════

Что дальше?

[S] SAVE REPORT — Сохранить отчёт (PDF/CSV)
[E] EDIT WEAK POSTS — Отредактировать слабые посты
[C] COMPARE POSTS — Сравнить топ vs слабые посты
[M] BACK to MENU — Вернуться в меню VALIDATE

═══════════════════════════════════════════════════════════════
```

**[S] SAVE REPORT:**
Export as PDF/CSV to `/outputs/performance-reports/` with timestamp

**[E] EDIT WEAK POSTS:**
Load mode-c EDIT with bottom 5 posts pre-selected

**[C] COMPARE POSTS:**
Show side-by-side comparison of top vs bottom performers

**[M] BACK to MENU:**
Load `../mode-v-00-menu.md`

---

## SAVED DATA

Store performance audit in permanent record:
```json
{
  "report_id": "performance-[timestamp]",
  "date_generated": "[today]",
  "summary": {
    "posts_analyzed": 18,
    "avg_ctr": 2.4,
    "avg_engagement": 5.1,
    "grade": "B+"
  },
  "top_performers": [1, 5, 8, 12, 15],
  "underperformers": [3, 7, 2, 6, 14],
  "insights": { ... }
}
```

---

## NEXT STEP

Handle user selection: save report, edit weak posts, or return to menu

