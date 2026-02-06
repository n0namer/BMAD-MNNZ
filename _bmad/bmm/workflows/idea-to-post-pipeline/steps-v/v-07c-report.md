---
description: Generate idea validation report with proceed/revise/skip recommendations
name: step-v-07c-report
nextStepFile: ./v-00-menu.md
type: report-generation
---

## SAVED DATA

Store idea validation report:
```json
{
  "report_id": "idea-validation-[timestamp]",
  "date_generated": "[today]",
  "total_ideas": 47,
  "proceed_count": 38,
  "revise_count": 6,
  "skip_count": 3,
  "viability_rate": 81,
  "proceed_ideas": [1, 3, 5, 6, ...],
  "revise_ideas": [2, 8, 12, 15, 18, 21],
  "skip_ideas": [4, 22, 35],
  "recommendations": [ ... ]
}
```

---

## NEXT STEP

Handle user selection: save report, proceed to research, or clarify ideas

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# VALIDATE V-07C: Idea Validation Report

## STEP GOAL:

Generate report with idea validation results: recommend proceed, revise, or skip for each idea.

## EXECUTION:

### 1. Display Report Header

```
═══════════════════════════════════════════════════════════════

  💡 IDEA VALIDATION REPORT

  Дата отчёта: [today]
  Проверено идей: 47
  Порог жизнеспособности: 81%

═══════════════════════════════════════════════════════════════
```

### 2. Overall Results

```
IDEA VIABILITY ASSESSMENT:

Ready for Research: 38 ideas (81%) ✅ PROCEED
Needs Clarification: 6 ideas (13%) ⚠️ REVISE FIRST
Not Viable Now: 3 ideas (6%) ❌ SKIP

Time Savings: By validating before research, you'll save
approximately 5-8 hours by skipping research on 3 ideas
```

### 3. PROCEED Ideas (Ready for Research)

```
✅ READY FOR RESEARCH (38 ideas):

These 38 ideas are specific, researchable, and have clear
audiences. Proceed directly to research phase (mode-c-02).

PRIORITY 1 (Start with these - highest engagement):
  1. "The Future of AI in Education"
  2. "Why Remote Work is Failing"
  3. "Hidden Costs of Not Delegating"
  4. "The Psychology of Productivity"
  5. "Emerging Trends in Tech for 2024"

PRIORITY 2 (Good ideas, solid audience):
  6-25. [20 more ideas listed with brief descriptions]

PRIORITY 3 (Smaller niche but viable):
  26-38. [12 more ideas listed]

Recommendation: Start with Priority 1 (top 5 ideas)
These have highest engagement potential and trending appeal.
```

### 4. REVISE Ideas (Clarify Before Research)

```
⚠️ NEEDS CLARIFICATION (6 ideas - Revise then Proceed):

Idea #2: "How to Build Better Habits"
  Problem: Too generic, similar to many existing posts
  Recommendation: Specify angle
    Options:
      → "The 66-Day Habit Building Method (Science-Backed)"
      → "How to Build Habits That Actually Stick (No Motivation)"
      → "The Specific Habit Loop Proven by 2.3M People"
  Action: Clarify angle, then proceed to research

Idea #8: "Productivity Tips for Developers"
  Problem: "Tips" is too generic, broad audience
  Recommendation: Add specificity
    Options:
      → "Stop Being Busy: The Focus Formula for Developers"
      → "Context Switching Costs Developers 2.1 Hours Daily"
      → "How to Achieve Flow State as a Programmer"
  Action: Clarify and narrow angle, then proceed

Idea #12: "Leadership in Modern Times"
  Problem: Vague topic, unclear target audience
  Recommendation: Specify audience and angle
    Options:
      → "Remote Team Leadership: The 5-Person Rule"
      → "Why Traditional Leadership Fails Gen Z Employees"
      → "Building Trust in Virtual Teams (5 Frameworks)"
  Action: Specify audience and angle

[3 more REVISE ideas with specific recommendations]

RECOMMENDATION: Spend 10-15 min clarifying these 6 ideas,
then add them to PROCEED list for research.
```

### 5. SKIP Ideas (Not Viable Now)

```
❌ NOT VIABLE AT THIS TIME (3 ideas - Skip for now):

Idea #4: "Something about marketing"
  Issues: ❌ Too vague | ❌ No clear angle | ❌ No audience
  Why: Needs complete reworking, not just clarification
  Recommendation: SKIP - Too much work to salvage
  Alternative: Come back to this in 2-3 months when clearer

Idea #22: "Random thoughts on life"
  Issues: ❌ Not specific | ❌ Too personal/philosophical
           ❌ Hard to make content | ❌ Limited audience
  Why: Not suitable for professional content platform
  Recommendation: SKIP - Doesn't fit content strategy

Idea #35: "Everything you need to know about..."
  Issues: ❌ Too broad | ❌ Competing with hundreds of posts
           ❌ No unique angle
  Why: Extremely saturated topic with no differentiation
  Recommendation: SKIP - Wait for unique angle to emerge

RECOMMENDATION: Archive these 3 ideas for now.
Consider revisiting in future when you have clearer angles.
```

### 6. Validation Summary by Criteria

```
VALIDATION DIMENSION BREAKDOWN:

Specificity (Specific enough?):
  ✅ 40 ideas (85%) are sufficiently specific
  ⚠️ 5 ideas (11%) need clarification
  ❌ 2 ideas (4%) too vague to salvage

Researchability (Can you research this?):
  ✅ 42 ideas (89%) have available research
  ⚠️ 4 ideas (9%) need creative sourcing
  ❌ 1 idea (2%) difficult to research

Audience Clarity:
  ✅ 41 ideas (87%) have clear target audience
  ⚠️ 5 ideas (11%) unclear audience
  ❌ 1 idea (2%) no audience

Uniqueness (Not duplicate?):
  ✅ 38 ideas (81%) unique angles
  ⚠️ 6 ideas (13%) similar but different angle
  ❌ 3 ideas (6%) duplicate topics

Engagement Potential:
  ✅ 39 ideas (83%) high engagement potential
  ⚠️ 6 ideas (13%) moderate potential
  ❌ 2 ideas (4%) low engagement potential
```

### 7. Action Plan

```
IMMEDIATE ACTIONS (Next 2 hours):

Step 1: Review REVISE ideas (6 ideas)
  → Spend 10-15 min clarifying each
  → Move to PROCEED list once clarified
  → Est. time: 1-1.5 hours

Step 2: Research Priority 1 ideas (5 ideas)
  → Start with highest engagement topics
  → Follow mode-c-02 RESEARCH workflow
  → Est. time: 2-3 hours per idea

Step 3: Archive SKIP ideas (3 ideas)
  → Move to archive for future reconsideration
  → Est. time: 5 minutes

NEXT MONTH:

Step 4: Revalidate 38 PROCEED ideas
  → Check for new competing posts
  → Identify best research angles
  → Prioritize based on trends

Step 5: Brainstorm replacements for SKIP ideas
  → Generate new ideas with clearer angles
  → Come back to similar topics with unique twists
```

### 8. Export & Actions

```
═══════════════════════════════════════════════════════════════

Что дальше?

[S] SAVE REPORT — Сохранить отчёт (PDF/CSV)
[R] RESEARCH IDEAS — Начать исследование идей (PROCEED)
[C] CLARIFY IDEAS — Уточнить идеи (REVISE)
[A] ARCHIVE SKIP — Архивировать неприемлемые идеи
[M] BACK to MENU — Вернуться в меню VALIDATE

═══════════════════════════════════════════════════════════════
```

**[S] SAVE REPORT:**
Export validation report to `/outputs/idea-validation-reports/`

**[R] RESEARCH IDEAS:**
Load mode-c-02 RESEARCH with PROCEED ideas pre-selected

**[C] CLARIFY IDEAS:**
Show form to clarify REVISE ideas, then move to PROCEED

**[A] ARCHIVE SKIP:**
Archive 3 SKIP ideas, mark as reviewed

**[M] BACK to MENU:**
Load `./v-00-menu.md`

---

## SAVED DATA

Store idea validation report:
```json
{
  "report_id": "idea-validation-[timestamp]",
  "date_generated": "[today]",
  "total_ideas": 47,
  "proceed_count": 38,
  "revise_count": 6,
  "skip_count": 3,
  "viability_rate": 81,
  "proceed_ideas": [1, 3, 5, 6, ...],
  "revise_ideas": [2, 8, 12, 15, 18, 21],
  "skip_ideas": [4, 22, 35],
  "recommendations": [ ... ]
}
```

---

## NEXT STEP

Handle user selection: save report, proceed to research, or clarify ideas

