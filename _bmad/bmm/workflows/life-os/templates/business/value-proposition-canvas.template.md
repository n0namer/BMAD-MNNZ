---
template: value-proposition-canvas
domain: business
tier: 2
framework: "Value Proposition Canvas (VPC)"
applicability: high
timeInvestment: moderate
complexity: medium
score: "21/25 (84%)"
synergies:
  - lean-canvas
  - business-model-canvas
  - jobs-to-be-done
  - design-thinking
integration_points:
  - step-01-collect-ideas.md
  - step-04-consilium.md
  - step-05-scoring.md
  - step-08-deep-plan.md
outputs:
  - value-proposition-canvas-analysis.md
  - "Append to workflow-plan.md"
scoring_contribution:
  provides_criteria: true
  provides_weights: true
  provides_scenarios: false
  mcda_dimensions:
    - "Pain-Relief Effectiveness"
    - "Gain Creation Strength"
    - "Customer Job Alignment"
deep_plan_contribution:
  generates_l2_headings: true
  generates_l3_tasks: true
  generates_milestones: true
linked_frameworks:
  - lean-canvas
  - business-model-canvas
  - design-thinking
  - jobs-to-be-done
prerequisite_frameworks: []
follows_frameworks: []
research_notes: "84% effectiveness. Companion to Business Model Canvas. Osterwalder & Pigneur."
---

# Value Proposition Canvas: {{project_name}}

> **Проект**: {{project_name}}
> **Домен**: Business & Career
> **Дата создания**: {{date}}
> **Аналитик**: {{user_name}}
> **Время на заполнение**: 45-60 минут

---

## Назначение

Value Proposition Canvas (VPC) -- инструмент глубокого анализа соответствия ценностного предложения потребностям клиента. Состоит из двух частей: Customer Profile (профиль клиента) и Value Map (карта ценности). Цель -- достичь Product-Market Fit.

**Когда применять:**
- Разработка нового продукта или сервиса
- Улучшение существующего ценностного предложения
- Анализ Product-Market Fit
- Глубокое понимание клиентских "болей" и "выгод"
- Ключевые слова: "ценность", "клиент", "боли", "выгоды", "product-market fit", "customer jobs"

---

## Интеграция с Life OS

### Step 1 -- Collect Ideas
- Design Thinking (Empathize phase) напрямую питает Pains и Gains
- Если в идее обнаружены слова "боль клиента", "выгода", "потребность" -- автоматически предлагать VPC
- Empathy Map данные -> Customer Profile

### Step 4 -- Consilium
- UX Designer / Product Manager лидирует VPC-анализ
- Business Strategist валидирует Product-Market Fit
- Six Hats: Red Hat для эмоциональных Jobs, Yellow Hat для Gains, Black Hat для Pains
- Consilium проверяет Fit между Value Map и Customer Profile
- TRIZ: если Pain Reliever создает новую Pain -- противоречие, применить 40 принципов

### Step 5 -- Scoring
- **Pain-Relief Effectiveness**: насколько Pain Relievers устраняют Pains (по severity)
- **Gain Creation Strength**: насколько Gain Creators доставляют Gains (по importance)
- **Customer Job Alignment**: совпадение Products/Services с Customer Jobs
- Веса: основаны на severity Pains и importance Gains

### Step 8 -- Deep Plan
- **L2 headings**: "Address Critical Pains", "Deliver Key Gains", "Validate Customer Jobs"
- **L3 tasks**: конкретные Pain Relievers и Gain Creators для создания
- **Milestones**: Pain-Reliever Fit validated, Gain-Creator Fit validated, Full Fit achieved

---

## Авто-заполнение

**Из workflow-plan.md:**
- `{{frontmatter.target_audience}}` -> Customer Segment description
- `{{frontmatter.mission}}` -> основа для Products & Services

**Из Lean Canvas (если заполнен):**
- LC "Problem" -> VPC "Pains"
- LC "Solution" -> VPC "Pain Relievers"
- LC "Customer Segments" -> VPC "Customer Profile"
- LC "UVP" -> VPC "Products & Services" summary

**Из Design Thinking (если проводился):**
- Empathy Map -> Customer Jobs (functional, social, emotional)
- User Interviews -> Pains (с цитатами) и Gains (с примерами)

---

## Customer Profile (Профиль клиента) -- Правая сторона

### Customer Jobs (Задачи клиента)

> Что клиент пытается сделать? Какие задачи решает в жизни/работе?

#### Functional Jobs (Функциональные задачи)

| # | Задача | Контекст | Частота | Важность |
|---|--------|---------|---------|----------|
| FJ1 | [Что клиент пытается выполнить?] | [Когда/где возникает] | [Daily/Weekly/Monthly] | [Critical/High/Medium/Low] |
| FJ2 | [Задача 2] | [Контекст] | [Частота] | [Важность] |
| FJ3 | [Задача 3] | [Контекст] | [Частота] | [Важность] |

#### Social Jobs (Социальные задачи)

| # | Задача | Желаемое восприятие |
|---|--------|-------------------|
| SJ1 | [Как клиент хочет выглядеть в глазах других?] | [Образ] |
| SJ2 | [Социальный статус / принадлежность] | [Образ] |

#### Emotional Jobs (Эмоциональные задачи)

| # | Задача | Желаемое чувство |
|---|--------|-----------------|
| EJ1 | [Как клиент хочет себя чувствовать?] | [Эмоция] |
| EJ2 | [Безопасность / уверенность / радость] | [Эмоция] |

---

### Pains (Боли клиента)

> Что раздражает, мешает, пугает клиента при выполнении задач?

| # | Боль | Severity | Частота | Текущее решение |
|---|------|----------|---------|----------------|
| P1 | [Боль 1 -- что именно мешает/раздражает] | [Extreme / High / Moderate / Low] | [Always / Often / Sometimes / Rarely] | [Как справляется сейчас] |
| P2 | [Боль 2] | [Severity] | [Частота] | [Текущее решение] |
| P3 | [Боль 3] | [Severity] | [Частота] | [Текущее решение] |
| P4 | [Боль 4] | [Severity] | [Частота] | [Текущее решение] |
| P5 | [Боль 5] | [Severity] | [Частота] | [Текущее решение] |

**Типы болей:**
- [ ] Нежелательные результаты ("Не работает", "Слишком медленно")
- [ ] Препятствия ("Нет времени", "Нет денег", "Нет навыков")
- [ ] Риски ("Могу потерять", "Могу выглядеть глупо")

---

### Gains (Выгоды клиента)

> Какие результаты и преимущества клиент хочет получить?

| # | Выгода | Importance | Тип | Ожидание |
|---|--------|-----------|-----|---------|
| G1 | [Выгода 1 -- желаемый результат] | [Critical / High / Nice-to-have] | [Required / Expected / Desired / Unexpected] | [Минимальный порог] |
| G2 | [Выгода 2] | [Importance] | [Тип] | [Порог] |
| G3 | [Выгода 3] | [Importance] | [Тип] | [Порог] |
| G4 | [Выгода 4] | [Importance] | [Тип] | [Порог] |
| G5 | [Выгода 5] | [Importance] | [Тип] | [Порог] |

---

## Value Map (Карта ценности) -- Левая сторона

### Products & Services (Продукты и сервисы)

> Что мы предлагаем клиенту?

| # | Продукт/Сервис | Тип | Статус | Привязка к Job |
|---|---------------|-----|--------|---------------|
| PS1 | [Продукт 1] | [Physical / Digital / Intangible / Financial] | [Existing / Planned / MVP] | [FJ1, SJ1] |
| PS2 | [Продукт 2] | [Тип] | [Статус] | [Jobs] |
| PS3 | [Сервис 1] | [Тип] | [Статус] | [Jobs] |

---

### Pain Relievers (Обезболивающие)

> Как наши продукты устраняют боли клиента?

| # | Pain Reliever | Устраняет Pain | Степень устранения | Доказательство |
|---|--------------|---------------|-------------------|---------------|
| PR1 | [Как конкретно устраняем боль 1] | P1 | [Full / Partial / Minimal] | [Данные / тесты / отзывы] |
| PR2 | [Как устраняем боль 2] | P2 | [Степень] | [Доказательство] |
| PR3 | [Как устраняем боль 3] | P3 | [Степень] | [Доказательство] |

---

### Gain Creators (Создатели выгод)

> Как наши продукты создают выгоды для клиента?

| # | Gain Creator | Создает Gain | Степень создания | Доказательство |
|---|-------------|-------------|-----------------|---------------|
| GC1 | [Как конкретно создаем выгоду 1] | G1 | [Full / Partial / Minimal] | [Данные / тесты / отзывы] |
| GC2 | [Как создаем выгоду 2] | G2 | [Степень] | [Доказательство] |
| GC3 | [Как создаем выгоду 3] | G3 | [Степень] | [Доказательство] |

---

## Fit Analysis (Анализ соответствия)

### Pain-Reliever Fit

| Pain | Severity | Pain Reliever | Degree | Fit Status |
|------|----------|--------------|--------|-----------|
| P1 | [Extreme/High/Moderate/Low] | PR[X] | [Full/Partial/Minimal/None] | [Matched / Weak / Gap] |
| P2 | [Severity] | PR[X] | [Degree] | [Status] |
| P3 | [Severity] | PR[X] | [Degree] | [Status] |

### Gain-Creator Fit

| Gain | Importance | Gain Creator | Degree | Fit Status |
|------|-----------|-------------|--------|-----------|
| G1 | [Critical/High/Nice-to-have] | GC[X] | [Full/Partial/Minimal/None] | [Matched / Weak / Gap] |
| G2 | [Importance] | GC[X] | [Degree] | [Status] |
| G3 | [Importance] | GC[X] | [Degree] | [Status] |

### Gaps (Пробелы)

| Тип | Элемент | Severity/Importance | Gap Description | Action Required |
|-----|---------|-------------------|----------------|----------------|
| Unaddressed Pain | P[X] | [Severity] | [Почему нет Pain Reliever] | [Что нужно создать] |
| Undelivered Gain | G[X] | [Importance] | [Почему нет Gain Creator] | [Что нужно создать] |

### Overall Fit Score

| Метрика | Значение |
|---------|---------|
| Pains addressed (Full/Partial) | [X/Y] ([%]) |
| Gains delivered (Full/Partial) | [X/Y] ([%]) |
| Critical gaps remaining | [count] |
| **Product-Market Fit Assessment** | [Strong / Moderate / Weak / No Fit] |

---

## Scoring Impact (данные для Step 5)

```yaml
criteria_from_framework:
  - name: "Pain-Relief Effectiveness"
    weight: 0.20
    rationale: "Средний Degree across top Pains (weighted by severity)"
  - name: "Gain Creation Strength"
    weight: 0.15
    rationale: "Средний Degree across top Gains (weighted by importance)"
  - name: "Customer Job Alignment"
    weight: 0.10
    rationale: "% Products/Services привязанных к конкретным Jobs"
```

---

## Deep Plan Contribution (данные для Step 8)

**L2 Headings:**
- "Address Critical Pains" (Pain Relievers для Extreme/High severity)
- "Deliver Key Gains" (Gain Creators для Critical/High importance)
- "Validate Customer Jobs" (интервью и тесты для подтверждения Jobs)

**L3 Tasks:**
- Создание конкретных Pain Relievers для каждого Gap
- Разработка Gain Creators для неохваченных Gains
- Customer interviews для валидации предположений (минимум 10)

**Milestones:**
- Pain-Reliever Fit validated (>80% critical pains addressed)
- Gain-Creator Fit validated (>70% high-importance gains delivered)
- Full Product-Market Fit achieved (paying customers confirm value)

---

## Метрики успеха

- **Fit Coverage**: % Pains/Gains с matched Relievers/Creators
- **Customer Validation Rate**: % клиентов, подтвердивших Jobs/Pains/Gains
- **Pain Resolution NPS**: удовлетворенность устранением болей (0-10)
- **Time to Fit**: дни от первого VPC до confirmed Product-Market Fit

---

## Синергии

| Фреймворк | Как усиливает VPC |
|-----------|------------------|
| **Lean Canvas** | LC "Problem" -> VPC "Pains". LC "Solution" -> VPC "Pain Relievers". **Auto-link**: двусторонняя синхронизация |
| **BMC** | VPC "Customer Jobs" -> BMC "Customer Segments". VPC "Pain Relievers" + "Gain Creators" -> BMC "Value Propositions" |
| **Design Thinking** | Empathize phase -> Customer Profile. Prototype -> Products & Services. Test -> Fit Analysis |
| **Jobs-to-be-Done** | JTBD framework углубляет Customer Jobs анализ |
| **TRIZ** | Если Pain Reliever создает новую Pain -- TRIZ для разрешения противоречия |

---

## Memory Storage

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "bmad:frameworks:business:vpc:{{project_id}}" \
  --content "VPC for {{project_name}}: Jobs=[count], Pains=[count](top: [pain]), Gains=[count](top: [gain]), Fit=[Strong/Moderate/Weak], Gaps=[count]"
```

---

## Решения (Decision Tracking)

1. **Решение**: [Что было решено на основе VPC-анализа]
   - **Обоснование**: [Почему, исходя из Fit Analysis]
   - **Компромиссы**: [Чем пожертвовали]
   - **Уверенность**: [High / Medium / Low]

---

## Следующие шаги

- [ ] Заполнить Customer Profile (начать с Customer Jobs)
- [ ] Ранжировать Pains по Severity и Gains по Importance
- [ ] Заполнить Value Map (Products, Pain Relievers, Gain Creators)
- [ ] Провести Fit Analysis -- найти Gaps
- [ ] Валидировать с клиентами (минимум 10 интервью)
- [ ] Синхронизировать с Lean Canvas (Problem <-> Pains, Solution <-> Relievers)
- [ ] Передать данные в BMC (Value Propositions block)
- [ ] Передать данные в Step 5 (scoring) и Step 8 (deep plan)

---

**Framework Version**: 1.0
**Life OS Version**: 2.0
**Template Last Updated**: 2026-02-04
