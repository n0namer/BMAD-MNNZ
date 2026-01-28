# Detailed Violations: Step Type Pattern Analysis

**Document:** File-by-file violations and issues
**Generated:** 2026-01-28
**Severity Levels:** Critical | Major | Minor

---

## CRITICAL VIOLATIONS

### 1. EDIT Mode Fragmentation Pattern (18 step pairs)

**Violation Type:** Type ambiguity + File duplication
**Severity:** CRITICAL
**Impact:** Routing logic unclear, maintenance risk

#### Pattern Identified:

Each EDIT step exists in two forms:
1. **Stub File** (minimal content, vague type): `step-e-[XY][a-c].md`
2. **Descriptor File** (actual content, specific type): `step-e-[XY][a-c]-[name].md`

Example: Mode E-01
```
step-e-01a.md
├── type: edit
├── Description: [MISSING]
└── Content: [MINIMAL]

step-e-01a-select-posts.md
├── type: selection-filter
├── Description: Filter posts for editing
└── Content: [FULL CONTENT]
```

#### Affected Files (18 total):

| Stub File | Descriptor File | Type Issue |
|-----------|-----------------|-----------|
| step-e-01a.md | step-e-01a-select-posts.md | edit → selection-filter |
| step-e-01b.md | step-e-01b-improvements.md | edit → ai-analysis-recommendation |
| step-e-01c.md | step-e-01c-apply-edits.md | edit → batch-apply-changes |
| step-e-02a.md | step-e-02a-load-checklist.md | edit → load-checklist |
| step-e-02b.md | step-e-02b-evaluate.md | edit → checklist-evaluation |
| step-e-02c.md | step-e-02c-apply.md | edit → apply-checklist-improvements |
| step-e-03a.md | step-e-03a-select-post.md | edit → single-selection |
| step-e-03b.md | step-e-03b-generate.md | edit → variant-generation |
| step-e-03c.md | step-e-03c-compare.md | edit → variant-comparison |
| step-e-04a.md | step-e-04a-load-posts.md | edit → load-data |
| step-e-04b.md | step-e-04b-recalculate.md | edit → metrics-recalculation |
| step-e-04c.md | step-e-04c-save.md | edit → save-metrics |
| step-e-05a.md | step-e-05a-identify.md | edit → filter-posts |
| step-e-05b.md | step-e-05b-rewrite.md | edit → auto-rewrite |
| step-e-05c.md | step-e-05c-compare.md | edit → before-after-comparison |
| step-e-06a.md | step-e-06a-select.md | edit → filter-old-posts |
| step-e-06b.md | step-e-06b-archive.md | edit → move-to-archive |
| step-e-07a.md | step-e-07a-load-history.md | edit → load-version-history |
| step-e-07b.md | step-e-07b-view.md | edit → display-history |
| step-e-08a.md | step-e-08a-select.md | edit → dual-selection |
| step-e-08b.md | step-e-08b-compare.md | edit → post-comparison |

#### Questions This Raises:

1. **Why two files?**
   - Stub files have minimal content (3-5 lines)
   - Real content in descriptor files
   - Routing unclear which to load

2. **Which is canonical?**
   - Stub files listed in mode-e-00-menu.md routing
   - Descriptor files contain actual implementation
   - Contradiction suggests incomplete refactoring

3. **What's routing logic?**
   - Load stub, which redirects to descriptor?
   - Load descriptor directly?
   - Load both?
   - Unknown

#### Example Code (step-e-01a.md):
```yaml
---
name: step-e-01a
type: edit
description: [NO DESCRIPTION]
nextStepFile: ./step-e-01a-select-posts.md
---

[ALMOST NO CONTENT]
```

#### Recommended Fix:

**Option A: Remove Stubs (Recommended)**
```
Delete all 18 step-e-[XY][a-c].md files
Rename all step-e-[XY][a-c]-[name].md → step-e-[XY][a-c].md
Update type: from specific type → match pattern
```

**Option B: Use Stubs as Routers**
```
Keep stub files as routing handlers
Change type: edit → router
Add routing logic to stubs
Make descriptor files endpoints (no next routing)
```

**Option C: Merge into Single Files**
```
Combine stub + descriptor content into one file
Keep descriptive naming: step-e-[XY][a-c]-[name].md
Update all mode-menu routing
Ensure type matches function
```

**Recommendation:** Use Option A (Remove Stubs)
- Simpler maintenance
- Clearer routing
- Type matches content
- Follows standard BMAD pattern

---

### 2. Data-Loading Steps Without Menu Pattern (8 steps)

**Violation Type:** Missing menu pattern specification
**Severity:** CRITICAL
**Impact:** Unclear step termination and routing

#### Affected Files:

| File | Current Type | Issue | Next Step |
|------|--------------|-------|-----------|
| mode-c-02/step-c-02a-load-ideas.md | data-loading | No menu spec | Next step unclear |
| mode-v-01/step-v-01a-load.md | data-loading | No menu spec | Hardcoded next? |
| mode-v-02/step-v-02a-load.md | data-loading | No menu spec | Auto-proceed? |
| mode-v-03/step-v-03a-load.md | data-loading | No menu spec | User choice? |
| mode-v-04/step-v-04a-load.md | data-loading | No menu spec | ??? |
| mode-v-05/step-v-05a-load.md | data-loading | No menu spec | ??? |
| mode-v-06/step-v-06a-load.md | data-loading | No menu spec | ??? |
| mode-v-07/step-v-07a-load.md | data-loading | No menu spec | ??? |

#### Problem Example:

```yaml
# mode-v-01/step-v-01a-load.md
---
name: step-v-01a-load
type: data-loading
description: Load quality metrics data
nextStepFile: ./step-v-01b-checks.md
---

# Where's the menu after loading?
# Auto-proceed to next step?
# Show a menu?
# User confirmation needed?
```

#### Questions:

1. **Should data-loading auto-proceed?**
   - Current: Unclear from type alone
   - Expected: Type should indicate (data-loading-auto vs data-loading-confirm)

2. **Does user see the loaded data?**
   - If yes: Should have menu for navigation
   - If no: Can auto-proceed
   - Type doesn't specify

3. **What if loading fails?**
   - No error handling visible
   - No retry menu
   - No fallback routing

#### Recommended Fix:

```yaml
# Change from:
type: data-loading

# Change to one of:
type: data-loading-auto    # Auto-proceed after loading
type: data-loading-display # Load and show data with menu
type: data-loading-confirm # Load and require confirmation

# Add explicit menu section:
# (even if minimal)
---
menu: |
  [C] Continue to next step
```

---

## MAJOR VIOLATIONS

### 3. Report Generation Without Subtype (8 steps)

**Violation Type:** Identical type for different report types
**Severity:** MAJOR
**Impact:** Cannot determine report purpose from type

#### Affected Files:

| File | Report Type | Actual Purpose |
|------|-------------|-----------------|
| mode-v-01/step-v-01c-report.md | report-generation | Quality checklist report |
| mode-v-02/step-v-02c-report.md | report-generation | Performance audit report |
| mode-v-03/step-v-03c-report.md | report-generation | Consistency check report |
| mode-v-04/step-v-04c-report.md | report-generation | Copywriting audit report |
| mode-v-05/step-v-05c-report.md | report-generation | Engagement prediction |
| mode-v-06/step-v-06c-report.md | report-generation | Batch validation summary |
| mode-v-08/step-v-08b-generate.md | report-generation | Comprehensive quality report |

**Problem:**

All 8 report steps have identical type, but completely different content and output formats.

```yaml
# mode-v-01/step-v-01c-report.md (Quality Report)
type: report-generation
# Output: CSV + PDF, quality scores, pass/fail

# mode-v-02/step-v-02c-report.md (Performance Report)
type: report-generation
# Output: Performance metrics, rankings, bottlenecks

# mode-v-03/step-v-03c-report.md (Consistency Report)
type: report-generation
# Output: Deviation analysis, pattern matching
```

#### Recommended Fix:

```yaml
# Change from generic:
type: report-generation

# Change to specific:
type: report-quality-checklist
type: report-performance-audit
type: report-consistency-check
type: report-copywriting-audit
type: report-engagement-predict
type: report-batch-validation
type: report-comprehensive

# Or use suffix pattern:
type: report-generation-quality
type: report-generation-audit
```

---

### 4. Selection Type Fragmentation (6 variants)

**Violation Type:** Inconsistent naming for similar functionality
**Severity:** MAJOR
**Impact:** No clear pattern, requires reading file content

#### Affected Files & Variations:

| Type Used | Count | Files | Issue |
|-----------|-------|-------|-------|
| selection | 5 | c-02b, c-03a, c-03b, c-05a, c-06a | Generic |
| single-selection | 1 | e-03a | Clarified |
| dual-selection | 1 | e-08a | Clarified |
| selection-filter | 1 | e-01a | Clarified |
| filter-posts | 1 | e-05a | Clarified |
| filter-old-posts | 1 | e-06a | Clarified |

#### Problem:

No consistent naming convention for selection variants.

```yaml
# CREATE Mode uses generic:
type: selection           # 5 occurrences

# EDIT Mode uses descriptive:
type: single-selection    # 1 specific variant
type: dual-selection      # 2-option variant
type: selection-filter    # Filtered variant
type: filter-posts        # Specific domain
type: filter-old-posts    # Even more specific
```

#### Recommended Fix:

**Standardize to pattern:** `selection-[variant]`

```yaml
type: selection-single    # One item selection
type: selection-dual      # Two-option choice
type: selection-multi     # Multiple items
type: selection-filter    # Filtered options
type: selection-ideas     # Ideas selection
type: selection-posts     # Posts selection
```

Or use domain prefix:

```yaml
type: ideas-selection
type: posts-selection
type: angles-selection
```

---

### 5. Analysis Type Inconsistency (6 steps)

**Violation Type:** 3 different type names for similar functionality
**Severity:** MAJOR
**Impact:** Cannot predict type name for new analysis step

#### Affected Files:

| Type Name | Count | Files |
|-----------|-------|-------|
| automated-analysis | 3 | mode-v-02b, mode-v-04b, mode-v-03b |
| ai-analysis | 2 | mode-v-05b, mode-c-05b |
| ai-analysis-recommendation | 1 | mode-e-01b |
| detailed-analysis | 1 | mode-c-07b |

#### Problem:

Four different type names for semantically similar operations.

```yaml
# Validation Mode:
type: automated-analysis        # Machine analysis

# Creation Mode:
type: ai-analysis              # AI analysis

# Edit Mode:
type: ai-analysis-recommendation # AI with suggestion

# Creation Mode:
type: detailed-analysis        # Human-style detailed
```

#### Recommended Fix:

Create standard pattern: `analysis-[variant]`

```yaml
type: analysis-automated   # Machine-driven
type: analysis-ai          # AI-driven
type: analysis-detailed    # Comprehensive
type: analysis-quick       # Fast overview
```

---

## MINOR VIOLATIONS

### 6. Inconsistent Functional Type Naming

**Violation Type:** Non-uniform naming conventions
**Severity:** MINOR
**Impact:** Harder to guess types for new steps

#### Examples:

| Pattern Inconsistency | Files | Fix |
|----------------------|-------|-----|
| before-after-comparison vs post-comparison | e-05c, e-08b | Standardize to comparison-* |
| load-version-history vs display-history | e-07a, e-07b | Standardize to history-* |
| batch-apply-changes vs apply-checklist-improvements | e-01c, e-02c | Standardize to apply-* |
| filter-posts vs filter-old-posts | e-05a, e-06a | Standardize to filter-* |
| move-to-archive vs confirmation | e-06b, c-05d | Standardize or clarify intent |

#### Recommended Naming Standards:

**Load Operations:**
```
load-data              # Load any data
load-checklist         # Load checklist template
load-ideas             # Load ideas
load-posts             # Load posts
load-history           # Load version/change history
```

**Display Operations:**
```
display-[what]         # Always use display- prefix
display-history        # Show history
display-results        # Show results
display-metrics        # Show metrics
```

**Filter Operations:**
```
filter-[domain]-[criteria]
filter-posts           # Filter by criteria
filter-ideas           # Filter ideas
filter-old-posts       # Filter by age
```

**Apply Operations:**
```
apply-[what]
apply-changes          # Apply edits
apply-improvements     # Apply recommendations
apply-archive          # Move to archive (use move- instead)
```

---

## ROUTING VERIFICATION ISSUES

### 7. Step Chain Continuity Questions

**Issue:** Some steps unclear about routing

#### Example: mode-v-01 sequence
```
step-v-01a-load.md
  ↓ (nextStepFile: ./step-v-01b-checks.md)
step-v-01b-checks.md (automated-validation)
  ↓ (nextStepFile: ./step-v-01c-report.md)
step-v-01c-report.md (report-generation)
  ↓ (nextStepFile: unclear from type)
Mode menu or exit?
```

**Problem:** Type alone doesn't indicate if step has menu or auto-proceeds.

#### Affected Patterns:

1. **Data-loading steps** - No menu pattern specified
2. **Report-generation steps** - Unclear if menu follows
3. **Management steps** - No next routing visible
4. **Confirmation steps** - Unclear what happens after

---

## SUMMARY TABLE: All Violations by Severity

| Severity | Category | Count | Files Affected | Effort |
|----------|----------|-------|-----------------|--------|
| CRITICAL | EDIT stub files | 18 | step-e-[01-08][a-c].md | 2-3h |
| CRITICAL | Data-loading menu pattern | 8 | mode-[c,v] load steps | 1h |
| MAJOR | Report subtype missing | 8 | mode-v [01-06, 08] | 30m |
| MAJOR | Selection fragmentation | 6 | 6 different types | 30m |
| MAJOR | Analysis inconsistency | 6 | 4 different types | 30m |
| MINOR | Naming inconsistency | 15+ | Various | 1h |
| MINOR | Menu pattern docs | All | Need documentation | 30m |
| **TOTAL** | | **65+** | **106 steps** | **6-7h** |

---

## Resolution Priority

### Sprint 1 (Critical - This Sprint)
1. Remove EDIT stub files (18 files)
   - Time: 30 minutes
   - Verification: Re-test all EDIT mode flows

2. Add menu pattern to data-loading types (8 files)
   - Time: 15 minutes
   - Format: Change type from `data-loading` to `data-loading-[pattern]`

### Sprint 2 (Major - Next Sprint)
3. Add report subtypes (8 files)
   - Time: 30 minutes
   - Format: Change type to `report-[subtype]`

4. Standardize selection types (6 files)
   - Time: 30 minutes
   - Format: Use `selection-[variant]` pattern

5. Standardize analysis types (6 files)
   - Time: 30 minutes
   - Format: Use `analysis-[variant]` pattern

### Sprint 3 (Minor - Documentation)
6. Create type taxonomy documentation
   - Time: 1 hour
   - Deliverable: types-reference.md

7. Add naming standards guide
   - Time: 1 hour
   - Deliverable: naming-conventions.md

---

## Files Ready for Immediate Action

### Ready to Delete (18 files):
```
mode-e-01/step-e-01a.md
mode-e-01/step-e-01b.md
mode-e-01/step-e-01c.md
mode-e-02/step-e-02a.md
mode-e-02/step-e-02b.md
mode-e-02/step-e-02c.md
[continues for e-03 through e-08]
Total: 18 files
```

### Ready for Quick Reclassification (8 files):
```
mode-c-02/step-c-02a-load-ideas.md          → data-loading-auto
mode-v-01/step-v-01a-load.md                → data-loading-auto
mode-v-02/step-v-02a-load.md                → data-loading-auto
[continues for v-03 through v-07]
Total: 8 files
Time: ~1 minute each
```

---

## Validation Complete

All violations documented. Workflow is **functionally correct** but needs **type standardization** for maintainability and clarity.
