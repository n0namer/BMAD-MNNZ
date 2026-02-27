---
name: 'step-v-07-decision-queue'
description: 'Display evaluated ideas awaiting GO/NO-GO activation decision'
nextStepFile: './step-v-05-retrospective.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
portfolioFile: '{bmb_creations_output_folder}/life-os/portfolio.md'
estimatedDuration: '5-10 minutes'
---

# Validation Step V-07: Decision Queue View

## STEP GOAL

Display all evaluated ideas with status=PLANNED that have completed scoring and deep planning, awaiting user's final GO/NO-GO activation decision. Show prioritized queue with key decision factors.

## WHEN TO USE

- **After scoring phase:** Review which ideas are ready to activate
- **During capacity planning:** Decide which planned idea to activate next
- **Weekly/monthly review:** Assess decision queue and priorities
- **On-demand:** Any time user needs to see pending decisions

## MANDATORY EXECUTION RULES (READ FIRST)

### Universal Rules
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Step-Specific Rules
- 🎯 Load workflow plan and portfolio for context
- 🎯 Use subprocess for decision queue analysis (Pattern 2: LLM Operations)
- 💬 Return structured decision queue, not raw workflow plan
- 📊 Display ideas ranked by score (highest first)
- 🎯 Show decision factors: score, capacity fit, dependencies, risks
- 💡 Provide activation recommendations based on context
- ✅ Allow activation decision from this view
- 🚫 FORBIDDEN to auto-activate without user confirmation

## EXECUTION PROTOCOLS

### Proactive Advice & Best Practices
- If user asks for decision-making guidance, use Search Orchestrator to retrieve best practices
- Provide context-aware recommendations based on portfolio state

### Search Orchestrator Protocol (Optional)
- Follow data/search-decision-protocol.md
- Execute: CLI memory search → local MD (rg) → web/MCP
- Use for: activation decision patterns, capacity planning strategies

## CONTEXT BOUNDARIES

- Available context: {workflowPlanFile}, {portfolioFile}
- Focus: PLANNED ideas with completed scoring/planning
- Filter: Only ideas with status=PLANNED or status=PLANNED_EVALUATED
- Action: Can trigger activation (transition to IN_PROGRESS)

## MANDATORY SEQUENCE

### 1. Load Decision Queue Data (Subprocess)

**Launch a subprocess that:**
1. Loads {workflowPlanFile} (all ideas)
2. Loads {portfolioFile} (current capacity and constraints)
3. Filters ideas with status=PLANNED and completed Deep Plan (step-08)
4. Ranks by score (descending)
5. Analyzes decision factors for each idea
6. Returns structured decision queue

**Subprocess filters for:**
- **Status:** PLANNED or PLANNED_EVALUATED
- **Completion:** Deep Plan (step-08) completed
- **Exclude:** Ideas without scoring or planning data

**Subprocess returns structured JSON with:**
- queue_summary (total, ready, blocked, needs_replan)
- capacity_context (current_active, max_capacity, available_slots)
- decision_queue (ranked list with full analysis)
- portfolio_recommendations (actionable suggestions)

📖 **Subprocess calculation rules:** `data/decision-prioritization-algorithm.md`
📖 **Queue data structure:** `data/decision-queue-management.md`

**Context savings:** ~2,000 lines (workflow plan + portfolio) → ~400 lines (structured decision queue)

**Graceful fallback:** If subprocess unavailable, load files in main context and filter/analyze manually.

---

### 2. Generate Decision Queue Report

**Display formatted markdown report with:**
- Queue summary (total, ready, blocked, needs_replan)
- Capacity context (current/max, available slots)
- Prioritized queue (ranked by score, readiness indicators 🟢🟡🔴)
- Per-idea: ID, readiness %, duration, risk, dependencies, recommendation
- Portfolio recommendations

📖 **Complete report template:** `data/decision-queue-management.md`

---

### 3. Display Menu Options

**Options:** [A]ctivate | [D]etails | [K]ill | [P]ostpone | [R]efresh | [B]ack to portfolio | [C]ontinue

---

### 4. Menu Handling Logic

**[A] Activate idea:**
1. Ask: "Which idea to activate? (Enter ID or rank #)"
2. Validate capacity and dependencies (see escalation rules)
3. Confirm: "Activate {idea_name}? This will transition to IN_PROGRESS. [Confirm/Cancel]"
4. IF confirmed: Execute step-x-01-kickoff.md, update status, create tracker, refresh queue

**[D] Details on idea:**
- Load Deep Plan (step-08 output), display L1-L6 structure, return to menu

**[K] Kill idea:**
- Confirm (irreversible), request reason, update status, archive, store decision, refresh queue

**[P] Postpone idea:**
- Request reason, update status to PLANNED_PAUSED, store reason, refresh queue

**[R] Refresh queue:**
- Re-execute Section 1 (reload data), re-display queue

**[B] Back to portfolio:**
- Load, read entire file, then execute step-v-06-portfolio-view.md

**[C] Continue:**
- Load, read entire file, then execute {nextStepFile} (retrospective)

📖 **Escalation rules:** `data/decision-escalation-rules.md`

---

### 5. Save Decision Records

**After any activation/kill/postpone decision:**

```bash
# Store decision in memory
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "decisions:activation:{idea_id}:{date}" \
  --content "{decision_type, idea_id, idea_name, reasoning, timestamp}"

# Log to decision journal
DECISION_LOG="{bmb_creations_output_folder}/life-os/output/decision-log.md"
echo "## {date} - {decision_type}: {idea_name}" >> "$DECISION_LOG"
echo "- **Score:** {score}" >> "$DECISION_LOG"
echo "- **Reasoning:** {reasoning}" >> "$DECISION_LOG"
echo "" >> "$DECISION_LOG"
```

---

## 🚨 SUCCESS CRITERIA

**Queue loaded in subprocess**, ideas ranked by score, decision factors shown (readiness, dependencies, risk, capacity), recommendations provided, activation seamless, decisions recorded.

**FAILURES:** Loading full plan in main context, missing filters/factors, no capacity check, decisions not logged.

## INTEGRATION

**From:** step-v-06 (Portfolio Dashboard) → [V] View Decision Queue
**To:** step-x-01 (Activate) | step-v-05 (Continue to Retrospective)

---

## RELATED FILES

📖 Workflow plan: `{workflowPlanFile}`
📖 Portfolio: `{portfolioFile}`
📖 Prioritization: `data/decision-prioritization-algorithm.md`
📖 Queue management: `data/decision-queue-management.md`
📖 Escalation: `data/decision-escalation-rules.md`
📖 Next step (activate): `steps-x/step-x-01-kickoff.md`
📖 Next step (continue): `{nextStepFile}` (Retrospective)

---

**Master Rule:** This is the decision-making hub for evaluated ideas. Provide clear, ranked queue with all decision factors. Make activation seamless. Record all decisions for learning.
