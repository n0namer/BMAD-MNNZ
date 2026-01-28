---
description: User selects which idea they want to write about
name: step-c-03a-select-idea
nextStepFile: ./step-c-03b-select-angle.md
type: selection
---

# CREATE C-03: Write Post - Select Idea

## STEP GOAL:

User selects which researched idea to write a post about.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Load Researched Ideas

Load from ideas_research.csv (ideas that have been researched).

### 2. Display Options

```
═══════════════════════════════════════════════════════════════

  ✍️  WRITE POST: Select Idea

═══════════════════════════════════════════════════════════════

Какую идею ты хочешь развить в пост?

[1] "ИИ контент за 3 часа" (8 углов найдено)
    Категория: automation | Исследовано: 2026-01-27

[2] "Speech-to-text для постов" (7 углов найдено)
    Категория: tech | Исследовано: 2026-01-27

[3] "Масштабирование личного бренда" (9 углов найдено)
    Категория: market | Исследовано: 2026-01-27

─────────────────────────────────────────────────────────────

[+] ADD & RESEARCH FIRST — Добавить и исследовать новую идею
[?] HELP — Показать справку
[M] Back to MENU — Вернуться в меню

═════════════════════════════════════════════════════════════════
```

### 3. Handle Selection

**[1-N] Select idea:**
```
Выбрал идею: "ИИ контент за 3 часа"

Переходим к выбору угла...
```
Load, read entire file, then execute `./step-c-03b-select-angle.md`

**[+] ADD & RESEARCH:**
Load, read entire file, then execute `../mode-c-01/step-c-01-add-idea.md`

**[?] HELP:**
Show detailed explanation of each idea

**[M] Back to MENU:**
Load `../mode-c-00-menu.md`

---

## NEXT STEP

When idea selected: Load, read entire file, then execute step-c-03b-select-angle.md

### Menu Handling Logic

**IF [M]: Back to MENU:**
Load `../mode-c-00-menu.md`

---

## NEXT STEP

When idea selected: Load, read entire file, then execute step-c-03b-select-angle.md

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.
