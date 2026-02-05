# Deep Plan Auto-Intelligence Protocols

**Purpose:** AI-powered auto-linking, auto-population, and scenario mapping for Deep Plan generation

**Reference from:** step-08-deep-plan.md

---

## Auto-Linking Protocol

**Before generating Deep Plan, AI scans for auto-linkable data across:**

1. **Workflow Plan** (Design Thinking, Consilium, Scoring)
2. **Framework Templates** (if multiple frameworks filled)
3. **Claude Flow Memory** (patterns from similar projects)

### Auto-Linking Rules

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

### User Interaction

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

### Memory Integration

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

---

## L2 Auto-Population Rules

**After auto-linking completes, check for L2 phase auto-population.**

### OKRs Framework Present

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

### NPV/Finance Framework Present

```
💡 **L2 Auto-Population Available**

Your NPV has {year_count} year timeline.
I can auto-generate L2 phases:

NPV Year 1-2 → L2 Phase 1: {first_milestone}
NPV Year 3-5 → L2 Phase 2: {second_milestone}
...

Use this structure? [✅ Yes] [✏️ Customize] [❌ Manual]
```

---

## L5 Auto-Population Rules

**After L2 populated, check L5 (daily tasks).**

### Pomodoro/Habit Loop Present

```
💡 **L5 Auto-Population Available**

Your Habit Loop has daily cue at {time}.
Auto-populate L5 daily tasks?

L5-1: {7:00 AM} - {habit_response} ({habit_loop})
L5-2: {time} - {pomodoro_task_1}
L5-3: {time} - {pomodoro_task_2}

Use this schedule? [✅ Yes] [✏️ Customize] [❌ Manual]
```

---

## Scenario Mapping (Semantic)

**Infer scenario by meaning (not keywords) using Search Orchestrator:**

1. CLI Claude Flow memory search to find nearest scenario template
2. Local MD search in plans/snapshots for similar cases
3. Web/MCP search only if ambiguity remains

**Scenario Templates:**
- Tech Expert / Architect
- Research / Discovery
- Ops / Delivery Helper
- Product / Strategy Contributor
- Invited Role (unclear contribution) as fallback

**Template Loading:**
- Use `../data/deep-plan-templates.md` as index
- Load only relevant `.part-*.md` template file
- If subprocess available, load in subprocess and return outline

**Mixed Scenarios:**
- If multiple scenarios match, use **Mixed Scenario** (combine top 2 templates)
- Merge unique nodes and remove duplicates

---

For complete Deep Plan execution, see: step-08-deep-plan.md
