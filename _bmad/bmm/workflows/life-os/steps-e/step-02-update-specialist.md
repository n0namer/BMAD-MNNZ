---
name: 'step-02-update-specialist'
description: 'Manage specialist: update skills, availability, or remove from roster'
nextStepFile: './step-01-update-project.md'
specialistsFolder: '{bmb_creations_output_folder}/life-os/specialists'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
journalFolder: '{bmb_creations_output_folder}/life-os/journal'
---

# Edit Step 2: Update Specialist

## STEP GOAL:

Manage specialist roster: add new specialist profile, update skills/availability, or remove from active roster.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', read entire file
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Step-Specific Rules:
- 🤝 Proactive guidance: highlight specialist utilization and gaps
- 🧭 If specialist is overallocated (3+ concurrent projects), flag early
- ✅ Ask for user confirmation before removing specialist
- 🎯 Focus ONLY on specialist profile management
- 🚫 FORBIDDEN to create new projects here
- 💬 Confirm all changes with the user
- 💬 Ask 1–2 questions at a time and adapt to responses

## EXECUTION PROTOCOLS:

### Specialist Management Protocol
- If adding specialist: capture name, expertise domain, availability
- If updating: which field? (skills, availability, domain, contact)
- If removing: confirm reason and archive profile

### Search Orchestrator Protocol (If user asks for specialist recommendations)
- Follow data/mcp_search_system_prompt_xml.md
- Execute: CLI memory search → local MD → web/MCP
- Suggest specialist archetypes by domain

---

## MANDATORY SEQUENCE

### 1. Select Specialist Action

Ask:
"Что вы хотите сделать со специалистом?

Если хотите управлять специалистом:
[A]dd - Добавить новго специалиста в реестр
[U]pdate - Обновить навыки/доступность существующего
[R]emove - Удалить специалиста из активного реестра

Укажите: [A] / [U] / [R]"

### 2A. IF ADD - New Specialist

Capture progressively (1-2 questions at a time):
- Имя / Title (role)
- Expertise domain (Business / Finance / Health / Personal Development)
- Key skills (3-5 words)
- Availability (Current WIP capacity, how many projects can they support?)
- Contact info (optional)

**Example Specialist Profile:**
```
## Specialist Profile: {Name}

**Role:** {Role/Title}
**Domain:** {Domain}
**Skills:** {Skill1, Skill2, Skill3, Skill4, Skill5}
**Availability:** {X projects max}
**WIP Status:** {0/X projects currently assigned}
**Last Updated:** {date}
```

### 2B. IF UPDATE - Existing Specialist

List available specialists:
```
Available Specialists:

1. {Name1} ({Domain}) - {X/Y current/max projects}
2. {Name2} ({Domain}) - {X/Y current/max projects}
3. {Name3} ({Domain}) - {X/Y current/max projects}

Which specialist to update? [1-3] or [Name]:
```

After selection, ask:
"Что обновить у {Name}?

[S]kills - Обновить навыки
[A]vailability - Изменить максимум проектов
[D]omain - Изменить специализацию
[O]ther - Другое изменение

Укажите: [S] / [A] / [D] / [O]"

Update the specialist profile with user input.

### 2C. IF REMOVE - Deactivate Specialist

Ask:
"Вы уверены, что хотите удалить {Name}?

Current assignment: {X projects}

Это действие:
- Удалит специалиста из активного реестра
- Сохранит его архив для истории
- Не повлияет на завершённые проекты

Подтвердить? [Y]es / [N]o"

If Y: Archive specialist profile, update active roster.

### 3. Document Change

Append to {workflowPlanFile}:
```markdown
## Edit: Specialist Management

**Action:** {ADD | UPDATE | REMOVE}
**Specialist:** {Name}
**Date:** {date}

**Changes:**
- {Change 1}
- {Change 2}

**Rationale:** {Why this change?}
```

Append journal entry to {journalFolder}/{specialist-id}-journal.md:
```markdown
### {Date}: {Action}

{Summary of change and rationale}
```

### 4. Display Specialist Summary

Show updated specialist roster:
```
✅ Specialist Updated

Updated Roster:

{Domain}: {Count} specialists
- {Name1} ({X/Y projects)
- {Name2} ({X/Y projects)
...

Portfolio Impact:
- Total WIP capacity: {total/max}
- Available capacity: {available}
```

### 5. Present Menu Options

Display: "**Select:** [C] Continue to Next Edit"

#### Menu Handling Logic:
- IF C: Save content to {workflowPlanFile}, update frontmatter, then load, read entire file, then execute step that user wants next (offer menu)
- IF Any other: help user respond, then redisplay menu

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed when user selects 'C'

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Specialist action confirmed (add/update/remove)
- Profile updated or created
- Change documented
- Portfolio capacity calculated

### ❌ SYSTEM FAILURE:
- Updating without confirmation
- Missing critical information
- Skipping documentation
- Not checking portfolio impact

**Master Rule:** Confirm all changes before persisting.

---

## SPECIALIST MANAGEMENT BEST PRACTICES

**When to Add:**
- Portfolio needs expertise in new domain
- Team has bandwidth for new specialist
- Clear role and availability established

**When to Update:**
- Specialist's availability changed
- New skills acquired
- Previous skills deprecated

**When to Remove:**
- Specialist no longer available
- Portfolio no longer needs expertise
- Specialist not used in 6+ months (archive suggested)

**Capacity Warning:**
- ⚠️ If specialist at 3+ concurrent projects → Flag as "at capacity"
- 🔴 If specialist at 5+ projects → Flag as "overallocated"
