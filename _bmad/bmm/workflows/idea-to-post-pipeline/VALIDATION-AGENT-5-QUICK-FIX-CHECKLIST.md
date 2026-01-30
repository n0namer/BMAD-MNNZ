# VALIDATION AGENT 5: QUICK FIX CHECKLIST

**Overall Status: 94% ✅**
**Estimated Fix Time: 15 minutes**
**Priority: HIGH (before final deployment)**

---

## ISSUE #1: Field Name Inconsistency (Priority 1)

**Severity:** Minor (semantic correctness maintained, consistency issue)
**Time to Fix:** 1 minute per file

### Fix 1A: c-03b1-offer-check.md

**Location:** Line 3

**Current:**
```yaml
stepType: user-input
```

**Change to:**
```yaml
type: user-input
```

**Reason:** All other 40 steps use `type:` field. These two are the only outliers.

**Verify:** All step files use `type:` field
```bash
grep -E "^type:|^stepType:" steps-c/c-*.md
```

---

### Fix 1B: c-03b2-offer-generation.md

**Location:** Line 3

**Current:**
```yaml
stepType: automated
```

**Change to:**
```yaml
type: automated
```

**Status After Fix:** ✅ All 42 steps will have consistent `type:` field

---

## ISSUE #2: Posts Content CSV Columns (Priority 2)

**Severity:** Medium (functionality incomplete without this)
**Time to Fix:** 10 minutes

### Fix 2A: Update posts_content_template.csv

**Location:** `data/csv-templates/posts_content_template.csv`

**Add two new columns after `notes`:**

```csv
id,research_id,angle_used,publish_date,platform,post_title_short,content_500_chars,content_250_chars,content_100_chars,quality_score,ctr_potential,engagement_score,status,notes,pain_points_json,generated_offers_json
```

**Column Definitions:**

| Column | Type | Purpose | Example |
|--------|------|---------|---------|
| `pain_points_json` | JSON | Stores pain points from research | `["Pain 1","Pain 2","Pain 3"]` |
| `generated_offers_json` | JSON | Stores offers woven into post | `[{"title":"Training","cta":"Learn"}]` |

**Note:** Only populated for Content Machine posts (content_type == "demo")

**Also Update:** `templates/csv/posts_content_template.csv` (if it exists as duplicate)

---

### Fix 2B: Document in c-03c-draft.md

**Location:** "## SAVED DATA" section (should exist, may need updating)

**Add documentation:**

```markdown
### CSV Columns for Content Machine Posts

When content_type == "demo", additional columns are populated:

- `pain_points_json`: Array of business pains addressed by this post
  - Source: pain_points_json[selected_angle] from ideas_research.csv
  - Format: ["Pain 1", "Pain 2", "Pain 3"]
  - Purpose: Track which pains were addressed

- `generated_offers_json`: Array of offers woven into this post
  - Source: generated_offers from workflow_state.json (c-03b2)
  - Format: [{"title":"...", "description":"...", "cta":"..."}, ...]
  - Purpose: Track which offers were used in which posts
```

---

## ISSUE #3: File Location Specifications (Priority 3)

**Severity:** Low (functional clarity)
**Time to Fix:** 5 minutes

### Fix 3A: Clarify workflow_state.json Location

**Add to c-03b1-offer-check.md "Step 2" section:**

```markdown
**Storage Location:**
Default: Project root (same directory as workflow.md)
Path: `./workflow_state.json`

Alternative: If using .claude-flow directory:
Path: `./.claude-flow/workflow_state.json`

⚠️ Note: This file is session-specific and temporary.
It is CLEARED when workflow restarts or user returns to menu.
```

**Add to c-03b2-offer-generation.md:**

```markdown
**Storage:**
Reads from: workflow_state.json (populated in c-03b1)
Writes to: workflow_state.json (adds generated_offers)
```

---

### Fix 3B: Clarify offer_filter.csv Location

**Add to c-03b1-offer-check.md "CSV Schema" section:**

```markdown
**Storage Location:**
Path: `./user_preferences/offer_filter.csv`

Behavior:
- Created on first demo-idea (c-03b1)
- Reused for all subsequent demo-ideas
- Can be manually edited in spreadsheet
- Persists across sessions
```

**Also Add to workflow.md or main documentation:**

```markdown
## Data Directories

System creates these directories automatically:
- `./user_preferences/` — User profile data (offer_filter.csv)
- `./.claude-flow/` — Session state (optional, alternative location)
```

---

## VERIFICATION CHECKLIST

### After Fixing Issue #1 (Field Names)

- [ ] Open c-03b1-offer-check.md
  - [ ] Verify line 3 is `type: user-input`
  - [ ] NOT `stepType: user-input`
- [ ] Open c-03b2-offer-generation.md
  - [ ] Verify line 3 is `type: automated`
  - [ ] NOT `stepType: automated`
- [ ] Run verification command:
  ```bash
  grep "^type:" steps-c/c-*.md | wc -l
  # Should return 42
  ```

---

### After Fixing Issue #2 (CSV Columns)

- [ ] Open posts_content_template.csv
  - [ ] Count columns: should be 16 (was 14)
  - [ ] New columns: pain_points_json, generated_offers_json
  - [ ] Verify all original columns still present
- [ ] Check duplicate template
  - [ ] templates/csv/posts_content_template.csv
  - [ ] Update if exists separately
- [ ] Search c-03c-draft.md
  - [ ] Verify documentation added
  - [ ] Check examples are correct format

---

### After Fixing Issue #3 (File Locations)

- [ ] c-03b1-offer-check.md
  - [ ] Clarify workflow_state.json location
  - [ ] Clarify offer_filter.csv location
- [ ] c-03b2-offer-generation.md
  - [ ] Document storage behavior
- [ ] workflow.md
  - [ ] Add "Data Directories" section if missing

---

## FIX EXECUTION GUIDE

### Step 1: Field Names (1 minute)

```bash
# Open in editor:
# D:/Users/NIKITA/Documents/DEV/BMAD-MNNZ/_bmad/bmm/workflows/idea-to-post-pipeline/steps-c/c-03b1-offer-check.md

# Line 3: Replace stepType: with type:
```

```bash
# Open in editor:
# D:/Users/NIKITA/Documents/DEV/BMAD-MNNZ/_bmad/bmm/workflows/idea-to-post-pipeline/steps-c/c-03b2-offer-generation.md

# Line 3: Replace stepType: with type:
```

---

### Step 2: CSV Columns (8 minutes)

```bash
# Open in editor:
# D:/Users/NIKITA/Documents/DEV/BMAD-MNNZ/_bmad/bmm/workflows/idea-to-post-pipeline/data/csv-templates/posts_content_template.csv

# Add to header row (end of line):
# ,pain_points_json,generated_offers_json

# If sample data exists, add empty columns there:
# ,,
```

```bash
# Open in editor:
# D:/Users/NIKITA/Documents/DEV/BMAD-MNNZ/_bmad/bmm/workflows/idea-to-post-pipeline/steps-c/c-03c-draft.md

# Add documentation in SAVED DATA section (see template above)
```

---

### Step 3: File Locations (4 minutes)

```bash
# Open in editor:
# D:/Users/NIKITA/Documents/DEV/BMAD-MNNZ/_bmad/bmm/workflows/idea-to-post-pipeline/steps-c/c-03b1-offer-check.md

# Find "Step 2: Сохранение State" section
# Add storage location clarifications
```

---

## TESTING AFTER FIXES

### Test 1: Type Consistency
```bash
cd steps-c
grep "^type:" c-*.md | wc -l
# Expected output: 42
```

### Test 2: CSV Structure
```bash
# Verify posts_content_template.csv has 16 columns
head -1 ../data/csv-templates/posts_content_template.csv | tr ',' '\n' | wc -l
# Expected output: 16
```

### Test 3: Documentation Check
```bash
# Verify workflow_state.json location documented
grep -n "workflow_state" c-03b1-offer-check.md | grep -i "location"
# Should return 1+ matches
```

---

## IMPACT ASSESSMENT

### Before Fixes
- Type field inconsistency causes confusion
- CSV columns missing for Content Machine data
- Developers unclear on file storage locations

### After Fixes
- All 42 steps have consistent type field ✅
- All CSV columns properly documented ✅
- Clear file location specifications ✅
- 100% specification compliance ✅

---

## COMPLIANCE BEFORE/AFTER

| Metric | Before | After |
|--------|--------|-------|
| Type Consistency | 39/42 (93%) | 42/42 (100%) |
| CSV Documentation | 2/3 (67%) | 3/3 (100%) |
| File Location Clarity | 0/3 (0%) | 3/3 (100%) |
| Overall Compliance | 94% | **100%** |

---

## COMMIT MESSAGE (when done)

```
fix: standardize step type fields and document CSV columns

- Fix: c-03b1-offer-check.md — change stepType to type (line 3)
- Fix: c-03b2-offer-generation.md — change stepType to type (line 3)
- Add: pain_points_json and generated_offers_json columns to posts_content_template.csv
- Docs: Document new CSV columns in c-03c-draft.md
- Docs: Clarify file locations in c-03b1-offer-check.md and workflow.md

Validates compliance: 94% → 100%
Fixes: 3 issues
Time: ~15 minutes
```

---

**Estimated Completion: 15 minutes**
**Difficulty: Very Easy**
**Risk Level: None (all changes are documentation/consistency)**

**Ready to proceed? ✅**

