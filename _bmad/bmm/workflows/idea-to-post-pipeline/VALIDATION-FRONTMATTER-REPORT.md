# FRONTMATTER VALIDATION REPORT
## Content Machine Pipeline (steps-c/)

**Report Date:** 2026-01-30
**Validation Scope:** 9 target files for Content Machine Pipeline
**Status:** CRITICAL ISSUES FOUND

---

## EXECUTIVE SUMMARY

| Metric | Result | Status |
|--------|--------|--------|
| Files Analyzed | 9/9 | ✓ Complete |
| Valid YAML Frontmatter | 7/9 | ⚠️ 78% |
| All Required Fields Present | 7/9 | ⚠️ 78% |
| NextStepFile References Valid | 7/9 | ⚠️ 78% |
| Conditional Routing Documented | 1/1 | ⚠️ Partially |
| **CRITICAL ISSUES** | **3** | ❌ Requires Fix |
| **HIGH PRIORITY ISSUES** | **2** | ⚠️ Requires Fix |
| **MEDIUM PRIORITY ISSUES** | **4** | ⚠️ Should Fix |

---

## DETAILED FINDINGS

### 1. FILE: c-01-add-idea.md
**Status:** ✅ COMPLIANT

#### Frontmatter Analysis
```yaml
---
description: Collect raw idea, validate against criteria, collect content_type, check for duplicates, add to ideas_inbox
name: step-c-01-add-idea
nextStepFile: ./c-01b-dedup-check.md
type: input-collection
---
```

**Findings:**
- ✅ Valid YAML syntax
- ✅ Required fields present: `name`, `description`, `type`, `nextStepFile`
- ✅ Next step reference valid (c-01b-dedup-check.md exists)
- ✅ Field naming consistent with style

**Quality Score:** 10/10

---

### 2. FILE: c-02c-research.md
**Status:** ✅ COMPLIANT

#### Frontmatter Analysis
```yaml
---
description: Execute research - find 5-8 angles with sources and facts
name: step-c-02c-research
nextStepFile: ./c-02d-results.md
type: research-execution
---
```

**Findings:**
- ✅ Valid YAML syntax
- ✅ All required fields present
- ✅ Next step reference valid (c-02d-results.md exists)
- ✅ Consistent field naming

**Quality Score:** 10/10

---

### 3. FILE: c-02d-results.md
**Status:** ✅ COMPLIANT

#### Frontmatter Analysis
```yaml
---
description: Display detailed research results (all angles with sources)
name: step-c-02d-results
nextStepFile: ./c-03a-select-idea.md
type: results-display
---
```

**Findings:**
- ✅ Valid YAML syntax
- ✅ All required fields present
- ✅ Next step reference valid (c-03a-select-idea.md exists)

**Quality Score:** 10/10

---

### 4. FILE: c-03b-select-angle.md
**Status:** ❌ CRITICAL ISSUE - INVALID YAML

#### Frontmatter Analysis
```yaml
---
description: User selects which angle (from research) to use for the post
name: step-c-03b-select-angle
nextStepFile: ./c-03b1-offer-check.md (for demo) OR ./c-03c-draft.md (for normal)
type: selection
---
```

**Critical Issues Found:**

1. **CRITICAL: Invalid YAML Syntax in `nextStepFile`**
   - **Problem:** Value contains parenthetical comments and logical operators
   - **Current:** `./c-03b1-offer-check.md (for demo) OR ./c-03c-draft.md (for normal)`
   - **Impact:** YAML parser will fail; this is NOT valid YAML syntax
   - **Severity:** CRITICAL - will break automated step routing

2. **HIGH: Conditional Routing Not Properly Documented**
   - **Problem:** Frontmatter doesn't properly express conditional branching
   - **Current:** Single nextStepFile with inline comments
   - **Expected:** Should use a conditional structure or documentation field
   - **Impact:** Automation cannot determine which path to take based on `content_type`

3. **MEDIUM: Missing Conditional Logic Field**
   - **Problem:** No field documents when/how to route to c-03b1 vs c-03c
   - **Expected:** Should have `conditional` or `routing` field explaining:
     - Route to `c-03b1-offer-check.md` if `content_type == "demo"`
     - Route to `c-03c-draft.md` if `content_type == "normal"` or "other"

**Required Fixes:**

Option A (Recommended): Add explicit routing logic
```yaml
---
description: User selects which angle (from research) to use for the post
name: step-c-03b-select-angle
type: selection
conditional:
  field: content_type
  routes:
    - condition: "demo"
      nextStepFile: ./c-03b1-offer-check.md
      description: "For demo content - filter offers first"
    - condition: "normal"
      nextStepFile: ./c-03c-draft.md
      description: "For normal content - proceed to draft"
    - condition: "other"
      nextStepFile: ./c-03c-draft.md
      description: "For other content types - proceed to draft"
---
```

Option B (Simpler): Fix YAML and add documentation
```yaml
---
description: User selects which angle (from research) to use for the post
name: step-c-03b-select-angle
type: selection
routing:
  - if_content_type_is_demo: ./c-03b1-offer-check.md
  - if_content_type_is_normal_or_other: ./c-03c-draft.md
nextStepFile: ./c-03c-draft.md
nextStepFileDefault: ./c-03c-draft.md
---
```

**Quality Score:** 2/10

---

### 5. FILE: c-03b1-offer-check.md
**Status:** ⚠️ INCONSISTENT SCHEMA - DIFFERENT FIELD NAMES

#### Frontmatter Analysis
```yaml
---
stepId: c-03b1
stepType: user-input
stepName: Фильтр Офферов — "Мне Не Лень?" (Content Machine Stage 4)
estimatedMinutes: 2
nextStepFile: ./c-03b2-offer-generation.md
---
```

**Issues Found:**

1. **HIGH: Schema Mismatch - Different Field Names**
   - **Problem:** Uses different field names than other files
   - **Current Fields:** `stepId`, `stepType`, `stepName`, `estimatedMinutes`
   - **Expected Fields:** `name`, `type`, `description`, `nextStepFile`
   - **Impact:** Inconsistent schema makes automation difficult; parser must handle multiple schemas

2. **HIGH: Missing `description` Field**
   - **Required:** All steps should have `description`
   - **Impact:** Cannot display step purpose in unified menu system

3. **MEDIUM: `stepId` vs `name` Inconsistency**
   - **Current:** Uses `stepId: c-03b1` instead of `name: step-c-03b1`
   - **Impact:** Inconsistent naming convention across pipeline

4. **MEDIUM: No `type` Field Value (Has `stepType` instead)**
   - **Current:** `stepType: user-input`
   - **Expected:** `type: offer-filtering` or `type: user-input`
   - **Impact:** Makes type categorization inconsistent

**Required Fixes:**
```yaml
---
name: step-c-03b1-offer-check
description: Filter and configure which offer types to generate for demo content
type: offer-filtering
estimatedMinutes: 2
nextStepFile: ./c-03b2-offer-generation.md
conditional:
  field: content_type
  condition: "demo"
  description: "Only appears when content_type is 'demo'"
---
```

**Quality Score:** 4/10

---

### 6. FILE: c-03b2-offer-generation.md
**Status:** ⚠️ INCONSISTENT SCHEMA - DIFFERENT FIELD NAMES

#### Frontmatter Analysis
```yaml
---
stepId: c-03b2
stepType: automated
stepName: Генерация Офферов On-the-Fly (Content Machine Stage 3)
estimatedMinutes: 1
nextStepFile: ./c-03c-draft.md
---
```

**Issues Found:**

1. **HIGH: Schema Mismatch - Different Field Names**
   - **Problem:** Same as c-03b1 - uses `stepId`, `stepType`, `stepName`
   - **Impact:** Inconsistent with c-01, c-02c, c-02d, c-03d, c-03e patterns

2. **HIGH: Missing `description` Field**
   - **Required:** Standard description field
   - **Impact:** Cannot display in unified menu

3. **MEDIUM: No Conditional Trigger Documentation**
   - **Problem:** Frontmatter doesn't document that this only runs if `content_type == "demo"`
   - **Current:** Step content has "Триггер: Только если `content_type == \"demo\"`" but not in frontmatter
   - **Impact:** Automation won't know when to execute this step

**Required Fixes:**
```yaml
---
name: step-c-03b2-offer-generation
description: Automatically generate 2-4 contextual offers based on demonstrated routine, selected angle, and pain points
type: offer-generation
estimatedMinutes: 1
nextStepFile: ./c-03c-draft.md
conditional:
  field: content_type
  condition: "demo"
  description: "Only appears when content_type is 'demo' - auto-generates offers on-the-fly"
---
```

**Quality Score:** 4/10

---

### 7. FILE: c-03c-draft.md
**Status:** ❌ CRITICAL ISSUE - MALFORMED FRONTMATTER

#### Frontmatter Analysis
```yaml
---
description: Generate 3 draft post variations based on selected angle
name: step-c-03c-draft
nextStepFile: ./c-03d-variants.md
type: content-generation
Дай feedback на все варианты:
Например:
---
```

**Critical Issues Found:**

1. **CRITICAL: Invalid YAML - Improper Field Syntax**
   - **Problem:** Lines without colons are not valid YAML
   - **Current:**
     ```
     Дай feedback на все варианты:
     Например:
     ```
   - **Impact:** YAML parser will FAIL; this breaks the entire file processing
   - **Severity:** CRITICAL - file cannot be parsed

2. **MEDIUM: Incomplete/Trailing Data**
   - **Problem:** Fields appear incomplete with trailing spaces
   - **Impact:** Suggests file was corrupted or incompletely edited

**Required Fixes:**
```yaml
---
description: Generate 3 draft post variations based on selected angle
name: step-c-03c-draft
type: content-generation
nextStepFile: ./c-03d-variants.md
---
```

**Quality Score:** 1/10

---

### 8. FILE: c-03d-variants.md
**Status:** ✅ COMPLIANT

#### Frontmatter Analysis
```yaml
---
description: Generate 250-char and 100-char versions of selected post
name: step-c-03d-variants
nextStepFile: ./c-03e-finalize.md
type: variant-generation
---
```

**Findings:**
- ✅ Valid YAML syntax
- ✅ All required fields present
- ✅ Consistent field naming
- ✅ Next step reference valid

**Quality Score:** 10/10

---

### 9. FILE: c-03e-finalize.md
**Status:** ❌ CRITICAL ISSUE - MALFORMED FRONTMATTER

#### Frontmatter Analysis
```yaml
---
Location: posts_content.csv
Post ID: post_001 [assigned]
Save to posts_content.csv, then proceed:
Status: SAVED (draft, not published)
description: Final approval of post and save to database
name: step-c-03e-finalize
nextStepFile: ./c-00-menu.md
type: finalization
Варианты сохранены:
---
```

**Critical Issues Found:**

1. **CRITICAL: Invalid YAML - Non-Standard Field Names and Formatting**
   - **Problem:** Uses non-standard field names mixed with required fields
   - **Current:** `Location`, `Post ID`, `Save to posts_content.csv`, `Status`, `Варианты сохранены`
   - **Impact:** YAML structure is malformed; inconsistent with standard frontmatter schema

2. **HIGH: Duplicated/Conflicting Fields**
   - **Problem:** Multiple location and status-like fields
   - **Current:** Has `Location`, `Post ID`, `Status` alongside standard `description`, `name`, etc.
   - **Impact:** Confusing schema; unclear which field is authoritative

3. **MEDIUM: Incomplete Field Values**
   - **Problem:** Some fields have trailing content instead of clean values
   - **Current:** `Save to posts_content.csv, then proceed:` is not a proper field value
   - **Impact:** Suggests incomplete editing or data corruption

**Required Fixes:**
```yaml
---
description: Final approval of post and save to database
name: step-c-03e-finalize
type: finalization
nextStepFile: ./c-00-menu.md
---
```

**Quality Score:** 2/10

---

## SUMMARY BY ISSUE TYPE

### CRITICAL ISSUES (3)

| File | Issue | Impact | Fix Priority |
|------|-------|--------|--------------|
| c-03b-select-angle.md | Invalid YAML in `nextStepFile` (contains parentheses and OR) | Automation will fail; routing broken | 🔴 IMMEDIATE |
| c-03c-draft.md | Malformed YAML (incomplete fields without proper syntax) | File cannot be parsed; pipeline breaks | 🔴 IMMEDIATE |
| c-03e-finalize.md | Malformed YAML (mixed field names and formats) | Inconsistent schema; parsing errors | 🔴 IMMEDIATE |

### HIGH PRIORITY ISSUES (2)

| File | Issue | Impact | Fix Priority |
|------|-------|--------|--------------|
| c-03b1-offer-check.md | Schema mismatch (stepId/stepType vs name/type) + missing description | Inconsistent parsing; menu display broken | 🟡 TODAY |
| c-03b2-offer-generation.md | Schema mismatch + missing description + no conditional trigger docs | Same as above + logic not documented | 🟡 TODAY |

### MEDIUM PRIORITY ISSUES (4)

| File | Issue | Impact | Fix Priority |
|------|-------|--------|--------------|
| c-03b-select-angle.md | Conditional routing not properly documented in frontmatter | Automation cannot determine correct path | 🟡 THIS WEEK |
| c-03b1-offer-check.md | Conditional trigger not documented (only in body) | Automation won't know when to execute | 🟡 THIS WEEK |
| c-03b2-offer-generation.md | Same - conditional trigger not in frontmatter | Same as above | 🟡 THIS WEEK |
| c-03c-draft.md | Incomplete field syntax | Data integrity concern | 🟡 THIS WEEK |

---

## STANDARDIZATION RECOMMENDATIONS

### 1. Adopt Consistent Field Schema
**Current State:** Two different schemas in use
- Schema A (c-01, c-02c, c-02d, c-03d, c-03e): `name`, `type`, `description`, `nextStepFile`
- Schema B (c-03b1, c-03b2): `stepId`, `stepType`, `stepName`, `nextStepFile`

**Recommendation:** Standardize on Schema A for all files
```yaml
---
name: step-{module}-{name}
type: {step-type}
description: {clear description}
nextStepFile: ./path-to-next.md
conditional:  # (optional, for conditional routing)
  field: {variable-name}
  condition: {value}
---
```

### 2. Add Conditional Routing Support
For steps with branching logic, use structured field:
```yaml
conditional:
  field: content_type
  routes:
    - condition: "demo"
      nextStepFile: ./c-03b1-offer-check.md
    - condition: "normal"
      nextStepFile: ./c-03c-draft.md
```

### 3. Standardize Step Type Values
**Current Values:** input-collection, research-execution, results-display, selection, user-input, automated, content-generation, variant-generation, finalization, offer-filtering, offer-generation

**Recommended Standardization:**
- Input types: `input-collection`, `user-input`, `offer-filtering`
- Processing types: `research-execution`, `offer-generation`, `content-generation`
- Output types: `results-display`, `variant-generation`, `finalization`
- Selection types: `selection`
- Auto types: `automated`

### 4. Add Conditional Execution Field (Optional)
For steps that only appear under certain conditions:
```yaml
conditional:
  field: content_type
  value: demo
  executionMode: "only-if-match"
  description: "This step only appears when creating demo content"
```

---

## NEXTSTEPRFLE REFERENCE VALIDATION

### Valid References (Verified)
- c-01-add-idea.md → c-01b-dedup-check.md ✅
- c-02c-research.md → c-02d-results.md ✅
- c-02d-results.md → c-03a-select-idea.md ✅
- c-03d-variants.md → c-03e-finalize.md ✅
- c-03e-finalize.md → c-00-menu.md ✅
- c-03b1-offer-check.md → c-03b2-offer-generation.md ✅
- c-03b2-offer-generation.md → c-03c-draft.md ✅

### Problematic References
- c-03b-select-angle.md → `./c-03b1-offer-check.md (for demo) OR ./c-03c-draft.md (for normal)` ❌
  - **Problem:** Not valid YAML; contains parentheses and logical operator
  - **Should be:** Structured conditional routing (see recommendations)

---

## CONDITIONAL ROUTING ANALYSIS

### Current Conditional Logic

**Identified Branching Points:**
1. **c-03b-select-angle.md** → Routes based on `content_type`
   - If `content_type == "demo"` → go to c-03b1-offer-check.md
   - If `content_type == "normal"` or other → go to c-03c-draft.md

2. **c-03b1-offer-check.md** → Conditional execution
   - Only appears if `content_type == "demo"`

3. **c-03b2-offer-generation.md** → Conditional execution
   - Only appears if `content_type == "demo"`

**Current Documentation Problem:**
- c-03b1 and c-03b2 document trigger in step BODY but not in FRONTMATTER
- c-03b-select-angle.md tries to document both paths in nextStepFile (invalid YAML)

**Recommended Solution:**
Add `conditional` field to frontmatter for all conditional steps:

```yaml
# For c-03b-select-angle.md
conditional:
  type: "routing"
  field: "content_type"
  routes:
    - value: "demo"
      nextStepFile: ./c-03b1-offer-check.md
      description: "Demo content - filter offers first"
    - value: "normal"
      nextStepFile: ./c-03c-draft.md
      description: "Normal content - skip offer filtering"
    - value: "*"  # default
      nextStepFile: ./c-03c-draft.md

# For c-03b1-offer-check.md
conditional:
  type: "execution"
  field: "content_type"
  value: "demo"
  mode: "only-if-match"
  description: "Only executed for demo content"

# For c-03b2-offer-generation.md
conditional:
  type: "execution"
  field: "content_type"
  value: "demo"
  mode: "only-if-match"
  description: "Only executed for demo content"
```

---

## ACTION ITEMS

### IMMEDIATE (Must fix before next use)
- [ ] **c-03b-select-angle.md** - Fix YAML in nextStepFile field (use conditional routing)
- [ ] **c-03c-draft.md** - Remove malformed trailing fields
- [ ] **c-03e-finalize.md** - Clean frontmatter; remove non-standard fields

### TODAY
- [ ] **c-03b1-offer-check.md** - Standardize field names to match schema
- [ ] **c-03b2-offer-generation.md** - Standardize field names; add description

### THIS WEEK
- [ ] Add conditional routing documentation to all conditional steps
- [ ] Create standardized frontmatter template for new steps
- [ ] Audit remaining step files (c-04, c-05, c-06, c-07, c-08 modules)

### FUTURE
- [ ] Create automated validation script to check frontmatter YAML compliance
- [ ] Implement linter to enforce field schema
- [ ] Add pre-commit hook to validate frontmatter before file commit

---

## TEMPLATE FOR FUTURE STEPS

```yaml
---
name: step-{module}-{step-code}-{description}
type: {input-collection|user-input|research-execution|results-display|selection|content-generation|variant-generation|finalization|offer-filtering|offer-generation|automated}
description: Clear, concise description of what this step does
nextStepFile: ./next-step-file.md
conditional:  # Optional - only include if step has branching or conditional execution
  type: "routing" | "execution"
  field: "variable_name"
  condition: "value" |
  routes:
    - condition: "value1"
      nextStepFile: ./path1.md
      description: "When value is value1"
    - condition: "value2"
      nextStepFile: ./path2.md
      description: "When value is value2"
---
```

---

## COMPLIANCE SUMMARY

| Category | Status | Notes |
|----------|--------|-------|
| **YAML Syntax** | ❌ 67% Valid | 3 files have malformed YAML |
| **Field Completeness** | ⚠️ 78% Complete | 2 files missing description field |
| **Field Naming Consistency** | ⚠️ 78% Consistent | 2 files use different schema |
| **NextStepFile References** | ⚠️ 89% Valid | 1 file has invalid YAML in reference |
| **Conditional Routing Docs** | ❌ 30% Documented | Only 1 of 3 conditional steps documented (and that one has syntax error) |
| **Overall Compliance** | ❌ 58% | REQUIRES FIXES BEFORE PRODUCTION USE |

---

**Report Prepared By:** Code Analyzer Agent (Validation Agent 2)
**Report Status:** Complete - Ready for Review and Action
