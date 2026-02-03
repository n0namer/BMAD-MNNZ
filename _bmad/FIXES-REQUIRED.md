# REQUIRED FIXES: v-00-load-style.md

**Generated:** 2026-01-30
**Validated File:** `steps-v/v-00-load-style.md` (lines 1-297)
**Status:** Critical issues found and documented

---

## ⛔ CRITICAL ISSUE #1: Wrong nextStepFile

### Location
**File:** `steps-v/v-00-load-style.md`
**Line:** 5
**Field:** `nextStepFile`

### Current State
```yaml
nextStepFile: ./v-01-consistency-check.md
```

### Problem
- File `v-01-consistency-check.md` **DOES NOT EXIST** in `steps-v/` directory
- Workflow will halt when trying to load this file
- Error message: "Cannot load step file ./v-01-consistency-check.md"
- This is a **BLOCKING ERROR** - workflow cannot proceed

### Correct Value
```yaml
nextStepFile: ./v-01a-load.md
```

### Why This Is Correct
- File `v-01a-load.md` **EXISTS** and is verified
- Contains next phase of VALIDATE workflow
- Named correctly: "VALIDATE V-01A: Load Posts for Quality Validation"
- Part of proper pipeline sequence:
  ```
  v-00-load-style.md (current)
    ↓
  v-01a-load.md (next) ← Correct file
    ↓
  v-01b-checks.md
    ↓
  v-01c-report.md
  ```

### How to Fix

#### Option A: Direct Edit (Recommended)
```bash
# Using any text editor
# Open: steps-v/v-00-load-style.md
# Line 5: Change
nextStepFile: ./v-01-consistency-check.md
# To:
nextStepFile: ./v-01a-load.md
# Save file
```

#### Option B: Command Line (Linux/macOS)
```bash
cd "D:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\idea-to-post-pipeline\steps-v"
sed -i 's|nextStepFile: \./v-01-consistency-check\.md|nextStepFile: ./v-01a-load.md|' v-00-load-style.md
```

#### Option C: PowerShell (Windows)
```powershell
$file = "D:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\idea-to-post-pipeline\steps-v\v-00-load-style.md"
(Get-Content $file) -replace 'nextStepFile: \./v-01-consistency-check\.md', 'nextStepFile: ./v-01a-load.md' | Set-Content $file
```

### Verification After Fix
```bash
# Check the fix
grep "nextStepFile" steps-v/v-00-load-style.md
# Should output:
# nextStepFile: ./v-01a-load.md
```

### Impact If Not Fixed
- **Severity:** 🔴 CRITICAL
- **Error Type:** BLOCKING
- **Impact:** Workflow halts immediately after v-00 completes
- **User Experience:** "File not found" error
- **Recovery:** Manual intervention required

---

## ⚠️ IMPORTANT ISSUE #2: Missing workflow_state.json

### Location
**File:** Missing from workflow root directory
**Expected Path:** `D:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\idea-to-post-pipeline\workflow_state.json`

### Problem
- File **DOES NOT EXIST** but is required by v-00-load-style.md (line 242-262)
- Workflow state cannot be persisted between steps
- Subsequent steps may fail when looking for saved state
- Loss of context if workflow is interrupted

### What Should Be Stored
According to v-00-load-style.md (lines 245-262):
```json
{
  "workflow_id": "idea-to-post-pipeline",
  "session_id": "2026-01-30-validate",
  "currentMode": "VALIDATE",
  "currentStep": "step-validate-00-load-style",
  "stepsCompleted": ["step-validate-00-load-style"],
  "styleGuideLoaded": true,
  "correctionsLoaded": true,
  "validationCriteriaReady": true,
  "context": {
    "styleGuide": { ... },
    "corrections": { ... },
    "validationCriteria": { ... }
  },
  "lastUpdated": "2026-01-30 HH:MM"
}
```

### How to Fix

#### Option A: Create with Initial Empty State
Create file: `workflow_state.json` in workflow root
```json
{
  "workflow_id": "idea-to-post-pipeline",
  "session_id": "",
  "currentMode": "VALIDATE",
  "currentStep": "",
  "stepsCompleted": [],
  "styleGuideLoaded": false,
  "correctionsLoaded": false,
  "validationCriteriaReady": false,
  "context": {},
  "lastUpdated": ""
}
```

#### Option B: Add Auto-Initialization to v-00
Add logic in v-00-load-style.md to create the file if missing:

```markdown
### NEW STEP: Auto-initialize workflow_state.json

IF workflow_state.json does NOT exist:
  1. Create file with initial empty state (shown above)
  2. Log: "Created workflow_state.json"
ELSE:
  1. Load existing workflow_state.json
  2. Verify required fields exist
  3. Update lastUpdated field
```

#### Option C: Initialize via Script
```bash
# Create the file before running workflow
cat > workflow_state.json << 'EOF'
{
  "workflow_id": "idea-to-post-pipeline",
  "session_id": "2026-01-30-validate",
  "currentMode": "VALIDATE",
  "currentStep": "step-validate-00-load-style",
  "stepsCompleted": [],
  "styleGuideLoaded": false,
  "correctionsLoaded": false,
  "validationCriteriaReady": false,
  "context": {},
  "lastUpdated": ""
}
EOF
```

### Verification After Fix
```bash
# Check file exists
test -f workflow_state.json && echo "✅ File exists" || echo "❌ File missing"

# Check JSON syntax
python -m json.tool workflow_state.json > /dev/null && echo "✅ JSON valid"
```

### Impact If Not Fixed
- **Severity:** 🟠 IMPORTANT
- **Error Type:** FUNCTIONAL
- **Impact:** State not persisted, subsequent steps may fail
- **User Experience:** Workflow can execute but loses context
- **Recovery:** Manual state management or step restart

---

## 💡 SUGGESTION #1: Dynamic session_id

### Issue
Session ID is currently hardcoded in template:
```json
"session_id": "2026-01-30-validate"
```

### Problem
- All workflow runs have the same session ID
- Cannot distinguish between separate execution sessions
- Makes debugging and logging difficult
- No timestamp of actual execution

### Recommendation
Generate session_id dynamically when v-00 runs:

#### Implementation Option A: In Execution
```bash
# When step runs, generate:
SESSION_ID=$(date +%Y%m%d-%H%M%S)-validate
# Example: 20260130-143025-validate

# Then save to workflow_state.json:
"session_id": "20260130-143025-validate"
```

#### Implementation Option B: In v-00 Instructions
Add to step execution:
```markdown
### NEW: Generate Session ID

Before Step 1 (Display Loading Message):
1. Get current timestamp: YYYY-MM-DD HH:MM:SS
2. Generate session_id: "{ISO_DATE}-{TIME}-validate"
3. Store in workflow_state.json
```

### Impact If Not Fixed
- **Severity:** 🟡 LOW
- **Error Type:** INFORMATIONAL
- **Impact:** Harder to track workflow executions
- **User Experience:** Works fine, just harder to debug
- **Fix Time:** ~5 minutes

---

## ✅ VERIFICATION CHECKLIST

After making all fixes, verify:

```
FIX #1: nextStepFile (CRITICAL)
  [ ] Line 5 updated to: ./v-01a-load.md
  [ ] File v-01a-load.md exists in steps-v/
  [ ] Can load file without error

FIX #2: workflow_state.json (IMPORTANT)
  [ ] File created in workflow root
  [ ] Contains valid JSON
  [ ] Has all required fields:
      - workflow_id
      - session_id
      - currentMode
      - currentStep
      - stepsCompleted
      - styleGuideLoaded
      - correctionsLoaded
      - validationCriteriaReady
      - context
      - lastUpdated
  [ ] File is readable/writable

FIX #3: session_id (OPTIONAL)
  [ ] session_id is generated dynamically (not hardcoded)
  [ ] Timestamp format: YYYYMMDD-HHMMSS-validate
  [ ] Different value for each workflow run
```

---

## 🧪 TESTING PLAN

### Test 1: Load v-00 Step
```bash
# Attempt to load the step file
# Should parse YAML frontmatter without errors
# Should display loading message in Russian
# Should attempt to load Style Guide and Corrections
```

**Expected:**
```
═══════════════════════════════════════════════════════════
  📚 ЗАГРУЗКА STYLE GUIDE И КОРРЕКТИРОВОК (VALIDATE MODE)...
═══════════════════════════════════════════════════════════
```

### Test 2: Verify Dependencies
```bash
# Check both required files exist
# STYLE-GUIDE-ETALON.md ✅
# CORRECTIONS-DATABASE.md ✅
```

### Test 3: Check workflow_state.json
```bash
# Verify file created and updated after v-00 execution
# Should contain all loaded data
# Should have correct session_id
# Should mark as completed
```

### Test 4: Transition to v-01a
```bash
# v-00 should load v-01a-load.md as next step
# Should NOT attempt to load v-01-consistency-check.md
# Workflow should continue without interruption
```

---

## 📋 PRIORITY MATRIX

```
┌──────────────────────────────────┬──────────┬─────────┐
│ ISSUE                            │ PRIORITY │ TIME    │
├──────────────────────────────────┼──────────┼─────────┤
│ nextStepFile wrong (FIX #1)      │ 🔴 P0    │ 2 min   │
│ workflow_state.json missing (#2) │ 🟠 P1    │ 5 min   │
│ Dynamic session_id (FIX #3)      │ 🟡 P2    │ 5 min   │
├──────────────────────────────────┼──────────┼─────────┤
│ TOTAL TIME TO PRODUCTION         │          │ 12 min  │
│ + Testing & Verification         │          │ 10 min  │
│ TOTAL WITH TESTING               │          │ 22 min  │
└──────────────────────────────────┴──────────┴─────────┘
```

---

## 🚀 DEPLOYMENT STEPS

### Step 1: Fix Critical Issue (2 min)
```bash
# Edit v-00-load-style.md line 5
# nextStepFile: ./v-01-consistency-check.md → ./v-01a-load.md
# Save file
```

### Step 2: Create workflow_state.json (5 min)
```bash
# Create workflow_state.json in workflow root
# Copy template from above
# Verify JSON syntax
```

### Step 3: Test Step Transition (10 min)
```bash
# Run v-00-load-style.md
# Verify it loads Style Guide and Corrections
# Verify it transitions to v-01a-load.md
# Verify no errors
```

### Step 4: Update Documentation (5 min)
```bash
# If needed, update workflow documentation
# Add notes about workflow_state.json initialization
# Document session_id format
```

### Step 5: Commit Changes
```bash
git add steps-v/v-00-load-style.md workflow_state.json
git commit -m "fix: correct nextStepFile reference and initialize workflow state"
```

---

## 📌 SUMMARY

| Aspect | Status | Details |
|--------|--------|---------|
| **Critical Issues** | 1 | nextStepFile wrong |
| **Important Issues** | 1 | workflow_state.json missing |
| **Suggestions** | 1 | dynamic session_id |
| **Production Ready** | ⚠️ NO | After fixes: ✅ YES |
| **Time to Fix** | ~20 min | With testing |
| **Complexity** | 🟢 LOW | Text changes only |
| **Risk of Fix** | 🟢 LOW | Simple changes |

---

**All fixes are simple text changes with zero risk to existing functionality.**

**After fixes, v-00-load-style.md will be production-ready.**
