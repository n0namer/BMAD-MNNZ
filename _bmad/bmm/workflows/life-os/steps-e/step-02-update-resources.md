---
name: 'step-02-update-resources'
description: 'Update portfolio resources: capacity, budget allocation, timeline constraints'
nextStepFile: './step-01-update-project.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
portfolioFolder: '{bmb_creations_output_folder}/life-os'
metricsFile: '{bmb_creations_output_folder}/life-os/metrics/metrics.md'
journalFolder: '{bmb_creations_output_folder}/life-os/journal'
---

# Edit Step 2: Update Resources

## STEP GOAL:

Manage portfolio-level resources: update personal capacity, adjust budget allocations, track timeline constraints, monitor WIP limits.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', read entire file
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Step-Specific Rules:
- 🤝 Proactive guidance: flag capacity overallocation and timeline risks
- 🧭 If WIP limit exceeded → Flag immediately with recommendations
- ✅ Ask for user confirmation before major capacity changes
- 🎯 Focus ONLY on resource management
- 🚫 FORBIDDEN to modify individual project details (use step-01 instead)
- 💬 Confirm all changes with the user
- 💬 Ask 1–2 questions at a time and adapt to responses

## EXECUTION PROTOCOLS:

### Resource Management Protocol
- Capacity is measured in hours/week available for projects
- WIP limit is max concurrent projects (typically 3)
- Timeline constraints affect all projects (e.g., vacation, conference)
- Budget tracks investment per strategic bucket

### Search Orchestrator Protocol (If user asks for capacity planning)
- Follow data/mcp_search_system_prompt_xml.md
- Execute: CLI memory search → local MD → web/MCP
- Suggest capacity allocation patterns

---

## MANDATORY SEQUENCE

### 1. Select Resource Action

Ask:
"Что вы хотите обновить в ресурсах портфеля?

[C]apacity - Изменить еженедельную ёмкость (часы)
[W]IP - Обновить лимит одновременных проектов
[T]imeline - Добавить временные ограничения (отпуск, события)
[B]udget - Обновить бюджет и распределение средств
[O]ther - Другое

Укажите: [C] / [W] / [T] / [B] / [O]"

### 2A. IF CAPACITY - Update Available Hours

Ask:
"Сколько часов в неделю вы можете инвестировать в проекты?

Текущий: {current} часов/неделю
Новое значение: [0-60] часов"

After input, calculate impact:
```
📊 Capacity Impact Analysis

Current WIP: {X projects, Y hours}
Available: {Z hours}

Impact:
- Current projects: {utilization}%
- Free capacity: {free} hours
- Overallocated: {Y - Z < 0 ? "YES ⚠️" : "NO ✅"}

{If overallocated: "⚠️ ALERT: Projects exceed capacity. Recommendations:
  1. Reduce WIP (currently {X}, recommend max {X-1})
  2. Extend timelines
  3. Delegate or pause lower-priority project"}
```

### 2B. IF WIP - Update Concurrent Project Limit

Ask:
"Сколько проектов можете вести одновременно?

Текущий лимит: {current} проектов
Новый лимит: [1-5] проектов"

After input, check WIP health:
```
📊 WIP Status

Current WIP: {X projects}
New WIP limit: {Y projects}

Active Projects:
1. {Project1} - {status}
2. {Project2} - {status}
...

{If X > Y: "⚠️ ALERT: Current WIP ({X}) exceeds new limit ({Y}).
Recommendations:
  1. Complete or pause {X-Y} projects
  2. Move {X-Y} to backlog
  3. Adjust timeline or defer"}
```

### 2C. IF TIMELINE - Add Constraints

Ask:
"Добавьте ограничение по времени на портфель.

Тип:
[V]acation - Отпуск (недоступны даты)
[C]onference - Конференция или событие
[B]uild - Строительство/переезд (занято время)
[O]ther - Другое

Укажите тип: [V] / [C] / [B] / [O]"

Capture:
- Event name
- Start date
- End date
- Impact on portfolio (e.g., "No new starts", "50% capacity", "Full pause")

Add to timeline constraints and recalculate all project timelines.

### 2D. IF BUDGET - Update Allocation

Ask:
"Обновите бюджет портфеля.

Текущий бюджет: ${current} (период: {period})
Новый бюджет: ${new} (период?)"

Then ask for allocation across strategic buckets:
```
Распределение по направлениям:

Strategic Buckets:
1. {Bucket1}: {X%} = ${amount}
2. {Bucket2}: {Y%} = ${amount}
3. {Bucket3}: {Z%} = ${amount}

Измените процент для каждого [0-100%]:
```

Calculate and show allocation:
```
📊 Budget Allocation

Total: ${total}

{Bucket1}: {X%} = ${amount}
  └─ Projects: {count}
  └─ Avg per project: ${per_project}

{Bucket2}: {Y%} = ${amount}
  └─ Projects: {count}
  └─ Avg per project: ${per_project}

{Bucket3}: {Z%} = ${amount}
  └─ Projects: {count}
  └─ Avg per project: ${per_project}

⚠️ Underfunded buckets: {list if any}
```

### 3. Document Changes

Append to {workflowPlanFile}:
```markdown
## Edit: Resource Management

**Date:** {date}
**Action:** {CAPACITY | WIP | TIMELINE | BUDGET}

**Changes:**
- {Change 1}
- {Change 2}

**Portfolio Impact:**
- Utilization: {X%}
- WIP Status: {status}
- Timeline Risks: {count}
- Budget Status: {status}
```

Update {metricsFile} with new resource baseline.

Append to {journalFolder}/resources-journal.md:
```markdown
### {Date}: {Action}

{Summary of resource change}

Rationale: {Why this change?}

Impact on existing projects:
- {Project1}: {Impact}
- {Project2}: {Impact}
```

### 4. Display Resource Summary

Show updated resource landscape:
```
✅ Resources Updated

Portfolio Capacity:
- Available: {X} hours/week
- Current WIP: {Y} projects (limit: {Z})
- Utilization: {U}%

Timeline Constraints:
- {Constraint1}: {date range}
- {Constraint2}: {date range}
- Impact on projects: {count}

Budget:
- Total: ${amount}
- Allocated: {X%}
- Available: {Y%}

Strategic Buckets:
- {Bucket1}: {percentage}
- {Bucket2}: {percentage}
- {Bucket3}: {percentage}
```

### 5. Present Menu Options

Display: "**Select:** [C] Continue to Next Edit"

#### Menu Handling Logic:
- IF C: Save to {workflowPlanFile}, then show Edit menu again
- IF Any other: help user respond, then redisplay menu

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed when user selects 'C'

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Resource type identified
- New values captured
- Portfolio impact calculated
- All projects recalculated
- Change documented

### ❌ SYSTEM FAILURE:
- Changing without impact analysis
- Exceeding WIP limits without action plan
- Missing project recalculation
- Skipping documentation

**Master Rule:** Every resource change must cascade through portfolio.

---

## RESOURCE MANAGEMENT BEST PRACTICES

**Capacity Planning:**
- 40-50 hours/week: Sustainable for 3 projects
- 60+ hours/week: Unsustainable (recommend reduce WIP)
- <20 hours/week: Too small, consolidate portfolio

**WIP Limits:**
- 3 projects: Optimal for focus + progress
- 4+ projects: Context switch overhead increases
- 1-2 projects: Only for high-risk or complex work

**Timeline Constraints:**
- Plan for vacation, conferences, life events
- Mark as "blocked" in project timelines
- Adjust milestone dates automatically

**Budget Allocation:**
- Strategic buckets prevent single-domain dominance
- Review quarterly for balance
- Underfunded buckets (<15% allocation) → escalate

**Red Flags:**
- 🔴 Utilization >100% → Reduce WIP or extend timelines
- 🔴 WIP > limit → Complete or pause projects immediately
- 🟡 Utilization 80-100% → Add buffer capacity
- 🟡 Underfunded bucket → Reallocate or pause projects
