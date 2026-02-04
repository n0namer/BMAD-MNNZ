---
name: 'step-00-return-to-plan'
description: 'Quickly restore context for a project using snapshot and journal'
projectsFolder: '{bmb_creations_output_folder}/life-os/projects'
snapshotsFolder: '{bmb_creations_output_folder}/life-os/snapshots'
journalFolder: '{bmb_creations_output_folder}/life-os/journal'
decisionsLog: '{bmb_creations_output_folder}/life-os/decisions/decision-log.md'
plansFolder: '{bmb_creations_output_folder}/life-os/plans'
---

# Return-to-Plan: Quick Context

## STEP GOAL:

Provide a fast context restore for a project (goal, status, last decision, next steps, and latest changes).

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Step-Specific Rules:
- 🎯 Focus ONLY on context recovery
- 🚫 FORBIDDEN to change project data here
- 💬 If files are missing, explain clearly and offer next best action

## EXECUTION PROTOCOLS:

- 🎯 Identify the target project
- 📖 Read project file, snapshot, and latest journal entry
- 💾 Provide a concise context summary

### Search Orchestrator Protocol (Required)
- Follow data/mcp_search_system_prompt_xml.md.
- Execute: CLI memory search -> local MD (rg) -> web/MCP.
- Convene consilium to rank 2–4 options with pros/cons and recommendation.
- Ask user to choose before proceeding.

### Semantic Decision Support
If a decision or prioritization remains unclear, use Search Orchestrator to rank 2–3 options.

## CONTEXT BOUNDARIES:

- Available context: project file, snapshot, journal, decision log
- Focus: current state and next actions

## MANDATORY SEQUENCE

### 1. Select Project

Ask:
"Какой проект вы хотите восстановить по контексту?  
Укажите ID/название, либо опишите — я помогу найти."

### 2. Load Sources

Load:
- Project file from {projectsFolder}
- Snapshot from {snapshotsFolder}
- Journal from {journalFolder}
- Project plan from {plansFolder}
- Decision log from {decisionsLog} (if relevant)

If any file is missing, state it and continue with available sources.

### 3. Present Context Snapshot

Summarize:
- Цель проекта
- Текущий статус
- Последнее решение (из snapshot или decision-log)
- Последнее изменение (из journal)
- Следующие шаги / ближайший фокус
- Глубина плана (если есть)

### 4. Present MENU OPTIONS

Display: "**Select:** [C] Continue"

#### Menu Handling Logic:
- IF C: End this step and return control to the user (no next step)
- IF Any other: help user respond, then redisplay menu

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Project identified
- Snapshot and journal consulted (if available)
- Context summary delivered

### ❌ SYSTEM FAILURE:
- Modifying data during return-to-plan
- Missing context summary

**Master Rule:** Return-to-plan is read-only and fast.
