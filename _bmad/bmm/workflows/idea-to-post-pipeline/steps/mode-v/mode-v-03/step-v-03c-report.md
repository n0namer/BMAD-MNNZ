---
description: Generate consistency report with issues and recommendations
name: step-v-03c-report
nextStepFile: ../../mode-v/mode-v-00-menu.md
type: report-generation
---

## SAVED DATA

Store consistency report in permanent record:
```json
{
  "report_id": "consistency-[timestamp]",
  "date_generated": "[today]",
  "summary": {
    "posts_analyzed": 20,
    "tone_consistency": 75,
    "brand_voice": 70,
    "messaging_alignment": 65,
    "writing_style": 85,
    "overall": 74
  },
  "high_priority_posts": [16, 17, 18, 19, 20],
  "issues": [ ... ]
}
```

---

## NEXT STEP

Handle user selection: save report, edit inconsistent posts, or generate style guide

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# VALIDATE V-03C: Consistency Check Report

## STEP GOAL:

Generate report showing consistency issues across posts with specific recommendations.

## EXECUTION:

### 1. Display Report Header

```
═══════════════════════════════════════════════════════════════

  📋 CONSISTENCY CHECK REPORT

  Дата отчёта: [today]
  Проверено постов: 20
  Диапазон: Jan 1-15, 2024

═══════════════════════════════════════════════════════════════
```

### 2. Summary Scores

```
CONSISTENCY SCORES:

Tone Consistency: 75% ⚠️ ACCEPTABLE
│ Some drift in recent posts, but mostly consistent

Brand Voice: 70% ⚠️ ACCEPTABLE
│ Vocabulary is shifting, signature phrases maintained

Messaging Alignment: 65% ⚠️ NEEDS WORK
│ Target audience and core message are drifting

Writing Style: 85% ✅ GOOD
│ Sentence/paragraph structure very consistent

═══════════════════════════════════════════════════════════════
OVERALL CONSISTENCY: 74% (ACCEPTABLE)
═══════════════════════════════════════════════════════════════
```

### 3. Detailed Issues

```
🔴 HIGH SEVERITY ISSUES:

Issue #1: Audience Shift (Posts #16-20)
  Problem: Recent posts target students/beginners
           Earlier posts targeted professionals
  Impact: Confuses reader about who content is for
  Posts affected: #16, #17, #18, #19, #20
  Recommendation: Choose ONE target audience and realign
  Fix time: 30-45 min per post

Issue #2: Messaging Misalignment (Posts #15-20)
  Problem: Early posts focus on productivity
           Recent posts focus on mindset/psychology
  Impact: Inconsistent value proposition
  Posts affected: #15, #16, #17, #18, #19, #20
  Recommendation: Either focus on ONE theme or clearly separate by topic
  Fix time: 20-30 min per post

🟡 MEDIUM SEVERITY ISSUES:

Issue #3: Tone Drift (Posts #16-20)
  Problem: Shift from professional to casual tone
  Impact: Affects brand perception
  Posts affected: #16, #17, #18, #19, #20
  Recommendation: Standardize tone across all posts
  Fix time: 10-15 min per post

Issue #4: Vocabulary Shift (Posts #9-11)
  Problem: Introduction of new vocabulary patterns
  Impact: Minor inconsistency
  Posts affected: #9, #10, #11
  Recommendation: Align with core vocabulary set
  Fix time: 5-10 min per post

🟢 LOW SEVERITY ISSUES:

Issue #5: Signature Phrases (Optional)
  Problem: "Don't miss this:" appears inconsistently
  Impact: Minimal - stylistic choice
  Recommendation: Either use consistently or remove
  Fix time: 5 min per post
```

### 4. Consistency Dimensions Breakdown

```
TONE ANALYSIS:

Posts #1-10: Professional + conversational ✅
├─ Example: "Here's something that changed my perspective..."
├─ Tone balance: 60% informal / 40% formal
└─ Consistency: EXCELLENT

Posts #11-15: Professional (slightly more formal) ⚠️
├─ Example: "It's crucial to understand that..."
├─ Tone balance: 55% informal / 45% formal
└─ Consistency: GOOD

Posts #16-20: Very casual (overly informal) ❌
├─ Example: "Dude, this is SO cool..."
├─ Tone balance: 70% informal / 30% formal
└─ Consistency: POOR
```

### 5. Brand Voice Analysis

```
SIGNATURE ELEMENTS:

Core Vocabulary (Using consistently):
  ✅ "powerful", "simple", "transform" (appears 15x)
  ✅ "Here's the thing:" (appears 12x)
  ⚠️ "Don't miss this:" (appears 5x - inconsistent)
  ❌ "amazing", "awesome" (new, conflicts with brand)

Writing Patterns (Maintained):
  ✅ Hook → Problem → Solution structure (90% of posts)
  ✅ Short paragraphs (3-5 sentences) consistent
  ✅ Action-oriented closing (95% of posts)

Audience Recognition:
  Posts #1-10: "If you're a professional..." ✅
  Posts #11-15: "Whether you're starting out..." (mixed) ⚠️
  Posts #16-20: "Hey student, listen up..." ❌ (new audience)
```

### 6. Recommendations

```
FIX PRIORITY:

URGENT (This Week):
  1. Realign audience in Posts #16-20
     → Choose: professionals OR beginners/students
     → Rewrite opening sentences to clarify audience
     → Est. 2-3 hours

  2. Standardize core message (productivity vs mindset)
     → Choose focus area
     → Review Posts #15-20, realign messaging
     → Est. 2-3 hours

SHORT-TERM (This Month):
  3. Unify tone across recent posts
     → Match tone to Posts #1-10 style
     → Review informal/formal balance
     → Est. 1-2 hours

  4. Align vocabulary
     → Remove "amazing/awesome" pattern
     → Strengthen "powerful/simple" pattern
     → Est. 1 hour

ONGOING:
  5. Create "Voice Guidelines" document
     → Document tone, vocabulary, target audience
     → Reference for future posts
     → Ensures new content stays consistent
```

### 7. Before/After Example

```
BEFORE (Inconsistent):

Post #5: "Here's the thing: if you want to transform your
productivity, it's simple. This powerful approach has helped
thousands of professionals..."

Post #18: "Dude, this is SO COOL! Here's an amazing thing
about mindset. It's awesome how beginning learners can use
this incredible technique..."

AFTER (Consistent):

Post #5: "Here's the thing: if you want to transform your
productivity, it's simple. This powerful approach has helped
thousands of professionals..."

Post #18: "Here's the thing: if you want to transform your
mindset, it's simple. This powerful approach has helped
thousands of professionals starting their journey..."

[Tone, vocabulary, audience now match]
```

### 8. Export & Actions

```
═══════════════════════════════════════════════════════════════

Что дальше?

[S] SAVE REPORT — Сохранить отчёт (PDF/CSV)
[E] EDIT INCONSISTENT POSTS — Отредактировать несогласованные
[G] GENERATE VOICE GUIDE — Создать руководство стиля
[M] BACK to MENU — Вернуться в меню VALIDATE

═══════════════════════════════════════════════════════════════
```

**[S] SAVE REPORT:**
Export as PDF/CSV to `/outputs/consistency-reports/`

**[E] EDIT INCONSISTENT POSTS:**
Load mode-c EDIT with Posts #15-20 pre-selected (highest impact)

**[G] GENERATE VOICE GUIDE:**
Create style guide document for future reference

**[M] BACK to MENU:**
Load `../mode-v-00-menu.md`

---

## SAVED DATA

Store consistency report in permanent record:
```json
{
  "report_id": "consistency-[timestamp]",
  "date_generated": "[today]",
  "summary": {
    "posts_analyzed": 20,
    "tone_consistency": 75,
    "brand_voice": 70,
    "messaging_alignment": 65,
    "writing_style": 85,
    "overall": 74
  },
  "high_priority_posts": [16, 17, 18, 19, 20],
  "issues": [ ... ]
}
```

---

## NEXT STEP

Handle user selection: save report, edit inconsistent posts, or generate style guide

