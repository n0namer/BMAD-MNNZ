---
description: Deep dive into specific post performance and detailed metrics over time
name: step-c-07b-deepdive
nextStepFile: ./c-07c-recommendations.md
type: detailed-analysis
---

# CREATE C-07: Analytics - Deep Dive

## STEP GOAL:

Provide detailed performance analysis of a single post over time.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Load Posts & Request Selection

```
═════════════════════════════════════════════════════════════════

  🔎 DEEP DIVE ANALYSIS

═════════════════════════════════════════════════════════════════

Какой пост проанализировать?

[1] Post #1: "3 часа вместо недели" (CTR: 4.6%)
[2] Post #3: "5 успешных фаундеров..." (CTR: 4.2%)
[3] Post #8: "Вот чего ты не знаешь..." (CTR: 4.8%)
[4] Post #4: "Масштабирование" (CTR: 2.6%) ⚠️
[5] Post #6: "ИИ контент и качество" (CTR: 3.7%)

[?] SEARCH — Поиск поста по названию

═════════════════════════════════════════════════════════════════
```

### 2. Display Detailed Analysis

Once user selects post:

```
DETAILED ANALYSIS: Post #1
─────────────────────────────────────────────────

📝 Post Info:
   Title: "3 часа вместо недели: как ИИ подтягивает контент"
   Angle: Time Saving
   Category: automation
   Created: 2026-01-27
   Published: 2026-01-28
   Status: Published

📊 Overall Performance (since publish):
   Total Views:       412
   Total Clicks:      19
   Overall CTR:       4.6% ⭐⭐⭐⭐⭐
   Avg Engagement:    4.8/5 stars
   Saves:             7
   Shares:            5
   Comments:          3

📈 DAILY BREAKDOWN:
─────────────────────────────────────────────────

Date    | Views | Clicks | CTR   | Comments | Shares
──────────────────────────────────────────────────
Jan 28  | 245   | 11     | 4.5%  | 2        | 1
Jan 29  | 412   | 19     | 4.6%  | 5        | 3
Jan 30  | 680   | 31     | 4.6%  | 12       | 7
Jan 31  | 945   | 43     | 4.5%  | 18       | 11

🔥 Trend: STRONG GROWTH (growing every day)

📉 Performance Score Over Time:
   Day 1: 89/100 (initial quality)
   Day 2: 91/100 (grows with engagement)
   Day 3: 93/100 (viral potential detected)
   Day 4: 92/100 (sustaining)

💡 Key Insights:
   ✅ Strong hook working (attracting clicks)
   ✅ Problem resonates with audience
   ✅ High engagement = quality confirmed
   ✅ Share rate high = valuable content

⚠️  Minor issues:
   • CTR stable at 4.5-4.6% (good but not +5%)
   • 3 comments is decent but could be higher
   • Could benefit from stronger CTA

═════════════════════════════════════════════════════════════════
```

### 3. Present Next Actions

```
На что обратить внимание?

[C] COMPARE — Сравнить с другим постом
[R] REWRITE LOW-CTR — Переписать слабые версии
[E] EDIT — Отредактировать этот пост
[I] INSIGHTS — Извлечь insights для новых постов
[M] Back to MENU

═════════════════════════════════════════════════════════════════
```

**[C] COMPARE:**
Select another post and compare side-by-side

**[R] REWRITE LOW-CTR:**
If CTR < 3%, offer to rewrite hook/CTA

**[E] EDIT:**
Load EDIT MODE for this post

**[I] INSIGHTS:**
Extract key lessons (what worked)

**[M] Back to MENU:**
Load `./c-00-menu.md`

---

## DATA SOURCE

Data loaded from metrics_tracking.csv (daily snapshots)

---

## NEXT STEP

Handle user selection

### Menu Handling Logic

**IF [C]: COMPARE:**
Select another post and compare side-by-side

**IF [R]: REWRITE LOW-CTR:**
If CTR < 3%, offer to rewrite hook/CTA

**IF [E]: EDIT:**
Load EDIT MODE for this post

**IF [I]: INSIGHTS:**
Extract key lessons (what worked)

**IF [M]: Back to MENU:**
Load `./c-00-menu.md`

---

## DATA SOURCE

Data loaded from metrics_tracking.csv (daily snapshots)

---

## NEXT STEP

Handle user selection

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.
