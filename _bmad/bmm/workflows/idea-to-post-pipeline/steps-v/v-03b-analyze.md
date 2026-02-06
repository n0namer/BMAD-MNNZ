---
description: Check consistency in tone, brand voice, messaging, and style across posts
name: step-v-03b-analyze
nextStepFile: ./v-03c-report.md
type: automated-analysis
---

# VALIDATE V-03B: Cross-Post Consistency Analysis

## STEP GOAL:

Analyze consistency across posts: tone consistency, brand voice alignment, messaging consistency, writing style uniformity.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Analysis Start

```
═══════════════════════════════════════════════════════════════

  🔍 ANALYZING CROSS-POST CONSISTENCY

  Анализирую 20 постов на консистентность...

═══════════════════════════════════════════════════════════════
```

### 2. Run Consistency Checks

For each dimension, analyze all posts:

#### CHECK 1: Tone Consistency
- Informal vs Formal: Does author maintain same tone?
- Professional vs Casual: Consistent mix?
- Serious vs Humorous: Consistent use of humor?

#### CHECK 2: Brand Voice
- Vocabulary: Consistent word choice patterns?
- Phrases: Recurring patterns/phrases?
- Personality: Same author "voice" throughout?

#### CHECK 3: Messaging Alignment
- Core message: Posts align with overall theme?
- Value proposition: Consistent benefits offered?
- Audience address: Same target audience recognition?

#### CHECK 4: Writing Style
- Sentence structure: Similar patterns?
- Paragraph length: Consistent formatting?
- Structure: Similar post organization (hook-problem-solution)?

### 3. Generate Consistency Analysis

```
Analyzing consistency...

TONE ANALYSIS:
┌─ Formal/Informal Ratio:
│  Post #1-5: 60% informal / 40% formal ✅ CONSISTENT
│  Post #6-10: 55% informal / 45% formal ✅ CONSISTENT
│  Post #11-15: 65% informal / 35% formal ⚠️ SLIGHTLY OFF
│  Post #16-20: 50% informal / 50% formal ❌ INCONSISTENT
│
└─ Overall Tone Consistency: 75% ⚠️

BRAND VOICE ANALYSIS:
┌─ Vocabulary patterns:
│  Posts #1-8: "powerful", "simple", "transform" - ✅ CONSISTENT
│  Posts #9-15: "amazing", "awesome", "incredible" - ⚠️ DIFFERENT
│  Posts #16-20: "essential", "critical", "vital" - ❌ NEW PATTERN
│
├─ Signature phrases:
│  "Here's the thing:" - appears 12x across posts ✅ SIGNATURE
│  "Don't miss this:" - appears 5x (less consistent) ⚠️
│
└─ Overall Brand Voice Consistency: 70% ⚠️

MESSAGING ALIGNMENT:
┌─ Core value proposition:
│  Posts #1-7: Productivity/efficiency focus ✅
│  Posts #8-14: Learning/growth focus ✅
│  Posts #15-20: Mindset/psychology focus ⚠️ SHIFT
│
├─ Target audience recognition:
│  Posts #1-10: Professionals/knowledge workers ✅
│  Posts #11-15: Mixed audience ⚠️
│  Posts #16-20: Students/beginners ❌ DIFFERENT
│
└─ Overall Messaging Consistency: 65% ⚠️

WRITING STYLE ANALYSIS:
┌─ Sentence structure:
│  Avg sentence length: 18 words
│  Variation: ±3 words ✅ CONSISTENT
│
├─ Paragraph structure:
│  Avg paragraph: 3-5 sentences ✅ CONSISTENT
│
└─ Overall Style Consistency: 85% ✅ GOOD
```

### 4. Summary

```
CONSISTENCY AUDIT COMPLETE:

Tone Consistency: 75% ⚠️ (slight drift in recent posts)
Brand Voice: 70% ⚠️ (vocabulary shifting)
Messaging: 65% ❌ (target audience changed)
Writing Style: 85% ✅ (good alignment)

OVERALL CONSISTENCY SCORE: 74% (ACCEPTABLE)

Issues Detected:
  1. Recent posts (16-20) shift tone and voice
  2. Messaging shifted from productivity to mindset
  3. Target audience changed from professionals to beginners
  4. New vocabulary patterns introduced
```

### 5. Progress

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Consistency Analysis: 100% Complete (20/20 posts)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## SAVED DATA

Store consistency analysis results:
```json
{
  "validation_type": "consistency_check",
  "posts_analyzed": 20,
  "scores": {
    "tone_consistency": 75,
    "brand_voice": 70,
    "messaging_alignment": 65,
    "writing_style": 85,
    "overall": 74
  },
  "issues": [
    {"type": "tone_drift", "posts": [16, 17, 18, 19, 20], "severity": "medium"},
    {"type": "vocabulary_shift", "posts": [9, 10, 11], "severity": "low"},
    {"type": "messaging_change", "posts": [15, 16, 17, 18, 19, 20], "severity": "high"},
    {"type": "audience_shift", "posts": [16, 17, 18, 19, 20], "severity": "high"}
  ]
}
```

---

## NEXT STEP

Generate detailed consistency report with specific issues and recommendations

