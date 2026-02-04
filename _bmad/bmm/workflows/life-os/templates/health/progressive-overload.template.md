---
template: progressive-overload
domain: health
tier: 1
framework: Progressive Overload
applicability: high
timeInvestment: moderate
complexity: low
synergies:
  - recovery-protocols
  - smart-goals
  - macros-tracking
  - habit-loop
integration_points:
  - step-01-collect-ideas.md
  - step-04-consilium.md
  - step-05-scoring.md
  - step-08-deep-plan.md
outputs:
  - progressive-overload-analysis.md
  - Append to workflow-plan.md
scoring_contribution:
  step_05_criteria:
    - name: health_readiness
      weight: 0.15
    - name: sustainability
      weight: 0.10
    - name: progression_rate
      weight: 0.12
    - name: injury_risk
      weight: 0.08
deep_plan_contribution:
  generates_l2: true
  l2_pattern: "Cycle-based: Foundation -> Progressive -> Peak -> Deload (repeating)"
  generates_l3: true
---

# Progressive Overload: {Project Name}

**Domain:** Health & Fitness (Fitness-Specific)
**Generated:** {date}
**Analyst:** {user_name}
**Tier:** 1 (Fundamental Training Principle)

## Цель Фреймворка

Progressive Overload -- фундаментальный принцип тренировки, впервые описанный Thomas Delorme (1945) в контексте реабилитации. Суть: для адаптации организм должен подвергаться постоянно увеличивающейся нагрузке. Без прогрессии тело адаптируется к текущему уровню стресса и перестает развиваться. Этот принцип применяется к силе, выносливости, гипертрофии, мощности и любому физическому качеству.

**Научный принцип:** General Adaptation Syndrome (Hans Selye, 1936) -- организм проходит через фазы Alarm -> Resistance -> Exhaustion. Progressive Overload оптимизирует фазу Resistance, избегая Exhaustion через периодизацию и deload.

## Когда Использовать

**Триггеры:**
- Keywords: сила, мышцы, прогрессия, тренировка, нагрузка, периодизация, программа
- Keywords (EN): strength, muscle, progression, training, load, periodization, program, plateau

**Идеально для:**
- Силовые тренировки (powerlifting, bodybuilding, general fitness)
- Программы набора мышечной массы
- Беговые программы (увеличение дистанции/скорости)
- Спортивная подготовка (sport-specific performance)
- Реабилитация (gradual return to activity)

**НЕ использовать для:**
- При наличии острой травмы (сначала: Recovery Protocols)
- Без начального baseline (сначала: 2-3 недели вводных тренировок)
- Для начинающих без техники (сначала: technique mastery)

## Интеграция с Life OS

### Step 1 (Collect Ideas)
- Определить тип физического качества для развития
- Зафиксировать текущий уровень (baseline assessment)

### Step 4 (Consilium)
- Strength Coach specialist проектирует периодизацию
- Sports Medicine specialist оценивает ограничения

### Step 5 (Scoring)
- Progression Rate -> оценка темпа прогресса (реалистичность)
- Injury Risk -> оценка риска травмы при данной прогрессии
- Recovery Adequacy -> достаточность восстановления

### Step 8 (Deep Plan)
- L2: Training blocks / мезоциклы (4-6 недель каждый)
- L3: отдельные тренировочные сессии и упражнения
- Deload week каждые 4-8 недель

## Структура Фреймворка

### Тренировочная Цель

**Что я хочу улучшить?**
- [ ] Strength (максимальная сила)
- [ ] Hypertrophy (мышечный рост)
- [ ] Endurance (выносливость)
- [ ] Power (мощность / скоростная сила)
- [ ] Skill (техническое мастерство)

**Конкретная цель:** [например, "Bench press 100 кг", "Пробежать 10 км за 50 мин"]
**Текущий уровень:** [измерение]
**Дата оценки:** [YYYY-MM-DD]

### 5 Переменных Прогрессии

#### 1. Weight / Вес (Intensity)

**Текущий:** [кг/lbs]
**План прогрессии:**
- Новичок: +2.5 кг/неделю (верх тела), +5 кг/неделю (низ тела)
- Средний: +1-2.5 кг каждые 1-2 недели
- Продвинутый: +0.5-1 кг каждые 2-4 недели

**Микро-прогрессия:** использовать 0.5-1.25 кг пластины для преодоления плато

#### 2. Reps / Повторения (Volume)

**Текущие:** [X reps]
**План прогрессии:** +1-2 rep/неделю при том же весе -> когда достигнут верхний диапазон -> увеличить вес, снизить reps

**Оптимальные диапазоны по целям:**

| Цель | Повторения | % от 1RM | Отдых |
|------|------------|----------|-------|
| Сила | 1-5 | 85-100% | 3-5 мин |
| Гипертрофия | 6-12 | 65-85% | 60-90 сек |
| Выносливость | 12-20+ | 50-65% | 30-60 сек |
| Мощность | 1-5 | 75-90% | 2-5 мин |

#### 3. Sets / Подходы (Volume)

**Текущие:** [X sets]
**План прогрессии:** +1 set каждые 2-4 недели
**Рекомендации:** 10-20 sets/мышечная группа/неделю для гипертрофии (Schoenfeld 2017)

#### 4. Frequency / Частота

**Текущая:** [X sessions/week]
**План прогрессии:** Добавлять 1 тренировку когда recovery позволяет
**Рекомендации:** Каждая мышечная группа 2-3 раза/неделю для оптимальной гипертрофии

#### 5. Density / Плотность (Decreased Rest)

**Текущий отдых:** [X секунд между подходами]
**План прогрессии:** -10-15 сек каждые 2 недели (только для endurance/conditioning)
**Важно:** Не сокращать отдых для силовых целей (нужны полные 3-5 мин)

### Типы Периодизации

#### Linear Periodization (Линейная)

```
Неделя 1-4:  Гипертрофия  (4x12 @ 65%)
Неделя 5-8:  Сила         (4x6 @ 80%)
Неделя 9-12: Мощность     (5x3 @ 90%)
Неделя 13:   DELOAD       (3x8 @ 50%)
```

**Лучше для:** Новичков, простых целей, первые 6-12 месяцев тренировок

#### DUP -- Daily Undulating Periodization

```
Понедельник:  Сила       (5x5 @ 85%)
Среда:        Гипертрофия (4x10 @ 70%)
Пятница:      Мощность   (6x3 @ 80%)
```

**Лучше для:** Средних и продвинутых, одновременное развитие нескольких качеств

#### Block Periodization (Блочная)

```
Блок 1 (4 нед): Accumulation  (высокий объем, средняя интенсивность)
Блок 2 (4 нед): Transmutation (средний объем, высокая интенсивность)
Блок 3 (2 нед): Realization   (низкий объем, максимальная интенсивность)
Deload (1 нед): Recovery      (50% объема и интенсивности)
```

**Лучше для:** Продвинутых атлетов, подготовка к соревнованиям

### График Прогрессии

| Неделя | Упражнение | Sets x Reps | Вес (кг) | RPE | Заметки |
|--------|------------|-------------|----------|-----|---------|
| 1 | [Упражнение] | [SxR] | [кг] | [1-10] | Baseline |
| 2 | | [SxR] | [+кг] | | Volume up |
| 3 | | [SxR] | [+кг] | | Intensity up |
| 4 | | [SxR] | [+кг] | | Progressive |
| 5 | | DELOAD | [-30%] | <6 | Recovery |
| 6 | | [SxR] | [new baseline] | | Next cycle |

## Deload Protocol (Разгрузочная Неделя)

**Когда делать deload:**
- Каждые 4-8 недель (по плану)
- При RPE > 9 на 2+ тренировках подряд
- При ухудшении сна или настроения
- При отсутствии прогресса 2+ недели
- При повышенном resting HR (>10% от нормы)

**Как делать deload:**

| Метод | Объем | Интенсивность | Частота |
|-------|-------|---------------|---------|
| Вариант A | -40-50% | Сохранить | Сохранить |
| Вариант B | Сохранить | -30-40% | Сохранить |
| Вариант C | -30% | -20% | -1 сессия |

**Важно:** Deload -- это НЕ отдых. Это активное восстановление с уменьшенной нагрузкой.

## Протокол Преодоления Плато

**Если нет прогресса 2+ недели:**

1. **Проверить recovery:**
   - [ ] Сон 7-9 часов?
   - [ ] Protein 1.6-2.2 г/кг?
   - [ ] Stress management?
   - [ ] Калории достаточны? (нельзя набрать мышцы в дефиците)

2. **Изменить переменную:**
   - [ ] Deload 1 неделю, затем новый цикл
   - [ ] Сменить вариацию упражнения (flat bench -> incline bench)
   - [ ] Изменить rep range (если 5x5 не работает -> попробовать 4x8)
   - [ ] Добавить accessory work (слабое звено цепи)

3. **Если recovery в порядке, но плато остается:**
   - [ ] Сменить тип периодизации (linear -> DUP)
   - [ ] Micro-loading (0.5-1.25 кг пластины)
   - [ ] Волнообразная прогрессия (2 шага вперед, 1 назад)

## Заполнение из Workflow Plan

**Auto-population rules:**
- `project_name` -> из frontmatter workflow-plan.md
- Тренировочная цель -> из идеи проекта (Step 1)
- Timeline -> из calendar sync для определения длины мезоциклов
- Если SMART Goal completed -> Target performance pre-filled
- Если Recovery Protocol exists -> Deload timing aligned

## Научная База

### Ключевые исследования:
1. **Delorme (1945):** Первая формализация progressive resistance exercise
2. **Selye (1936):** General Adaptation Syndrome -- теоретическая основа
3. **Schoenfeld et al. (2017):** 10-20+ sets/muscle group/week для оптимальной гипертрофии (J Strength Cond Res)
4. **Rhea et al. (2003):** DUP превосходит linear periodization для experienced lifters (meta-analysis)
5. **Kraemer & Ratamess (2004):** Fundamentals of resistance training progression (Med Sci Sports Exerc)
6. **ACSM Position Stand (2009):** Evidence-based recommendations for resistance training progression

### RPE Scale (Rate of Perceived Exertion):

| RPE | Описание | Reps in Reserve (RIR) |
|-----|----------|----------------------|
| 10 | Максимальное усилие | 0 RIR |
| 9 | Очень тяжело, мог(ла) бы еще 1 rep | 1 RIR |
| 8 | Тяжело, мог(ла) бы еще 2-3 reps | 2-3 RIR |
| 7 | Умеренно тяжело | 3-4 RIR |
| 6 | Легко-умеренно | 4+ RIR |
| 5 | Легко | Много в запасе |

**Рекомендация:** Тренироваться при RPE 7-9 для прогресса. RPE 10 -- только для тестов 1RM.

## Частые Ошибки

1. **Слишком быстрая прогрессия** -- добавлять вес каждую тренировку без учета recovery
2. **Игнорирование deload** -- "deload -- для слабых" -> overtraining и травмы
3. **Только увеличение веса** -- забывать про volume, frequency, density
4. **Ego lifting** -- жертвовать техникой ради большего веса
5. **Отсутствие трекинга** -- без записей невозможно контролировать прогрессию
6. **Одна и та же программа > 12 недель** -- без смены стимула адаптация замедляется

## Метрики и Измерения

### Ключевые метрики:

| Метрика | Формула | Частота | Цель |
|---------|---------|---------|------|
| Total Volume | Sets x Reps x Weight | Каждая тренировка | Рост на 5-10% за мезоцикл |
| Estimated 1RM | Weight x (1 + 0.0333 x Reps) | Каждые 4 недели | Рост |
| RPE Trend | Средний RPE за неделю | Еженедельно | 7-8.5 (не выше 9 постоянно) |
| Adherence | Completed / Planned sessions | Еженедельно | > 85% |

### Трекинг в Таблице:

| Дата | Упражнение | Sets | Reps | Вес | Total Volume | RPE | Заметки |
|------|------------|------|------|-----|-------------|-----|---------|
| [Date] | [Name] | [S] | [R] | [W] | [S*R*W] | [RPE] | |

### Фитнес-трекер интеграция:
- **Garmin / Apple Watch:** HR зоны во время тренировки, recovery time advisor
- **WHOOP:** Strain score, recovery score, sleep performance
- **Strong / Hevy app:** автоматический трекинг объема и progression charts
- **Spreadsheet:** Google Sheets / Excel для детального анализа

## Синергии с Другими Фреймворками

### Progressive Overload + Recovery Protocols
- Overload создает стимул для адаптации
- Recovery обеспечивает суперкомпенсацию
- Deload Protocol ← Recovery "Load Management"
- Без recovery прогрессия невозможна (overtraining = regression)

### Progressive Overload + SMART Goals
- SMART дает конечную цель ("bench press 100 кг к 1 июня")
- Progressive Overload дает путь (+1-2.5 кг/неделю -> 12 недель -> 100 кг)

### Progressive Overload + Macros Tracking
- Training volume определяет calorie needs
- Protein 1.6-2.2 г/кг необходим для мышечной адаптации
- Calorie surplus для набора массы, поддержание для recomposition

### Progressive Overload + Habit Loop
- Habit Loop обеспечивает consistency (ходить в зал)
- Progressive Overload обеспечивает progression (что делать в зале)
- Habit Cue: "После работы -> переодеться" / Response: training session

## Память Claude Flow

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "health:progressive-overload:template-usage:{project_id}" \
  --content "Progressive Overload for {project_name}: Goal={goal}, Periodization={type}, Current 1RM={value}, Cycle={week}/of{total}"
```
