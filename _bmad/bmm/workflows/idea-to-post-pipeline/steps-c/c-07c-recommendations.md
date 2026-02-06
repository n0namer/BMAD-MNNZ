---
description: Generate AI recommendations based on analytics data
name: step-c-07c-recommendations
nextStepFile: ./c-00-menu.md
type: actionable-insights
---

## NEXT STEP

Handle user selection

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# CREATE C-07: Analytics - Recommendations

## STEP GOAL:

Analyze all data and provide actionable recommendations for content improvement.

## EXECUTION:

### 1. Display Recommendations Header

```
═════════════════════════════════════════════════════════════════

  💡 ACTIONABLE RECOMMENDATIONS

═════════════════════════════════════════════════════════════════

Based on 30 days of data and 12 posts published.
```

### 2. Generate Recommendations

```
RECOMMENDATION 1: Focus on TOP ANGLES
────────────────────────────────────────────────

Your best performing angles:
  🥇 Curiosity gap: 4.6% avg CTR
  🥈 Time saving: 4.4% avg CTR
  🥉 Social proof: 4.1% avg CTR

❌ Weakest angles:
  • Growth/Scalability: 3.1% avg CTR
  • Quality discussion: 3.3% avg CTR

ACTION:
  👉 Next 3 posts: Use curiosity + time saving angles ONLY
  👉 Archive or rewrite low-performing angles
  👉 Expected result: +10-15% CTR improvement

─────────────────────────────────────────────────

RECOMMENDATION 2: Improve WEAK POSTS (CTR < 3%)
────────────────────────────────────────────────

Posts that underperformed:
  ❌ Post #4 "Масштабирование" (2.6% CTR)
  ❌ Post #6 "ИИ контент и качество" (3.7% CTR)

Issues identified:
  • Hook not strong enough (no urgency)
  • Problem description too vague
  • CTA not explicit

ACTION:
  👉 Rewrite hook for both posts (add urgency/specificity)
  👉 Add numbers/facts to problem statement
  👉 Make CTA action-oriented ("try now" vs "think about")
  👉 Re-publish and track
  👉 Expected improvement: 3-4% CTR (+30% boost)

─────────────────────────────────────────────────

RECOMMENDATION 3: Leverage VIRAL POSTS
────────────────────────────────────────────────

Your top performer:
  🚀 Post #8 "Вот чего ты не знаешь..." (4.8% CTR)

What made it work:
  ✅ Strong curiosity hook (mystery hook)
  ✅ Clear problem (knowledge gap)
  ✅ Specific solution
  ✅ Social proof (implicit: "everyone should know")

ACTION:
  👉 Analyze this post thoroughly (deep dive)
  👉 Replicate the pattern for 3 new posts
  👉 Use curiosity gap + specific facts formula
  👉 Expected result: Maintain 4.5%+ CTR

─────────────────────────────────────────────────

RECOMMENDATION 4: Optimize POSTING SCHEDULE
────────────────────────────────────────────────

Performance by day of week:
  Monday:    4.2% CTR ✅
  Tuesday:   4.8% CTR 🚀 BEST
  Wednesday: 3.9% CTR
  Thursday:  4.1% CTR
  Friday:    3.5% CTR ⚠️

ACTION:
  👉 Post Tuesday mornings (best performance)
  👉 Avoid Friday posts (lower engagement)
  👉 Post 2-3 times per Tuesday for maximum reach
  👉 Expected improvement: +8-12% CTR

─────────────────────────────────────────────────

RECOMMENDATION 5: Increase ENGAGEMENT (Comments/Shares)
────────────────────────────────────────────────

Current engagement rate: 3.8% (decent)
Target: 4.5%+ (excellent)

What drives engagement:
  • Posts with questions: +40% comments
  • Posts with specific facts: +30% shares
  • Posts with call-to-action: +25% saves

ACTION:
  👉 Add 1 question to each post (mid or end)
  👉 Include 3-5 specific numbers/facts
  👉 Make CTA more engaging ("save this" vs "read more")
  👉 Expected improvement: Engagement 4.8/5+ stars

─────────────────────────────────────────────────

RECOMMENDATION 6: Topic DIVERSIFICATION
────────────────────────────────────────────────

Current topics:
  • ИИ & Content: 6 posts (50%)
  • Time Saving: 3 posts (25%)
  • Personal Growth: 2 posts (17%)
  • Other: 1 post (8%)

Recommendation:
  • ИИ is your strength (keep it)
  • Add more "Personal Growth" posts (good angle)
  • Consider audience pain points (what else do they need?)

ACTION:
  👉 Next 3 ideas: 2x ИИ + 1x Personal Growth
  👉 Research broader skill-building angles
  👉 Expected result: Wider audience appeal + growth

─────────────────────────────────────────────────

QUICK WINS (implement immediately)
─────────────────────────────────────────────────

✅ EASY (< 30 min each):
  1. Rewrite Post #4 hook (add urgency)
  2. Rewrite Post #6 CTA (make explicit)
  3. Schedule next posts for Tuesday
  4. Add questions to all drafts

✅ MEDIUM (30-60 min):
  5. Analyze Post #8 in detail (what made it viral?)
  6. Create 3 new posts with curiosity angle
  7. Add numbers/facts to all weak posts

✅ LONG-TERM (ongoing):
  8. Track which angles work best (update angles_library.csv)
  9. Experiment with new angles monthly
  10. Build a "winning formula" playbook

═════════════════════════════════════════════════════════════════
```

### 3. Present Implementation Options

```
Готово! Что делать дальше?

[1] FIX WEAK POSTS — Переписать посты с низким CTR
   (автоматически перейду в EDIT MODE для Posts #4 и #6)

[2] CREATE NEW POSTS — Создать новые посты с топ углами
   (вернусь в CREATE MODE для новых идей)

[3] ANALYZE POST #8 — Детальный анализ вирусного поста
   (посмотрю что точно сработало)

[4] SCHEDULE POSTS — Спланировать публикацию по дням
   (оптимизирую по лучшим дням недели)

[M] Back to MENU — Вернуться в меню

═════════════════════════════════════════════════════════════════
```

**[1] FIX WEAK POSTS:**
Load EDIT MODE for selected posts

**[2] CREATE NEW POSTS:**
Load CREATE MODE with recommended angles

**[3] ANALYZE POST #8:**
Load deep-dive analysis for top post

**[4] SCHEDULE POSTS:**
Open scheduling interface

**[M] Back to MENU:**
Load `./c-00-menu.md`

---

## NEXT STEP

Handle user selection
