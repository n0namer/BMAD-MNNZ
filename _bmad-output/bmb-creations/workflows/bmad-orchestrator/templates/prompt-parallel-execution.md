---
title: "Task Tool Prompts - Parallel Execution"
guide_type: "Prompt Templates for Step 04"
version: "2.0"
last_updated: "2026-02-26"
usage_context: "Step 04: Parallel Workflow Execution via Task Tool"
---

# Task Tool Prompts for Parallel Workflow Execution

**Purpose:** Prompt templates for spawning parallel agents and managing concurrent workflow execution using Claude Code's Task tool.

**When to Use:** During Step 04 when executing orchestration plan with multiple workflows/phases

---

## 1. Workflow Execution Prompt Template

### Base Template Structure

```
You are executing phase [PHASE_NUMBER] of a multi-workflow orchestration.

Orchestration Context:
- Session ID: [SESSION_ID]
- Current Phase: [PHASE_NUMBER] of [TOTAL_PHASES]
- Workflows in This Phase: [N]
- Parallel Zones: [M]
- Critical Path: [DURATION] minutes
- Total Time Budget: [DURATION] minutes

Your Assignment:
Execute the following workflow(s) in this phase:
[WORKFLOW_LIST_WITH_DETAILS]

Input Data:
[INPUT_ARTIFACTS_AND_CONTEXT]

Expected Outputs:
[EXPECTED_ARTIFACTS_AND_FORMAT]

Success Criteria:
[VALIDATION_RULES]

After completing your part, submit results to:
Result Location: [checkpoint-phase-[PHASE_NUMBER].md]
Format: [Checkpoint template structure]

Do NOT proceed to next phase until checkpoint is approved.
```

---

## 2. Specific Prompt Templates by Phase Type

### Phase Type A: Sequential Workflows (Dependent)

**Scenario:** Workflows that must execute one after another due to data dependencies.

**Prompt Template:**

```
Execute Phase [X]: [Phase Name] - Sequential Execution

This phase has [N] sequential workflows that depend on each other:

Workflow 1: [Name]
  ├─ Input: [Artifact from previous phase or external]
  ├─ Process: [What this workflow does]
  ├─ Output: [Expected artifacts]
  └─ Duration: [X] minutes (budget)

Workflow 2: [Name]
  ├─ Input: [Output from Workflow 1]
  ├─ Process: [What this workflow does]
  ├─ Output: [Expected artifacts]
  └─ Duration: [X] minutes (budget)

Workflow 3: [Name]
  ├─ Input: [Output from Workflow 2]
  ├─ Process: [What this workflow does]
  ├─ Output: [Expected artifacts]
  └─ Duration: [X] minutes (budget)

Execution Steps:
1. Execute Workflow 1 with provided inputs
2. Validate Workflow 1 outputs match expected format
3. Pass Workflow 1 outputs to Workflow 2 as inputs
4. Execute Workflow 2
5. Validate Workflow 2 outputs
6. Pass Workflow 2 outputs to Workflow 3 as inputs
7. Execute Workflow 3
8. Validate final outputs

Quality Gates (Execute ALL):
- [ ] Validate input data exists and is accessible
- [ ] Check output format after each workflow
- [ ] Verify no data loss in transformations
- [ ] Ensure cross-artifact references are valid
- [ ] Check for conflicts/inconsistencies

Checkpoint Creation:
After all workflows complete, create checkpoint document:
  - File: [checkpoint-phase-[X].md]
  - Include: Results from all 3 workflows
  - Status: PASS (all workflows ✓) or FAIL (describe issues)
  - Mark artifacts that failed validation

Do NOT continue until checkpoint is reviewed and approved.
```

---

### Phase Type B: Parallel Workflows (Independent)

**Scenario:** Multiple workflows that can execute simultaneously (no data dependencies).

**Prompt Template:**

```
Execute Phase [X]: [Phase Name] - Parallel Execution

This phase has [M] parallel zones with [N] total workflows.
All workflows can execute concurrently (no dependencies).

┌─ Parallel Zone 1 ────────────────────────┐
│ Workflow A: [Name]                       │
│   Duration: [X] min                      │
│   Input: [External data/artifact]        │
│   Output: [Expected artifacts]           │
│                                           │
│ Workflow B: [Name]                       │
│   Duration: [X] min                      │
│   Input: [External data/artifact]        │
│   Output: [Expected artifacts]           │
│                                           │
│ Workflow C: [Name]                       │
│   Duration: [X] min                      │
│   Input: [External data/artifact]        │
│   Output: [Expected artifacts]           │
└─────────────────────────────────────────┘

┌─ Parallel Zone 2 ────────────────────────┐
│ Workflow D: [Name]                       │
│   Duration: [X] min                      │
│   Input: [External data/artifact]        │
│   Output: [Expected artifacts]           │
│                                           │
│ Workflow E: [Name]                       │
│   Duration: [X] min                      │
│   Input: [External data/artifact]        │
│   Output: [Expected artifacts]           │
└─────────────────────────────────────────┘

Parallel Execution Strategy:
- Execute all 5 workflows at the same time
- Maximum parallelism: [N] agents
- Expected total time: [Max individual duration] (parallel advantage)
- Planned duration: [X] minutes

Zone Execution:
Zone 1:
  - Start Workflows A, B, C at T=0:00
  - Expected completion: T=[Duration]:00
  - Proceed only after ALL 3 workflows complete

Zone 2:
  - Start Workflows D, E at T=[Duration]:00
  - Expected completion: T=[Duration]:00
  - Proceed only after ALL workflows complete

Phase Completion:
  - All zones must complete before moving to next phase
  - Total phase time: [Duration] minutes
  - Slack time available: [X] minutes

Quality Gates (Per Workflow):
- [ ] Inputs validated for each workflow
- [ ] Outputs generated for each workflow
- [ ] Format validation for each output
- [ ] No data conflicts between parallel workflows
- [ ] All artifacts accessible and properly named

Conflict Detection:
Monitor for conflicts during parallel execution:
- Write-after-write: Two workflows writing to same file
- Resource contention: Two workflows using same resource
- Data inconsistency: Parallel outputs contradict

If conflict detected:
  1. Log conflict details
  2. Stop offending workflows
  3. Resolve conflict (coordinate outputs)
  4. Re-execute if necessary

Checkpoint Creation:
After all parallel zones complete:
  - File: [checkpoint-phase-[X].md]
  - Include Zone 1 results (Workflows A, B, C)
  - Include Zone 2 results (Workflows D, E)
  - Include conflict resolution log
  - Status: PASS (all ✓) or FAIL (describe)

Do NOT continue until checkpoint approved.
```

---

### Phase Type C: Hybrid (Sequential + Parallel)

**Scenario:** Some workflows parallel, some sequential dependencies.

**Prompt Template:**

```
Execute Phase [X]: [Phase Name] - Hybrid Execution

This phase mixes sequential dependencies and parallel execution:

T=0:00 ─ Workflow A (Sequential) ──────────┐
           Input: [External]                │
           Duration: 30 min                │
           Output: artifact_A.md           │
                    ↓                      │ Critical Path
T=0:30 ─ [Parallel Zone 1] ─────────────┤ (controls phase time)
        │ Workflow B (depends on A)      │
        │   Duration: 20 min             │
        │   Input: artifact_A.md         │
        │   Output: artifact_B.yml       │
        │                                │
        │ Workflow C (independent)       │
        │   Duration: 25 min             │
        │   Input: [External]            │
        │   Output: artifact_C.json      │
        │                                │
        │ Workflow D (independent)       │
        │   Duration: 15 min             │
        │   Input: [External]            │
        │   Output: artifact_D.csv       │
        └────────────────────────────────┘
                    ↓
T=0:55 ─ Workflow E (Sequential) ──────────┐
           Depends on: B (artifact_B.yml)  │
           Duration: 10 min                │
           Input: artifacts from B, C, D  │
           Output: aggregated_output.md   │
                    ↓                      │
T=1:05 ─ [PHASE COMPLETE] ────────────────┘

Execution Timeline:
1. T=0:00 - Start Workflow A
2. T=0:30 - When A completes, start:
           - Workflow B (with A's output)
           - Workflow C (independent)
           - Workflow D (independent)
   All 3 run in parallel
3. T=0:55 - When B, C, D complete:
           - Start Workflow E
           - Input: B's output + C's output + D's output
4. T=1:05 - All workflows complete

Critical Path: A → B → E (55 minutes)
Slack Paths:
  - A → (C parallel with B) → E (fast path, 55 min)
  - A → (D parallel with B) → E (fast path, 55 min)

Dependency Constraints:
- Workflow A must complete before B starts ✓
- Workflow B must complete before E starts ✓
- Workflows C and D have no dependencies ✓

Parallel Zone 1 (T=0:30 - T=0:55):
Execute B, C, D concurrently:
  [ Start B with A's output ]
  [ Start C with external input ]
  [ Start D with external input ]
  → All 3 run in parallel (25 min max)
  → Wait for longest to complete
  → Proceed when ALL complete

Aggregation (T=0:55):
When all parallel workflows done:
  - Workflow B output: artifact_B.yml
  - Workflow C output: artifact_C.json
  - Workflow D output: artifact_D.csv
  → Pass ALL to Workflow E as inputs

Quality Gates:
Sequential Validation:
  - [ ] Workflow A output ready for B
  - [ ] Workflow B input validated from A
  - [ ] Workflow E inputs from B, C, D all present
  - [ ] Artifact format compatibility verified

Parallel Validation:
  - [ ] Workflows B, C, D all start successfully
  - [ ] No resource conflicts during parallel execution
  - [ ] All 3 complete independently
  - [ ] Output format validation for each

Checkpoint Creation:
After all workflows complete:
  - Sequential execution: A → B → E status ✓
  - Parallel execution: C, D status alongside B ✓
  - Aggregation successful ✓
  - File: [checkpoint-phase-[X].md]
  - Timeline: [Actual] vs [Planned 1:05]

Do NOT continue until checkpoint approved.
```

---

## 3. Error Recovery Prompt Template

### For Failed Workflows

**Scenario:** A workflow fails during execution. How to handle.

**Prompt Template:**

```
Error Recovery Protocol - Phase [X]

Workflow Failed: [Workflow Name]
  Error Type: [Implementation failure / Validation failure / Timeout / Resource]
  Severity: [Critical / High / Medium / Low]
  Error Details: [Error message and context]
  Time of Failure: [Timestamp]

Impact Analysis:
  Dependent Workflows: [List workflows blocked by this failure]
  Phase Status: [IN_PROGRESS / BLOCKED]
  Can Continue?: [Yes, skip failed workflow / No, phase blocked]

Recovery Options:

OPTION A: Retry with Same Parameters
  - Re-execute [Workflow Name] with same inputs
  - Conditions: Only if error is transient (timeout, resource)
  - Expected: Same inputs should work now
  - Risk: Low (same setup)

OPTION B: Retry with Modified Parameters
  - Re-execute with different approach/parameters
  - Example: [Adjusted inputs or configuration]
  - Conditions: If error is deterministic but fixable
  - Expected: Modified approach succeeds
  - Risk: Medium (change unknown variables)

OPTION C: Skip and Use Fallback
  - Bypass [Workflow Name]
  - Use fallback workflow: [Alternative workflow]
  - Example: Use previous output or manual template
  - Conditions: Only if fallback is available
  - Risk: Potential quality loss

OPTION D: Pause Phase and Manual Investigation
  - Stop all workflows in phase
  - Pause execution
  - Manual investigation and fix required
  - Conditions: Critical error, no other option
  - Risk: High (requires manual intervention)

RECOMMENDATION: [Recommend Option A/B/C/D with reasoning]

Recovery Action:
[ ] Execute selected option
[ ] Log recovery action and timestamp
[ ] Document what changed (if any)
[ ] Validate recovery success

If Recovery Successful:
  - Workflow [Name] output: [Artifact generated]
  - Continue with dependent workflows
  - Note recovery in checkpoint

If Recovery Failed:
  - Re-evaluate options
  - Escalate to step-06 validation
  - May require phase restart

Checkpoint Update:
  - Original workflow status: FAILED → [RECOVERED / SKIPPED]
  - Recovery method: [Method used]
  - Recovery outcome: [Success / Failed again]
  - Impact on phase: [Proceed / Needs rework]
```

---

## 4. Result Aggregation Prompt Template

### When Multiple Workflows Produce Outputs

**Scenario:** Combining outputs from multiple workflows into single coherent result.

**Prompt Template:**

```
Result Aggregation - Phase [X]

Workflows Completed:
1. Workflow A: artifact_A.md ✓
2. Workflow B: artifact_B.yml ✓
3. Workflow C: artifact_C.json ✓

Aggregation Task:
Combine outputs into unified deliverable: [Final output name]

Aggregation Rules:

Rule 1: Format Unification
  - Convert all artifacts to consistent format
  - Input formats: [md, yml, json]
  - Output format: [md / yml / json]
  - Method: [How to convert]

Rule 2: Content Merging
  - Artifact A content: [Summary of content]
  - Artifact B content: [Summary of content]
  - Artifact C content: [Summary of content]
  - Merge logic: [How to combine]
    Example: "Section 1 from A, Section 2 from B, Section 3 from C"

Rule 3: Deduplication
  - Common elements: [Elements appearing in multiple artifacts]
  - Deduplication strategy: [Keep first / Merge / Mark variants]
  - References: [How to maintain cross-references]

Rule 4: Cross-Reference Validation
  - Links from A to B: [Validate these are still correct]
  - Links from B to C: [Validate these are still correct]
  - Links from C to A: [Validate these are still correct]

Rule 5: Metadata Preservation
  - Source tracking: [Which artifact contributes which section]
  - Timestamps: [Preserve original creation times]
  - Authors: [Credit original workflow executors]

Aggregation Steps:

Step 1: Format Analysis
  [ ] Review artifact_A.md structure
  [ ] Review artifact_B.yml structure
  [ ] Review artifact_C.json structure
  [ ] Identify conflicts and overlaps

Step 2: Content Extraction
  [ ] Extract key sections from A
  [ ] Extract key sections from B
  [ ] Extract key sections from C
  [ ] Identify common themes

Step 3: Merge & Unify
  [ ] Create unified structure
  [ ] Merge content per rules
  [ ] Resolve conflicts using [conflict resolution method]
  [ ] Validate no data loss

Step 4: Link Validation
  [ ] Check all cross-references are valid
  [ ] Update links if needed
  [ ] Validate all references resolve

Step 5: Final Validation
  [ ] Generated artifact is well-formed
  [ ] All sections present
  [ ] No orphaned content
  [ ] Metadata preserved

Output:
  File: [aggregated_output.md or .yml or .json]
  Size: [Expected size]
  Sections: [List main sections]
  Status: [READY for next phase / NEEDS REVIEW]

Quality Checklist:
  - [ ] All source artifacts used
  - [ ] No data lost
  - [ ] Format consistent
  - [ ] Cross-references valid
  - [ ] Metadata complete
```

---

## 5. Conflict Resolution Prompt Template

### When Parallel Workflows Have Conflicting Outputs

**Scenario:** Two workflows write to same file or produce conflicting information.

**Prompt Template:**

```
Conflict Resolution - Phase [X]

Conflict Detected:
  Type: [Write-After-Write / Data Inconsistency / Resource Contention]
  Workflows Involved: [Workflow A, Workflow B]
  Artifact Affected: [artifact_name.md]
  Timestamp: [When conflict detected]

Conflict Details:

Workflow A Output:
  Content: [What Workflow A wrote]
  Timestamp: [When written]
  Intent: [What this workflow intended]

Workflow B Output:
  Content: [What Workflow B wrote]
  Timestamp: [When written]
  Intent: [What this workflow intended]

Analysis:

Question 1: Are they trying to write same content?
  Answer: [Yes - deduplication / No - real conflict]

Question 2: Can both coexist?
  Answer: [Yes - merge / No - must choose one]

Question 3: Which takes priority?
  Answer: [A (earlier) / B (later) / Context-dependent]

Conflict Resolution Options:

OPTION A: Keep Latest
  - Use output from [Later workflow]
  - Discard output from [Earlier workflow]
  - Rationale: [Why later is correct]

OPTION B: Merge Both
  - Combine both outputs into single artifact
  - Structure: [How to present both]
  - Example: [Show example of merged output]

OPTION C: Create Variants
  - Keep both outputs as separate artifacts
  - Artifact A: artifact_from_workflow_A.md
  - Artifact B: artifact_from_workflow_B.md
  - Document: [Create document explaining variants]

OPTION D: Manual Selection
  - User selects which one to keep
  - Present both options
  - [Show comparison]

RECOMMENDATION: [Recommend Option A/B/C/D with reasoning]

Resolution Implementation:

[ ] Apply conflict resolution
[ ] Update affected artifact(s)
[ ] Document resolution in checkpoint
[ ] Validate resulting artifact

Validation:
  - [ ] Artifact is well-formed
  - [ ] No remnants of conflict
  - [ ] Cross-references still valid
  - [ ] Metadata preserved

Checkpoint Update:
  - Conflict detected: [Workflows A and B]
  - Resolution method: [Option chosen]
  - Resolution time: [HH:MM]
  - Outcome: [RESOLVED / UNRESOLVED]
```

---

## 6. Checkpoint Creation Prompt Template

### Final Step: Create Phase Checkpoint

**Prompt Template:**

```
Create Checkpoint - Phase [X] Complete

Phase Summary:
  Phase Number: [X]
  Total Phases: [N]
  Status: [PASS / FAIL / NEEDS_REWORK]
  Duration: [Actual] vs [Planned] minutes

Workflows in Phase: [List with status]
  [✓ Workflow A - PASS]
  [✓ Workflow B - PASS]
  [✗ Workflow C - FAIL]
  [○ Workflow D - SKIPPED]

Artifacts Generated:
  - artifact_1.md (from Workflow A)
  - artifact_2.yml (from Workflow B)
  - aggregated_output.md (combined A+B)

Issues/Resolutions:
  [Issue 1: Description and resolution]
  [Conflict 1: Type and resolution]
  [Note: Additional context]

Validation Results:
  - Format validation: [PASS / FAIL]
  - Content validation: [PASS / FAIL]
  - Cross-reference validation: [PASS / FAIL]
  - Overall: [PASS / FAIL / MANUAL_REVIEW]

Create Checkpoint File:
File: checkpoint-phase-[X].md
Location: [orchestration-session-[SESSION_ID]/checkpoints/]

Include:
  - Phase Overview (metadata)
  - Workflow Results (all workflows in phase)
  - Parallel Zone Results (if applicable)
  - Sequential Dependency Results (if applicable)
  - Conflict Log (if any conflicts)
  - Artifact Manifest (all outputs)
  - Quality Validation (checklist)
  - Issues & Resolutions (log)
  - Next Phase Dependencies (what next phase needs)
  - Approval Status: [READY_FOR_APPROVAL]

Checkpoint Status:
  [ ] All required artifacts present
  [ ] Checkpoint file created
  [ ] Checkpoint in correct format
  [ ] Ready for approval

Next Step:
  → Proceed to Step 05 (Cascade Sync) if approved
  → Wait for checkpoint approval before continuing
  → If issues found: Execute error recovery
```

---

## 7. Example: Complete Phase Execution

### Scenario: Execute Phase 1 with 3 Sequential Workflows

**Full Prompt Example:**

```
Execute Phase 1: Product Requirements Discovery - Sequential Execution

Session ID: session-20260226-141500
Task: Create comprehensive Product Requirements Document for new feature

This phase has 3 sequential workflows:

WORKFLOW 1: Discover Business Context
  Input: Feature description from user
  Duration: 30 minutes
  Output: business-context.md (describing why feature matters)

WORKFLOW 2: Define User Requirements
  Input: business-context.md (from Workflow 1)
  Duration: 45 minutes
  Output: user-requirements.md (detailed requirements from users)

WORKFLOW 3: Create PRD Document
  Input: user-requirements.md (from Workflow 2)
  Duration: 60 minutes
  Output: product-requirements-document.md (final PRD)

Execution Steps:

1. Execute Workflow 1: Discover Business Context
   [ ] Load user's feature description
   [ ] Analyze business context and rationale
   [ ] Document why this feature is needed
   [ ] Output: business-context.md
   [ ] Validate: File exists and contains expected sections

2. Execute Workflow 2: Define User Requirements
   [ ] Load business-context.md from Workflow 1
   [ ] Extract user needs from context
   [ ] Define detailed requirements
   [ ] Output: user-requirements.md
   [ ] Validate: Matches business context, contains user stories

3. Execute Workflow 3: Create PRD
   [ ] Load user-requirements.md from Workflow 2
   [ ] Create comprehensive Product Requirements Document
   [ ] Include all sections (business, technical, acceptance criteria)
   [ ] Output: product-requirements-document.md
   [ ] Validate: Well-formed, complete, references validated

Quality Gates:
   [ ] Business context clearly documented
   [ ] User requirements match business context
   [ ] PRD incorporates both context and requirements
   [ ] No orphaned or invalid references
   [ ] All formatting correct

Expected Total Time: 135 minutes (sum of sequential)

After All Workflows Complete:
   1. Create checkpoint file: checkpoint-phase-1.md
   2. Document all results in checkpoint
   3. Validate all artifacts
   4. Mark status: READY_FOR_APPROVAL
   5. Wait for approval before proceeding to Phase 2

DO NOT CONTINUE until checkpoint is approved.
```

---

## 8. Quick Reference Checklist

### For Every Phase Execution

**Pre-Execution:**
- [ ] Phase objectives clear
- [ ] Input artifacts identified and available
- [ ] Workflows list complete with dependencies
- [ ] Duration budgets set
- [ ] Success criteria defined

**During Execution:**
- [ ] Workflows started in correct order
- [ ] Parallel zones properly coordinated
- [ ] Inputs passed correctly to dependent workflows
- [ ] Outputs validated immediately after generation
- [ ] Conflicts detected and resolved

**Post-Execution:**
- [ ] All artifacts generated
- [ ] Format validation passed
- [ ] Cross-references validated
- [ ] Aggregation completed (if needed)
- [ ] Checkpoint file created
- [ ] Status set to READY_FOR_APPROVAL
- [ ] Ready for next phase

---

*Parallel Execution Prompts Version: 2.0 | Last Updated: 2026-02-26*
