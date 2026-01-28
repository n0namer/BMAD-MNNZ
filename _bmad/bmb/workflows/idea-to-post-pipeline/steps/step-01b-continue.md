---
continuableEnabled: true
description: Load previous session state and resume from last step
name: step-01b-continue
nextStepFile: (determined dynamically by currentStep in workflow_state.json)
stateFile: workflow_state.json
type: continuation
---

# Step 1b: Session Resumption

## STEP GOAL:

To load the saved session state from `workflow_state.json`, restore the user's context, and jump directly to the last incomplete step.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator

### Role Reinforcement:

- ✅ You are a Session Recovery Specialist
- ✅ Treat the user's previous context with respect
- ✅ Restore state transparently
- ✅ Enable seamless continuation

### Step-Specific Rules:

- 🎯 Focus ONLY on state loading and restoration
- 🚫 FORBIDDEN to modify state (only read and display)
- 💬 Be transparent about what was saved
- 📋 Verify state integrity before restoring

## EXECUTION PROTOCOLS:

### HALT AND WAIT RULES

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**

- 🎯 Load workflow_state.json
- 💾 Parse and validate state structure
- 📖 Display recovered context to user
- 🚫 Confirm user wants to proceed with resumption

---

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load & Parse State File

Read `workflow_state.json` from the workflow root directory.

Expected structure:
```json
{
  "workflow_id": "idea-to-post-pipeline",
  "session_id": "2026-01-27-v1",
  "currentMode": "CREATE" | "EDIT" | "VALIDATE" | "YOLO",
  "currentStep": "step-c-03c-draft",
  "stepsCompleted": [...],
  "context": {
    "selectedIdea": 1,
    "selectedAngle": "angle_3",
    "draftVersion": 1,
    "draftFeedback": [...],
    "postVariants": {...}
  },
  "lastUpdated": "2026-01-27 21:30",
  "sessionDuration": "45 min"
}
```

**IF file is valid:** Proceed to step 2
**IF file is corrupted:** Display error and offer options:
  - [R] Try to repair (read-only recovery)
  - [N] Start fresh (create new state)
  - [?] Show detailed error

### 2. Display Recovered Context

Display in Russian (clear, friendly format):

```
═══════════════════════════════════════════════════════════════

  ✅ Сессия восстановлена!

Найдена сохранённая сессия от [lastUpdated]:

  Режим: [currentMode]
  Последний шаг: [currentStep]
  Шаги выполнены: [count from stepsCompleted]
  Длительность предыдущей сессии: [sessionDuration]

═══════════════════════════════════════════════════════════════

  Восстановленный контекст:
```

Display mode-specific context:

**IF currentMode = "CREATE":**
```
  Создание контента:
    Выбранная идея: [selectedIdea] — "[idea title]"
    Выбранный угол: [selectedAngle] — "[angle description]"
    Версия черновика: [draftVersion]
    Feedback на черновик: [draftFeedback list]
```

**IF currentMode = "EDIT":**
```
  Редактирование:
    Загруженный пост: [loadedPostId]
    Версия для редакции: [editVersion]
    Выбранные улучшения: [improvements list]
```

**IF currentMode = "VALIDATE":**
```
  Проверка качества:
    Количество постов для проверки: [postCount]
    Выполнено проверок: [completedValidations]/[totalValidations]
```

**IF currentMode = "YOLO":**
```
  YOLO автоматизация:
    Параметры: [yoloOptions]
    Выполнено: [completedSteps]/[totalSteps]
```

### 3. Confirm Resumption

Display confirmation menu:

```
═══════════════════════════════════════════════════════════════

Хочешь продолжить с этой точки?

[Y] Да, продолжить с [currentStep]
[N] Нет, начать заново с главного меню
[M] Показать полный контекст (JSON)
[R] Вернуться в меню режимов (step-00-menu)
```

#### Menu Handling Logic:

**IF Y:**
- Display: "Продолжаю... 🚀"
- Determine nextStepFile based on currentStep
- Load, read entire file, then execute nextStepFile with context

**IF N:**
- Display: "Ок, начинаем с нуля! 🆕"
- Delete (or backup) workflow_state.json
- Load, read entire file, then execute step-00-menu.md

**IF M:**
- Pretty-print full workflow_state.json (formatted JSON)
- Display all fields
- Return to confirmation menu

**IF R:**
- Clear session memory but keep state file
- Load, read entire file, then execute step-00-menu.md
- User can still resume later if they want

### 4. Context Restoration (if resuming)

Before jumping to nextStepFile, prepare context:

```
═══════════════════════════════════════════════════════════════

  📋 Контекст восстановлен:

  ✅ Session ID: [session_id]
  ✅ Mode: [currentMode]
  ✅ Current Step: [currentStep]
  ✅ Context variables: [context keys list]

  Переходим к [currentStep]...

═══════════════════════════════════════════════════════════════
```

---

## 🚨 CRITICAL RULES

- 🛑 NEVER modify workflow_state.json (read-only operations)
- 📋 If state is corrupted, offer recovery options, don't assume
- 💾 Preserve full state when resuming (all context)
- 🚫 Don't skip steps (jump directly to currentStep)
- 📖 Always display human-friendly summary before resuming

---

## SUCCESS CRITERIA

- ✅ State file loaded successfully
- ✅ Context restored accurately
- ✅ User sees clear summary of previous progress
- ✅ Resumption confirmed before jumping to next step
- ✅ All context variables preserved for next step

---

## NEXT STEP

When user selects [Y]:
- Load, read entire file, then execute step file determined by `currentStep`
- Pass full context to next step

When user selects [N] or [R]:
- Load, read entire file, then execute step-00-menu.md
