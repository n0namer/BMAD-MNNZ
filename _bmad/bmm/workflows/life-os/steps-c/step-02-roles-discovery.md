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

Identify required roles using AI-powered role matching and sphere detection, create missing role stubs before specialist matching.

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

**📚 Reference:** See `data/sphere-detection-rules.md` for complete detection algorithm

### 2. AI-Powered Role Matching

**🤖 Automatic Role Suggestion Algorithm:**

Uses intelligent role matching from `data/role-matching-algorithm.md`:
1. **Extract keywords** from idea title + description
2. **Detect domains** (business, tech, design, finance, health, personal, etc.)
3. **Match keywords to 50+ specialist roles** from `data/specialist-roles.yaml`
4. **Apply contextual refinement** (budget, timeline, complexity, stage)
5. **Rank and deduplicate** roles by relevance
6. **Return top 2-8 roles** based on complexity tier

**📚 References:**
- Algorithm logic: `data/role-matching-algorithm.md`
- Role database: `data/specialist-roles.yaml` (50+ specialists)
- Role descriptions: `data/roles-descriptions.md`
- Selection logic: `data/roles-auto-selection.md`

**Complexity-based limits:**
- Quick (<8): 2-3 core roles
- Standard (8-15): 4-6 roles
- Deep (>15): 6-8 comprehensive roles

#### Present AI Suggestions

```
🤖 **AI-Suggested Specialist Roles**

**Detected Domains:** {primary_domain}, {secondary_domain}
**Project Complexity:** {Quick/Standard/Deep}
**Keywords Analyzed:** {top_keywords}

**Recommended Roles:**

1. **{Role Name}** — Priority: {High/Medium/Low}
   - **Relevance Score:** {score}/100
   - **Why:** {keyword matches and domain fit}
   - **Contribution:** {what this role brings}

2. **{Role Name}** — Priority: {High/Medium/Low}
   ...

**Optional Roles (consider if project expands):**
- {Optional Role 1} — {brief rationale}
- {Optional Role 2} — {brief rationale}

**Algorithm Details:**
- {N} keywords analyzed
- {N} roles evaluated from database
- {N} contextual factors applied (budget, timeline, stage)

---

**Actions:**
[A] Approve these roles
[M] Modify (add/remove/change roles)
[R] Regenerate with different criteria
[?] Explain role selection logic
[C] Continue with these roles
```

#### User Response Handling

- **A** or **C**: Proceed to append
- **M**: Enter interactive modification mode
  - Add: "Add Marketing Strategist"
  - Remove: "Remove UX Designer" (with impact warning)
  - Replace: "Replace PM with Startup Advisor"
  - Priority: "Make Architect high priority"
- **R**: Re-run algorithm with adjusted parameters
- **?**: Show detailed scoring and keyword matches

#### CSV Fallback (If AI Insufficient)

**Fallback for base roles using subprocess (Pattern 1 + Pattern 3):**

1. Loads {rolesBase} CSV file
2. Filters rows matching identified spheres
3. Extracts only: role, sphere, priority, default_template
4. Returns ONLY relevant rows (~10-20 lines instead of 150+)

**📚 Reference:** See `data/roles-filtering-algorithm.md` for complete CSV filtering algorithm

**Graceful fallback:** If subprocess unavailable, grep CSV for sphere matches

**Context Savings:** ~450 lines (150 CSV rows → 10-20 filtered rows)

**Integration:** AI specialist matching takes priority; CSV fallback used only if insufficient matches.

### 3. Append to Workflow Plan (After Approval)

```markdown
## Roles

**Spheres:** {list}
**Detected Domains:** {primary_domain}, {secondary_domain}
**Required Roles:**
- {role} — priority: {high/medium/low} — {relevance_note}

**Role Matching Details:**
- Algorithm version: 1.0.0
- Keywords analyzed: {count}
- Roles evaluated: {count}
- Complexity tier: {Quick/Standard/Deep}

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
