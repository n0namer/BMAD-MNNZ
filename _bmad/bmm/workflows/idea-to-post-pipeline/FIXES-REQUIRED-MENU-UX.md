# MENU & UX FIXES REQUIRED

**Priority:** LOW (all cosmetic/consistency only)
**Effort:** Trivial (10 minutes total)
**Risk:** NONE (no logic changes)

---

## Fix #1: Standardize [M] Menu Label

**Severity:** MINOR
**Type:** Terminology Consistency
**Effort:** Trivial (2 edits)

### Current State
```
c-01-add-idea.md has:
  [M] Back to CREATE MENU

All other menus have:
  [M] Back to MENU
```

### Issue
Inconsistent terminology confuses user expectations:
- "CREATE MENU" suggests a sub-menu within CREATE mode
- "MENU" is clearer (back to main mode menu)

### Fix

**File:** `steps-c/c-01-add-idea.md`

**Change 1 (Line 242):**
```
OLD:  [M] Back to CREATE MENU — Другие операции
NEW:  [M] Back to MENU — Вернуться в меню
```

**Change 2 (Line 254):**
```
OLD:  Load `./c-00-menu.md`
NEW:  Load `./c-00-menu.md`
(This is correct, comment stays as-is)
```

### Impact
- ✅ User sees consistent [M] behavior everywhere
- ✅ Expectation matches reality (goes to c-00-menu.md)
- ✅ No behavioral change, just label

---

## Fix #2: Standardize File Reference Naming

**Severity:** MINOR
**Type:** Naming Convention Consistency
**Effort:** Minor (3-4 edits)

### Current State
```
Most files use:
  ./c-02d-results.md
  ./c-03d-variants.md

Some comments use (WRONG):
  ./step-c-02d-results.md
  ./step-c-03d-variants.md
```

### Issue
If file path matching is strict, will cause file-not-found errors.
Inconsistency in documentation makes maintenance harder.

### Fix

**File 1:** `steps-c/c-02c-research.md`

**Change (Line 195):**
```
OLD:  Load, read entire file, then execute `./step-c-02d-results.md`
NEW:  Load, read entire file, then execute `./c-02d-results.md`
```

**File 2:** `steps-c/c-03c-draft.md`

**Change (Line 314):**
```
OLD:  Load, read entire file, then execute `./step-c-03d-variants.md`
NEW:  Load, read entire file, then execute `./c-03d-variants.md`
```

### Verification
All file references should match pattern: `./c-XXx-name.md`

### Impact
- ✅ Consistent naming convention
- ✅ Prevents file-not-found errors
- ✅ Easier maintenance
- ✅ No behavioral change

---

## Fix #3: Clarify [V] VIEW FULL Option

**Severity:** MINOR
**Type:** Documentation Clarity
**Effort:** Trivial (2 edits)

### Current State
```
c-03c-draft.md shows:
  [V] VIEW FULL — Показать полные версии (250/100 chars)

But actually generates:
  500-char, 250-char, and 100-char versions (3 total)
```

### Issue
User might expect only 2 variants (250 and 100), but 3 are available (500, 250, 100).
The parenthetical "(250/100 chars)" is misleading.

### Fix

**File:** `steps-c/c-03c-draft.md`

**Change 1 (Line 256):**
```
OLD:  [V] VIEW FULL — Показать полные версии (250/100 chars)
NEW:  [V] VIEW FULL — Показать полные версии (500, 250, 100 chars)
```

**Change 2 (Line 297):**
```
OLD:  [V] VIEW FULL — Показать полные версии (250/100 chars)
NEW:  [V] VIEW FULL — Показать полные версии (500, 250, 100 chars)
```

### Impact
- ✅ Clear expectation: user knows 3 variants available
- ✅ No behavioral change
- ✅ Better UX clarity

---

## Fix #4: Add Visual Section Headers (Optional Polish)

**Severity:** COSMETIC
**Type:** Visual Organization
**Effort:** Minor (but optional)
**Recommendation:** NICE TO HAVE (not required)

### Current State
```
c-03c-draft.md displays 6 variants without clear section separation:

Draft 1: DIRECT & PUNCHY (89/100) ⭐
Draft 2: STORYTELLING (84/100)
Draft 3: DATA-DRIVEN (86/100)

Draft 4: PAS (Problem-Agitate-Solution) (87/100) 🔥
Draft 5: Hook-Story-Offer (88/100) 🚀
Draft 6: Show Your Work (Austin Kleon) (85/100) ✨
```

### Issue (Cosmetic)
For users unfamiliar with Content Machine, the jump from Draft 3 to Draft 4 is not immediately obvious.
Visual hierarchy could be improved with section headers.

### Optional Fix

**File:** `steps-c/c-03c-draft.md`

**Lines 267-279, change to:**
```
═════════════════════════════════════════════════════════════════

  ✅ 6 DRAFT VARIANTS CREATED (Content Machine)

  БАЗОВЫЕ ВАРИАНТЫ (Standard Frameworks):
  ─────────────────────────────────────────
  Draft 1: DIRECT & PUNCHY (89/100) ⭐
  Draft 2: STORYTELLING (84/100)
  Draft 3: DATA-DRIVEN (86/100)

  CONTENT MACHINE ФРЕЙМВОРКИ (With Pain Points + Offers):
  ─────────────────────────────────────────
  Draft 4: PAS (Problem-Agitate-Solution) (87/100) 🔥
  Draft 5: Hook-Story-Offer (88/100) 🚀
  Draft 6: Show Your Work (Austin Kleon) (85/100) ✨

  Что дальше?

  [1-6] SELECT DRAFT — Выбрать понравившийся вариант
  [F] FEEDBACK — Дать feedback на все варианты
  [G] GENERATE NEW — Создать новые варианты
  [V] VIEW FULL — Показать полные версии (500, 250, 100 chars)
  [M] Back to MENU

═════════════════════════════════════════════════════════════════
```

### Impact
- ✅ Better visual organization
- ✅ Clearer distinction between standard and CM variants
- ✅ No behavioral change
- ⚠️ Optional (cosmetic only)

---

## QUICK FIX CHECKLIST

### Must Do (5 minutes):
- [ ] Fix #1: Menu label standardization (2 edits)
- [ ] Fix #2: File reference naming (2 edits)

### Should Do (2 minutes):
- [ ] Fix #3: Clarify [V] option (2 edits)

### Nice to Do (3 minutes, optional):
- [ ] Fix #4: Add visual section headers (optional)

**Total Time:** 5-10 minutes

---

## TESTING AFTER FIXES

### Test 1: Navigate with [M] from c-01
```
1. Execute c-01-add-idea.md
2. Select [M] Back to MENU
3. Should load c-00-menu.md ✓
```

### Test 2: Verify file paths work
```
1. Execute c-02c-research.md
2. Select [A] ANGLES
3. Should load c-02d-results.md ✓
4. Select [1-8] SELECT ANGLE
5. Should load c-03b-select-angle.md ✓
```

### Test 3: Verify [V] VIEW FULL shows 3 variants
```
1. Execute c-03c-draft.md
2. Select [V] VIEW FULL
3. Should show 500, 250, and 100-char versions ✓
```

### Test 4: Visual check (optional)
```
1. Execute c-03c-draft.md (for demo)
2. See 6 drafts with clear section headers (if applied)
3. Visual hierarchy clear ✓
```

---

## BEFORE/AFTER COMPARISON

| Issue | Before | After | Impact |
|-------|--------|-------|--------|
| Menu label | "Back to CREATE MENU" | "Back to MENU" | Consistency |
| File refs | `./step-c-02d.md` | `./c-02d.md` | Safety |
| [V] option | "(250/100 chars)" | "(500, 250, 100)" | Clarity |
| Sections | No separation | Section headers | Polish |

---

## NO CHANGES NEEDED TO

✅ Logic or routing (all correct)
✅ Conditional gating (all correct)
✅ Demo flow isolation (all correct)
✅ Halt-and-wait rules (all documented)
✅ Back-to-menu functionality (all working)
✅ Menu options or ordering
✅ Any behavioral aspects

---

## SUMMARY

**Fixes Required:** 4 issues, all trivial
**Blocking Issues:** None
**Logic Changes:** None
**User-Facing Changes:** Minimal (just labels/clarity)
**Risk Level:** ZERO (pure text updates)
**Testing Required:** Simple (path verification)
**Time Estimate:** 5-10 minutes

**Recommendation:** Apply all 4 fixes before user testing.

---

