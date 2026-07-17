# Life OS Workflow - Complete Files Inventory

## Overview

This document provides a complete inventory of all step files referenced in the Life OS workflow (workflow.md).

---

## CREATE MODE STEPS (steps-c folder)

### Foundation Steps (Pre-execution)

| # | File | Referenced | Status | Purpose |
|---|------|-----------|--------|---------|
| 0 | step-00-foundation-check.md | ✅ YES (Lines 135, 137) | ACTIVE | Entry point - Check if foundation data exists |
| 0.1 | step-00.1-portfolio-intake.md | ✅ YES (Line 136) | ACTIVE | Batch mode - Collect 3-10 ideas |
| 0.5 | step-00.5-project-stage.md | ✅ YES (Line 146) | ACTIVE | Foundation step 1 - Determine current state (Точка А) |
| 0.6 | step-00.6-resource-assessment.md | ✅ YES (Line 147) | ACTIVE | Foundation step 2 - Calculate Speed Multiplier |
| 0.7 | step-00.7-optimization-intelligence.md | ✅ YES (Line 148) | ACTIVE | Foundation step 3 - Suggest optimal approaches |
| 0-goals | step-00-goals-discovery.md | ⚠️ UNCLEAR (Line 149) | ACTIVE | Optional - Goals discovery ⚠️ ROUTING ISSUE |

### Idea Collection & Analysis

| # | File | Referenced | Status | Purpose |
|---|------|-----------|--------|---------|
| 1 | step-01-collect-ideas.md | ✅ YES (Lines 152, 204) | ACTIVE | Collect ideas from user |
| 2 | step-02-roles-discovery.md | ✅ YES (Line 217) | ACTIVE | Define required roles (Standard/Deep only) |
| 3 | step-03-specialist-match.md | ✅ YES (Line 218) | ACTIVE | Match specialists to roles (Standard/Deep only) |

### Consilium & Scoring

| # | File | Referenced | Status | Purpose |
|---|------|-----------|--------|---------|
| 4-lite | step-04-consilium-lite.md | ✅ YES (Line 211) | ACTIVE | Quick Track - 2-3 specialists, single round |
| 4 | step-04-consilium.md | ✅ YES (Line 219) | ACTIVE | Standard/Deep - Full consilium with Six Hats |
| 4.5 | step-04.5-triz-analysis.md | ✅ YES (Line 235) | ACTIVE | Deep Track - TRIZ analysis (auto-triggered if contradictions) |
| 5 | step-05-scoring.md | ✅ YES (Lines 206, 220) | ACTIVE | MCDA scoring (varies by track) |

### Integration & Planning

| # | File | Referenced | Status | Purpose |
|---|------|-----------|--------|---------|
| 6 | step-06-integration.md | ✅ YES (Lines 221, 237) | ACTIVE | Portfolio integration & WIP check |
| 7 | step-07-calendar-sync.md | ✅ YES (Line 238) | ACTIVE | Deep Track - Sync milestones to calendar |
| 8 | step-08-deep-plan.md | ✅ YES (Lines 222, 239) | ACTIVE | Create L1-L3 (Standard) or L1-L6 (Deep) plan |
| 8.5 | step-08.5-final-polish.md | ✅ YES (Line 240) | ACTIVE | Deep Track - Final review and refinement |
| 8.7 | step-08.7-activation-decision.md | ❌ NOT REFERENCED | UNKNOWN | ⚠️ Unknown purpose - file exists but not routed |
| 9 | step-09-complete.md | ✅ YES (Lines 207, 242) | ACTIVE | Completion checkpoint |
| 9-task | step-09-task-layer.md | ❌ NOT REFERENCED | UNKNOWN | ⚠️ Unknown purpose - file exists but not routed |

**Summary: 20 files, 18 referenced, 2 orphaned**

---

## VALIDATE MODE STEPS (steps-v folder)

### Review Modes

| # | File | Referenced | Status | Purpose |
|---|------|-----------|--------|---------|
| 0 | step-00-return-to-plan.md | ✅ YES (Line 443) | ACTIVE | Special mode - Quick context restore |
| 1 | step-01-daily-review.md | ✅ YES (Line 419) | ACTIVE | Daily quick review (5 min) |
| 2 | step-02-weekly-review.md | ✅ YES (Line 420) | ACTIVE | Weekly full review (30 min) |
| 3 | step-03-monthly-review.md | ✅ YES (Line 421) | ACTIVE | Monthly alignment check (1 hour) |
| 4 | step-04-quarterly-review.md | ✅ YES (Line 422) | ACTIVE | Quarterly pivot/kill decisions (2 hours) |
| 5 | step-05-refactoring-summary.md | ❌ NOT REFERENCED | UNKNOWN | ⚠️ Unknown purpose - file exists but not routed |
| v-5 | step-v-05-retrospective.md | ❌ NOT REFERENCED | UNKNOWN | ⚠️ Unknown purpose - file exists, naming inconsistency |

**Summary: 7 files, 5 referenced, 2 orphaned**

---

## EDIT MODE STEPS (steps-e folder)

### Project/Resource Management

| # | File | Referenced | Status | Purpose |
|---|------|-----------|--------|---------|
| 1 | step-01-update-project.md | ✅ YES (Line 435) | ACTIVE | Update existing project |
| 2a | step-02-update-specialist.md | ✅ YES (Line 436) | ACTIVE | Manage specialists |
| 2b | step-02-update-resources.md | ✅ YES (Line 437) | ACTIVE | Update portfolio resources |
| 3 | step-03-update-goals.md | ✅ YES (Line 438) | ACTIVE | Update long-term goals |
| 2-rescoring | step-02-rescoring.md | ❌ NOT REFERENCED | UNKNOWN | ⚠️ Unknown purpose - file exists but not routed |
| 3-kill | step-03-kill-project.md | ❌ NOT REFERENCED | UNKNOWN | ⚠️ Unknown purpose - file exists but not routed |
| 4-deep | step-04-deep-plan.md | ❌ NOT REFERENCED | UNKNOWN | ⚠️ Unknown purpose - file exists but not routed |

**Summary: 7 files, 4 referenced, 3 orphaned**

---

## EXECUTION MODE STEPS (steps-x folder)

### Execution Lifecycle

| # | File | Referenced | Status | Purpose |
|---|------|-----------|--------|---------|
| X-01 | step-x-01-kickoff.md | ✅ YES (Line 349) | ACTIVE | Start execution (PLANNED → IN_PROGRESS) |
| X-02 | step-x-02-weekly-pulse.md | ✅ YES (Line 359) | ACTIVE | Weekly status check (3-question protocol) |
| X-03 | step-x-03-milestone-gate.md | ✅ YES (Line 367) | ACTIVE | Milestone gate review |
| X-04 | step-x-04-pivot-or-kill.md | ✅ YES (Line 373) | ACTIVE | Pivot/kill decision framework |

**Summary: 4 files, 4 referenced, 0 orphaned**

---

## GRAND TOTALS

| Category | Total Files | Referenced | Orphaned | Status |
|----------|------------|-----------|----------|--------|
| Create (steps-c) | 20 | 18 (90%) | 2 (10%) | ⚠️ 2 orphaned |
| Validate (steps-v) | 7 | 5 (71%) | 2 (29%) | ⚠️ 2 orphaned |
| Edit (steps-e) | 7 | 4 (57%) | 3 (43%) | ⚠️ 3 orphaned |
| Execution (steps-x) | 4 | 4 (100%) | 0 (0%) | ✅ Complete |
| **TOTAL** | **38** | **31 (82%)** | **7 (18%)** | ⚠️ Incomplete |

---

## Orphaned Files Requiring Investigation

### High Priority (Production Blocking)

| File | Folder | Reason | Action Needed |
|------|--------|--------|---------------|
| step-00-goals-discovery.md | steps-c | Routing unclear in lines 149-151 | Add explicit routing OR remove menu option |
| step-05-refactoring-summary.md | steps-v | Not in VALIDATE menu | Add to menu OR archive |
| step-v-05-retrospective.md | steps-v | Not in VALIDATE menu, naming inconsistent | Add to menu OR archive |

### Medium Priority (Design Clarity)

| File | Folder | Reason | Action Needed |
|------|--------|--------|---------------|
| step-08.7-activation-decision.md | steps-c | Not referenced | Document purpose OR remove |
| step-09-task-layer.md | steps-c | Not referenced | Document purpose OR remove |
| step-02-rescoring.md | steps-e | Not referenced | Document purpose OR remove |
| step-03-kill-project.md | steps-e | Not referenced | Document purpose OR remove |
| step-04-deep-plan.md | steps-e | Not referenced | Document purpose OR remove |

---

## File Status Legend

| Symbol | Meaning |
|--------|---------|
| ✅ YES | File referenced in workflow.md with clear routing |
| ⚠️ UNCLEAR | File exists, referenced but routing ambiguous |
| ❌ NOT REFERENCED | File exists in folder but not routed anywhere |
| ACTIVE | File is properly configured and in use |
| UNKNOWN | Purpose unclear, needs investigation |

---

## Verification Checklist

- [x] All CREATE mode files verified
- [x] All VALIDATE mode files verified
- [x] All EDIT mode files verified
- [x] All EXECUTION mode files verified
- [x] Orphaned files identified
- [x] Routing paths confirmed
- [ ] Orphaned files classified (PENDING - user action required)
- [ ] Production-ready status confirmed (BLOCKED - issues must be resolved)

---

## Next Steps

### Required Before Production Use

1. **Resolve CRITICAL ISSUE #1**
   - File: step-00-goals-discovery.md
   - Action: Add explicit routing to workflow.md lines 149-151

2. **Resolve CRITICAL ISSUE #2**
   - Files: step-05-refactoring-summary.md, step-v-05-retrospective.md
   - Action: Add to VALIDATE menu OR archive to _archive/

### Recommended Improvements

3. Document purpose of each orphaned file (steps 3-7 in medium priority list)
4. Standardize naming conventions (step-v-05 → step-05)
5. Add subprocess pattern documentation to workflow.md
6. Specify Return-to-Plan output format

---

## Related Documents

- Full detailed report: `VALIDATION_REPORT_LIFE_OS_MENUS.md`
- Summary: `VALIDATION_SUMMARY.txt`
- Visual routing diagram: `MENU_ROUTING_DIAGRAM.txt`

---

**Report Date:** 2026-02-06
**Status:** ⚠️ PASS (Critical issues require fixes before production)
**Validator:** Code Review Agent
