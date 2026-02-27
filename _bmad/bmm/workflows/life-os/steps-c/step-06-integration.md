---
name: 'step-06-integration'
description: 'Classify project, assess portfolio health, and define integration plan'
nextStepFile: './step-07-calendar-sync.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
decisionsLog: '{bmb_creations_output_folder}/life-os/decisions/decision-log.md'
strategicBucketsRef: '../data/strategic-buckets.md'
portfolioHealthRef: '../data/portfolio-health.md'
integrationPatternsRef: '../data/integration-patterns.md'
workflowMappingRef: '../data/bmad-workflow-mapping.md'
timelineRef: '../data/timeline-allocation.md'
wipRef: '../data/wip-enforcement.md'
portfolioTemplatesRef: '../data/portfolio-templates.md'
portfolioAlignmentRef: '../data/portfolio-alignment-scoring.md'
portfolioWipRef: '../data/portfolio-wip-management.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 6: Portfolio Integration

## STEP GOAL:

Classify project, assess portfolio health, define integration approach, and document integration plan.

## MANDATORY EXECUTION RULES:

- 🛑 NEVER generate without user input | 📖 Read complete step first | 🔄 Read entire next step when loading
- 📋 FACILITATOR role only | ⚙️ Subprocess fallback: achieve outcome in main thread
- ✅ Speak in `{communication_language}` | 🤝 Highlight risks/opportunities proactively
- 🧭 Surface WIP/kill criteria early | ✅ Confirm before changing scope | 🎯 Integration focus only
- 🚫 NEVER change step-05 scores | 💬 1-2 questions max | 💬 Load only relevant sharded parts
- 🎯 Use subprocess for WIP capacity check (Pattern 1 + Pattern 3)
- 💬 Return ONLY WIP status summary, not full portfolio files

## EXECUTION PROTOCOLS:

**MCP/Search:** If unclear, use MCP search → consilium ranks 2-4 options → user chooses

**Data Ops:** Load only relevant parts from {strategicBucketsRef}, {portfolioHealthRef}, {integrationPatternsRef}, {workflowMappingRef}, {timelineRef}, {wipRef}. Use subprocess if available, otherwise manual. Explicitly validate that active projects stay within the IDEAL capacity limit (max 2–3 simultaneously active), tie the integration plan back to the goals cascade (1/3/5/10-year intent), and flag any deviations so subsequent reviews can correct course.

**Outputs:** Append to {workflowPlanFile} | Record in {decisionsLog} | Use {portfolioTemplatesRef}, {portfolioAlignmentRef}, {portfolioWipRef} for JIT guidance

**Context:** Workflow plan (idea + scoring) | Focus: portfolio fit | Dependency: step-05 complete

## MANDATORY SEQUENCE

### 1. Classify Strategic Bucket
Use {strategicBucketsRef} + {portfolioAlignmentRef} to classify. Confirm with user, capture reasoning.


### 2. Check Portfolio Health
#### WIP Capacity Check (Subprocess - Pattern 1 + Pattern 3)

**Launch a subprocess that:**
1. **Grep operation (Pattern 1):** Searches portfolio folder (from {workflowPlanFile} config or {bmb_creations_output_folder}/life-os/portfolio/) for `status: IN_PROGRESS` across all project files
2. **Count:** Calculates current active project count
3. **Load WIP rules (Pattern 3):** From `{wipRef}` extracts WIP limit (usually 3 for personal portfolios, 5+ for teams)
4. **Check threshold (Pattern 3):** From `{portfolioWipRef}` determines health status:
   - 🟢 0-66% of limit (0-2 for limit=3) = healthy
   - 🟡 67-99% of limit (2 for limit=3) = approaching (warning)
   - 🔴 100%+ of limit (3+ for limit=3) = FULL (blocking, must defer/kill/override)
5. **Returns ONLY:** current_count, limit, status_emoji, available_slots, decision_options (if over limit) (~10-15 lines)

**Subprocess returns:** WIP status summary instead of full portfolio files + WIP guides

**Example output:**
```
WIP Status: 🟡 APPROACHING (2/3 projects active)
Available slots: 1
Status: Can accept 1 more project before FULL
```

**Graceful fallback:** If subprocess unavailable:
1. Grep portfolio folder in main context: `rg "status: IN_PROGRESS" {portfolio_folder}`
2. Count matches manually
3. Load WIP limit from {wipRef} manually
4. Determine status manually using {portfolioWipRef} rules

**Context Savings:** ~950 lines (full portfolio project files + WIP enforcement guide + WIP management guide) → ~10-15 lines (status summary) = ~935-940 lines saved

Use {portfolioHealthRef} + {portfolioAlignmentRef} to assess allocation and WIP. If subprocess available, compute there. If unhealthy, discuss rebalancing (see {portfolioAlignmentRef}). User decides.

### 3. Define Integration Approach
Use {integrationPatternsRef} + {portfolioTemplatesRef} for pattern (Standalone/Platform Extension/Bundle/Enabler). Confirm dependencies. If multiple fit, Search Orchestrator ranks 2-3 options.

### 4. Suggest BMAD Workflow
Use {workflowMappingRef} to suggest workflow. Confirm: start now/defer/skip.

### 5. Propose Timeline & Resources
Use {timelineRef}: start date, end/duration, weekly capacity. Confirm with user.

### 6. Enforce WIP Limit
Check WIP using {wipRef} + {portfolioWipRef}:
- 🟢 0-2/3 healthy | 🟡 2/3 approaching | 🔴 3/3 FULL (must defer/kill/override)

If exceeded, present options (see {portfolioWipRef}). User confirms choice.

### 7. Ensure Decision Log Exists
If {decisionsLog} missing, create with template from {portfolioTemplatesRef}. Otherwise append decision.

### 8. Append Integration Summary
Use template from {portfolioTemplatesRef} to append to {workflowPlanFile}.

### 9. Stage Gate: Plan Readiness DoD
Confirm: summary complete, WIP decided, timeline agreed, user approves calendar sync.
Append gate decision using {portfolioTemplatesRef} template.

### 10. Present MENU OPTIONS

**Quick Feedback:** 👍 Helpful | 😐 OK | 👎 Frustrating [Enter to skip]

Save feedback:
```bash
npx claude-flow@v3alpha memory store --namespace "user-context" \
  --key "feedback:step-06-integration:{timestamp}" \
  --content "{\"step\":\"step-06-integration\",\"rating\":\"{rating}\",\"comment\":\"{comment}\",\"timestamp\":\"{ISO}\"}"
```

**Select:** [A] Advanced Elicitation [P] Party Mode [C] Continue

**Logic:**
- A: Execute {advancedElicitationTask} to refine portfolio fit → redisplay menu
- P: Execute {partyModeWorkflow} for alternative approaches → redisplay menu
- C: Save to {workflowPlanFile}, update frontmatter, read and execute {nextStepFile}
- Other: Help user → redisplay menu

**Rules:** HALT after menu | Proceed ONLY on 'C' | Return after A/P

## SUCCESS/FAILURE

**✅ SUCCESS:** Bucket confirmed | Health assessed | Pattern documented | Timeline agreed | WIP decided

**❌ FAILURE:** Skipped confirmations | No workflow plan append | Missing WIP decision

**Master Rule:** Integration requires explicit confirmation and recorded decisions.




