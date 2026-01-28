---
description: Display high-level performance dashboard with top posts and trends
name: step-c-07a-dashboard
nextStepFile: ./step-c-07b-deepdive.md
type: analytics-dashboard
---

## DATA SOURCES

Metrics loaded from:
- `metrics_tracking.csv` (views, clicks, CTR, engagement)
- `posts_content.csv` (post details, angles)
- Last 30 days of data

---

## NEXT STEP

Handle user selection

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# CREATE C-07: Analytics - Dashboard

## STEP GOAL:

Display overall performance dashboard with key metrics and top performers.

## EXECUTION:

### 1. Display Dashboard Header

```
═════════════════════════════════════════════════════════════════

  📊 ANALYTICS DASHBOARD

  Период: Last 30 days

═════════════════════════════════════════════════════════════════
```

### 2. Show Key Metrics

```
KEY METRICS (30 дней)
─────────────────────────────────────────────────

  📈 Total Views:        15,847
  👆 Total Clicks:       642
  📊 Average CTR:        4.1% (EXCELLENT)
  💬 Total Comments:     124
  🔄 Total Shares:       89
  ⭐ Avg Engagement:     3.8/5 stars

  📝 Posts Created:      12
  ✅ Posts Published:    10
  ⏳ Drafts:             2

═════════════════════════════════════════════════════════════════
```

### 3. Show Top Performers

```
TOP POSTS (by CTR)
─────────────────────────────────────────────────

🥇 POST #8: "Вот чего ты не знаешь про ИИ"
   Views: 523 | Clicks: 25 | CTR: 4.8% ⭐⭐⭐⭐⭐
   Angle: Curiosity | Engagement: 4.9/5
   Date: 2026-02-01 | Status: Published

🥈 POST #1: "3 часа вместо недели"
   Views: 412 | Clicks: 19 | CTR: 4.6% ⭐⭐⭐⭐⭐
   Angle: Time Saving | Engagement: 4.8/5
   Date: 2026-01-28 | Status: Published

🥉 POST #3: "5 успешных фаундеров уже используют..."
   Views: 312 | Clicks: 13 | CTR: 4.2% ⭐⭐⭐⭐
   Angle: Social Proof | Engagement: 4.5/5
   Date: 2026-01-29 | Status: Published

─ LOW PERFORMERS (CTR < 3%) ─────────────────────

❌ POST #6: "ИИ контент и качество"
   Views: 189 | Clicks: 7 | CTR: 3.7% ⚠️
   Angle: Quality | Engagement: 3.2/5
   Recommendation: Needs rewrite (weak hook)

❌ POST #4: "Масштабирование"
   Views: 156 | Clicks: 4 | CTR: 2.6% ❌ POOR
   Angle: Growth | Engagement: 2.1/5
   Recommendation: Urgent: rewrite hook + CTA

═════════════════════════════════════════════════════════════════
```

### 4. Trend Analysis

```
TRENDS (30-day analysis)
─────────────────────────────────────────────────

📈 CTR Trend:
   Week 1:  2.8% (learning curve)
   Week 2:  3.5% (+25% improvement)
   Week 3:  4.0% (+14% improvement)
   Week 4:  4.1% (steady)

👌 Pattern: Learning effect! Older posts getting better.

📈 Engagement Trend:
   Week 1:  3.0/5 (average)
   Week 2:  3.5/5 (+17%)
   Week 3:  4.0/5 (+14%)
   Week 4:  3.8/5 (stable)

🔥 Best Angles (by CTR):
   1. Curiosity (4.6% avg)
   2. Time Saving (4.4% avg)
   3. Social Proof (4.1% avg)

💤 Weakest Angles (by CTR):
   1. Growth (3.1% avg)
   2. Quality (3.3% avg)

═════════════════════════════════════════════════════════════════
```

### 5. Present Options

```
Что смотреть дальше?

[D] DEEP DIVE — Детальный анализ конкретного поста
[R] RECOMMENDATIONS — Рекомендации что улучшить
[E] EXPORT — Экспортировать данные в CSV
[M] Back to MENU

═════════════════════════════════════════════════════════════════
```

**[D] DEEP DIVE:**
Load, read entire file, then execute `./step-c-07b-deepdive.md`

**[R] RECOMMENDATIONS:**
Load, read entire file, then execute `./step-c-07c-recommendations.md`

**[E] EXPORT:**
Export metrics_tracking.csv to user

**[M] Back to MENU:**
Load `../mode-c-00-menu.md`

---

## DATA SOURCES

Metrics loaded from:
- `metrics_tracking.csv` (views, clicks, CTR, engagement)
- `posts_content.csv` (post details, angles)
- Last 30 days of data

---

## NEXT STEP

Handle user selection
