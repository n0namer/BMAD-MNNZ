---
title: Output Format Validation - Fixes Checklist
date: 2026-02-06
status: READY_TO_IMPLEMENT
priority: HIGH_PRIORITY_ITEMS
---

# Output Format Validation - Implementation Checklist

## OVERVIEW

This checklist tracks the 5 findings from the output format validation and provides step-by-step fixes.

**Total Issues:** 5 (0 critical, 2 high, 3 medium)
**Estimated Fix Time:** 2-3 hours
**Blocking Release:** No

---

## HIGH PRIORITY ITEMS (Do This Sprint)

### 1. Create decision-log.template.md

**Severity:** HIGH
**Impact:** Decisions currently appended to workflow-plan.md, should be separately stored

**Current Situation:**
- Decisions handled in step-05-scoring.md (lines 125-142)
- Appended to workflow-plan.md
- No separate decision-log template exists
- Makes it hard to audit decisions independently

**Action Items:**
- [ ] Create file: `_bmad/bmm/workflows/life-os/templates/project/decision-log.template.md`
- [ ] Define YAML frontmatter:
  ```yaml
  ---
  idea_id: IDEA-YYYY-NNN
  project_id: PROJ-YYYY-NNN
  decision_date: YYYY-MM-DD
  decision: [GO/NO-GO/DEFER/PIVOT]
  stage: [foundation/scoring/planning/execution/review]
  approved_by: [role/name]
  ---
  ```
- [ ] Define sections:
  - Decision (what was decided)
  - Rationale (why)
  - Trade-offs (what was sacrificed)
  - Approval (who approved)
  - Notes (additional context)
- [ ] Update step-05-scoring.md:
  - Add instruction to save to `decisions/decision-log.md`
  - Reference new template
  - Add line: `npx claude-flow@v3alpha memory store --namespace "shared-knowledge" --key "decision:{idea-id}"`
- [ ] Update workflow.md:
  - Line 452 should reference new template
  - Add note: "Decisions stored separately in decisions/decision-log.md"

**Files to Modify:**
- Create: `templates/project/decision-log.template.md`
- Modify: `steps-c/step-05-scoring.md` (add save instruction)
- Modify: `workflow.md` (line 452, clarify location)

**Effort:** 30 minutes


### 2. Document ideas-bank Folder Structure

**Severity:** HIGH
**Impact:** Structure inferred from code but not explicit, causes confusion

**Current Situation:**
- workflow.md line 451 mentions `ideas-bank/`
- No explicit subfolder structure documented
- Idea statuses implied from idea.template.md (line 6: `status: inbox`)
- Status flow: inbox → evaluated → planned → executed → archived

**Action Items:**
- [ ] Update workflow.md OUTPUTS section (lines 447-458):
  - Add explicit folder structure
  - Include this under "All artifacts live in {bmb_creations_output_folder}/life-os/":

  ```
  **Ideas Bank Structure:**

  ideas-bank/
  ├── inbox/              — New ideas, not yet evaluated
  │   └── IDEA-YYYY-NNN.md
  ├── evaluated/          — Scored with decision made
  │   └── IDEA-YYYY-NNN.md
  ├── planned/            — Approved, in planning phase
  │   └── IDEA-YYYY-NNN.md
  ├── executed/           — In progress or completed
  │   └── IDEA-YYYY-NNN.md
  └── archived/           — Rejected or deferred
      └── IDEA-YYYY-NNN.md

  **Status Transitions:**
  1. Create in inbox/
  2. Move to evaluated/ (after step-05-scoring)
  3. Move to planned/ (if approved + activated)
  4. Move to executed/ (when project starts)
  5. Move to archived/ (when killed/deferred)
  ```

- [ ] Add note explaining status transitions
- [ ] Reference idea.template.md line 6 status field

**Files to Modify:**
- Modify: `workflow.md` (lines 447-458, expand OUTPUTS section)

**Effort:** 15 minutes


---

## MEDIUM PRIORITY ITEMS (Do in v3.1)

### 3. Standardize Timestamp Field Names

**Severity:** MEDIUM
**Impact:** Inconsistent field naming makes scripting harder

**Current Inconsistency:**
- `idea.template.md` line 5: `created: YYYY-MM-DD`
- `workflow-plan.template.md` line 3: `creationDate: '{{date}}'`
- `domain-template-architecture.md` line 47: `created_date: "[YYYY-MM-DD]"`

**Target Standard:** `created_date` (underscore format, ISO 8601)

**Action Items:**
- [ ] Update `templates/idea.template.md`:
  ```yaml
  - created: YYYY-MM-DD
  + created_date: YYYY-MM-DD
  ```

- [ ] Update `templates/project.template.md`:
  ```yaml
  - started: YYYY-MM-DD
  + created_date: YYYY-MM-DD
  ```

- [ ] Update `templates/workflow-plan.template.md`:
  ```yaml
  - creationDate: '{{date}}'
  + created_date: '{{date}}'
  ```

- [ ] Update all 42 domain templates to use `created_date`
  - Run: `grep -r "creationDate\|^created:" templates/ --include="*.template.md"`
  - Replace all occurrences with `created_date`

- [ ] Add comment in templates to clarify field purpose:
  ```yaml
  # Creation timestamp (ISO 8601 format)
  created_date: YYYY-MM-DD
  ```

**Files to Modify:**
- All 42 template files in templates/ directory

**Effort:** 45 minutes (with batch find-replace)


### 4. Create metrics.template.md

**Severity:** MEDIUM
**Impact:** Metrics referenced but no standard template, leads to inconsistent tracking

**Current Situation:**
- workflow.md line 453: `metrics/metrics.md`
- Data in workflow.md lines 669-671 but no template
- Expected to track:
  - Framework effectiveness ratings
  - Success rate monitoring
  - Time investment tracking

**Action Items:**
- [ ] Create file: `templates/metrics/metrics.template.md`
- [ ] Define YAML frontmatter:
  ```yaml
  ---
  date_generated: YYYY-MM-DD
  period: [daily|weekly|monthly|quarterly]
  as_of_date: YYYY-MM-DD
  ---
  ```

- [ ] Define sections:
  - Framework Effectiveness (table: framework, success_rate, uses, rating)
  - Project Portfolio (status, active_count, completion_rate)
  - Time Investment (hours by domain, average per project)
  - Risk Summary (active blockers, milestone delays)
  - Strategic Alignment (goal progress, capacity usage)

- [ ] Update workflow.md line 453 to reference new template

**Files to Modify:**
- Create: `templates/metrics/metrics.template.md`
- Modify: `workflow.md` (line 453, reference template)

**Effort:** 30 minutes


### 5. Add Required vs Optional Field Markers

**Severity:** MEDIUM
**Impact:** Templates don't mark which fields are required, harder to validate

**Current Situation:**
- All templates have YAML frontmatter
- No indication which fields are required vs optional
- Users might forget to fill required fields

**Action Items:**
- [ ] Add section comments to all 42 templates:
  ```yaml
  ---
  # === REQUIRED FIELDS (must always be present) ===
  id: IDEA-YYYY-NNN
  title: [Your Title]
  created_date: YYYY-MM-DD

  # === OPTIONAL FIELDS (can be null or filled later) ===
  evaluation: null
  decision: null
  ```

- [ ] Document in each template:
  - Required: Show example values
  - Optional: Explain when typically filled
  - Timestamp: Enforce ISO 8601 format

- [ ] Create validation guide: `data/frontmatter-validation-rules.md`
  - Required field list per template type
  - Valid value ranges
  - Format examples

**Files to Modify:**
- All 42 template files (add comments)
- Create: `data/frontmatter-validation-rules.md`

**Effort:** 1.5 hours (many files)


---

## LOW PRIORITY ITEMS (Backlog)

### 6. Create NAMING_CONVENTIONS.md

**Severity:** LOW
**Impact:** ID and naming rules scattered across templates, not centralized

**Location:** Create `_bmad/bmm/workflows/life-os/data/NAMING_CONVENTIONS.md`

**Content:**
```markdown
# Naming Conventions for Life OS

## IDs

### Format
{TYPE}-{YYYY}-{NNN}

### Components
- **TYPE**: IDEA | PROJ
- **YYYY**: Calendar year (UTC) - Example: 2026
- **NNN**: Sequential number - Format: 001-999 per year/type

### Examples
- IDEA-2026-001 (first idea of 2026)
- IDEA-2026-042 (42nd idea of 2026)
- PROJ-2026-001 (first project of 2026)

### Generation Rules
1. Type determines prefix (IDEA or PROJ)
2. Use calendar year (January 1 starts at 001)
3. Increment within type (IDEA and PROJ separate sequences)
4. Reset each calendar year
5. Never reuse numbers (gaps are OK)

## Timestamps

### Format
ISO 8601 (YYYY-MM-DD)

### Rules
- Use UTC time consistently
- Use date only (no time component)
- Examples: 2026-02-06, 2026-12-31

## Field Names

### Standard Fields
- created_date (not created, not creationDate)
- completed_date (or null if not done)
- updated_date (optional, for tracking changes)

### Status Values
- Idea: inbox, evaluated, planned, executed, archived
- Project: active, paused, completed, archived
- Workflow: IN_PROGRESS, COMPLETED, PAUSED

### Sphere Values
- health
- wealth (financial)
- relationships
- growth (personal development)
- contribution (giving back)

### Domain Values (for frameworks)
- business
- finance
- health
- personal (personal development)
- universal (applies to all)

## File Organization

### Paths
All artifacts: {bmb_creations_output_folder}/life-os/

### Naming Pattern
{type}/{id}/{name}.md where applicable

### Examples
- ideas-bank/inbox/IDEA-2026-001.md
- projects/PROJ-2026-001/README.md
- decisions/decision-log.md
```

**Effort:** 20 minutes


### 7. Clarify Portfolio.md Location

**Severity:** LOW
**Impact:** Minor ambiguity about exact path

**Current Situation:**
- workflow.md line 450: `portfolio.md` (dashboard)
- No explicit path shown

**Action:** Clarify in workflow.md OUTPUTS section:
```
File: {bmb_creations_output_folder}/life-os/portfolio.md
Template: templates/project/portfolio-dashboard.template.md
```

**Effort:** 5 minutes


### 8. Document NNN Range Explicitly

**Severity:** LOW
**Impact:** ID generation scripts might fail without clear spec

**Action Items:**
- [ ] Update idea.template.md line 2 comment:
  ```yaml
  # ID format: IDEA-YYYY-NNN
  # NNN: 001-999 (sequential per year)
  id: IDEA-YYYY-NNN
  ```

- [ ] Update project.template.md line 2 comment:
  ```yaml
  # ID format: PROJ-YYYY-NNN
  # NNN: 001-999 (sequential per year)
  id: PROJ-YYYY-NNN
  ```

- [ ] Add to NAMING_CONVENTIONS.md (from item #6)

**Effort:** 10 minutes


---

## IMPLEMENTATION TIMELINE

### Sprint 1 (This Week)
- [x] Complete output format validation
- [ ] Item #1: Create decision-log.template.md (30 min)
- [ ] Item #2: Document ideas-bank structure (15 min)
**Time:** 45 minutes

### Sprint 2 (Next Week)
- [ ] Item #3: Standardize timestamp fields (45 min)
- [ ] Item #4: Create metrics.template.md (30 min)
- [ ] Item #5: Add Required/Optional markers (1.5 hours)
**Time:** 2.75 hours

### Sprint 3+ (Backlog)
- [ ] Item #6: Create NAMING_CONVENTIONS.md (20 min)
- [ ] Item #7: Clarify portfolio.md location (5 min)
- [ ] Item #8: Document NNN range (10 min)
**Time:** 35 minutes

**Total Implementation Time:** ~3.5 hours


---

## VERIFICATION CHECKLIST

After implementing all fixes:

- [ ] All 42 templates use `created_date` field
- [ ] decision-log.template.md created and referenced
- [ ] ideas-bank folder structure documented in workflow.md
- [ ] metrics.template.md created
- [ ] All templates mark required vs optional fields
- [ ] NAMING_CONVENTIONS.md created (if doing backlog)
- [ ] No inconsistencies in field naming across templates
- [ ] All YAML frontmatter validated against rules

---

## FILES TO MODIFY SUMMARY

**Create (3 files):**
1. `templates/project/decision-log.template.md`
2. `templates/metrics/metrics.template.md`
3. `data/NAMING_CONVENTIONS.md` (optional backlog)

**Modify (Multiple):**
1. `workflow.md` (lines 450-458, clarify paths)
2. `steps-c/step-05-scoring.md` (lines 172+, save to decision-log)
3. All 42 template files (field names, markers)

**Total Files to Touch:** ~50 (1 new, 1 major workflow change, 48+ templates)

---

## PRIORITY RECOMMENDATION

**For v3.0 Release:**
- [x] Complete validation (DONE)
- [ ] Implement HIGH priority items (2 items, 45 min)
- [ ] Implement MEDIUM priority items (3 items, 2.75 hours)
- [ ] Total: ~3.25 hours
- [ ] Backlog LOW priority items (3 items, 35 min)

**Decision:** Can release v3.0 after HIGH + MEDIUM priority items. LOW priority items improve DX but aren't blocking.

---

**Report:** OUTPUT_FORMAT_VALIDATION_REPORT.md
**Summary:** OUTPUT_FORMAT_VALIDATION_SUMMARY.txt
**Checklist:** This file
**Status:** READY_TO_IMPLEMENT
**Approved By:** Code Review Agent
**Date:** 2026-02-06

