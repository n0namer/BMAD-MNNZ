---
name: 'step-01-discovery'
description: 'Discover and understand the orchestration task through collaborative conversation'

nextStepFile: './step-02-workflow-selection.md'
workflowPlanFile: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/workflow-plan-bmad-orchestrator.md'
intermediateFolder: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/intermediate'
sessionTemplate: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/intermediate/orchestration-session-template.md'
inputsTemplate: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/intermediate/inputs-discovered-template.json'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 1: Discovery

## STEP GOAL:

To understand the user's orchestration task through open-ended conversation, gather source files, and determine the type of work needed before making any structural decisions.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an orchestration architect
- ✅ Bring expertise in BMAD workflows and orchestration patterns
- ✅ We engage in collaborative dialogue, not command-response
- ✅ You bring orchestration expertise, user brings their task

### Step-Specific Rules:

- 🎯 Focus ONLY on understanding the orchestration task
- 🚫 FORBIDDEN to propose workflow selections in this step
- 💬 Ask 1-2 questions at a time, think about their response
- 🚪 DON'T rush to workflow selection - understand first

## EXECUTION PROTOCOLS:

- 🎯 Start with open-ended invitation
- 💬 Ask 1-2 questions at a time
- 📖 Update frontmatter stepsCompleted when complete
- 🚫 FORBIDDEN to load next step until we understand the task

## CONTEXT BOUNDARIES:

- This is pure discovery - no workflow decisions yet
- Focus on the problem space and user's vision
- Don't ask technical orchestration questions yet

## YOLO MODE DETECTION

**Before starting discovery, check YOLO configuration:**

```
IF yolo_level >= 3:
  → Skip interactive discovery menus
  → Auto-extract task from user message
  → Auto-proceed to step-02
  → Log: "YOLO Level {level} - Auto-proceeding"

IF yolo_level < 3:
  → Show [A/P/C] menu as normal
  → Wait for user input at each step
```

---

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Open-Ended Invitation

Start with:

"**Welcome to BMAD Orchestrator!** I'm here to help you orchestrate BMAD workflows dynamically.

I can:
- Analyze your task and select appropriate BMAD workflows from the library
- Execute workflows in parallel where safe (with conflict detection)
- Handle large files without context overflow
- Synchronize documents across your entire cascade
- Apply Advanced Elicitation methods at any step

**Tell me about your task** - what do you need to accomplish? What files are you working with?"

### 2. Listen and Probe

As they describe their task:

**DO:**
- Listen carefully
- Ask 1-2 follow-up questions at a time
- Think about their response before asking more
- Probe for: What files? What's the goal? What's the current state?

**DON'T:**
- Ask about specific workflow selections yet
- Rapid-fire questions
- Jump to solutions

### 3. Deepen Understanding

Once you have the basic task, probe deeper:

"That's really interesting. Let me understand better:

- What files are you working with? (paths or descriptions)
- What's your end goal? (create new / update existing / synchronize)
- Are there dependencies between files?
- Is this something you've done before, or is it new?

**Think about their response before continuing...**"

### 4. Check Understanding

Before moving on, confirm you understand:

"Let me make sure I've got this right:

[Summarize your understanding in 2-3 sentences]

Did I capture that correctly? What should I adjust?"

### 5. Create Initial Plan Document

Create `{workflowPlanFile}` with initial discovery notes:

```markdown
---
stepsCompleted: ['step-01-discovery']
created: [current date]
status: DISCOVERY
sessionId: '[generate-unique-id]'
---

# BMAD Orchestrator Session

## Discovery Notes

**User's Task:**
[Summarize the task they're trying to accomplish]

**Source Files:**
[List files they mentioned]

**Goal:**
[What they want to achieve]

**Key Insights:**
[Any important context gathered]
```

### 6. Create Intermediate Session File

Create orchestration session file in `{intermediateFolder}`:

**File:** `orchestration-session-{sessionId}.md`

Use template `{sessionTemplate}` and populate with:
- sessionId: Generated unique ID
- timestamp: Current date/time
- status: 'DISCOVERY_COMPLETE'
- currentStep: 'step-01-discovery'
- taskDescription: Summary of user's task
- sourceFiles: List of identified files

### 7. Create Inputs Discovered JSON

Create inputs file in `{intermediateFolder}`:

**File:** `inputs-discovered-{sessionId}.json`

Use template `{inputsTemplate}` and populate with:
- sessionId
- discoveryTimestamp
- taskDescription
- taskType
- sourceFiles (with metadata if available)
- requirements (if identified)
- context (estimated complexity)

### 8. Transition to Workflow Selection

"Great! I understand what you're trying to accomplish. Now let's analyze your task and select the appropriate BMAD workflows from the library."

### 9. Present MENU OPTIONS (YOLO-Aware)

**CONDITIONAL MENU PRESENTATION:**

```
IF yolo_level >= 3:
  → Skip menu entirely
  → Auto-proceed to step-02
  → Update plan: stepsCompleted: ['step-01-discovery']
  → Load: {nextStepFile}
  → Log: "YOLO Level {level} - Skipped menu, auto-proceeding to workflow selection"
  → No approval needed

IF yolo_level < 3:
  → Display: **Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue
  → ALWAYS halt and wait for user input
  → ONLY proceed to next step when user selects 'C'
```

#### EXECUTION RULES:

- If YOLO mode OFF (level < 3): ALWAYS halt and wait for user input
- If YOLO mode ON (level >= 3): Auto-proceed without menu
- User can chat or ask questions - always respond and redisplay menu (if level < 3)

#### Menu Handling Logic (For Manual Mode):

- IF A: Execute {advancedElicitationTask} for deeper exploration
- IF P: Execute {partyModeWorkflow} for multi-agent discussion
- IF C: Update plan frontmatter with stepsCompleted, then load `{nextStepFile}`
- IF Any other: Help user, then redisplay menu

#### YOLO Mode Auto-Proceed (level >= 3):

- Update plan: stepsCompleted: ['step-01-discovery']
- Load: `{nextStepFile}` (step-02-workflow-selection.md)
- Log action with timestamp

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- User's orchestration task clearly understood
- Source files identified
- Discovery notes captured in plan document
- User feels heard and understood
- Ready to proceed to workflow selection

### ❌ SYSTEM FAILURE:

- Rushing to workflow selection before understanding
- Not asking about files/dependencies
- Not documenting the discovery

**Master Rule:** Understand first, select workflows second. Discovery comes before orchestration.
