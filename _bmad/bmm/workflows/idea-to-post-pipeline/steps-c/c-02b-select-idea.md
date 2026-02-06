---
description: User selects which idea to research
name: step-c-02b-select-idea
nextStepFile: ./c-02c-research.md
type: selection
---

# CREATE C-02: Research - Select Idea

## STEP GOAL:

User selects which idea to research. Confirm and proceed.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Confirm Selection

User selected idea #[N].

```
Ты выбрал идею:

  "ИИ контент за 3 часа"
  Категория: automation
  Добавлено: 2026-01-27

Правильно?
[Y] Да, исследуй эту идею!
[N] Нет, выбрать другую
[?] Показать ещё идеи
```

### 2. Handle Responses

**[Y] - Confirm:**
```
✅ Начинаю исследование...

Будет поиск:
  • 5-10 разных углов для представления идеи
  • Источники и факты для каждого угла
  • Релевантность каждого угла (0-100%)

Это займет 15-20 минут... ⏳
```
Load, read entire file, then execute `./step-c-02c-research.md`

**[N] - Back:**
Load `./step-c-02a-load-ideas.md` (show list again)

**[?] - Show list:**
Redisplay ideas list from step-c-02a


### Menu Handling Logic

**IF [Y]: - Confirm:**
```
✅ Начинаю исследование...

Будет поиск:
  • 5-10 разных углов для представления идеи
  • Источники и факты для каждого угла
  • Релевантность каждого угла (0-100%)

Это займет 15-20 минут... ⏳
```
Load, read entire file, then execute `./step-c-02c-research.md`

**IF [N]: - Back:**
Load `./step-c-02a-load-ideas.md` (show list again)

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.
---

## NEXT STEP

When user confirms [Y]:
- Load, read entire file, then execute step-c-02c-research.md
- Pass selected_idea_id to next step
