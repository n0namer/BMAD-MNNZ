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

- 🎯 Load projectStageExamples in subprocess when user needs help (Pattern 3: JIT Example Loading)
- 💬 Return ONLY matching stage example (A-F), not entire file
- ⚙️ TOOL/SUBPROCESS FALLBACK: If subprocess unavailable, achieve outcome in main context thread

### Optimization Pattern 3: JIT Example Loading (Just-In-Time)

**Current State (Inefficient):**
- Loads full examples file (~1,500 lines)
- Contains all 6 stages + 10+ example scenarios
- Context bloated when user only needs 1-2 examples
- Load time: ~2-3 seconds

**Optimized State (Efficient):**
- Loads ONLY matching stage example (~150 lines)
- Context reduction: 90% fewer lines
- Load time: <500ms
- User gets faster, focused answer

### Project Stage Examples (JIT Loading - Subprocess Implementation)

**When user uncertain about stage classification:**

**Subprocess workflow:**
1. User provides stage description or answers clarifying questions
2. Subprocess spawned with task: "Find matching stage example"
3. Subprocess loads `data/foundation-examples/project-stage-examples.md`
4. Subprocess searches for matching stage (A-F) based on user description
5. Subprocess extracts ONLY matching stage section (lines X-Y)
6. Subprocess returns formatted response to parent
7. Parent (main context) presents example to user for confirmation

**Subprocess task instruction:**
```
Task: Match user project description to stage and extract example
Input: User's stage description or responses to clarifying questions
Process:
1. Load data/foundation-examples/project-stage-examples.md
2. Match against stages:
   - Stage A: "Idea only, no code" → match keywords: "just thinking", "no code", "early", "concept"
   - Stage B: "Prototype/POC" → match keywords: "prototype", "proof of concept", "working locally", "beta"
   - Stage C: "MVP in development" → match keywords: "partial", "in progress", "incomplete", "building"
   - Stage D: "MVP launched" → match keywords: "launched", "users", "feedback", "live"
   - Stage E: "Production/scaling" → match keywords: "paying", "customers", "growing", "production"
   - Stage F: "Mature product" → match keywords: "mature", "optimization", "evolution", "optimization focus"
3. Extract matching stage section (approximately 150 lines including description + examples)
4. Format as returned example (see below)
5. Return ONLY the matching stage, not full file

Return format:
---
## Stage {A-F}: {Stage Name}

{Stage description from examples file}

**Characteristics:**
{Key characteristics}

**Example Scenario:**
{One concrete example matching user's description}

**Timeline Impact:**
- Greenfield estimate: {X} weeks
- Adjusted timeline: {Y} weeks ({Z}% of greenfield)
- Time saved: {W} weeks

**Completion Calculation:**
- Technical: {X}%
- Product: {Y}%
- Market: {Z}%
- Operations: {W}%
- **Overall: {AVERAGE}%**
---
```

**Expected savings:**
- Lines reduced: 1,500 → 150 (90% reduction)
- Context window saved: ~2,250 tokens
- Load time: ~2.5 seconds → <500ms

**Graceful fallback:**
```
If subprocess unavailable or fails:
1. Load full examples file in main context
2. Display entire Stage Lifecycle Descriptions section
3. User manually finds matching example
4. Continue with assessment

This maintains functionality even if subprocess tools aren't available.
```

**Subprocess unavailability handling:**
```markdown
⚙️ If subprocess tools aren't available:

Instead, I'll load the full examples file and help you:
1. Scan through stage descriptions together
2. Identify which stage matches your situation
3. Review the specific example for that stage
4. Calculate your completion percentage

Takes slightly longer (main context instead of subprocess),
but achieves the same outcome with the same accuracy.
```

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
