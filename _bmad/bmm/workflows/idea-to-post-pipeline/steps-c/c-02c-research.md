---
description: Execute research - find 5-8 angles with sources and facts
name: step-c-02c-research
nextStepFile: ./c-02d-results.md
type: research-execution
---

## SAVED DATA

Results saved to ideas_research.csv:
```csv
id,original_idea_id,research_date,main_angle,sub_angles_count,best_angle_id,angles_list,sources_count,avg_relevance
1,1,[today],"Time Saving via ИИ",8,"angle_1",[list of angles],32,86
```

---

## NEXT STEP

Handle user selection from step 4

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# CREATE C-02: Research - Execute

## STEP GOAL:

Research the selected idea and find 5-8 different angles with supporting sources.

## EXECUTION:

### 1. Display Research Start

```
═══════════════════════════════════════════════════════════════

  🔍 RESEARCHING: "ИИ контент за 3 часа"

  Поиск углов, источников и фактов...

═══════════════════════════════════════════════════════════════
```

### 2. Research Process

Using web search + analysis, find angles like:

```
ANGLE 1: Time Saving ⏱️
├─ Main insight: "Saves 70% of content creation time"
├─ Sources found: 7 (news articles, blogs, studies)
├─ Key facts:
│  • Average copywriter: 2-3 hours per post
│  • With ИИ: 20-30 minutes per post
│  • Relevance: 92% (highly relevant)
└─ Best for: Founders, agencies, busy entrepreneurs

ANGLE 2: Quality Control 🎯
├─ Main insight: "ИИ content can be higher quality if well-guided"
├─ Sources found: 5 (studies, case studies)
├─ Key facts:
│  • Quality depends on prompts and editing
│  • Best practice: ИИ write → human edit
│  • Relevance: 88% (relevant)
└─ Best for: Perfectionists, detail-oriented teams

ANGLE 3: Scalability 📈
├─ Main insight: "Create unlimited variations without hiring"
├─ Sources found: 6 (business blogs, research)
├─ Key facts:
│  • Hiring writer: $2000-5000/month
│  • ИИ subscription: $20-40/month
│  • Relevance: 85% (relevant)
└─ Best for: Growth-focused businesses

ANGLE 4: Learning Tool 📚
├─ Main insight: "Using ИИ teaches you better copywriting"
├─ Sources found: 4 (opinion pieces, educational)
├─ Key facts:
│  • ИИ shows different writing styles
│  • Forces you to refine your prompts
│  • Relevance: 78% (relevant)
└─ Best for: Aspiring copywriters, learners

...and so on (up to 8-10 angles)
```

---

### 2.5 Генерация Болей Предпринимателей (Content Machine Stage 2)

**Триггер:** Только если `content_type == "demo"` (режим [R] в c-01)

На этом шаге система автоматически генерирует **3-5 предпринимательских болей** для КАЖДОГО исследованного угла.

**Логика:**

Для каждого angle (angle_1, angle_2, ..., angle_N):

```
Система вызывает LLM с промптом:

РУТИНА (что вы демонстрируете):
"{idea_text}"

КОНТЕКСТ:
- Инструменты: {tools_used}
- Результат: {demonstrated_result}

УГОЛ ПУБЛИКАЦИИ:
"{angle_name} — {angle_description}"

ЗАДАЧА:
Генерируй 3-5 **болей предпринимателей**, которые эта рутина закрывает.

Боли должны быть на языке бизнеса (не техники):
- Скорость обработки информации
- Зависимость от конкретных людей
- Нет описанных процессов
- Невозможность масштабировать
- Потеря контекста при передаче
- Высокие зарплаты специалистов

Результат: JSON список из 3-5 болей.
```

**Вывод для каждого угла:**

```
ANGLE 1: Time Saving ⏱️
Боли, которые эта рутина решает:
├─ 🔴 Медленная документация берёт 2-3 дня на большой объём
├─ 🔴 Все процессы в голове у одного человека
├─ 🔴 Нельзя масштабировать без найма новых специалистов
└─ 🔴 Непроцессированная информация = нельзя продать бизнес

ANGLE 2: Quality Control 🎯
Боли, которые эта рутина решает:
├─ 🔴 Качество документов зависит от тогоне написал их
├─ 🔴 Нет стандарта, каждый пишет по-своему
├─ 🔴 Редактирование и проверка занимают много времени
└─ 🔴 Трудно передать задачу другому (плохо описано)
```

**Сохранение:**

Система добавляет колонку `pain_points_json` в ideas_research.csv:

```csv
id, original_idea_id, ..., pain_points_json
1, 1, ..., "{\"angle_1\": {\"pains\": [\"Боль 1\", \"Боль 2\", \"Боль 3\"]}, \"angle_2\": {...}}"
```

**Следующий шаг:**
Система продолжит к Шагу 3 (Aggregate Results) с сохранёнными болями.

---

### 3. Aggregate Results

```
═══════════════════════════════════════════════════════════════

  ✅ RESEARCH COMPLETE

  Found: 8 different angles
  Sources: 32 total (average 4 per angle)
  Avg relevance: 86% (GOOD)
  Time: 18 minutes

═════════════════════════════════════════════════════════════════

Результаты сохранены в ideas_research.csv
```

### 4. Offer Next Steps

```
Что дальше?

[W] WRITE — Написать пост из одного из этих углов
[A] ANGLES — Посмотреть все углы в деталях
[M] Back to MENU — Вернуться в меню

═════════════════════════════════════════════════════════════════
```

**[W] WRITE:**
Load, read entire file, then execute `./c-03a-select-idea.md`

**[A] ANGLES:**
Load, read entire file, then execute `./c-02d-results.md`

**[M] Back to MENU:**
Load `./c-00-menu.md`

---

## SAVED DATA

Results saved to ideas_research.csv:
```csv
id,original_idea_id,research_date,main_angle,sub_angles_count,best_angle_id,angles_list,sources_count,avg_relevance
1,1,[today],"Time Saving via ИИ",8,"angle_1",[list of angles],32,86
```

---

## NEXT STEP

Handle user selection from step 4
