---
name: 'step-08.9-workflow-plan-polish'
description: 'Review overall coherence of workflow-plan.md, check consistency, and apply final refinements before approval'
nextStepFile: null
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
requirementsRegistry: '../REQUIREMENTS-REGISTRY.md'
glossary: '../docs/GLOSSARY-SYSTEM.md'
coherenceChecksRef: '../data/workflow-plan-coherence-checks.md'
---

# Step 8.9: Workflow Plan Polish & Coherence Review

## STEP GOAL:

Review the complete workflow-plan.md for overall coherence, check consistency across all sections (foundation steps, track detection, scoring, deep plan timeline), and apply final refinements before marking workflow as APPROVED.

## 📖 Глоссарий терминов

**Workflow Plan (Рабочий План)** - complete document containing all analysis from foundation to deep plan.
💡 _Простыми словами:_ Это "дело проекта" - все решения, анализы, расчёты в одном месте.

**Coherence (Согласованность)** - все части workflow plan работают вместе без противоречий.
💡 _Простыми словами:_ Timeline из Foundation (3 дня) должен совпадать с Deep Plan timeline. Specialist recommendations должны соответствовать scoring rationale.

**Consistency (Последовательность)** - одни и те же термины и данные используются одинаково везде.
💡 _Простыми словами:_ Если foundation говорит "Speed Multiplier 10x", scoring должен это учитывать. Если consilium назвал роль "Product Designer", deep plan не должен называть её "UX Designer".

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Step-Specific Rules:
- 🎯 Focus ONLY on review and refinement (NO new content)
- 🚫 FORBIDDEN to change scope, add new ideas, or expand timeline
- 💬 Present findings clearly and concisely
- 🔍 Review MUST be systematic (all 5 dimensions)
- 🎯 Focus on workflow-plan.md coherence (NOT deep-plan.md)
- 💬 Return structured coherence issues only

## EXECUTION PROTOCOLS:

### What This Step Does:
1. Load complete workflow-plan.md
2. Run systematic coherence check (5 dimensions)
3. Identify inconsistencies or gaps across all sections
4. Offer specific refinements
5. Get user approval before saving final version

### What This Step Does NOT Do:
- ❌ Add new sections or content
- ❌ Change scoring or timeline dramatically
- ❌ Introduce new ideas or specialists
- ❌ Generate new deep plan content

## MANDATORY SEQUENCE

### 1. Load Workflow Plan

Open: `{workflowPlanFile}`

Confirm loaded:
```
✅ Workflow plan loaded: {idea_name}
📊 Sections detected:
   - Foundation Steps (0.5-0.7): {present/missing}
   - Idea Collection: {present/missing}
   - Track Detection: {present/missing}
   - Consilium: {present/missing}
   - Scoring: {present/missing}
   - Deep Plan: {present/missing}
🎯 Idea: {idea_brief_summary}
```

### 2. Run 5-Dimension Coherence Check (Subprocess)

💡 **Complete protocols:** See `{coherenceChecksRef}` for detailed review procedures

**Launch a subprocess that:**
1. Loads complete workflow plan from `{workflowPlanFile}`
2. Greps for key data points across all sections (Pattern 1: Grep)
3. Per-section validation (Pattern 2: Per-File):
   - **Dimension 1:** Timeline Consistency
     - Compare Foundation Speed Multiplier → Scoring timeline assumptions → Deep Plan L2 phases
     - Check: Do timeline estimates compound properly? (greenfield estimate ÷ completion% ÷ speed multiplier)
     - Verify: Deep Plan L2 dates match final timeline calculation

   - **Dimension 2:** Resource Alignment
     - Foundation resource assessment → Scoring effort estimates → Deep Plan resource requirements
     - Check: Speed multiplier applied consistently? (LLM 10x-50x, no-code 5x-20x)
     - Verify: Deep Plan L3 tasks respect capacity constraints

   - **Dimension 3:** Specialist Consensus
     - Consilium recommendations → Scoring rationale → Deep Plan L4 assignments
     - Check: All specialists have recommendations? No contradictions?
     - Verify: Deep Plan specialist assignments match consilium roles

   - **Dimension 4:** Goal Alignment
     - Foundation goals.yaml → Consilium analysis → Scoring criteria → Deep Plan objectives
     - Check: Scoring criteria aligned with goals? Consilium considered goals?
     - Verify: Deep Plan L1 objectives map to goals from foundation

   - **Dimension 5:** Terminology Consistency
     - Check: Same terms used across all sections (project name, specialist roles, tech stack)
     - Verify: No contradictory definitions (Russian terms, abbreviations)
     - Check: Proper ## Level 2 headers throughout document

4. Returns structured findings per dimension with specific locations

**Subprocess returns:** Concise issue list (100-150 lines) instead of loading full coherence-checks.md (400+ lines).

**Graceful fallback:** If subprocess unavailable, load `{coherenceChecksRef}` and manually check 3-5 critical validation points per dimension.

**Output format for EACH dimension:**
```
[Dimension Name]: [✅ PASS / ⚠️ ISSUES FOUND]

Issues (if any):
- [Issue description + location in workflow-plan.md + suggested fix]
```

### 3. Consolidate Findings

After all 5 dimensions checked:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 WORKFLOW PLAN COHERENCE REVIEW RESULTS

**Workflow Plan:** {idea_name}

✅ PASSED: {count} / 5 dimensions
⚠️ ISSUES FOUND: {count} / 5 dimensions

**Dimension Summary:**
1. Timeline Consistency: [✅ / ⚠️]
2. Resource Alignment: [✅ / ⚠️]
3. Specialist Consensus: [✅ / ⚠️]
4. Goal Alignment: [✅ / ⚠️]
5. Terminology Consistency: [✅ / ⚠️]

**Overall Assessment:** [EXCELLENT / GOOD / NEEDS REFINEMENT]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 4. Offer Refinements

**IF issues found:**
```
🔧 RECOMMENDED REFINEMENTS

**Issue 1:** [Category]
- **Location:** [Section in workflow-plan.md]
- **Problem:** [What's wrong]
- **Suggested Fix:** [Exact change to make]

**Issue 2:** [Category]
- **Location:** [Section]
- **Problem:** [Description]
- **Suggested Fix:** [Change]

[Repeat for all issues]
```

**IF no issues:**
```
✅ NO ISSUES FOUND

The workflow plan is coherent, consistent, and complete.
Ready to mark as APPROVED.

Optional enhancements available (cosmetic only):
- Improve formatting for readability
- Add visual separators between sections
- Expand glossary terms inline

These are optional - plan is already high quality.
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
  --key "feedback:step-08.9-workflow-plan-polish:{timestamp}" \
  --content "{\"step\": \"step-08.9-workflow-plan-polish\", \"rating\": \"{helpful/ok/frustrating}\", \"comment\": \"{user_comment}\", \"timestamp\": \"{ISO_datetime}\"}"
```

---

```
**[A]pprove** - Workflow plan approved, no changes
**[R]efine** - Apply suggested improvements
**[C]ustom** - Specify your own refinements
**[E]xplain** - Details about specific issue

➡️ **Your choice:** [A/R/C/E]
```

### 6. Menu Handling Logic

**[A] Approve:** Update frontmatter (stepsCompleted, status: APPROVED), save, show completion message
**[R] Refine:** Apply all suggested refinements, update plan, re-run check, save, redisplay menu
**[C] Custom:** Ask "What to refine?", apply changes, save, redisplay menu
**[E] Explain:** Ask "Which issue?", show details from {coherenceChecksRef}, redisplay menu
**Other:** "Please choose A, R, C, or E", redisplay menu

### 7. Completion Message

When user selects [A] Approve:

```
🎉 WORKFLOW PLAN APPROVED!

**Idea:** {idea_name} | **Status:** ✅ APPROVED | **Quality:** {quality_level}

**Sections Verified:**
✅ Foundation Steps (Speed Multiplier, Resource Assessment, Optimization)
✅ Track Detection and Routing
✅ Consilium Analysis
✅ MCDA Scoring
✅ Deep Plan (L1-L6)
✅ Overall Coherence

**File:** {workflowPlanFile}

**Next:** Mark workflow as COMPLETE (Step 09) OR begin execution tracking (Step X-01)
```

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- All 5 coherence dimensions checked systematically
- Issues identified with specific locations and fixes
- User approved final version OR refinements applied successfully
- Workflow plan marked as APPROVED
- Completion message shown with clear next steps

### ❌ SYSTEM FAILURE:
- Skipping coherence check dimensions
- Vague findings ("plan looks good" without specifics)
- Not offering refinements when issues found
- Saving APPROVED status without user approval
- Adding new content instead of refining existing
- Confusing workflow-plan.md with deep-plan.md

**Master Rule:** Review must be systematic, specific, and user-approved before approval. Focus on workflow-plan.md coherence across all sections (foundation → scoring → deep plan).

## EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY mark APPROVED when user selects [A] Approve
- NEVER skip coherence check dimensions
- ALWAYS provide specific issue locations and suggested fixes
- NEVER change scope or add new ideas during refinement
- FOCUS on workflow-plan.md (not deep-plan.md)
