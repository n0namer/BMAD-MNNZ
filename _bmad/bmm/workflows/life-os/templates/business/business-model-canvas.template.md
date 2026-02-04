---
template: business-model-canvas
domain: business
tier: 2
framework: "Business Model Canvas (BMC)"
applicability: high
timeInvestment: moderate
complexity: medium
score: "21/25 (84%)"
synergies:
  - lean-canvas
  - value-proposition-canvas
  - porters-five-forces
  - okrs
  - value-stream-mapping
integration_points:
  - step-04-consilium.md
  - step-05-scoring.md
  - step-08-deep-plan.md
outputs:
  - business-model-canvas-analysis.md
  - "Append to workflow-plan.md"
scoring_contribution:
  provides_criteria: true
  provides_weights: true
  provides_scenarios: false
  mcda_dimensions:
    - "Revenue Potential"
    - "Customer Reach"
    - "Resource Efficiency"
    - "BMC Completeness"
deep_plan_contribution:
  generates_l2_headings: true
  generates_l3_tasks: true
  generates_milestones: true
linked_frameworks:
  - lean-canvas
  - value-proposition-canvas
  - swot
  - porters-five-forces
  - okrs
prerequisite_frameworks: []
follows_frameworks:
  - lean-canvas
research_notes: "84% effectiveness. Osterwalder's 9-block canvas for business model visualization."
---

# Business Model Canvas: {{project_name}}

> **Проект**: {{project_name}}
> **Домен**: Business & Career
> **Дата создания**: {{date}}
> **Аналитик**: {{user_name}}
> **Время на заполнение**: 60-90 минут

---

## Назначение

Business Model Canvas (BMC) -- визуальный фреймворк Александра Остервальдера для описания, анализа и дизайна бизнес-моделей через 9 взаимосвязанных блоков. Дает целостную картину бизнеса на одной странице.

**Когда применять:**
- Дизайн или переосмысление бизнес-модели
- Визуализация всех компонентов бизнеса
- Сравнение нескольких бизнес-моделей
- Переход от Lean Canvas к полной модели
- Ключевые слова: "бизнес-модель", "ценностное предложение", "клиенты", "партнеры", "доход"

---

## Интеграция с Life OS

### Step 4 -- Consilium
- Business Strategist валидирует каждый из 9 блоков
- Financial Analyst оценивает Cost Structure и Revenue Streams
- Innovation Expert (TRIZ) ищет противоречия между блоками
- Six Hats: White Hat проверяет факты в каждом блоке, Green Hat генерирует альтернативы

### Step 5 -- Scoring
- **BMC Completeness**: `score = (filled_blocks / 9) * 10`
- Каждый блок оценивается по качеству (0-10)
- Revenue Potential: Revenue Streams * Customer Segments reach
- Resource Efficiency: Value Created / Key Resources consumed
- Формула: `BMC_Score = (completeness * 0.3) + (revenue_potential * 0.4) + (resource_efficiency * 0.3)`

### Step 8 -- Deep Plan
- **L2 headings**: "Customer Acquisition", "Value Delivery", "Revenue Generation", "Cost Management"
- **L3 tasks**: конкретные действия из каждого из 9 блоков
- **Milestones**: каждый блок реализован -> контрольная точка

---

## Авто-заполнение

**Из workflow-plan.md:**
- `{{frontmatter.mission}}` -> Value Propositions (основа)
- `{{frontmatter.target_audience}}` -> Customer Segments

**Из Lean Canvas (если заполнен):**
- LC "Customer Segments" <-> BMC "Customer Segments"
- LC "Solution" -> BMC "Value Propositions"
- LC "Revenue Streams" <-> BMC "Revenue Streams"
- LC "Cost Structure" <-> BMC "Cost Structure"

**Из Porter's Five Forces (если заполнен):**
- "Bargaining Power of Suppliers" -> BMC "Key Partnerships" (стратегия ответа)
- "Competitive Rivalry" -> BMC "Value Propositions" (дифференциация)

---

## 9 Блоков Business Model Canvas

### 1. Customer Segments (Сегменты клиентов)

> Для кого мы создаем ценность? Кто наши ключевые клиенты?

| Сегмент | Описание | Размер | Потребности | Приоритет |
|---------|----------|--------|-----------|----------|
| [Сегмент 1] | [Демография, поведение] | [TAM/SAM] | [Что нужно] | [Primary / Secondary] |
| [Сегмент 2] | [Описание] | [Размер] | [Потребности] | [Приоритет] |
| [Сегмент 3] | [Описание] | [Размер] | [Потребности] | [Приоритет] |

**Тип рынка**: [ ] Mass Market [ ] Niche [ ] Segmented [ ] Diversified [ ] Multi-sided

---

### 2. Value Propositions (Ценностные предложения)

> Какую ценность мы доставляем? Какие проблемы решаем?

| Сегмент | Ценностное предложение | Тип ценности | Дифференциатор |
|---------|----------------------|-------------|---------------|
| [Сегмент 1] | [Что получает клиент] | [Newness / Performance / Customization / Design / Brand / Price / Cost Reduction / Risk Reduction / Accessibility / Convenience] | [Чем отличаемся] |
| [Сегмент 2] | [VP] | [Тип] | [Отличие] |

---

### 3. Channels (Каналы)

> Как мы достигаем и коммуницируем с клиентскими сегментами?

| Фаза | Канал | Тип | Статус |
|------|-------|-----|--------|
| **Awareness** (Узнаваемость) | [Как узнают о нас] | [Own / Partner] | [Active / Planned] |
| **Evaluation** (Оценка) | [Как оценивают предложение] | [Own / Partner] | [Статус] |
| **Purchase** (Покупка) | [Как покупают] | [Own / Partner] | [Статус] |
| **Delivery** (Доставка) | [Как доставляем ценность] | [Own / Partner] | [Статус] |
| **After-Sales** (Поддержка) | [Как поддерживаем] | [Own / Partner] | [Статус] |

---

### 4. Customer Relationships (Отношения с клиентами)

> Какие отношения строим и поддерживаем?

| Сегмент | Тип отношений | Цель | Стоимость |
|---------|--------------|------|----------|
| [Сегмент 1] | [Personal Assistance / Self-Service / Automated / Communities / Co-creation] | [Acquisition / Retention / Upselling] | [$/клиент/мес] |
| [Сегмент 2] | [Тип] | [Цель] | [Стоимость] |

---

### 5. Revenue Streams (Потоки дохода)

> За что платят клиенты? Как платят сейчас?

| Поток | Модель | Цена | % от общего дохода | Сегмент |
|-------|--------|------|-------------------|---------|
| [Поток 1] | [Asset Sale / Subscription / Licensing / Brokerage / Advertising] | [$/ед. или $/мес] | [%] | [Сегмент] |
| [Поток 2] | [Модель] | [Цена] | [%] | [Сегмент] |

**Ценообразование**: [ ] Fixed (List / Volume / Segment) [ ] Dynamic (Negotiation / Yield / Auction)

**Общий MRR target**: $[сумма/мес]
**Общий ARR target**: $[сумма/год]

---

### 6. Key Resources (Ключевые ресурсы)

> Какие ресурсы требуются для ценностных предложений?

| Ресурс | Тип | Владение | Критичность |
|--------|-----|----------|------------|
| [Ресурс 1] | [Physical / Intellectual / Human / Financial] | [Own / Lease / Partner] | [Critical / Important / Nice-to-have] |
| [Ресурс 2] | [Тип] | [Владение] | [Критичность] |
| [Ресурс 3] | [Тип] | [Владение] | [Критичность] |

---

### 7. Key Activities (Ключевые активности)

> Какие ключевые действия требует наша бизнес-модель?

| Активность | Категория | Частота | Ответственный |
|-----------|----------|---------|--------------|
| [Активность 1] | [Production / Problem Solving / Platform/Network] | [Daily / Weekly / Monthly] | [Роль] |
| [Активность 2] | [Категория] | [Частота] | [Роль] |
| [Активность 3] | [Категория] | [Частота] | [Роль] |

---

### 8. Key Partnerships (Ключевые партнерства)

> Кто наши ключевые партнеры и поставщики?

| Партнер | Тип партнерства | Что получаем | Что даем | Риск зависимости |
|---------|----------------|-------------|---------|-----------------|
| [Партнер 1] | [Strategic Alliance / Coopetition / Joint Venture / Supplier] | [Ресурс/услуга] | [Ценность] | [H/M/L] |
| [Партнер 2] | [Тип] | [Получаем] | [Даем] | [Риск] |

**Мотивация партнерств**: [ ] Optimization & Economy of Scale [ ] Reduction of Risk [ ] Acquisition of Resources

---

### 9. Cost Structure (Структура расходов)

> Какие основные расходы в нашей бизнес-модели?

| Категория | Тип | Ежемесячно | % от дохода | Привязка к блоку |
|-----------|-----|-----------|------------|-----------------|
| [Расход 1] | [Fixed / Variable] | $[сумма] | [%] | [Key Resources / Key Activities / Key Partnerships] |
| [Расход 2] | [Тип] | $[сумма] | [%] | [Блок] |
| [Расход 3] | [Тип] | $[сумма] | [%] | [Блок] |

**Характер модели**: [ ] Cost-Driven (минимизация расходов) [ ] Value-Driven (максимизация ценности)

**Economies of Scale**: [Да / Нет / Потенциально]
**Economies of Scope**: [Да / Нет / Потенциально]

**Total Monthly Burn**: $[сумма]
**Breakeven**: [Month X at Y customers]

---

## Scoring Impact (данные для Step 5)

```yaml
criteria_from_framework:
  - name: "BMC Completeness"
    weight: 0.10
    rationale: "Количество качественно заполненных блоков из 9"
    formula: "(filled_blocks / 9) * 10"
  - name: "Revenue Potential"
    weight: 0.15
    rationale: "Revenue Streams * Customer Segments reach"
  - name: "Resource Efficiency"
    weight: 0.10
    rationale: "Value Created / Key Resources consumed"
  - name: "Market Attractiveness"
    weight: 0.15
    rationale: "Customer Segments size * Value Proposition strength"
```

---

## Deep Plan Contribution (данные для Step 8)

**L2 Headings (из блоков BMC):**
- "Customer Acquisition" (Segments + Channels + Relationships)
- "Value Delivery" (Value Propositions + Key Activities + Key Resources)
- "Revenue Generation" (Revenue Streams + Pricing)
- "Cost Management" (Cost Structure + Key Partnerships)

**L3 Tasks (конкретные действия):**
- Из каждого блока извлекаются 2-3 ключевых действия
- Channels -> план маркетинга и продаж
- Key Activities -> операционный план
- Key Partnerships -> план переговоров и контрактов

**Milestones:**
- Customer Segment validated (interviews complete)
- Value Proposition tested (landing page / MVP)
- First Revenue Stream active
- Breakeven reached

---

## Синергии

| Фреймворк | Как усиливает BMC |
|-----------|------------------|
| **Lean Canvas** | Lean Canvas как "быстрый старт", затем BMC для полноты. Customer Segments синхронизируются |
| **VPC** | Customer Jobs из VPC -> BMC Customer Segments. Pain Relievers + Gain Creators -> BMC Value Propositions |
| **Porter's Five Forces** | Competitive Rivalry -> BMC дифференциация. Supplier Power -> BMC Key Partnerships стратегия |
| **SWOT** | Strengths -> Key Resources. Threats -> Risk для Revenue Streams |
| **OKRs** | Key Activities -> OKR Initiatives. Revenue targets -> OKR Key Results |

---

## Consistency Check (проверка согласованности)

| Проверка | Статус | Комментарий |
|----------|--------|------------|
| VP решает реальную проблему сегмента? | [ ] | |
| Channels достигают целевых сегментов? | [ ] | |
| Revenue Streams покрывают Cost Structure? | [ ] | |
| Key Resources достаточны для Key Activities? | [ ] | |
| Key Partnerships закрывают ресурсные gaps? | [ ] | |

---

## Memory Storage

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "bmad:frameworks:business:bmc:{{project_id}}" \
  --content "BMC for {{project_name}}: Segments=[count], VP=[summary], Revenue=[model], Completeness=[X/9], Breakeven=[month]"
```

---

## Решения (Decision Tracking)

1. **Решение**: [Что было решено на основе BMC]
   - **Обоснование**: [Почему, исходя из анализа блоков]
   - **Компромиссы**: [Чем пожертвовали]
   - **Уверенность**: [High / Medium / Low]

---

## Следующие шаги

- [ ] Заполнить все 9 блоков (начинать с Customer Segments и Value Propositions)
- [ ] Проверить согласованность блоков (Consistency Check)
- [ ] Рассчитать Breakeven point
- [ ] Синхронизировать с VPC (Customer Jobs -> Segments)
- [ ] Передать Key Activities в OKRs как Initiatives
- [ ] Использовать Porter's для анализа конкурентных блоков
- [ ] Передать данные в Step 5 (scoring) и Step 8 (deep plan)

---

**Framework Version**: 1.0
**Life OS Version**: 2.0
**Template Last Updated**: 2026-02-04
