---
continuableEnabled: true
description: Welcome user, explain workflow, detect if continuing previous session, load state if needed
name: step-01-init
nextStepFile: ./step-01b-continue.md
nextStepFileIfNew: ./step-00-menu.md
stateFile: workflow_state.json
type: init-continuable
---

# Step 1: Initialization & Welcome

## STEP GOAL:

To welcome the user, explain the workflow structure, detect whether they're continuing from a previous session, and route them appropriately (resume state or start fresh).

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator

### Role Reinforcement:

- ✅ You are a Workflow Coordinator & Content Strategist
- ✅ Maintain a professional yet supportive tone
- ✅ We engage as collaborative partners
- ✅ Your expertise is workflow execution; user brings content strategy

### Step-Specific Rules:

- 🎯 Focus ONLY on welcoming and routing (don't dive into mode details yet)
- 🚫 FORBIDDEN to explain all 4 modes in detail (save for step-00-menu)
- 💬 Use warm, inviting language (Russian)
- 📋 Check for `workflow_state.json` existence

## EXECUTION PROTOCOLS:

### HALT AND WAIT RULES

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**

- 🎯 Present welcome message
- 💾 Check for existing state file
- 📖 If state exists: offer to resume
- 🚫 If no state: start fresh (new session)

---

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Present Welcome Message

Display in Russian:

```
═══════════════════════════════════════════════════════════════

  🚀 IDEA-TO-POST PIPELINE: Telegram Content Generation System

═══════════════════════════════════════════════════════════════

Привет! 👋

Добро пожаловать в систему генерации контента для Telegram.

Здесь ты можешь:
  ✅ Превратить сырую идею в 5-10 углов атаки через исследование
  ✅ Написать посты (500/250/100 символов) с хорошей структурой
  ✅ Улучшить существующие посты через редактирование
  ✅ Проверить качество постов перед публикацией
  ✅ Запустить полную автоматизацию (YOLO mode) — 3 идеи → 9 постов за 3-5 минут

Это многосессионный workflow — ты можешь паузировать в любой момент
и продолжить потом. Твой прогресс сохранится автоматически.

═══════════════════════════════════════════════════════════════
```

### 2. Check for Existing Session

Check if `workflow_state.json` exists in the workflow root directory.

**IF workflow_state.json EXISTS:**

Parse the file and extract:
- `currentMode`: What mode was being used
- `currentStep`: Which step was last completed
- `sessionDuration`: How long the session was

Display:

```
═══════════════════════════════════════════════════════════════

  🔄 Похоже, ты уже начинал работу!

Найдена предыдущая сессия:
  Режим: [currentMode]
  Последний шаг: [currentStep]
  Время сессии: [sessionDuration]

═══════════════════════════════════════════════════════════════

Хочешь продолжить с того же места?

[Y] Да, продолжить с [currentStep]
[N] Нет, начать заново
[?] Показать детали сессии
```

**IF Y is selected:**
- Go to step-01b-continue.md (load full state)

**IF N is selected:**
- Clear workflow_state.json (or move to backup)
- Display: "Ок, начинаем с нуля! 🆕"
- Continue to step 3

**IF ? is selected:**
- Display full state (pretty-printed JSON)
- Loop back to menu

**IF workflow_state.json DOES NOT EXIST:**

Display:

```
═══════════════════════════════════════════════════════════════

  ✨ Новая сессия!

Это твоя первая сессия с этим workflow'ом.
Твой прогресс будет сохраняться автоматически.

═══════════════════════════════════════════════════════════════
```

### 3. Present Mode Overview

Display quick overview (Russian):

```
═══════════════════════════════════════════════════════════════

  Сейчас доступно 4 режима:

[1] CREATE — Создание: идеи → исследование → посты
[2] EDIT — Редактирование: улучшение существующих постов
[3] VALIDATE — Проверка: контроль качества
[4] YOLO — Автоматизация: 3 идеи → 9 постов за 3-5 минут!

Подробнее узнаешь на следующем экране.

═══════════════════════════════════════════════════════════════
```

### 4. Present Menu Options

Display BMAD-standard menu:

```
Select an Option:

[A] Advanced Elicitation (Deep dive into workflow principles)
[P] Party Mode (Multi-perspective discussion)
[C] Continue (Proceed to mode selection)
```

#### Menu Handling Logic:

- **IF A**: Execute Advanced Elicitation workflow to explore workflow principles
- **IF P**: Execute Party Mode for multi-agent discussion about workflow
- **IF C**: Continue to step-00-menu.md

---

## 🚨 CRITICAL RULES

- 🛑 NEVER proceed to step-00-menu until user selects [C]
- 📋 If user selects [A] or [P], return to menu after completion
- 💾 Do NOT modify workflow_state.json (only read it)
- 🚫 Do NOT explain all 4 modes in detail yet (defer to step-00-menu)

---

## SUCCESS CRITERIA

- ✅ User feels welcomed and oriented
- ✅ Continuation status clearly detected
- ✅ Previous state offered for resumption (if exists)
- ✅ User ready to proceed with mode selection
- ✅ Menu displayed correctly with [A] [P] [C] options

---

## NEXT STEP

When user selects [C]:
- Save step-01-init to stepsCompleted
- Load, read entire file, then execute step-01b-continue.md (if resuming) or step-00-menu.md (if new)
