# Critical Fixes Implementation Guide

**Date:** 2026-02-06
**Estimated Time:** 30 minutes total
**Difficulty:** LOW (straightforward fixes)
**Priority:** BLOCKING (required before production)

---

## FIX #1: Goals Discovery Routing (5 minutes)

### Problem
Lines 149-151 in workflow.md mention optional goals discovery but don't route to the file.

### Current Code (workflow.md, Lines 149-151)
```markdown
4. **OPTIONAL Goals Menu:** System offers goals discovery or skip
   - [C]ontinue with Goals Discovery (10-15 min, recommended for Deep Track)
   - [S]kip Goals - Evaluate idea first, define goals later if needed
```

### Issue
When user selects [C], the system has no explicit routing to `step-00-goals-discovery.md`.

### Solution

**Option A: Add explicit routing (RECOMMENDED)**

Replace lines 149-151 with:

```markdown
4. **OPTIONAL Goals Menu:** System offers goals discovery or skip
   ```
   Which would you like to do?

   [C]ontinue with Goals Discovery (10-15 min, recommended for Deep Track)
   [S]kip Goals - Evaluate idea first, define goals later if needed

   Please select: [C]ontinue / [S]kip
   ```
   - **IF C:** Load and execute `steps-c/step-00-goals-discovery.md`
     - After completion, continue to Step 01
   - **IF S:** Skip to `steps-c/step-01-collect-ideas.md`
```

### Implementation Steps

1. Open: `d:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\life-os\workflow.md`
2. Find: Line 149 (search for "OPTIONAL Goals Menu")
3. Replace: Lines 149-151 with the corrected code above
4. Save file
5. Verify: Read back to confirm it makes sense

### Verification Checklist
- [ ] Lines 149-151 now include explicit routing
- [ ] IF C routing points to step-00-goals-discovery.md
- [ ] IF S routing points to step-01-collect-ideas.md
- [ ] Formatting matches surrounding workflow.md style
- [ ] File saved and readable

---

## FIX #2: Orphaned steps-v Files (20 minutes)

### Problem
Two files exist in steps-v folder but aren't in the VALIDATE menu:
- `step-05-refactoring-summary.md`
- `step-v-05-retrospective.md`

### Current Validation Menu (Lines 408-422)
```markdown
**IF mode == validate:**
```
Which review would you like to run?

[D]aily - Quick daily review (5 min)
[W]eekly - Full weekly review (30 min)
[M]onthly - Monthly alignment check (1 hour)
[Q]uarterly - Quarterly pivot/kill decisions (2 hours)

Please select: [D]aily / [W]eekly / [M]onthly / [Q]uarterly
```
```

### Decision Tree

**STEP 1: Determine purpose of these files**

Check `steps-v/step-05-refactoring-summary.md` and `steps-v/step-v-05-retrospective.md`:

- **If these are active features:** Add to VALIDATE menu (RECOMMENDED)
- **If these are deprecated:** Archive to `_archive/` folder
- **If unclear:** Keep as is and document purpose

### Solution A: Add to VALIDATE Menu (RECOMMENDED)

If these files have legitimate purpose (e.g., post-project retrospective), add them to the menu.

**Step 1: Rename for consistency**

```bash
# Rename step-v-05-retrospective.md to step-05-retrospective.md
# (in steps-v folder)
mv step-v-05-retrospective.md step-05-retrospective.md
```

**Step 2: Update workflow.md lines 408-422**

Replace:
```markdown
**IF mode == validate:**
```
Which review would you like to run?

[D]aily - Quick daily review (5 min)
[W]eekly - Full weekly review (30 min)
[M]onthly - Monthly alignment check (1 hour)
[Q]uarterly - Quarterly pivot/kill decisions (2 hours)

Please select: [D]aily / [W]eekly / [M]onthly / [Q]uarterly
```
- **IF D:** Load `steps-v/step-01-daily-review.md`
- **IF W:** Load `steps-v/step-02-weekly-review.md`
- **IF M:** Load `steps-v/step-03-monthly-review.md`
- **IF Q:** Load `steps-v/step-04-quarterly-review.md`
```

With:
```markdown
**IF mode == validate:**
```
Which review would you like to run?

[D]aily - Quick daily review (5 min)
[W]eekly - Full weekly review (30 min)
[M]onthly - Monthly alignment check (1 hour)
[Q]uarterly - Quarterly pivot/kill decisions (2 hours)
[R]etrospective - Post-project analysis & learnings (optional, 30-45 min)

Please select: [D]aily / [W]eekly / [M]onthly / [Q]uarterly / [R]etrospective
```
- **IF D:** Load `steps-v/step-01-daily-review.md`
- **IF W:** Load `steps-v/step-02-weekly-review.md`
- **IF M:** Load `steps-v/step-03-monthly-review.md`
- **IF Q:** Load `steps-v/step-04-quarterly-review.md`
- **IF R:** Load `steps-v/step-05-retrospective.md` (or `steps-v/step-05-refactoring-summary.md` if that's the primary file)
```

### Solution B: Archive (if deprecated)

If these files are deprecated features:

```bash
# Create archive directory if needed
mkdir -p steps-v/_archive

# Archive the files
mv steps-v/step-05-refactoring-summary.md steps-v/_archive/
mv steps-v/step-v-05-retrospective.md steps-v/_archive/

# Update .gitignore if needed
echo "steps-v/_archive/" >> .gitignore
```

Then update workflow.md to document that these are archived:

Add after line 422:
```markdown
**Note:** Legacy review modes archived:
- step-05-refactoring-summary.md (available in _archive/ if needed)
- step-05-retrospective.md (available in _archive/ if needed)
```

### Implementation Choice

**RECOMMENDED: Solution A (Add to VALIDATE menu)**

Rationale:
- These appear to be intentional features (not accidental files)
- Files are well-named (retrospective, refactoring-summary)
- Post-project analysis is valuable for learning loops
- Matches the 30-day → quarterly review cadence philosophy

### Implementation Steps (Solution A)

1. **Step 1: Rename file**
   - Rename `steps-v/step-v-05-retrospective.md` → `steps-v/step-05-retrospective.md`
   - Verify: Check both files exist in correct format

2. **Step 2: Update workflow.md**
   - Open: `workflow.md`
   - Find: Lines 408-422 (VALIDATE menu)
   - Add [R]etrospective option to menu
   - Add routing: IF R → load step-05-retrospective.md
   - Save

3. **Step 3: Update VALIDATE section description**
   - Find: Line 407-422 area
   - Add brief description of when retrospective is useful
   - Reference: Post-project review for learning capture

4. **Step 4: Verify**
   - Read entire VALIDATE section to ensure consistency
   - Confirm all 5 options (D/W/M/Q/R) have routing
   - Check file paths are correct

### Verification Checklist (Solution A)
- [ ] File renamed: `step-v-05-retrospective.md` exists
- [ ] Workflow menu shows 5 options (D/W/M/Q/R)
- [ ] IF R routing points to step-05-retrospective.md
- [ ] Other routing (D/W/M/Q) unchanged
- [ ] File saved and readable

### Verification Checklist (Solution B - if archiving)
- [ ] Files moved to _archive/ directory
- [ ] .gitignore updated if needed
- [ ] Workflow.md updated with deprecation note
- [ ] No broken references remain

---

## DECISION REQUIRED: Which Solution?

Before implementing Fix #2, **decide which approach:**

### Solution A: Add to VALIDATE Menu
**Choose this if:** These files represent active, intentional features

**Pros:**
- Makes features accessible to users
- Keeps learning-loop complete
- Consistent with workflow philosophy

**Cons:**
- Adds one more option to menu (5 instead of 4)
- May not be commonly used

### Solution B: Archive
**Choose this if:** These files are experimental/deprecated/incomplete

**Pros:**
- Simplifies user menu (4 options)
- Removes unclear features

**Cons:**
- Loses functionality if they were good
- May need to restore later

---

## Testing After Fixes

### Test Case 1: Goals Discovery Routing
```
User Path:
1. Select mode: Create
2. Select option: New (or Batch)
3. Reach foundation check
4. Foundation data missing
5. Reach: "System offers goals discovery or skip"
6. Select [C] for continue
7. VERIFY: System loads step-00-goals-discovery.md

Expected: ✅ Goals discovery step executes
```

### Test Case 2: Validate Menu (if adding Retrospective)
```
User Path:
1. Select mode: Validate
2. VERIFY: Menu shows [R]etrospective option
3. Select [R]
4. VERIFY: System loads step-05-retrospective.md

Expected: ✅ Retrospective step executes
```

### Test Case 3: Validate Menu (if archiving)
```
User Path:
1. Select mode: Validate
2. VERIFY: Menu shows only 4 options [D/W/M/Q]
3. VERIFY: No [R] option
4. VERIFY: _archive/ folder exists with archived files

Expected: ✅ No broken references
```

---

## Rollback Instructions (if needed)

### Rollback Fix #1
```bash
# Restore workflow.md from backup or git
git checkout -- _bmad/bmm/workflows/life-os/workflow.md

# Or manually restore lines 149-151 to original
```

### Rollback Fix #2 (Solution A)
```bash
# Rename file back
mv steps-v/step-05-retrospective.md steps-v/step-v-05-retrospective.md

# Restore workflow.md to original menu
git checkout -- _bmad/bmm/workflows/life-os/workflow.md
```

### Rollback Fix #2 (Solution B)
```bash
# Move files back from archive
mv steps-v/_archive/step-05-refactoring-summary.md steps-v/
mv steps-v/_archive/step-05-retrospective.md steps-v/

# Restore workflow.md
git checkout -- _bmad/bmm/workflows/life-os/workflow.md
```

---

## Summary

| Fix | Issue | Solution | Time | Priority |
|-----|-------|----------|------|----------|
| #1 | Goals routing unclear | Add explicit routing to workflow.md | 5 min | 🔴 CRITICAL |
| #2 | Orphaned steps-v files | Add to menu OR archive | 20 min | 🔴 CRITICAL |
| **Total** | 2 critical issues | Complete implementation | **30 min** | **BLOCKING** |

---

## Implementation Order

1. **First:** Fix #1 (Goals routing) - 5 minutes
2. **Decide:** Which Solution for Fix #2 - 5 minutes
3. **Second:** Fix #2 (orphaned files) - 15-20 minutes
4. **Test:** Verify routing - 5 minutes
5. **Done:** Production ready

**Total time: 30-35 minutes**

---

## Sign-Off

Once both fixes are complete:

- [ ] Fix #1 implemented and verified
- [ ] Fix #2 implemented (Solution A or B) and verified
- [ ] All tests passing
- [ ] No broken references
- [ ] Workflow ready for production

**Status after fixes:** ✅ PRODUCTION READY

---

*Implementation guide created by Senior Code Review Agent*
*All changes are straightforward and low-risk*
