---
description: Generate engagement prediction report with 1-5 star scores
name: step-v-05c-report
nextStepFile: ../../mode-v/mode-v-00-menu.md
type: report-generation
---

## SAVED DATA

Store engagement predictions in permanent record:
```json
{
  "report_id": "engagement-[timestamp]",
  "date_generated": "[today]",
  "summary": {
    "posts_predicted": 18,
    "average_score": 0.68,
    "average_stars": 3.4,
    "pass_rate": 89,
    "below_threshold": 2
  },
  "distribution": {
    "five_stars": 0,
    "four_stars": 8,
    "three_stars": 6,
    "two_stars": 2,
    "one_star": 0
  },
  "high_engagement": [1, 5, 8, 11, 13, 15, 17, 18],
  "low_engagement": [3, 7],
  "factor_analysis": { ... }
}
```

---

## NEXT STEP

Handle user selection: save report, edit low-engagement posts, or create template

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# VALIDATE V-05C: Engagement Prediction Report

## STEP GOAL:

Generate report predicting engagement potential with star scores and recommendations for improvement.

## EXECUTION:

### 1. Display Report Header

```
═══════════════════════════════════════════════════════════════

  🔮 ENGAGEMENT PREDICTION REPORT

  Дата отчёта: [today]
  Проверено постов: 18
  Порог: ≥3 stars = acceptable

═══════════════════════════════════════════════════════════════
```

### 2. Overall Prediction

```
ENGAGEMENT PREDICTION SUMMARY:

Average Engagement Score: 0.68 / 1.0 → ⭐⭐⭐ 3.4 stars

Pass Rate: 16/18 posts (89%) ✅ ACCEPTABLE
Concern Posts: 2 posts score <3 stars

Grade: B+ (Good engagement potential overall)
Confidence: 85% (based on engagement factor analysis)
```

### 3. Distribution by Stars

```
⭐⭐⭐⭐⭐ 5 Stars (0.85-1.0): 0 posts (0%) EXCEPTIONAL
     0 posts with exceptional engagement potential

⭐⭐⭐⭐ 4 Stars (0.70-0.84): 8 posts (44%) GOOD
     High engagement potential, ready to publish
     Examples: Posts #1, #5, #8, #11, #13, #15, #17, #18

⭐⭐⭐ 3 Stars (0.55-0.69): 6 posts (33%) MARGINAL
     Acceptable engagement potential, minor improvements recommended
     Examples: Posts #2, #4, #6, #9, #12, #14

⭐⭐ 2 Stars (0.40-0.54): 2 posts (11%) POOR
     Below threshold, needs significant improvement
     Posts #3, #7

⭐ 1 Star (<0.40): 0 posts (0%)
     No posts at critical level
```

### 4. High-Engagement Posts (4+ Stars)

```
🏆 HIGH ENGAGEMENT POTENTIAL (4+ stars):

Post #1: "5 Ways to Transform Your Productivity"
  ⭐⭐⭐⭐ (4.0 stars)
  Why it will engage:
    ✅ High specificity (5 specific ways)
    ✅ Strong emotional appeal (aspiration)
    ✅ Curiosity (list format)
    ✅ Emotional resonance (transformation promise)
  Engagement Factors:
    • Urgency: 0.7 (medium)
    • Curiosity: 0.8 (high)
    • Specificity: 0.9 (very high)
    • Emotional: 0.8 (high)
    • Social Proof: 0.7 (medium)
  Recommendation: Ready to publish as-is

Post #5: "The Hidden Cost of Procrastination"
  ⭐⭐⭐⭐ (3.9 stars)
  Why it will engage:
    ✅ Curiosity gap (hidden cost)
    ✅ Data-driven (specific costs)
    ✅ Emotional trigger (fear/regret)
  Engagement Factors:
    • Urgency: 0.8 (high - time sensitive)
    • Curiosity: 0.8 (high - "hidden")
    • Specificity: 0.8 (high - costs quantified)
    • Emotional: 0.8 (high - regret trigger)
    • Social Proof: 0.7 (medium)
  Recommendation: Ready to publish

Post #8: "Complete Guide to Building Better Habits"
  ⭐⭐⭐⭐ (3.8 stars)
  Why it will engage:
    ✅ Comprehensive value (complete guide)
    ✅ Universal appeal (habits)
    ✅ Emotional resonance (self-improvement)
  Engagement Factors:
    • Urgency: 0.6 (medium)
    • Curiosity: 0.7 (medium-high)
    • Specificity: 0.8 (high - "guide" implies completeness)
    • Emotional: 0.8 (high - personal growth)
    • Social Proof: 0.7 (medium)
  Recommendation: Ready to publish
```

### 5. Low-Engagement Posts (<3 Stars) - Needs Improvement

```
❌ LOW ENGAGEMENT POTENTIAL (<3 stars - NEEDS WORK):

Post #3: "Why Most People Fail at Fitness"
  ⭐⭐ (2.0 stars) POOR
  Problems:
    ❌ Low urgency (0.3) - no time pressure
    ❌ Low specificity (0.2) - "most people" too vague
    ❌ Low social proof (0.3) - no data or research
    ⚠️ No engagement drivers

  How to Fix (Est. 20-30 min):
    1. Add specificity:
       BEFORE: "Why Most People Fail at Fitness"
       AFTER: "87% Quit in 30 Days: The #1 Fitness Mistake"
       → Adds urgency (30 days), specificity (87%), curiosity (#1)

    2. Add social proof:
       → "Study shows 87% of people quit fitness routines"
       → "These 3 mistakes are blamed by 2.3M fitness enthusiasts"

    3. Increase emotional appeal:
       → "The mistake that costs you 3+ YEARS of wasted effort"

    4. Add urgency:
       → "Stop wasting time: avoid this before starting"

  Expected Improvement: 2.0 → 3.5+ stars ✅

Post #7: "The Secret to Better Sleep"
  ⭐⭐ (2.3 stars) POOR
  Problems:
    ❌ Low urgency (0.4) - no deadline
    ⚠️ Low specificity (0.5) - "secret" is vague
    ❌ Low social proof (0.4) - no data
    ⚠️ Moderate emotional appeal only

  How to Fix (Est. 15-20 min):
    1. Make title more specific:
       BEFORE: "The Secret to Better Sleep"
       AFTER: "Sleep 2 Hours Less, Feel 5X Better: The Proven Method"
       → Adds specificity, emotional benefit, curiosity

    2. Add research data:
       → "Study: This 10-minute routine improves sleep quality 47%"
       → "Works for 92% of insomniacs (peer-reviewed)"

    3. Add urgency:
       → "Your sleep crisis is solvable NOW"
       → "Before trying medication, try this"

    4. Strengthen CTA:
       → "Get the verified sleep optimization guide"

  Expected Improvement: 2.3 → 3.6+ stars ✅
```

### 6. Engagement Factors Deep-Dive

```
FACTOR ANALYSIS:

SPECIFICITY (Strongest Factor - Avg 0.76):
  Posts with high specificity perform well
  ✅ Use numbers: "5 ways", "47% increase", "3x faster"
  ✅ Use specific claims: "30-day cycle", "2-hour method"
  ⚠️ Avoid: "many", "some", "various", "several"

EMOTIONAL APPEAL (Strong - Avg 0.71):
  Posts triggering emotion get more shares
  ✅ Aspiration: "Transform", "Unlock", "Master"
  ✅ Fear-based: "Mistake", "Cost", "Failure"
  ✅ Relatability: "Common struggle", "Everyone does this"
  ⚠️ Avoid: Purely informational, no emotion

CURIOSITY (Strong - Avg 0.69):
  Curiosity-gap hooks drive engagement
  ✅ Strong: "Why", "Secret", "Hidden", "Surprising"
  ✅ Format: Lists ("5 ways"), "What if", "Should you"
  ⚠️ Weak: Straightforward titles, no mystery

URGENCY (Moderate - Avg 0.55):
  Time pressure increases sharing
  ✅ Strong: Explicit deadlines, limited time, "NOW"
  ⚠️ Weak: Evergreen content, "anytime", "eventually"
  Recommendation: Add urgency where appropriate

SOCIAL PROOF (Weakest - Avg 0.54):
  Data/research makes content shareable
  ✅ Strong: Studies, statistics, case studies, testimonials
  ⚠️ Weak: Personal anecdotes only, unverified claims
  Recommendation: Add data to 3 posts
```

### 7. Recommendations

```
QUICK WINS (Improve from 2-3 stars to 3+ stars):
  1. Rewrite Posts #3, #7 (biggest impact)
     → Est. 30 min total
     → Expected lift: +1 star each

  2. Add data to Posts #2, #4, #6 (marginal posts)
     → Est. 15 min per post
     → Expected lift: +0.3 stars each

SHORT-TERM (Build engagement potential):
  3. Template for future posts based on 4-star examples
     → Use Post #1, #5, #8 as models
     → Apply to all new content

  4. Create "Engagement Checklist"
     → Before publishing, verify all 5 factors
     → Target min 3 stars for all posts
```

### 8. Export & Actions

```
═══════════════════════════════════════════════════════════════

Что дальше?

[S] SAVE REPORT — Сохранить отчёт (PDF/CSV)
[E] EDIT LOW POSTS — Отредактировать посты <3 звёзд
[T] CREATE TEMPLATE — Создать шаблон с высоким взаимодействием
[M] BACK to MENU — Вернуться в меню VALIDATE

═══════════════════════════════════════════════════════════════
```

**[S] SAVE REPORT:**
Export as PDF/CSV to `/outputs/engagement-reports/`

**[E] EDIT LOW POSTS:**
Load mode-c EDIT with Posts #3, #7 pre-selected

**[T] CREATE TEMPLATE:**
Generate template based on high-engagement posts

**[M] BACK to MENU:**
Load `../mode-v-00-menu.md`

---

## SAVED DATA

Store engagement predictions in permanent record:
```json
{
  "report_id": "engagement-[timestamp]",
  "date_generated": "[today]",
  "summary": {
    "posts_predicted": 18,
    "average_score": 0.68,
    "average_stars": 3.4,
    "pass_rate": 89,
    "below_threshold": 2
  },
  "distribution": {
    "five_stars": 0,
    "four_stars": 8,
    "three_stars": 6,
    "two_stars": 2,
    "one_star": 0
  },
  "high_engagement": [1, 5, 8, 11, 13, 15, 17, 18],
  "low_engagement": [3, 7],
  "factor_analysis": { ... }
}
```

---

## NEXT STEP

Handle user selection: save report, edit low-engagement posts, or create template

