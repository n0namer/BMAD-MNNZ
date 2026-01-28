---
description: Collect user's actual ideas/content before parallel execution
name: step-yolo-01b-ideas-input
nextStepFile: ./step-yolo-02-parallel-execute.md
stateFile: workflow_state.json
type: user-content-collection
---

# YOLO Step 1b: Ideas Input Collection

## STEP GOAL:

To collect the user's actual ideas and content that will be transformed into posts. This is the critical step that was missing - we now ask the user for THEIR content before starting parallel execution.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator

### Role Reinforcement:

- ✅ You are a Content Collector & Collaborator
- ✅ Listen carefully to user's ideas
- ✅ Accept multiple formats (text, bullet points, full articles)
- ✅ Clarify if needed, but don't judge or rewrite

### Step-Specific Rules:

- 🎯 Focus ONLY on collecting user's ideas
- 🚫 FORBIDDEN to generate ideas yourself (that's the bug we're fixing!)
- 💬 Accept ideas in any format the user provides
- 📋 Store ideas for passing to parallel execution

## EXECUTION PROTOCOLS:

### HALT AND WAIT RULES

**ALWAYS halt and wait for user input after requesting ideas.**
**ONLY proceed to next step when user provides their ideas.**

- 🎯 Display input request
- 💾 Collect user's 3 ideas
- 📖 Confirm understanding
- 🚫 Do NOT start execution until ideas are provided

---

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Welcome & Context Setting

Display in Russian:

```
═══════════════════════════════════════════════════════════════

  📝 STEP 2: Your Ideas

═══════════════════════════════════════════════════════════════

Отлично! Теперь мне нужны ТВОИ идеи.

Это самая важная часть — я буду превращать ВАШ контент в посты,
не генерировать примеры вместо тебя.

═══════════════════════════════════════════════════════════════
```

### 2. Request User's 3 Ideas

Display in Russian:

```
Дай мне 3 идеи для превращения в посты.

Формат — как удобно:
  • Просто названия ("ИИ контент", "Speech-to-text", "Масштабирование")
  • Несколько строк описания для каждой
  • Полный текст статей/постов (если есть)
  • Ссылки на источники

Пример:

Идея 1: "ИИ контент — как это работает"
Описание: Экономия времени, масштабирование без найма, качество vs скорость

Идея 2: "Speech-to-text для авторов"
Описание: Дикуй посты на ходу, минимум редактирования

Идея 3: "Масштабирование команды"
Описание: От одного к системе, делегирование, первые нанятые

───────────────────────────────────────────────────────────

Введи твои 3 идеи (копируй выше, заполняй):
```

### 3. Collect & Parse Ideas

Wait for user input. Extract:

```yaml
user_ideas:
  idea_1:
    title: [string]
    description: [string]
    content: [optional - full text if provided]
  idea_2:
    title: [string]
    description: [string]
    content: [optional - full text if provided]
  idea_3:
    title: [string]
    description: [string]
    content: [optional - full text if provided]
```

### 4. Confirm Understanding

Display back to user:

```
═══════════════════════════════════════════════════════════════

  ✅ Получил твои идеи!

Будем работать с:

1️⃣  [Idea 1 Title]
    [Short description]

2️⃣  [Idea 2 Title]
    [Short description]

3️⃣  [Idea 3 Title]
    [Short description]

═══════════════════════════════════════════════════════════════

Всё верно?

[Y] Да, идеи правильные
[N] Нет, хочу изменить
[?] Показать детали
```

### 5. Handle User Response

**IF Y:**
- Display: "Отлично! Запускаю параллельное исполнение..."
- Update workflow_state.json:
  - currentStep: "step-yolo-01b-ideas-input"
  - userIdeas: [all collected ideas]
  - stepsCompleted: ["step-yolo-01-input", "step-yolo-01b-ideas-input"]
- Load, read entire file, then execute `./step-yolo-02-parallel-execute.md`
- **PASS userIdeas to step-yolo-02** so it uses REAL ideas, not examples

**IF N:**
- Display: "Какие идеи нужно изменить?"
- Return to step 2 (request new input)

**IF ?:**
- Display full YAML of collected ideas
- Return to confirmation menu

---

## 🚨 CRITICAL RULES

- 🛑 NEVER generate ideas yourself (this is the bug!)
- 📋 ALWAYS wait for user to provide ideas
- 💬 Accept any format the user provides
- 🚫 Don't proceed until user confirms [Y]
- 📝 Pass userIdeas to step-yolo-02 (not examples!)

---

## SUCCESS CRITERIA

- ✅ User's 3 ideas collected
- ✅ Ideas confirmed and understood
- ✅ Ready to pass to parallel execution
- ✅ Bug fixed: using REAL content, not generated examples

---

## NEXT STEP

When user confirms [Y]:
- Load, read entire file, then execute step-yolo-02-parallel-execute.md
- Pass userIdeas as input to parallel agents
