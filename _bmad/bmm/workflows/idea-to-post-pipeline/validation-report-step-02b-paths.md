# Critical Path Violations Report

**Workflow:** idea-to-post-pipeline
**Validation Date:** 2026-01-30
**Validator:** BMAD Workflow Validator Agent

---

## Config Variables (Exceptions)

The following configuration variables are loaded from `_bmad/bmb/config.yaml` and are legitimate path references:

| Variable | Value | Status |
|----------|-------|--------|
| `project_name` | "BMAD-MNNZ" | Template variable |
| `output_folder` | "_bmad-output/bmb-creations/workflows/" | Output path (SKIP validation) |
| `communication_language` | "Russian" | Non-path |
| `document_output_language` | "Russian" | Non-path |

**Note:** Output paths using config variables like `{output_folder}` are intentionally SKIPPED from dead link validation as they are created at runtime.

---

## Content Path Violations

### CRITICAL: workflow.md References Non-Existent Directory

| File | Line | Issue | Details |
|------|------|-------|---------|
| `workflow.md` | 185 | Dead link | `./steps/step-01-init.md` - `steps/` directory does not exist. Actual file: `./step-01-init.md` |
| `workflow.md` | 225 | Dead link | `./steps/step-01-init.md` - same issue |

### CRITICAL: Mode Menu Files Reference Non-Existent Subdirectories

Files in `steps-c/`, `steps-e/`, `steps-v/` reference `./mode-X-NN/step-X-NN-*.md` pattern but actual structure is flat.

| File | Line | Issue | Details |
|------|------|-------|---------|
| `step-00-menu.md` | 7 | Dead link | `./mode-yolo/step-yolo-01-input.md` - should be `./steps-yolo/yolo-01-input.md` |
| `step-00-menu.md` | 233 | Dead link | Same as above |
| `steps-c/c-00-menu.md` | 126 | Dead link | `./mode-c-01/step-c-01-add-idea.md` - should be `./c-01-add-idea.md` |
| `steps-c/c-00-menu.md` | 132 | Dead link | `./mode-c-02/step-c-02a-load-ideas.md` - should be `./c-02a-load-ideas.md` |
| `steps-c/c-00-menu.md` | 138 | Dead link | `./mode-c-03/step-c-03a-select-idea.md` - should be `./c-03a-select-idea.md` |
| `steps-c/c-00-menu.md` | 144 | Dead link | `./mode-c-04/step-c-04-search.md` - should be `./c-04a-search-criteria.md` |
| `steps-c/c-00-menu.md` | 150 | Dead link | `./mode-c-05/step-c-05a-select-post.md` - should be `./c-05a-select-post.md` |
| `steps-c/c-00-menu.md` | 156 | Dead link | `./mode-c-06/step-c-06a-select-posts.md` - should be `./c-06a-select-posts.md` |
| `steps-c/c-00-menu.md` | 162 | Dead link | `./mode-c-07/step-c-07a-dashboard.md` - should be `./c-07a-dashboard.md` |
| `steps-c/c-00-menu.md` | 168 | Dead link | `./mode-c-08/step-c-08a-backup.md` - should be `./c-08a-backup.md` |
| `steps-e/e-00-menu.md` | 138 | Dead link | `./mode-e-01/step-e-01a-select-posts.md` - should be `./e-01a-select-posts.md` |
| `steps-e/e-00-menu.md` | 144 | Dead link | `./mode-e-02/step-e-02a-load-checklist.md` - should be `./e-02a-load-checklist.md` |
| `steps-e/e-00-menu.md` | 150 | Dead link | `./mode-e-03/step-e-03a-select-post.md` - should be `./e-03a-select-post.md` |
| `steps-e/e-00-menu.md` | 156 | Dead link | `./mode-e-04/step-e-04a-load-posts.md` - should be `./e-04a-load-posts.md` |
| `steps-e/e-00-menu.md` | 162 | Dead link | `./mode-e-05/step-e-05a-identify.md` - should be `./e-05a-identify.md` |
| `steps-e/e-00-menu.md` | 168 | Dead link | `./mode-e-06/step-e-06a-select.md` - should be `./e-06a-select.md` |
| `steps-e/e-00-menu.md` | 174 | Dead link | `./mode-e-07/step-e-07a-load-history.md` - should be `./e-07a-load-history.md` |
| `steps-e/e-00-menu.md` | 180 | Dead link | `./mode-e-08/step-e-08a-select.md` - should be `./e-08a-select.md` |
| `steps-v/v-00-menu.md` | 116 | Dead link | `./mode-v-01/step-v-01a-load.md` - should be `./v-01a-load.md` |
| `steps-v/v-00-menu.md` | 122 | Dead link | `./mode-v-02/step-v-02a-load.md` - should be `./v-02a-load.md` |
| `steps-v/v-00-menu.md` | 128 | Dead link | `./mode-v-03/step-v-03a-load.md` - should be `./v-03a-load.md` |
| `steps-v/v-00-menu.md` | 134 | Dead link | `./mode-v-04/step-v-04a-load.md` - should be `./v-04a-load.md` |
| `steps-v/v-00-menu.md` | 140 | Dead link | `./mode-v-05/step-v-05a-load.md` - should be `./v-05a-load.md` |
| `steps-v/v-00-menu.md` | 146 | Dead link | `./mode-v-06/step-v-06a-load.md` - should be `./v-06a-load.md` |
| `steps-v/v-00-menu.md` | 152 | Dead link | `./mode-v-07/step-v-07a-load.md` - should be `./v-07a-load.md` |
| `steps-v/v-00-menu.md` | 158 | Dead link | `./mode-v-08/step-v-08a-compile.md` - should be `./v-08a-compile.md` |

### HIGH: v-08a-compile.md References Non-Existent JSON Sources

| File | Line | Issue | Details |
|------|------|-------|---------|
| `steps-v/v-08a-compile.md` | 41 | Dead link | `./mode-v-01/validation-results.json` - directory doesn't exist |
| `steps-v/v-08a-compile.md` | 46 | Dead link | `./mode-v-02/validation-results.json` - directory doesn't exist |
| `steps-v/v-08a-compile.md` | 51 | Dead link | `./mode-v-03/validation-results.json` - directory doesn't exist |
| `steps-v/v-08a-compile.md` | 56 | Dead link | `./mode-v-04/validation-results.json` - directory doesn't exist |
| `steps-v/v-08a-compile.md` | 61 | Dead link | `./mode-v-05/validation-results.json` - directory doesn't exist |
| `steps-v/v-08a-compile.md` | 66 | Dead link | `./mode-v-06/validation-results.json` - directory doesn't exist |
| `steps-v/v-08a-compile.md` | 71 | Dead link | `./mode-v-07/validation-results.json` - directory doesn't exist |

### MEDIUM: Cross-Mode Navigation Dead Link

| File | Line | Issue | Details |
|------|------|-------|---------|
| `steps-v/v-01c-report.md` | 174 | Dead link | `../../mode-c/mode-c-05/step-c-05a-select-post.md` - incorrect path structure |

---

## Dead Links Summary

### Actual Directory Structure vs Referenced Structure

**Actual Structure:**
```
idea-to-post-pipeline/
├── workflow.md
├── step-00-menu.md
├── step-01-init.md
├── step-01b-continue.md
├── steps-c/
│   ├── c-00-menu.md
│   ├── c-01-add-idea.md
│   ├── c-02a-load-ideas.md
│   └── ... (flat structure)
├── steps-e/
│   ├── e-00-menu.md
│   └── ... (flat structure)
├── steps-v/
│   ├── v-00-menu.md
│   └── ... (flat structure)
└── steps-yolo/
    ├── yolo-01-input.md
    └── ... (flat structure)
```

**Referenced Structure (Incorrect):**
```
idea-to-post-pipeline/
├── workflow.md (references ./steps/step-01-init.md)
├── steps/                    <- DOES NOT EXIST
│   └── step-01-init.md
├── mode-yolo/                <- DOES NOT EXIST
│   └── step-yolo-01-input.md
├── steps-c/
│   ├── mode-c-01/            <- DOES NOT EXIST
│   │   └── step-c-01-add-idea.md
│   └── ...
└── ...
```

### Dead Link Count by File

| File | Dead Links | Severity |
|------|------------|----------|
| `workflow.md` | 2 | CRITICAL |
| `step-00-menu.md` | 2 | CRITICAL |
| `steps-c/c-00-menu.md` | 8 | CRITICAL |
| `steps-e/e-00-menu.md` | 8 | CRITICAL |
| `steps-v/v-00-menu.md` | 8 | CRITICAL |
| `steps-v/v-08a-compile.md` | 7 | HIGH |
| `steps-v/v-01c-report.md` | 1 | MEDIUM |
| **TOTAL** | **36** | |

---

## Module Awareness

### Module Context Issue

| File | Line | Issue | Details |
|------|------|-------|---------|
| `workflow.md` | 178 | Module mismatch | This workflow is in `_bmad/bmm/` but references `_bmad/bmb/config.yaml` |

**Analysis:** The workflow is located in the BMM (Method) module at `_bmad/bmm/workflows/idea-to-post-pipeline/` but loads configuration from BMB (Blueprints) module at `_bmad/bmb/config.yaml`.

**Recommendation:** Either:
1. Move workflow to `_bmad/bmb/workflows/` if it's a blueprint workflow
2. Create a BMM-specific config at `_bmad/bmm/config.yaml`
3. Document this cross-module dependency as intentional

**Severity:** MEDIUM - Cross-module dependency may cause issues if modules are used independently.

---

## Summary

| Severity | Count | Description |
|----------|-------|-------------|
| CRITICAL | 28 | Dead links in main workflow and menu files - workflow cannot navigate |
| HIGH | 7 | Dead links to validation result JSON files |
| MEDIUM | 2 | Cross-mode navigation issues and module awareness |
| **TOTAL** | **37** | |

---

## Status: FAIL

**The workflow has 37 path violations that will prevent proper execution.**

### Root Cause

The step file references use an outdated directory structure pattern (`./mode-X-NN/step-X-NN-*.md`) while the actual files are organized in a flat structure within mode-specific directories (`./steps-X/X-NN-*.md`).

### Required Fixes

1. **workflow.md**: Change `./steps/step-01-init.md` to `./step-01-init.md`
2. **step-00-menu.md**: Change `./mode-yolo/step-yolo-01-input.md` to `./steps-yolo/yolo-01-input.md`
3. **All mode menu files**: Update navigation paths to use flat structure
   - Pattern: `./mode-c-01/step-c-01-add-idea.md` -> `./c-01-add-idea.md`
4. **v-08a-compile.md**: Update JSON source paths to valid locations
5. **v-01c-report.md**: Fix cross-mode navigation path

### Estimated Fix Time

- 37 path corrections across 7 files
- Estimated time: 30-45 minutes (manual) or 5 minutes (automated find/replace)
