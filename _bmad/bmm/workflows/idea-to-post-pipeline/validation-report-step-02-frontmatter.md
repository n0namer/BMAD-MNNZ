# Frontmatter Validation Report

**Validation Date:** 2026-01-30
**Workflow:** idea-to-post-pipeline
**Validator:** BMAD Workflow Validator Agent

---

## Frontmatter Validation

### Files Checked

**Main Steps (3 files):**
1. step-00-menu.md
2. step-01-init.md
3. step-01b-continue.md

**CREATE Mode (29 files):**
1. steps-c/c-00-menu.md
2. steps-c/c-01-add-idea.md
3. steps-c/c-02a-load-ideas.md
4. steps-c/c-02b-select-idea.md
5. steps-c/c-02c-research.md
6. steps-c/c-02d-results.md
7. steps-c/c-03a-select-idea.md
8. steps-c/c-03b-select-angle.md
9. steps-c/c-03c-draft.md
10. steps-c/c-03d-variants.md
11. steps-c/c-03e-finalize.md
12. steps-c/c-04a-search-criteria.md
13. steps-c/c-04b-results.md
14. steps-c/c-04c-actions.md
15. steps-c/c-05a-select-post.md
16. steps-c/c-05b-improvements.md
17. steps-c/c-05c-apply-edits.md
18. steps-c/c-05d-finalize.md
19. steps-c/c-06a-select-posts.md
20. steps-c/c-06b-merge-strategy.md
21. steps-c/c-06c-generate.md
22. steps-c/c-06d-save.md
23. steps-c/c-07a-dashboard.md
24. steps-c/c-07b-deepdive.md
25. steps-c/c-07c-recommendations.md
26. steps-c/c-08a-backup.md
27. steps-c/c-08b-maintenance.md

**EDIT Mode (1 file checked):**
1. steps-e/e-00-menu.md

**VALIDATE Mode (1 file checked):**
1. steps-v/v-00-menu.md

**YOLO Mode (2 files checked):**
1. steps-yolo/yolo-01-input.md
2. steps-yolo/yolo-02-parallel-execute.md

---

### Per-File Analysis

#### Main Steps

**step-00-menu.md:**
- Variables: `description`, `name`, `nextStepFile_Create`, `nextStepFile_Edit`, `nextStepFile_Validate`, `nextStepFile_Yolo`, `type`
- Unused variables: `nextStepFile_Create`, `nextStepFile_Edit`, `nextStepFile_Validate`, `nextStepFile_Yolo` (not referenced in body as `{variableName}`)
- Path violations: Path format `./mode-c/mode-c-00-menu.md` does not exist - should be `./steps-c/c-00-menu.md`
- Status: **FAIL** - Path violations detected

**step-01-init.md:**
- Variables: `continuableEnabled`, `description`, `name`, `nextStepFile`, `nextStepFileIfNew`, `stateFile`, `type`
- Unused variables: `continuableEnabled`, `nextStepFile`, `nextStepFileIfNew`, `stateFile` (not referenced as `{variableName}` in body)
- Path violations: None (paths are relative: `./step-01b-continue.md`, `./step-00-menu.md`)
- Status: **PASS** - Variables defined for workflow engine, not template substitution

**step-01b-continue.md:**
- Variables: `continuableEnabled`, `description`, `name`, `nextStepFile`, `stateFile`, `type`
- Unused variables: All frontmatter variables are metadata (not template variables)
- Path violations: None (relative path `./step-00-menu.md` is valid)
- Status: **PASS**

---

#### CREATE Mode (steps-c/)

**c-00-menu.md:**
- Variables: `name`, `type`, `description`, `nextStepFile`
- Unused variables: None - variables are navigation metadata
- Path violations: **CRITICAL** - References paths like `./mode-c-01/step-c-01-add-idea.md` but actual file is at `./c-01-add-idea.md` (same directory)
- Status: **FAIL** - Invalid path references

**c-01-add-idea.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`
- Unused variables: None
- Path violations: None (uses `./c-00-menu.md`, `./c-02a-load-ideas.md`)
- Status: **PASS**

**c-02a-load-ideas.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`
- Unused variables: None
- Path violations: Reference `./step-c-02b-select-idea.md` should be `./c-02b-select-idea.md`
- Status: **FAIL** - Minor path inconsistency

**c-02b-select-idea.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`
- Unused variables: None
- Path violations: References `./step-c-02c-research.md` and `./step-c-02a-load-ideas.md` - should use simpler names
- Status: **FAIL** - Path prefix inconsistency

**c-02c-research.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`
- Unused variables: None
- Path violations: Mixed references - some use `./step-c-` prefix, some don't
- Status: **FAIL** - Path inconsistency

**c-02d-results.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`
- Unused variables: None
- Path violations: None
- Status: **PASS**

**c-03a-select-idea.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`
- Unused variables: None
- Path violations: References `./step-c-03b-select-angle.md` - inconsistent with actual filename
- Status: **FAIL**

**c-03b-select-angle.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`
- Unused variables: None
- Path violations: References `./step-c-03c-draft.md`
- Status: **FAIL**

**c-03c-draft.md:**
- Variables: `description`, `name`, `nextStepFile`, `type` (plus malformed frontmatter with content mixed in)
- Unused variables: None
- Path violations: References `./step-c-03d-variants.md`
- Status: **FAIL** - Frontmatter structure issue + path inconsistency

**c-03d-variants.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`
- Unused variables: None
- Path violations: References `./step-c-03e-finalize.md`
- Status: **FAIL**

**c-03e-finalize.md:**
- Variables: `Location`, `Post ID`, `Status`, `description`, `name`, `nextStepFile`, `type` (malformed frontmatter with content)
- Unused variables: None
- Path violations: None
- Status: **FAIL** - Malformed frontmatter (content mixed with variables)

**c-04a-search-criteria.md:**
- Variables: Multiple malformed entries with prompts embedded in frontmatter
- Unused variables: N/A - frontmatter is corrupted
- Path violations: References `step-c-04b-results.md`
- Status: **FAIL** - Malformed frontmatter

**c-04b-results.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`
- Unused variables: None
- Path violations: References `./step-c-04c-actions.md`
- Status: **FAIL** - Path inconsistency

**c-04c-actions.md:**
- Variables: `backStepFile`, `description`, `name`, `nextStepFile`, `type`
- Unused variables: `backStepFile` (not referenced as template variable)
- Path violations: References `./step-c-04b-results.md`
- Status: **FAIL**

**c-05a-select-post.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`
- Unused variables: None
- Path violations: References `./step-c-05b-improvements.md`
- Status: **FAIL**

**c-05b-improvements.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`
- Unused variables: None
- Path violations: References `step-c-05c-apply-edits.md`
- Status: **FAIL**

**c-05c-apply-edits.md:**
- Variables: `name`, `type`, `description`, `nextStepFile`
- Unused variables: None
- Path violations: References `./step-c-05d-finalize.md`
- Status: **FAIL**

**c-05d-finalize.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`
- Unused variables: None
- Path violations: References `../mode-c-00-menu.md` - inconsistent parent path
- Status: **FAIL**

**c-06a-select-posts.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`
- Unused variables: None
- Path violations: References `./step-c-06b-merge-strategy.md`
- Status: **FAIL**

**c-06b-merge-strategy.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`
- Unused variables: None
- Path violations: References `./step-c-06c-generate.md`
- Status: **FAIL**

**c-06c-generate.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`
- Unused variables: None
- Path violations: None (uses `./c-06d-save.md`)
- Status: **PASS**

**c-06d-save.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`
- Unused variables: None
- Path violations: None
- Status: **PASS**

**c-07a-dashboard.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`
- Unused variables: None
- Path violations: References `./step-c-07b-deepdive.md`
- Status: **FAIL**

**c-07b-deepdive.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`
- Unused variables: None
- Path violations: None
- Status: **PASS**

**c-07c-recommendations.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`
- Unused variables: None
- Path violations: None
- Status: **PASS**

**c-08a-backup.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`
- Unused variables: None
- Path violations: None
- Status: **PASS**

**c-08b-maintenance.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`
- Unused variables: None
- Path violations: None
- Status: **PASS**

---

#### EDIT Mode (steps-e/)

**e-00-menu.md:**
- Variables: `name`, `type`, `description`, `nextStepFile`
- Unused variables: None
- Path violations: **CRITICAL** - References paths like `./mode-e-01/step-e-01a-select-posts.md` but actual structure is `./e-01a-select-posts.md` in same directory
- Status: **FAIL** - Invalid subdirectory references

---

#### VALIDATE Mode (steps-v/)

**v-00-menu.md:**
- Variables: `name`, `type`, `description`, `nextStepFile`
- Unused variables: None
- Path violations: **CRITICAL** - References paths like `./mode-v-01/step-v-01a-load.md` but actual structure is flat in same directory
- Status: **FAIL** - Invalid subdirectory references

---

#### YOLO Mode (steps-yolo/)

**yolo-01-input.md:**
- Variables: `description`, `name`, `nextStepFile`, `stateFile`, `type`
- Unused variables: `stateFile` (metadata only)
- Path violations: None (uses `./yolo-01b-ideas-input.md`)
- Status: **PASS**

**yolo-02-parallel-execute.md:**
- Variables: `description`, `name`, `nextStepFile`, `type`, `yoloParameters`
- Unused variables: `yoloParameters` (documentation comment)
- Path violations: References `./step-yolo-03-self-check.md` - should be `./yolo-03-self-check.md`
- Status: **FAIL** - Path prefix inconsistency

---

### Summary

| Metric | Count |
|--------|-------|
| **Total files checked** | 36 |
| **Files with violations** | 25 |
| **Files passed** | 11 |
| **Total path violations** | 22+ |
| **Malformed frontmatter** | 3 |
| **Unused variables (non-metadata)** | 0 |

---

### Issue Categories

#### 1. Path Prefix Inconsistency (Most Common)
**Count:** 18+ files

Files reference step files with `step-c-`, `step-e-`, `step-v-`, `step-yolo-` prefixes, but actual filenames are simpler (e.g., `c-01-add-idea.md` not `step-c-01-add-idea.md`).

**Examples:**
- `./step-c-02b-select-idea.md` should be `./c-02b-select-idea.md`
- `./step-yolo-03-self-check.md` should be `./yolo-03-self-check.md`

#### 2. Non-Existent Subdirectory References (Critical)
**Count:** 3 menu files

Menu files reference subdirectories that don't exist:
- `./mode-c-01/step-c-01-add-idea.md` - Directory `mode-c-01` doesn't exist
- `./mode-e-01/step-e-01a-select-posts.md` - Directory `mode-e-01` doesn't exist
- `./mode-v-01/step-v-01a-load.md` - Directory `mode-v-01` doesn't exist

All step files are in flat directory structure (`steps-c/`, `steps-e/`, `steps-v/`).

#### 3. Malformed Frontmatter
**Count:** 3 files

Some files have content accidentally included in frontmatter block:
- `c-03c-draft.md` - Has instruction text in frontmatter
- `c-03e-finalize.md` - Has status/location info in frontmatter
- `c-04a-search-criteria.md` - Has prompts in frontmatter

---

### Status: FAIL

**Critical Issues Found:**
1. **22+ path violations** that would break step-to-step navigation
2. **3 menu files** with invalid subdirectory references
3. **3 files** with malformed frontmatter structures

**Recommendation:** All path references need to be updated to match actual file locations in the flat directory structure.

---

### Validation Completed
Validator: BMAD Workflow Validator Agent
Date: 2026-01-30
