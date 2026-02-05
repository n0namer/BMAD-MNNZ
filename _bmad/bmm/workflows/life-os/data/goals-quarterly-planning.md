# Quarterly Planning & Goals Review

## Review Cadence

Goals from Step 00 should be reviewed quarterly using:

**File:** `steps-v/step-04-quarterly-review.md`

---

## What Gets Reviewed

1. **Progress tracking** - How much closer to each goal?
2. **Goal adjustment** - Do goals need updating?
3. **Alignment check** - Are current projects aligned?
4. **New goals** - Any emerging priorities?

---

## SMART Validation Checklist

For EACH goal, verify:

| Criterion | Question | Example (Good) | Example (Bad) |
|-----------|----------|----------------|---------------|
| **S**pecific | What exactly? | "Английский до B2 по CEFR" | "Выучить английский" |
| **M**easurable | How to measure? | "Пассивный доход ₽50K/месяц" | "Больше зарабатывать" |
| **A**chievable | Realistic? | "10K бег за 50 мин через 6 месяцев" | "Марафон за месяц" |
| **R**elevant | Why this goal? | Aligns with career/health/finance vision | Random, disconnected |
| **T**ime-bound | When? | "Через 1 год", "К декабрю 2025" | "Когда-нибудь" |

---

## Common Goal Refinement Patterns

### Vague → Specific

| Before | After |
|--------|-------|
| "Стать здоровее" | "Снизить вес до 75 кг, бегать 10K" |
| "Заработать больше" | "Пассивный доход ₽50K/месяц" |
| "Изучить программирование" | "Сделать 3 full-stack проекта на GitHub" |
| "Быть успешным" | "Запустить SaaS с ₽1M ARR" |

---

## Time Horizon Guidelines

### 1-Year Goals
- **Focus:** Concrete outcomes, clear metrics
- **Examples:** Certifications, revenue targets, fitness milestones
- **Weight in scoring:** 0.5 (highest priority)

### 3-Year Goals
- **Focus:** Strategic positioning, capability building
- **Examples:** Market position, team scale, expertise level
- **Weight in scoring:** 0.3 (strategic fit)

### 5-10 Year Goals
- **Focus:** Vision, purpose, legacy
- **Examples:** Financial independence, industry leadership, impact
- **Weight in scoring:** 0.2 (long-term alignment)

---

## Quarterly Review Protocol

**When to trigger:** Every 3 months or via `step-04-quarterly-review.md`

**Steps:**
1. Load goals from `{goalsFile}`
2. Compare current state vs. goal state
3. Calculate progress % for each goal
4. Identify blocked goals (why?)
5. Adjust goals if needed (update YAML + memory)
6. Archive outdated goals (move to `goals-archive-{quarter}.yaml`)

---

## Integration with Strategic Alignment (Step 05)

Every idea evaluated in Step 05 gets scored:

```
Alignment Score = Σ (impact_on_goal_i × weight_i)
```

Where:
- `impact_on_goal_i` = 0 (no impact), 0.5 (indirect), 1.0 (direct)
- `weight_i` = timeframe weight (0.5/0.3/0.2)

**Example:**
Idea: "Launch newsletter for entrepreneurs"
- 1-year goal "₽50K passive income" → impact 1.0 (direct) × 0.5 = 0.5
- 3-year goal "10K клиентов" → impact 1.0 (direct) × 0.3 = 0.3
- 5-10 year goal "Thought leader" → impact 1.0 (direct) × 0.2 = 0.2
- **Total Alignment Score:** 1.0 (perfect alignment)

---

**Reference:** Load this file for quarterly planning, goal review, or alignment scoring details.
