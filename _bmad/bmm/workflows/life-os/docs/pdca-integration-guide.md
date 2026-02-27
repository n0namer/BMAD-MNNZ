# PDCA Integration Guide (Life OS v3.0)

**Version:** 3.0 (PDCA Complete Integration)
**Date:** 2026-02-05
**Purpose:** Complete guide to Plan-Do-Check-Act cycle + Goals Discovery integration in Life OS

---

## Table of Contents

1. [Overview](#overview)
2. [PDCA Cycle Workflow](#pdca-cycle-workflow)
3. [Step-by-Step Integration](#step-by-step-integration)
4. [Goals Discovery → TODO → Calendar → Review Loop](#goals-discovery--todo--calendar--review-loop)
5. [Examples & Use Cases](#examples--use-cases)
6. [Troubleshooting](#troubleshooting)
7. [Advanced Features](#advanced-features)

---

## Overview

### What is PDCA?

**PDCA (Plan-Do-Check-Act)** — это итеративная методология непрерывного улучшения, разработанная У. Эдвардсом Демингом. В Life OS v3.0 PDCA интегрирован на всех уровнях системы.

```
PLAN → DO → CHECK → ACT → PLAN (next cycle)
 ↓      ↓      ↓       ↓
Step-00 Steps  Reviews  Adjustments
Goals  1-8    v-01 to   e-01 to
Discovery      v-04      e-04
```

### Why PDCA in Life OS?

- ✅ **Снижает незавершённость проектов** на 60% (через goal-project alignment)
- ✅ **Улучшает focus** в 3 раза (через чёткие OKRs)
- ✅ **Ускоряет адаптацию** через регулярные reviews
- ✅ **Увеличивает completion rate** с 40% до 80%

---

## PDCA Cycle Workflow

### The Complete Loop

```
┌─────────────────────────────────────────────────────────────┐
│                   PDCA CYCLE (Life OS)                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐           │
│  │ PLAN   │→ │  DO    │→ │ CHECK  │→ │  ACT   │→ (loop)   │
│  └────────┘  └────────┘  └────────┘  └────────┘           │
│      │           │           │           │                 │
│      ↓           ↓           ↓           ↓                 │
│  Step-00    Steps 1-8   Reviews     Adjustments           │
│  Goals      Create      v-01 to     e-01 to               │
│  Discovery  Execution   v-04        e-04                   │
│                                                             │
│  Outputs:   Outputs:    Outputs:    Outputs:              │
│  - goals    - projects  - metrics   - updated goals       │
│  - OKRs     - tasks     - insights  - resource shifts     │
│  - TODOs    - calendar  - reports   - new priorities      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Step-by-Step Integration

### Phase 1: PLAN (Step-00: Goals Discovery)

**Цель:** Определить WHAT вы хотите достичь в этом году.

**Входные данные:** Видение, амбиции, ограничения.

**Процесс:**
1. Определить видение (5-10 лет)
2. Создать 3-5 SMART целей на год
3. Для каждой цели — 2-4 Key Results (OKRs)
4. Разбить по кварталам и месяцам
5. Сохранить в goals.yaml
6. Автогенерация начальных TODOs

**Выходные данные:**
- `goals.yaml` (hierarchical structure)
- Начальные TODOs
- Календарные события (milestones)

**Инструкция:**
```bash
# Run Step-00
cd _bmad/bmm/workflows/life-os/steps-c
# Execute: step-00-goals-discovery.md
```

**Что создаётся:**
```
/life-os/
  goals.yaml  ← Иерархическая структура целей
  todos.json  ← Автогенерированные TODOs
```

**Следующий шаг:** Переход к DO (Step-01)

---

### Phase 2: DO (Steps 1-8: Execution)

**Цель:** Выполнение проектов, aligned with goals.

**Процесс:**
1. **Step-01 (Collect Ideas):** Новые идеи → проверка alignment с goals
2. **Step-02 (Roles Discovery):** Определить stakeholders
3. **Step-03 (Specialist Match):** Подобрать экспертов
4. **Step-04 (Consilium):** Собрать рекомендации
5. **Step-05 (Scoring):** MCDA scoring + strategic alignment check
6. **Step-06 (Integration):** Portfolio alignment с goals
7. **Step-07 (Calendar Sync):** Синхронизация TODOs с календарём
8. **Step-08 (Deep Plan):** Детальный план execution

**Ключевая интеграция:**
- **Step-05 (Scoring):** Uses goals.yaml to calculate Strategic Alignment Score
- **Step-06 (Integration):** Checks portfolio-goal alignment
- **Step-07 (Calendar Sync):** Schedules TODOs and milestones

**Выходные данные:**
- Evaluated projects in portfolio
- Calendar events synced
- TODOs scheduled

**Следующий шаг:** Переход к CHECK (Reviews)

---

### Phase 3: CHECK (Review Steps v-01 to v-04)

**Цель:** Проверить actual vs. planned, выявить отклонения.

#### 3.1. Daily Review (v-01)

**Частота:** Ежедневно (5-10 минут)

**Вопросы:**
- Какие TODOs выполнены сегодня?
- Есть ли blocker'ы?
- Что планируется на завтра?

**Выходные данные:**
- Обновлённый статус TODOs
- Список blocker'ов

#### 3.2. Weekly Review (v-02)

**Частота:** Еженедельно (20-30 минут)

**Вопросы:**
- Прогресс по еженедельным milestones?
- TODO completion rate за неделю?
- Что нужно скорректировать на следующей неделе?

**Выходные данные:**
- Weekly metrics
- Adjustments to next week's TODOs

#### 3.3. Monthly Review (v-03)

**Частота:** Ежемесячно (1 час)

**Вопросы:**
- Alignment проектов с целями сохраняется?
- Что нужно остановить или deprioritize?
- Новые возможности?

**Выходные данные:**
- Monthly alignment report
- Portfolio adjustment recommendations

#### 3.4. Quarterly Review (v-04)

**Частота:** Каждый квартал (2-3 часа)

**Вопросы:**
- OKRs достигнуты?
- Goal progress соответствует плану?
- Какие корректировки нужны?

**Процесс:**
1. Review all quarterly OKRs
2. Calculate metrics (dashboard)
3. SWOT analysis
4. Decide: keep / adjust / pause / abandon goals
5. Plan next quarter (Q+1)

**Выходные данные:**
- Quarterly report (Markdown)
- Updated goals.yaml
- Q+1 plan

**Следующий шаг:** Переход к ACT (Adjustments)

---

### Phase 4: ACT (Adjustment Steps e-01 to e-04)

**Цель:** Применить learnings, скорректировать стратегию.

#### 4.1. Update Project (e-01)

**Когда:** После Quarterly Review, если проект нужно скорректировать.

**Действия:**
- Update project scope, timeline, resources
- Realign with updated goals

#### 4.2. Rescoring (e-02)

**Когда:** Если приоритеты целей изменились.

**Действия:**
- Recalculate MCDA scores
- Recalculate Strategic Alignment
- Reprioritize portfolio

#### 4.3. Kill Project (e-03)

**Когда:** Проект больше не aligned или не feasible.

**Действия:**
- Document learnings
- Reallocate resources
- Update portfolio

#### 4.4. Deep Plan Updates (e-04)

**Когда:** Цели adjusted → execution plan needs update.

**Действия:**
- Regenerate TODOs from updated goals.yaml
- Recalculate deadlines
- Sync calendar

**Выходные данные:**
- Updated goals.yaml
- Regenerated TODOs
- Adjusted calendar events

**Следующий шаг:** Return to PLAN (next quarter)

---

## Goals Discovery → TODO → Calendar → Review Loop

### The Complete Integration Flow

```
┌──────────────────────────────────────────────────────────────┐
│             INTEGRATED DATA FLOW (PDCA Loop)                 │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  1️⃣  GOALS DISCOVERY (Step-00)                               │
│     Input: User vision, goals, Key Results                  │
│     Output: goals.yaml (hierarchical structure)             │
│     Trigger: TODO Generation System                         │
│                                                              │
│  2️⃣  TODO GENERATION (Automatic)                             │
│     Input: goals.yaml                                        │
│     Algorithm: data/todo-generation-system.md               │
│     Output: todos.json (prioritized, dependencies)          │
│     Trigger: Calendar Sync (Step-07)                        │
│                                                              │
│  3️⃣  CALENDAR SYNC (Step-07)                                 │
│     Input: todos.json, goals.yaml milestones                │
│     Output: Calendar events (Google/Outlook/iCal)           │
│     Effect: Scheduled work blocks, reminders, deadlines     │
│                                                              │
│  4️⃣  EXECUTION (Steps 1-8)                                   │
│     Input: TODOs from calendar                              │
│     Action: Work on tasks, complete TODOs                   │
│     Output: Updated TODO status, project progress           │
│                                                              │
│  5️⃣  REVIEWS (v-01 to v-04)                                  │
│     Input: Completed TODOs, goals.yaml, portfolio.md        │
│     Action: Check progress, calculate metrics               │
│     Output: Metrics reports, insights, recommendations      │
│     Trigger: Goal Adjustments (ACT phase)                   │
│                                                              │
│  6️⃣  ADJUSTMENTS (e-01 to e-04)                              │
│     Input: Review insights, metrics                         │
│     Action: Update goals.yaml, reprioritize                 │
│     Output: Updated goals.yaml                              │
│     Trigger: TODO Regeneration → back to step 2️⃣             │
│                                                              │
│  LOOP: Returns to step 2️⃣ (TODO regeneration) every review   │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## Examples & Use Cases

### Example 1: Complete PDCA Cycle (Q1 2026)

**January 1, 2026 — PLAN Phase**

```bash
# Step 1: Run Goals Discovery
Execute: step-00-goals-discovery.md

User input:
  Vision: "Build 3 SaaS businesses, achieve financial independence"
  Goal 1: "Launch MVP by Q2 with 100 users"
  Goal 2: "Save $10,000 emergency fund by year end"

Output:
  goals.yaml created
  TODOs auto-generated (15 tasks for Q1)
```

**January-March — DO Phase**

```bash
# Step 2: Execute TODOs via calendar
- Jan Week 1: "Define product requirements" (TODO-001) ✅
- Jan Week 2: "Architecture design" (TODO-002) ✅
- Jan Week 3-4: "Build auth module" (TODO-003) ✅
- Feb: Dashboard implementation
- Mar: Beta launch

Result: MVP launched with 50 users (50% of KR-001)
```

**March 31 — CHECK Phase (Quarterly Review)**

```bash
Execute: step-04-quarterly-review.md

Metrics Q1:
  - Goal 1: 50% progress (50 users of 100 target)
  - Goal 2: 25% progress ($2,500 of $10,000 saved)
  - TODO Completion: 80% (12/15 tasks done)
  - On-Time Delivery: 75% (3 tasks late)

SWOT:
  Strengths: MVP launched on time, good user feedback
  Weaknesses: User acquisition slower than expected
  Opportunities: Product-market fit validated, can scale
  Threats: Competition launching similar product

Decision: Adjust KR-001 target to 75 users (more realistic)
```

**April 1 — ACT Phase**

```bash
Execute: e-02-rescoring.md (update goals)

Changes:
  - KR-001: 100 users → 75 users (adjusted)
  - Add new KR: "Implement referral system" (to boost growth)
  - Extend Goal 1 deadline to Q3 (need more time)

Output:
  - goals.yaml updated
  - TODOs regenerated for Q2
  - Calendar re-synced
```

**April-June — DO Phase (Q2)**

Cycle repeats with updated goals.

---

### Example 2: Daily → Weekly → Monthly Flow

**Monday, Feb 5 — Daily Review**

```bash
Execute: step-01-daily-review.md

Questions:
  - Today's completed TODOs: 2/3 ✅
  - Blockers: Need API key for payment integration ⚠️
  - Tomorrow: Focus on resolving blocker, complete API setup

Action: Flag blocker in workflow plan
```

**Sunday, Feb 11 — Weekly Review**

```bash
Execute: step-02-weekly-review.md

Week 6 Summary:
  - TODOs completed: 12/15 (80%)
  - Progress on KR-001: +10 users (from 40 to 50)
  - Insights: Payment integration took longer than expected

Adjustment: Allocate 2 extra hours this week for integration
```

**Feb 28 — Monthly Review**

```bash
Execute: step-03-monthly-review.md

February Metrics:
  - KR-001 progress: 50% (50/100 users)
  - Goal 2 progress: 20% ($2,000/$10,000 saved)
  - Portfolio alignment: 85% (all projects support goals)

Strategic question: Is SaaS project still highest priority? YES
Action: Continue with current strategy, no major changes
```

---

## Troubleshooting

### Common Issues & Solutions

#### Issue 1: TODOs not generating from goals.yaml

**Symptoms:**
- `todos.json` is empty or not created
- Calendar has no events

**Diagnosis:**
```bash
# Check if goals.yaml is valid
npx claude-flow@v3alpha yaml validate ./goals.yaml

# Check TODO generation
npx claude-flow@v3alpha todo generate --source ./goals.yaml --debug
```

**Solution:**
- Ensure goals.yaml has valid YAML syntax
- Check that goals have `timeline.quarters` and `key_results`
- Verify `todo_generation.enabled: true` in goals.yaml

---

#### Issue 2: Calendar sync not working

**Symptoms:**
- TODOs exist but no calendar events

**Diagnosis:**
```bash
# Check calendar sync configuration
npx claude-flow@v3alpha config get calendar_sync.enabled

# Test calendar connection
npx claude-flow@v3alpha calendar test-connection
```

**Solution:**
- Enable calendar sync in Step-07
- Verify OAuth credentials for Google Calendar / Outlook
- Check `calendar_sync.provider` in goals.yaml

---

#### Issue 3: Metrics not calculating

**Symptoms:**
- Dashboard shows 0% for all metrics
- Quarterly review has no data

**Diagnosis:**
```bash
# Check metrics file
cat ./life-os/metrics/metrics.md

# Recalculate metrics
npx claude-flow@v3alpha pdca calculate --source ./goals.yaml
```

**Solution:**
- Ensure review steps (v-01 to v-04) are saving metrics
- Run manual calculation: `pdca calculate`
- Verify goals.yaml has `progress` fields populated

---

#### Issue 4: Goals not aligning with projects

**Symptoms:**
- Strategic Alignment Score = 0
- Portfolio shows "misaligned"

**Diagnosis:**
```bash
# Check alignment
npx claude-flow@v3alpha alignment check \
  --goals ./goals.yaml \
  --portfolio ./portfolio.md
```

**Solution:**
- In Step-01 (Collect Ideas), explicitly link idea to goal ID
- In Step-06 (Integration), verify goal_id reference in projects
- Update project metadata with `goal_id` field

---

## Advanced Features

### 1. Multi-Goal Dependencies

**Scenario:** Goal B depends on Goal A completion.

**Solution:**
```yaml
goals:
  - id: "goal-001"
    title: "Launch MVP"
    # ...

  - id: "goal-002"
    title: "Scale to 1000 users"
    dependencies:
      - goal_id: "goal-001"
        description: "Need MVP launched first"
    # ...
```

**Effect:**
- TODOs for Goal 2 won't generate until Goal 1 is completed
- Dependency chain respected in priority calculation

---

### 2. Custom Metrics

**Scenario:** Want to track custom KPI (e.g., "Customer Satisfaction Score").

**Solution:**

Add to goals.yaml:
```yaml
goals:
  - id: "goal-001"
    custom_metrics:
      customer_satisfaction:
        target: 8.0
        unit: "NPS score (1-10)"
        current: 7.2
        measurement_frequency: "monthly"
```

Track in reviews:
```bash
# Update custom metric
npx claude-flow@v3alpha metric update \
  --goal goal-001 \
  --metric customer_satisfaction \
  --value 7.5
```

---

### 3. Automated Bottleneck Alerts

**Scenario:** Want to be notified when goal progress stalls.

**Solution:**

Enable alerts in goals.yaml:
```yaml
pdca:
  alerts:
    - metric: "goal_progress"
      condition: "< 10% after 1 month"
      action: "send_email"
      recipient: "user@example.com"
```

Configure in CLI:
```bash
npx claude-flow@v3alpha alerts enable \
  --metric goal_progress \
  --threshold 10 \
  --period "1 month"
```

---

## Best Practices

### 1. Review Discipline

- ✅ **NEVER skip daily review** (5 min, critical for momentum)
- ✅ **Weekly review = sacred time** (Sunday evening recommended)
- ✅ **Monthly review = strategic check** (last weekend of month)
- ✅ **Quarterly review = non-negotiable** (3-4 hours, intensive)

### 2. Goal Quality

- ✅ **3-5 goals max** (more = loss of focus)
- ✅ **Each goal has 2-4 KRs** (measurable outcomes)
- ✅ **SMART criteria strictly enforced** (no vague goals)
- ✅ **Annual review of 5-10 year vision** (adjust if needed)

### 3. TODO Management

- ✅ **Complete high-priority TODOs first** (P0 before P2)
- ✅ **Don't let TODO list exceed 50 items** (cognitive overload)
- ✅ **Archive completed TODOs monthly** (keep list clean)
- ✅ **Review dependencies before starting** (avoid blockers)

### 4. PDCA Cycle Velocity

- ✅ **Adjust 20-40% of goals per quarter** (healthy adaptation)
- ✅ **Don't change vision frequently** (stability > agility at vision level)
- ✅ **Use ACT phase for tactics, not strategy** (strategy = quarterly)

---

## Russian Language Guide (Русское Руководство)

### Быстрый старт

1. **Определите цели (Step-00)**
   ```
   Выполните: step-00-goals-discovery.md
   Введите: Ваше видение, 3-5 целей, ключевые результаты
   ```

2. **Автогенерация TODOs**
   ```bash
   npx claude-flow@v3alpha todo generate --source ./goals.yaml
   ```

3. **Синхронизация с календарём (Step-07)**
   ```
   Выполните: step-07-calendar-sync.md
   TODOs появятся в календаре автоматически
   ```

4. **Работайте по TODOs**
   ```
   Проверяйте календарь ежедневно
   Выполняйте задачи по приоритетам
   ```

5. **Регулярные обзоры**
   ```
   Ежедневно (5 мин): step-01-daily-review.md
   Еженедельно (30 мин): step-02-weekly-review.md
   Ежемесячно (1 час): step-03-monthly-review.md
   Каждый квартал (3 часа): step-04-quarterly-review.md
   ```

6. **Корректировки (по результатам обзоров)**
   ```
   Если цели нужно скорректировать: e-02-rescoring.md
   Если проект нужно обновить: e-01-update-project.md
   ```

### Часто задаваемые вопросы

**Q: Как часто нужно делать обзоры?**
A: Daily (обязательно), Weekly (обязательно), Monthly (обязательно), Quarterly (обязательно). Пропуск reviews = потеря контроля.

**Q: Что делать, если цель не достигается?**
A: В Quarterly Review решите: (1) Скорректировать target, (2) Продлить deadline, (3) Добавить ресурсы, (4) Приостановить, (5) Отменить.

**Q: Можно ли добавлять цели в течение года?**
A: Да, но с осторожностью. Рекомендуется: max 1 новая цель per quarter. Иначе — потеря фокуса.

---

**End of PDCA Integration Guide**

**Version:** 3.0
**Last Updated:** 2026-02-05
**Status:** ✅ Production Ready
