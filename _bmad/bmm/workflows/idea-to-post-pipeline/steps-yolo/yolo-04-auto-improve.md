---
description: Auto-fix posts scoring below 90%, iterate up to 3 times, present options if still failing
name: step-yolo-04-auto-improve
nextStepFile: ./yolo-05-variants.md
type: improvement-engine
---

# YOLO Step 4: Automatic Improvement Engine

## STEP GOAL:

Iteratively improve posts that scored below 90% quality threshold, max 3 iterations. If still failing, mark for manual review in summary.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Improvement Start

```
═══════════════════════════════════════════════════════════════

  🔧 AUTO-IMPROVING LOW-SCORING POSTS

  Улучшаю посты с score < 90%...

═══════════════════════════════════════════════════════════════
```

### 2. Identify Posts for Improvement

```
Posts needing improvement:
  ⚠️  Post #2: 78% (improve hook + CTA)
  ⚠️  Post #5: 82% (improve problem clarity)
  ❌ Post #6: 45% (major rewrite needed)
```

### 3. Iterative Improvement Loop

**For each failing post (max 3 iterations):**

```
POST #2 - ITERATION 1
─────────────────────────────────────────────

Current: "Как ИИ помогает с контентом"
Score: 78% (Hook: weak, Problem: vague)

Fix 1: Strengthen hook with urgency
New: "3 часа вместо недели: как ИИ подтягивает контент"
Score: 84% ✅ (improved, but still needs CTA)

Fix 2: Make CTA more explicit
New: "3 часа вместо недели: как ИИ подтягивает контент 👉 Хочешь попробовать?"
Score: 91% ✅ PASS!

RESULT: ✅ IMPROVED (3 iterations: 78% → 84% → 91%)
```

### 4. Handle Persistent Failures

```
POST #6 - ITERATION 1-3
─────────────────────────────────────────────

Iteration 1: Rewrite with stronger hook
  Result: 52% (minor improvement)

Iteration 2: Try alternative angle (emotional instead of technical)
  Result: 68% (better, still below threshold)

Iteration 3: Try curiosity angle
  Result: 74% (progress, but < 90%)

RESULT: ⚠️ NEEDS REVIEW (74% after 3 iterations)
  Mark for manual improvement or discard
```

### 5. Display Improvement Summary

```
═══════════════════════════════════════════════════════════════

  ✅ AUTO-IMPROVEMENT COMPLETE:

  ✅ 6 posts IMPROVED & NOW PASSING (≥ 90%)
  ⚠️  2 posts PARTIALLY IMPROVED (70-90%, needs review)
  ❌ 1 post STILL FAILING (< 70%, flag for manual work)

═══════════════════════════════════════════════════════════════

Переходим к генерации вариантов...
```

---

## NEXT STEP

Load, read entire file, then execute `./step-yolo-05-variants.md`
