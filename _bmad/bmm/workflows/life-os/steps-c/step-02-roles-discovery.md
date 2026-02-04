---
name: 'step-02-roles-discovery'
description: 'Determine required roles for the project and create missing role stubs'
nextStepFile: './step-03-specialist-match.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
rolesBase: '../data/roles-base.csv'
specialistsFolder: '{bmb_creations_output_folder}/life-os/specialists'
---

# Step 2: Roles Discovery

## STEP GOAL:

Identify which roles are needed for this project, using the base roles by sphere,
and create missing role stubs before specialist matching.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', read entire file
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Step-Specific Rules:
- 🎯 Focus ONLY on role discovery
- 🚫 FORBIDDEN to match specialists here
- 🤖 Fully automatic: do not ask the user for role input
- ✅ Use idea summary + domain inference to select roles

## EXECUTION PROTOCOLS:

- 🎯 Load {rolesBase} and present relevant roles
- 💾 Append roles to {workflowPlanFile}
- 📖 Create role stubs in {specialistsFolder} if missing

### Search Orchestrator Protocol (Required)
- Follow data/mcp_search_system_prompt_xml.md.
- Execute: CLI memory search -> local MD (rg) -> web/MCP.
- Convene consilium to rank 2–4 options with pros/cons and recommendation.
- Ask user to choose before proceeding.

### Semantic Decision Support
If a decision or prioritization remains unclear, use Search Orchestrator to rank 2–3 options.

## CONTEXT BOUNDARIES:

- Available context: idea summary from workflow plan
- Focus: required roles only

## MANDATORY SEQUENCE

### 1. Infer Spheres (Automatic, Semantic)

Infer spheres by meaning using the Search Orchestrator:
1) CLI Claude Flow memory search
2) Local MD search in plans/snapshots
3) Web/MCP search only if ambiguous

Select 1–3 spheres from:
business, finance, career, health, relationships, learning, home, legal, creative, community.

### 2. Select Roles (Automatic)

Use {rolesBase} (CSV) to select roles for the inferred spheres.
Prefer roles with matching tags and map default_template for later deep plan.
If the idea implies a missing role, add a new role label.
If multiple roles overlap in scope, merge and keep the highest priority.

### 4. Append to Workflow Plan

Append:
```markdown
## Roles

**Spheres:** {list}
**Required Roles:**
- {role} — priority: {high/medium/low}
- {role} — priority: {high/medium/low}

**Notes:**
- {constraints or gaps}
```

### 5. Create Missing Role Profiles (Automatic)

If a role does not exist in {specialistsFolder}, create a role profile:
```markdown
---
name: {role}
status: ACTIVE
created: {today}
---

# {role}

## Scope
{1-2 sentences describing the responsibility boundary}

## Typical Contributions
- {contribution 1}
- {contribution 2}
- {contribution 3}

## Signals This Role Is Needed
- {signal 1}
- {signal 2}
```

### 6. Present MENU OPTIONS

Display: "**Select:** [C] Continue"

#### Menu Handling Logic:
- IF C: Save content to {workflowPlanFile}, update frontmatter, then load, read entire file, then execute {nextStepFile}
- IF Any other: help user respond, then redisplay menu

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Spheres identified
- Roles confirmed
- Plan updated

### ❌ SYSTEM FAILURE:
- Proceeding without role confirmation
- Skipping plan update

**Master Rule:** Roles must be explicit before specialist matching.

