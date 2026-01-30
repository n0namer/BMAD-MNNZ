# FRONTMATTER FIXES - ACTION CHECKLIST

**Status:** 3 Critical + 2 High Priority Issues Identified
**Target Completion:** Before next pipeline execution

---

## PRIORITY 1: CRITICAL (FIX IMMEDIATELY)

### Issue 1: c-03b-select-angle.md - Invalid YAML nextStepFile

**File:** `steps-c/c-03b-select-angle.md`

**Current (BROKEN):**
```yaml
---
description: User selects which angle (from research) to use for the post
name: step-c-03b-select-angle
nextStepFile: ./c-03b1-offer-check.md (for demo) OR ./c-03c-draft.md (for normal)
type: selection
---
```

**Problem:** `nextStepFile` contains invalid YAML with parentheses and "OR" operator

**Fix Option A (Recommended - Full Conditional):**
```yaml
---
description: User selects which angle (from research) to use for the post
name: step-c-03b-select-angle
type: selection
conditional:
  type: "routing"
  field: "content_type"
  routes:
    - condition: "demo"
      nextStepFile: ./c-03b1-offer-check.md
      description: "Demo content - filter offers first"
    - condition: "normal"
      nextStepFile: ./c-03c-draft.md
      description: "Normal content - skip offer filtering"
    - condition: "*"
      nextStepFile: ./c-03c-draft.md
      description: "Default - proceed to draft"
---
```

**Fix Option B (Simple Fix):**
```yaml
---
description: User selects which angle (from research) to use for the post
name: step-c-03b-select-angle
type: selection
nextStepFile: ./c-03c-draft.md
---
```
Then add conditional routing logic in step body.

**Recommended:** Option A

**Verification After Fix:**
- [ ] File can be parsed as valid YAML
- [ ] `conditional.routes` array has all 3 cases
- [ ] All referenced files exist

---

### Issue 2: c-03c-draft.md - Malformed YAML

**File:** `steps-c/c-03c-draft.md`

**Current (BROKEN):**
```yaml
---
description: Generate 3 draft post variations based on selected angle
name: step-c-03c-draft
nextStepFile: ./c-03d-variants.md
type: content-generation
Дай feedback на все варианты:
Например:
---
```

**Problem:** Last 2 lines are not valid YAML fields (no values after colons, trailing spaces)

**Fix:**
```yaml
---
description: Generate 3 draft post variations based on selected angle
name: step-c-03c-draft
type: content-generation
nextStepFile: ./c-03d-variants.md
---
```

**What to do:** Remove the last 2 lines completely. If that feedback text should be in the file, move it BELOW the frontmatter.

**Verification After Fix:**
- [ ] Frontmatter ends with `---` on clean line
- [ ] No trailing whitespace
- [ ] File parses as valid YAML

---

### Issue 3: c-03e-finalize.md - Malformed YAML

**File:** `steps-c/c-03e-finalize.md`

**Current (BROKEN):**
```yaml
---
Location: posts_content.csv
Post ID: post_001 [assigned]
Save to posts_content.csv, then proceed:
Status: SAVED (draft, not published)
description: Final approval of post and save to database
name: step-c-03e-finalize
nextStepFile: ./c-00-menu.md
type: finalization
Варианты сохранены:
---
```

**Problems:**
1. Contains non-standard fields mixed with required fields
2. Some fields have incomplete/trailing syntax
3. Inconsistent with standard schema

**Fix:**
```yaml
---
description: Final approval of post and save to database
name: step-c-03e-finalize
type: finalization
nextStepFile: ./c-00-menu.md
---
```

**What to do:**
1. Remove these fields: `Location`, `Post ID`, `Save to posts_content.csv`, `Status`, `Варианты сохранены`
2. Keep only the 4 required fields
3. Move any informational content to step body

**Verification After Fix:**
- [ ] Only 4 fields in frontmatter: description, name, type, nextStepFile
- [ ] Fields in alphabetical order (best practice)
- [ ] No non-standard fields remain
- [ ] File parses as valid YAML

---

## PRIORITY 2: HIGH (FIX TODAY)

### Issue 4: c-03b1-offer-check.md - Schema Mismatch

**File:** `steps-c/c-03b1-offer-check.md`

**Current (NON-STANDARD):**
```yaml
---
stepId: c-03b1
stepType: user-input
stepName: Фильтр Офферов — "Мне Не Лень?" (Content Machine Stage 4)
estimatedMinutes: 2
nextStepFile: ./c-03b2-offer-generation.md
---
```

**Problems:**
1. Uses `stepId`, `stepType`, `stepName` instead of standard `name`, `type`, `description`
2. Missing required `description` field
3. No conditional trigger documentation

**Fix:**
```yaml
---
name: step-c-03b1-offer-check
type: offer-filtering
description: Filter and configure which offer types to generate for demo content
nextStepFile: ./c-03b2-offer-generation.md
estimatedMinutes: 2
conditional:
  type: "execution"
  field: "content_type"
  condition: "demo"
  mode: "only-if-match"
  description: "Only executed when content_type is 'demo'"
---
```

**What to do:**
1. Rename fields: `stepId` → `name`, `stepType` → `type`, `stepName` → `description`
2. Add `conditional` section to document when this step runs
3. Ensure `name` value matches filename pattern

**Verification After Fix:**
- [ ] Uses standard field names: name, type, description, nextStepFile
- [ ] Field order: name, type, description, nextStepFile, then optional fields
- [ ] Has conditional section explaining execution trigger
- [ ] Matches schema of other files (c-01, c-02c, etc.)

---

### Issue 5: c-03b2-offer-generation.md - Schema Mismatch

**File:** `steps-c/c-03b2-offer-generation.md`

**Current (NON-STANDARD):**
```yaml
---
stepId: c-03b2
stepType: automated
stepName: Генерация Офферов On-the-Fly (Content Machine Stage 3)
estimatedMinutes: 1
nextStepFile: ./c-03c-draft.md
---
```

**Problems:**
1. Same as Issue 4 - non-standard field names
2. Missing `description` field
3. Missing conditional trigger documentation

**Fix:**
```yaml
---
name: step-c-03b2-offer-generation
type: offer-generation
description: Automatically generate 2-4 contextual offers based on demonstrated routine, selected angle, and pain points
nextStepFile: ./c-03c-draft.md
estimatedMinutes: 1
conditional:
  type: "execution"
  field: "content_type"
  condition: "demo"
  mode: "only-if-match"
  description: "Only executed when content_type is 'demo' - auto-generates offers on-the-fly"
---
```

**What to do:**
Same as Issue 4 - standardize field names and add conditional documentation

**Verification After Fix:**
- [ ] Uses standard field names
- [ ] Field order is consistent
- [ ] Has conditional section
- [ ] Description explains what step auto-generates

---

## PRIORITY 3: MEDIUM (FIX THIS WEEK)

### Remaining Medium Priority Items

These are documented in the full validation report. Recommended actions:

**Conditional Routing Documentation** (c-03b-select-angle.md)
- [ ] Ensure conditional.routes covers all content_type values
- [ ] Document both "demo" and "normal" paths
- [ ] Add default route

**Optional: Add estimatedMinutes Field**
- [ ] c-01-add-idea.md (currently missing)
- [ ] c-02c-research.md (currently missing)
- [ ] c-02d-results.md (currently missing)
- [ ] c-03c-draft.md (currently missing)
- [ ] c-03d-variants.md (currently missing)
- [ ] c-03e-finalize.md (currently missing)

Example:
```yaml
estimatedMinutes: 3
```

---

## STANDARD FIELD ORDER (BEST PRACTICE)

Apply this order to all files for consistency:

```yaml
---
name: step-{code}
type: {type}
description: {description}
nextStepFile: ./path-to-next.md
estimatedMinutes: {number}
conditional:  # Only if conditional
  type: "routing" | "execution"
  ...
---
```

---

## QUICK VALIDATION SCRIPT

After making changes, verify each file:

```bash
# Check if file is valid YAML
python -m yaml steps-c/FILENAME.md

# Or using Node.js
node -e "require('js-yaml').load(require('fs').readFileSync('./steps-c/FILENAME.md', 'utf8'))"
```

---

## FILES STATUS AFTER FIXES

| File | Issue | Status | Fix Priority | Verification |
|------|-------|--------|--------------|--------------|
| c-01-add-idea.md | None | ✅ Pass | - | Skip |
| c-02c-research.md | None | ✅ Pass | - | Skip |
| c-02d-results.md | None | ✅ Pass | - | Skip |
| c-03b-select-angle.md | Invalid YAML | ❌ Fail | 🔴 NOW | Update frontmatter |
| c-03b1-offer-check.md | Schema mismatch | ❌ Fail | 🟡 TODAY | Rename fields |
| c-03b2-offer-generation.md | Schema mismatch | ❌ Fail | 🟡 TODAY | Rename fields |
| c-03c-draft.md | Malformed YAML | ❌ Fail | 🔴 NOW | Remove bad lines |
| c-03d-variants.md | None | ✅ Pass | - | Skip |
| c-03e-finalize.md | Malformed YAML | ❌ Fail | 🔴 NOW | Clean frontmatter |

**Total to fix:** 5 files (3 critical + 2 high)
**Estimated time:** 15-20 minutes
**Impact:** Enables proper pipeline automation and conditional routing

---

## TESTING AFTER FIXES

1. **YAML Validation**
   - [ ] All 9 files parse as valid YAML
   - [ ] No syntax errors
   - [ ] All required fields present

2. **Conditional Routing Test**
   - [ ] c-03b-select-angle → c-03b1 when content_type="demo"
   - [ ] c-03b-select-angle → c-03c when content_type="normal"
   - [ ] c-03b1 skipped for normal content
   - [ ] c-03b2 skipped for normal content

3. **NextStepFile References**
   - [ ] All nextStepFile values point to valid files
   - [ ] No broken links
   - [ ] Paths are relative and correct

4. **Automation Ready**
   - [ ] Can parse and route steps automatically
   - [ ] Can display menu with proper descriptions
   - [ ] Can determine conditional execution paths

---

**Checklist created by:** Code Analyzer Agent
**Date:** 2026-01-30
**Next step:** Execute fixes and run tests
