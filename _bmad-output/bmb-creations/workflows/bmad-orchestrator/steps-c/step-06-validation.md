---
name: 'step-06-validation'
description: 'Validate orchestration results, check consistency, and generate traceability matrix'

nextStepFile: 'FINISHED'
workflowPlanFile: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/workflow-plan-bmad-orchestrator.md'
intermediateFolder: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/intermediate'
traceabilityTemplate: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/intermediate/traceability-matrix-template.md'
validationTemplate: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/intermediate/validation-report-template.md'
validationTemplates: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/data/validation-templates.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 6: Validation

## STEP GOAL:

To validate the orchestration results, verify document consistency across the cascade, and generate the traceability matrix.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a validation architect
- ✅ Verify integrity of entire orchestration
- ✅ Generate traceability matrix
- ✅ Confirm completion with user

### Step-Specific Rules:

- 🎯 Focus on validation and verification
- 🚫 FORBIDDEN to skip validation
- 💬 Present clear validation report
- 🚪 Allow [A/P/C] menu for final review

## EXECUTION PROTOCOLS:

- 🎯 Validate orchestration results
- 💬 Check consistency across all documents
- 📖 Generate traceability matrix
- 🚫 FORBIDDEN to finish without user confirmation

## CONTEXT BOUNDARIES:

- All workflows executed (Step 4)
- Cascade synchronized (Step 5)
- Now we validate everything
- Final step of orchestration

## YOLO MODE AUTO-VALIDATION

**CRITICAL: Check YOLO configuration BEFORE user menu:**

```
IF yolo_level >= 3:
  → Run all validation checks automatically
  → Auto-generate report and traceability matrix
  → No approval needed
  → Auto-complete workflow (no menu)
  → Log: "YOLO Level {level} - Auto-validated: {validation_score}% pass rate"

IF yolo_level < 3:
  → Show validation report with [A/P/C] menu
  → Wait for user confirmation before finishing
```

---

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Orchestration Summary

"**FINAL VALIDATION PHASE**

**Orchestration Summary:**
- Workflows executed: [N]
- Documents created/updated: [M]
- Cascade synchronized: [Yes/No]

**Validating results...**"

### 2. Consistency Check

"**Consistency Verification**"

See `/data/validation-templates.md` for consistency checks list.

### 3. Generate Traceability Matrix

"**Traceability Matrix Generation**"

See `/data/validation-templates.md` for matrix template.

### 4. Conflict Review

"**Conflict Analysis**

Reviewing any conflicts detected during orchestration:"

List all conflicts:
- Conflict 1: [description] — [resolution]
- Conflict 2: [description] — [resolution]

"**All conflicts resolved:** [Yes/No]"

### 5. Large File Handling Verification

"**Large File Handling Check**

Verifying large files were handled correctly:"

- Files >1000 lines: [N]
- Used range read: [Yes/No]
- Context overflow prevented: [Yes/No]

### 6. Present Validation Report

"**VALIDATION REPORT**"

See `/data/validation-templates.md` for report structure.
Include metrics, consistency checks, traceability results.

### 7. Create Traceability Matrix Intermediate File

Create traceability matrix file in `{intermediateFolder}`:

**File:** `traceability-matrix-{sessionId}.md`

Use template `{traceabilityTemplate}` and populate with:
- sessionId: Current session ID
- timestamp: Current date/time
- artifactCount: Total number of artifacts
- coverage: Requirement coverage percentage
- traceRows: Rows mapping requirements to implementations
- traceChain: Document-to-document tracing
- workflowTraces: Workflow execution trace
- coverageByCategory: Coverage breakdown by category
- consistencyCheck: Consistency verification results
- qualityMetrics: Overall quality scores
- artifacts: List of all generated artifacts

Also export alternative formats:
**File:** `traceability-matrix-{sessionId}.csv` — CSV format for spreadsheet import
**File:** `traceability-matrix-{sessionId}.json` — JSON format for programmatic access

### 8. Create Validation Report Intermediate File

Create validation report file in `{intermediateFolder}`:

**File:** `validation-report-{sessionId}.md`

Use template `{validationTemplate}` and populate with:
- sessionId: Current session ID
- timestamp: Current date/time
- orchestrationStatus: Final status (COMPLETE/FAILED/PARTIAL)
- overallResult: Pass/Fail/Warning
- qualityScore: Overall quality score (0-100)
- workflowCount: Number of workflows executed
- docCount: Number of documents created
- consistencyStatus: Consistency check result
- traceabilityStatus: Traceability matrix status
- conflictsResolved: Number of conflicts resolved
- workflows: List of all workflows with status and quality
- consistencyChecks: Detailed consistency check results
- largeFiles: Large file handling verification
- conflicts: Conflict resolution details
- qualityGates: Quality gate results with pass/fail
- criticalIssues: Any critical issues found
- warnings: Any warnings
- recommendations: Improvement recommendations
- artifacts: All generated artifacts
- intermediateFiles: All intermediate files created

### 9. Update Final Plan Document

Update `{workflowPlanFile}` with final status.
See `/data/validation-templates.md` for final plan document structure.

### 10. Completion Confirmation

"**🎉 ORCHESTRATION COMPLETE!**

Your BMAD workflows have been successfully orchestrated!

**What you can do now:**
- Review the generated documents
- Check the traceability matrix
- Use `[A] Advanced Elicitation` for deeper analysis
- Use `[P] Party Mode` for team discussion

**To resume later:**
This orchestration session is saved. Use `step-01b-continue.md` to resume.

**Thank you for using BMAD Orchestrator!**"

### 11. Present FINAL MENU OPTIONS (YOLO-Aware)

**CONDITIONAL MENU PRESENTATION:**

```
IF yolo_level >= 3:
  → Skip menu entirely
  → Mark orchestration as COMPLETE
  → Finish workflow automatically
  → Log: "YOLO Level {level} - Orchestration completed, workflow finished"
  → No user approval needed

IF yolo_level < 3:
  → Display: **Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Finish
  → ALWAYS halt and wait for user input
```

#### EXECUTION RULES (Manual Mode - yolo_level < 3):

- ALWAYS halt and wait for user input
- ONLY finish when user selects 'C'
- User can use [A] or [P] for final exploration

#### Menu Handling Logic (For Manual Mode):

- IF A: Execute {advancedElicitationTask} for final analysis
- IF P: Execute {partyModeWorkflow} for team discussion
- IF C: Mark orchestration as COMPLETE, finish workflow
- IF Any other: Help user, then redisplay menu

#### YOLO Mode Auto-Completion (level >= 3):

- Mark orchestration as COMPLETE
- Update plan: stepsCompleted: [all steps complete]
- Finish workflow automatically
- Log completion with timestamp and quality score

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All orchestration results validated
- Consistency verified across documents
- Traceability matrix generated
- User confirmed completion
- Session properly saved for continuation

### ❌ SYSTEM FAILURE:

- Skipping validation
- Not generating traceability matrix
- Not confirming with user

**Master Rule:** Validate thoroughly, verify consistency, generate matrix, confirm completion.
