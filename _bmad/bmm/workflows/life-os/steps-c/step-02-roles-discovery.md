---
name: 'step-02-roles-discovery'
description: 'Determine required roles for the project and create missing role stubs'
nextStepFile: './step-03-specialist-match.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
rolesBase: '../data/roles-base.csv'
specialistsFolder: '{bmb_creations_output_folder}/life-os/specialists'
---

# Step 2: Roles Discovery

## STEP GOAL

Identify required roles using base roles by sphere, create missing role stubs before specialist matching.

## MANDATORY EXECUTION RULES

### Universal Rules
- 🛑 NEVER generate content without user input
- 📖 Read complete step file before any action
- 🔄 When loading next step with 'C', read entire file
- 📋 YOU ARE A FACILITATOR, not content generator
- ✅ Output in Agent communication style with `{communication_language}`

### Step-Specific Rules
- 🎯 Focus ONLY on role discovery
- 🚫 FORBIDDEN to match specialists here
- 🤖 Suggest roles based on analysis, user confirms
- ✅ Use idea summary + domain inference
- 🎯 Use subprocess for roles CSV filtering (Pattern 1 + Pattern 3)
- 💬 Return ONLY relevant roles, not full CSV file

## EXECUTION PROTOCOLS

- 🎯 Load {rolesBase}, present relevant roles
- 💾 Append roles to {workflowPlanFile}
- 📖 Create role stubs in {specialistsFolder} if missing
- 📚 Use Search Orchestrator (data/mcp_search_system_prompt_xml.md): CLI memory → local MD → web/MCP
- 🎯 Convene consilium to rank 2–4 options, present to user

**Context:** Idea summary from workflow plan, focus on required roles only

## MANDATORY SEQUENCE

### 1. Infer Spheres

**Search Orchestrator priority:**
1. CLI Claude Flow memory search
2. Local MD search (plans/snapshots)
3. Web/MCP (if ambiguous)

**Select 1–3 spheres:** business, finance, career, health, relationships, learning, home, legal, creative, community

**📚 Reference:** See `data/roles-auto-selection.md` for inference protocol

### 2. Select Roles (Suggest + Confirm)

**Logic:**
- Use {rolesBase} CSV for sphere → role mapping
- Match tags, map default_template
- Suggest new role if gap exists
- Merge overlapping roles (keep highest priority)

**📚 References:**
- Selection logic: `data/roles-auto-selection.md`
- Role descriptions: `data/roles-descriptions.md`

#### Roles CSV Filtering (Subprocess - Pattern 1 + Pattern 3)

**Launch a subprocess that:**
1. Loads {rolesBase} CSV file
2. Filters rows matching identified spheres (from step 1)
3. Extracts only: role, sphere, priority, default_template
4. Returns ONLY relevant rows (~10-20 lines instead of 150+ full CSV)

**Subprocess returns:** Filtered roles matching current spheres + priority + template mapping

**Graceful fallback:** If subprocess unavailable, grep CSV in main context for sphere matches, then load full CSV

**Context Savings:** ~450 lines (150 CSV rows → 10-20 filtered rows)

**Present suggested roles:**
```
📋 Suggested Roles for this project:

**Spheres:** {list}
**Required Roles:**
- {role} — priority: {high/medium/low} — {brief rationale}

**Notes:**
- {constraints or gaps}

Please confirm: [A]pprove / [M]odify / [C]ontinue
```

**User response handling:**
- **A** or **C**: Proceed to append
- **M**: Ask changes, update, re-present
- **Other**: Help user, redisplay menu

### 3. Append to Workflow Plan (After Approval)

```markdown
## Roles

**Spheres:** {list}
**Required Roles:**
- {role} — priority: {high/medium/low}

**Notes:**
- {constraints or gaps}
```

### 4. Create Missing Role Profiles (After Approval)

**Template location:** `data/roles-templates.md`

**Create:** `{specialistsFolder}/{role-slug}.md`

```markdown
---
name: {role}
status: ACTIVE
created: {today}
---

# {role}

## Scope
{1-2 sentences describing responsibility boundary}

## Typical Contributions
- {contribution 1}
- {contribution 2}

## Signals This Role Is Needed
- {signal 1}
- {signal 2}
```

### 5. Present MENU OPTIONS

---

## 📊 Quick Feedback (Optional)

How was this step?

👍 Helpful | 😐 OK | 👎 Frustrating

[Type feedback or press Enter to skip]

**After user responds (or skips), save to memory:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "user-context" \
  --key "feedback:step-02-roles-discovery:{timestamp}" \
  --content "{\"step\": \"step-02-roles-discovery\", \"rating\": \"{helpful/ok/frustrating}\", \"comment\": \"{user_comment}\", \"timestamp\": \"{ISO_datetime}\"}"
```

---

Display: "**Select:** [C] Continue"

#### Menu Handling Logic:
- IF C: Save content to {workflowPlanFile}, update frontmatter, then load, read entire file, then execute {nextStepFile}
- IF Any other: help user respond, then redisplay menu

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Spheres identified and presented
- Roles suggested and confirmed by user
- Plan updated after user approval

### ❌ SYSTEM FAILURE:
- Proceeding without role confirmation
- Skipping plan update

**Master Rule:** Roles must be explicit before specialist matching.

