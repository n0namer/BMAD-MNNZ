---
description: Run 5 automated quality checks in parallel (quality/CTR/consistency/copy/engagement)
name: step-yolo-03-self-check
nextStepFile: ./step-yolo-04-auto-improve.md
type: validation
---

# YOLO Step 3: Automated Self-Check

## STEP GOAL:

Run 5 parallel quality checks on all generated posts, score each one, identify issues for auto-fixing.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Check Start

```
═══════════════════════════════════════════════════════════════

  🔍 AUTOMATED QUALITY CHECKS (5 parallel)

  Проверяю все посты по 5 критериям...

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
