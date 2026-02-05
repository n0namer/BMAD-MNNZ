---
template: lean-canvas
domain: business
tier: 1
framework: "Lean Canvas"
applicability: high
timeInvestment: moderate
complexity: low
score: "22/25 (88%)"
synergies:
  - value-proposition-canvas
  - okrs
  - business-model-canvas
  - design-thinking
  - triz
integration_points:
  - step-04-consilium.md
  - step-05-scoring.md
  - step-08-deep-plan.md
outputs:
  - lean-canvas-analysis.md
  - "Append to workflow-plan.md"
scoring_contribution:
  provides_criteria: true
  provides_weights: true
  provides_scenarios: false
  mcda_dimensions:
    - "Problem-Solution Fit"
    - "UVP Clarity"
    - "Cost Efficiency"
deep_plan_contribution:
  generates_l2_headings: true
  generates_l3_tasks: true
  generates_milestones: true
linked_frameworks:
  - value-proposition-canvas
  - business-model-canvas
  - okrs
  - jobs-to-be-done
prerequisite_frameworks: []
follows_frameworks: []
research_notes: "88% effectiveness. Ash Maurya's 1-page business model for lean startups."
tracking:
  enabled: true
  category: business
  auto_complete_threshold: 0.95
  usage_count: 0
  last_used: null
---

# Lean Canvas: {{project_name}}

> **Проект**: {{project_name}}
> **Домен**: Business & Career
> **Дата создания**: {{date}}
> **Аналитик**: {{user_name}}
> **Время на заполнение**: 30-60 минут

---

## Назначение

Lean Canvas -- одностраничная модель бизнеса по методологии Ash Maurya. Фокусируется на проблемах клиентов и решениях, а не на инфраструктуре. Идеален для быстрой валидации идей, стартапов и новых продуктов.

**Когда применять:**
- Валидация новой бизнес-идеи или стартапа
- Быстрый pivot -- нужно переосмыслить модель за 30 минут
- Первая итерация бизнес-модели перед глубоким BMC
- Ключевые слова: "стартап", "MVP", "валидация", "проблема", "решение", "клиент"

---

## Интеграция с Life OS

### Step 4 -- Consilium
- Consilium валидирует КАЖДЫЙ из 9 блоков Lean Canvas
- Business Strategist проверяет Problem-Solution Fit
- Financial Analyst оценивает Revenue Streams и Cost Structure
- Innovation Expert (TRIZ) ищет противоречия между Problem и Solution
- Six Hats: Green Hat для генерации Unfair Advantage, Black Hat для проверки рисков

### Step 5 -- Scoring
- Каждый блок получает оценку заполненности и качества (0-10)
- **Problem-Solution Fit**: насколько Solution решает Problem
- **UVP Clarity**: ясность и убедительность ценностного предложения
- **Cost Efficiency**: соотношение CAC к LTV
- Формула: `LC_Score = avg(block_scores) * problem_solution_fit_weight`

### Step 8 -- Deep Plan
- **L2 headings**: "MVP Development", "Customer Discovery", "Channel Testing"
- **L3 tasks**: эксперименты валидации по каждому блоку
- **Milestones**: Problem validated, Solution validated, Channel tested

---

## Авто-заполнение

**Из workflow-plan.md:**
- `{{frontmatter.mission}}` -> основа для Unique Value Proposition
- `{{frontmatter.target_audience}}` -> Customer Segments
- `{{frontmatter.project_type}}` -> определяет релевантность блоков

**Из VPC template (если заполнен):**
- VPC "Pains" -> Lean Canvas "Problem"
- VPC "Gain Creators" -> Lean Canvas "Solution"
- VPC "Customer Jobs" -> Lean Canvas "Customer Segments"

---

## 9 Блоков Lean Canvas

### 1. Problem (Проблема) -- Top 3

**Главные проблемы целевой аудитории:**

1. **Проблема 1**: [Описание]
   - Насколько болезненна (1-10): [оценка]
   - Как часто возникает: [ежедневно / еженедельно / периодически]

2. **Проблема 2**: [Описание]
   - Насколько болезненна (1-10): [оценка]
   - Как часто возникает: [частота]

3. **Проблема 3**: [Описание]
   - Насколько болезненна (1-10): [оценка]
   - Как часто возникает: [частота]

**Существующие альтернативы**: [Как клиенты решают эти проблемы СЕЙЧАС?]

---

### 2. Customer Segments (Сегменты клиентов)

- **Early Adopters**: [Кто попробует первым? Характеристики, мотивация]
- **Целевой сегмент**: [Идеальный клиент -- демография, поведение, потребности]
- **Размер рынка (TAM/SAM/SOM)**:
  - TAM: [общий размер рынка]
  - SAM: [доступный сегмент]
  - SOM: [реально достижимая доля]

---

### 3. Unique Value Proposition (Уникальное ценностное предложение)

> [Одно четкое, убедительное предложение -- Почему вы ОТЛИЧАЕТЕСЬ и СТОИТЕ покупки?]

**High-Level Concept**: [Аналогия "X для Y" -- например, "Uber для доставки еды"]

**Проверка UVP:**
- [ ] Понятно за 8 секунд?
- [ ] Отличается от конкурентов?
- [ ] Решает главную проблему?
- [ ] Обещает конкретную выгоду?

---

### 4. Solution (Решение) -- Top 3

| # | Решение | Какую проблему решает | MVP-версия |
|---|---------|----------------------|-----------|
| 1 | [Решение 1] | Проблема 1 | [Минимальная версия] |
| 2 | [Решение 2] | Проблема 2 | [Минимальная версия] |
| 3 | [Решение 3] | Проблема 3 | [Минимальная версия] |

---

### 5. Channels (Каналы)

**Путь к клиентам:**

| Тип | Канал | Стоимость | Эффективность (est.) |
|-----|-------|-----------|---------------------|
| **Inbound** | [Как клиенты находят вас] | [$/мес] | [H/M/L] |
| **Outbound** | [Как вы находите клиентов] | [$/мес] | [H/M/L] |
| **Viral** | [Как клиенты приводят клиентов] | [$/мес] | [H/M/L] |

---

### 6. Revenue Streams (Потоки дохода)

- **Модель монетизации**: [Подписка / Транзакция / Реклама / Лицензия / Freemium]
- **Ценообразование**: [$/единица или $/мес]
- **Lifetime Value (LTV)**: [Ожидаемая сумма за весь срок клиента]
- **Monthly Recurring Revenue (MRR) target**: [$/мес к Month 12]

---

### 7. Cost Structure (Структура расходов)

| Категория | Ежемесячно | Единоразово | Примечания |
|-----------|-----------|------------|-----------|
| **Customer Acquisition Cost (CAC)** | $[сумма] | -- | [Как рассчитано] |
| **Дистрибуция** | $[сумма] | -- | |
| **Хостинг / Инфраструктура** | $[сумма] | $[сумма] | |
| **Люди (зарплаты)** | $[сумма] | -- | |
| **Маркетинг** | $[сумма] | -- | |
| **Прочее** | $[сумма] | $[сумма] | |
| **ИТОГО** | $[сумма/мес] | $[сумма] | |

**LTV:CAC Ratio**: [LTV / CAC] (цель: >3:1)

---

### 8. Key Metrics (Ключевые метрики)

**Pirate Metrics (AARRR):**

| Метрика | Определение | Целевое значение | Текущее |
|---------|------------|------------------|---------|
| **Acquisition** | [Как привлекаем] | [target] | [current] |
| **Activation** | [Первый "aha!" момент] | [target] | [current] |
| **Retention** | [Возвращение клиентов] | [target] | [current] |
| **Revenue** | [Монетизация] | [target] | [current] |
| **Referral** | [Рекомендации] | [target] | [current] |

---

### 9. Unfair Advantage (Нечестное преимущество)

> [Что НЕ МОЖЕТ быть легко скопировано или куплено конкурентами?]

**Проверка:**
- [ ] Инсайдерская информация / экспертиза?
- [ ] Сетевой эффект?
- [ ] Патенты / IP?
- [ ] Уникальная команда?
- [ ] Organic audience / community?
- [ ] Эксклюзивные партнерства?

Если "ничего" -- это нормально на старте. Unfair Advantage строится со временем.

---

## Scoring Impact (данные для Step 5)

```yaml
criteria_from_framework:
  - name: "Problem-Solution Fit"
    weight: 0.20
    rationale: "Насколько Solution реально решает Problem (по оценке consilium)"
  - name: "UVP Clarity"
    weight: 0.15
    rationale: "Ясность ценностного предложения -- понятно за 8 секунд"
  - name: "Cost Efficiency (LTV:CAC)"
    weight: 0.15
    rationale: "Финансовая жизнеспособность модели"
```

---

## Deep Plan Contribution (данные для Step 8)

**L2 Headings:**
- "MVP Development" (из блоков Solution + Key Metrics)
- "Customer Discovery" (из блоков Problem + Customer Segments)
- "Channel Testing" (из блока Channels)
- "Revenue Validation" (из блоков Revenue Streams + Cost Structure)

**L3 Tasks:**
- Эксперименты валидации для каждого блока
- Customer interviews (минимум 10)
- Landing page test для UVP
- Pricing experiments

**Milestones:**
- Problem validated (10+ customer interviews confirm pain)
- Solution MVP launched
- First paying customer
- LTV:CAC > 3:1 confirmed

---

## Синергии

| Фреймворк | Как усиливает Lean Canvas |
|-----------|--------------------------|
| **VPC** | Pains -> Problem, Gain Creators -> Solution. **Auto-link**: заполнить VPC после LC |
| **BMC** | Lean Canvas как "быстрый старт" перед полным BMC. Customer Segments синхронизируются |
| **TRIZ** | Применять TRIZ для инноваций в Solution -- разрешение противоречий Problem vs. Constraints |
| **OKRs** | Key Metrics из LC -> Key Results в OKR |
| **Design Thinking** | Empathize -> Problem, Ideate -> Solution, Test -> Key Metrics |

**Примечание по TRIZ**: Если Problem содержит противоречие (хочу X, но мешает Y), используйте TRIZ Quick Analysis для нахождения инвенторского решения.

---

## Memory Storage

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "bmad:frameworks:business:lean-canvas:{{project_id}}" \
  --content "Lean Canvas for {{project_name}}: Problem=[top problem], UVP=[value prop], Revenue=[model], LTV:CAC=[ratio]"
```

---

## Решения (Decision Tracking)

1. **Решение**: [Что было решено на основе Lean Canvas]
   - **Обоснование**: [Почему, исходя из данных блоков]
   - **Компромиссы**: [Чем пожертвовали]
   - **Уверенность**: [High / Medium / Low]

---

## Следующие шаги

- [ ] Заполнить все 9 блоков (начинать с Problem и Customer Segments)
- [ ] Проверить UVP -- понятно за 8 секунд?
- [ ] Рассчитать LTV:CAC ratio
- [ ] Определить Unfair Advantage (или план его создания)
- [ ] Передать данные в VPC template для углубленного анализа
- [ ] Передать Key Metrics в OKRs как Key Results
- [ ] Передать данные в Step 5 (scoring) и Step 8 (deep plan)

---

**Framework Version**: 1.0
**Life OS Version**: 2.0
**Template Last Updated**: 2026-02-04
