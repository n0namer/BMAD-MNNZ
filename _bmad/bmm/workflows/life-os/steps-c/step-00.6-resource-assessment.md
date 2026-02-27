---
name: 'step-00.6-resource-assessment'
description: 'Assess available resources and calculate speed multiplier (LLM 10x-50x, team, budget)'
nextStepFile: './step-00.7-optimization-intelligence.md'
resourceAssessmentFile: '{bmb_creations_output_folder}/life-os/resource-assessment.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
speedMultipliersData: '../data/speed-multipliers.yaml'
resourceAssessmentExamples: '../data/foundation-examples/resource-assessment-examples.md'
---

# Step 0.6: Resource Assessment

## STEP GOAL

Determine **available resources** (LLM, team, budget, tools) and calculate **Speed Multiplier** - how many times faster the project can be realized compared to traditional development.

**Why this matters:**
- LLM-assisted development is 10x-50x faster than traditional
- No-code tools are 5x-20x faster than manual coding
- Existing codebase is 2x-5x faster than greenfield
- **Without accounting for Speed Multiplier, timelines are inflated by 10x-100x**

💡 **Reference:** For complete multiplier examples, case studies, and asset templates, load: `{resourceAssessmentExamples}`

## MANDATORY EXECUTION RULES

**Universal Rules:**
- 🛑 NEVER assume traditional speed | 📖 Read complete step before action
- 🎯 Role: Resource analyst (not planner) | ✅ Save to BOTH Markdown AND Claude Flow memory
- ⚙️ TOOL FALLBACK: If subprocess unavailable, achieve outcome in main thread
- ✅ SPEAK OUTPUT in {communication_language}

**Your Job:** Identify resources (human + AI) → Calculate speed multiplier → Document constraints → Save for Step 08 timeline

## EXECUTION PROTOCOL

**Search Orchestrator Protocol (Required):** Follow data/mcp_search_system_prompt_xml.md. Execute: CLI memory search → local MD (rg) → web/MCP. Convene consilium, rank 2-4 options, ask user to choose.

### 1. Welcome User

```
⚡ **Step 0.6: Resource Assessment**

Traditional development takes MONTHS. With LLM/no-code - WEEKS or DAYS.
Examples: Auto-responder 2-4 months → 3-5 DAYS (10x-20x). Katana 12 weeks → 3-4 weeks (4x).

**Goal:** Determine resources and calculate Speed Multiplier.
📖 Complete examples: {resourceAssessmentExamples}
```

### 2. Resource Assessment Questions

**Ask these 4 core questions progressively:**

#### Question 1: Development Resources

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❓ **Question 1: What development resources are available?**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Check ALL that apply:

**AI/LLM:** [ ] Claude Code/Cline [ ] GitHub Copilot [ ] Cursor AI [ ] GPT-4 [ ] v0.dev/Bolt.new
**Team:** [ ] Full-time devs ({N}) [ ] Part-time ({hrs/week}) [ ] Freelancers [ ] Solo
**No-Code:** [ ] Supabase [ ] Vercel/Netlify [ ] Bubble/Webflow [ ] Zapier/Make [ ] Airtable/Notion
**Infrastructure:** [ ] Existing codebase ({X}% reusable) [ ] CI/CD [ ] Cloud (AWS/GCP/Azure) [ ] DevOps

📝 **Brief description:**
```

---

#### Question 2: Development Speed Profile

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❓ **Question 2: What is your development speed?**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[A] **LLM writes code** (10x-50x) | [B] **Traditional** (1x baseline) | [C] **No-code tools** (5x-20x) | [D] **Hybrid** (20x-100x)

📝 **Your profile:** [A/B/C/D]
📖 **Detailed profiles:** {resourceAssessmentExamples}
```

---

#### Question 3: Constraints and Limitations

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❓ **Question 3: What are your constraints?**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Budget:** {amount / unlimited / minimal}
**Time:** {hours/week, deadline, priority}
**Team:** {full-time/part-time, skill gaps, coordination}
**Technical:** {legacy, compliance, platform}

📝 **Primary constraint:** _______________
📖 **Constraint analysis and mitigation:** {resourceAssessmentExamples}
```

---

#### Question 4: Existing Assets

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❓ **Question 4: What assets do you already have?**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

(From Step 0.5 we know completion %. Now assess reusability)

- Existing codebase: {X}% reusable?
- Design system / UI components: {yes/no}
- API integrations (auth, payment, external): {which ready?}
- Test data, user research, docs: {yes/no}

📝 **What can be reused:** _______________
📖 **Complete inventory templates:** {resourceAssessmentExamples}
```

---

### Step-Specific Subprocess Optimization Rules

- 🎯 Load speed multipliers data in subprocess (Pattern 3)
- 💬 Return calculated multiplier only, not full YAML
- ⚙️ TOOL/SUBPROCESS FALLBACK: If subprocess unavailable, achieve outcome in main context thread

### Speed Multiplier Calculation (Subprocess) - Optimization Pattern 3

**Subprocess Strategy:** Loads `data/speed-multipliers.yaml` (352 lines total), extracts ONLY base multiplier for user's selected method (A/B/C/D), applies method-specific adjustments (code %, team, constraints), returns calculated multiplier + formula (50 lines vs 352 full YAML).

**Expected Savings:** ~302 lines (86% reduction in context loading)

**Subprocess Implementation:**

```markdown
Launch subprocess that:
1. Read `data/speed-multipliers.yaml`
2. Match user's method selection:
   - [A] LLM writes code → Extract `base_multipliers.llm_assisted_solo/team` + `adjustment_factors`
   - [B] Traditional → Extract `base_multipliers.traditional_manual` (no adjustments)
   - [C] No-code tools → Extract `base_multipliers.nocode_tools` + `adjustment_factors`
   - [D] Hybrid → Extract `base_multipliers.hybrid_approach` + ALL `adjustment_factors`
3. For selected method, apply adjustments based on:
   - Existing codebase reusability ({Y}%)
   - Infrastructure readiness (basic/intermediate/advanced)
   - Team size (solo/small/medium/large)
   - Budget constraints (minimal/moderate/generous)
   - Time constraints (tight/normal/flexible)
4. Calculate final formula: Base + Adjustments - Penalties
5. Return output (max 50 lines):
   - Selected method + base multiplier
   - Applied adjustments + values
   - Final calculated multiplier
   - Example timeline calculation

Fallback: If subprocess unavailable, load full `data/speed-multipliers.yaml` in main context and perform calculation inline.
```

**Output Format (50 lines max):**
```
⚡ Speed Multiplier Calculation
Selected Method: {A/B/C/D}
Base Multiplier: {X}x

Applied Adjustments:
+ {Codebase reusability}: +{bonus}x
+ {Infrastructure}: +{bonus}x
+ {Team size}: +{bonus}x

Applied Penalties:
- {Budget constraint}: -{penalty}x
- {Time constraint}: -{penalty}x

Final Calculation: {Base} + {Total Adjustments} - {Total Penalties} = {FINAL}x
Timeline Example: 12 weeks (traditional) ÷ {FINAL}x = {12/FINAL} weeks
```

**Fallback:** If subprocess unavailable, load full data in main context.

📖 **Subprocess format and detailed examples:** {resourceAssessmentExamples}

---

### 3. Calculate Speed Multiplier

Based on user answers, calculate Speed Multiplier using data from `{speedMultipliersData}`:

```
⚡ **Speed Multiplier Calculation**

**Base:** {method} = {X}x
**Adjustments:** +{positive_total}x (codebase, tools, team, infra)
**Penalties:** -{penalty_total}x (budget, time, coordination)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**FINAL SPEED MULTIPLIER: {TOTAL}x**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 **Example:** Traditional 12 weeks → Actual: {12/TOTAL} weeks (saved {12-12/TOTAL} weeks)
```

📖 **Detailed calculation examples and formulas:** {resourceAssessmentExamples}

---

### 4. Save Resource Assessment (Dual Storage)

Create file: `{resourceAssessmentFile}` with frontmatter: `id`, `created`, `speedMultiplier: {TOTAL}x`, `developmentMethod: {A/B/C/D}`

**Required sections:**
1. **Available Resources:** Method {A/B/C/D}, Base {X}x, Resources list, Existing assets ({Y}% code, design, data, integrations)
2. **Constraints:** Budget, Time, Team, Technical + Primary constraint
3. **Speed Multiplier:** Base {X}x + Adjustments + Penalties = **FINAL: {TOTAL}x**
4. **Timeline Impact:** Formula: Traditional ÷ {TOTAL}. Example: 12 weeks → {12/TOTAL} weeks
5. **Memory Note:** [Resource assessment. Multiplier: {TOTAL}x. Method: {A/B/C/D}. Next: Optimization intelligence.]

📖 **Complete template:** {resourceAssessmentExamples}

### 5. Update Workflow Plan

Append to {workflowPlanFile}:

```markdown
## Resource Assessment (Step 0.6)
**Speed Multiplier:** {TOTAL}x | **Method:** {A/B/C/D} | **Base:** {X}x
**Resources:** LLM/AI: {tools} | Team: {size} | No-code: {tools} | Existing: {Y}%
**Primary Constraint:** {constraint}
**Timeline Formula:** Traditional Estimate ÷ {TOTAL} (Example: 12 weeks → {12/TOTAL} weeks)
```

Update frontmatter: append `step-00.6-resource-assessment` to `stepsCompleted`.

### 6. Save to Claude Flow Memory

```bash
npx claude-flow@v3alpha memory store --namespace "shared-knowledge" --key "life-os:speed-multiplier:{IDEA_ID}" --content "{TOTAL}x"
npx claude-flow@v3alpha memory store --namespace "shared-knowledge" --key "life-os:resources:{IDEA_ID}" --content "{json_of_resources}"
```

### 7. Confirm Save

```
✅ **Resources assessed!**

Saved: 📄 {resourceAssessmentFile} | 🧠 Claude Flow: life-os:speed-multiplier:{IDEA_ID}
Speed Multiplier: {TOTAL}x (ready for Step 08)

Summary: Method {method} | Multiplier {TOTAL}x | Constraint {constraint} | Example: 12 weeks → {12/TOTAL}

Next: Step 0.7 - optimal approaches for maximum speed.
```

---

### 8. Proceed to Next Step (Auto-Proceed)

Display: "**Moving to optimization intelligence...**"
Then load, read entire file, then execute {nextStepFile}.

#### Menu Handling Logic:
- After completion, immediately save state, then load, read entire file, execute {nextStepFile}

#### EXECUTION RULES:
- **This is an auto-proceed step** (no menu displayed)
- **Do NOT wait** for user menu selection
- **Do NOT display** interactive options
- Save resource assessment to dual storage (Markdown + Claude Flow memory)
- Update workflow plan frontmatter with completion status
- Immediately transition to Step 0.7 (optimization intelligence)

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS
- Method identified (A/B/C/D) | Speed Multiplier calculated (adjustments + penalties)
- Resources inventory + constraints documented | Timeline formula for Step 08
- Saved to Markdown + Claude Flow memory | User understands time savings

### ❌ SYSTEM FAILURE
- Assuming 1x speed by default | Not asking about LLM | Not calculating Speed Multiplier
- Ignoring existing assets | Not identifying constraints | Not saving to both storages

**Master Rule:** NEVER assume 1x speed. ALWAYS calculate real Speed Multiplier. Modern tools are 10x-100x faster.

**Critical Impact:** Without this step, timelines ignore LLM acceleration and are wrong by 10x-50x.
