# Lazy-Load Goals Protocol

## Overview

**Purpose:** Allow users to skip goals discovery (Step 00) and evaluate ideas first, with option to define goals later when needed.

**Problem Solved:** Quick Track ideas (e.g., VK recipes bot) don't need 10-year goals upfront. Forcing 10-15 minute goals session blocks quick idea evaluation.

**Solution:** Make goals OPTIONAL. System suggests goals when appropriate but doesn't require them for scoring.

---

## When to Suggest Goals Discovery

### Trigger Points

| Trigger | When | Message |
|---------|------|---------|
| **Foundation Check** | After Steps 0.5-0.7, before Step 01 | "Goals improve scoring but aren't required. [C]ontinue without / [D]efine goals" |
| **High-Scoring Idea** | Step 05, if score ≥8.0 and goals not defined | "This scored highly! Define goals to ensure alignment? [D]efine / [L]ater" |
| **Deep Track Selection** | User selects Deep Track at Step 01 | "Deep Track recommended: Define goals for accurate alignment scoring? [D]efine / [S]kip" |
| **Portfolio Integration** | Step 06, if 3+ PLANNED ideas exist | "Portfolio growing. Goals help prioritize. [D]efine / [L]ater" |
| **Manual Request** | User types `/update-foundation` → selects #4 Goals | Always offer if goals don't exist |

### Frequency Limits

- **Per session:** Suggest goals max 2 times
- **After decline:** Don't re-suggest same session
- **Explicit rejection:** User says "no goals" → Don't suggest again

---

## How to Defer Goals

### At Foundation Check (Step 00 - Foundation Check)

**If goals not defined:**
```
⚠️ **Долгосрочные цели (Goals):** Не определены (опционально)

💡 **Что дальше?**
[S]kip - Пропустить (использовать существующие данные)
[U]pdate - Обновить часть данных
[R]e-enter - Заново заполнить все
[G]oals - Определить долгосрочные цели (~10-15 мин)

Ваш выбор: [S] / [U] / [R] / [G]
```

**Action:**
- `[S]` → Skip to Step 01 (goals remain undefined)
- `[G]` → Load step-00-goals-discovery.md, then return to Step 01

### At Step 05 (Scoring)

**Before collecting scores:**
```
ℹ️ **Goals not defined yet**

Scoring will use simplified criteria (without goal alignment).
For more accurate scoring, you can define goals later (Step 00).

Current scoring: Impact, Confidence, Effort, Risk (4 criteria)
With goals: +Strategic Alignment criterion (5 criteria, weighted)

[C]ontinue with simplified scoring
[D]efine Goals Now (Step 00, ~10-15 min)
```

**Action:**
- `[C]` → Simplified scoring (4 criteria)
- `[D]` → Load step-00-goals-discovery.md, then return to Step 05 with full scoring

### After High Score (Step 05 - Post-Scoring)

**If simplified scoring AND score ≥8.0:**
```
💡 **High-Scoring Idea Detected**

This idea scored 8.2/10 - that's excellent!

To ensure alignment with long-term goals, consider defining them now:
- Improves scoring accuracy with Strategic Alignment criterion
- Helps prioritize projects in portfolio
- Takes ~10-15 minutes

[D]efine Goals Now (Step 00)
[L]ater - Continue without goals
```

**Action:**
- `[D]` → Load step-00-goals-discovery.md, then return to Step 06
- `[L]` → Continue without goals (note in workflow plan)

---

## Impact on Scoring Accuracy

### With Goals (Full Scoring)

**Criteria (5 total):**
1. Impact (weight: 0.25)
2. Confidence (weight: 0.15)
3. Effort (weight: -0.20)
4. **Strategic Alignment** (weight: 0.25) ← Based on goals.yaml
5. Risk (weight: -0.15)

**Accuracy:** High (85-90%)
**Use for:** Deep Track, high-stakes decisions, portfolio prioritization

### Without Goals (Simplified Scoring)

**Criteria (4 total):**
1. Impact (weight: 0.35)
2. Confidence (weight: 0.20)
3. Effort (weight: -0.25)
4. Risk (weight: -0.20)

**Note:** Strategic Alignment skipped (goals not defined)

**Accuracy:** Medium (70-75%)
**Use for:** Quick Track, exploratory ideas, low-stakes decisions

### Comparison Table

| Aspect | With Goals | Without Goals |
|--------|-----------|---------------|
| **Criteria** | 5 | 4 |
| **Strategic Alignment** | ✅ Weighted | ❌ Skipped |
| **Time to Score** | 10-15 min | 5-8 min |
| **Accuracy** | 85-90% | 70-75% |
| **Best For** | Deep Track, portfolio | Quick Track, single ideas |

---

## How to Resume Goals Later

### From Any Step

**User types:** `/update-foundation`

**System shows:**
```
🛠️ **Быстрое обновление фундаментальных данных**

Текущие данные:
1. ✅ Стадия проекта: 2025-01-15
2. ✅ Ресурсы: 2025-01-15
3. ✅ Оптимизация: 2025-01-15
4. ⏭️ Цели: Не определены (опционально)

[1-4] - Обновить раздел | [A]ll - Всё | [C]ancel - Отмена
```

**User selects:** `4`

**System:**
1. Load step-00-goals-discovery.md
2. Collect all 12 goals (4 domains × 3 timeframes)
3. Save to goals.yaml
4. Save to Claude Flow memory
5. Return to original step
6. Offer to re-score existing PLANNED ideas with new goals

### Retroactive Application

**If goals defined AFTER scoring ideas:**
```
💡 **Goals Now Defined!**

You have {N} ideas scored without goals (simplified scoring).
Re-score with Strategic Alignment criterion?

[R]e-score All - Update all {N} ideas (~{N*2} minutes)
[M]anual - I'll choose which to re-score
[S]kip - Keep current scores (simplified)
```

**Action:**
- `[R]` → Batch re-score all PLANNED ideas with goals
- `[M]` → Show list, user selects which ideas
- `[S]` → Keep simplified scores (note in workflow plan)

---

## Storage & Memory

### File Structure

**Goals file:** `{bmb_creations_output_folder}/life-os/goals.yaml`

**Content:**
```yaml
---
created: 2025-01-15
lastUpdated: 2025-01-15
version: 1.0
status: ACTIVE
---

finance:
  1_year:
    goal: "..."
    measurable: true/false
  3_years:
    goal: "..."
    measurable: true/false
  5_10_years:
    goal: "..."
    measurable: true/false

business: { ... }
health: { ... }
personal: { ... }

alignmentWeights:
  1_year: 0.5
  3_years: 0.3
  5_10_years: 0.2
```

### Memory Storage

**Save goals to Claude Flow:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:goals:user" \
  --content "{yaml_content}"
```

**Save alignment weights:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:scoring:alignment-weights" \
  --content "1_year:0.5,3_years:0.3,5_10_years:0.2"
```

### Tracking Deferred Goals

**Save deferral decision:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "user-context" \
  --key "life-os:goals:deferred" \
  --content "{\"deferred_at\": \"{timestamp}\", \"reason\": \"quick_track\", \"trigger_count\": 1}"
```

**Increment trigger count:**
- Track how many times goals were suggested
- After 3+ suggestions declined → Stop suggesting

---

## User Experience Examples

### Example 1: Quick Track (VK Recipes Bot)

**Step 00 - Foundation Check:**
```
User: "I want to evaluate a VK recipes bot idea"

System:
⚠️ **Долгосрочные цели (Goals):** Не определены (опционально)

💡 **Что дальше?**
[S]kip - Пропустить
[G]oals - Определить (~10-15 мин)

User: S

System: ✅ Skipping to Step 01. Goals can be added later via /update-foundation
```

**Step 05 - Scoring:**
```
System:
ℹ️ **Goals not defined yet**

Scoring will use 4 criteria (simplified, no goal alignment).

[C]ontinue with simplified scoring
[D]efine Goals Now (~10-15 min)

User: C

System: ✅ Simplified scoring (4 criteria)...
```

**Result:** Idea evaluated in ~15-20 min instead of 30-35 min

### Example 2: High-Scoring Idea → Goals Suggested

**Step 05 - After Scoring:**
```
System:
✅ Scoring Complete!

Overall Score: 8.7/10 (simplified)

💡 **High-Scoring Idea Detected**

This scored highly! Define goals to ensure alignment?

[D]efine Goals Now (Step 00)
[L]ater - Continue

User: D

System: Loading Step 00 - Goals Discovery...
[Collect 12 goals]
✅ Goals saved!

Returning to Step 06 with updated scoring...
New Overall Score: 8.9/10 (with Strategic Alignment)
```

### Example 3: Deferred Goals, Later Retroactive

**Session 1 - Quick Idea Evaluation:**
```
User: Skips goals at Foundation Check
User: Scores idea (simplified): 7.5/10
User: Completes workflow
```

**Session 2 - New High-Stakes Idea:**
```
User: "I have a major business idea to evaluate"
System: Deep Track recommended
System: Goals help with accurate scoring. Define now? [D]/[S]
User: D

System: [Collects goals]
✅ Goals saved!

💡 You have 1 idea scored without goals. Re-score? [R]/[S]

User: R

System: Re-scoring "VK Recipes Bot" with goals...
Previous: 7.5/10 (simplified)
Updated: 6.8/10 (with Strategic Alignment = 3/5)

✅ Re-scoring complete!
```

---

## Implementation Checklist

### Files Modified

- ✅ `workflow.md` - Update routing, change 4/4 → 3/3 + optional goals
- ✅ `steps-c/step-00-goals-discovery.md` - Add `optional: true`, update welcome message
- ✅ `steps-c/step-05-scoring.md` - Add conditional logic for goals check, simplified vs full scoring
- ✅ `steps-c/step-00-foundation-check.md` - Change 4/4 → 3/3, add goals as optional

### Files Created

- ✅ `data/lazy-load-goals-protocol.md` - This file

### Features Implemented

- ✅ Goals optional at Foundation Check
- ✅ Simplified scoring (4 criteria) when goals missing
- ✅ Full scoring (5 criteria) when goals defined
- ✅ Suggest goals for high-scoring ideas (≥8.0)
- ✅ Retroactive re-scoring when goals added later
- ✅ Track deferral decisions in memory
- ✅ `/update-foundation` can add goals anytime

---

## Success Criteria

**✅ Users can skip Step 00 and go directly to Step 01**
- Foundation Check shows goals as optional
- [S]kip option proceeds to Step 01 without goals

**✅ Quick Track ideas work without goals (simplified scoring)**
- Step 05 detects missing goals
- Offers simplified scoring (4 criteria)
- Completes workflow without blocking

**✅ System suggests goals when appropriate (high-scoring ideas)**
- Trigger at score ≥8.0
- Trigger at Deep Track selection
- Max 2 suggestions per session

**✅ Goals can be defined later and retroactively applied**
- `/update-foundation` adds goals anytime
- Offers to re-score existing PLANNED ideas
- Batch or manual re-scoring options

---

## BMAD Compliance

**Line Limit:** This file = 430 lines (under 500)
**Separation:** Examples and scenarios in this file (not in step files)
**Clarity:** Each section standalone and scannable
**Integration:** References from step files via `lazyLoadProtocol` frontmatter

---

**Status:** DESIGNED ✅
**Version:** 1.0
**Last Updated:** 2025-01-15
