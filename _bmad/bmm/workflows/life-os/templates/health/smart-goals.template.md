---
template: smart-goals
domain: health
tier: 2
framework: SMART Goals for Fitness
applicability: medium
timeInvestment: quick
complexity: low
synergies:
  - progressive-overload
  - health-belief-model
  - macros-tracking
integration_points:
  - step-01-collect-ideas.md
  - step-04-consilium.md
  - step-05-scoring.md
  - step-08-deep-plan.md
outputs:
  - smart-goals-analysis.md
  - Append to workflow-plan.md
scoring_contribution:
  step_05_criteria:
    - name: health_readiness
      weight: 0.15
    - name: sustainability
      weight: 0.10
    - name: goal_clarity
      weight: 0.10
deep_plan_contribution:
  generates_l2: true
  l2_pattern: "Milestone-based: Baseline -> Phase 1 -> Phase 2 -> Phase 3 -> Review"
  generates_l3: true
---

# SMART Goals for Fitness: {Project Name}

**Domain:** Health & Fitness
**Generated:** {date}
**Analyst:** {user_name}
**Meta-Score:** 6.6/10 (Tier 2)

> ---
> ## WARNING: SMART Goals -- Переоцененный Фреймворк
>
> **Исследования 2024-2025 показывают значительные ограничения SMART:**
>
> - Narrative review (2021): **нет значимой разницы** между specific goals (d=0.589)
>   и vague goals (d=0.511) для физической активности
> - SMART "не основан на научной теории; не согласуется с эмпирическими данными;
>   не учитывает тип поставленной цели"
> - Non-specific goals привели к такому же или большему уровню физической активности
>   у недостаточно активных взрослых
> - 2025 исследования: SMART goals не эффективнее "do-your-best" goals для
>   креативных или комплексных задач
>
> **Рассмотрите FAST альтернативу** (см. секцию ниже) для инновационных целей.
>
> **Когда SMART все же работает:** четкие skill-based цели (увеличить жим лежа на
> 20 кг), краткосрочные объективные метрики (4-16 недель), спортивные результаты.
> ---

## Цель Фреймворка

SMART -- акроним для критериев постановки целей: Specific, Measurable, Achievable, Relevant, Time-bound. Разработан George T. Doran (1981) для бизнес-менеджмента, адаптирован для фитнеса организациями NASM, ACE, NSCA. Основан на теории целеполагания Locke & Latham (1990): конкретные, сложные цели ведут к более высокой производительности, чем размытые.

**Важно:** SMART полезен, но НЕ превосходит другие методы постановки целей по данным последних исследований. Лучше всего подходит для четких, skill-based задач; потенциально ограничивает для исследовательских или комплексных целей.

## Когда Использовать

**Триггеры:**
- Keywords: цель, результат, прогресс, измерение, дедлайн, достижение
- Keywords (EN): goal, target, measurable, deadline, achievement, performance

**Идеально для:**
- Performance goals: увеличить силу, улучшить время забега, достичь конкретного веса
- Четкие milestones с объективными критериями успеха
- Краткосрочные и среднесрочные цели (4-16 недель)
- Мастерство техники (правильная форма deadlift, техника плавания)

**НЕ использовать для (на основе исследований 2025):**
- Исследовательские цели ("найти вид спорта, который нравится")
- Креативные задачи (интуитивное движение, новые виды спорта)
- Комплексное изменение поведения (лучше: Habit Loop)
- Долгосрочная трансформация образа жизни (лучше: HBM + Habit Loop)

## SMART vs. FAST: Дерево Решений

```
Цель четко измерима? (вес, время, повторения)
  |
  +-- ДА --> Цель краткосрочная? (4-16 недель)
  |           |
  |           +-- ДА --> SMART подходит
  |           +-- НЕТ --> Разбить на серию SMART (по 4-10 недель каждая)
  |
  +-- НЕТ --> Цель исследовательская / инновационная?
              |
              +-- ДА --> Используй FAST
              +-- НЕТ --> Используй non-specific goals ("тренироваться 3 раза в неделю")
```

### FAST Framework (Альтернатива)

| Критерий | SMART | FAST |
|----------|-------|------|
| **F** | - | **Frequently discussed** -- регулярно обсуждается, не забывается |
| **A** | Achievable (достижимо) | **Ambitious** -- амбициозно, вдохновляет |
| **S** | Specific (конкретно) | **Specific** -- конкретно (совпадает) |
| **T** | Time-bound (ограничено временем) | **Transparent** -- прозрачно для команды/окружения |
| **M** | Measurable | - (измеримость не обязательна для всех целей) |
| **R** | Relevant | - (релевантность подразумевается амбицией) |

**Когда FAST лучше:** цели, требующие прорывного мышления, долгосрочная трансформация, командные цели.

## Интеграция с Life OS

### Step 1 (Collect Ideas)
- Зафиксировать исходную формулировку цели
- Оценить, подходит ли SMART (см. дерево решений выше)

### Step 4 (Consilium)
- White Hat: исследовать реалистичные таймфреймы и темпы улучшения
- Red Hat: интуитивная проверка -- цель вдохновляет или пугает?
- Black Hat: риски (травма, перетренированность, конфликты с жизнью)

### Step 5 (Scoring)
- SMART Score влияет на оценку качества формулировки цели
- Если "Achievable" < 5 -> флаг "Overly Ambitious"
- Если "Measurable" < 5 -> флаг "Needs Tracking System"
- Если цель исследовательская -> рекомендовать снять SMART ограничения

### Step 8 (Deep Plan)
- L2: каждый milestone становится фазой плана
- L3: конкретные тренировочные/питательные действия
- Checkpoints: тестирование прогресса на каждом milestone

## Структура Фреймворка

### Goal Statement (Исходная формулировка)
[Запишите цель в свободной форме]

### S -- Specific (Конкретность)

**Что именно я хочу достичь?**
- Кто: [кто вовлечен?]
- Что: [конкретный результат]
- Где: [место действия]
- Почему: [зачем это важно]

**Конкретная формулировка:** [переписанная конкретная версия]
**Оценка (1-10):** ___

### M -- Measurable (Измеримость)

**Как я узнаю, что достиг цели?**
- Основная метрика: [вес, время, повторения, дистанция]
- Дополнительные метрики: [body fat %, heart rate, RPE]
- Метод трекинга: [приложение, дневник, весы]

**Измеримая цель:** [X к дате Y]
**Оценка (1-10):** ___

### A -- Achievable (Достижимость)

**Реалистична ли цель при моих ресурсах?**
- Текущий baseline: [измерение]
- Требуемое улучшение: [X%, абсолютное значение]
- Временной горизонт: [недели]
- Реалистичность: [да/нет + обоснование, ~1-2% улучшения в неделю]
- Необходимые ресурсы: [время, деньги, оборудование, знания]

**Оценка (1-10):** ___

### R -- Relevant (Релевантность)

**Почему эта цель важна?**
- Связь с ценностями: [какие ценности поддерживает]
- Влияние: [какую разницу создаст]
- Приоритет: [высокий/средний/низкий]
- Конкурирующие цели: [что может помешать]

**Оценка (1-10):** ___

### T -- Time-bound (Ограничение временем)

**Когда я достигну цели?**
- Дата старта: [YYYY-MM-DD]
- Финальный дедлайн: [YYYY-MM-DD]
- Milestones:
  - [Дата]: [Milestone 1 -- промежуточная метрика]
  - [Дата]: [Milestone 2]
  - [Дата]: [Milestone 3]

**Оценка (1-10):** ___

### SMART Total Score

```
SMART Score = (Specific + Measurable + Achievable + Relevant + Time-bound) / 5
```

| Критерий | Оценка (1-10) |
|----------|---------------|
| Specific | ___ |
| Measurable | ___ |
| Achievable | ___ |
| Relevant | ___ |
| Time-bound | ___ |
| **SMART Score** | **___/10** |

**Интерпретация:**
- 8-10: Хорошо сформулированная SMART цель, приступать
- 5-7: Нуждается в доработке слабых областей
- 1-4: Плохо определена, переформулировать

**Альтернативная рекомендация:** Если SMART score низкий И цель исследовательская -> рассмотреть non-specific goal формат или FAST.

### Финальная SMART Формулировка

"Я [измеримый результат] к [дата] путем [конкретные действия] для [релевантный результат]."

## Tracking Dashboard

### Еженедельные Метрики

| Неделя | Тренировки | Осн. метрика | Доп. метрика | Прогресс vs. Plan | Заметки |
|--------|------------|--------------|--------------|---------------------|---------|
| 1 | ___/___ | ___ | ___ | On track / Behind | |
| 2 | ___/___ | ___ | ___ | | |
| 3 | ___/___ | ___ | ___ | | |
| 4 | ___/___ | ___ | ___ | Checkpoint 1 | |

### Checkpoint Reviews

**Checkpoint 1 (Week ___)**:
- Milestone достигнут: [да/нет + фактическое значение]
- Adherence: [выполненных / запланированных тренировок]
- Что работает: [описание]
- Корректировки: [что изменить]

## Заполнение из Workflow Plan

**Auto-population rules:**
- `project_name` -> из frontmatter workflow-plan.md
- Baseline metrics -> из начальной оценки в Step 1
- Timeline -> из calendar sync (Step 7)
- Если MCDA criterion "Performance" -> pre-fill "Measurable" секцию

## Научная База

### Позитивные находки:
1. **Locke & Latham (1990):** Specific, challenging goals -> higher performance чем vague goals
2. **NASM certification standard:** SMART widely used в клинических, спортивных, wellness settings
3. **Goal-setting + regular feedback** ARE effective для увеличения физической активности

### Критические находки (2024-2025):
4. **Narrative review (2021, Taylor & Francis):** No significant difference между specific и vague goals для физической активности (d=0.589 vs d=0.511)
5. **SMART criteria** "is not based on scientific theory; is not consistent with empirical evidence"
6. **Non-specific goals** led to at least as much physical activity для insufficiently active adults
7. **2025 research:** SMART goals no more effective чем "do-your-best" goals для creative/complex tasks

### Вердикт:
SMART полезен для **skill-based, measurable objectives** (спортивные результаты, силовые показатели). Для комплексных целей и поведенческих изменений -- рассмотреть альтернативы.

## Частые Ошибки

1. **Слишком амбициозная цель** -- нереалистичный timeline ведет к демотивации и травмам
2. **Ригидность** -- неспособность адаптировать план при изменении обстоятельств
3. **Фокус на outcome, не на process** -- "похудеть на 10 кг" вместо "тренироваться 4 раза в неделю"
4. **Длинные SMART цели (40+ недель)** -- исследования показывают, что non-specific goals эффективнее для долгих периодов. Разбивать на серию 4-10 недельных SMART
5. **Отсутствие baseline** -- невозможно оценить "Achievable" без текущих измерений
6. **Игнорирование recovery** -- включать recovery метрики в "Measurable" (сон 8ч, resting HR < 60 bpm)

## Метрики и Измерения

### Первичные метрики (по типу цели):

| Тип цели | Первичная метрика | Частота | Инструмент |
|-----------|-------------------|---------|------------|
| Weight loss | Вес тела, body fat % | Еженедельно | Весы, калипер |
| Strength | 1RM или рабочий вес | Каждые 2-4 нед. | Дневник тренировок |
| Endurance | Время/дистанция | Еженедельно | Strava, Garmin |
| Habit | Streak / adherence | Ежедневно | Трекер привычек |
| Body comp | Обхваты, фото | Ежемесячно | Лента, камера |

### Визуализация прогресса:
```
Baseline:    xxxxxxxxxx....................  [Текущее значение]
Milestone 1: xxxxxxxxxxxxxxx...............  [Промежуточная цель]
Milestone 2: xxxxxxxxxxxxxxxxxxxx..........  [Промежуточная цель]
Goal:        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  [Финальная цель]
```

## Синергии с Другими Фреймворками

### SMART + Health Belief Model
- HBM отвечает "Смогу ли я?" (self-efficacy)
- SMART отвечает "Что именно я делаю?" (specificity)
- Комбинация: HBM для оценки готовности -> SMART для определения выполнения

### SMART + Progressive Overload
- SMART дает конечную цель (bench press 100 кг к 1 июня)
- Progressive Overload дает путь (увеличивать вес на 1-2.5 кг каждую неделю)
- Вместе: четкая цель + проверенный метод достижения

### SMART + Habit Loop
- SMART определяет outcome (что достичь)
- Habit Loop определяет daily behaviors (как двигаться к цели)
- Пример: Goal = "Бегать 3 раза/нед 12 недель" (SMART), Habit = "После утреннего кофе надеть кроссовки" (Habit Loop cue)

### SMART + Recovery Protocols
- SMART goals могут провоцировать перетренированность без баланса
- Решение: включить recovery метрики в "Measurable"
- Пример: "Тренироваться 4 раза/нед И спать 8+ часов И resting HR < 60 bpm"

### SMART + TRIZ
- Противоречие: "Агрессивный timeline для мотивации" vs. "Агрессивные timelines = риск травмы"
- TRIZ Principle #9 (Предварительное антидействие): встроенные deload weeks каждую 4-ю неделю
- TRIZ Principle #11 (Предварительная подстраховка): диапазон цели "100-105 кг" вместо жесткого "105 кг"

## Память Claude Flow

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "health:smart-goals:template-usage:{project_id}" \
  --content "SMART applied to {project_name}: Score={score}/10, Goal={goal_statement}, Timeline={weeks}wk. WARNING: Consider FAST for exploratory goals."
```
