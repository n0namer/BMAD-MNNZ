# Recommended Step Type Taxonomy
**Purpose:** Standardize and clarify step type classification
**Target Adoption:** Next sprint
**Backward Compatible:** Yes (mapping provided)

---

## Type System Architecture

### Three-Tier Classification System

```
TIER 1: Framework Types (Core Routing)
├── init-continuable     - Initial step with state resumption
├── main-menu            - Primary mode selection (4 modes)
├── mode-menu            - Sub-mode selection (8 options)
└── continuation         - Resume from saved state

TIER 2: Functional Category + Menu Pattern
├── [category]-[menu]
└── Examples:
    - data-loading-auto      # Load → auto-proceed
    - selection-filter       # Select from filtered set
    - report-generation-view # Generate report, show menu
    - edit-inline            # Edit with inline confirmation

TIER 3: Specialized Types (Use Sparingly)
├── Named for unique behavior
└── Examples:
    - parallel-execution     # Spawn parallel tasks
    - variant-generation     # Generate alternatives
    - ai-analysis            # AI-driven analysis
```

---

## Recommended Type Set

### Framework Types (5)

| Type | Usage | Menu | Next Step |
|------|-------|------|-----------|
| `init-continuable` | Entry point with session management | [Y/N/?/A/P] | step-01b-continue or step-00-menu |
| `main-menu` | Primary mode selection | [1/2/3/4/?/A/P] | mode-c/e/v/yolo |
| `mode-menu` | Sub-mode selection within mode | [1-8/?/A/P] | Sub-mode steps |
| `continuation` | Resume previous session | [C/M/etc] | Same mode, last step |
| `route` | Conditional routing (decision tree) | Custom | Based on condition |

### Functional Types with Menu Pattern (28)

#### A. Data Operations (7 types)

```
data-loading-auto
├─ Purpose: Load data, auto-proceed to next
├─ Menu: None (or minimal confirmation)
├─ Example: step-v-01a-load.md
├─ Used in: Validation mode, Research
└─ Files affected: 8

data-loading-display
├─ Purpose: Load and display data with options
├─ Menu: [C] Continue, [R] Review, [M] Back to menu
├─ Example: step-c-02a-load-ideas.md
├─ Used in: CREATE mode
└─ Files affected: 3

load-checklist
├─ Purpose: Load validation checklist template
├─ Menu: [C] Continue, [M] Back to menu
├─ Example: step-e-02a-load-checklist.md
├─ Used in: EDIT mode
└─ Files affected: 1

data-compilation
├─ Purpose: Compile and organize data
├─ Menu: [C] Continue, [M] Back
├─ Example: step-v-08a-compile.md
├─ Used in: Validation final reports
└─ Files affected: 1

Results precedence: Auto > Display > Custom
```

#### B. Input/Collection (3 types)

```
input-collection
├─ Purpose: Collect user-provided data
├─ Menu: [R] Research this, [A] Add more, [M] Back to menu
├─ Example: step-c-01-add-idea.md
├─ Used in: CREATE mode
└─ Files affected: 1

input-specification
├─ Purpose: Parse automation parameters
├─ Menu: [C] Continue, [M] Back to menu
├─ Example: step-yolo-01-input.md
├─ Used in: YOLO mode
└─ Files affected: 1

metrics-input
├─ Purpose: Input performance metrics
├─ Menu: [S] Save, [E] Edit, [M] Back
├─ Example: N/A (recommend creating if needed)
├─ Used in: Manual metric updates
└─ Files affected: 0
```

#### C. Selection/Filtering (5 types)

```
selection-single
├─ Purpose: Select one item from list
├─ Menu: [S] Select, [F] Filter, [M] Back
├─ Example: step-e-03a-select-post.md
├─ Used in: EDIT mode single actions
└─ Files affected: 1

selection-multi
├─ Purpose: Select multiple items
├─ Menu: [D] Done selecting, [F] Filter, [M] Back
├─ Example: step-c-06a-select-posts.md
├─ Used in: CREATE mode batch operations
└─ Files affected: 1

selection-filter
├─ Purpose: Select from filtered results
├─ Menu: [A] Apply, [F] Refine filter, [M] Back
├─ Example: step-e-01a-select-posts.md
├─ Used in: EDIT mode with filtering
└─ Files affected: 1

filter-criteria
├─ Purpose: Define filter parameters
├─ Menu: [A] Apply filter, [C] Cancel, [M] Back
├─ Example: N/A (recommend creating if needed)
├─ Used in: Advanced filtering
└─ Files affected: 0

search-input
├─ Purpose: Search with criteria
├─ Menu: Custom based on results
├─ Example: step-c-04a-search-criteria.md
├─ Used in: CREATE mode search
└─ Files affected: 1
```

#### D. Generation/Creation (5 types)

```
content-generation
├─ Purpose: Generate content (posts, variants, etc.)
├─ Menu: [R] Review, [E] Edit, [M] Back
├─ Example: step-c-03c-draft.md
├─ Used in: CREATE mode writing
└─ Files affected: 1

variant-generation
├─ Purpose: Generate alternatives/variants
├─ Menu: [S] Select best, [E] Edit, [M] Back
├─ Example: step-e-03b-generate.md, step-yolo-05-variants.md
├─ Used in: EDIT, YOLO modes
└─ Files affected: 3

research-execution
├─ Purpose: Research topic, generate insights
├─ Menu: [R] Review results, [S] See summary, [M] Back
├─ Example: step-c-02c-research.md
├─ Used in: CREATE mode idea research
└─ Files affected: 1

generation-parallel
├─ Purpose: Parallel generation of multiple items
├─ Menu: Varies, typically [C] Continue when done
├─ Example: step-yolo-02-parallel-execute.md
├─ Used in: YOLO mode automation
└─ Files affected: 1

data-compilation
├─ Purpose: Compile data into structured format
├─ Menu: [C] Continue, [E] Edit, [M] Back
├─ Example: step-v-08a-compile.md
├─ Used in: Final report compilation
└─ Files affected: 1
```

#### E. Analysis (4 types)

```
analysis-automated
├─ Purpose: Machine-driven analysis
├─ Menu: [V] View results, [R] Review, [M] Back
├─ Example: step-v-02b-audit.md, step-v-03b-analyze.md
├─ Used in: VALIDATE mode checks
└─ Files affected: 3

analysis-ai
├─ Purpose: AI-driven content/quality analysis
├─ Menu: [R] Review suggestions, [A] Apply, [M] Back
├─ Example: step-v-05b-predict.md
├─ Used in: VALIDATE mode
└─ Files affected: 2

analysis-detailed
├─ Purpose: Comprehensive analysis with insights
├─ Menu: [V] View full report, [S] Summary only, [M] Back
├─ Example: step-c-07b-deepdive.md
├─ Used in: CREATE mode analytics
└─ Files affected: 1

improvement-recommendation
├─ Purpose: Analyze and recommend improvements
├─ Menu: [A] Apply all, [S] Select, [R] Review, [M] Back
├─ Example: step-e-01b-improvements.md
├─ Used in: EDIT mode suggestions
└─ Files affected: 1
```

#### F. Validation/Checking (4 types)

```
validation-checklist
├─ Purpose: Validate against checklist
├─ Menu: [P] Pass, [F] Fail with feedback, [M] Back
├─ Example: step-v-01b-checks.md
├─ Used in: VALIDATE mode quality checks
└─ Files affected: 2

validation-parallel
├─ Purpose: Parallel validation checks
├─ Menu: [C] Continue when all done, [M] Back
├─ Example: step-v-06b-batch-checks.md
├─ Used in: VALIDATE mode batch validation
└─ Files affected: 1

validation-automated
├─ Purpose: Automated validation without menu
├─ Menu: None or [C] Continue
├─ Example: N/A, internal use in YOLO
├─ Used in: YOLO self-check
└─ Files affected: 1

improvement-engine
├─ Purpose: Auto-improve with suggestions
├─ Menu: [A] Apply suggestions, [R] Review, [M] Back
├─ Example: step-yolo-04-auto-improve.md
├─ Used in: YOLO automation
└─ Files affected: 1
```

#### G. Editing (3 types)

```
edit-inline
├─ Purpose: Inline editing with immediate feedback
├─ Menu: [S] Save, [C] Cancel, [P] Preview
├─ Example: step-e-01a.md (rename from generic "edit")
├─ Used in: EDIT mode inline edits
└─ Files affected: 18 (current generic "edit" files)

edit-bulk
├─ Purpose: Batch editing of multiple items
├─ Menu: [A] Apply all, [S] Select subset, [M] Back
├─ Example: step-e-01c-apply-edits.md
├─ Used in: EDIT mode batch operations
└─ Files affected: 1

auto-rewrite
├─ Purpose: Automatically rewrite content
├─ Menu: [A] Accept, [E] Edit, [M] Back
├─ Example: step-e-05b-rewrite.md
├─ Used in: EDIT mode content optimization
└─ Files affected: 1
```

#### H. Comparison (3 types)

```
comparison-variant
├─ Purpose: Compare multiple variants
├─ Menu: [S] Select best, [M] Back
├─ Example: step-e-03c-compare.md
├─ Used in: EDIT mode variant selection
└─ Files affected: 1

comparison-before-after
├─ Purpose: Show before/after comparison
├─ Menu: [A] Accept changes, [R] Reject, [E] Edit
├─ Example: step-e-05c-compare.md
├─ Used in: EDIT mode change review
└─ Files affected: 1

comparison-post
├─ Purpose: Compare posts side-by-side
├─ Menu: [S] Select winner, [E] Edit either, [M] Back
├─ Example: step-e-08b-compare.md
├─ Used in: EDIT mode post selection
└─ Files affected: 1
```

#### I. Reporting (5 types)

```
report-quality
├─ Purpose: Quality assessment report
├─ Menu: [E] Export, [D] Drill down, [M] Back
├─ Example: step-v-01c-report.md
├─ Used in: VALIDATE mode
└─ Files affected: 1

report-audit
├─ Purpose: Audit findings report
├─ Menu: [E] Export, [F] Fix issues, [M] Back
├─ Example: step-v-02c-report.md
├─ Used in: VALIDATE mode
└─ Files affected: 1

report-analytics
├─ Purpose: Analytics and insights
├─ Menu: [D] Deep dive, [E] Export, [M] Back
├─ Example: step-c-07a-dashboard.md
├─ Used in: CREATE mode analytics
└─ Files affected: 1

report-summary
├─ Purpose: Summary results
├─ Menu: [V] View details, [E] Export, [M] Back
├─ Example: step-yolo-06-summary.md
├─ Used in: YOLO mode results
└─ Files affected: 1

report-actionable
├─ Purpose: Actionable insights
├─ Menu: [A] Apply suggestions, [M] Back
├─ Example: step-c-07c-recommendations.md
├─ Used in: CREATE mode recommendations
└─ Files affected: 1
```

#### J. Management/Admin (3 types)

```
management-backup
├─ Purpose: Backup data management
├─ Menu: [B] Backup now, [S] Schedule, [M] Back
├─ Example: step-c-08a-backup.md
├─ Used in: CREATE mode maintenance
└─ Files affected: 1

management-archive
├─ Purpose: Archive old data
├─ Menu: [A] Archive now, [P] Preview, [M] Back
├─ Example: step-e-06b-archive.md
├─ Used in: EDIT mode maintenance
└─ Files affected: 1

maintenance
├─ Purpose: General maintenance operations
├─ Menu: Custom based on operation
├─ Example: step-c-08b-maintenance.md
├─ Used in: Database maintenance
└─ Files affected: 1
```

#### K. Display/View (2 types)

```
display-history
├─ Purpose: Show change history
├─ Menu: [S] Show selected, [C] Compare, [M] Back
├─ Example: step-e-07b-view.md
├─ Used in: EDIT mode version tracking
└─ Files affected: 1

display-results
├─ Purpose: Display search or operation results
├─ Menu: [S] Select items, [R] Refine, [M] Back
├─ Example: step-c-02d-results.md, step-c-04b-results.md
├─ Used in: CREATE mode results display
└─ Files affected: 2
```

#### L. Confirmation/Decision (2 types)

```
confirmation
├─ Purpose: Confirm action before proceeding
├─ Menu: [Y] Yes confirm, [N] Cancel, [E] Edit
├─ Example: step-c-05d-finalize.md, step-c-06d-save.md
├─ Used in: CREATE mode finalization
└─ Files affected: 2

decision
├─ Purpose: Choose between options
├─ Menu: [O1] Option 1, [O2] Option 2, [M] Back
├─ Example: step-c-06b-merge-strategy.md
├─ Used in: CREATE mode merge decisions
└─ Files affected: 1
```

### Specialized Types (Use Only If Necessary)

```
parallel-execution
├─ Purpose: Execute tasks in parallel
├─ Menu: None (progress display only)
├─ Example: step-yolo-02-parallel-execute.md
└─ Rationale: Unique architectural pattern

These types should ONLY be used when:
1. Standard type patterns don't fit
2. Behavior is fundamentally different
3. Documented with clear specifications
```

---

## Migration Mapping

### From Current → Recommended

```yaml
# Current → Recommended (with mappings)

FRAMEWORK TYPES:
init-continuable → init-continuable ✓ (no change)
main-menu → main-menu ✓ (no change)
mode-menu → mode-menu ✓ (no change)
continuation → continuation ✓ (no change)

VAGUE TYPES REQUIRING FIX:

edit (18 files):
  step-e-01a.md → edit-inline
  step-e-02a.md → edit-inline
  step-e-03a.md → edit-inline
  [... all e-mode steps ...]

data-loading (8 files):
  mode-c-02a-load-ideas.md → data-loading-display
  mode-v-*/step-v-*a-load.md → data-loading-auto

selection (5 files):
  step-c-02b-select-idea.md → selection-multi
  step-c-03a-select-idea.md → selection-single
  step-c-05a-select-post.md → selection-single
  step-c-06a-select-posts.md → selection-multi
  step-c-04a-search-criteria.md → search-input

ALREADY COMPLIANT (rename only):
input-collection → input-collection ✓
input-specification → input-specification ✓
research-execution → research-execution ✓
content-generation → content-generation ✓
variant-generation → variant-generation ✓
automated-analysis → analysis-automated
ai-analysis → analysis-ai
ai-analysis-recommendation → improvement-recommendation
detailed-analysis → analysis-detailed

REQUIRES SUBTYPE (add suffix):
report-generation → report-[type]:
  ├─ report-quality
  ├─ report-audit
  ├─ report-analytics
  └─ report-summary

CONSOLIDATE/RENAME:
selection-filter → selection-filter ✓
single-selection → selection-single
dual-selection → selection-multi (or custom routing)
filter-posts → selection-filter (domain-specific)
filter-old-posts → selection-filter (with criteria)

ALREADY NAMED WELL (OK):
confirmation → confirmation ✓
decision → decision ✓
management → management-[type]
```

---

## Implementation Steps

### Phase 1: Update Type Fields (2 hours)

**Files to modify:** 65 files

**Step 1.1: Fix EDIT Mode (18 files)**
```
For each step-e-[XY][a-c].md:
  1. Delete stub file (if separate from descriptor)
  2. Rename descriptor to step-e-[XY][a-c].md
  3. Update type: edit → appropriate type
  4. Update nextStepFile if needed
  5. Test routing
```

**Step 1.2: Fix Data-Loading (8 files)**
```
For each data-loading step:
  1. Determine behavior: auto-proceed or display?
  2. Update type accordingly:
     - type: data-loading-auto
     - OR type: data-loading-display
  3. Add menu section if display type
```

**Step 1.3: Add Report Subtypes (8 files)**
```
For each report-generation step:
  1. Read step content
  2. Determine report type
  3. Update type field:
     - type: report-quality
     - type: report-audit
     - etc.
```

**Step 1.4: Standardize Selection/Analysis (15 files)**
```
For selection types (5):
  1. Map to standard: selection-[variant]

For analysis types (6):
  1. Map to standard: analysis-[variant]
```

### Phase 2: Documentation (1 hour)

**Create/Update Documents:**
1. `/docs/type-taxonomy.md` - This document
2. `/docs/type-to-menu-mapping.md` - Menu patterns per type
3. `/docs/step-examples.md` - Example files per type
4. Update workflow comments

### Phase 3: Testing (1 hour)

**Validation:**
1. All files parse correctly
2. Routing chains complete
3. No unreachable steps
4. Menu transitions work
5. No circular routing

---

## Type-to-Menu Mapping

### Quick Reference Table

| Type Category | Type Name | Menu Style | Next Step |
|---------------|-----------|-----------|-----------|
| Framework | init-continuable | [Y/N/?/A/P] | Conditional |
| Framework | main-menu | [1/2/3/4/?/A/P] | Conditional |
| Framework | mode-menu | [1-8/?/A/P] | Conditional |
| Framework | route | Custom | Conditional |
| Data | data-loading-auto | (none) | Auto-proceed |
| Data | data-loading-display | [C/R/M] | User choice |
| Input | input-collection | [R/A/M] | Branch on choice |
| Input | input-specification | [C/M] | User confirms |
| Selection | selection-single | [S/F/M] | User selects |
| Selection | selection-multi | [D/F/M] | User selects |
| Selection | selection-filter | [A/F/M] | User confirms |
| Generation | content-generation | [R/E/M] | User reviews |
| Generation | variant-generation | [S/E/M] | User selects |
| Analysis | analysis-automated | [V/R/M] | User reviews |
| Analysis | analysis-ai | [R/A/M] | User confirms |
| Validation | validation-checklist | [P/F/M] | Auto-score |
| Editing | edit-inline | [S/C/P] | User confirms |
| Editing | edit-bulk | [A/S/M] | User confirms |
| Comparison | comparison-variant | [S/M] | User selects |
| Comparison | comparison-before-after | [A/R/E] | User chooses |
| Reporting | report-[type] | [E/D/M] | User action |
| Management | management-[type] | Custom | Depends |

---

## Benefits of New Taxonomy

### For Developers:
- Clear type-to-behavior mapping
- Self-documenting step files
- Easier to predict next step from type
- Simplified debugging

### For Maintainers:
- Consistent patterns across workflow
- Easier to add new steps
- Simpler code review process
- Better documentation

### For Users:
- More predictable menu patterns
- Clearer step intentions
- Better error messaging
- More intuitive routing

### For Architecture:
- Scalable type system
- Extensible through subtypes
- Backward compatible
- Clear separation of concerns

---

## Examples

### Example 1: Selection Step (Before → After)

**Before:**
```yaml
# step-c-02b-select-idea.md
type: selection
description: Select an idea from the list
nextStepFile: ./step-c-02c-research.md
```

**After:**
```yaml
# step-c-02b-select-idea.md
type: selection-multi
description: Select idea(s) to research
nextStepFile: ./step-c-02c-research.md
menu: |
  [S] Start research
  [F] Filter ideas
  [M] Back to menu
```

### Example 2: Data Loading (Before → After)

**Before:**
```yaml
# step-v-01a-load.md
type: data-loading
description: Load quality metrics
nextStepFile: ./step-v-01b-checks.md
```

**After:**
```yaml
# step-v-01a-load.md
type: data-loading-auto
description: Load quality metrics
nextStepFile: ./step-v-01b-checks.md
menu: |
  [Automatically proceeds to checks]
```

### Example 3: Report (Before → After)

**Before:**
```yaml
# step-v-02c-report.md
type: report-generation
description: Generate performance audit report
```

**After:**
```yaml
# step-v-02c-report.md
type: report-audit
description: Generate performance audit report
menu: |
  [E] Export report
  [F] Fix identified issues
  [M] Back to menu
```

---

## Adoption Timeline

- **Week 1:** Document and plan (this document)
- **Week 2:** Phase 1 - Update all type fields
- **Week 3:** Phase 2 - Update documentation
- **Week 4:** Phase 3 - Testing and validation

---

## Backward Compatibility

Old type names can be mapped through a compatibility layer:

```yaml
# compatibility-map.yaml
edit: edit-inline
data-loading: data-loading-auto  # Default to auto
report-generation: report-generic
selection: selection-multi       # Default to multi
```

This allows gradual migration without breaking existing automation.

---

## Questions & Answers

**Q: Why not just use one type per file?**
A: Menu pattern is essential context for routing. Two-part classification (category + pattern) is more informative.

**Q: What about custom steps?**
A: Use closest standard type + document the difference.

**Q: Will this change the routing?**
A: No, only the type field. All nextStepFile references remain valid.

**Q: Can I still use old type names?**
A: Yes, until migration is complete. Compatibility mapping provided.

---

## Summary

This taxonomy provides:
- ✓ 28 functional type combinations
- ✓ 5 framework types
- ✓ Clear naming patterns
- ✓ Self-documenting steps
- ✓ Backward compatibility
- ✓ Easy to extend

**Status:** Ready for implementation
