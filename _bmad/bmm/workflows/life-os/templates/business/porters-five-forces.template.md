---
template: porters-five-forces
domain: business
tier: 3
framework: "Porter's Five Forces"
applicability: medium
timeInvestment: intensive
complexity: high
score: "19/25 (76%)"
synergies:
  - swot
  - business-model-canvas
  - ansoff-matrix
  - lean-canvas
integration_points:
  - step-04-consilium.md
  - step-05-scoring.md
  - step-08-deep-plan.md
outputs:
  - porters-five-forces-analysis.md
  - "Append to workflow-plan.md"
scoring_contribution:
  provides_criteria: true
  provides_weights: true
  provides_scenarios: false
  mcda_dimensions:
    - "Competitive Advantage Sustainability"
    - "Market Entry Risk"
    - "Industry Attractiveness"
deep_plan_contribution:
  generates_l2_headings: true
  generates_l3_tasks: true
  generates_milestones: false
linked_frameworks:
  - swot
  - business-model-canvas
  - ansoff-matrix
  - okrs
prerequisite_frameworks: []
follows_frameworks: []
research_notes: "76% effectiveness. Classic competitive analysis by Michael Porter."
---

# Porter's Five Forces: {{project_name}}

> **Проект**: {{project_name}}
> **Домен**: Business & Career
> **Дата создания**: {{date}}
> **Аналитик**: {{user_name}}
> **Время на заполнение**: 60-120 минут

---

## Назначение

Porter's Five Forces -- фреймворк Майкла Портера для анализа конкурентной структуры отрасли. Оценивает 5 сил, определяющих привлекательность рынка и потенциальную прибыльность. Помогает выбрать конкурентную стратегию.

**Когда применять:**
- Выход на новый рынок или в новую отрасль
- Оценка конкурентной позиции
- Стратегический анализ перед крупными инвестициями
- Ключевые слова: "конкуренция", "рынок", "отрасль", "барьеры входа", "поставщики", "заменители"

**Когда НЕ применять:**
- Стартап на ранней стадии (нет четкой отрасли)
- Некоммерческие/неконкурентные рынки
- Требуется быстрое решение (фреймворк требует исследования)

---

## Интеграция с Life OS

### Step 4 -- Consilium
- **Market Analyst** лидирует Five Forces анализ
- Business Strategist использует результаты для стратегических решений
- Financial Analyst оценивает финансовые импликации каждой силы
- Six Hats: White Hat (факты по каждой силе), Black Hat (наихудшие сценарии), Green Hat (стратегии ответа)

### Step 5 -- Scoring
- **Industry Attractiveness Score**: среднее по 5 силам (инверсия -- низкие силы = высокая привлекательность)
- **Market Entry Risk**: сумма сил, препятствующих входу
- **Competitive Advantage Sustainability**: устойчивость нашей позиции
- Формула: `Attractiveness = (5 - avg_force_strength) / 5 * 10`
- Highest weight -- наиболее значимая сила

### Step 8 -- Deep Plan
- **L2 headings**: "Build Entry Barriers", "Reduce Supplier Dependence", "Differentiate from Rivals"
- **L3 tasks**: оборонительные и наступательные стратегии

---

## Авто-заполнение

**Из SWOT (если заполнен):**
- SWOT "Threats" -> Threat of New Entrants + Competitive Rivalry
- SWOT "Strengths" -> основа для Defensive Strategies

**Из BMC (если заполнен):**
- BMC "Key Partnerships" -> Bargaining Power of Suppliers (контекст)
- BMC "Customer Segments" -> Bargaining Power of Buyers (контекст)
- BMC "Value Propositions" -> дифференциация от Substitutes

---

## Анализ 5 Сил

### 1. Threat of New Entrants (Угроза новых участников)

**Общий уровень угрозы**: [ ] High [ ] Medium [ ] Low

#### Барьеры входа

| Барьер | Оценка (1-10) | Комментарий |
|--------|-------------|------------|
| **Требования к капиталу** | [X] | [Сколько нужно для входа?] |
| **Экономия масштаба** | [X] | [Существующие игроки имеют cost advantage?] |
| **Лояльность бренду** | [X] | [Насколько сильны бренды в отрасли?] |
| **Регуляторные барьеры** | [X] | [Лицензии, сертификации, разрешения?] |
| **Доступ к дистрибуции** | [X] | [Каналы заблокированы существующими игроками?] |
| **Switching costs для клиентов** | [X] | [Дорого ли клиентам менять поставщика?] |
| **Технологические барьеры** | [X] | [Требуется ли уникальная технология?] |

**Средний балл барьеров**: [X/10]
**Итоговая оценка угрозы** (инверсия барьеров): [H/M/L]

**Анализ**: [Почему такой уровень угрозы? Какие барьеры слабые?]

---

### 2. Bargaining Power of Suppliers (Переговорная сила поставщиков)

**Общий уровень силы**: [ ] High [ ] Medium [ ] Low

#### Факторы

| Фактор | Оценка (1-10) | Комментарий |
|--------|-------------|------------|
| **Концентрация поставщиков** | [X] | [Мало поставщиков = высокая сила] |
| **Стоимость переключения** | [X] | [Дорого ли нам менять поставщика?] |
| **Наличие заменителей поставки** | [X] | [Есть ли альтернативные источники?] |
| **Угроза прямой интеграции** | [X] | [Может ли поставщик стать конкурентом?] |
| **Уникальность ресурса** | [X] | [Насколько уникален ресурс поставщика?] |

**Средний балл**: [X/10]

**Ключевые поставщики и зависимость:**

| Поставщик | Ресурс | Зависимость | Альтернативы |
|-----------|--------|------------|-------------|
| [Поставщик 1] | [Что поставляет] | [Critical/High/Medium/Low] | [Количество альтернатив] |
| [Поставщик 2] | [Ресурс] | [Зависимость] | [Альтернативы] |

**Анализ**: [Почему такой уровень силы? Какие зависимости критичны?]

---

### 3. Bargaining Power of Buyers (Переговорная сила покупателей)

**Общий уровень силы**: [ ] High [ ] Medium [ ] Low

#### Факторы

| Фактор | Оценка (1-10) | Комментарий |
|--------|-------------|------------|
| **Концентрация покупателей** | [X] | [Мало крупных покупателей = высокая сила] |
| **Стоимость переключения** | [X] | [Дорого ли покупателю уйти?] |
| **Ценовая чувствительность** | [X] | [Насколько важна цена?] |
| **Угроза обратной интеграции** | [X] | [Может ли покупатель производить сам?] |
| **Информированность покупателя** | [X] | [Знает ли о ценах/альтернативах?] |
| **Объем закупок** | [X] | [Покупатель покупает большие объемы?] |

**Средний балл**: [X/10]

**Ключевые сегменты покупателей:**

| Сегмент | Доля дохода (%) | Сила переговоров | Лояльность |
|---------|----------------|-----------------|-----------|
| [Сегмент 1] | [%] | [H/M/L] | [H/M/L] |
| [Сегмент 2] | [%] | [Сила] | [Лояльность] |

**Анализ**: [Почему такой уровень силы? Кто самый сильный покупатель?]

---

### 4. Threat of Substitute Products (Угроза заменителей)

**Общий уровень угрозы**: [ ] High [ ] Medium [ ] Low

#### Заменители

| # | Заменитель | Цена vs. наш продукт | Performance vs. наш | Switching Cost | Тренд |
|---|-----------|---------------------|---------------------|---------------|-------|
| 1 | [Заменитель 1] | [Cheaper/Same/More expensive] | [Better/Same/Worse] | [H/M/L] | [Growing/Stable/Declining] |
| 2 | [Заменитель 2] | [Цена] | [Performance] | [Cost] | [Тренд] |
| 3 | [Заменитель 3] | [Цена] | [Performance] | [Cost] | [Тренд] |

**Price-Performance Ratio анализ**: [Какой заменитель дает лучшее соотношение цена/качество?]

**Анализ**: [Почему такой уровень угрозы? Какие заменители растут?]

---

### 5. Competitive Rivalry (Конкурентное соперничество)

**Общий уровень интенсивности**: [ ] High [ ] Medium [ ] Low

#### Факторы

| Фактор | Оценка (1-10) | Комментарий |
|--------|-------------|------------|
| **Количество конкурентов** | [X] | [Много равных = высокое соперничество] |
| **Темп роста отрасли** | [X] | [Медленный рост = борьба за долю] |
| **Дифференциация продукта** | [X] | [Низкая дифференциация = ценовые войны] |
| **Барьеры выхода** | [X] | [Высокие = конкуренты остаются даже при убытках] |
| **Fixed costs / Value added** | [X] | [Высокие fixed = давление на объемы] |
| **Стратегическая важность** | [X] | [Отрасль критична для крупных игроков?] |

**Средний балл**: [X/10]

**Карта конкурентов:**

| Конкурент | Доля рынка | Стратегия | Сильные стороны | Слабые стороны |
|-----------|-----------|-----------|----------------|---------------|
| [Конкурент 1] | [%] | [Cost Leader / Differentiator / Niche] | [Сильные] | [Слабые] |
| [Конкурент 2] | [%] | [Стратегия] | [Сильные] | [Слабые] |
| [Конкурент 3] | [%] | [Стратегия] | [Сильные] | [Слабые] |
| **Наша позиция** | [%] | [Стратегия] | [Сильные] | [Слабые] |

**Анализ**: [Почему такой уровень соперничества?]

---

## Industry Attractiveness Score (Оценка привлекательности отрасли)

| Сила | Уровень (1-5) | Вес | Weighted |
|------|-------------|-----|---------|
| Threat of New Entrants | [1=low, 5=high] | 0.20 | [X] |
| Bargaining Power of Suppliers | [1-5] | 0.20 | [X] |
| Bargaining Power of Buyers | [1-5] | 0.20 | [X] |
| Threat of Substitutes | [1-5] | 0.20 | [X] |
| Competitive Rivalry | [1-5] | 0.20 | [X] |
| **Total Force Score** | | **1.00** | **[Sum]** |

**Industry Attractiveness** = (5 - Total_Force_Score) / 5 * 10 = **[X/10]**

| Score | Interpretation |
|-------|---------------|
| 8-10 | Highly attractive -- strong profit potential |
| 5-7 | Moderately attractive -- selective entry |
| 2-4 | Low attractiveness -- avoid or niche strategy |
| 0-1 | Unattractive -- do not enter |

**Наиболее значимая сила**: [Какая из 5 оказывает наибольшее влияние?]

---

## Стратегические импликации

### Defensive Strategies (Оборонительные)

| # | Стратегия | Против какой силы | Приоритет | Ресурсы |
|---|-----------|------------------|----------|---------|
| D1 | [Стратегия защиты 1] | [Force X] | [H/M/L] | [Что нужно] |
| D2 | [Стратегия защиты 2] | [Force Y] | [H/M/L] | [Что нужно] |
| D3 | [Стратегия защиты 3] | [Force Z] | [H/M/L] | [Что нужно] |

### Offensive Opportunities (Наступательные)

| # | Возможность | Эксплуатация слабой силы | Приоритет | Ресурсы |
|---|-----------|------------------------|----------|---------|
| O1 | [Как использовать слабую силу 1] | [Weak Force X] | [H/M/L] | [Что нужно] |
| O2 | [Как использовать слабую силу 2] | [Weak Force Y] | [H/M/L] | [Что нужно] |

### Recommended Competitive Strategy (Porter's Generic)

> [ ] **Cost Leadership** -- быть самым дешевым
> [ ] **Differentiation** -- быть уникальным (Value > Price)
> [ ] **Focus (Cost)** -- дешевле в нише
> [ ] **Focus (Differentiation)** -- уникальный в нише

**Обоснование выбора**: [Почему эта стратегия, исходя из 5 сил?]

---

## Scoring Impact (данные для Step 5)

```yaml
criteria_from_framework:
  - name: "Industry Attractiveness"
    weight: 0.15
    rationale: "Общий балл привлекательности отрасли"
    formula: "(5 - avg_force) / 5 * 10"
  - name: "Competitive Advantage Sustainability"
    weight: 0.15
    rationale: "Наша дифференциация vs. Competitive Rivalry + Substitutes"
  - name: "Market Entry Risk"
    weight: 0.10
    rationale: "Сумма сил, препятствующих успешному входу"
```

---

## Deep Plan Contribution (данные для Step 8)

**L2 Headings:**
- "Build Entry Barriers" (если мы уже на рынке -- защита позиции)
- "Reduce Supplier Dependence" (диверсификация поставщиков)
- "Differentiate from Rivals" (укрепление конкурентного преимущества)
- "Counter Substitutes" (снижение угрозы заменителей)

**L3 Tasks:**
- Defensive strategies -> конкретные действия с дедлайнами
- Offensive opportunities -> план захвата
- Competitive monitoring -> регулярный мониторинг конкурентов

---

## Синергии

| Фреймворк | Как усиливает Five Forces |
|-----------|--------------------------|
| **SWOT** | Threats <- Five Forces (New Entrants + Rivalry). Strengths -> Defensive Strategies |
| **BMC** | Key Partnerships <- Supplier Power response. Customer Relationships <- Buyer Power mitigation |
| **Lean Canvas** | UVP <- Differentiation from Rivals. Unfair Advantage <- Entry Barriers we build |
| **OKRs** | Defensive Strategies -> OKR Objectives. Market share targets -> Key Results |
| **TRIZ** | Contradictions in forces -> TRIZ inventive principles for resolution |

---

## Memory Storage

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "bmad:frameworks:business:porters:{{project_id}}" \
  --content "Porter's Five Forces for {{project_name}}: Attractiveness=[X/10], Dominant force=[force], Strategy=[cost/diff/focus], Top threat=[threat], Competitors=[count]"
```

---

## Решения (Decision Tracking)

1. **Решение**: [Что было решено на основе Five Forces]
   - **Обоснование**: [Почему, исходя из анализа 5 сил]
   - **Компромиссы**: [Чем пожертвовали]
   - **Уверенность**: [High / Medium / Low]

---

## Следующие шаги

- [ ] Собрать данные по каждой из 5 сил (минимум 3 фактора на силу)
- [ ] Оценить Industry Attractiveness Score
- [ ] Определить наиболее значимую силу
- [ ] Разработать Defensive и Offensive стратегии
- [ ] Выбрать конкурентную стратегию (Cost/Differentiation/Focus)
- [ ] Передать Threats в SWOT для расширенного анализа
- [ ] Передать стратегии в OKRs как Objectives/Initiatives
- [ ] Передать данные в Step 5 (scoring) и Step 8 (deep plan)

---

**Framework Version**: 1.0
**Life OS Version**: 2.0
**Template Last Updated**: 2026-02-04
