---
name: 'step-05-cascade-sync'
description: 'Synchronize related documents across the cascade after workflow execution'

nextStepFile: './step-06-validation.md'
workflowPlanFile: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/workflow-plan-bmad-orchestrator.md'
intermediateFolder: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/intermediate'
syncReportTemplate: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/intermediate/sync-report-template.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 5: Cascade Synchronization

## STEP GOAL:

To synchronize related documents across the cascade — updating dependent files to reflect changes from the master document.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a synchronization architect
- ✅ Identify related documents automatically
- ✅ Propagate changes with minimal conflicts
- ✅ Maintain document consistency across cascade

### Step-Specific Rules:

- 🎯 Focus on synchronizing related documents
- 🚫 FORBIDDEN to skip synchronization
- 💬 Report each synchronization action
- 🚪 Allow [C] Continue or review each sync

## EXECUTION PROTOCOLS:

- 🎯 Identify related documents in cascade
- 💬 Propagate changes from master to dependents
- 📖 Update frontmatter stepsCompleted when complete
- 🚫 FORBIDDEN to leave documents inconsistent

## CONTEXT BOUNDARIES:

- Workflows executed from Step 4
- Master document(s) updated
- Now we propagate to related documents
- Cascade synchronization completes the orchestration

## YOLO MODE AUTO-SYNC

**CRITICAL: Check YOLO configuration BEFORE sync menus:**

```
IF yolo_level >= 3:
  → Auto-apply all synchronization changes
  → No review/approval needed
  → Auto-proceed to step-06
  → Log: "YOLO Level {level} - Auto-synced {N} documents, {M} changes applied"

IF yolo_level < 3:
  → Show [A] Apply [R] Review [S] Skip menu for each document
  → Wait for user confirmation before applying changes
```

---

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Identify Cascade Relationships

"**Cascade Synchronization Phase**

Analyzing document relationships...

**Master Document(s):**
- [list master files from execution]

**Detecting Related Documents:**
Scanning for:
- Documents referencing master files
- Documents in same project/folder
- Documents with related frontmatter
- Documents linked by naming conventions

**Cascade Map:**"

Build cascade map showing:
```
Master: [file.md]
  ├─ Related: [dependent1.md] — references section X
  ├─ Related: [dependent2.md] — shares frontmatter keys
  └─ Related: [folder/dependent3.md] — in same project
```

### 2. Detect Changes in Master

"**Change Detection**

Comparing master document(s) to previous state...

**Changes Detected:**
- Section [X]: [Added/Modified/Removed]
- Frontmatter [key]: [Changed from → to]
- Structure: [reorganized]

**Impact Analysis:**
- [Dependent 1]: High impact (references changed section)
- [Dependent 2]: Medium impact (shared metadata)
- [Dependent 3]: Low impact (same project, no direct refs)"

### 3. Synchronize Each Related Document (YOLO-Aware)

For each related document:

**CONDITIONAL SYNC PRESENTATION:**

```
IF yolo_level >= 3:
  → Auto-apply all changes to this document
  → Log: "Auto-synced {file_name}: {change_summary}"
  → Skip to next document

IF yolo_level < 3:
  → Display options menu for user approval
```

**Manual Sync Menu (yolo_level < 3):**

"**Synchronizing: [dependent-file.md]**

Changes to propagate:
- [Change 1] — from master section [X]
- [Change 2] — metadata update

**Options:**
[A] Apply all changes automatically
[R] Review each change
[S] Skip this document
[E] Edit changes before applying

What would you like? [A/R/S/E]"

**Handle response:**
- IF A: Apply changes, document, move to next
- IF R: Show each change, ask confirm/skip/edit
- IF S: Document skip reason, move to next
- IF E: Let user edit, then apply

**YOLO Mode Auto-Apply (level >= 3):**

- Apply all detected changes
- Log: "Auto-synced {file_name} — {change_count} changes"
- Move to next document
- No user interaction needed

### 4. Large File Handling During Sync

If related document is large:

"**Large File Detected:** [filename] ([X] lines)

Using range read for synchronization:
- Only reading sections that need updates
- Context usage: [Y%] of limit
- Append-only for additions

**Synchronizing relevant sections only...**"

### 5. Cascade Update Report

After synchronizing all related documents:

"**CASCADE SYNCHRONIZATION COMPLETE**

**Summary:**
- Documents synchronized: [N]
- Changes applied: [M]
- Skipped: [K]
- Conflicts: [L] (if any)

**Updated Files:**
- [file1.md] — [changes summary]
- [file2.md] — [changes summary]
...

**Consistency Status:** ✅ All documents synchronized / ⚠️ [N] conflicts need resolution"

### 6. Create Sync Report Intermediate File

Create sync report file in `{intermediateFolder}`:

**File:** `sync-report-{sessionId}.md`

Use template `{syncReportTemplate}` and populate with:
- sessionId: Current session ID
- timestamp: Current date/time
- masterCount: Number of master documents
- relatedCount: Number of related documents found
- syncedCount: Number of documents successfully synced
- conflictCount: Number of conflicts detected
- status: Overall synchronization status
- masters: List of master documents with changes detected
- successfulSyncs: List of successful synchronizations
- skippedSyncs: List of skipped synchronizations with reasons
- conflicts: List of conflicts with resolutions
- cascadeGraph: Visual representation of cascade relationships
- propagationLog: Log of all change propagation actions
- largeFiles: Any large files handled during sync

Also create changes propagated JSON:
**File:** `changes-propagated-{sessionId}.json`
- Machine-readable list of all changes
- Source and target for each change
- Change type and status

### 7. Update Plan Document

Update `{workflowPlanFile}` with cascade sync results:

```markdown
## Cascade Synchronization

**Master Document(s):**
- [file.md]

**Synchronized Documents:**
| File | Changes | Status |
|------|---------|--------|
| [file1.md] | [summary] | ✅ Synced |
| [file2.md] | [summary] | ⏭️ Skipped |

**Conflicts (if any):**
- [file.md]: [conflict description] — [resolution]

**Consistency Check:**
- All documents aligned: [Yes/No]
- Manual review needed: [files]
```

Update frontmatter: `stepsCompleted: ['step-01-discovery', 'step-02-workflow-selection', 'step-03-orchestration-plan', 'step-04-execution-loop', 'step-05-cascade-sync']`

### 8. Transition to Validation

"Excellent! Cascade synchronization is complete. All related documents have been updated to reflect the master document changes.

Now proceeding to final validation..."

### 9. Present MENU OPTIONS (YOLO-Aware)

**CONDITIONAL MENU PRESENTATION:**

```
IF yolo_level >= 3:
  → Skip menu entirely
  → Auto-proceed to step-06
  → Update plan: stepsCompleted: [sync phase complete]
  → Load: {nextStepFile}
  → Log: "YOLO Level {level} - Auto-proceeded to validation"

IF yolo_level < 3:
  → Display: **Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue
  → ALWAYS halt and wait for user input
```

#### EXECUTION RULES (Manual Mode - yolo_level < 3):

- ALWAYS halt and wait for user input
- ONLY proceed to next step when user selects 'C'
- User can chat or ask questions - always respond and redisplay menu

#### Menu Handling Logic (For Manual Mode):

- IF A: Execute {advancedElicitationTask} for deeper exploration
- IF P: Execute {partyModeWorkflow} for multi-agent discussion
- IF C: Update plan frontmatter, then load `{nextStepFile}`
- IF Any other: Help user, then redisplay menu

#### YOLO Mode Auto-Proceed (level >= 3):

- Update plan: stepsCompleted: [all sync phase complete]
- Load: `{nextStepFile}` (step-06-validation.md)
- Log action with sync summary

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All related documents identified
- Changes propagated successfully
- Large files handled with range read
- Consistency maintained across cascade
- User could review/approve changes
- Ready for final validation

### ❌ SYSTEM FAILURE:

- Missing related documents
- Changes not propagated
- Inconsistent state left behind
- No user review option

**Master Rule:** Identify all related docs, propagate changes carefully, maintain consistency, get user approval.
