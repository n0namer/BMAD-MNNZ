# File Structure & Size Validation Report

**Validation Date:** 2026-01-30
**Target Workflow:** D:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\idea-to-post-pipeline
**Validator:** BMAD Workflow Validator Agent

---

## File Structure & Size

### Folder Structure Assessment

```
idea-to-post-pipeline/
├── workflow.md                           (Main workflow file)
├── step-00-menu.md                       (Main menu)
├── step-01-init.md                       (Initialization)
├── step-01b-continue.md                  (Session continuation)
├── 00-START-HERE.md                      (Documentation)
├── CONVERSION-SUMMARY.md                 (Documentation)
├── CLEANUP-SUMMARY.md                    (Documentation)
├── COMPLETION-REPORT.txt                 (Documentation)
├── DOCUMENTATION_ENHANCEMENT_SUMMARY.md  (Documentation)
├── VERIFICATION-REPORT.txt               (Documentation)
├── validation-guide.md                   (Documentation)
├── .bmad_workflow_assessment.md          (Assessment)
│
├── steps-c/                              (CREATE mode - 27 files)
│   ├── c-00-menu.md
│   ├── c-01-add-idea.md
│   ├── c-02a-load-ideas.md ... c-02d-results.md
│   ├── c-03a-select-idea.md ... c-03e-finalize.md
│   ├── c-04a-search-criteria.md ... c-04c-actions.md
│   ├── c-05a-select-post.md ... c-05d-finalize.md
│   ├── c-06a-select-posts.md ... c-06d-save.md
│   ├── c-07a-dashboard.md ... c-07c-recommendations.md
│   └── c-08a-backup.md, c-08b-maintenance.md
│
├── steps-e/                              (EDIT mode - 46 files)
│   ├── e-00-menu.md
│   ├── e-01a-select-posts.md ... e-01c.md (+ duplicates)
│   ├── e-02a.md ... e-02c.md
│   ├── e-03a-select-post.md ... e-03c.md
│   ├── e-04a.md ... e-04c.md
│   ├── e-05a.md ... e-05c.md
│   ├── e-06a.md ... e-06c.md
│   ├── e-07a-load-history.md ... e-07c.md
│   └── e-08a-select.md ... e-08c.md
│
├── steps-v/                              (VALIDATE mode - 24 files)
│   ├── v-00-menu.md
│   ├── v-01a-load.md, v-01b-checks.md, v-01c-report.md
│   ├── v-02a-load.md ... v-02c-report.md
│   ├── v-03a-load.md ... v-03c-report.md
│   ├── v-04a-load.md ... v-04c-report.md
│   ├── v-05a-load.md ... v-05c-report.md
│   ├── v-06a-load.md ... v-06c-report.md
│   ├── v-07a-load.md ... v-07c-report.md
│   └── v-08a-compile.md, v-08b-generate.md
│
├── steps-yolo/                           (YOLO mode - 7 files)
│   ├── yolo-01-input.md
│   ├── yolo-01b-ideas-input.md
│   ├── yolo-02-parallel-execute.md
│   ├── yolo-03-self-check.md
│   ├── yolo-04-auto-improve.md
│   ├── yolo-05-variants.md
│   └── yolo-06-summary.md
│
├── subprocesses/                         (7 subprocess files + README)
│   ├── README.md
│   ├── subprocess-parallel-research.md
│   ├── subprocess-parallel-write.md
│   ├── subprocess-batch-validation.md
│   ├── subprocess-auto-fix.md
│   ├── subprocess-variant-generation.md
│   ├── subprocess-parallel-execute.md
│   └── subprocess-metrics-aggregation.md
│
├── data/                                 (Reference data)
│   ├── csv-templates/                    (5 CSV templates)
│   ├── checklist-templates/              (5 checklist files)
│   ├── report-templates/                 (2 report templates)
│   ├── comparison-matrices/              (1 file)
│   ├── menu-routing/                     (1 file)
│   └── reference/                        (4 reference files)
│
└── templates/                            (Mirror of data/ templates)
    ├── csv/                              (5 CSV templates)
    ├── checklists/                       (5 checklist files)
    ├── reports/                          (2 report templates)
    ├── comparison/                       (1 file)
    └── menu/                             (1 file)
```

**Total Directories:** 19
**Total Files:** ~150+ (including duplicates between data/ and templates/)

---

### Required Files Check

| Required Component | Status | Location(s) |
|-------------------|--------|-------------|
| workflow.md | YES | Root folder |
| steps folder(s) | YES | steps-c/, steps-e/, steps-v/, steps-yolo/ |
| data folder | YES | data/ (with 6 subfolders) |
| templates folder | YES | templates/ (with 5 subfolders) |

**Additional Observations:**
- Root-level step files present: step-00-menu.md, step-01-init.md, step-01b-continue.md
- Subprocess optimization folder present with 7 specialized files
- Reference documentation present (timing-sla.md, faq.md, etc.)

---

### File Size Analysis

| File | Lines | Status |
|------|-------|--------|
| **ROOT FILES** | | |
| workflow.md | 226 | WARNING (200-300) |
| step-00-menu.md | 274 | WARNING (200-300) |
| step-01-init.md | 208 | WARNING (200-300) |
| step-01b-continue.md | 227 | WARNING (200-300) |
| | | |
| **CREATE MODE (steps-c/)** | | |
| c-00-menu.md | 208 | WARNING (200-300) |
| c-01-add-idea.md | 134 | GOOD |
| c-02a-load-ideas.md | 73 | GOOD |
| c-02b-select-idea.md | 87 | GOOD |
| c-02c-research.md | 144 | GOOD |
| c-02d-results.md | 125 | GOOD |
| c-03a-select-idea.md | 92 | GOOD |
| c-03b-select-angle.md | 113 | GOOD |
| c-03c-draft.md | 185 | GOOD |
| c-03d-variants.md | 159 | GOOD |
| c-03e-finalize.md | 173 | GOOD |
| c-04a-search-criteria.md | 156 | GOOD |
| c-04b-results.md | 160 | GOOD |
| c-04c-actions.md | 353 | EXCEEDS LIMIT |
| c-05a-select-post.md | 242 | WARNING (200-300) |
| c-05b-improvements.md | 325 | EXCEEDS LIMIT |
| c-05c-apply-edits.md | 282 | WARNING (200-300) |
| c-05d-finalize.md | 538 | EXCEEDS LIMIT |
| c-06a-select-posts.md | 400 | EXCEEDS LIMIT |
| c-06b-merge-strategy.md | 278 | WARNING (200-300) |
| c-06c-generate.md | 181 | GOOD |
| c-06d-save.md | 177 | GOOD |
| c-07a-dashboard.md | 173 | GOOD |
| c-07b-deepdive.md | 172 | GOOD |
| c-07c-recommendations.md | 222 | WARNING (200-300) |
| c-08a-backup.md | 219 | WARNING (200-300) |
| c-08b-maintenance.md | 320 | EXCEEDS LIMIT |
| | | |
| **EDIT MODE (steps-e/)** | | |
| e-00-menu.md | 231 | WARNING (200-300) |
| (46 total files - many are short stubs) | ~50-100 each | GOOD |
| | | |
| **VALIDATE MODE (steps-v/)** | | |
| v-00-menu.md | 254 | WARNING (200-300) |
| (24 total files) | ~50-150 each | MOSTLY GOOD |
| | | |
| **YOLO MODE (steps-yolo/)** | | |
| yolo-01-input.md | 278 | WARNING (200-300) |
| yolo-01b-ideas-input.md | ~195 | GOOD |
| yolo-02-parallel-execute.md | 249 | WARNING (200-300) |
| yolo-03-self-check.md | ~175 | GOOD |
| yolo-04-auto-improve.md | ~100 | GOOD |
| yolo-05-variants.md | ~120 | GOOD |
| yolo-06-summary.md | ~220 | WARNING (200-300) |
| | | |
| **SUBPROCESSES** | | |
| README.md | 175 | GOOD |
| subprocess-parallel-research.md | 307 | EXCEEDS LIMIT |
| subprocess-parallel-write.md | 375 | EXCEEDS LIMIT |
| subprocess-batch-validation.md | 441 | EXCEEDS LIMIT |
| subprocess-auto-fix.md | 444 | EXCEEDS LIMIT |
| subprocess-variant-generation.md | 458 | EXCEEDS LIMIT |
| subprocess-parallel-execute.md | 428 | EXCEEDS LIMIT |
| subprocess-metrics-aggregation.md | 569 | EXCEEDS LIMIT |

---

### Issues Found

#### CRITICAL Issues (Line Count > 300)

1. **c-04c-actions.md** (353 lines) - POST ACTIONS step exceeds limit
   - Contains duplicated menu handling logic
   - Recommendation: Split into separate files or consolidate logic

2. **c-05b-improvements.md** (325 lines) - IMPROVEMENTS step exceeds limit
   - Contains detailed improvement options repeated twice
   - Recommendation: Remove duplication, extract to templates

3. **c-05d-finalize.md** (538 lines) - FINALIZE step significantly exceeds limit
   - Contains extensive menu handling logic duplicated
   - Recommendation: Split save options into separate file

4. **c-06a-select-posts.md** (400 lines) - SELECT POSTS exceeds limit
   - Contains filter/sort logic duplicated
   - Recommendation: Extract filter logic to shared template

5. **c-08b-maintenance.md** (320 lines) - MAINTENANCE step exceeds limit
   - Contains full diagnostic workflow
   - Recommendation: Split into maintenance-diagnostics.md and maintenance-optimize.md

6. **ALL SUBPROCESS FILES** (307-569 lines) - All 7 subprocess files exceed limit
   - subprocess-parallel-research.md: 307 lines
   - subprocess-parallel-write.md: 375 lines
   - subprocess-batch-validation.md: 441 lines
   - subprocess-auto-fix.md: 444 lines
   - subprocess-variant-generation.md: 458 lines
   - subprocess-parallel-execute.md: 428 lines
   - subprocess-metrics-aggregation.md: 569 lines
   - **Note:** These are optimization specifications, not step files - may be acceptable

#### WARNING Issues (Line Count 200-300)

1. **workflow.md** (226 lines) - Approaching limit but acceptable for main workflow file
2. **step-00-menu.md** (274 lines) - Contains all 4 mode menus
3. **step-01-init.md** (208 lines) - Welcome + continuation logic
4. **step-01b-continue.md** (227 lines) - Session resume logic
5. **c-00-menu.md** (208 lines) - CREATE mode menu
6. **c-05a-select-post.md** (242 lines) - Post selection with filters
7. **c-05c-apply-edits.md** (282 lines) - Edit application workflow
8. **c-06b-merge-strategy.md** (278 lines) - Merge strategy selection
9. **c-07c-recommendations.md** (222 lines) - Analytics recommendations
10. **c-08a-backup.md** (219 lines) - Backup workflow
11. **e-00-menu.md** (231 lines) - EDIT mode menu
12. **v-00-menu.md** (254 lines) - VALIDATE mode menu
13. **yolo-01-input.md** (278 lines) - YOLO input specification
14. **yolo-02-parallel-execute.md** (249 lines) - Parallel execution

#### Structural Issues

1. **Duplicate folders:** Both `data/` and `templates/` contain identical CSV and checklist files
   - Recommendation: Remove duplication, keep only one location

2. **Naming inconsistency:** steps-e/ contains both short names (e-01a.md) and long names (e-01a-select-posts.md)
   - Recommendation: Standardize naming convention

3. **Orphan files in root:** Russian-named documentation files should be moved or removed
   - "bmad napisal mne bolshe 80 dokumentov..." (not valid workflow file)
   - "ty ne dal.md" (not valid workflow file)

---

### Summary Statistics

| Category | Count | Status |
|----------|-------|--------|
| Files < 200 lines | ~120 | GOOD |
| Files 200-300 lines | ~14 | WARNING |
| Files > 300 lines | ~12 | EXCEEDS LIMIT |
| Total Files | ~150 | |

---

### Status: WARNING - REQUIRES ATTENTION

**Validation Result:** The workflow structure is complete and well-organized, but there are significant file size violations that need addressing.

**Action Items:**

1. **HIGH PRIORITY:** Refactor 5 step files exceeding 300 lines (c-04c, c-05b, c-05d, c-06a, c-08b)
2. **MEDIUM PRIORITY:** Consider splitting subprocess files or documenting exception rationale
3. **LOW PRIORITY:** Clean up duplicate data/templates folders
4. **LOW PRIORITY:** Remove orphan Russian-named files from root

---

*Report generated by BMAD Workflow Validator Agent*
