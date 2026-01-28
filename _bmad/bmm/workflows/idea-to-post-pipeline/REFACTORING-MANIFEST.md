# File Refactoring Manifest

## PROJECT: Reduce Oversized Step Files

**Objective:** Refactor 32 step files exceeding 200 lines by extracting templates, menus, and data structures.

**Status:** IN PROGRESS
**Progress:** 1/32 files completed (step-v-08b-generate.md)

---

## REFACTORING STRATEGY

### Phase 1: Extract Core Templates (COMPLETED)
- ✅ comprehensive-validation-report-template.md (report structure)
- ✅ merge-strategies-matrix.md (strategy options & comparison table)
- ✅ step-menu-options.md (menu routing & options)
- ✅ dimensional-report-sections.md (dimensional analysis format)

### Phase 2: Refactor Critical Files (> 250 lines)
Progress: 1/5 completed

1. ✅ step-v-08b-generate.md (374 → 212 lines)
   - Extracted: Report template reference
   - Saved: 162 lines

2. ⏳ step-c-06b-merge-strategy.md (362 lines)
   - Target: Extract merge strategies matrix
   - Goal: Reduce to ~150 lines

3. ⏳ step-c-05d-finalize.md (348 lines)
   - Target: Extract checklist & templates
   - Goal: Reduce to ~140 lines

4. ⏳ step-v-04c-report.md (327 lines)
   - Target: Extract report template
   - Goal: Reduce to ~120 lines

5. ⏳ step-c-08b-maintenance.md (315 lines)
   - Target: Extract checklist & procedures
   - Goal: Reduce to ~110 lines

### Phase 3: Refactor Warning Files (200-250 lines)
Progress: 0/23 completed

Target: Reduce each from 200-250 lines to <150 lines
Strategy: Extract menus, checklists, templates similar to critical files

**Files:**
- step-e-02c-apply.md (303)
- step-v-05c-report.md (295)
- step-e-05c-compare.md (292)
- step-e-02b-evaluate.md (290)
- step-c-06a-select-posts.md (287)
- step-00-menu.md (278)
- step-e-08b-compare.md (273)
- step-c-05c-apply-edits.md (273)
- step-e-01c-apply-edits.md (266)
- step-v-06c-report.md (261)
- step-e-03c-compare.md (257)
- step-v-03c-report.md (256)
- step-e-07b-view.md (254)
- step-v-07c-report.md (253)
- step-c-05b-improvements.md (248)
- step-yolo-01-input.md (244)
- step-e-03b-generate.md (235)
- step-v-02c-report.md (232)
- step-e-04b-recalculate.md (232)
- step-v-00-menu.md (231)
- step-01b-continue.md (222)
- step-c-04c-actions.md (219)
- step-yolo-06-summary.md (215)

---

## EXTRACTION TEMPLATES CREATED

### 1. comprehensive-validation-report-template.md
**Purpose:** Standardize validation report structure
**Size:** 110 lines
**Contains:** Report sections, dimensional breakdown format, data structure
**Used by:** All V-XX report steps (v-01c, v-02c, v-03c, v-04c, v-05c, v-06c, v-07c, v-08b)

### 2. merge-strategies-matrix.md
**Purpose:** Document merge strategy options with comparison table
**Size:** 160 lines
**Contains:** 6 merge strategies with descriptions, comparison table, selection guide
**Used by:** step-c-06b-merge-strategy.md (and similar merge-related steps)

### 3. step-menu-options.md
**Purpose:** Standardize menu presentation format
**Size:** 70 lines
**Contains:** Menu patterns, data format, routing logic
**Used by:** All menu-displaying steps (step-00-menu, mode-v-00-menu, mode-c-00-menu, etc.)

### 4. dimensional-report-sections.md
**Purpose:** Template for dimensional analysis sections
**Size:** 140 lines
**Contains:** Section format, status indicators, dimension templates, usage guide
**Used by:** All dimensional analysis steps

---

## REFACTORING CHECKLIST

### Completed Refactoring ✅
- [x] step-v-08b-generate.md - 374 lines → 212 lines

### In Progress ⏳
- [ ] step-c-06b-merge-strategy.md (362 lines)
- [ ] step-c-05d-finalize.md (348 lines)
- [ ] step-v-04c-report.md (327 lines)
- [ ] step-c-08b-maintenance.md (315 lines)

### Planned 🔲
- [ ] step-e-02c-apply.md (303 lines)
- [ ] step-v-05c-report.md (295 lines)
- [ ] step-e-05c-compare.md (292 lines)
- [ ] step-e-02b-evaluate.md (290 lines)
- [ ] step-c-06a-select-posts.md (287 lines)
- [ ] step-00-menu.md (278 lines)
- [ ] step-e-08b-compare.md (273 lines)
- [ ] step-c-05c-apply-edits.md (273 lines)
- [ ] step-e-01c-apply-edits.md (266 lines)
- [ ] step-v-06c-report.md (261 lines)
- [ ] step-e-03c-compare.md (257 lines)
- [ ] step-v-03c-report.md (256 lines)
- [ ] step-e-07b-view.md (254 lines)
- [ ] step-v-07c-report.md (253 lines)
- [ ] step-c-05b-improvements.md (248 lines)
- [ ] step-yolo-01-input.md (244 lines)
- [ ] step-e-03b-generate.md (235 lines)
- [ ] step-v-02c-report.md (232 lines)
- [ ] step-e-04b-recalculate.md (232 lines)
- [ ] step-v-00-menu.md (231 lines)
- [ ] step-01b-continue.md (222 lines)
- [ ] step-c-04c-actions.md (219 lines)
- [ ] step-yolo-06-summary.md (215 lines)

---

## REFACTORING PATTERNS

### Pattern 1: Report Files (V-XX steps)
**Files:** All steps ending in `-report.md` or `-generate.md`
**Extraction:**
1. Remove full report template → reference `comprehensive-validation-report-template.md`
2. Remove dimensional sections → reference `dimensional-report-sections.md`
3. Remove critical issues list → extract to data/critical-issues-{step_id}.json
4. Remove success metrics → extract to data/success-metrics-{step_id}.json
5. Keep only: report generation logic, menu options, saved data structure

**Typical Reduction:** 300+ lines → 120-150 lines

### Pattern 2: Menu Files (00-menu steps)
**Files:** step-00-menu.md, mode-v-00-menu.md, mode-c-00-menu.md, mode-e-00-menu.md
**Extraction:**
1. Remove full menu options → reference `step-menu-options.md`
2. Remove detailed descriptions → keep brief summary
3. Remove help text → extract to data/help-{step_id}.md
4. Keep only: menu display, routing logic, execution rules

**Typical Reduction:** 250+ lines → 80-120 lines

### Pattern 3: Strategy/Comparison Files
**Files:** step-*-merge-strategy.md, step-*-compare.md
**Extraction:**
1. Remove comparison tables → extract to data/comparison-matrices/
2. Remove option descriptions → reference comparison matrix
3. Remove preview examples → extract to data/previews/
4. Keep only: strategy selection logic, user interaction flow

**Typical Reduction:** 280+ lines → 100-140 lines

### Pattern 4: Improvement/Edit Files
**Files:** step-*-improvements.md, step-*-apply.md, step-*-apply-edits.md
**Extraction:**
1. Remove improvement templates → extract to data/checklist-templates/
2. Remove example improvements → extract to data/examples/
3. Remove edit guides → extract to data/edit-guides/
4. Keep only: selection logic, execution instructions

**Typical Reduction:** 240+ lines → 100-130 lines

---

## BENEFITS OF REFACTORING

### Readability
- Reduced file sizes = easier to understand core logic
- Clear references to templates = better navigation
- Templates serve as source of truth

### Maintainability
- Change template once, affects all uses
- Easier to locate and update common patterns
- Reduced duplication across similar steps

### Scalability
- Adding new report type = reference template
- Adding new merge strategy = add to matrix
- Adding new menu = use menu template

### Performance
- Faster file loading (smaller files)
- Easier searching within codebase
- Better IDE performance

---

## NEXT STEPS

1. Complete refactoring of remaining 4 critical files
2. Refactor 23 warning files (200-250 lines)
3. Verify all references work correctly
4. Test workflow with refactored files
5. Update INDEX.md with new data structure references
6. Archive old versions in `/_archived/oversized-originals/`

---

## FINAL METRICS (ESTIMATED)

**Total files:** 32
**Total lines before:** ~8,500 lines
**Total lines after:** ~5,200 lines
**Lines saved:** ~3,300 lines (38.8%)
**Templates created:** 4
**Data files created:** ~30-40
**Reduction per file:** 160-180 lines average

**Result:** More maintainable, scalable, readable codebase with shared templates
