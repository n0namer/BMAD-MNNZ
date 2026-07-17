---
name: 'step-01b-continue'
description: 'Resume orchestration from previous checkpoint'

workflowPlanFile: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/workflow-plan-bmad-orchestrator.md'
---

# Step 1b: Continue Orchestration

## STEP GOAL:

To resume a previous orchestration session from the last checkpoint.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: Restore state from plan document before proceeding
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an orchestration resumption handler
- ✅ Restore previous context accurately
- ✅ Let user confirm or adjust the plan
- ✅ Resume from exact checkpoint

### Step-Specific Rules:

- 🎯 Focus on restoring previous state
- 🚫 FORBIDDEN to skip state restoration
- 💬 Present clear status and options
- 🚪 Allow user to adjust before resuming

## EXECUTION PROTOCOLS:

- 🎯 Load previous plan document
- 💬 Restore context and state
- 📖 Determine next step from stepsCompleted
- 🚫 FORBIDDEN to proceed without user confirmation

## CONTEXT BOUNDARIES:

- This is a continuation, not a fresh start
- Previous orchestration state exists in plan document
- We restore and continue from checkpoint
- User may adjust before resuming

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Previous Session

"**Resuming BMAD Orchestrator Session**

Loading previous orchestration state...

**Session Details:**"

Read `{workflowPlanFile}` and extract:
- Created date
- Current status
- stepsCompleted array
- Workflows selected
- Orchestration plan
- Last checkpoint

### 2. Restore Context

"**Restored Context:**

**Session Started:** [date]
**Last Activity:** [timestamp]
**Status:** [In Progress / Paused / Error]

**Progress:**
- Completed steps: [list from stepsCompleted]
- Current phase: [determine from stepsCompleted]

**Previously Selected:**
- Workflows: [list]
- Target files: [list]

**Orchestration Plan:**
[summary from plan document]"

### 3. Determine Next Step

Based on `stepsCompleted` array in frontmatter:

**IF stepsCompleted includes:**
- `step-01-discovery` only → Next: `step-02-workflow-selection`
- `step-02-workflow-selection` → Next: `step-03-orchestration-plan`
- `step-03-orchestration-plan` → Next: `step-04-execution-loop`
- `step-04-execution-loop` → Next: `step-05-cascade-sync` (or continue execution)
- `step-05-cascade-sync` → Next: `step-06-validation`
- `step-06-validation` → Session already complete

### 4. Present Resume Options

"**RESUME OPTIONS**

**Current State:**
- Last completed: [step name]
- Next step: [step name]
- Progress: [X] of 6 steps

**What would you like to do?**

[C] Continue from next step ([step name])
[R] Review and adjust plan
[S] Start over (new session)
[A] Advanced Elicitation on current state

Select: [C/R/S/A]"

**Handle response:**
- IF C: Load next step file, continue
- IF R: Show current plan, allow adjustments, then ask again
- IF S: Confirm, then redirect to step-01-discovery
- IF A: Run Advanced Elicitation, then re-present options

### 5. Resume Execution

If user selects [C]:

"**Resuming orchestration...**

Loading: [nextStepFile]
Restoring context...

**Ready to continue from:** [step name]

Proceeding to next step now."

Load and execute the next step file.

### 6. Handle Completion Case

If `step-06-validation` is in stepsCompleted:

"**SESSION ALREADY COMPLETE**

This orchestration session was already completed on [date].

**Results:**
- Workflows executed: [N]
- Documents updated: [M]
- Status: ✅ COMPLETE

**Options:**
[N] Start new orchestration session
[R] Review completed session
[S] Start over with same parameters

What would you like? [N/R/S]"

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Previous session state loaded correctly
- Context accurately restored
- Next step correctly determined
- User confirmed resume action
- Orchestration continues seamlessly

### ❌ SYSTEM FAILURE:

- Not loading previous state
- Incorrect next step determination
- Proceeding without user confirmation
- Losing previous context

**Master Rule:** Restore accurately, confirm with user, resume seamlessly.
