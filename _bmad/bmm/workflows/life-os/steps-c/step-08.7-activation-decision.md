---
name: 'step-08.7-activation-decision'
description: 'L2-S3: Decide whether to activate idea into active project now or defer'
nextStepFile: './step-08.8-activation-setup.md'
deferNextStepFile: './step-09-complete.md'
ideaFile: '{bmb_creations_output_folder}/life-os/ideas-bank/planned/idea-{NNN}-{sphere}-{name}.md'
projectsFolder: '{bmb_creations_output_folder}/life-os/projects-bank/'
capacityLimit: 5
---

# Step 8.7: Activation Decision (L2-S3)

## STEP GOAL

Decide whether to activate a planned idea into an active project NOW or DEFER to later.

**Critical Moment:** Idea (file) → Project (folder)
**Next Step:** If ACTIVATE → Step 8.8 (Setup) | If DEFER → Step 09 (Complete)

💡 **Decision Guide:** `../data/activation-decision-guide.md`

## MANDATORY EXECUTION RULES

**Universal:**
- 🛑 Check WIP capacity BEFORE activation (max 5 active projects)
- 📖 Read complete step file first
- 💬 Facilitator role - never auto-decide
- ✅ Always speak in `{communication_language}`
- 🎯 MUST call activation script if user chooses ACTIVATE

**Step-Specific:**
- 🚫 FORBIDDEN to activate if capacity 5/5 (must complete/kill first)
- 🎯 This step ONLY decides - Step 8.8 handles execution
- 💬 Guide user through decision factors

## EXECUTION PROTOCOLS

Follow Search Orchestrator protocol (CLI memory → local MD → web/MCP) for decisions.

---

## MANDATORY SEQUENCE

### 1. Check Capacity

**Check active projects:**
```bash
ACTIVE_COUNT=$(ls -1 "{projectsFolder}/active/" | wc -l)
```

**Display:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 CAPACITY: {ACTIVE_COUNT} / {capacityLimit}
{if <5: "✅ Available" | if =5: "⚠️ Full - Must free space"}

Active: {list project names}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 2. Display Idea Summary

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 IDEA: {idea_name} ({sphere})
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Score: {score}/10 | Impact: {impact}/5 | Feasibility: {feasibility}/5
Plan: {L1-L3|L1-L6} | Duration: {duration} | Resources: {resources}
Top Risks: {top_3_risks}
```

### 3. Activation Decision Menu

**If capacity available (< 5):**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ ACTIVATION DECISION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Options:

[A] ACTIVATE NOW
    → Create active project folder
    → Move to projects-bank/active/
    → Archive idea to ideas-bank/archive/activated/
    → Add to WIP ({ACTIVE_COUNT+1}/5)

[D] DEFER
    → Keep in ideas-bank/planned/
    → Add revisit trigger
    → Available for future activation

[R] REVIEW PLAN
    → Return to Step 08 (Deep Plan)
    → Revise plan before deciding

Choice: [A/D/R]
```

**If capacity FULL (5/5):**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  CAPACITY FULL (5/5) - CANNOT ACTIVATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Must free space first:

[C] Complete Project → Run completion workflow → Return to activate
[K] Kill/Pause Project → Archive and free capacity → Return to activate
[D] Defer This Idea → Keep in planned/ → Activate later
[B] Back → Return without changes

Active Projects: {list with status}

Choice: [C/K/D/B]
```

### 4. Route to Next Step (If [A] Selected)

**Proceed to activation setup:**
```
✅ **Decision: ACTIVATE**

Moving to Step 8.8 (Activation Setup) to create project structure...
```

**Then load, read entire file, execute {nextStepFile}** (step-08.8-activation-setup.md)

### 5. Handle Defer (If [D] Selected)

**Ask for revisit trigger:**
```
📋 **Defer Decision**

When should we revisit this idea?

[1] Specific date: {YYYY-MM-DD}
[2] Condition: "When {condition occurs}"
[3] Quarterly review
[4] Annual review
[5] No specific trigger

Choice: [1/2/3/4/5]
```

**Update idea frontmatter:**
```yaml
status: planned
defer_reason: {user input}
revisit_trigger: {selected trigger}
deferred_date: {ISO_DATE}
```

**Confirmation:**
```
📋 Idea Deferred

File: ideas-bank/planned/idea-{NNN}-{sphere}-{name}.md
Status: PLANNED (not activated)
Revisit: {trigger}

You can activate anytime by running this step again.

[OK] Continue to Step 09
```

### 6. Update Memory

**After defer decision:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "user-context" \
  --key "life-os:deferred:idea-{NNN}" \
  --content "{\"idea_id\":\"idea-{NNN}\",\"deferred_date\":\"{ISO_DATE}\",\"reason\":\"{reason}\",\"revisit_trigger\":\"{trigger}\"}"
```

**Note:** Activation memory update happens in Step 8.8 (after project actually created).

---

## QUALITY GATES

**Required Before Proceeding:**
- ☐ Capacity checked (5/5 = must handle first)
- ☐ Plan complete (L1-L3 minimum)
- ☐ Scores documented
- ☐ User decision explicit (activate/defer)
- ☐ If defer: revisit trigger captured

**Red Flags:**
- Capacity full (5/5) but trying to activate without action
- Plan incomplete or missing
- User unsure about commitment
- Skipping defer trigger (if deferring)

---

## SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Capacity checked before decision
- User decision explicit (activate/defer)
- If activated: routed to Step 8.8 for setup
- If deferred: revisit trigger documented, routed to Step 09
- Memory updated with decision

### ❌ FAILURE:
- Activating without capacity check
- User decision ambiguous
- Missing defer trigger (if deferring)
- Skipping memory update
- Not routing to appropriate next step

**Master Rule:** Decision must be capacity-aware and clearly documented.

---

## ROUTING LOGIC

**If user selected [A] ACTIVATE:**
- Save decision state
- Display: "Moving to activation setup..."
- Load, read entire file, execute {nextStepFile} (step-08.8-activation-setup.md)

**If user selected [D] DEFER:**
- Update idea frontmatter with defer metadata
- Display: "Idea deferred. Completing workflow..."
- Load, read entire file, execute {deferNextStepFile} (step-09-complete.md)

**If user selected [R] REVIEW:**
- Return to Step 08 (Deep Plan)
- User can revise plan before deciding

**Time Estimate:**
- Capacity check: 2 min
- Decision discussion: 5 min
- Defer trigger (if deferring): 2 min
- **Total: 7-10 min** (activation setup happens in Step 8.8)
