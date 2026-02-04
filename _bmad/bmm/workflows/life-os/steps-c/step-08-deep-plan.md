---
name: 'step-08-deep-plan'
description: 'Build or deepen a multi-level plan (L1-L6) for project participation'
projectPlanFile: '{bmb_creations_output_folder}/life-os/plans/{project_id}-plan.md'
snapshotFile: '{bmb_creations_output_folder}/life-os/snapshots/{project_id}.md'
journalFile: '{bmb_creations_output_folder}/life-os/journal/{project_id}.md'
deepPlanTemplatesRef: '../data/deep-plan-templates.md'
completeStepFile: './step-09-complete.md'
---

# Step 8: Deep Plan Builder

## STEP GOAL:

Create or deepen a multi-level plan (L1-L6) so the user can contribute effectively even with unclear role.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Step-Specific Rules:
- 🎯 Focus ONLY on planning depth and clarity
- 🚫 FORBIDDEN to change scope or timeline here
- 💬 Ask 1–2 questions at a time
- 💬 Confirm each level before moving deeper

## EXECUTION PROTOCOLS:

- 🎯 Load the project plan, snapshot, and journal
- 💾 Update the Deep Plan section
- 📖 Append a journal entry about the deep plan iteration
- 🧾 Record evidence snapshot in journal or workflow plan

### Search Orchestrator Protocol (Required)
- Follow data/mcp_search_system_prompt_xml.md.
- Execute: CLI memory search -> local MD (rg) -> web/MCP.
- Convene consilium to rank 2–4 options with pros/cons and recommendation.
- Ask user to choose before proceeding.

### Semantic Decision Support
If a decision or prioritization remains unclear, use Search Orchestrator to rank 2–3 options.

## MANDATORY SEQUENCE

### 1. Load Current Context

Open:
- {projectPlanFile}
- {snapshotFile} (if exists)
- {journalFile} (if exists)

Summarize the current goal, status, and next step.

### 2. Confirm Planning Mode

Ask the user for confirmation before generating the deep plan:
- "Сделать авто‑генерацию глубинного плана (L1–L6) сейчас? [Да/Нет]"

If the user says **No**, ask what level of detail they want and proceed manually.

### 3. Auto-Select Planning Mode

Automatically choose the planning mode:
- Default: Use template and build full depth (L1 -> L6)
- If role is unclear or user is invited without scope, use the "Invited Role" template

### 4. Auto-Linking Check (Intelligence Layer)

**Before generating Deep Plan, AI scans for auto-linkable data:**

**Sources Checked:**
1. **Workflow Plan** (Design Thinking, Consilium, Scoring)
2. **Framework Templates** (if multiple frameworks filled)
3. **Claude Flow Memory** (patterns from similar projects)

**Auto-Linking Rules:**
```yaml
# Business → Finance
lean_canvas.revenue_streams → npv.cash_inflows
lean_canvas.cost_structure → npv.cash_outflows
okrs.key_results → deep_plan.l2_phases

# Health → Personal
habit_loop.cue → deep_plan.l5_daily_tasks
progressive_overload.weekly_plan → pomodoro.schedule

# Finance → Personal
npv.project_timeline → deep_plan.l2_phases
monte_carlo.scenarios → deep_plan.scenario_branches

# Workflow Plan → All
workflow_plan.project_name → all_templates.project_name
workflow_plan.consilium.specialists → template.recommended_roles
```

**If auto-links found (≥1):**
```
🔗 **Auto-Linking Detected**

Found {count} auto-linkable fields:

1. {Source Framework}.{field} → {Target Framework}.{field}
   - Value: "{preview}"
   - Confidence: {percentage}%

2. {Source}.{field} → {Target}.{field}
   - Value: "{preview}"
   - Confidence: {percentage}%

Apply all links? [✅ Yes] [🔍 Review individually] [❌ Skip]
```

**If user approves:**
- Auto-populate target fields
- Show summary of populated fields
- Log to memory for learning

**If user reviews individually:**
- Show each link with full context
- Allow accept/reject per link
- Learn from rejections (lower confidence for that rule)

**Memory Integration:**
```bash
# Store successful links
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "auto-linking:{source}→{target}:success" \
  --content "Confidence {%}, User accepted, Project {id}"

# Store rejections for learning
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "auto-linking:{source}→{target}:rejected" \
  --content "Reason: {user_reason}, Lower confidence next time"
```

**L2 Auto-Population:**

After auto-linking completes, check for L2 phase auto-population:

**If OKRs framework present:**
```
💡 **L2 Auto-Population Available**

Your OKRs have {count} Key Results.
I can auto-generate L2 phases from them:

OKR: {objective}
  → L2 Phase 1: {KR1 as phase name}
  → L2 Phase 2: {KR2 as phase name}
  → L2 Phase 3: {KR3 as phase name}

Use this structure? [✅ Yes] [✏️ Customize] [❌ Manual]
```

**If NPV/Finance framework present:**
```
💡 **L2 Auto-Population Available**

Your NPV has {year_count} year timeline.
I can auto-generate L2 phases:

NPV Year 1-2 → L2 Phase 1: {first_milestone}
NPV Year 3-5 → L2 Phase 2: {second_milestone}
...

Use this structure? [✅ Yes] [✏️ Customize] [❌ Manual]
```

**After L2 populated, check L5:**

**If Pomodoro/Habit Loop present:**
```
💡 **L5 Auto-Population Available**

Your Habit Loop has daily cue at {time}.
Auto-populate L5 daily tasks?

L5-1: {7:00 AM} - {habit_response} ({habit_loop})
L5-2: {time} - {pomodoro_task_1}
L5-3: {time} - {pomodoro_task_2}

Use this schedule? [✅ Yes] [✏️ Customize] [❌ Manual]
```

### 5. Build L1-L6 (Automatic)

Auto-generate the full depth using the selected template:
- L1: Role/mission
- L2: Contribution areas (2-5)
- L3: Work streams for each area
- L4: Stages for each stream
- L5: Tasks for each stage
- L6: Atomic actions

### 6. Scenario Mapping (Automatic, Semantic)

Infer scenario by meaning (not keywords) using the Search Orchestrator:
1) CLI Claude Flow memory search to find nearest scenario template
2) Local MD search in plans/snapshots for similar cases
3) Web/MCP search only if ambiguity remains

Pick the top 1–2 scenarios and map to templates:
- Tech Expert / Architect
- Research / Discovery
- Ops / Delivery Helper
- Product / Strategy Contributor
- Invited Role (unclear contribution) as fallback

Use {deepPlanTemplatesRef} as the index and load only the relevant `.part-*.md` template file.
If subprocess is available, load the relevant part in a subprocess and return only the selected outline.

If multiple scenarios match, use a **Mixed Scenario** (combine top 2 templates).
Insert the selected template structure and auto-fill a best-effort example outline.

When mixing templates, merge unique nodes and remove duplicates.

### 7. Update Project Plan

Update the "Deep Plan (L1-L6)" section in {projectPlanFile} with the generated outline.
Fill RACI for key L2 nodes and add 2–4 If-Then actions.
Update Plan Quality Metrics:
- Depth Covered = levels present / 6
- Nodes Count = total nodes across L1-L6
- RACI Coverage = % of L2 nodes with R and A
- If-Then Coverage = count of If-Then actions

Compute metrics explicitly:
- Levels present: count L1..L6 headers that exist in the outline
- Nodes count: count all L* lines in the outline
- RACI coverage: (L2 nodes with R and A) / (total L2 nodes)
- If-Then coverage: count of If-Then entries

Quality Gate (must pass before completion):
- L1–L4 present
- RACI Coverage >= 70%
- If-Then Coverage >= 2
If not met, extend the plan until the gate is satisfied.

**If TRIZ was used during planning:**
- Document which TRIZ principle(s) were applied in a dedicated section
- Show before/after contradiction resolution with clear comparison
- Add TRIZ principle as L2 strategy node when appropriate (e.g., "L2: Segmentation - Phase 1 MVP + Phase 2 Polish")
- Include trade-off analysis and why TRIZ approach was chosen
- Update Quality Metrics to reflect TRIZ optimization impact

### 8. Update Journal

Append a journal entry:
- Date
- What was deepened
- Key decisions

### 9. Present MENU OPTIONS

Display menu with method options:

```
**Choose next action:**

**[T] TRIZ** - Resolve planning contradictions (if L2+ reveals conflicts)
**[R] Revise Plan** - Restructure levels
**[Q] Quality Gate** - Check completeness (L1-L4, RACI ≥70%, If-Then ≥2)
**[C] Continue** - Finalize plan

➡️ **Your choice:** [T/R/Q/C]
```

**[T] TRIZ - Planning Contradiction Resolution (Optional)**
- **When to use:** L2+ planning reveals fundamental contradictions (e.g., "Need to launch fast but also need thorough testing", "Limited budget but requires expensive tool")
- **What happens:** Launch Step 4.5 - TRIZ Analysis (Full ARIZ mode recommended for strategic projects)
- **Outputs:** L2 phase structure informed by TRIZ solution, updated deep plan with contradiction-free path
- **Integration:** ARIZ generates L1-L3 structure automatically (see ariz-full.template.md Section 13.2)
- **Skip if:** Plan is executable without resolving contradictions

#### Menu Handling Logic:
- IF T:
  - Identify planning contradictions (timeline, resources, quality trade-offs)
  - Proceed to Step 4.5: TRIZ Analysis (jump to optional step if available)
  - Apply TRIZ principle to resolve contradiction
  - Return here with optimized L2 structure
  - Common outcome: TRIZ principle becomes L2 node (e.g., "L2: Segmentation - Phase 1 MVP + Phase 2 Polish")
  - Document which TRIZ principle(s) applied in Deep Plan section
  - Show before/after contradiction resolution
  - Redisplay menu after TRIZ integration
- IF R: Allow user to revise plan levels, restructure L1-L6 hierarchy, then redisplay menu
- IF Q: Run quality gate check (verify L1-L4 present, RACI Coverage ≥70%, If-Then Coverage ≥2), show results, allow user to extend plan if needed, then redisplay menu
- IF C: Save updates to {projectPlanFile} and {journalFile}, update frontmatter if present, then load, read entire file, then execute {completeStepFile}
- IF Any other: help user respond, then redisplay menu

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY complete when user selects 'C'

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Deep plan created or expanded
- Updates saved to plan and journal

### ❌ SYSTEM FAILURE:
- Skipping confirmation
- Not saving updates

**Master Rule:** Depth must be explicit, confirmed, and documented.

