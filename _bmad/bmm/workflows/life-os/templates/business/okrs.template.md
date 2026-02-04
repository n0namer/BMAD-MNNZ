---
template: okrs
domain: business
tier: 1
framework: "OKRs (Objectives and Key Results)"
applicability: high
timeInvestment: moderate
complexity: medium
score: "23/25 (92%)"
synergies:
  - lean-canvas
  - swot
  - eisenhower
  - deliberate-practice
  - smart-goals-health
integration_points:
  - step-04-consilium.md
  - step-05-scoring.md
  - step-08-deep-plan.md
outputs:
  - okrs-analysis.md
  - "Append to workflow-plan.md"
scoring_contribution:
  provides_criteria: true
  provides_weights: true
  provides_scenarios: false
  mcda_dimensions:
    - "Strategic Alignment"
    - "KR Achievement Likelihood"
    - "Resource Requirements"
deep_plan_contribution:
  generates_l2_headings: true
  generates_l3_tasks: true
  generates_milestones: true
linked_frameworks:
  - lean-canvas
  - business-model-canvas
  - gtd
  - eisenhower
prerequisite_frameworks: []
follows_frameworks: []
research_notes: "92% effectiveness in meta-analysis. Google, Intel, LinkedIn standard."
---

# OKRs (Objectives and Key Results): {{project_name}}

> **Проект**: {{project_name}}
> **Домен**: Business & Career
> **Дата создания**: {{date}}
> **Аналитик**: {{user_name}}
> **Время на заполнение**: 45-90 минут

---

## Назначение

OKR -- система постановки целей, соединяющая амбициозные качественные цели (Objectives) с конкретными измеримыми результатами (Key Results). Используется Google, Intel, LinkedIn и другими для выравнивания стратегии с тактическим исполнением.

**Когда применять:**
- Запуск нового продукта или бизнеса
- Квартальное или годовое планирование
- Необходимо измерить прогресс к стратегической цели
- Несколько команд или ролей должны работать синхронно
- Ключевые слова: "цель", "результат", "метрика", "выравнивание", "OKR"

---

## Интеграция с Life OS

### Step 4 -- Consilium
- Business Strategist рекомендует OKR для любого проекта, требующего стратегического выравнивания
- Six Thinking Hats: Yellow Hat генерирует амбициозные Objectives, Black Hat проверяет реалистичность Key Results
- Specialist Match: если обнаружены ключевые слова "цель", "метрика", "KPI" -- автоматически предлагать OKR

### Step 5 -- Scoring
- **Strategic Alignment (20%)**: Objectives проекта сравниваются с mission из workflow-plan.md
- **KR Achievement Likelihood**: каждый KR оценивается по вероятности достижения (0-100%)
- **Resource Requirements**: инициативы оцениваются по ресурсоемкости
- Формула: `OKR_Score = avg(KR_confidence) * strategic_alignment_weight`

### Step 8 -- Deep Plan
- **L2 headings**: каждый Key Result становится отдельной фазой
- **L3 tasks**: инициативы разбиваются на конкретные задачи по неделям
- **Milestones**: 25%, 50%, 75%, 100% достижения каждого KR

---

## Авто-заполнение

**Из workflow-plan.md:**
- `{{frontmatter.mission}}` -> Objective (основа для формулировки)
- `{{frontmatter.project_id}}` -> привязка к проекту
- `{{frontmatter.timeline}}` -> Time Horizon для OKR

**Из consilium output:**
- Рекомендации специалистов -> формулировки KR
- TRIZ-противоречия -> ограничения для KR targets

---

## Структура фреймворка

### Objective 1

> **Формулировка**: [Качественная, вдохновляющая цель -- ЧТО мы хотим достичь?]
> **Горизонт**: [Квартал | Год | Мультигод]
> **Выравнивание**: [Какой стратегической цели подчинена -- из workflow-plan.md mission]

#### Key Result 1.1

| Параметр | Значение |
|----------|----------|
| **Метрика** | [Что измеряем] |
| **Базовая линия** | [Текущее состояние: X] |
| **Целевое значение** | [Желаемое состояние: Y] |
| **Частота измерения** | [Ежедневно / Еженедельно / Ежемесячно] |
| **Ответственный** | [Роль или имя] |
| **Уверенность** | [Low 30% / Medium 50% / High 70%] |

#### Key Result 1.2

| Параметр | Значение |
|----------|----------|
| **Метрика** | [Что измеряем] |
| **Базовая линия** | [Текущее состояние: X] |
| **Целевое значение** | [Желаемое состояние: Y] |
| **Частота измерения** | [Ежедневно / Еженедельно / Ежемесячно] |
| **Ответственный** | [Роль или имя] |
| **Уверенность** | [Low 30% / Medium 50% / High 70%] |

#### Key Result 1.3

| Параметр | Значение |
|----------|----------|
| **Метрика** | [Что измеряем] |
| **Базовая линия** | [Текущее состояние: X] |
| **Целевое значение** | [Желаемое состояние: Y] |
| **Частота измерения** | [Ежедневно / Еженедельно / Ежемесячно] |
| **Ответственный** | [Роль или имя] |
| **Уверенность** | [Low 30% / Medium 50% / High 70%] |

### Initiatives (Действия для достижения KR)

| # | Инициатива | Связь с KR | Срок | Статус |
|---|-----------|-----------|------|--------|
| 1 | [Инициатива 1] | KR 1.1 | [Дата] | [ ] |
| 2 | [Инициатива 2] | KR 1.2, KR 1.3 | [Дата] | [ ] |
| 3 | [Инициатива 3] | KR 1.1, KR 1.3 | [Дата] | [ ] |

### Objective 2 (если применимо)

> **Формулировка**: [Вторая качественная цель]
> **Горизонт**: [Период]
> **Выравнивание**: [Стратегическая привязка]

_Повторить структуру KR 2.1, 2.2, 2.3 по аналогии с Objective 1._

---

## Scoring Impact (данные для Step 5)

```yaml
criteria_from_framework:
  - name: "Strategic Alignment"
    weight: 0.20
    rationale: "Objective должен быть выровнен с mission проекта"
  - name: "KR Achievement Likelihood"
    weight: 0.15
    rationale: "Средняя уверенность по всем KR"
  - name: "Resource Efficiency"
    weight: 0.10
    rationale: "Количество инициатив на один KR (меньше = эффективнее)"
```

---

## Deep Plan Contribution (данные для Step 8)

**L2 Headings (генерируются автоматически):**
- Каждый Key Result -> отдельная фаза L2
- Пример: "KR1: Достичь 10 клиентов" -> L2: "Привлечение клиентов"

**L3 Tasks (генерируются из инициатив):**
- Каждая инициатива разбивается на недельные задачи
- Привязка к конкретным неделям/спринтам

**Milestones (контрольные точки):**
- 25% KR target -- промежуточная проверка
- 50% KR target -- mid-review
- 75% KR target -- финальный рывок
- 100% KR target -- достижение цели

---

## Tracking (отслеживание прогресса)

| Неделя | KR 1.1 Progress | KR 1.2 Progress | KR 1.3 Progress | Overall | Примечания |
|--------|-----------------|-----------------|-----------------|---------|-----------|
| 1 | [X/Y] | [X/Y] | [X/Y] | [%] | [Наблюдения] |
| 2 | [X/Y] | [X/Y] | [X/Y] | [%] | |
| 3 | [X/Y] | [X/Y] | [X/Y] | [%] | |
| 4 | [X/Y] | [X/Y] | [X/Y] | [%] | |

---

## Метрики успеха

- **OKR Completion Rate**: процент KR, достигнутых на 70%+ (норма Google: 60-70%)
- **Alignment Score**: степень связи Objective с mission (0-10)
- **Initiative Efficiency**: % инициатив, которые реально повлияли на KR
- **Time-to-Value**: дни от старта до первого значимого движения KR

---

## Синергии

| Фреймворк | Как усиливает OKR |
|-----------|-------------------|
| **Lean Canvas** | Key Metrics из Lean Canvas -> KR для бизнес-метрик |
| **BMC** | Key Activities из BMC -> Инициативы OKR |
| **SWOT** | SO-стратегии -> формулировки Objectives |
| **Eisenhower** | Q2 (Important, Not Urgent) -> время на OKR-инициативы |
| **GTD** | OKR Initiatives -> GTD Projects -> Next Actions |
| **TRIZ** | Противоречия в KR -> TRIZ для нахождения решений |

---

## Memory Storage

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "bmad:frameworks:business:okrs:{{project_id}}" \
  --content "OKR analysis for {{project_name}}: [Objective summary], [KR count], [avg confidence]%"
```

---

## Решения (Decision Tracking)

1. **Решение**: [Что было решено на основе OKR-анализа]
   - **Обоснование**: [Почему, исходя из KR-данных]
   - **Компромиссы**: [Чем пожертвовали]
   - **Уверенность**: [High / Medium / Low]

---

## Следующие шаги

- [ ] Заполнить Objective(s) -- выровнять с mission из workflow-plan.md
- [ ] Определить 3-5 KR на каждый Objective
- [ ] Оценить уверенность каждого KR (30/50/70%)
- [ ] Создать инициативы и привязать к KR
- [ ] Передать данные в Step 5 (scoring) и Step 8 (deep plan)

---

**Framework Version**: 1.0
**Life OS Version**: 2.0
**Template Last Updated**: 2026-02-04
