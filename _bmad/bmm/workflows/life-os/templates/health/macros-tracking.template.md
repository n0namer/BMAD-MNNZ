---
template: macros-tracking
domain: health
tier: 2
framework: Macronutrient Tracking
applicability: medium
timeInvestment: moderate
complexity: medium
synergies:
  - progressive-overload
  - recovery-protocols
  - smart-goals
integration_points:
  - step-01-collect-ideas.md
  - step-04-consilium.md
  - step-05-scoring.md
  - step-08-deep-plan.md
outputs:
  - macros-tracking-analysis.md
  - Append to workflow-plan.md
scoring_contribution:
  step_05_criteria:
    - name: health_readiness
      weight: 0.15
    - name: sustainability
      weight: 0.10
    - name: nutritional_adherence
      weight: 0.10
deep_plan_contribution:
  generates_l2: true
  l2_pattern: "Phase-based: Calculate TDEE -> Set Targets -> Track -> Adjust"
  generates_l3: true
---

# Macronutrient Tracking: {Project Name}

**Domain:** Health & Fitness (Nutrition-Specific)
**Generated:** {date}
**Analyst:** {user_name}
**Tier:** 2 (Nutrition-Specific)

## Цель Фреймворка

Macronutrient Tracking -- доказательный подход к питанию, основанный на учете трех макронутриентов: белков, жиров и углеводов. Вместо подсчета "только калорий" или следования жестким диетам, macros tracking обеспечивает гибкий контроль состава тела через управление энергетическим балансом и соотношением нутриентов. Подход "If It Fits Your Macros" (IIFYM) позволяет включать любые продукты при соблюдении дневных целей.

**Ключевой принцип:** Калорийный баланс определяет вес тела. Соотношение макронутриентов определяет состав тела (мышцы vs. жир).

## Когда Использовать

**Триггеры:**
- Keywords: питание, калории, белок, диета, набор массы, сушка, макросы
- Keywords (EN): nutrition, calories, protein, diet, bulk, cut, macros, TDEE, meal plan

**Идеально для:**
- Целенаправленное изменение состава тела (похудение, набор мышц)
- Оптимизация спортивного питания
- Контроль при медицинских рекомендациях (диабет, PCOS)
- Понимание своего питания на количественном уровне

**НЕ использовать для:**
- Лица с расстройствами пищевого поведения (анорексия, булимия, BED) -- трекинг может усугубить
- Склонность к obsessive behavior вокруг еды -- рассмотреть intuitive eating
- Начинающие, которым достаточно простых изменений (больше овощей, меньше junk food)

> **WARNING:** Если у вас история расстройств пищевого поведения или трекинг вызывает
> тревогу/навязчивость, прекратите использование и обратитесь к специалисту.

## Интеграция с Life OS

### Step 1 (Collect Ideas)
- Определить цель питания (cut/bulk/maintenance/recomposition)
- Зафиксировать текущие пищевые привычки

### Step 4 (Consilium)
- Nutritionist specialist рассчитывает TDEE и макро-цели
- Sports Dietitian адаптирует под тип тренировок

### Step 5 (Scoring)
- Nutritional Adherence -> оценка способности следовать плану
- Energy Balance -> правильность калорийного баланса

### Step 8 (Deep Plan)
- L2: фазы Calculate, Setup, Track, Adjust
- L3: еженедельное планирование меню, grocery list
- L5: ежедневный трекинг питания

## Структура Фреймворка

### Физические Данные

| Параметр | Значение | Единица |
|----------|----------|---------|
| Вес | ___ | кг |
| Рост | ___ | см |
| Возраст | ___ | лет |
| Пол | M / F | |
| Activity Level | ___ | см. таблицу ниже |
| Цель | Cut / Bulk / Maintenance / Recomp | |

### Шаг 1: Расчет BMR (Basal Metabolic Rate)

**Формула Mifflin-St Jeor** (наиболее точная, 2005 ADA Position Paper):

```
Мужчины: BMR = (10 x вес_кг) + (6.25 x рост_см) - (5 x возраст) + 5
Женщины: BMR = (10 x вес_кг) + (6.25 x рост_см) - (5 x возраст) - 161
```

**Мой BMR:** ___ ккал/день

### Шаг 2: Расчет TDEE (Total Daily Energy Expenditure)

**TDEE = BMR x Activity Multiplier**

| Уровень активности | Множитель | Описание |
|---------------------|-----------|----------|
| Sedentary | 1.2 | Офисная работа, без тренировок |
| Lightly Active | 1.375 | Легкие тренировки 1-3 раза/нед |
| Moderately Active | 1.55 | Тренировки 3-5 раз/нед |
| Very Active | 1.725 | Тяжелые тренировки 6-7 раз/нед |
| Extremely Active | 1.9 | Физ. работа + тяжелые тренировки |

**Мой Activity Multiplier:** ___
**Мой TDEE:** ___ ккал/день

### Шаг 3: Калорийная Цель

| Цель | Калории | Темп изменения |
|------|---------|----------------|
| **Aggressive Cut** | TDEE - 750 (30% deficit) | ~0.7 кг/нед (риск потери мышц) |
| **Moderate Cut** | TDEE - 500 (20% deficit) | ~0.5 кг/нед (рекомендуется) |
| **Mild Cut** | TDEE - 250 (10% deficit) | ~0.25 кг/нед (для уже худых) |
| **Maintenance** | TDEE | 0 кг/нед |
| **Lean Bulk** | TDEE + 250 | ~0.25 кг/нед (минимизация жира) |
| **Standard Bulk** | TDEE + 500 | ~0.5 кг/нед |

**Моя калорийная цель:** ___ ккал/день

### Шаг 4: Макро-Цели

#### Protein / Белок

**Рекомендации по исследованиям:**

| Цель | г/кг веса тела | Источник |
|------|----------------|----------|
| Минимум для здоровья | 0.8 г/кг | WHO/RDA |
| Сохранение мышц при cut | 1.6-2.2 г/кг | Helms et al. 2014 |
| Набор мышечной массы | 1.6-2.2 г/кг | Schoenfeld & Aragon 2018 |
| Атлеты с высоким объемом | 2.2-2.7 г/кг | ISSN Position Stand 2017 |

**Мой protein target:** ___ г/день = ___ ккал (x4 ккал/г)

#### Fats / Жиры

**Рекомендации:**
- Минимум: 0.8 г/кг (гормональное здоровье)
- Оптимум: 1.0-1.2 г/кг
- Общий % от калорий: 20-35%

**Мой fat target:** ___ г/день = ___ ккал (x9 ккал/г)

#### Carbs / Углеводы

**Расчет: Оставшиеся калории после белка и жиров**

```
Carb calories = Total calories - Protein calories - Fat calories
Carb grams = Carb calories / 4
```

**Мой carb target:** ___ г/день = ___ ккал (x4 ккал/г)

### Итоговая Таблица Макросов

| Макронутриент | Граммы | Калории | % от суточных |
|---------------|--------|---------|---------------|
| Protein | ___ г | ___ ккал | ___% |
| Fats | ___ г | ___ ккал | ___% |
| Carbs | ___ г | ___ ккал | ___% |
| **ИТОГО** | | **___ ккал** | 100% |

### Шаблон Приема Пищи

| Прием | Время | Protein (г) | Fats (г) | Carbs (г) | Ккал | Продукты |
|-------|-------|-------------|----------|-----------|------|----------|
| Завтрак | [HH:MM] | ___ | ___ | ___ | ___ | [Примеры] |
| Перекус 1 | [HH:MM] | ___ | ___ | ___ | ___ | |
| Обед | [HH:MM] | ___ | ___ | ___ | ___ | |
| Перекус 2 | [HH:MM] | ___ | ___ | ___ | ___ | |
| Ужин | [HH:MM] | ___ | ___ | ___ | ___ | |
| **Итого** | | ___ | ___ | ___ | ___ | |

## Flexible vs. Rigid Dieting

### Flexible Dieting (IIFYM) -- РЕКОМЕНДУЕТСЯ

**Принцип:** Любые продукты допустимы, если дневные макро-цели соблюдены.

| Аспект | Описание |
|--------|----------|
| Правило 80/20 | 80% калорий из цельных продуктов, 20% -- свободный выбор |
| Нет "запрещенных" продуктов | Снижает binge eating и чувство вины |
| Социальная гибкость | Можно есть в ресторанах, на вечеринках |
| Adherence | Выше долгосрочная приверженность (Stewart et al. 2002) |

### Rigid Dieting -- ИЗБЕГАТЬ ДЛЯ БОЛЬШИНСТВА

| Аспект | Описание |
|--------|----------|
| "Чистое питание" | Только "правильные" продукты, остальное запрещено |
| All-or-nothing | Один срыв -> "день испорчен" -> переедание |
| Social isolation | Трудно есть с другими |
| Adherence | Ниже долгосрочная приверженность |

**Исследование:** Smith et al. (1999) -- rigid dieting associated with higher BMI, mood disturbance, and disinhibited eating.

## Протокол Корректировки

**Каждые 2-4 недели оценивать прогресс:**

```
Прогресс соответствует ожиданиям?
  |
  +-- ДА --> Продолжить без изменений
  |
  +-- НЕТ, вес не снижается (при cut) -->
  |     Снизить калории на 5-10% (в основном за счет carbs)
  |     ИЛИ увеличить activity (NEAT: больше шагов, бытовая активность)
  |
  +-- НЕТ, вес не растет (при bulk) -->
  |     Увеличить калории на 5-10% (в основном carbs)
  |
  +-- НЕТ, теряю мышцы (при cut) -->
        Увеличить protein до 2.2-2.7 г/кг
        Снизить deficit (менее агрессивный cut)
        Убедиться в наличии силовых тренировок
```

**Признаки метаболической адаптации (при длительном cut):**
- Снижение energy levels
- Повышенный голод
- Остановка прогресса при корректном дефиците
- Решение: diet break 1-2 недели на maintenance calories, затем продолжить

## Заполнение из Workflow Plan

**Auto-population rules:**
- Body metrics -> из начальной оценки (Step 1)
- Цель (cut/bulk) -> из SMART Goal template
- Training schedule -> из Progressive Overload template (для расчета activity level)
- Protein needs -> синхронизация с Recovery Protocols

## Научная База

### Ключевые исследования:
1. **Mifflin-St Jeor (1990):** Наиболее точная формула BMR (ADA Position Paper 2005)
2. **Helms et al. (2014):** 1.6-2.2 г/кг protein для сохранения мышц при дефиците (JISSN)
3. **Schoenfeld & Aragon (2018):** Protein distribution 0.4-0.55 г/кг per meal, 4+ meals (JISSN)
4. **ISSN Position Stand (2017):** Evidence-based recommendations for sports nutrition
5. **Stewart et al. (2002):** Flexible vs. rigid dieting -- flexible associated with lower BMI
6. **Hall et al. (2015):** Metabolic adaptation to caloric restriction -- TDEE снижается при длительном дефиците

### Точность макро-трекинга:
- FDA допускает +/-20% погрешность на этикетках
- Домашнее приготовление точнее ресторанной еды на 30-50%
- Рекомендация: взвешивать ключевые продукты (protein sources) первые 2-4 недели

## Частые Ошибки

1. **Слишком агрессивный дефицит** -- >30% deficit = потеря мышц, crash diets = rebound
2. **Недостаток белка** -- без 1.6+ г/кг мышцы теряются даже при тренировках
3. **Игнорирование жиров** -- <0.8 г/кг = гормональные нарушения (testosterone, estrogen)
4. **Obsessive tracking** -- если трекинг вызывает тревогу, перейти на intuitive eating
5. **Не корректировать TDEE** -- при изменении веса TDEE меняется, пересчитывать каждые 4-6 недель
6. **Weekend binge** -- 5 дней дефицита, 2 дня surplus = нулевой прогресс

## Метрики и Измерения

### Ежедневный Лог

| Дата | Вес (утро) | Protein | Fats | Carbs | Ккал | Adherence | Заметки |
|------|------------|---------|------|-------|------|-----------|---------|
| [Date] | ___ кг | ___ г | ___ г | ___ г | ___ | Y/N | [Самочувствие] |

### Еженедельный Обзор

| Неделя | Ср. вес | Изменение | Ср. ккал | Ср. protein | Adherence % | Заметки |
|--------|---------|-----------|----------|-------------|-------------|---------|
| 1 | ___ | baseline | ___ | ___ | ___% | |
| 2 | ___ | ±___кг | ___ | ___ | ___% | |

### Инструменты:
- **MyFitnessPal** -- крупнейшая база продуктов, barcode scanner
- **Cronometer** -- более точный для микронутриентов
- **MacroFactor** -- AI-адаптивный TDEE, рекомендации корректировок
- **Кухонные весы** -- необходимы для точности (первые 2-4 недели минимум)

## Синергии с Другими Фреймворками

### Macros + Progressive Overload
- Training volume определяет calorie needs
- Protein timing вокруг тренировок (pre/post workout)
- Surplus для набора массы, deficit для cut + strength training

### Macros + Recovery Protocols
- Protein 1.6-2.2 г/кг -> мышечное восстановление
- Hydration (30-40 мл/кг) -> часть recovery
- Anti-inflammatory foods -> nutrition component of recovery

### Macros + SMART Goals
- SMART target (80 кг к маю) -> определяет calorie target
- Weekly weight targets -> checkpoint для adherence
- Measurable: body weight, body fat %, waist circumference

### Macros + Habit Loop
- Meal prep as Sunday habit (Cue: Sunday morning -> Response: prep 5 meals)
- Daily logging habit (Cue: after each meal -> Response: log in app)
- Water intake habit (Cue: every hour alarm -> Response: drink 250 мл)

## Память Claude Flow

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "health:macros-tracking:template-usage:{project_id}" \
  --content "Macros for {project_name}: Goal={cut/bulk/maint}, TDEE={value}kcal, Targets=P{protein}g/F{fats}g/C{carbs}g, Adherence={rate}%"
```
