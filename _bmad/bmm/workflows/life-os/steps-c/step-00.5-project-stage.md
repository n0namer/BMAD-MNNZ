---
name: 'step-00.5-project-stage'
description: 'Discover current project stage (Point A) - what exists, what works, what needs completion'
nextStepFile: './step-00.6-resource-assessment.md'
stageAssessmentFile: '{bmb_creations_output_folder}/life-os/project-stage-assessment.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
projectStageExamples: '../data/foundation-examples/project-stage-examples.md'
---

# Step 0.5: Project Stage Discovery (Point A Definition)

## STEP GOAL

Determine **current project state** (Point A) - what already exists, what works, what needs completion. This is CRITICAL for correct timeline, resource, and scoring estimates in Step 05.

**Why this matters:**
- Without understanding Point A, all plans assume "from scratch" (greenfield)
- Timelines are inflated 10x-100x if existing work is ignored
- Scoring is incorrect if existing progress is ignored
- Resources are wasted inefficiently (duplicate work)

💡 **Reference:** For complete examples, stage descriptions, and calculation walkthroughs, load: `{projectStageExamples}`

## MANDATORY EXECUTION RULES

### Universal Rules
- 🛑 NEVER assume project starts from scratch
- 📖 CRITICAL: Read complete step before action
- 🎯 You are a discovery facilitator, not an estimator
- ✅ Save assessment to BOTH Markdown AND Claude Flow memory
- ⚙️ TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess or tool you do not have access to, achieve the outcome in the main thread
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role
You are a project stage analyst. Your job is to:
- Assess current project state objectively
- Identify what already exists and works
- Document progress percentage across dimensions
- Save findings for timeline adjustment in Step 08

## EXECUTION PROTOCOL

### Search Orchestrator Protocol
- Follow data/mcp_search_system_prompt_xml.md.
- Execute: CLI memory → local MD → web/MCP → consilium ranking.

### 1. Welcome User

```
🔍 **Step 0.5: Point A Definition**

📍 **WHERE ARE WE NOW?** - the most critical question for planning.

💡 Without understanding Point A, timelines can be wrong by 10x-100x.
Let's determine where you are right now.
```

### 2. Stage Assessment Questions

**Ask these 3 core questions progressively:**

#### Question 1: Project Lifecycle Stage

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❓ **Question 1: What stage is the project at?**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[A] **Idea only** - no code, prototypes, or users
[B] **Prototype/POC** - works locally, no users
[C] **MVP in development** - partial functionality
[D] **MVP launched** - has users and feedback
[E] **Production** - paying customers, focus on growth
[F] **Mature product** - optimization and evolution

📝 **Your stage:** [A/B/C/D/E/F]
```

**If user unsure:**
```
💡 Let me help determine. Answer:
- Is there working code? (yes → at least B)
- Are there users? (yes → at least D)
- Are there paying customers? (yes → at least E)
```

#### Question 2: What Already Exists and Works

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❓ **Question 2: What already exists and WORKS?**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- [ ] Code/infrastructure (which components?)
- [ ] Team and processes
- [ ] Users and metrics
- [ ] Assets (design, documentation, integrations)

📝 **Describe what works:**
```

#### Question 3: What's Blocking Progress

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❓ **Question 3: What's BLOCKING progress?**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- [ ] Technical (architecture, debt, competencies)
- [ ] Resource (time, budget, people)
- [ ] Market (PMF, users, competitors)
- [ ] Organizational (focus, coordination, priorities)

📝 **Main blocker:**
```

### Step-Specific Subprocess Optimization Rules

- 🎯 Load projectStageExamples in subprocess when user needs help (Pattern 3)
- 💬 Return ONLY matching stage example (A-F), not entire file
- ⚙️ TOOL/SUBPROCESS FALLBACK: If subprocess unavailable, achieve outcome in main context thread

### Project Stage Examples (JIT Loading)

**If user uncertain about stage classification:**

**Launch a subprocess that:**
1. Loads data/project-stage-examples.md
2. Finds stage example matching user's description (A-F)
3. Returns ONLY matching example + completion % calculation
4. Parent presents example to user

**Subprocess returns:** 150 lines (one example) instead of 1,500 lines (all examples)

**Expected format from subprocess:**
```markdown
## Stage {A-F}: {Stage Name}

{Stage description}

**Example Scenario:**
{Matching example}

**Completion Calculation:**
- Technical: {X}%
- Product: {Y}%
- Market: {Z}%
- Operations: {W}%
- **Overall: {AVERAGE}%**

**Timeline Impact:** {100-AVERAGE}% of greenfield estimate
```

**Graceful fallback:** If subprocess unavailable, load full examples file in main context.

### 3. Calculate Completion Percentage

**Quick Reference:**
- **Stage A:** 0-10% | **Stage B:** 10-25% | **Stage C:** 25-50%
- **Stage D:** 50-70% | **Stage E:** 70-90% | **Stage F:** 90-100%

**Adjustments:**
- Add +5% per major component working
- Subtract -10% per major blocker

```
📊 **Project Readiness Assessment**

**Technical Readiness:** {X}%
**Product Readiness:** {X}%
**Market Readiness:** {X}%
**Operational Readiness:** {X}%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**OVERALL READINESS: {AVERAGE}%**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 **What this means:**
- {AVERAGE}% already done → Timeline reduced by ~{AVERAGE}%
- Timeline adjustment: {100-AVERAGE}% of greenfield estimate
```

**Formula:** `Overall % = (Technical% + Product% + Market% + Operations%) / 4`

📖 **Detailed calculation examples available in:** `{projectStageExamples}`

### 4. Save Stage Assessment (Dual Storage)

Create file: `{stageAssessmentFile}`

```markdown
---
id: stage-assessment-{timestamp}
projectStage: {A/B/C/D/E/F}
overallCompletion: {X}%
---

# Project Stage Assessment (Point A)

## Current Stage
**Lifecycle Stage:** {A/B/C/D/E/F}

## What Exists and Works
### Technical / Product / Market / Operations
- {list what exists} - Completion: {X}%

## Blockers
**Primary:** {user's main blocker}

## Timeline Impact
- Greenfield: 0% → Actual: {X}% complete
- **Timeline Adjustment:** {100-X}% of greenfield
- Example: 12 weeks × {100-X}% = {adjusted} weeks

## Memory Note
[Stage: {X}%. Timeline: {100-X}%. Next: Resources.]
```

### 5. Update Workflow Plan

Prepend to {workflowPlanFile}:

```markdown
## Step 0.5: Stage {A-F}, Completion {X}%, Timeline {100-X}%
- Dimensions: Tech {X}% | Product {X}% | Market {X}% | Ops {X}%
- Blocker: {main blocker}
```

Update frontmatter: append `step-00.5-project-stage` to `stepsCompleted`.

### 6. Save to Claude Flow Memory

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:project-stage:{IDEA_ID}" \
  --content "{markdown_content}"

npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:completion-percentage:{IDEA_ID}" \
  --content "{X}%"
```

### 7. Confirm Save

```
✅ **Point A defined!**

📄 {stageAssessmentFile}
🧠 Memory: life-os:project-stage:{IDEA_ID}

**Findings:** Stage {stage}, {X}% complete, blocker: {blocker}
**Next step:** Step 0.6 - resource assessment
```

### 8. Proceed to Next Step (Auto-Proceed)

Display: "**Proceeding to resource assessment...**"
Then load, read entire file, then execute {nextStepFile}.

#### Menu Handling Logic:
- After completion, immediately save state, then load, read entire file, execute {nextStepFile}

#### EXECUTION RULES:
- **This is an auto-proceed step** (no menu displayed)
- **Do NOT wait** for user menu selection
- **Do NOT display** interactive options
- Save assessment to dual storage (Markdown + Claude Flow memory)
- Update workflow plan frontmatter with completion status
- Immediately transition to Step 0.6 (resource assessment)

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS
- Stage clearly identified (A/B/C/D/E/F)
- Completion % calculated across 4 dimensions
- Primary blocker documented
- Timeline adjustment factor calculated
- Saved to Markdown file
- Saved to Claude Flow memory
- User confident about current state

### ❌ SYSTEM FAILURE
- Assuming project starts from scratch (greenfield fallacy)
- Not asking about existing work
- Not calculating completion %
- Not identifying blockers
- Not saving to both storages
- Timeline adjustment not calculated

**Master Rule:** NEVER assume greenfield. ALWAYS discover Point A. All plans depend on knowing WHERE YOU ARE NOW.

**Critical Impact:** Without this step, timelines are wrong by 10x-100x.
