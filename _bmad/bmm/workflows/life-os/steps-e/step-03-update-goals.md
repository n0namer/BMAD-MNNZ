---
name: 'step-03-update-goals'
description: 'Update long-term goals: add, modify, or retire strategic objectives'
nextStepFile: './step-01-update-project.md'
goalsFolder: '{bmb_creations_output_folder}/life-os/goals'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
journalFolder: '{bmb_creations_output_folder}/life-os/journal'
---

# Edit Step 3: Update Goals

## STEP GOAL:

Manage long-term strategic goals: add new goals, modify existing ones, track progress, or retire completed goals.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', read entire file
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Step-Specific Rules:
- 🤝 Proactive guidance: highlight goal-project alignment and progress
- 🧭 If goal has no active projects, flag for alignment check
- ✅ Ask for user confirmation before major goal changes
- 🎯 Focus ONLY on goal management
- 🚫 FORBIDDEN to create new projects here
- 💬 Confirm all changes with the user
- 💬 Ask 1–2 questions at a time and adapt to responses

## EXECUTION PROTOCOLS:

### Goal Management Protocol
- Goals are long-term (6-12+ months)
- Connect to domains: Business / Finance / Health / Personal Development
- Track active projects per goal (alignment check)
- Measure progress against objectives

### Search Orchestrator Protocol (If user asks for goal frameworks)
- Follow data/mcp_search_system_prompt_xml.md
- Execute: CLI memory search → local MD → web/MCP
- Suggest frameworks: OKRs, SMART Goals, Mission statements

---

## MANDATORY SEQUENCE

### 1. Select Goal Action

Ask:
"Что вы хотите сделать с целями?

[N]ew - Добавить новую долгосрочную цель
[U]pdate - Обновить существующую цель
[P]rogress - Отметить прогресс по цели
[R]etire - Завершить или отказаться от цели

Укажите: [N] / [U] / [P] / [R]"

### 2A. IF NEW - Add Goal

Capture progressively (1-2 questions at a time):

1. **Goal Domain**
   "В какой области? [Business] [Finance] [Health] [Personal Dev]"

2. **Goal Statement**
   "Опишите цель в 1-2 предложениях (конкретная, важная)"

3. **Target Timeline**
   "На какой срок? (e.g., 6 месяцев, 1 год, 2 года)"

4. **Success Criteria**
   "Как узнать, что цель достигнута? (2-3 конкретных критерия)"

5. **Connected Projects** (Optional for now)
   "Есть ли существующие проекты, которые помогают этой цели? (можно добавить позже)"

**Goal Profile Template:**
```markdown
## Goal: {Goal Name}

**Domain:** {Domain}
**Timeline:** {Duration}
**Status:** ACTIVE

### Goal Statement
{Concise goal statement}

### Success Criteria
- {Criterion 1}
- {Criterion 2}
- {Criterion 3}

### Connected Projects
- {Project1}
- {Project2}

### Progress
- Started: {date}
- Current: {percentage}%
- Next Milestone: {date}

### Last Updated
{date}
```

### 2B. IF UPDATE - Modify Goal

List current goals:
```
Active Goals:

1. {Goal1} ({Domain}) - {X}% progress
2. {Goal2} ({Domain}) - {X}% progress
3. {Goal3} ({Domain}) - {X}% progress

Which goal to update? [1-3] or [Name]:
```

After selection, ask:
"Что обновить у '{Goal}'?

[S]tatement - Переформулировать цель
[T]imeline - Изменить сроки
[C]riteria - Обновить критерии успеха
[P]rojects - Добавить/убрать проекты
[O]ther - Другое изменение

Укажите: [S] / [T] / [C] / [P] / [O]"

Update the goal profile with user input.

### 2C. IF PROGRESS - Track Progress

List goals:
```
Current Goals:

1. {Goal1} - {X}% → {X+Y}%
2. {Goal2} - {X}% → {X+Y}%

Which goal? [1-3] or [Name]:
```

After selection:
"Current progress on '{Goal}': {X}%

New progress: [0-100]%
Notes: (optional - what changed?)"

Update progress in goal file and journal.

### 2D. IF RETIRE - Complete/Retire Goal

Ask:
"Вы хотите завершить или отказаться от цели '{Goal}'?

[C]omplete - Цель достигнута ✅
[R]etire - Отказываемся от цели (причина?)
[P]ause - Отложить на время

Укажите: [C] / [R] / [P]"

If Complete: Mark with date achieved, archive to completed goals.
If Retire: Capture reason, archive with learnings.
If Pause: Keep in active list but mark as "PAUSED", set resume target date.

### 3. Document Change

Append to {workflowPlanFile}:
```markdown
## Edit: Goal Management

**Action:** {NEW | UPDATE | PROGRESS | RETIRE}
**Goal:** {Goal Name}
**Domain:** {Domain}
**Date:** {date}

**Changes:**
- {Change 1}
- {Change 2}

**Impact on Portfolio:**
- Projects affected: {count}
- Timeline implications: {notes}
```

Append to {journalFolder}/goals-journal.md:
```markdown
### {Date}: {Action} - {Goal Name}

{Summary of change and rationale}

Connected projects updated:
- {Project1}
- {Project2}
```

### 4. Display Goals Summary

Show updated goals landscape:
```
✅ Goals Updated

Active Goals by Domain:

Business: {count}
- {Goal1} - {X}%
- {Goal2} - {X}%

Finance: {count}
- {Goal1} - {X}%

Health: {count}
- {Goal1} - {X}%

Personal Dev: {count}
- {Goal1} - {X}%

Portfolio Alignment:
- {X} projects have goal alignment
- {X} projects need goal connection
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
- Goal action confirmed (add/update/progress/retire)
- Goal profile created or updated
- Timeline and criteria clear
- Change documented
- Portfolio impact assessed

### ❌ SYSTEM FAILURE:
- Changing without confirmation
- Unclear criteria for success
- Skipping documentation
- Not checking project alignment

**Master Rule:** Goals should be SMART, connected to projects, and regularly tracked.

---

## GOALS MANAGEMENT BEST PRACTICES

**Goal Scope:**
- 6-12+ months duration (shorter items belong in projects)
- Clear success criteria (measurable)
- Aligned with portfolio domains
- 3-5 major goals maximum (avoid dilution)

**Goal-Project Connection:**
- Projects should serve 1-2 major goals
- If project has no goal → Align or kill
- If goal has no projects → Create first project

**Progress Tracking:**
- Monthly: Review progress on all active goals
- Quarterly: Assess goal relevance, adjust if needed
- Annually: Retire old, set new for next cycle

**Common Issues:**
- ⚠️ Too many goals (>5) → Focus, kill non-critical
- 🔴 Goals with no projects → Create first project or retire
- 🟡 Stalled goals (same % for 3+ months) → Escalate to consilium
