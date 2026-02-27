---
name: 'step-02-update-resources'
description: 'Update portfolio resources: capacity, budget allocation, timeline constraints'
nextStepFile: './step-01-update-project.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
portfolioFolder: '{bmb_creations_output_folder}/life-os'
metricsFile: '{bmb_creations_output_folder}/life-os/metrics/metrics.md'
journalFolder: '{bmb_creations_output_folder}/life-os/journal'
resourceGuideFile: '../data/resource-update-guide.md'
---

# Edit Step 2: Update Resources

## STEP GOAL

Manage portfolio-level resources: update personal capacity, adjust budget allocations, track timeline constraints, monitor WIP limits.

💡 **Detailed Analysis Templates:** `{resourceGuideFile}`

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

Ask: "Сколько часов в неделю? Текущий: {current} | Новое: [0-60]"

Calculate impact:
```
📊 Capacity Impact

WIP: {X projects, Y hours} | Available: {Z hours}
Utilization: {Y/Z}% | Free: {Z-Y} hours
{if Y>Z: "⚠️ OVERALLOCATED - Reduce WIP or extend timelines" else: "✅ OK"}

📖 Detailed analysis templates: {resourceGuideFile}
```

### 2B. IF WIP - Update Concurrent Project Limit

Ask: "Сколько проектов одновременно? Текущий: {current} | Новый: [1-5]"

Check WIP health:
```
📊 WIP Status

Current: {X projects} | New limit: {Y projects}
{if X>Y: "⚠️ Must free {X-Y} slots - Complete/pause/kill" else: "✅ OK"}

Active: {list projects with status}
📖 Detailed WIP analysis: {resourceGuideFile}
```

### 2C. IF TIMELINE - Add Constraints

Ask: "Тип ограничения: [V]acation | [C]onference | [B]uild | [O]ther"

Capture: Event name, start/end dates, impact (e.g., "50% capacity", "Full pause")

Recalculate all project timelines. 📖 Timeline adjustment formulas: {resourceGuideFile}

### 2D. IF BUDGET - Update Allocation

Ask: "Новый бюджет: ${amount} за {period}? Текущий: ${current}"

Ask for bucket allocation (each bucket 0-100%):

Show allocation:
```
📊 Budget

Total: ${total}
{Bucket1}: {X%} = ${amt} | {count} projects | Avg ${per_proj}
{Bucket2}: {Y%} = ${amt} | {count} projects | Avg ${per_proj}
...

{if any <15%: "⚠️ Underfunded: {bucket_name}" else: "✅ Balanced"}
📖 Allocation best practices: {resourceGuideFile}
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

## QUICK REFERENCE

**Best Practices:**
- Capacity: 40-50 hrs/week for 3 projects (sustainable)
- WIP: 3 projects optimal, 4+ increases overhead
- Timeline: Plan for vacation, conferences (add buffers)
- Budget: Review quarterly, underfunded <15% = red flag

**Red Flags:**
- 🔴 Utilization >100% → Reduce WIP
- 🔴 WIP > limit → Complete/pause projects
- 🟡 Underfunded bucket (<15%) → Reallocate

📖 **Complete best practices, analysis templates, and decision trees:** {resourceGuideFile}
