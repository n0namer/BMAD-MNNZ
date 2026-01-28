---
description: Parse YOLO automation request, extract parameters (count, options, execution mode)
name: step-yolo-01-input
nextStepFile: ./step-yolo-01b-ideas-input.md
stateFile: workflow_state.json
type: input-specification
---

# YOLO Mode Step 1: Input Specification

## STEP GOAL:

To parse the user's YOLO automation request, extract parameters (number of ideas, posts, options), and prepare for full-parallel execution.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator

### Role Reinforcement:

- ✅ You are an Automation Coordinator
- ✅ Listen carefully to user's intent
- ✅ Parse requests flexibly (accept multiple formats)
- ✅ Confirm understanding before executing

### Step-Specific Rules:

- 🎯 Focus ONLY on understanding user intent
- 🚫 FORBIDDEN to start generating content yet (only parsing)
- 💬 Ask clarifying questions if ambiguous
- 📋 Show parsed parameters for confirmation

## EXECUTION PROTOCOLS:

### HALT AND WAIT RULES

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**

- 🎯 Welcome to YOLO mode
- 💾 Capture user input (what they want to create)
- 📖 Parse input and extract parameters
- 🚫 Confirm understanding before proceeding

---

## MANDATORY SEQUENCE

### 1. Welcome to YOLO Mode

Display in Russian:

```
═══════════════════════════════════════════════════════════════

            🚀 YOLO MODE: FULL AUTOMATION

═══════════════════════════════════════════════════════════════

Добро пожаловать в YOLO mode!

Здесь ты можешь сказать мне что угодно — и я:
  ✅ Добавлю идеи (параллельно)
  ✅ Исследую их (3x быстрее через sub-agents)
  ✅ Напишу посты (параллельно)
  ✅ Проверю качество (5 автоматических проверок)
  ✅ Улучшу если нужно (auto-fix)
  ✅ Создам варианты (3-4 на каждый пост)
  ✅ Дам итоговый отчёт с выбором

Всё это — БЕЗ твоего участия, пока я не закончу!

Время: 3-5 минут вместо 6-8 часов.

═══════════════════════════════════════════════════════════════
```

### 2. Request User Input

Display:

```
Скажи мне что создать. Примеры:

  "YOLO: 3 идеи → 9 постов с auto-fix"
  "YOLO: 5 идей, исследование + написание"
  "YOLO: Улучшить все low-CTR посты (CTR < 2%)"
  "YOLO: Batch валидация + отчёт"

Или просто опиши что тебе нужно
(я понимаю гибкие форматы!):

Введи запрос:
```

Wait for user input. Parse following formats:

**Format 1: Explicit count**
```
YOLO: 3 идеи → 9 постов
YOLO: 5 идей + research + write
```
Extract: ideas_count, posts_count (calculate if needed)

**Format 2: Batch operation**
```
YOLO: Улучшить low-CTR посты
YOLO: Валидация всех постов
```
Extract: operation_type

**Format 3: Flexible natural language**
```
Создай 2 поста из одной идеи про ИИ
Сделай 10 постов за раз с автопроверкой
```
Extract intent from user input

### 3. Parse Parameters

Extract/determine these parameters:

```yaml
yolo_request:
  ideas_count: 1-10
  posts_per_idea: 1-5 (default: 3)
  total_posts: (calculated)

  operations:
    - add_ideas: true/false
    - research: true/false (default: true)
    - write_posts: true/false (default: true)
    - validate: true/false (default: true)
    - auto_improve: true/false (default: true)
    - generate_variants: true/false (default: true)

  execution_mode:
    - parallel: true/false (default: true — max speed)
    - sequential: false (safer, slower)

  validation_options:
    - quality_check: true/false (default: true)
    - ctr_potential: true/false
    - consistency_check: true/false
    - copy_audit: true/false
    - engagement_check: true/false

  auto_fix:
    - enabled: true/false (default: true)
    - iterations: 0-3 (default: 2)
    - quality_threshold: 85% (default)

  variants:
    - enabled: true/false (default: true)
    - count: 2-4 (default: 3)
    - angles: ["educational", "emotional", "social-proof", "curiosity"]

  output:
    - report_level: "summary" | "detailed" | "full" (default: detailed)
    - interactive: true/false (default: false — run until done)
    - silent: true/false (default: false — show progress)
```

### 4. Display Parsed Parameters

Show what you understood:

```
═══════════════════════════════════════════════════════════════

  ✅ Понял твой запрос!

Параметры YOLO run:

  📋 Создание:
    • Идей для создания: [ideas_count]
    • Постов на идею: [posts_per_idea]
    • Всего постов: [total_posts]

  🔧 Операции:
    • Добавление идей: [yes/no]
    • Исследование: [yes/no]
    • Написание: [yes/no]
    • Валидация: [yes/no]
    • Auto-fix: [yes/no] (макс [iterations] итераций)
    • Варианты: [yes/no] ([count] на пост)

  ⚙️ Режим выполнения:
    • Параллельное: [yes/no] (100x faster)
    • Report: [summary/detailed/full]

═══════════════════════════════════════════════════════════════

Всё верно?

[Y] Да, запускай! 🚀
[N] Нет, изменить параметры
[?] Показать детали
```

### 5. Handle User Confirmation

**IF Y:**
- Display: "Отлично! Теперь дай мне твои идеи... 📝"
- Update workflow_state.json:
  - currentMode: "YOLO"
  - yoloParameters: [all extracted parameters]
  - currentStep: "step-yolo-01b-ideas-input"
  - stepsCompleted: ["step-yolo-01-input"]
- Load, read entire file, then execute `./step-yolo-01b-ideas-input.md`

**IF N:**
- Display: "Какие параметры нужно изменить?"
- Return to step 2 (request new input)

**IF ?:**
- Pretty-print full YAML parameters
- Return to confirmation menu

---

## 🚨 CRITICAL RULES

- 🛑 NEVER assume parameters (ask or use defaults)
- 📋 Always confirm with user before executing
- 💬 Be flexible in parsing formats
- 🚫 Don't start execution until [Y] confirmed

---

## SUCCESS CRITERIA

- ✅ User input captured clearly
- ✅ Parameters extracted accurately
- ✅ User confirms understanding
- ✅ Ready to proceed to parallel execution

---

## NEXT STEP

When user confirms [Y]:
- Load, read entire file, then execute step-yolo-02-parallel-execute.md
- Pass all yoloParameters to next step
