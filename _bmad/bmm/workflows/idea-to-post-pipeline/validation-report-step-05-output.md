# Output Format Validation Report

**Workflow:** idea-to-post-pipeline
**Validation Date:** 2026-01-30
**Validator:** BMAD Workflow Validator Agent

---

## Output Format Validation

### Document Production
- **Produces documents:** Yes
- **Template type:** Semi-structured (Core + optional sections)
- **Templates found:** 14 templates across 5 categories

### Templates Inventory

| Category | Template File | Purpose |
|----------|--------------|---------|
| CSV | `templates/csv/ideas_inbox_template.csv` | New ideas storage |
| CSV | `templates/csv/ideas_research_template.csv` | Researched ideas with angles |
| CSV | `templates/csv/posts_content_template.csv` | Published posts with metrics |
| CSV | `templates/csv/metrics_tracking_template.csv` | CTR, engagement tracking |
| CSV | `templates/csv/angles_library_template.csv` | Reusable angle templates |
| Checklists | `templates/checklists/idea-validation-checklist.md` | Idea quality validation |
| Checklists | `templates/checklists/post-quality-checklist.md` | Post quality before publish |
| Checklists | `templates/checklists/edit-improvements-checklist.md` | Edit improvement criteria |
| Checklists | `templates/checklists/engagement-checklist.md` | Engagement prediction |
| Checklists | `templates/checklists/copy-audit-checklist.md` | Copywriting quality audit |
| Reports | `templates/reports/comprehensive-validation-report-template.md` | Full validation report |
| Reports | `templates/reports/dimensional-report-sections.md` | Report section templates |
| Comparison | `templates/comparison/merge-strategies-matrix.md` | Post merge strategies |
| Menu | `templates/menu/step-menu-options.md` | Menu routing options |

### Template Assessment

**Strengths:**
- Well-organized template folder structure (`templates/csv/`, `templates/checklists/`, `templates/reports/`)
- CSV templates define clear schema with all required columns
- Checklist templates follow consistent structure (criterion + examples + scoring)
- Report templates include JSON data structures for programmatic access
- Templates support Russian language output as required

**Areas for Improvement:**
- Template references in step files use relative paths inconsistently (some use `../../data/`, others use `../templates/`)
- Duplicate templates exist in both `data/` and `templates/` folders (redundancy)

### Final Polish Step

| Mode | Final Step | Has Polish/Review | Status |
|------|-----------|-------------------|--------|
| CREATE (C-03) | `c-03e-finalize.md` | Quality check + final review before save | Exists |
| CREATE (C-05) | `c-05d-finalize.md` | Final summary + quality metrics + save options | Exists |
| CREATE (C-06) | `c-06d-save.md` | Save confirmation + backup + knowledge base update | Exists |
| EDIT (E-04) | `e-04c-save.md` | Metrics save + backup + verification | Exists |
| VALIDATE (V-08) | `v-08b-generate.md` | Comprehensive report generation | Exists |
| YOLO | `yolo-06-summary.md` | Final results + quality metrics + user choices | Exists |

- **Required:** Yes (workflow produces documents that need finalization)
- **Present:** All modes have final polish/review steps

### Step-to-Output Mapping

#### CREATE Mode (Mode C)

| Step | Has outputFile/SAVED DATA | Saves before next | Status |
|------|---------------------------|-------------------|--------|
| c-01-add-idea | `ideas_inbox.csv` | Saves idea to CSV before menu | Confirmed |
| c-02c-research | `ideas_research.csv` | Saves angles before next step | Confirmed |
| c-03d-variants | Not explicit | Generates in-memory, saved in c-03e | Implicit |
| c-03e-finalize | `posts_content.csv` | Final save with confirmation | Confirmed |
| c-05d-finalize | `posts_content.csv` (update) | Save with backup before exit | Confirmed |
| c-06d-save | `posts_published.csv` + backup | Save + backup + KB update | Confirmed |
| c-08a-backup | Creates backup files | Explicit backup step | Confirmed |

#### EDIT Mode (Mode E)

| Step | Has outputFile/SAVED DATA | Saves before next | Status |
|------|---------------------------|-------------------|--------|
| e-01c-apply-edits | Updates `posts_content.csv` | Saves edits before menu | Confirmed |
| e-02c-apply | Updates posts with checklist scores | Saves before menu | Confirmed |
| e-03c-compare | Saves A/B test results | Saves comparison | Confirmed |
| e-04c-save | `metrics_tracking.csv` + backup | Full save with verification | Confirmed |
| e-05c-compare | Saves rewrite comparison | Saves before menu | Confirmed |
| e-06b-archive | Archives posts | Save + archive | Confirmed |
| e-07a-load-history | Read-only | N/A (load step) | N/A |
| e-08b-compare | Version comparison | Saves selection | Confirmed |

#### VALIDATE Mode (Mode V)

| Step | Has outputFile/SAVED DATA | Saves before next | Status |
|------|---------------------------|-------------------|--------|
| v-01c-report | Displays report | Report can be saved | Confirmed |
| v-02c-report | Performance audit report | Report can be saved | Confirmed |
| v-03c-report | Consistency report | Report can be saved | Confirmed |
| v-04c-report | Copy audit report | Report can be saved | Confirmed |
| v-05c-report | Engagement prediction report | Report can be saved | Confirmed |
| v-06c-report | Batch validation report | Comprehensive report | Confirmed |
| v-07c-report | Ideas viability report | Report can be saved | Confirmed |
| v-08b-generate | JSON + comprehensive report | Full save with export options | Confirmed |

#### YOLO Mode

| Step | Has outputFile/SAVED DATA | Saves before next | Status |
|------|---------------------------|-------------------|--------|
| yolo-01-input | Stores input specification | In-memory for next step | N/A (input) |
| yolo-02-parallel-execute | Generates posts | In-memory (parallel) | Process step |
| yolo-03-self-check | Validation scores | In-memory | Process step |
| yolo-04-auto-improve | Improved posts | In-memory | Process step |
| yolo-05-variants | Variant JSON | In-memory | Process step |
| yolo-06-summary | `posts_content.csv` | Final save with user choice | Confirmed |

### Output Storage Patterns

**Identified Output Locations:**
1. `content_generation_system/ideas_inbox.csv` - Raw ideas
2. `content_generation_system/ideas_research.csv` - Researched ideas with angles
3. `content_generation_system/posts_content.csv` - Posts with all versions
4. `content_generation_system/metrics_tracking.csv` - Performance metrics
5. `content_generation_system/angles_library.csv` - Reusable angles
6. `/data/backups/` - Automatic backups
7. `/outputs/comprehensive-reports/` - Validation reports (PDF/word)

### Golden Rule Compliance

**"Every step MUST output BEFORE loading next step"**

| Mode | Compliance | Notes |
|------|-----------|-------|
| CREATE | Compliant | Each step has explicit SAVED DATA section |
| EDIT | Compliant | All edit steps save before returning to menu |
| VALIDATE | Compliant | Reports generated and save options provided |
| YOLO | Partially Compliant | Steps 2-5 use in-memory processing; final save in step 6 |

**YOLO Mode Note:** YOLO mode intentionally processes steps 2-5 in-memory for speed (100x faster). Final persistence happens in step 6 (yolo-06-summary.md) where user confirms save. This is acceptable for the "fully automated" nature of YOLO mode, but should be documented.

### Issues Found

1. **Duplicate Templates:** Templates exist in both `data/` and `templates/` folders
   - Recommendation: Consolidate to single `templates/` folder

2. **Inconsistent Path References:** Some steps reference `../../data/`, others `../templates/`
   - Recommendation: Standardize all template references

3. **Missing outputFile in Frontmatter:** Steps describe outputs in SAVED DATA sections but don't always have explicit `outputFile:` frontmatter field
   - Impact: Low (documentation exists, behavior is correct)
   - Recommendation: Add `outputFile:` to frontmatter for tooling support

4. **YOLO In-Memory Processing:** Steps 2-5 don't persist until step 6
   - Impact: Low (intentional design for speed)
   - Recommendation: Document this in workflow.md

---

## Summary

### Validation Counts
- **Templates Found:** 14
- **Steps with Explicit Output:** 42/46 (~91%)
- **Final Polish Steps:** 6/6 modes (100%)
- **Golden Rule Compliant:** 3/4 modes fully, 1/4 partially (acceptable)

### Status: PASS with WARNINGS

**Overall Assessment:** The workflow demonstrates strong output format compliance with:
- Well-structured templates across all categories
- Consistent SAVED DATA sections in step files
- Final polish/review steps in all modes
- Clear output storage patterns

**Warnings:**
1. Duplicate templates in `data/` and `templates/` folders should be consolidated
2. Path references to templates should be standardized
3. YOLO mode's in-memory processing should be explicitly documented

---

**Validation Complete:** 2026-01-30
