---
description: Central hub for choosing between 4 operational modes (CREATE/EDIT/VALIDATE/YOLO)
name: step-00-menu
nextStepFile_Create: ./steps-c/c-00-menu.md
nextStepFile_Edit: ./steps-e/e-00-menu.md
nextStepFile_Validate: ./steps-v/v-00-menu.md
nextStepFile_Yolo: ./steps-yolo/yolo-01-input.md
type: main-menu
---

# Main Menu: Choose Your Mode

## STEP GOAL:

To present all 4 operational modes clearly, allow user to select one, and route them to the appropriate mode workflow.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator

### Role Reinforcement:

- ✅ You are a Workflow Coordinator
- ✅ Help user choose the right mode for their current needs
- ✅ Provide clear, concise information
- ✅ Maintain professional, supportive tone

### Step-Specific Rules:

- 🎯 Focus ONLY on mode selection
- 🚫 FORBIDDEN to force user into a specific mode
- 💬 Use clear, visual presentation
- 📋 Show time estimates and use cases

## EXECUTION PROTOCOLS:

- 🎯 Display all 4 modes with descriptions
- 💾 Wait for user selection [1-4]
- 📖 Route to correct mode menu
- 🚫 Halt at menu until user selects

---

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Display Mode Overview

Present all 4 modes in Russian with clear formatting:

```
═══════════════════════════════════════════════════════════════

             🎯 CHOOSE YOUR MODE

═══════════════════════════════════════════════════════════════

[1] CREATE MODE
    ─────────────────────────────────────────────────────────
    Для создания новых постов

    Процесс: Идеи → Исследование → Написание → Метрики

    Режимы внутри:
      [1a] Добавить идею
      [1b] Исследовать идею (5-10 углов)
      [1c] Написать пост (3 варианта: 500/250/100)
      [1d] Поиск постов
      [1e] Редактировать пост (быстрые правки)
      [1f] Объединить посты
      [1g] Аналитика (top posts, insights)
      [1h] Управление базой (backup, export)

    Для кого: Создание контентной библиотеки
    Взаимодействие: Совместное (50/50 ты и я)
    Время: 2-3 часа на цикл (идея → 3 поста + метрики)
    Особенность: Feedback loops, continuable sessions

    Best for: Основной workflow создания контента

───────────────────────────────────────────────────────────────

[2] EDIT MODE
    ─────────────────────────────────────────────────────────
    Для улучшения существующих постов

    Режимы внутри:
      [2a] Массовое редактирование
      [2b] Редактирование по чек-листу
      [2c] A/B тестирование вариантов
      [2d] Обновление метрик
      [2e] Переписать low-CTR посты
      [2f] Архивировать старые посты
      [2g] История версий
      [2h] Сравнить посты

    Для кого: Оптимизация опубликованного контента
    Взаимодействие: Автономное с рекомендациями (70% я)
    Время: 30-60 мин на цикл
    Особенность: Batch operations, auto-improvement suggestions

    Best for: Улучшение CTR underperformers

───────────────────────────────────────────────────────────────

[3] VALIDATE MODE
    ─────────────────────────────────────────────────────────
    Для проверки качества

    Режимы внутри:
      [3a] Проверка качества по чек-листу
      [3b] Аудит перформанса
      [3c] Проверка консистентности
      [3d] Аудит копирайтинга
      [3e] Проверка engagement потенциала
      [3f] Batch валидация всех постов
      [3g] Валидация идей перед созданием
      [3h] Генерация отчёта о качестве

    Для кого: Pre-publishing validation & batch improvement
    Взаимодействие: Автономное (90% я)
    Время: 10-30 мин на цикл
    Особенность: 5 параллельных проверок, scoring

    Best for: Quality assurance перед публикацией

───────────────────────────────────────────────────────────────

[4] YOLO MODE 🚀 MVP Feature
    ─────────────────────────────────────────────────────────
    Для ПОЛНОЙ АВТОМАТИЗАЦИИ за минуты

    Процесс: Spec → Parallel add → Parallel research → Parallel write
             → Auto-validate → Auto-improve → Generate variants → Summary

    Пример: "YOLO: 3 идеи → 9 постов с auto-fix"

    Включает:
      ✅ Параллельное добавление идей
      ✅ Параллельное исследование (3x faster)
      ✅ Параллельное написание постов
      ✅ Автоматическая валидация (5 checks)
      ✅ Автоматическое улучшение (если score < 90%)
      ✅ Генерация 3-4 вариантов (разные углы)
      ✅ Итоговый report с выбором

    Для кого: Fast prototyping & content sprints
    Взаимодействие: 100% автономное (до итогов)
    Время: 3-5 минут (вместо 6-8 часов!)
    Особенность: Parallel execution, self-checking, no interruptions

    Best for: MVP демонстрация, быстрые sprint'ы

    Примеры команд:
      YOLO: 5 идей → 15 постов с auto-fix
      YOLO: 3 идеи + research + write + validate
      YOLO: Batch улучшить low-CTR посты

───────────────────────────────────────────────────────────────

[?] Help — Показать этот экран снова
[A] Advanced Elicitation — Глубокое изучение
[P] Party Mode — Мультиперспективное обсуждение

═══════════════════════════════════════════════════════════════
```

### 2. Present Selection Menu

Display in Russian:

```
ВЫБЕРИ РЕЖИМ:

[1] CREATE — Создание контента
[2] EDIT — Редактирование постов
[3] VALIDATE — Проверка качества
[4] YOLO — Полная автоматизация

[?] Помощь
[A] Advanced Elicitation
[P] Party Mode
```

### 3. Handle User Selection

#### Option [1] - CREATE Mode:
```
Переходим в CREATE MODE...
Выбирай что делать:
[1a] Добавить новую идею
[1b] Исследовать идею
[1c] Написать пост
[1d] Поиск постов
[1e] Редактировать пост
[1f] Объединить посты
[1g] Аналитика
[1h] Управление базой
```
Load, read entire file, then execute `./steps-c/c-00-menu.md`

#### Option [2] - EDIT Mode:
```
Переходим в EDIT MODE...
```
Load, read entire file, then execute `./steps-e/e-00-menu.md`

#### Option [3] - VALIDATE Mode:
```
Переходим в VALIDATE MODE...
```
Load, read entire file, then execute `./steps-v/v-00-menu.md`

#### Option [4] - YOLO Mode:
```
🚀 ЗАПУСКАЕМ YOLO AUTOMATION!

Скажи мне что ты хочешь создать:

Примеры:
  "YOLO: 3 идеи → 9 постов с auto-fix"
  "YOLO: 5 идей + research + write"
  "YOLO: Batch улучшить low-CTR посты"

Или просто опиши что нужно...
```
Load, read entire file, then execute `./steps-yolo/yolo-01-input.md`

#### Option [?] - Help:
Return to step 1 (redisplay this menu)

#### Option [A] - Advanced Elicitation:
Execute Advanced Elicitation workflow, then return to this menu

#### Option [P] - Party Mode:
Execute Party Mode workflow to discuss workflow approaches, then return to this menu

#### Option Any Other Input:
Display: "Не понимаю 🤔 Выбери [1], [2], [3], [4], [?], [A] или [P]"
Return to menu

---

## 🚨 CRITICAL RULES

- 🛑 ALWAYS halt and wait for user input
- 📋 ONLY proceed when user selects [1-4]
- 💬 If user selects [A] or [P], return to menu after completion
- 🚫 NEVER force user into a mode

---

## SUCCESS CRITERIA

- ✅ All 4 modes clearly explained
- ✅ User understands differences between modes
- ✅ User feels empowered to choose
- ✅ Selection handled correctly and routed properly

---

## NEXT STEP

When user selects [1-4]:
- Display confirmation
- Load, read entire file, then execute appropriate mode menu file
- Maintain current session state in workflow_state.json
