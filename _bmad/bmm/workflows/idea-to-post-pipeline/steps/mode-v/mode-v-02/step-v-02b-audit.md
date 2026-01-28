---
description: Analyze CTR, engagement rate, comments, shares for performance audit
name: step-v-02b-audit
nextStepFile: ./step-v-02c-report.md
type: automated-analysis
---

# VALIDATE V-02B: Performance Audit Analysis

## STEP GOAL:

Analyze performance metrics: CTR (click-through rate), engagement rate, comment trends, share patterns.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Analysis Start

```
═══════════════════════════════════════════════════════════════

  🔍 ANALYZING PERFORMANCE METRICS

  Анализирую 18 постов по метрикам производительности...

═══════════════════════════════════════════════════════════════
```

### 2. Calculate Performance Metrics

For each post, calculate:

#### METRIC 1: Click-Through Rate (CTR)
- Formula: (clicks / views) × 100
- Good: >3%, Acceptable: 2-3%, Poor: <2%

#### METRIC 2: Engagement Rate
- Formula: (likes + comments + shares) / views × 100
- Good: >5%, Acceptable: 3-5%, Poor: <3%

#### METRIC 3: Average Comments per Post
- Track comment count trend
- Good: >10, Acceptable: 5-10, Poor: <5

#### METRIC 4: Share/Retweet Rate
- Formula: shares / views × 100
- Good: >1%, Acceptable: 0.5-1%, Poor: <0.5%

### 3. Analyze Results

```
Analyzing metrics...

Post #1: "5 Ways to Increase Productivity"
├─ Views: 2,340
├─ CTR: 3.2% (GOOD) ✅
├─ Engagement: 184 (7.9%) [EXCELLENT] ✅
├─ Comments: 12 (GOOD) ✅
└─ Share rate: 0.34% (ACCEPTABLE) ⚠️
STATUS: TOP PERFORMER 🏆

Post #2: "Common Mistake When Learning React"
├─ Views: 1,890
├─ CTR: 2.1% (ACCEPTABLE) ⚠️
├─ Engagement: 92 (4.9%) [ACCEPTABLE] ⚠️
├─ Comments: 5 (POOR) ❌
└─ Share rate: 0.11% (POOR) ❌
STATUS: UNDERPERFORMER 📉

Post #3: "Why Most People Fail at Fitness"
├─ Views: 980
├─ CTR: 1.8% (POOR) ❌
├─ Engagement: 42 (4.3%) [ACCEPTABLE] ⚠️
├─ Comments: 3 (POOR) ❌
└─ Share rate: 0.10% (POOR) ❌
STATUS: NEEDS IMPROVEMENT ⚠️

...Processing 15 more posts...
```

### 4. Auto-Analysis Summary

```
Performance Analysis Complete:

SUMMARY STATISTICS:
├─ Average CTR: 2.4% (ACCEPTABLE range)
├─ Average Engagement: 5.1% (GOOD range)
├─ Avg comments per post: 7.2 (ACCEPTABLE)
├─ Avg share rate: 0.42% (POOR)
└─ Top 3 performers: Posts #1, #5, #8

DISTRIBUTION:
  Top performers (>6% engagement): 5 posts
  Acceptable (4-6% engagement): 8 posts
  Underperformers (<4% engagement): 5 posts

TRENDS:
  📈 CTR improving (trend analysis shows growth)
  📉 Share rate declining (needs investigation)
  ✅ Comments stable
```

### 5. Progress

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Performance Analysis: 100% Complete (18/18 posts)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## SAVED DATA

Store performance analysis results:
```json
{
  "validation_type": "performance_audit",
  "posts_analyzed": 18,
  "analysis_date": "[today]",
  "summary": {
    "avg_ctr": 2.4,
    "avg_engagement": 5.1,
    "avg_comments": 7.2,
    "avg_share_rate": 0.42
  },
  "top_performers": [1, 5, 8],
  "underperformers": [2, 3, 7],
  "results": [...]
}
```

---

## NEXT STEP

Generate detailed performance audit report with top/bottom performers and trends

