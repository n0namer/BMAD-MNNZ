---
name: 'step-08.5-final-polish'
description: 'Review overall coherence, check consistency, and apply final refinements before completion'
nextStepFile: null
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
requirementsRegistry: '../REQUIREMENTS-REGISTRY.md'
glossary: '../docs/GLOSSARY-SYSTEM.md'
coherenceChecksRef: '../data/final-polish-coherence-checks.md'
---

# Step 8.5: Final Polish & Coherence Review

## STEP GOAL:

Review the complete workflow plan for overall coherence, check consistency across all sections, and apply final refinements before marking workflow as COMPLETE. Tie the refinements to the IDEAL PDCA loop (IDEAL 1.5) by flagging what will go into the next daily/weekly review and storing the high-level learnings in shared memory for future patterns (IDEAL 1.4).

## 📖 Глоссарий терминов

**Coherence (Согласованность)** - все части плана работают вместе без противоречий.
💡 _Простыми словами:_ Как в пазле - все кусочки должны подходить друг к другу. Если timeline говорит "3 недели", а scoring предполагает "12 недель работы" → нет coherence.

**Consistency (Последовательность)** - одни и те же термины и данные используются одинаково везде.
💡 _Простыми словами:_ Если в одном месте назвал проект "Katana", а в другом "Saas for Beauty" → inconsistency.

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
- 🎯 Use subprocess for Deep Plan coherence validation (Pattern 1 + Pattern 2: Grep + Per-File)
- 💬 Return structured coherence issues only

## EXECUTION PROTOCOLS:

### What This Step Does:
1. Load complete workflow plan
2. Run systematic coherence check (5 dimensions)
3. Identify inconsistencies or gaps
4. Offer specific refinements
5. Get user approval before saving final version

### What This Step Does NOT Do:
- ❌ Add new sections or content
- ❌ Change scoring or timeline dramatically
- ❌ Introduce new ideas or specialists

## MANDATORY SEQUENCE

### 1. Load Workflow Plan

Open: `{workflowPlanFile}`

Confirm loaded:
```
✅ Workflow plan loaded: {idea_name}
📊 Current status: {current_status}
🎯 Idea: {idea_brief_summary}
```

### 2. Run 5-Dimension Coherence Check (Subprocess)

💡 **Complete protocols:** See `{coherenceChecksRef}` for detailed review procedures

**Launch a subprocess that:**
1. Loads complete workflow plan from `{workflowPlanFile}`
2. Loads Deep Plan section with L1-L6 structure
3. Greps for timeline references across all sections (Pattern 1: Grep)
4. Per-file validation of each dimension (Pattern 2: Per-File):
   - **Dimension 1:** Timeline Consistency - Compare Foundation Steps (0.5/0.6/0.7) dates, Deep Plan timeline, scoring assumptions
   - **Dimension 2:** Goal Alignment - Check consilium → goals.yaml → scoring chain
   - **Dimension 3:** Specialist Consistency - Verify all specialists have recommendations, no contradictions
   - **Dimension 4:** Terminology Consistency - Check terms, Russian definitions, abbreviations
   - **Dimension 5:** Completeness - Verify required sections, no TBD/placeholders, valid references
5. Returns structured findings per dimension with specific locations

**Subprocess returns:** Concise issue list (100-150 lines) instead of loading full final-polish-coherence-checks.md (400+ lines).

**Graceful fallback:** If subprocess unavailable, load `{coherenceChecksRef}` and manually check 3-5 critical validation points per dimension.

**Output format for EACH dimension:**
```
[Dimension Name]: [✅ PASS / ⚠️ ISSUES FOUND]

Issues (if any):
- [Issue description + location + suggested fix]
```

### 3. Consolidate Findings

After all 5 dimensions checked:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 COHERENCE REVIEW RESULTS

**Workflow Plan:** {idea_name}

✅ PASSED: {count} / 5 dimensions
⚠️ ISSUES FOUND: {count} / 5 dimensions

**Dimension Summary:**
1. Timeline Consistency: [✅ / ⚠️]
2. Goal Alignment: [✅ / ⚠️]
3. Specialist Consistency: [✅ / ⚠️]
4. Terminology Consistency: [✅ / ⚠️]
5. Completeness: [✅ / ⚠️]

**Overall Assessment:** [EXCELLENT / GOOD / NEEDS REFINEMENT]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 4. Offer Refinements

**IF issues found:**
```
🔧 RECOMMENDED REFINEMENTS

**Issue 1:** [Category]
- **Location:** [Section in workflow plan]
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
Ready to mark as COMPLETE.

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
  --key "feedback:step-08.5-final-polish:{timestamp}" \
  --content "{\"step\": \"step-08.5-final-polish\", \"rating\": \"{helpful/ok/frustrating}\", \"comment\": \"{user_comment}\", \"timestamp\": \"{ISO_datetime}\"}"
```

---

```
**[A]pprove** - Plan complete, no changes
**[R]efine** - Apply suggested improvements
**[C]ustom** - Specify your own refinements
**[E]xplain** - Details about specific issue

➡️ **Your choice:** [A/R/C/E]
```

### 6. Menu Handling Logic

**[A] Approve:** Update frontmatter (stepsCompleted, status: COMPLETE), save, show completion message
**[R] Refine:** Apply all suggested refinements, update plan, re-run check, save, redisplay menu
**[C] Custom:** Ask "What to refine?", apply changes, save, redisplay menu
**[E] Explain:** Ask "Which issue?", show details from {coherenceChecksRef}, redisplay menu
**Other:** "Please choose A, R, C, or E", redisplay menu

### 7. Completion Message

When user selects [A] Approve:

```
🎉 WORKFLOW PLAN COMPLETE!

**Idea:** {idea_name} | **Status:** ✅ COMPLETE | **Quality:** {quality_level}

**Created:** Workflow plan, Foundation data, Consilium, Deep plan (L1-L6), Scoring, Coherence review
**File:** {workflowPlanFile}

**Next:** Switch to Validate mode (V) to track progress OR start implementation
```

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- All 5 coherence dimensions checked systematically
- Issues identified with specific locations and fixes
- User approved final version OR refinements applied successfully
- Workflow plan marked as COMPLETE
- Completion message shown with clear next steps

### ❌ SYSTEM FAILURE:
- Skipping coherence check dimensions
- Vague findings ("plan looks good" without specifics)
- Not offering refinements when issues found
- Saving COMPLETE status without user approval
- Adding new content instead of refining existing

**Master Rule:** Review must be systematic, specific, and user-approved before completion.

## EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY mark COMPLETE when user selects [A] Approve
- NEVER skip coherence check dimensions
- ALWAYS provide specific issue locations and suggested fixes
- NEVER change scope or add new ideas during refinement
