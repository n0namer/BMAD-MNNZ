# FRONTMATTER VALIDATION - TECHNICAL FINDINGS
## Deep Dive Analysis for Developers

**Analysis Date:** 2026-01-30
**Focus:** YAML syntax, schema consistency, conditional routing implementation
**Audience:** Developers, Pipeline Architects

---

## TABLE OF CONTENTS

1. [YAML Syntax Issues](#yaml-syntax-issues)
2. [Schema Design Problems](#schema-design-problems)
3. [Conditional Routing Architecture](#conditional-routing-architecture)
4. [NextStepFile Routing](#nextstepfile-routing)
5. [Recommended Data Model](#recommended-data-model)
6. [Implementation Examples](#implementation-examples)
7. [Automation Implications](#automation-implications)

---

## YAML SYNTAX ISSUES

### Issue A: Invalid YAML in String Values

**File:** `c-03b-select-angle.md`

**Symptom:** YAML parser fails with syntax error

**Root Cause:**
```yaml
nextStepFile: ./c-03b1-offer-check.md (for demo) OR ./c-03c-draft.md (for normal)
```

This is not valid YAML because:
- The value contains unquoted text with parentheses
- The value contains an unescaped logical operator `OR`
- YAML parser interprets `(for` as a separate token

**Why It Failed:**
```
YAML Parser sees:
├─ key: nextStepFile
├─ value: ./c-03b1-offer-check.md
├─ (unexpected token): (
├─ unexpected text: for demo
├─ unexpected operator: OR
└─ Expected: end of line after value
```

**Correct Solutions:**

Option 1: Quote the entire value
```yaml
nextStepFile: "./c-03b1-offer-check.md (for demo) OR ./c-03c-draft.md (for normal)"
```
Problem: Parser can't use this as a file path; automation can't determine which file to use.

Option 2: Use array of objects (Recommended)
```yaml
conditional:
  type: "routing"
  routes:
    - condition: "demo"
      nextStepFile: ./c-03b1-offer-check.md
    - condition: "normal"
      nextStepFile: ./c-03c-draft.md
```
Benefit: Parser can deterministically choose the correct path based on condition evaluation.

---

### Issue B: Fields Without Values

**File:** `c-03c-draft.md`

**Symptom:** YAML parsing error or unexpected behavior

**Root Cause:**
```yaml
Дай feedback на все варианты:
Например:
```

These lines have colons but no values. In YAML:
- `:` followed by nothing = `null` value
- Trailing space doesn't change this
- Next line starting with text is unexpected

**Why It Failed:**
```
YAML Parser sees:
├─ key: "Дай feedback на все варианты"
├─ value: null (nothing after colon)
├─ key: "Например"
├─ value: null
└─ Result: Document has unexpected null fields
```

**Correct Solution:**
Remove these lines entirely. If the text is important:
```yaml
---
description: Generate 3 draft post variations based on selected angle
name: step-c-03c-draft
type: content-generation
nextStepFile: ./c-03d-variants.md
---

## Feedback Instructions

Дай feedback на все варианты:
Например:
```

Move content to file body, after frontmatter.

---

### Issue C: Mixed Field Semantics

**File:** `c-03e-finalize.md`

**Symptom:** Schema inconsistency; parser must handle multiple field interpretations

**Root Cause:**
```yaml
Location: posts_content.csv
Post ID: post_001 [assigned]
Save to posts_content.csv, then proceed:
Status: SAVED (draft, not published)
description: Final approval of post and save to database
```

These lines mix:
- **Metadata fields** (Location, Status) with **standard fields** (description, nextStepFile)
- **Imperative instructions** ("Save to...") mixed with **declarative structure**
- **Different naming conventions** (camelCase, SCREAMING_SNAKE_CASE, imperative phrases)

**Why It Failed:**
```
YAML Parser success: Technically valid YAML
Semantic failure: Multiple interpretations of field purposes
├─ Is "Location" metadata or a reference?
├─ Is "Status" a fixed value or dynamic?
├─ Is "Save to..." an instruction or documentation?
└─ Which fields are authoritative?
```

**Correct Solution:**
Keep only the standardized fields:
```yaml
---
description: Final approval of post and save to database
name: step-c-03e-finalize
type: finalization
nextStepFile: ./c-00-menu.md
---
```

If metadata is needed, add a separate structured section:
```yaml
---
description: Final approval of post and save to database
name: step-c-03e-finalize
type: finalization
nextStepFile: ./c-00-menu.md
metadata:
  outputLocation: posts_content.csv
  outputStatus: draft
---
```

---

## SCHEMA DESIGN PROBLEMS

### Problem 1: Two Conflicting Schema Versions

**Schema A (Used in: c-01, c-02c, c-02d, c-03d, c-03e, expected everywhere)**
```yaml
name: {identifier}
type: {step-type}
description: {text}
nextStepFile: {path}
```

**Schema B (Used in: c-03b1, c-03b2, non-standard)**
```yaml
stepId: {identifier}
stepType: {step-type}
stepName: {text}
estimatedMinutes: {number}
nextStepFile: {path}
```

**Conflict Analysis:**

| Field | Schema A | Schema B | Difference |
|-------|----------|----------|------------|
| Step ID | `name: step-c-03b1` | `stepId: c-03b1` | Naming convention differs; prefix "step-" |
| Step Type | `type: offer-filtering` | `stepType: user-input` | Same concept, different field name |
| Description | `description: "text"` | `stepName: "Фильтр Офферов..."` | Same purpose, different field name |
| Metadata | Missing | `estimatedMinutes: 2` | Schema B has extra field |

**Impact on Automation:**

```javascript
// Code expecting Schema A fails for Schema B
function getStepName(frontmatter) {
  return frontmatter.name;  // Returns undefined for Schema B!
}

// Code must detect schema version
function getStepName(frontmatter) {
  if (frontmatter.name) return frontmatter.name;          // Schema A
  if (frontmatter.stepName) return frontmatter.stepName;  // Schema B
  throw new Error("Unknown schema!");
}
```

**Better Solution:** Standardize on one schema with optional fields

```yaml
---
name: step-c-03b1-offer-check
type: offer-filtering
description: Filter and configure which offer types to generate for demo content
nextStepFile: ./c-03b2-offer-generation.md
estimatedMinutes: 2  # Optional field that can be added anywhere
---
```

---

### Problem 2: Missing Description Field in Schema B

**Files Affected:** c-03b1-offer-check.md, c-03b2-offer-generation.md

**Issue:** Schema B uses `stepName` for a long, Russian-language title instead of English description

**Current:**
```yaml
stepName: Фильтр Офферов — "Мне Не Лень?" (Content Machine Stage 4)
```

**Problem:**
1. Not translatable for English-speaking users
2. Too long for UI menu display
3. Mixes descriptive text with UI labels ("Stage 4")
4. Doesn't follow standard field naming

**Solution:**

```yaml
---
name: step-c-03b1-offer-check
type: offer-filtering
description: Filter and configure which offer types to generate for demo content  # English, clear
stepName: Фильтр Офферов — "Мне Не Лень?"  # Optional: Russian display name
stage: 4  # Optional: Extract stage number separately
---
```

Or simply use the standard schema:

```yaml
---
name: step-c-03b1-offer-check
type: offer-filtering
description: Filter and configure which offer types to generate for demo content
nextStepFile: ./c-03b2-offer-generation.md
---
```

---

### Problem 3: Missing Conditional Trigger Documentation

**Files Affected:** c-03b1-offer-check.md, c-03b2-offer-generation.md

**Current State:** Triggers documented in step BODY, not in FRONTMATTER

**From c-03b1-offer-check.md body:**
```
**Триггер:** Только если `content_type == "demo"` (режим [R] в c-01)
```

**Problem:**
- Documentation is in step content, not machine-parseable frontmatter
- Automation cannot determine when to execute this step
- Step appears in all pipelines, not conditionally

**Solution:** Add conditional field to frontmatter

```yaml
---
name: step-c-03b1-offer-check
type: offer-filtering
description: Filter and configure which offer types to generate for demo content
nextStepFile: ./c-03b2-offer-generation.md
conditional:
  type: "execution"
  field: "content_type"
  condition: "demo"
  mode: "only-if-match"
  description: "Only executed when content_type is 'demo'"
---
```

---

## CONDITIONAL ROUTING ARCHITECTURE

### Current State: Ad Hoc Routing

**Problem:** Conditional logic exists but is not formally structured

**Current Implementation (Broken):**
```yaml
nextStepFile: ./c-03b1-offer-check.md (for demo) OR ./c-03c-draft.md (for normal)
```

**Issues:**
1. Not parseable YAML
2. No deterministic routing algorithm
3. No formal decision tree
4. No default/fallback handling

---

### Proposed Solution 1: Inline Conditional Routing

**Design:** Include routing rules in frontmatter

```yaml
---
name: step-c-03b-select-angle
type: selection
description: User selects which angle (from research) to use for the post
conditional:
  type: "routing"
  field: "content_type"
  routes:
    - condition: "demo"
      nextStepFile: ./c-03b1-offer-check.md
      description: "Demo content - filter offers first"
      priority: 1
    - condition: "normal"
      nextStepFile: ./c-03c-draft.md
      description: "Normal content - skip offer filtering"
      priority: 2
    - condition: "*"  # Default/wildcard
      nextStepFile: ./c-03c-draft.md
      description: "Default - proceed to draft"
      priority: 3
---
```

**Routing Algorithm:**

```javascript
function getNextStep(frontmatter, context) {
  if (!frontmatter.conditional || frontmatter.conditional.type !== "routing") {
    // No conditional routing
    return frontmatter.nextStepFile;
  }

  const { field, routes } = frontmatter.conditional;
  const value = context[field];

  // Find matching route
  for (const route of routes.sort((a,b) => a.priority - b.priority)) {
    if (route.condition === "*" || route.condition === value) {
      return route.nextStepFile;
    }
  }

  throw new Error(`No matching route for ${field}=${value}`);
}

// Usage:
const nextStep = getNextStep(
  c03bFrontmatter,
  { content_type: "demo" }  // From user's c-01 choice
);
// Returns: "./c-03b1-offer-check.md"
```

**Advantages:**
- ✅ Formal, parseable structure
- ✅ Clear priority/priority handling
- ✅ Default case supported
- ✅ Extensible to multiple conditions

---

### Proposed Solution 2: Conditional Execution

**Design:** Separate execution control from next-step routing

**For steps that only execute under certain conditions:**

```yaml
---
name: step-c-03b1-offer-check
type: offer-filtering
description: Filter and configure which offer types to generate for demo content
nextStepFile: ./c-03b2-offer-generation.md
conditional:
  type: "execution"
  field: "content_type"
  condition: "demo"
  mode: "only-if-match"
  description: "This step only runs when content_type is 'demo'"
---
```

**Execution Algorithm:**

```javascript
function shouldExecute(frontmatter, context) {
  if (!frontmatter.conditional || frontmatter.conditional.type !== "execution") {
    return true;  // Execute by default
  }

  const { field, condition, mode } = frontmatter.conditional;
  const value = context[field];

  if (mode === "only-if-match") {
    return value === condition;
  }
  if (mode === "skip-if-match") {
    return value !== condition;
  }

  throw new Error(`Unknown execution mode: ${mode}`);
}

// Usage:
if (shouldExecute(c03b1Frontmatter, { content_type: "demo" })) {
  executeStep(c03b1Frontmatter);
  nextStep = c03b1Frontmatter.nextStepFile;  // "./c-03b2-offer-generation.md"
} else {
  // Skip this step
  nextStep = c03bFrontmatter.nextStepFile;  // "./c-03c-draft.md"
}
```

**Advantages:**
- ✅ Separates execution control from routing
- ✅ Can skip steps without creating branch point
- ✅ Multiple skip modes (only-if-match, skip-if-match)

---

### Complete Workflow with Both Types

**Example: Full content_type branching**

```
START: c-03b-select-angle
  ├─ CONDITIONAL ROUTING (field: content_type)
  │
  ├─ IF content_type == "demo":
  │   │
  │   ├─ EXECUTE: c-03b1-offer-check
  │   │   └─ CONDITIONAL EXECUTION (only-if-match: demo)
  │   │
  │   ├─ EXECUTE: c-03b2-offer-generation
  │   │   └─ CONDITIONAL EXECUTION (only-if-match: demo)
  │   │
  │   └─ NEXT: c-03c-draft
  │
  ├─ IF content_type == "normal":
  │   │
  │   ├─ SKIP: c-03b1-offer-check (condition not met)
  │   ├─ SKIP: c-03b2-offer-generation (condition not met)
  │   │
  │   └─ NEXT: c-03c-draft
  │
  └─ DEFAULT:
      └─ NEXT: c-03c-draft
```

**Implementation:**

```javascript
// Step: c-03b-select-angle
async function executeC03b(context) {
  // ... user selects angle ...

  // Determine next step based on content_type
  const nextStepPath = getNextStep(
    c03bFrontmatter,
    context  // Contains content_type
  );

  return loadAndExecuteStep(nextStepPath, context);
}

// Generic step executor
async function executeStep(stepFrontmatter, context) {
  // Check if step should execute
  if (!shouldExecute(stepFrontmatter, context)) {
    console.log(`Skipping ${stepFrontmatter.name} (condition not met)`);
    // Jump to next step
    return executeStep(
      loadStep(stepFrontmatter.nextStepFile),
      context
    );
  }

  // Execute the step
  console.log(`Executing ${stepFrontmatter.name}`);
  // ... step logic ...

  // Proceed to next step
  const nextStepPath = stepFrontmatter.nextStepFile;
  const nextStepFrontmatter = loadStep(nextStepPath);

  return executeStep(nextStepFrontmatter, context);
}
```

---

## NEXTSTEPFILE ROUTING

### Current State Analysis

**Valid References:**
- c-01-add-idea.md → c-01b-dedup-check.md ✅
- c-02c-research.md → c-02d-results.md ✅
- c-02d-results.md → c-03a-select-idea.md ✅
- c-03d-variants.md → c-03e-finalize.md ✅
- c-03e-finalize.md → c-00-menu.md ✅ (loops back)
- c-03b1-offer-check.md → c-03b2-offer-generation.md ✅
- c-03b2-offer-generation.md → c-03c-draft.md ✅

**Invalid References:**
- c-03b-select-angle.md → `./c-03b1-offer-check.md (for demo) OR ./c-03c-draft.md (for normal)` ❌

**Analysis:**

All references use relative paths with `./` prefix. This is good for:
- Portable step files (can move directories)
- Consistent file resolution
- No hardcoded absolute paths

**Recommendation:** Keep relative path convention, but validate that referenced files exist.

---

### NextStepFile Resolution Algorithm

```javascript
function resolveNextStep(relativeStep, currentFileDir) {
  // Example:
  // relativeStep: "./c-03b1-offer-check.md"
  // currentFileDir: "D:\\...\\steps-c"

  const path = require('path');
  const absPath = path.resolve(currentFileDir, relativeStep);

  if (!fs.existsSync(absPath)) {
    throw new Error(`Next step file not found: ${absPath}`);
  }

  return absPath;
}
```

**Validation Checklist:**
- [ ] Path uses relative notation (./filename.md)
- [ ] Referenced file exists
- [ ] No circular references (except back to menu)
- [ ] File is in steps-c directory (same level)

---

## RECOMMENDED DATA MODEL

### Standard Step Frontmatter Schema

```typescript
interface StepFrontmatter {
  // Required
  name: string;              // step-{code}
  type: StepType;            // One of predefined types
  description: string;       // English, concise
  nextStepFile: string;      // Path to next step (relative)

  // Optional
  estimatedMinutes?: number;      // Time estimate
  conditional?: ConditionalLogic; // Routing/execution conditions
  metadata?: Record<string, any>; // Custom metadata
}

type StepType =
  | "input-collection"      // Collect user input
  | "user-input"            // Single user input field
  | "offer-filtering"       // Filter/configure options
  | "offer-generation"      // Auto-generate offers
  | "research-execution"    // Execute research
  | "results-display"       // Display results
  | "selection"             // User selects from options
  | "content-generation"    // Generate content
  | "variant-generation"    // Generate variants
  | "finalization"          // Final step before completion
  | "automated";            // Automatic step (no user input)

interface ConditionalLogic {
  type: "routing" | "execution";

  // For routing type
  field?: string;           // Variable to check
  routes?: Route[];         // Decision tree

  // For execution type
  condition?: string;       // Single condition value
  mode?: "only-if-match" | "skip-if-match";

  description?: string;     // Human-readable explanation
}

interface Route {
  condition: string;        // Value to match (or "*" for default)
  nextStepFile: string;     // Where to go if matched
  description?: string;     // Explanation
  priority?: number;        // Route priority (lower = higher priority)
}
```

### YAML Representation

```yaml
---
name: step-c-03b-select-angle
type: selection
description: User selects which angle (from research) to use for the post
nextStepFile: ./c-03c-draft.md
estimatedMinutes: 2
conditional:
  type: "routing"
  field: "content_type"
  description: "Route to offer filtering if demo content, otherwise to draft"
  routes:
    - condition: "demo"
      nextStepFile: ./c-03b1-offer-check.md
      description: "Demo content - filter offers first"
      priority: 1
    - condition: "normal"
      nextStepFile: ./c-03c-draft.md
      description: "Normal content - skip offer filtering"
      priority: 2
    - condition: "*"
      nextStepFile: ./c-03c-draft.md
      description: "Default fallback"
      priority: 99
---
```

---

## IMPLEMENTATION EXAMPLES

### Example 1: Simple Linear Step

```yaml
---
name: step-c-02c-research
type: research-execution
description: Execute research - find 5-8 angles with sources and facts
nextStepFile: ./c-02d-results.md
estimatedMinutes: 15
---
```

**Parser Code:**
```javascript
const frontmatter = parseYAML(fileContent);
const nextStep = frontmatter.nextStepFile;  // "./c-02d-results.md"
```

---

### Example 2: Conditional Routing

```yaml
---
name: step-c-03b-select-angle
type: selection
description: User selects which angle to develop
nextStepFile: ./c-03c-draft.md
conditional:
  type: "routing"
  field: "content_type"
  routes:
    - condition: "demo"
      nextStepFile: ./c-03b1-offer-check.md
      priority: 1
    - condition: "*"
      nextStepFile: ./c-03c-draft.md
      priority: 99
---
```

**Parser Code:**
```javascript
function getNextStep(frontmatter, context) {
  if (!frontmatter.conditional) {
    return frontmatter.nextStepFile;
  }

  if (frontmatter.conditional.type === "routing") {
    const { field, routes } = frontmatter.conditional;
    const value = context[field];

    const route = routes
      .sort((a,b) => a.priority - b.priority)
      .find(r => r.condition === "*" || r.condition === value);

    return route?.nextStepFile || frontmatter.nextStepFile;
  }

  return frontmatter.nextStepFile;
}

const nextStep = getNextStep(frontmatter, { content_type: "demo" });
// Returns: "./c-03b1-offer-check.md"
```

---

### Example 3: Conditional Execution

```yaml
---
name: step-c-03b1-offer-check
type: offer-filtering
description: Filter which offer types to generate for demo content
nextStepFile: ./c-03b2-offer-generation.md
conditional:
  type: "execution"
  field: "content_type"
  condition: "demo"
  mode: "only-if-match"
---
```

**Parser Code:**
```javascript
function shouldExecute(frontmatter, context) {
  if (!frontmatter.conditional) return true;

  if (frontmatter.conditional.type === "execution") {
    const { field, condition, mode } = frontmatter.conditional;
    const value = context[field];

    if (mode === "only-if-match") {
      return value === condition;
    }
    if (mode === "skip-if-match") {
      return value !== condition;
    }
  }

  return true;  // Default: execute
}

if (shouldExecute(frontmatter, { content_type: "demo" })) {
  // Execute step
} else {
  // Skip to next step
  context.nextStep = frontmatter.nextStepFile;
}
```

---

## AUTOMATION IMPLICATIONS

### Pipeline Automation Requirements

**To automate the pipeline, the system must be able to:**

1. **Parse frontmatter**
   - ✅ Valid YAML syntax (currently broken in 3 files)
   - ✅ Required fields present
   - ⚠️ Optional conditional fields documented

2. **Route between steps**
   - ✅ Resolve relative file paths
   - ❌ Handle conditional routing (not documented)
   - ❌ Handle conditional execution (not documented)

3. **Display menus**
   - ✅ Extract step name and description
   - ⚠️ Support different schema versions
   - ❌ Explain conditional routing to users

4. **Track context**
   - ❓ Maintain state (content_type, user choices)
   - ❓ Save/restore session state
   - ❓ Track user history through pipeline

### Current Blockers

| Blocker | Impact | Status |
|---------|--------|--------|
| Invalid YAML in 3 files | Cannot parse files | 🔴 Critical |
| Schema mismatch | Cannot unify parser logic | 🟡 High |
| Conditional routing not documented | Cannot auto-route based on content_type | 🟡 High |
| Conditional execution not documented | Cannot skip steps conditionally | 🟡 High |

### Required Changes for Full Automation

1. **Fix YAML Syntax** (3 files)
   ```
   Effort: 15 minutes
   Impact: Unblocks parsing entirely
   ```

2. **Standardize Schema** (all files)
   ```
   Effort: 30 minutes
   Impact: Enables unified parser
   ```

3. **Document Conditional Routing** (c-03b-select-angle.md)
   ```
   Effort: 10 minutes
   Impact: Enables intelligent routing
   ```

4. **Document Conditional Execution** (c-03b1, c-03b2)
   ```
   Effort: 10 minutes
   Impact: Enables conditional step skipping
   ```

5. **Implement Routing Algorithm** (Pipeline code)
   ```
   Effort: 1-2 hours (dev time)
   Impact: Fully automated conditional pipeline
   ```

**Total Effort:** ~2.5-3 hours for full automation capability

---

## VALIDATION CHECKLIST FOR NEW STEPS

When creating new step files, use this checklist:

```markdown
### Frontmatter Validation Checklist

- [ ] File starts with `---`
- [ ] All required fields present: name, type, description, nextStepFile
- [ ] Field names are lowercase with hyphens (name, not Name)
- [ ] All field values are properly quoted/escaped
- [ ] No fields without values (no trailing colons without values)
- [ ] File ends with `---` on clean line
- [ ] nextStepFile points to existing step (verified)
- [ ] No circular references (except back to menu)
- [ ] Type is one of: input-collection, user-input, selection, content-generation, etc.
- [ ] Description is English, concise (under 80 characters)
- [ ] If conditional routing: conditional.type = "routing" with routes array
- [ ] If conditional execution: conditional.type = "execution" with condition+mode
- [ ] All YAML valid: `python -m yaml filename.md` succeeds
- [ ] Frontmatter can be parsed: `js-yaml.load(fs.readFileSync(filename))`

### YAML Validation Command

```bash
# Python
python -m yaml steps-c/filename.md

# Node.js (quick test)
node -e "const yaml = require('js-yaml'); const fs = require('fs'); console.log(yaml.load(fs.readFileSync('steps-c/filename.md')))"

# jq (pretty print)
cat steps-c/filename.md | yq eval '.  steps-c/filename.md'
```
```

---

**Report Prepared By:** Code Analyzer Agent (Deep Technical Analysis)
**Technical Review:** Required before implementation
**Next Step:** Execute fixes and implement routing algorithm
