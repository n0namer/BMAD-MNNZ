---
description: Collect raw idea, validate against criteria, add to ideas_inbox
name: step-c-01-add-idea
nextStepFile: ../../mode-c/mode-c-00-menu.md
type: input-collection
---

## SAVED DATA

Idea automatically saved to ideas_inbox.csv:
```csv
id,date_added,source,raw_idea,category,status,notes
[N],[today],user_input,"[idea description]",[category],active,[auto-generated notes]
```

---

## NEXT STEP

Handle user selection and route accordingly

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# CREATE C-01: Add New Idea

## STEP GOAL:

Collect a raw idea from user, validate it, and add to ideas_inbox.csv.

## EXECUTION:

### 1. Request Idea Input

```
═══════════════════════════════════════════════════════════════

  💡 ADD NEW IDEA

  Расскажи мне идею для контента. Может быть что угодно:
  • Проблема которую ты видишь
  • Инсайт который хочешь поделиться
  • Тренд в твоей нише
  • Вопрос который часто слышишь
  • Что-то что тебя вдохновило

  Просто напиши (2-3 предложения достаточно):

═══════════════════════════════════════════════════════════════
```

Wait for user input.

### 2. Validate Idea

Check against [idea-validation-checklist.md](../../data/checklist-templates/idea-validation-checklist.md):

```
Проверяю твою идею...

✓ Специфичная? ✅
✓ Исследуемая? ✅
✓ Аудитория понятна? ✅
✓ Не дубликат? ✅

Статус: ✅ PASS — Идея готова к исследованию!
```

If FAIL:
```
⚠️  Вопросы по идее:
  • [Specific feedback]
  • [Suggestion for improvement]

Хочешь доработать или выбрать другую идею?
```

### 3. Add to Inbox

```
Добавляю идею в inbox...

Идея #[N]:
├─ Title: "[user-provided-title]"
├─ Raw description: "[description]"
├─ Category: [detected/user-specified]
├─ Status: active
├─ Date added: [today]
└─ Priority: [medium by default]

✅ Идея добавлена в ideas_inbox.csv
```

### 4. Present Next Options

```
═══════════════════════════════════════════════════════════════

  Что дальше?

  [R] RESEARCH — Исследуй эту идею (найти углы)
  [A] ADD MORE — Добавь ещё идею
  [M] Back to CREATE MENU — Другие операции

═══════════════════════════════════════════════════════════════
```

**[R] RESEARCH:**
Load, read entire file, then execute `../mode-c-02/step-c-02a-load-ideas.md`

**[A] ADD MORE:**
Return to step 1 (request new idea)

**[M] Back to CREATE MENU:**
Load `../mode-c-00-menu.md`

---

## SAVED DATA

Idea automatically saved to ideas_inbox.csv:
```csv
id,date_added,source,raw_idea,category,status,notes
[N],[today],user_input,"[idea description]",[category],active,[auto-generated notes]
```

---

## NEXT STEP

Handle user selection and route accordingly
