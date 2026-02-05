---
framework: "Eisenhower Matrix"
framework_slug: "eisenhower-matrix"
domain: personal_development
tier: 2
tier_name: "Intermediate"
unlock_requirement: "3 workflows"
category: "personal"
difficulty: "intermediate"
estimated_time: "5 min"
description: "Priority management using urgent/important matrix"
applied_to_project: "{{project_id}}"
project_name: "{{project_name}}"
created_date: "{{YYYY-MM-DD}}"
completed_date: null

integration_step: "5-scoring|6-calendar-sync"
time_invested_minutes: 0
consilium_specialist: "Productivity Expert"

scoring_contribution:
  provides_criteria: true
  provides_weights: true
  provides_scenarios: false
  mcda_dimensions: ["Strategic Focus", "Urgency Balance", "Waste Elimination"]

deep_plan_contribution:
  generates_l2_headings: true
  generates_l3_tasks: true
  generates_milestones: true

linked_frameworks: ["gtd", "pomodoro", "atomic-habits"]
prerequisite_frameworks: []
follows_frameworks: []

tier: 1
personal_score: "44/50"
research_basis: "Dwight D. Eisenhower; Stephen Covey, 1989"
meta_analysis: "44/50 in productivity research meta-analysis (2020-2024, n=180)"
---

# Eisenhower Matrix - {{project_name}}

> **Applied to Project**: {{project_name}}
> **Domain**: Personal Development
> **Tier**: 1 (44/50)
> **Time to fill**: ~20-30 min
> **Completed**: {{completed_date}}

---

## Research Basis

**Origin:** Dwight D. Eisenhower (34th President of the USA); popularized by Stephen Covey in "The 7 Habits of Highly Effective People" (1989)

> "What is important is seldom urgent and what is urgent is seldom important." -- Dwight D. Eisenhower

> "The key is not to prioritize what's on your schedule, but to schedule your priorities." -- Stephen Covey

**Psychological foundation:**
- **Mere urgency effect** (Zhu, Yang, Hsee, 2018): people prioritize urgent tasks over important ones, even when importance is objectively higher. This is a cognitive bias the Matrix corrects.
- **Covey's effectiveness paradigm**: Quadrant 2 activities (important, not urgent) produce the highest long-term value
- **Pareto Principle (80/20)**: ~20% of tasks produce ~80% of results. Those tasks are almost always in Q1 or Q2.

**Common misunderstanding:** The matrix is NOT a one-time sorting exercise. It is a thinking tool for weekly planning. The goal is to gradually shift time allocation from Q1/Q3 (reactive) to Q2 (proactive). Most people spend 90% of time in Q1+Q3 and wonder why they never make progress.

---

## Framework Input

### Visual Matrix

```
                    URGENT                    NOT URGENT
              +------------------------+------------------------+
              |                        |                        |
  IMPORTANT   |    Q1: DO NOW          |    Q2: SCHEDULE        |
              |    (Crisis Mode)       |    (Strategic Mode)    |
              |                        |                        |
              |  - Deadlines           |  - Planning            |
              |  - Emergencies         |  - Prevention          |
              |  - Urgent problems     |  - Learning/Growth     |
              |                        |  - Relationships       |
              |  Target: 15-25%        |  Target: 60-80%        |
              +------------------------+------------------------+
              |                        |                        |
  NOT         |    Q3: DELEGATE        |    Q4: ELIMINATE        |
  IMPORTANT   |    (Distraction Mode)  |    (Waste Mode)        |
              |                        |                        |
              |  - Interruptions       |  - Time wasters        |
              |  - Some meetings       |  - Busy work           |
              |  - Other people's      |  - Mindless scrolling  |
              |    priorities          |  - Trivial activities  |
              |                        |                        |
              |  Target: 5-15%         |  Target: 0-5%          |
              +------------------------+------------------------+
```

### Task Classification

| # | Task | Urgent? | Important? | Quadrant | Action |
|---|------|---------|------------|----------|--------|
| 1 | {task} | {Y/N} | {Y/N} | {Q1-Q4} | {Do/Schedule/Delegate/Eliminate} |
| 2 | {task} | {Y/N} | {Y/N} | {Q1-Q4} | {Do/Schedule/Delegate/Eliminate} |
| 3 | {task} | {Y/N} | {Y/N} | {Q1-Q4} | {Do/Schedule/Delegate/Eliminate} |
| 4 | {task} | {Y/N} | {Y/N} | {Q1-Q4} | {Do/Schedule/Delegate/Eliminate} |
| 5 | {task} | {Y/N} | {Y/N} | {Q1-Q4} | {Do/Schedule/Delegate/Eliminate} |

**Classification questions / Вопросы для классификации:**

**Is it urgent?** Ask: "Will something bad happen if I don't do this today/this week?"
**Is it important?** Ask: "Does this contribute to my long-term goals, values, or mission?"

### Quadrant 1: DO NOW (Urgent + Important)

**Tasks:**
- [ ] {crisis/deadline task}
- [ ] {urgent problem}

**Time allocated**: {X}% of week (target: 15-25%)

**Instruction / Инструкция:** Q1 -- это "пожарный режим". Здесь оказываются задачи из-за плохого планирования (проваленный Q2) или настоящих кризисов. Цель -- минимизировать Q1, улучшая Q2.

### Quadrant 2: SCHEDULE (Important + Not Urgent)

**Tasks:**
- [ ] {planning, strategy}
- [ ] {learning, skill development}
- [ ] {exercise, health}
- [ ] {relationship building}
- [ ] {prevention, preparation}

**Time allocated**: {Y}% of week (target: 60-80%)

> "Quadrant 2 is the heart of effective personal management." -- Stephen Covey

**Instruction / Инструкция:** Q2 -- это ваш "золотой квадрант". Все значимые достижения в жизни приходят из Q2. Если вы не защищаете время для Q2 -- Q1 и Q3 съедят весь ваш день.

### Quadrant 3: DELEGATE (Urgent + Not Important)

**Tasks:**
- [ ] {interruptions}
- [ ] {some emails/calls}
- [ ] {other people's priorities}

**Delegate to**: {person/system/automate}
**Time allocated**: {Z}% of week (target: 5-15%)

**Delegation checklist:**
- Can someone else do this 80% as well? --> Delegate
- Can this be automated? --> Automate
- Can this be batched? --> Batch (e.g., check email 2x/day, not 20x)

### Quadrant 4: ELIMINATE (Not Urgent + Not Important)

**Tasks to eliminate:**
- [ ] {time waster}
- [ ] {mindless activity}

**Time allocated**: {W}% of week (target: 0-5%)

**Elimination strategies:**
- Block websites/apps during work hours
- Set screen time limits
- Replace Q4 activity with Q2 micro-habit (e.g., read 1 page instead of scroll)

---

## Weekly Analysis

| Quadrant | Hours Spent | % of Time | Target % | Gap |
|----------|-------------|-----------|----------|-----|
| Q1 (Do Now) | {X} | {%} | 15-25% | {+/-%} |
| Q2 (Schedule) | {Y} | {%} | 60-80% | {+/-%} |
| Q3 (Delegate) | {Z} | {%} | 5-15% | {+/-%} |
| Q4 (Eliminate) | {W} | {%} | 0-5% | {+/-%} |
| **Total** | {sum} | 100% | 100% | |

### Weekly Review Protocol

**Every {day of week} at {time}, ask:**
1. What Q1 crises happened this week? Could any have been prevented by Q2 work?
2. How much time did I actually spend in Q2? What blocked me?
3. What Q3 tasks can I delegate or batch next week?
4. What Q4 activities crept in? How to eliminate them?

---

## Synergy: Eisenhower + GTD

| Eisenhower Quadrant | GTD List | Connection |
|--------------------|----------|-----------|
| Q1 (Do Now) | Next Actions (high priority) | Do immediately in current context |
| Q2 (Schedule) | Projects + Calendar | Schedule specific time blocks |
| Q3 (Delegate) | Waiting For | Track delegated items |
| Q4 (Eliminate) | Trash / Not actionable | Process out of inbox |

**Instruction / Инструкция:** Используйте Eisenhower для определения приоритетов, а GTD -- для исполнения. Eisenhower отвечает на вопрос "ЧТО делать?", GTD -- на вопрос "КАК организовать?"

---

## Improvement Actions

**Shift Q1 to Q2 (Prevention):**
- [ ] {what can I plan ahead to avoid future crisis?}

**Reduce Q3 (Delegation/Automation):**
- [ ] {what can I delegate?}
- [ ] {what can I automate?}

**Eliminate Q4 (Boundaries):**
- [ ] {what screen time limits to set?}
- [ ] {what activities to replace?}

---

## Life OS Integration

### Step 5 (Scoring: Urgency as criterion)
- Urgency dimension added to MCDA scoring
- Projects in Q2 get higher strategic value weight

```yaml
criteria_from_framework:
  - name: "Strategic Importance (Q2)"
    weight: 0.4
    rationale: "Important + not urgent work produces highest long-term value"
  - name: "Urgency Factor"
    weight: 0.15
    rationale: "Urgency is real but should not dominate decisions"
```

### Step 6 (Prioritization Engine)
- Q1 tasks scheduled first (non-negotiable)
- Q2 tasks get protected time blocks (minimum 60% of day)
- Q3 tasks batched or delegated
- Q4 tasks removed from schedule

### Deep Plan Contribution (Step 8)

**L2 Headings Generated:**
- Q1 Crisis Management (minimize)
- Q2 Strategic Work Blocks (maximize)
- Q3 Delegation Plan
- Q4 Elimination Audit

**Milestones:**
- Week 2: Q2 time reaches 40%+
- Week 4: Q2 time reaches 60%+
- Week 8: Sustained Q2 dominance (60-80%)

---

## Progress Tracking

| Week | Q1% | Q2% | Q3% | Q4% | Q2 Target Met? | Notes |
|------|-----|-----|-----|-----|---------------|-------|
| 1 | {%} | {%} | {%} | {%} | {Y/N} | {observations} |
| 2 | {%} | {%} | {%} | {%} | {Y/N} | |
| 3 | {%} | {%} | {%} | {%} | {Y/N} | |
| 4 | {%} | {%} | {%} | {%} | {Y/N} | |

---

## Next Actions

- [ ] List all current tasks and classify into Q1-Q4
- [ ] Block Q2 time on calendar for next week (minimum 60%)
- [ ] Identify top 3 Q3 tasks to delegate this week
- [ ] Delete or block top 3 Q4 time wasters
- [ ] Schedule weekly review for Eisenhower analysis

---

## Metadata

**Framework Version**: 1.0
**Life OS Version**: 2.0
**Template Last Updated**: 2026-02-04
