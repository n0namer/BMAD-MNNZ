---
description: Load posts with engagement metrics for performance audit
name: step-v-02a-load
nextStepFile: ./step-v-02b-audit.md
type: data-loading
---

# VALIDATE V-02A: Load Posts with Performance Metrics

## STEP GOAL:

Load published posts with engagement metrics (CTR, likes, comments, shares) for performance audit.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Loading Status

```
═══════════════════════════════════════════════════════════════

  📊 VALIDATE V-02: PERFORMANCE AUDIT

  Loading posts with engagement metrics...

═══════════════════════════════════════════════════════════════
```

### 2. Load Posts from Analytics Database

Query `posts_analytics.csv` with metrics:
- Status: `published` (only published posts have metrics)
- Metrics: views, clicks, likes, comments, shares, retweets
- Date range: last 60 days (or user-specified)

Example output:
```
Loaded 18 published posts (last 60 days):

Post #1: "5 Ways to..."
├─ Views: 2,340 | CTR: 3.2% | Engagement: 184
├─ Likes: 45 | Comments: 12 | Shares: 8

Post #2: "Common Mistake..."
├─ Views: 1,890 | CTR: 2.1% | Engagement: 92
├─ Likes: 28 | Comments: 5 | Shares: 2

...

Post #18: "Why Most People..."
├─ Views: 980 | CTR: 1.8% | Engagement: 42
├─ Likes: 15 | Comments: 3 | Shares: 1
```

### 3. Display Metric Summary

```
METRICS LOADED:
  Total posts: 18
  Date range: Dec 1 - Jan 28, 2024
  Avg views per post: 1,456
  Avg engagement rate: 5.2%

Ready for performance audit.
```

### 4. Confirmation

```
Proceed with performance audit?

[Y] YES — Начать аудит производительности
[M] MODIFY — Изменить диапазон постов
[?] BACK — Вернуться в меню

═══════════════════════════════════════════════════════════════
```

**[Y] YES:**
Load, read entire file, then execute `./step-v-02b-audit.md`

**[M] MODIFY:**
Return to step 2 (let user select date range, platforms, etc.)

**[?] BACK:**
Load `../mode-v-00-menu.md`


### Menu Handling Logic

**IF [Y]: YES:**
Load, read entire file, then execute `./step-v-02b-audit.md`

**IF [M]: MODIFY:**
Return to step 2 (let user select date range, platforms, etc.)

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.
---

## SAVED DATA

Store loaded posts with metrics in validation session:
```json
{
  "validation_session_id": "v-02-[timestamp]",
  "loaded_posts": 18,
  "date_range": "2023-12-01 to 2024-01-28",
  "posts": [
    {
      "id": 1,
      "title": "5 Ways to...",
      "views": 2340,
      "clicks": 75,
      "likes": 45,
      "comments": 12,
      "shares": 8,
      "ctr": 3.2,
      "engagement_rate": 5.2
    },
    ...
  ]
}
```

---

## NEXT STEP

Analyze CTR, engagement rate, and performance metrics

