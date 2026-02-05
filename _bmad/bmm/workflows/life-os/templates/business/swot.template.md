---
template: swot
domain: business
tier: 2
tier_name: "Intermediate"
unlock_requirement: "3 workflows"
category: "business"
difficulty: "intermediate"
estimated_time: "10 min"
description: "SWOT analysis for strategic business planning"
framework: "SWOT Analysis"
applicability: high
timeInvestment: moderate
complexity: low
score: "21/25 (84%)"
synergies:
  - porters-five-forces
  - okrs
  - six-thinking-hats
  - business-model-canvas
integration_points:
  - step-04-consilium.md
  - step-05-scoring.md
  - step-08-deep-plan.md
outputs:
  - swot-analysis.md
  - "Append to workflow-plan.md"
scoring_contribution:
  provides_criteria: true
  provides_weights: true
  provides_scenarios: true
  mcda_dimensions:
    - "Strategic Position"
    - "Risk Exposure"
    - "Opportunity Capture"
deep_plan_contribution:
  generates_l2_headings: true
  generates_l3_tasks: true
  generates_milestones: false
linked_frameworks:
  - porters-five-forces
  - business-model-canvas
  - lean-canvas
  - okrs
prerequisite_frameworks: []
follows_frameworks: []
research_notes: "84% effectiveness. Classic strategic framework."
---

# SWOT Analysis: {{project_name}}

> **Проект**: {{project_name}}
> **Домен**: Business & Career
> **Дата создания**: {{date}}
> **Аналитик**: {{user_name}}
> **Время на заполнение**: 30-45 минут

---

## Назначение

SWOT -- классический фреймворк стратегического анализа, оценивающий внутренние (Strengths, Weaknesses) и внешние (Opportunities, Threats) факторы. Расширяется до TOWS-матрицы для генерации стратегий.

**Когда применять:**
- Стратегическое планирование проекта или бизнеса
- Анализ ситуации перед принятием важного решения
- Оценка конкурентной позиции
- Ключевые слова: "анализ", "стратегия", "конкуренты", "риски", "преимущества"

---

## Интеграция с Life OS

### Step 4 -- Consilium
- Каждый специалист consilium вносит вклад в квадранты на основе Six Thinking Hats:
  - **White Hat** (факты) -> Strengths (подтвержденные данными)
  - **Black Hat** (осторожность) -> Weaknesses + Threats
  - **Yellow Hat** (оптимизм) -> Opportunities + Strengths
  - **Green Hat** (креативность) -> SO/WO-стратегии (новые идеи)
  - **Red Hat** (интуиция) -> приоритизация факторов по "ощущению важности"
  - **Blue Hat** (процесс) -> координация заполнения всех квадрантов
- Market Analyst лидирует анализ Threats и Opportunities
- Business Strategist лидирует анализ Strengths и Weaknesses

### Step 5 -- Scoring
- SWOT генерирует сценарии: Best case (SO), Worst case (WT), Mixed (ST, WO)
- Threats получают веса = Probability x Impact
- Strengths повышают оценку Strategic Alignment
- Формула: `SWOT_Score = (strengths_count * leverage + opportunities_score) - (threats_risk + weaknesses_severity)`

### Step 8 -- Deep Plan
- **L2 headings**: "Capitalize on Strengths", "Address Weaknesses", "Seize Opportunities", "Mitigate Threats"
- **L3 tasks**: каждая TOWS-стратегия становится набором действий

---

## Авто-заполнение из Consilium

**Из step-04-consilium.md:**
- Каждый специалист добавляет 1-3 пункта в соответствующий квадрант
- TRIZ-анализ: противоречия часто обнажают пары Strength/Weakness
- Porter's Five Forces (если заполнен): Threats <- Competitive Rivalry + New Entrants

---

## 4 Квадранта SWOT

### Strengths (Сильные стороны) -- Внутренние, Позитивные

| # | Сила | Доказательство | Как использовать (Leverage) |
|---|------|---------------|---------------------------|
| S1 | [Сильная сторона 1] | [Почему это правда -- факты, метрики] | [Как усилить / капитализировать] |
| S2 | [Сильная сторона 2] | [Доказательство] | [Использование] |
| S3 | [Сильная сторона 3] | [Доказательство] | [Использование] |
| S4 | [Сильная сторона 4] | [Доказательство] | [Использование] |
| S5 | [Сильная сторона 5] | [Доказательство] | [Использование] |

---

### Weaknesses (Слабые стороны) -- Внутренние, Негативные

| # | Слабость | Доказательство | Митигация (как уменьшить) |
|---|---------|---------------|--------------------------|
| W1 | [Слабость 1] | [Почему это проблема] | [План устранения] |
| W2 | [Слабость 2] | [Доказательство] | [Митигация] |
| W3 | [Слабость 3] | [Доказательство] | [Митигация] |
| W4 | [Слабость 4] | [Доказательство] | [Митигация] |
| W5 | [Слабость 5] | [Доказательство] | [Митигация] |

---

### Opportunities (Возможности) -- Внешние, Позитивные

| # | Возможность | Временное окно | Требования для захвата |
|---|------------|---------------|----------------------|
| O1 | [Возможность 1] | [Когда окно открыто?] | [Что нужно для реализации?] |
| O2 | [Возможность 2] | [Окно] | [Требования] |
| O3 | [Возможность 3] | [Окно] | [Требования] |
| O4 | [Возможность 4] | [Окно] | [Требования] |
| O5 | [Возможность 5] | [Окно] | [Требования] |

---

### Threats (Угрозы) -- Внешние, Негативные

| # | Угроза | Вероятность | Влияние | Risk Score | Ответ |
|---|--------|-----------|---------|-----------|-------|
| T1 | [Угроза 1] | [H/M/L] | [H/M/L] | [P x I] | [Как митигировать] |
| T2 | [Угроза 2] | [H/M/L] | [H/M/L] | [P x I] | [Ответ] |
| T3 | [Угроза 3] | [H/M/L] | [H/M/L] | [P x I] | [Ответ] |
| T4 | [Угроза 4] | [H/M/L] | [H/M/L] | [P x I] | [Ответ] |
| T5 | [Угроза 5] | [H/M/L] | [H/M/L] | [P x I] | [Ответ] |

---

## TOWS Matrix (Стратегии)

### SO-Стратегии (Силы + Возможности -> Наступление)

> Используем сильные стороны для захвата возможностей.

| # | Стратегия | S используемые | O захватываемые | Приоритет |
|---|-----------|---------------|-----------------|----------|
| SO1 | [Стратегия 1] | S1, S3 | O1 | [H/M/L] |
| SO2 | [Стратегия 2] | S2 | O2, O3 | [H/M/L] |

---

### WO-Стратегии (Слабости + Возможности -> Улучшение)

> Преодолеваем слабости для захвата возможностей.

| # | Стратегия | W устраняемые | O захватываемые | Приоритет |
|---|-----------|--------------|-----------------|----------|
| WO1 | [Стратегия 1] | W1 | O1 | [H/M/L] |
| WO2 | [Стратегия 2] | W2, W3 | O2 | [H/M/L] |

---

### ST-Стратегии (Силы + Угрозы -> Защита)

> Используем сильные стороны для нейтрализации угроз.

| # | Стратегия | S используемые | T нейтрализуемые | Приоритет |
|---|-----------|---------------|------------------|----------|
| ST1 | [Стратегия 1] | S1 | T1 | [H/M/L] |
| ST2 | [Стратегия 2] | S3, S4 | T2 | [H/M/L] |

---

### WT-Стратегии (Слабости + Угрозы -> Минимизация)

> Минимизируем слабости и избегаем угроз.

| # | Стратегия | W минимизируемые | T избегаемые | Приоритет |
|---|-----------|-----------------|-------------|----------|
| WT1 | [Стратегия 1] | W1, W2 | T1 | [H/M/L] |
| WT2 | [Стратегия 2] | W3 | T3, T4 | [H/M/L] |

---

## Scoring Impact (данные для Step 5)

```yaml
criteria_from_framework:
  - name: "Strategic Position"
    weight: 0.15
    rationale: "Баланс S vs. W -- внутренняя сила проекта"
  - name: "Risk Exposure"
    weight: 0.15
    rationale: "Суммарный Risk Score всех Threats"
  - name: "Opportunity Capture"
    weight: 0.10
    rationale: "Количество реалистичных SO-стратегий"

scenarios_from_framework:
  - name: "Best Case (SO)"
    description: "Все SO-стратегии успешны"
    probability: "20%"
  - name: "Base Case (SO+WO)"
    description: "Часть стратегий успешна, слабости частично устранены"
    probability: "60%"
  - name: "Worst Case (WT)"
    description: "Угрозы реализовались, слабости не устранены"
    probability: "20%"
```

---

## Deep Plan Contribution (данные для Step 8)

**L2 Headings:**
- "Capitalize on Strengths" (SO-стратегии)
- "Address Weaknesses" (WO-стратегии)
- "Seize Opportunities" (SO + WO стратегии)
- "Mitigate Threats" (ST + WT стратегии)

**L3 Tasks:**
- Каждая TOWS-стратегия разбивается на конкретные действия
- Threats с высоким Risk Score получают приоритетные задачи
- Opportunities с ограниченным временным окном получают дедлайны

---

## Сводная таблица

| Квадрант | Кол-во факторов | Средний вес | Доминирующий |
|----------|----------------|-------------|-------------|
| Strengths | [N] | -- | [Самая сильная S] |
| Weaknesses | [N] | -- | [Самая критичная W] |
| Opportunities | [N] | -- | [Самая перспективная O] |
| Threats | [N] | [Avg Risk Score] | [Самая опасная T] |

**Общая оценка**: [Наступательная / Оборонительная / Смешанная позиция]

---

## Метрики успеха

- **Strategy Execution Rate**: % TOWS-стратегий, переведенных в действия
- **Threat Mitigation Coverage**: % угроз с планом ответа
- **Opportunity Capture Rate**: % возможностей с конкретным action plan
- **SWOT Refresh Frequency**: обновление каждые [3 / 6 / 12] месяцев

---

## Синергии

| Фреймворк | Как усиливает SWOT |
|-----------|-------------------|
| **Porter's Five Forces** | Threats <- Five Forces competitive analysis. **Auto-link**: T = Entry threat + Rivalry |
| **BMC** | Key Resources <- Strengths. Key Partners -> response to Supplier Power (Threats) |
| **Lean Canvas** | Problem <- Opportunities (unmet market needs). UVP <- SO-strategies |
| **OKRs** | SO-стратегии -> Objectives. TOWS-стратегии -> Initiatives |
| **TRIZ** | Противоречия S vs. W -> TRIZ для системного разрешения |
| **Six Thinking Hats** | Структурирует consilium-вклад по квадрантам |

---

## Memory Storage

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "bmad:frameworks:business:swot:{{project_id}}" \
  --content "SWOT for {{project_name}}: S=[count] W=[count] O=[count] T=[count], Position=[offensive/defensive], Top SO=[strategy], Top Threat=[threat]"
```

---

## Решения (Decision Tracking)

1. **Решение**: [Что было решено на основе SWOT-анализа]
   - **Обоснование**: [Почему, исходя из квадрантов и TOWS]
   - **Компромиссы**: [Чем пожертвовали]
   - **Уверенность**: [High / Medium / Low]

---

## Следующие шаги

- [ ] Заполнить все 4 квадранта (минимум 3 пункта в каждом)
- [ ] Оценить Risk Score для каждой Threat
- [ ] Составить TOWS-матрицу (минимум 2 стратегии в каждом квадранте)
- [ ] Определить приоритеты стратегий (H/M/L)
- [ ] Передать Threats в Porter's Five Forces для углубления
- [ ] Передать SO-стратегии в OKRs как Objectives
- [ ] Передать данные в Step 5 (scoring) и Step 8 (deep plan)

---

**Framework Version**: 1.0
**Life OS Version**: 2.0
**Template Last Updated**: 2026-02-04
