---
description: Run 5 automated quality checks in parallel (quality/CTR/consistency/copy/engagement)
name: step-yolo-03-self-check
nextStepFile: ./yolo-04-auto-improve.md
type: validation
---

# YOLO Step 3: Automated Self-Check

## STEP GOAL:

Run 8 parallel quality checks on all generated posts (quality/CTR/consistency/copy/engagement/SEO/readability/brand-voice), score each one, identify issues for auto-fixing.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Check Start

```
═══════════════════════════════════════════════════════════════

  🔍 AUTOMATED QUALITY CHECKS (8 parallel)

  Проверяю все посты по 8 критериям...

═══════════════════════════════════════════════════════════════
```

### 2. Run Parallel Checks

**Check 1: Quality Checklist**
- Hook strength: Strong/Weak
- Problem clarity: Clear/Vague
- Solution relevance: Relevant/Irrelevant
- CTA clarity: Explicit/Weak
- Tone consistency: Consistent/Inconsistent

```
Post #1: "ИИ подтянет контент за 3 часа"
├─ Hook: ✅ STRONG (urgency + specificity)
├─ Problem: ✅ CLEAR (time = money)
├─ Solution: ✅ RELEVANT (ИИ helps)
├─ CTA: ✅ CLEAR (explicit action)
├─ Tone: ✅ CONSISTENT
└─ Overall: ✅ 92% PASS
```

**Check 2: CTR Potential**
- Formula: (urgency + specificity + curiosity) / 3
- Score: 0-5%+

```
Post #1: 4.5% CTR potential (HIGH)
Post #2: 3.2% CTR potential (MEDIUM) ⚠️
Post #3: 5.1% CTR potential (EXCELLENT)
```

**Check 3: Consistency**
- Tone: Consistent/Inconsistent
- Format: Consistent/Inconsistent
- Length: Consistent/Inconsistent

```
All 9 posts: ✅ 95% CONSISTENT
```

**Check 4: Copy Audit**
- Strong verbs: Yes/No
- Specific numbers: Yes/No
- Clear benefits: Yes/No

```
Post #1: ✅ Excellent copy
Post #2: ⚠️ CTA too generic (needs improvement)
Post #6: ❌ WEAK copy (needs rewrite)
```

**Check 5: Engagement Potential**
- Factors: Hook, social proof, CTA
- Score: 1-5 stars

```
Post #1: 4.8/5 stars
Post #8: 5.0/5 stars (TOP PERFORMER)
Post #6: 2.1/5 stars ❌ (needs major work)
```

**Check 6: SEO Optimization (NEW)**
- Keyword density: 1-3% optimal
- Meta description quality: Good/Fair/Poor
- Readability for search: Yes/No
- Title optimization: Optimized/Needs work

```
Post #1: SEO Score 88%
├─ Keyword density: 2.1% ✅ OPTIMAL
├─ Meta quality: ✅ GOOD (compelling + under 160 chars)
├─ Search readability: ✅ YES (clear structure)
└─ Title optimization: ✅ OPTIMIZED (hook + keyword)

Post #2: SEO Score 62% ⚠️
├─ Keyword density: 0.4% ⚠️ TOO LOW
├─ Meta quality: ⚠️ FAIR (needs more compelling hook)
├─ Search readability: ✅ YES
└─ Title optimization: ⚠️ NEEDS WORK (missing keyword)

Post #6: SEO Score 41% ❌
├─ Keyword density: 0.1% ❌ INSUFFICIENT
├─ Meta quality: ❌ POOR (too vague, 85 chars only)
├─ Search readability: ❌ NO (poor structure)
└─ Title optimization: ❌ WEAK (no keyword, no hook)
```

**Check 7: Readability Analysis (NEW)**
- Flesch Reading Ease: 60-70 ideal (conversational)
- Avg sentence length: 15-20 words optimal
- Complex words: <10% threshold
- Paragraph structure: Good/Fair/Poor

```
Post #1: Readability Score 92%
├─ Flesch score: 68 ✅ CONVERSATIONAL
├─ Avg sentence: 17 words ✅ OPTIMAL
├─ Complex words: 6% ✅ UNDER THRESHOLD
└─ Structure: ✅ GOOD (varied sentence length)

Post #3: Readability Score 71% ⚠️
├─ Flesch score: 52 ⚠️ SLIGHTLY DIFFICULT
├─ Avg sentence: 23 words ⚠️ TOO LONG
├─ Complex words: 9% ✅ OK
└─ Structure: ⚠️ FAIR (needs more variation)

Post #6: Readability Score 48% ❌
├─ Flesch score: 38 ❌ DIFFICULT
├─ Avg sentence: 28 words ❌ TOO LONG
├─ Complex words: 14% ❌ OVER THRESHOLD
└─ Structure: ❌ POOR (monotonous, no breaks)
```

**Check 8: Brand Voice Consistency (NEW)**
- Tone match: Consistent/Inconsistent
- Vocabulary alignment: Good/Fair/Poor
- Personality traits: Present/Absent
- Voice guidelines: Followed/Violated

```
Post #1: Brand Voice Score 94%
├─ Tone: ✅ CONSISTENT (casual, expert)
├─ Vocabulary: ✅ GOOD (brand-specific terms used)
├─ Personality: ✅ PRESENT (confident, helpful)
└─ Guidelines: ✅ FOLLOWED (all 5 traits present)

Post #4: Brand Voice Score 78% ⚠️
├─ Tone: ✅ CONSISTENT
├─ Vocabulary: ⚠️ FAIR (generic terms used)
├─ Personality: ⚠️ WEAK (lacks confidence)
└─ Guidelines: ⚠️ PARTIALLY (3/5 traits present)

Post #6: Brand Voice Score 52% ❌
├─ Tone: ❌ INCONSISTENT (too formal/stiff)
├─ Vocabulary: ❌ POOR (no brand terms)
├─ Personality: ❌ ABSENT (robotic voice)
└─ Guidelines: ❌ VIOLATED (1/5 traits present)
```

### 3. Display Summary

```
═══════════════════════════════════════════════════════════════

  ✅ VALIDATION SUMMARY:

  ✅ 6 posts PASS (quality ≥ 90%)
  ⚠️  2 posts NEEDS IMPROVEMENT (70-90%)
  ❌ 1 post NEEDS REWRITE (< 70%)

═══════════════════════════════════════════════════════════════

Переходим к автоматическому улучшению...
```

---

## NEXT STEP

Load, read entire file, then execute `./step-yolo-04-auto-improve.md`
