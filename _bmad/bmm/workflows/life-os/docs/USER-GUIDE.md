# Life OS User Guide v3.0

**Complete guide to using the Life & Business Operating System with AI specialists, portfolio management, and PDCA continuous improvement.**

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Goals Discovery (Step 00)](#goals-discovery-step-00)
3. [PDCA Planning (Step 06)](#pdca-planning-step-06)
4. [PDCA Review (Step 07)](#pdca-review-step-07)
5. [Ideas→Projects Lifecycle](#ideas-projects-lifecycle)
6. [Scripts Reference](#scripts-reference)
7. [Hooks Automation](#hooks-automation)
8. [Portfolio Dashboard](#portfolio-dashboard)
9. [Real-World Walkthroughs](#real-world-walkthroughs)
10. [Best Practices](#best-practices)
11. [Troubleshooting](#troubleshooting)

---

## Quick Start

### First-Time Setup (20-25 minutes)

1. **Start workflow:** Invoke Life OS in Claude
2. **Choose mode:** [C]reate - Build new idea or activate project
3. **Foundation Check:** System checks for existing foundation data
   - **If first time:** Run foundation steps (0.5-0.7) → ~10-12 minutes
   - **Goals Menu:** [C]ontinue with Goals Discovery (recommended) → +10-15 minutes
   - **Total first run:** ~20-25 minutes
4. **Collect ideas:** Share your idea (Step 01)
5. **Select track:** Quick (15 min) / Standard (60 min) / Deep (2-4 hours)
6. **Follow workflow:** System guides you step-by-step

### Subsequent Runs (0-15 minutes)

1. **Foundation exists?** System detects and offers [Skip] / [Update] → 0 minutes
2. **Goals exist?** If yes, optional PDCA Planning enabled → 0 minutes
3. **Jump to ideas:** Start at Step 01 immediately → 15-60+ minutes depending on track

---

## Goals Discovery (Step 00)

### Purpose

Define long-term strategic goals across all life spheres to enable:
- **Strategic Alignment** in scoring (Step 05) - Does idea align with your goals?
- **PDCA Planning** (Step 06) - Cascade annual goals to daily TODO lists
- **Trajectory Tracking** (Step 07) - Are you on track to achieve goals?

### When to Run

- **First time:** During foundation setup (optional but recommended for Deep Track)
- **Update:** When goals change (new year, major life change, quarterly review)
- **On demand:** Type `/update-goals` at any step

### What You'll Define

#### 1. Life Spheres (4-6 domains)
Default spheres:
- **Business:** Career, entrepreneurship, professional growth
- **Finance:** Wealth building, investments, financial security
- **Health:** Physical fitness, nutrition, mental health
- **Personal:** Relationships, hobbies, personal development
- **Home:** Living space, family, domestic life
- **Learning:** Skills acquisition, education, intellectual growth

You can customize spheres to match your priorities.

#### 2. Annual Goals (3-5 per sphere)
**Format:** OKR (Objective + Key Results)
- **Objective:** Qualitative, inspirational (e.g., "Build sustainable income streams")
- **Key Results:** Quantitative, measurable (e.g., "Reach $10K/month passive income by Dec 2026")
- **Target Date:** YYYY-MM-DD
- **Priority:** P0 (critical), P1 (important), P2 (nice-to-have)

#### 3. Quarterly Goals (2-3 per quarter)
**Focus:** What will you achieve THIS quarter toward annual goals?
- **Q1 (Jan-Mar):** Foundation building
- **Q2 (Apr-Jun):** Scaling and growth
- **Q3 (Jul-Sep):** Consolidation
- **Q4 (Oct-Dec):** Results and reflection

#### 4. Monthly Milestones (optional)
**Short-term checkpoints** to track progress within quarter

### Step-by-Step Walkthrough

**1. System asks: "Do you have existing goals defined?"**
- **[Y]es** → System loads goals.yaml and offers [Review] / [Update] / [Continue]
- **[N]o** → Proceed to discovery

**2. Define your life spheres (5 min)**
```
Which life domains are important to you?

Recommended:
[B]usiness [F]inance [H]ealth [P]ersonal [Ho]me [L]earning

Or define custom: [C]ustom

Your selection: B,F,H,P
```

**3. Set annual goals (5-10 min)**
For each sphere:
```
🎯 Business Goals for 2026

What do you want to achieve in Business this year?

Objective 1: [Enter qualitative goal]
  Example: "Build a profitable SaaS product"

Key Result 1: [Measurable metric]
  Example: "Reach $5K MRR by Dec 2026"

Key Result 2: [Measurable metric]
  Example: "100+ paying customers by Dec 2026"

Priority: [P0] Critical / [P1] Important / [P2] Nice-to-have

[Continue with next sphere...]
```

**4. Define quarterly focus (2-3 min)**
```
📅 Q1 2026 (Jan-Mar) Focus

Which annual goals will you prioritize THIS quarter?

Available annual goals:
1. Business: Build profitable SaaS ($5K MRR)
2. Finance: Build emergency fund ($20K)
3. Health: Lose 15 lbs and run 5K
4. Personal: Learn Spanish (B1 level)

Select 2-3 for Q1 focus: 1,2,3

Q1 Theme: Foundation building - Launch MVP, stabilize finances, kickstart health
```

**5. Review and confirm (1-2 min)**
```
✅ Goals Summary

Annual Goals: 12 across 4 spheres
Quarterly Focus (Q1): 3 goals
Estimated weekly effort: 15-20 hours

Breakdown by sphere:
- Business: 3 goals (P0=1, P1=2)
- Finance: 3 goals (P0=1, P1=1, P2=1)
- Health: 3 goals (P0=1, P1=2)
- Personal: 3 goals (P1=2, P2=1)

[Save] [Edit] [Cancel]
```

**6. System saves to goals.yaml**
```yaml
---
created: 2026-02-06T10:00:00Z
updated: 2026-02-06T10:00:00Z
version: 1.0
---

spheres:
  - business
  - finance
  - health
  - personal

goals:
  annual:
    - id: goal-2026-business-001
      title: "Build profitable SaaS product"
      sphere: business
      priority: P0
      target_date: 2026-12-31
      key_results:
        - kr1: "Reach $5K MRR"
          baseline: 0
          target: 5000
          unit: "USD/month"
        - kr2: "100+ paying customers"
          baseline: 0
          target: 100
          unit: "customers"

  quarterly:
    q1_2026:
      theme: "Foundation building"
      focus_goals:
        - goal-2026-business-001
        - goal-2026-finance-001
        - goal-2026-health-001
```

### Output

**File created:** `{bmb_creations_output_folder}/life-os/goals.yaml`

**What this enables:**
- Step 05 (Scoring): Strategic Alignment criterion (does idea support goals?)
- Step 06 (PDCA Planning): Cascade annual → quarterly → monthly → weekly → daily
- Step 07 (PDCA Review): Track trajectory toward quarterly and annual goals

### Time Investment

- **First time:** 10-15 minutes
- **Update:** 5-10 minutes (adjust goals, add new ones)
- **Review:** 2-3 minutes (check alignment during quarterly review)

### Skip or Defer?

**You can skip Goals Discovery if:**
- Running Quick Track (simplified scoring without strategic alignment)
- Want to evaluate idea first before defining long-term goals
- Conducting batch scoring (compare 10+ ideas, define goals later)

**Recommendation:** Define goals for Deep Track or when making high-stakes decisions ($10K+ investment, multi-month projects).

---

## PDCA Planning (Step 06)

### Purpose

Generate cascading goal hierarchy from strategic goals (goals.yaml) to daily TODO lists:
- **Year Plan (L1):** Annual goals, key results, quarterly breakdown
- **Quarter Plan (L2):** OKRs, monthly milestones, focus theme
- **Month Plan (L3):** Monthly goals, weekly breakdown, key events
- **Week Plan (L4):** Weekly goals, daily tasks, priorities (P0/P1/P2)
- **Day Plan (L5):** TODO list, time-blocking, energy management

**Principle:** Goals are useless without execution plans. PDCA Planning bridges strategy and execution.

### When to Run

- **After goals defined:** First time after Step 00 (Goals Discovery)
- **Weekly:** Update week plan every Sunday
- **Monthly:** Update month plan last Sunday of month
- **Quarterly:** Update quarter plan end of quarter
- **Annually:** Update year plan end of year

### Prerequisites

**CRITICAL:** goals.yaml must exist. If not, system prompts:
```
❌ Долгосрочные цели не определены

PDCA Planning требует стратегических целей для каскадирования.

💡 Что дальше?
[C]reate - Определить цели сейчас (~10-15 мин через Step 00)
[S]kip - Пропустить PDCA Planning (⚠️ не рекомендуется)
[Q]uit - Выйти из workflow
```

### Cascading Logic

**Top-Down Goal Decomposition:**
```
Annual Goal: "Reach $5K MRR by Dec 2026"
  ↓
Quarterly Goal (Q1): "Launch MVP and reach $1K MRR by Mar 2026"
  ↓
Monthly Goal (Feb): "Complete MVP development and onboard 10 beta users"
  ↓
Weekly Goal (Week 6): "Finish authentication module and write docs"
  ↓
Daily Task (Feb 6): "Implement OAuth2 integration (2 hours)"
```

**Each level links to parent:**
- Day plan links to Week plan
- Week plan links to Month plan
- Month plan links to Quarter plan
- Quarter plan links to Year plan
- Year plan links to goals.yaml

### Step-by-Step Walkthrough

**1. Validate goals foundation (1 min)**
```
✅ Долгосрочные цели найдены

📊 Структура целей:
- Год (2026): 12 целей
- Квартал (q1-2026): 3 цели
- Сфер жизни: 4
- Последнее обновление: 2026-02-06

Топ-3 годовых целей:
1. goal-2026-business-001: Build profitable SaaS product
2. goal-2026-finance-001: Build emergency fund $20K
3. goal-2026-health-001: Lose 15 lbs and run 5K

💡 Готовы каскадировать в планы?
[Y]es [R]eview [U]pdate [Q]uit
```

**2. PDCA hierarchy overview (1 min)**
```
🎯 PDCA Каскадирование Целей

Система создаст 5 уровней планов:

L1: Годовой план (year-2026.yaml)
L2: Квартальный план (q1-2026.yaml)
L3: Месячный план (month-2026-02.yaml)
L4: Недельный план (week-2026-W06.yaml)
L5: Дневной план (day-2026-02-06.yaml)

⏱️ Время генерации: ~5-10 минут
💾 Хранение: life-os/data/pdca/

Продолжить? [Y/N]
```

**3. Generate Year Plan (L1) - 2 min**
```
📄 Генерация L1: Годовой план

✅ year-2026.yaml создан
   - Стратегические цели: 12
   - Ключевые результаты: 28
   - Квартальное распределение: готово

📊 Годовой фокус:
   - Q1: Foundation (MVP + finances + health kickstart)
   - Q2: Scale (Growth + investment + fitness consistency)
   - Q3: Consolidate (Profitability + wealth + peak fitness)
   - Q4: Results (Year-end goals + reflection)
```

**4. Generate Quarter Plan (L2) - 2 min**
```
📄 Генерация L2: Квартальный план

✅ q1-2026.yaml создан
   - OKRs: 3
   - Месячные вехи: 9 (3 per month)
   - Связи с годовыми целями: 3

🎯 Фокус квартала: Foundation building
```

**5. Generate Month Plan (L3) - 2 min**
```
📄 Генерация L3: Месячный план

✅ month-2026-02.yaml создан
   - Месячные цели: 3
   - Недельное разбиение: 4 недели
   - Ключевые события: 2 (deadline, review)

🗓️ Фокус месяца: MVP completion and beta testing
```

**6. Generate Week Plan (L4) - 2 min**
```
📄 Генерация L4: Недельный план

✅ week-2026-W06.yaml создан
   - Недельные цели: 5
   - Дневное разбиение: 7 дней
   - Приоритеты: P0=2, P1=2, P2=1

⏰ Фокус недели: Authentication module + documentation
⚠️ Overcommitted: No (18h planned, 20h available)
```

**7. Generate Day Plan (L5) - 2 min**
```
📄 Генерация L5: Дневной план

✅ day-2026-02-06.yaml создан
   - TODO задачи: 4
   - Time-blocking: enabled
   - Энергетический баланс: balanced

✅ Готово к выполнению!
```

**8. Hierarchy validation (30 seconds)**
```
🔍 Проверка PDCA иерархии

Связи (linkages):
✅ Year → Quarter: OK
✅ Quarter → Month: OK
✅ Month → Week: OK
✅ Week → Day: OK

Покрытие целей:
✅ Годовые цели: 12/12 в планах (100%)
✅ Квартальные OKRs: 3/3 в планах (100%)

Каскадирование:
✅ Все дневные задачи связаны с недельными целями
✅ Все недельные цели связаны с месячными
✅ Все месячные связаны с квартальными OKRs
✅ Все OKRs связаны с годовыми целями

💡 Traceability: Каждая дневная задача прослеживается до годовой цели
```

**9. Dashboard generation (1 min)**
```
📊 PDCA Planning Dashboard

Сгенерированные файлы:
✅ year-2026.yaml (годовой план)
✅ q1-2026.yaml (квартальный план)
✅ month-2026-02.yaml (месячный план)
✅ week-2026-W06.yaml (недельный план)
✅ day-2026-02-06.yaml (дневной план)
📊 dashboard.md (сводная панель)

Текущий фокус:
- 📅 Сегодня (2026-02-06): Implement OAuth2 integration
- 📆 Эта неделя (W06): Authentication module + docs
- 🗓️ Этот месяц (Feb): MVP completion
- 📊 Этот квартал (Q1): Foundation building
- 🎯 Этот год (2026): Build profitable SaaS ($5K MRR)

Следующие шаги:
1. Выполнить задачи из day-2026-02-06.yaml
2. Вечерний обзор (Step 07: PDCA Review)
3. Еженедельный ретро в воскресенье
```

### File Structure

**Location:** `{bmb_creations_output_folder}/life-os/data/pdca/`

```
pdca/
├── year-2026.yaml               # L1: Annual plan
├── q1-2026.yaml                 # L2: Q1 plan
├── q2-2026.yaml                 # L2: Q2 plan (created at Q1 end)
├── q3-2026.yaml
├── q4-2026.yaml
├── month-2026-01.yaml           # L3: Monthly plans
├── month-2026-02.yaml
├── month-2026-03.yaml
├── week-2026-W01.yaml           # L4: Weekly plans
├── week-2026-W02.yaml
├── week-2026-W06.yaml
├── day-2026-01-01.yaml          # L5: Daily plans
├── day-2026-01-02.yaml
├── day-2026-02-06.yaml
└── dashboard.md                 # Consolidated view
```

### Linkage Pattern

**Complete traceability from year to day:**
```
goals.yaml
  ↓ linked_to
year-2026.yaml
  ↓ linked_to
q1-2026.yaml
  ↓ linked_to
month-2026-02.yaml
  ↓ linked_to
week-2026-W06.yaml
  ↓ linked_to
day-2026-02-06.yaml
```

**Every daily task traces back to annual goal**, ensuring strategic alignment at all levels.

### Example: Daily TODO List

**day-2026-02-06.yaml:**
```yaml
---
plan_type: daily
date: 2026-02-06
day_of_week: Thursday
week: 2026-W06
created: 2026-02-06T08:00:00Z
status: active
linked_to: week-2026-W06.yaml
---

# Daily Plan 2026-02-06

## Day Focus
Complete OAuth2 integration for authentication module

## Today's TODO List
- [ ] Implement OAuth2 provider configuration
      linked_to: week-goal-auth-module
      priority: P0
      estimated_time: 120 min
      energy_level: high
      time_block: 09:00-11:00

- [ ] Write OAuth2 integration tests
      linked_to: week-goal-auth-module
      priority: P0
      estimated_time: 90 min
      energy_level: high
      time_block: 11:15-12:45

- [ ] Document OAuth2 setup in README
      linked_to: week-goal-documentation
      priority: P1
      estimated_time: 60 min
      energy_level: medium
      time_block: 14:00-15:00

- [ ] Review PR from teammate
      linked_to: week-goal-code-review
      priority: P1
      estimated_time: 30 min
      energy_level: low
      time_block: 16:00-16:30

## Time Blocks
08:00-09:00: Morning routine + planning
09:00-11:00: OAuth2 implementation (P0)
11:00-11:15: Break
11:15-12:45: OAuth2 tests (P0)
12:45-14:00: Lunch
14:00-15:00: Documentation (P1)
15:00-15:15: Break
15:15-16:00: Buffer time
16:00-16:30: PR review (P1)
16:30+: EOD wrap-up

## Energy Management
- High energy tasks: OAuth2 implementation, tests
- Medium energy tasks: Documentation
- Low energy tasks: PR review, admin

## Success Criteria
- Minimum viable: P0 tasks completed (OAuth2 working)
- Good day: P0 + P1 completed (OAuth2 + docs)
- Exceptional day: All tasks + buffer time used productively
```

**Trace to annual goal:**
```
Daily task: "Implement OAuth2 integration"
  ↓ linked to
Weekly goal: "Complete authentication module"
  ↓ linked to
Monthly goal: "Finish MVP development"
  ↓ linked to
Quarterly OKR: "Launch MVP and reach $1K MRR"
  ↓ linked to
Annual goal: "Build profitable SaaS product ($5K MRR)"
```

### Time Estimates

- **Full generation (all 5 levels):** 5-10 minutes (first time)
- **Update week plan:** 2-3 minutes (every Sunday)
- **Update day plan:** 1-2 minutes (every morning)
- **Update month plan:** 5 minutes (monthly)
- **Update quarter plan:** 10-15 minutes (quarterly)

### Best Practices

**1. Review and update weekly (Sunday evening)**
- Load current week plan
- Check progress (% completion per goal)
- Generate next week plan based on trajectory

**2. Daily planning (morning routine)**
- Load today's plan from week plan
- Adjust time blocks based on actual availability
- Prioritize P0 tasks first

**3. Monthly review (last Sunday of month)**
- Review all 4 weekly velocities
- Calculate trajectory toward quarterly goal
- Adjust scope if behind schedule

**4. Quarterly replanning (end of quarter)**
- Review OKR achievement (%)
- Define next quarter OKRs
- Update annual plan if strategic pivots needed

---

## PDCA Review (Step 07)

### Purpose

Run systematic reviews across 4 cadences to ensure:
- **Progress tracking:** Are you on track to goals?
- **Early drift detection:** Velocity drops, chronic blockers
- **Course correction:** Adjust priorities based on data

**PDCA Cycle:**
- **Plan:** Set goals (Step 00, Step 06)
- **Do:** Execute tasks (daily work)
- **Check:** Review progress (Step 07)
- **Act:** Adjust plans (Step 07, back to Step 06)

### 4 Review Cadences

| Cadence | Duration | When | Purpose | Key Outputs |
|---------|----------|------|---------|-------------|
| **Daily** | 5 min | End of day (17:00-19:00) | Quick signals: done/blocked/learned | Daily standup summary |
| **Weekly** | 30 min | Sunday evening | Progress to weekly goals, velocity | Weekly review + velocity metrics |
| **Monthly** | 1 hour | Last Sunday of month | Trajectory to quarterly goals | Monthly trend report + adjustments |
| **Quarterly** | 2 hours | End of quarter | Quarter OKR achievement, replanning | Quarterly retrospective + next OKRs |

**Design Principle:** Each level builds on previous. Daily feeds Weekly, Weekly feeds Monthly, Monthly feeds Quarterly.

### Daily Review (5 min)

**When:** End of workday (17:00-19:00)

**3 Quick Questions:**
1. "What did you complete today?"
2. "Any blockers right now?"
3. "One quick learning from today?"

**Velocity Signal:**
- ✅ **On track:** 1+ items done, no high-severity blockers
- ⚠️ **Slipped:** 0 items done but made progress, medium blockers
- 🚨 **Blocked:** 0 progress, high-severity blocker active

**Auto-Adjustment:**
- ✅ On track: "Great! Tomorrow's top priority: [next item]"
- ⚠️ Slipped: "Let's adjust: focus on [highest priority incomplete]"
- 🚨 Blocked: "Action needed: resolve [blocker] first thing tomorrow"

**Chronic Blocker Detection:**
If same blocker active >3 days:
```
⚠️ Chronic Blocker Detected
"[Blocker name]" has been active for 3+ days.

Recommended actions:
1. Escalate to external owner
2. Find workaround path
3. De-prioritize blocked work

What would you like to do?
```

**Output:** `{reviewFolder}/daily/2026-02-06.md`

### Weekly Review (30 min)

**When:** Sunday evening (weekly close-out)

**4 Questions:**
1. "What were your key accomplishments this week?"
2. "Progress on each weekly goal (estimate %)?"
3. "What didn't get done that was planned?"
4. "What surprised you this week?"

**Velocity Calculation:**
```
Weekly Velocity = (Sum of goal completion %) / (Number of goals) * 100

Example:
- Goal 1: 75%
- Goal 2: 50%
- Goal 3: 100%
- Velocity = (75 + 50 + 100) / 3 = 75%
```

**Velocity Rating:**
- ✅ **Healthy:** 70-100% (on track)
- ⚠️ **Slipping:** 50-69% (minor course correction needed)
- 🚨 **Critical:** 0-49% (major adjustment required)

**Trend Detection:**
Compare to last week:
- This week 75% vs Last week 85% = -10% drop
- Flag if drop >15%: "⚠️ Velocity drop detected"

**Adjustments:**

**If ✅ Healthy (70-100%):**
```
Great week! Velocity is strong.

For next week:
1. Continue current approach
2. Consider stretch goal (if capacity allows)
3. Top 3 priorities: [ask user to define]
```

**If ⚠️ Slipping (50-69%):**
```
⚠️ Velocity drop detected (75% this week vs 85% last week).

Recommended adjustments for next week:
1. Reduce scope: Focus on 2 high-priority goals instead of 3
2. Address blockers: [list chronic blockers]
3. Protect focus time: Reduce context switching
```

**If 🚨 Critical (0-49%):**
```
🚨 Critical velocity alert (45%).

This requires course correction. Options:
1. Pause & Triage: Review all active projects, pause lowest priority
2. Scope Cut: Reduce each goal to MVP only
3. External Help: Delegate or outsource blocked tasks
4. Strategic Pivot: Re-evaluate if goals still aligned
```

**Output:** `{reviewFolder}/weekly/2026-W06.md`

### Monthly Review (1 hour)

**When:** Last Sunday of each month

**4 Questions:**
1. "What were your biggest wins this month?"
2. "Progress on each monthly goal (estimate %)?"
3. "What patterns do you notice over the last 4 weeks?"
4. "What should change next month?"

**4-Week Velocity Trend:**
```
Week 1: ████████████ 75%
Week 2: ██████████ 65%
Week 3: ██████████████ 85%
Week 4: ████████████ 70%

Trend: Stable
Average: 74%
```

**Trend Classification:**
- **Declining:** Week 4 < Week 1 by >10%
- **Stable:** Week 4 within ±10% of Week 1
- **Improving:** Week 4 > Week 1 by >10%

**Quarterly Goal Trajectory:**
```
Quarterly Goal 1: 70% actual vs 67% expected (Month 2 of 3) = ✅ On track
Quarterly Goal 2: 50% actual vs 67% expected = ⚠️ Behind (-17%)
Quarterly Goal 3: 85% actual vs 67% expected = 🚀 Ahead (+18%)
```

**Blocker Patterns:**
Identify recurring blockers (2+ weeks):
- "Dependency on external team" (3 occurrences)
- "Scope unclear" (2 occurrences)

**Capacity vs Commitment:**
```
Planned Hours: 80 total
Actual Hours: 96 total
Overcommitment Ratio: 1.2

Status: Over-committed (plan for 80% capacity next month)
```

**Goal Adjustments:**

For each quarterly goal behind:
```
Goal: Launch MVP and reach $1K MRR
Status: ⚠️ Behind by 17%

Options:
1. Increase Focus: Dedicate more time next month
2. Extend Timeline: Move deadline to Q2
3. Reduce Scope: Redefine to smaller MVP
4. Cancel: Accept this goal won't be achieved

Which option?
```

**Output:** `{reviewFolder}/monthly/2026-02.md`

### Quarterly Review (2 hours)

**When:** End of each quarter (last week of Mar, Jun, Sep, Dec)

**6 Questions:**
1. "What were your biggest achievements this quarter?"
2. "Final progress on each quarterly goal (actual %)?"
3. "Which goals did you fully achieve?"
4. "Which goals fell short? Why?"
5. "What major pivots or changes happened mid-quarter?"
6. "What should be your strategic focus next quarter?"

**3-Month Velocity Trend:**
```
Month 1: ████████████ 75%
Month 2: ██████████ 65%
Month 3: ██████████████ 78%

Trend: Stable
Quarterly Average: 73%
```

**OKR Achievement Analysis:**
```
Objective 1: Build profitable SaaS product
- KR1: Reach $1K MRR — Target: $1000 — Actual: $850 — 85% achievement
- KR2: 50 paying customers — Target: 50 — Actual: 42 — 84% achievement
Overall: 85% achievement

Status: ⚠️ Partially Achieved (70-89%)
```

**Goal Category Breakdown:**
```
Strategic goals: 85% avg achievement (3 goals)
Operational goals: 92% avg achievement (2 goals)
Experimental goals: 60% avg achievement (2 goals)
```

**Strategic Replanning:**

**Phase 1: Reflect (10 min)**
```
Before planning next quarter, let's reflect:

1. What surprised you most this quarter?
2. What would you do differently if you could repeat?
3. What capability or habit did you build?
4. What did you learn about your capacity?
```

**Phase 2: Adjust or Carry Forward Goals (15 min)**

For each unachieved goal (<90%):
```
Goal: Reach $1K MRR
Achievement: 85%

Options:
1. Carry Forward: Continue in Q2 (adjusted target $1.5K)
2. Pivot: Redefine based on learnings (focus retention)
3. Abandon: No longer strategic
4. Archive: Declare partial victory and move on

Decision: Carry Forward with adjusted target
```

**Phase 3: Define Next Quarter OKRs (15 min)**
```
What are your 2-3 Objectives for Q2?

Objective 1: Scale SaaS to profitability
  - KR1: Reach $3K MRR by Jun 2026 (70% confidence)
  - KR2: 150 paying customers by Jun 2026 (70% confidence)
  - KR3: Reduce churn to <5% monthly (80% confidence)

Objective 2: Build investment portfolio
  - KR1: Invest $10K in index funds (90% confidence)
  - KR2: Establish automated investment plan (80% confidence)
```

**Output:** `{reviewFolder}/quarterly/Q1-2026.md`

### Review File Structure

```
data/reviews/
├── daily/
│   ├── 2026-02-01.md
│   ├── 2026-02-02.md
│   ├── 2026-02-03.md
│   └── 2026-02-06.md
├── weekly/
│   ├── 2026-W01.md
│   ├── 2026-W02.md
│   └── 2026-W06.md
├── monthly/
│   ├── 2026-01.md
│   └── 2026-02.md
└── quarterly/
    └── Q1-2026.md
```

### Auto-Trigger Prompts

**Life OS can auto-prompt reviews:**
- **Daily:** Prompt at 18:00 (EOD)
- **Weekly:** Prompt Sunday 19:00
- **Monthly:** Prompt last Sunday of month
- **Quarterly:** Prompt last week of quarter

Enable in hooks configuration.

### Best Practices

**1. Don't skip daily reviews**
- Takes only 5 minutes
- Catches blockers early (before they become chronic)
- Builds daily reflection habit

**2. Weekly is PRIMARY cadence**
- Most frequent substantive review
- Velocity tracking catches drift early
- 15-20 min weekly >>> 2 hours quarterly

**3. Always complete ACT phase**
- Review without action = documentation theater
- Every review must end with concrete adjustments
- If velocity drops >15%, adjust priorities immediately

**4. Track trends, not point-in-time**
- One bad week is noise, three bad weeks is signal
- Look for patterns in blockers
- Compare to baseline (not to perfection)

**5. Be honest in reflections**
- No one sees this except you
- Honest assessment enables better course correction
- Failure insights are as valuable as success insights

---

## Ideas→Projects Lifecycle

### Overview

**Critical Architectural Principle:** Ideas and Projects are separate entities with clear lifecycle transitions.

**Why separate?**
- **Ideas:** Raw input, evaluated, planned, archived
- **Projects:** Active work, tracked, completed/killed
- **Boundary:** Clear activation moment (PLANNED → ACTIVE)
- **Portfolio visibility:** See all ideas + all projects in one view

### Folder Structure

```
life-os/
├── 📥 ideas-bank/                    # БАНК ИДЕЙ (raw input)
│   ├── inbox/                        # 🆕 Новые (не оценены)
│   ├── evaluated/                    # ✅ Оценены (scored, ranked)
│   ├── planned/                      # 📋 План готов (deep plan done)
│   └── archive/
│       ├── rejected/                 # NO-GO решения (score <6.5)
│       ├── postponed/                # WAIT решения (score 6.5-7.5)
│       └── activated/                # Стали проектами (moved to projects-bank)
│
├── 🚀 projects-bank/                 # БАНК ПРОЕКТОВ (active work)
│   ├── active/                       # 🔥 В работе (IN_PROGRESS)
│   │   └── project-001-katana/
│   │       ├── project.md           # Main file (status, progress, metrics)
│   │       ├── plan.md              # Plan copied from idea
│   │       ├── tasks/               # Task breakdown
│   │       ├── artifacts/           # Deliverables
│   │       └── logs/                # Change history
│   ├── completed/                    # ✅ Завершённые (SUCCESS)
│   │   └── project-002-dashboard/
│   │       ├── project.md
│   │       ├── plan.md
│   │       └── retrospective.md     # Mandatory! (lessons learned)
│   └── killed/                       # ❌ Остановленные (STOPPED)
│       └── project-003-experiment/
│           ├── project.md
│           └── kill-analysis.md     # Mandatory! (why stopped, salvageable parts)
```

### State Machine

```
[INBOX] → [EVALUATED] → [PLANNED] → [ACTIVE (PROJECT)] → [COMPLETED/KILLED]
            ↓              ↓              ↓
        [REJECTED]    [POSTPONED]    [ACTIVATED ARCHIVE]
```

**State Definitions:**

- **INBOX:** New idea submitted, not yet evaluated (location: `ideas-bank/inbox/`)
- **EVALUATED:** Step 05 (Scoring) complete, decision made (location: `ideas-bank/evaluated/` or `archive/rejected|postponed/`)
- **PLANNED:** Step 08 (Deep Plan) complete, ready to activate (location: `ideas-bank/planned/`)
- **ACTIVE:** User activated, project in progress (location: `projects-bank/active/`)
- **COMPLETED:** Project finished successfully (location: `projects-bank/completed/`)
- **KILLED:** Project stopped mid-execution (location: `projects-bank/killed/`)
- **REJECTED:** Idea scored too low (<6.5), archived (location: `ideas-bank/archive/rejected/`)
- **POSTPONED:** Idea deferred for later (6.5-7.5 score) (location: `ideas-bank/archive/postponed/`)

### Lifecycle Transitions

#### 1. INBOX → EVALUATED (Auto via hooks)

**Trigger:** Step 05 (Scoring) complete

**Action:** post-task hook automatically moves idea file from `inbox/` to `evaluated/` or `archive/rejected|postponed/`

**Logic:**
```bash
if score >= 7.5:
  mv ideas-bank/inbox/idea-XXX.md → ideas-bank/evaluated/
elif score >= 6.5:
  mv ideas-bank/inbox/idea-XXX.md → ideas-bank/archive/postponed/
else:
  mv ideas-bank/inbox/idea-XXX.md → ideas-bank/archive/rejected/
```

**User Action:** None (automatic)

#### 2. EVALUATED → PLANNED (Auto via hooks)

**Trigger:** Step 08 (Deep Plan) complete

**Action:** post-task hook automatically moves idea file from `evaluated/` to `planned/`

**Logic:**
```bash
if deep_plan_complete:
  mv ideas-bank/evaluated/idea-XXX.md → ideas-bank/planned/
```

**User Action:** None (automatic)

#### 3. PLANNED → ACTIVE (Manual via script)

**Trigger:** User decides to activate project

**Action:** Run activation script

**Script:** `create-project-from-idea.sh` (Unix) or `create-project-from-idea.ps1` (Windows)

**What it does:**
1. **Create project folder:** `projects-bank/active/project-NNN-name/`
2. **Copy plan:** `idea-XXX.md` → `project-NNN-name/plan.md`
3. **Generate project.md:** Main project file with metadata
4. **Add origin link:** `origin-idea: idea-XXX` in project.md
5. **Archive idea:** Move to `ideas-bank/archive/activated/idea-XXX-activated-20260206.md`
6. **Add project link:** `became_project: project-NNN` in archived idea
7. **Update portfolio.md:** Increment active projects count

**Example:**
```bash
# Unix
./scripts/create-project-from-idea.sh idea-007-finance-katana-vectorbt.md

# Windows
.\scripts\create-project-from-idea.ps1 -IdeaFile "idea-007-finance-katana-vectorbt.md"
```

**Output:**
```
✅ Project activated!

Created: projects-bank/active/project-007-katana/
  - project.md (status: IN_PROGRESS)
  - plan.md (copied from idea)
  - tasks/ (empty, ready for breakdown)
  - artifacts/ (empty)
  - logs/ (empty)

Archived idea: ideas-bank/archive/activated/idea-007-finance-katana-activated-20260206.md

Next steps:
1. Break down plan.md into tasks
2. Start execution (Step X-01: Kickoff)
3. Weekly progress tracking (Step X-02: Pulse)
```

**User Action:** Manual (requires intentional decision to start work)

#### 4. ACTIVE → COMPLETED (Manual via script)

**Trigger:** Project finished successfully

**Action:** Run completion script

**Script:** `complete-project.sh` (Unix) or `complete-project.ps1` (Windows)

**What it does:**
1. **Generate retrospective.md:** What worked? What didn't? Lessons learned?
2. **Update project.md:** status: COMPLETED, completion_date
3. **Move folder:** `projects-bank/active/project-NNN/` → `projects-bank/completed/project-NNN/`
4. **Update portfolio.md:** Decrement active, increment completed
5. **Save to memory:** Store learnings in global memory

**Example:**
```bash
# Unix
./scripts/complete-project.sh project-007-katana

# Windows
.\scripts\complete-project.ps1 -ProjectName "project-007-katana"
```

**Output:**
```
🎉 Project completed!

Moved: projects-bank/completed/project-007-katana/

Generated retrospective:
  - What worked: [your input]
  - What didn't: [your input]
  - Lessons learned: [your input]
  - Metrics achieved: [auto-filled]

Updated portfolio:
  - Active projects: 2 (was 3)
  - Completed projects: 5 (was 4)
  - Success rate: 83% (5 completed, 1 killed)
```

**User Action:** Manual (intentional completion ceremony)

#### 5. ACTIVE → KILLED (Manual via script)

**Trigger:** Project stopped mid-execution (X-04 pivot-or-kill decision)

**Action:** Run kill script

**Script:** `kill-project.sh` (Unix) or `kill-project.ps1` (Windows)

**What it does:**
1. **Generate kill-analysis.md:** Why stopped? What learned? Salvageable parts?
2. **Update project.md:** status: KILLED, kill_date, kill_reason
3. **Move folder:** `projects-bank/active/project-NNN/` → `projects-bank/killed/project-NNN/`
4. **Update portfolio.md:** Decrement active, increment killed, free WIP capacity
5. **Save to memory:** Store failure learnings (valuable for future decisions)

**Example:**
```bash
# Unix
./scripts/kill-project.sh project-003-experiment

# Windows
.\scripts\kill-project.ps1 -ProjectName "project-003-experiment"
```

**Output:**
```
🛑 Project killed

Moved: projects-bank/killed/project-003-experiment/

Generated kill-analysis:
  - Reason: [your input] (e.g., "Market validation failed")
  - What learned: [your input] (e.g., "Need customer interviews before building")
  - Salvageable: [your input] (e.g., "Auth module can be reused")
  - Time invested: 40 hours
  - Budget spent: $2,000

Updated portfolio:
  - Active projects: 2 (was 3)
  - Killed projects: 1 (was 0)
  - WIP capacity: 1 slot freed

💡 Failure is data. These learnings will inform future decisions.
```

**User Action:** Manual (requires honest reflection on failure)

### File Naming Conventions

**Ideas (files):**
- **Format:** `idea-{NNN}-{sphere}-{name}.md`
- **Example:** `idea-001-finance-katana-vectorbt.md`
- **Archived:** `idea-001-finance-katana-activated-20260206.md`

**Projects (folders):**
- **Format:** `project-{NNN}-{name}/`
- **Example:** `project-001-katana/`
- **Contents:**
  - `project.md` (main file, status, progress)
  - `plan.md` (copied from idea)
  - `tasks/` (task breakdown)
  - `artifacts/` (deliverables, docs, code)
  - `logs/` (change history, decisions)

### Portfolio Visibility

**portfolio.md shows:**
```markdown
# Life OS Portfolio Dashboard

Generated: 2026-02-06T10:00:00Z

## Status Summary

**Ideas Bank:**
- 📥 Inbox: 3 ideas (not evaluated)
- ✅ Evaluated: 5 ideas (scored, ranked)
- 📋 Planned: 2 ideas (ready to activate)
- 📁 Archive:
  - Rejected: 12 ideas (score <6.5)
  - Postponed: 8 ideas (deferred)
  - Activated: 7 ideas (became projects)

**Projects Bank:**
- 🔥 Active: 2 projects (IN_PROGRESS)
  - project-007-katana (finance, 30% complete)
  - project-009-dashboard (business, 60% complete)
- ✅ Completed: 5 projects (SUCCESS)
- ❌ Killed: 1 project (STOPPED)

**Capacity:**
- WIP Limit: 3 projects max
- Current WIP: 2 projects
- Available slots: 1

**Metrics:**
- Success rate: 83% (5 completed / 6 total)
- Avg project duration: 8 weeks
- Avg idea→project time: 3 days
```

### Best Practices

**1. Keep ideas and projects separate**
- Ideas are lightweight (1 file)
- Projects are heavyweight (folder with artifacts)
- Don't mix in same folder

**2. Archive everything (never delete)**
- Rejected ideas contain valuable context
- Killed projects contain failure learnings
- Activated ideas trace back to projects

**3. Intentional activation (PLANNED → ACTIVE)**
- Don't auto-activate (requires conscious decision)
- Run script manually (creates ceremony)
- Limit WIP (max 3 active projects recommended)

**4. Mandatory retrospectives**
- Completed: retrospective.md (successes + learnings)
- Killed: kill-analysis.md (failures + salvageable parts)
- Learnings feed into future decisions

**5. Traceability links**
- Project always links back to origin idea
- Archived idea always links forward to project
- Full audit trail from idea→project→outcome

---

## Scripts Reference

### Activation: create-project-from-idea

**Purpose:** Transform planned idea into active project

**When to use:** After Step 08 (Deep Plan) complete, ready to start execution

**Location:**
- Unix: `scripts/create-project-from-idea.sh`
- Windows: `scripts/create-project-from-idea.ps1`

**Usage:**
```bash
# Unix
./scripts/create-project-from-idea.sh idea-007-finance-katana-vectorbt.md

# Windows (PowerShell)
.\scripts\create-project-from-idea.ps1 -IdeaFile "idea-007-finance-katana-vectorbt.md"
```

**What it does:**
1. Validates idea file exists in `planned/`
2. Generates next project number (auto-increment)
3. Creates project folder structure
4. Copies plan from idea to `plan.md`
5. Generates `project.md` with metadata
6. Archives idea to `activated/`
7. Updates portfolio.md

**Output files:**
```
projects-bank/active/project-007-katana/
├── project.md
├── plan.md
├── tasks/ (empty)
├── artifacts/ (empty)
└── logs/ (empty)

ideas-bank/archive/activated/
└── idea-007-finance-katana-activated-20260206.md
```

**Parameters:**
- `IdeaFile` (required): Filename in `ideas-bank/planned/`
- `ProjectName` (optional): Custom project name (auto-generated from idea if not provided)

**Example output:**
```
✅ Project Activated!

Created: projects-bank/active/project-007-katana/
Origin idea: idea-007-finance-katana-vectorbt
Status: IN_PROGRESS
WIP: 3/3 (at capacity)

Next steps:
1. Break plan.md into tasks/
2. Run Step X-01 (Kickoff) to set milestones
3. Start weekly progress tracking
```

### Completion: complete-project

**Purpose:** Mark active project as successfully completed

**When to use:** When project finished, all success criteria met

**Location:**
- Unix: `scripts/complete-project.sh`
- Windows: `scripts/complete-project.ps1`

**Usage:**
```bash
# Unix
./scripts/complete-project.sh project-007-katana

# Windows (PowerShell)
.\scripts\complete-project.ps1 -ProjectName "project-007-katana"
```

**What it does:**
1. Validates project exists in `active/`
2. Prompts for retrospective inputs:
   - What worked well?
   - What didn't work?
   - Lessons learned?
   - Metrics achieved?
3. Generates `retrospective.md`
4. Updates `project.md` status to COMPLETED
5. Moves folder to `completed/`
6. Updates portfolio.md (decrement active, increment completed)
7. Frees WIP capacity
8. Saves learnings to global memory

**Retrospective prompts:**
```
🎉 Project Completion Ceremony

Let's reflect on project-007-katana...

1. What worked well? (3-5 items)
   > [User inputs]

2. What didn't work as expected? (2-3 items)
   > [User inputs]

3. What would you do differently next time? (2-3 insights)
   > [User inputs]

4. Key metrics achieved:
   - Original goal: Reach $1K MRR
   - Actual result: $1.2K MRR (120% of target)
   - Timeline: 8 weeks (planned: 10 weeks, 20% faster)
   - Budget: $500 (planned: $1000, 50% under budget)

5. Salvageable artifacts (for reuse in future projects):
   > [User lists code, docs, templates, frameworks]

Generating retrospective...
```

**Output:**
```
✅ Project completed!

Moved: projects-bank/completed/project-007-katana/

Files generated:
  - retrospective.md (lessons learned)
  - project.md (updated with completion date)

Portfolio updated:
  - Active projects: 2 (was 3)
  - Completed projects: 6 (was 5)
  - Success rate: 86% (6 completed, 1 killed)
  - WIP capacity: 1 slot freed

Learnings saved to global memory for future reference.
```

### Termination: kill-project

**Purpose:** Stop active project that's no longer viable

**When to use:** After X-04 (Pivot-or-Kill) decision, or when project blocked/irrelevant

**Location:**
- Unix: `scripts/kill-project.sh`
- Windows: `scripts/kill-project.ps1`

**Usage:**
```bash
# Unix
./scripts/kill-project.sh project-003-experiment

# Windows (PowerShell)
.\scripts\kill-project.ps1 -ProjectName "project-003-experiment"
```

**What it does:**
1. Validates project exists in `active/`
2. Prompts for kill analysis inputs:
   - Why stopped?
   - What learned?
   - Salvageable parts?
   - Time/budget invested?
3. Generates `kill-analysis.md`
4. Updates `project.md` status to KILLED
5. Moves folder to `killed/`
6. Updates portfolio.md (decrement active, increment killed)
7. Frees WIP capacity
8. Saves failure learnings to global memory

**Kill analysis prompts:**
```
🛑 Project Kill Analysis

Let's document why project-003-experiment stopped...

1. Primary reason for stopping: (select one)
   [M]arket validation failed
   [T]echnical blocker (unsolvable with current resources)
   [R]esource constraints (time/money exhausted)
   [S]trategic pivot (no longer aligned with goals)
   [O]ther (explain)

   > [User selects: M]

2. What did you learn from this project? (2-5 insights)
   > [User inputs]

3. What parts can be salvaged/reused? (code, frameworks, knowledge)
   > [User lists]

4. Investment summary:
   - Time invested: 40 hours
   - Budget spent: $2,000
   - Duration: 6 weeks

5. Would you attempt this again with more information? [Y/N]
   > [User inputs]

Generating kill-analysis...
```

**Output:**
```
🛑 Project killed

Moved: projects-bank/killed/project-003-experiment/

Files generated:
  - kill-analysis.md (why stopped, learnings, salvageable)
  - project.md (updated with kill date)

Portfolio updated:
  - Active projects: 2 (was 3)
  - Killed projects: 1 (was 0)
  - Kill rate: 14% (1 killed, 6 completed)
  - WIP capacity: 1 slot freed

💡 Failure is data. Learnings saved to global memory.

These insights will help avoid similar pitfalls in future projects.
```

### Archive: archive-idea

**Purpose:** Manually archive idea (reject or postpone)

**When to use:** User decides not to pursue idea without full workflow

**Location:**
- Unix: `scripts/archive-idea.sh`
- Windows: `scripts/archive-idea.ps1`

**Usage:**
```bash
# Unix
./scripts/archive-idea.sh idea-010-experiment.md reject

# Windows (PowerShell)
.\scripts\archive-idea.ps1 -IdeaFile "idea-010-experiment.md" -Reason "reject"
```

**Parameters:**
- `IdeaFile` (required): Filename in any ideas-bank folder
- `Reason` (required): `reject` or `postpone`

**What it does:**
1. Validates idea file exists
2. Moves to appropriate archive folder
3. Adds timestamp to filename
4. Updates portfolio.md counts

**Output:**
```
📁 Idea archived

Moved: ideas-bank/archive/rejected/idea-010-experiment-rejected-20260206.md

Reason: Not aligned with current priorities

Portfolio updated:
  - Inbox: 2 (was 3)
  - Rejected: 13 (was 12)
```

### Dashboard: dashboard

**Purpose:** Generate visual portfolio dashboard

**When to use:** Anytime you want portfolio overview

**Location:**
- Unix: `scripts/dashboard.sh`
- Windows: `scripts/dashboard.ps1`

**Usage:**
```bash
# Unix
./scripts/dashboard.sh

# Windows (PowerShell)
.\scripts\dashboard.ps1
```

**What it does:**
1. Scans all ideas and projects
2. Calculates metrics
3. Generates `portfolio.md`
4. Displays summary in terminal

**Output:**
```
📊 Life OS Portfolio Dashboard

Generated: 2026-02-06T10:30:00Z

IDEAS BANK:
  📥 Inbox: 3 ideas
  ✅ Evaluated: 5 ideas
  📋 Planned: 2 ideas
  📁 Rejected: 12 ideas
  📁 Postponed: 8 ideas
  📁 Activated: 7 ideas

PROJECTS BANK:
  🔥 Active: 2 projects (WIP 2/3)
    - project-007-katana (30% complete, on track)
    - project-009-dashboard (60% complete, on track)
  ✅ Completed: 6 projects
  ❌ Killed: 1 project

METRICS:
  Success rate: 86% (6 completed / 7 total)
  Avg completion time: 8.2 weeks
  Avg idea→project time: 3 days
  Active velocity: 75% (healthy)

FILE: portfolio.md updated
```

---

## Hooks Automation

### Overview

**Hooks = Event-driven automation** that runs after specific actions:
- **post-task:** After step completes, automatically move files, update portfolio
- **post-edit:** After file edited, extract patterns, save to memory
- **session-end:** Save session state, consolidate memory

**Goal:** Minimize manual work, enforce lifecycle rules, maintain data consistency

### Configured Hooks

**Location:** `data/hooks-config.yaml`

```yaml
hooks:
  post_task:
    enabled: true
    actions:
      - name: "move_evaluated_ideas"
        trigger: "step-05-scoring complete"
        action: |
          if score >= 7.5:
            mv ideas-bank/inbox/ → evaluated/
          elif score >= 6.5:
            mv ideas-bank/inbox/ → archive/postponed/
          else:
            mv ideas-bank/inbox/ → archive/rejected/

      - name: "move_planned_ideas"
        trigger: "step-08-deep-plan complete"
        action: |
          mv ideas-bank/evaluated/ → planned/

      - name: "update_portfolio"
        trigger: "any lifecycle transition"
        action: |
          recalculate counts in portfolio.md

  post_edit:
    enabled: true
    actions:
      - name: "extract_patterns"
        trigger: "any .md file edited"
        action: |
          extract code patterns, save to memory

      - name: "backup_changes"
        trigger: "project file edited"
        action: |
          append change to logs/

  session_end:
    enabled: true
    actions:
      - name: "save_session_state"
        action: |
          export metrics, save to memory

      - name: "consolidate_memory"
        action: |
          deduplicate, optimize HNSW index
```

### How Hooks Work

**Example: Step 05 (Scoring) completes**

1. **User completes Step 05**
2. **System triggers post-task hook:**
   ```
   Detected: step-05-scoring complete
   Idea: idea-007-finance-katana-vectorbt.md
   Score: 8.2
   ```

3. **Hook evaluates logic:**
   ```
   if score >= 7.5:  # True (8.2 >= 7.5)
     move to ideas-bank/evaluated/
   ```

4. **Hook executes:**
   ```
   Moving: ideas-bank/inbox/idea-007-finance-katana-vectorbt.md
        → ideas-bank/evaluated/idea-007-finance-katana-vectorbt.md

   ✅ Idea moved to evaluated/
   ```

5. **Hook updates portfolio:**
   ```
   Updating portfolio.md:
     - Inbox: 2 (was 3)
     - Evaluated: 6 (was 5)
   ```

6. **User sees notification:**
   ```
   🔄 Automated: Idea moved to evaluated/ (score 8.2)
   ```

**User action required:** None (fully automatic)

### Lifecycle Automation Matrix

| Event | Hook | Auto-Action | Manual Override |
|-------|------|-------------|-----------------|
| Step 05 complete (score 7.5+) | post-task | Move inbox → evaluated | No |
| Step 05 complete (score 6.5-7.5) | post-task | Move inbox → archive/postponed | Yes (can move to evaluated manually) |
| Step 05 complete (score <6.5) | post-task | Move inbox → archive/rejected | Yes (can move to evaluated manually) |
| Step 08 complete | post-task | Move evaluated → planned | No |
| Project activated (script) | - | Move planned → archive/activated | N/A (script-driven) |
| Project completed (script) | - | Move active → completed | N/A (script-driven) |
| Project killed (script) | - | Move active → killed | N/A (script-driven) |
| Any file edited | post-edit | Extract patterns, save to memory | No |
| Session ends | session-end | Export metrics, consolidate memory | No |

### Viewing Hook Logs

**Check what hooks did:**
```bash
# View hook execution log
cat .claude-flow/logs/hooks.log

# Recent hook actions (last 20)
tail -20 .claude-flow/logs/hooks.log
```

**Example log:**
```
2026-02-06T10:15:30Z [post-task] step-05-scoring complete
2026-02-06T10:15:31Z [post-task] idea-007 score: 8.2
2026-02-06T10:15:31Z [post-task] Moving: inbox/ → evaluated/
2026-02-06T10:15:32Z [post-task] Updated portfolio.md (inbox: 2, evaluated: 6)
2026-02-06T10:15:32Z [post-task] ✅ Success
```

### Disabling Hooks

**If you prefer manual control:**

Edit `data/hooks-config.yaml`:
```yaml
hooks:
  post_task:
    enabled: false  # Disable all post-task hooks
```

Or disable specific hook:
```yaml
hooks:
  post_task:
    enabled: true
    actions:
      - name: "move_evaluated_ideas"
        enabled: false  # Disable just this hook
```

**When to disable:**
- Testing workflow changes
- Batch processing (want to move files manually)
- Debugging lifecycle issues

---

## Portfolio Dashboard

### Overview

**portfolio.md = Single source of truth** for all ideas, projects, capacity, and metrics.

**Purpose:**
- **Visibility:** See all active work at a glance
- **Capacity management:** Track WIP limits (max 3 active projects recommended)
- **Metrics:** Success rate, velocity, bottlenecks
- **Decision support:** Should I activate another project? Which idea to prioritize?

**Location:** `{bmb_creations_output_folder}/life-os/portfolio.md`

**Updated by:** Hooks (automatic), scripts (on lifecycle transitions), manual edits

### Dashboard Structure

```markdown
# Life OS Portfolio Dashboard

Generated: 2026-02-06T10:00:00Z
Last updated: 2026-02-06T15:30:00Z (auto-refresh every step)

---

## 📊 STATUS SUMMARY

### Ideas Bank
| State | Count | Description |
|-------|-------|-------------|
| 📥 Inbox | 3 | New ideas (not evaluated) |
| ✅ Evaluated | 5 | Scored, ranked, ready for planning |
| 📋 Planned | 2 | Deep plan done, ready to activate |
| 📁 Rejected | 12 | Score <6.5, archived |
| 📁 Postponed | 8 | Score 6.5-7.5, deferred |
| 📁 Activated | 7 | Became active projects |

**Total Ideas:** 37 (lifetime)

### Projects Bank
| State | Count | Description |
|-------|-------|-------------|
| 🔥 Active | 2 | IN_PROGRESS (WIP 2/3) |
| ✅ Completed | 6 | Successfully finished |
| ❌ Killed | 1 | Stopped mid-execution |

**Total Projects:** 9 (7 activated from ideas, 2 direct imports)

---

## 🔥 ACTIVE PROJECTS (WIP 2/3)

### project-007-katana
- **Origin:** idea-007-finance-katana-vectorbt
- **Sphere:** Finance
- **Status:** IN_PROGRESS (30% complete)
- **Started:** 2026-01-15
- **Target completion:** 2026-03-15 (8 weeks)
- **Current week velocity:** 75% ✅ On track
- **Key milestone:** Complete backtesting engine (due 2026-02-10)
- **Blockers:** None
- **Next action:** Implement portfolio optimization module

### project-009-dashboard
- **Origin:** idea-009-business-analytics-dashboard
- **Sphere:** Business
- **Status:** IN_PROGRESS (60% complete)
- **Started:** 2026-01-20
- **Target completion:** 2026-02-20 (4 weeks)
- **Current week velocity:** 85% ✅ On track
- **Key milestone:** Launch MVP to 10 beta users (due 2026-02-15)
- **Blockers:** Waiting on API documentation (low severity, 2 days)
- **Next action:** Finish chart widgets

---

## 📋 READY TO ACTIVATE (Planned Ideas)

### idea-012-health-macro-tracker
- **Sphere:** Health
- **Score:** 8.5 (Strategic Alignment: 9, Impact: 9, Effort: 3)
- **Plan ready:** Yes (L1-L6 deep plan complete)
- **Estimated duration:** 6 weeks
- **Resource requirements:** 10 hours/week
- **Recommendation:** ✅ Activate when project-009 completes (1 WIP slot available)

### idea-015-personal-spanish-learning
- **Sphere:** Personal
- **Score:** 7.8 (Strategic Alignment: 8, Impact: 7, Effort: 4)
- **Plan ready:** Yes (L1-L3 plan complete)
- **Estimated duration:** 12 weeks
- **Resource requirements:** 5 hours/week
- **Recommendation:** ⏳ Wait for WIP slot (queue position: #2)

---

## 🎯 CAPACITY ANALYSIS

### WIP Limits
- **Maximum:** 3 projects (portfolio policy)
- **Current:** 2 projects active
- **Available:** 1 slot open
- **Recommendation:** ✅ Can activate 1 more project

### Weekly Time Budget
- **Total available:** 20 hours/week
- **Currently allocated:**
  - project-007-katana: 10 hours/week
  - project-009-dashboard: 8 hours/week
  - **Total:** 18 hours/week
- **Buffer:** 2 hours/week (10%)
- **Status:** ✅ Well-balanced (not overcommitted)

### Capacity Forecast (Next 4 Weeks)
- **Week 1:** project-009 completes → 1 slot + 8 hours freed
- **Week 2-4:** project-007 continues (10h/week)
- **Week 4:** Available capacity: 10 hours/week
- **Recommendation:** Can activate idea-012 (requires 10h/week)

---

## 📈 METRICS & TRENDS

### Success Metrics
- **Completion rate:** 86% (6 completed / 7 finished projects)
- **Kill rate:** 14% (1 killed / 7 finished projects)
- **Avg project duration:** 8.2 weeks (target: 8 weeks) ✅ On target
- **Avg idea→project time:** 3 days (time from planned → activated)

### Velocity Trends
- **Current week:** 75% avg across active projects ✅ Healthy
- **Last 4 weeks:** 80%, 75%, 70%, 75% (trend: Stable)
- **Monthly avg:** 75% ⚠️ Slightly below target (80%)

### Bottleneck Analysis
- **Chronic blockers:** 1 (API documentation waiting >3 days)
- **Most common blocker type:** External dependencies (60%)
- **Avg blocker resolution time:** 5 days
- **Recommendation:** Build buffer for external dependencies

### Goal Alignment
- **Ideas aligned with goals:** 85% (17/20 evaluated ideas)
- **Active projects on trajectory:** 100% (2/2 projects on track to goals)
- **Quarterly goal progress:** 67% (Month 2 of 3) ✅ On track

---

## 🚨 ALERTS & RECOMMENDATIONS

### Immediate Actions
- ✅ **No critical alerts** (all systems healthy)

### Opportunities
1. **Activate idea-012** (health-macro-tracker) when project-009 completes (~5 days)
2. **Review idea-015** (spanish-learning) for potential scope reduction (12 weeks → 8 weeks)

### Risks
- **Velocity trend:** Declining slightly (80% → 75% over 4 weeks)
  - **Action:** Review capacity allocation in next weekly review
- **External dependency:** project-009 blocked on API docs (2 days, low severity)
  - **Action:** Escalate if not resolved by 2026-02-08

---

## 📅 UPCOMING MILESTONES

### This Week (2026-W06)
- [ ] project-007: Complete backtesting engine (due 2026-02-10)
- [ ] project-009: Finish chart widgets (due 2026-02-08)

### Next 2 Weeks
- [ ] project-009: Launch MVP to beta users (due 2026-02-15)
- [ ] project-007: Implement portfolio optimization (due 2026-02-17)

### This Month (February 2026)
- [ ] project-009: Complete and launch (target 2026-02-20)
- [ ] project-007: Reach 50% completion (target 2026-02-28)

---

## 🔄 RECENT ACTIVITY (Last 7 Days)

- **2026-02-06:** idea-016 evaluated (score 7.2, moved to evaluated/)
- **2026-02-05:** project-009 milestone reached (50% complete)
- **2026-02-04:** Weekly review completed (velocity: 75%)
- **2026-02-03:** idea-017 submitted (in inbox/)
- **2026-02-02:** project-007 blocker resolved (authentication issue)
- **2026-02-01:** idea-018 archived (rejected, score 5.5)
- **2026-01-31:** Quarterly review completed (Q4 2025: 85% OKR achievement)

---

## 📚 REFERENCE

### Quick Links
- [Goals Foundation](./goals.yaml)
- [PDCA Dashboard](./data/pdca/dashboard.md)
- [Ideas Bank](./ideas-bank/)
- [Projects Bank](./projects-bank/)
- [Metrics History](./metrics/metrics.md)
- [Decision Log](./decisions/decision-log.md)

### Next Review Cadences
- **Daily:** Today 18:00
- **Weekly:** Sunday 2026-02-09 19:00
- **Monthly:** Sunday 2026-02-23 (last Sunday of month)
- **Quarterly:** Week of 2026-03-24 (Q1 end)

---

**Dashboard auto-updated by hooks after every lifecycle transition.**
```

### How to Read Dashboard

**1. Status Summary**
- **Quick glance:** How many ideas in each stage? How many active projects?
- **Key metric:** WIP (2/3) = 2 active, 3 max, 1 slot available

**2. Active Projects**
- **Focus:** What's in progress right now?
- **Health check:** Velocity (✅/⚠️/🚨), blockers, next actions
- **Decision support:** Should I activate more? Or wait for completion?

**3. Ready to Activate**
- **Queue:** Which planned ideas should I start next?
- **Prioritization:** Sorted by score + strategic alignment
- **Timing:** When can I activate? (depends on WIP capacity)

**4. Capacity Analysis**
- **Overcommitted?** Are you trying to do too much?
- **Under-utilized?** Do you have unused capacity?
- **Forecast:** When will capacity free up?

**5. Metrics & Trends**
- **Historical performance:** Am I improving over time?
- **Velocity trends:** Are things slowing down?
- **Bottlenecks:** What's blocking progress most often?

**6. Alerts & Recommendations**
- **Proactive guidance:** System suggests next best actions
- **Risk flagging:** Early warning of problems
- **Opportunity detection:** When to activate, when to pause

### Dashboard Update Frequency

**Auto-updated by hooks:**
- After Step 05 (Scoring): Idea counts update
- After Step 08 (Deep Plan): Planned ideas count
- After project activation: Active projects count, WIP
- After project completion/kill: Completed/killed counts, capacity freed
- After daily/weekly review: Velocity metrics update

**Manual refresh:**
```bash
# Generate latest dashboard
./scripts/dashboard.sh  # Unix
.\scripts\dashboard.ps1  # Windows
```

**Recommended review frequency:**
- **Daily:** Quick glance (5 seconds) - Any alerts? WIP status?
- **Weekly:** Full read (2 minutes) - Velocity trends? Capacity forecast?
- **Monthly:** Deep analysis (10 minutes) - Success rate? Bottlenecks? Strategic alignment?

---

## Real-World Walkthroughs

### Walkthrough 1: Quick Track (15 minutes)

**Scenario:** You have a simple idea (build Chrome extension for productivity), low stakes, want quick evaluation.

**Step-by-step:**

1. **Start Life OS:** Invoke workflow in Claude
2. **Select mode:** [C]reate
3. **Foundation check:** [S]kip (if foundation already exists)
4. **Share idea (Step 01):** "I want to build a Chrome extension that blocks distracting websites during work hours"
5. **Track selection:** [Q]uick Track
6. **Consilium Lite (Step 04-lite):** System spawns 2-3 specialists, quick perspectives (5 min)
7. **Simplified Scoring (Step 05):** 3 criteria only (Impact, Effort, Alignment) → Score: 7.8
8. **Decision:** ✅ GO (score >7.5)
9. **Complete (Step 09):** Idea saved to `evaluated/`, ready for planning when you want

**Total time:** 15 minutes
**Output:** Scored idea, quick validation, minimal investment

**When to use Quick Track:**
- Low-risk ideas (<$1K investment, <2 weeks effort)
- Quick validation before committing
- Batch processing (evaluate 10+ ideas quickly)

---

### Walkthrough 2: Standard Track with PDCA (60 minutes)

**Scenario:** You want to launch a SaaS product ($10K investment, 3 months effort), need solid plan and execution tracking.

**Step-by-step:**

**Phase 1: Foundation (10 min, first time only)**
1. **Start Life OS**
2. **Select mode:** [C]reate
3. **Foundation check:** [N]o data found
4. **Goals Discovery (Step 00):** Define annual goals (Business: "$5K MRR", Finance: "$20K emergency fund", Health: "Run 5K")
5. **Foundation steps:** 0.5 (Stage), 0.6 (Resources), 0.7 (Optimization) → ~5 minutes

**Phase 2: Idea Evaluation (30 min)**
6. **Share idea (Step 01):** "SaaS platform for AI-powered customer support automation"
7. **Track selection:** [S]tandard Track
8. **Roles Discovery (Step 02):** System suggests: Product Manager, Tech Lead, Marketing Strategist, Finance Analyst
9. **Specialist Match (Step 03):** Confirm specialists
10. **Consilium (Step 04):** 4-6 specialists, Six Hats, 15-20 min discussion
11. **Full Scoring (Step 05):** 9 criteria → Score: 8.5 (HIGH GO)
12. **PDCA Planning (Step 06):** Cascade goals → year/quarter/month/week/day plans (10 min)

**Phase 3: Deep Plan (20 min)**
13. **Deep Plan L1-L3 (Step 08):** High-level plan with phases, milestones, risks
14. **Complete (Step 09):** Idea saved to `planned/`, ready to activate

**Total time:** 60 minutes (or 50 min if foundation exists)
**Output:** Scored idea (8.5), deep plan (L1-L3), PDCA cascade ready

**Next steps:**
1. **Activate project:** Run `create-project-from-idea.sh` when ready
2. **Start execution:** Step X-01 (Kickoff)
3. **Weekly tracking:** Step X-02 (Pulse), Step 07 (Weekly Review)

---

### Walkthrough 3: Deep Track with Full TRIZ (4 hours)

**Scenario:** Major strategic decision ($100K+ investment, 12+ months commitment), need comprehensive analysis with contradiction resolution.

**Step-by-step:**

**Phase 1: Strategic Foundation (20 min)**
1. **Goals Discovery (Step 00):** Define/update annual and quarterly goals
2. **Foundation steps:** Ensure all foundation data current

**Phase 2: Consilium & Contradiction Analysis (90 min)**
3. **Share idea (Step 01):** "Build B2B AI platform targeting enterprise customers"
4. **Track selection:** [D]eep Track
5. **Roles Discovery (Step 02):** 6-8 specialists including Security Architect, Compliance Expert
6. **Consilium Deep (Step 04):** Multi-round, 25-30 min, high-quality perspectives
7. **Contradiction detection:** Consilium reveals: "Need fast time-to-market (12 months) BUT enterprise requires extensive security/compliance (adds 18+ months)"
8. **TRIZ Auto-Trigger (Step 04.5):** System offers TRIZ analysis
9. **TRIZ Structured (Step 04.5):** 40 Inventive Principles applied, solutions generated (30-60 min)
   - **Solution found:** "Segmentation + Prior Action" → Launch MVP to SMBs (fast), build enterprise features in parallel (compliance pipeline)

**Phase 3: Comprehensive Planning (90 min)**
10. **Full Scoring (Step 05):** 10+ criteria, weighted by goals → Score: 9.2 (EXCEPTIONAL)
11. **PDCA Planning (Step 06):** Full cascade with monthly milestones
12. **PDCA Review Setup (Step 07):** Configure daily/weekly/monthly/quarterly cadences
13. **Deep Plan L1-L6 (Step 08):** Comprehensive plan with scenarios, dependencies, risk mitigation (60 min)
14. **Final Polish (Step 08.5):** Review and refine (10 min)

**Phase 4: Execution Setup (20 min)**
15. **Kickoff (Step X-01):** Transition to IN_PROGRESS, set 5 key milestones with dates
16. **Complete (Step 09):** Idea → Project activated

**Total time:** 4 hours
**Output:**
- Scored idea (9.2 exceptional)
- TRIZ solutions (contradiction resolved)
- Deep plan L1-L6 (comprehensive)
- PDCA cascade (execution ready)
- Milestones set (tracking ready)

**Ongoing:**
- Daily reviews (5 min EOD)
- Weekly velocity tracking (30 min Sunday)
- Monthly trajectory checks (1 hour)
- Quarterly strategic replanning (2 hours)

---

### Walkthrough 4: Ideas→Projects Lifecycle (Complete Journey)

**Scenario:** Follow one idea from inbox to project completion.

**Day 1: Idea Submission**
1. **Submit idea:** "Build algorithmic trading bot using VectorBT"
2. **Location:** `ideas-bank/inbox/idea-007-finance-katana-vectorbt.md`
3. **Status:** INBOX (not evaluated)

**Day 2: Evaluation (Standard Track, 60 min)**
4. **Run workflow:** Step 01 → 05
5. **Score:** 8.2 (GO)
6. **Hook auto-moves:** `inbox/` → `evaluated/`
7. **Location:** `ideas-bank/evaluated/idea-007-finance-katana-vectorbt.md`
8. **Status:** EVALUATED (ready for planning)

**Day 3: Planning (Step 08, 30 min)**
9. **Deep Plan:** L1-L3 plan created
10. **Hook auto-moves:** `evaluated/` → `planned/`
11. **Location:** `ideas-bank/planned/idea-007-finance-katana-vectorbt.md`
12. **Status:** PLANNED (ready to activate)

**Day 4: Activation (5 min)**
13. **Check capacity:** WIP 2/3 (1 slot available) ✅
14. **Run script:**
    ```bash
    ./scripts/create-project-from-idea.sh idea-007-finance-katana-vectorbt.md
    ```
15. **Project created:** `projects-bank/active/project-007-katana/`
16. **Idea archived:** `ideas-bank/archive/activated/idea-007-finance-katana-activated-20260204.md`
17. **Status:** ACTIVE (IN_PROGRESS)

**Week 1-8: Execution (8 weeks)**
18. **Daily reviews:** 5 min EOD, track blockers
19. **Weekly pulse:** Step X-02, velocity tracking
20. **Milestones:** 3 reached on time, 1 delayed (adjusted)

**Week 9: Completion (30 min)**
21. **Project finished:** All success criteria met
22. **Run script:**
    ```bash
    ./scripts/complete-project.sh project-007-katana
    ```
23. **Retrospective:** Document learnings
24. **Project moved:** `active/` → `completed/`
25. **Status:** COMPLETED

**Final state:**
- **Idea:** `ideas-bank/archive/activated/idea-007-finance-katana-activated-20260204.md` (links to project-007)
- **Project:** `projects-bank/completed/project-007-katana/` (includes retrospective.md)
- **Traceability:** Full audit trail from idea → project → completion
- **Learnings:** Saved to global memory for future reference

**Total timeline:** 8 weeks (Day 1 submission → Week 9 completion)

---

## Best Practices

### 1. Start with Goals (Step 00)

**Why:** Strategic alignment criterion (Step 05) requires goals. Without goals, scoring is less meaningful.

**When to define goals:**
- **First time:** During initial foundation setup
- **Annually:** End of year planning
- **Major life changes:** New job, relocation, health event

**Best practice:**
- Spend 15 minutes upfront to define goals
- Review quarterly (adjust based on progress)
- Update goals.yaml when priorities shift

**Impact:** Ideas that align with goals score higher → better prioritization.

---

### 2. Respect WIP Limits

**Why:** Overcommitment kills velocity. Max 3 active projects recommended.

**WIP limit guidelines:**
- **1 project:** Low utilization (OK if part-time)
- **2-3 projects:** Optimal (balanced focus + variety)
- **4+ projects:** Overcommitted (velocity drops, nothing finishes)

**Best practice:**
- Check portfolio.md before activating new project
- If at WIP limit, complete/kill existing project first
- Resist "just one more" temptation

**Impact:** Maintaining WIP limits increases completion rate by 40-60%.

---

### 3. Run Weekly Reviews (Step 07)

**Why:** Most frequent substantive review, catches velocity drops early.

**Weekly review protocol:**
- **When:** Sunday evening (weekly close-out)
- **Duration:** 30 minutes
- **Focus:** Velocity calculation, adjust next week priorities

**Best practice:**
- Set recurring calendar event (Sunday 19:00)
- Complete even when busy (takes only 30 min)
- Use velocity trend to adjust scope preemptively

**Impact:** Weekly reviews reduce project failure rate by 35% (catch problems early).

---

### 4. Automate with Hooks

**Why:** Manual file management is error-prone and time-consuming.

**What to automate:**
- ✅ Idea movements (inbox → evaluated → planned)
- ✅ Portfolio updates (counts, metrics)
- ✅ Memory extraction (patterns, learnings)
- ❌ Project activation (keep manual for intentionality)

**Best practice:**
- Enable all hooks except project activation
- Review hook logs monthly (catch automation errors)
- Disable hooks only when debugging

**Impact:** Hooks save 10-15 minutes per idea (no manual file moves).

---

### 5. Document Learnings (Retrospectives)

**Why:** Failure insights are as valuable as success patterns.

**When to document:**
- **Project completion:** Mandatory retrospective.md (what worked, what didn't)
- **Project kill:** Mandatory kill-analysis.md (why stopped, salvageable parts)
- **Quarterly review:** Strategic learnings (big picture insights)

**Best practice:**
- Be honest (no one sees this except you)
- Focus on actionable insights (not just descriptions)
- Save to global memory (reuse across projects)

**Impact:** Documented learnings reduce repeat failures by 50% (learn from mistakes).

---

### 6. Traceability is Key

**Why:** Every daily task should trace back to annual goal.

**How traceability works:**
```
Daily task: "Implement OAuth2 integration"
  ↓ linked to
Weekly goal: "Complete authentication module"
  ↓ linked to
Monthly goal: "Finish MVP development"
  ↓ linked to
Quarterly OKR: "Launch MVP and reach $1K MRR"
  ↓ linked to
Annual goal: "Build profitable SaaS product ($5K MRR)"
```

**Best practice:**
- Every file has `linked_to` field (automatic via Step 06)
- Verify linkages during monthly review
- If daily task doesn't trace to goal → question if it's strategic

**Impact:** Traceability prevents busywork (ensures all effort aligned with goals).

---

### 7. Adjust Quickly (Act Phase)

**Why:** PDCA without "Act" is just documentation theater.

**Act triggers:**
- Velocity drop >15%: Reduce scope immediately
- Chronic blocker >5 days: Escalate or find workaround
- Behind on quarterly goal >17%: Adjust timeline or scope
- Overcommitment ratio >1.2: Plan for 80% capacity next period

**Best practice:**
- Don't wait for quarterly review to adjust
- Act on signals in weekly review (faster feedback loop)
- Small adjustments beat big pivots

**Impact:** Quick adjustments keep velocity stable (prevent catastrophic failures).

---

## Troubleshooting

### Problem: "goals.yaml not found" error in Step 06

**Symptoms:** Step 06 (PDCA Planning) fails with error message

**Cause:** Goals Discovery (Step 00) not completed

**Solution:**
```
Option 1: Run Step 00 now
  - System prompts: [C]reate goals (10-15 min)
  - Complete goals discovery
  - Return to Step 06 automatically

Option 2: Skip PDCA Planning
  - System prompts: [S]kip
  - Continue without PDCA cascade
  - Can run Step 00 + 06 later anytime
```

**Prevention:** Run Goals Discovery during first-time foundation setup.

---

### Problem: Ideas not moving from inbox to evaluated automatically

**Symptoms:** After Step 05 (Scoring), idea still in `inbox/`

**Cause:** post-task hook disabled or failed

**Diagnosis:**
```bash
# Check if hooks enabled
cat data/hooks-config.yaml | grep "post_task:"
# Should show: enabled: true

# Check hook logs for errors
tail -20 .claude-flow/logs/hooks.log
```

**Solution:**
```
Option 1: Re-enable hooks
  - Edit data/hooks-config.yaml
  - Set post_task.enabled: true
  - Restart session

Option 2: Move manually
  - mv ideas-bank/inbox/idea-XXX.md ideas-bank/evaluated/
  - Update portfolio.md counts manually
```

**Prevention:** Don't disable post-task hooks unless testing.

---

### Problem: Portfolio dashboard shows incorrect counts

**Symptoms:** portfolio.md shows "Active: 3" but only 2 projects in `active/`

**Cause:** Hook failed to update portfolio, or manual file operations

**Solution:**
```bash
# Regenerate dashboard from scratch
./scripts/dashboard.sh  # Unix
.\scripts\dashboard.ps1  # Windows

# Verify counts manually
ls ideas-bank/inbox/ | wc -l
ls projects-bank/active/ | wc -l
```

**Prevention:** Use scripts for lifecycle transitions (not manual file moves).

---

### Problem: Velocity consistently <70% (slipping)

**Symptoms:** Weekly reviews show 60-65% velocity for 3+ weeks

**Causes:**
- Overcommitted (planned capacity > available)
- Unrealistic estimates (goals too ambitious)
- Chronic blockers (not addressed)
- Scope creep (tasks expanding mid-execution)

**Solution:**
```
Step 1: Diagnose root cause (weekly review)
  - Capacity analysis: Planned hours vs actual hours
  - Blocker analysis: Any recurring blockers?
  - Scope analysis: Are goals expanding?

Step 2: Adjust next week (Act phase)
  - Reduce scope: 2 goals instead of 3
  - Address blockers: Escalate or find workaround
  - Increase buffer: Plan for 80% of capacity (not 100%)

Step 3: Monitor for 2 weeks
  - If velocity improves → Keep adjustments
  - If velocity still low → Deeper investigation (quarterly review)
```

**Prevention:**
- Plan for 80-85% of capacity (always leave buffer)
- Address blockers within 3 days (don't let them become chronic)
- Review weekly velocity (catch drops early)

---

### Problem: Can't activate project (WIP limit reached)

**Symptoms:** Try to activate idea but portfolio shows "WIP 3/3"

**Cause:** Already at maximum WIP limit (3 active projects)

**Solution:**
```
Option 1: Complete existing project
  - Focus on finishing 1 project
  - Run complete-project.sh
  - Then activate new project

Option 2: Kill stalled project
  - Identify lowest priority or blocked project
  - Run kill-project.sh
  - Free up WIP slot

Option 3: Increase WIP limit (not recommended)
  - Edit portfolio policy (increase max from 3 to 4)
  - WARNING: Higher WIP often reduces velocity
```

**Best practice:** Complete or kill existing project before activating new one.

**Why WIP limits matter:** Studies show completion rate drops 40-60% when WIP >3.

---

### Problem: PDCA plans out of sync (week plan doesn't match month plan)

**Symptoms:** Weekly goals don't align with monthly goals

**Cause:** Generated PDCA plans long ago, not updated since

**Solution:**
```
Step 1: Regenerate current level
  - For week plan: Run Step 06, regenerate week-YYYY-WNN.yaml
  - For month plan: Run Step 06, regenerate month-YYYY-MM.yaml

Step 2: Verify linkages
  - Run validation: Check that week links to month, month links to quarter

Step 3: Update regularly
  - Week plan: Update every Sunday
  - Month plan: Update last Sunday of month
  - Quarter plan: Update end of quarter
```

**Prevention:** Update PDCA plans weekly (don't let them become stale).

---

### Problem: Step 07 (Review) taking too long

**Symptoms:** Daily review takes 20+ minutes (should be 5 min)

**Cause:** Asking too many questions or over-analyzing

**Solution:**
```
Daily Review Should Be:
  - 3 questions only (done, blocked, learned)
  - Short answers (1-2 sentences each)
  - Total: 5 minutes max

If taking longer:
  - Skip optional questions (learning can be skipped)
  - Save deep reflection for weekly review
  - Use template responses (e.g., "No blockers")
```

**Best practice:** Daily = quick signals, Weekly = substantive analysis.

---

### Problem: Lost project files after completion

**Symptoms:** Can't find project-XXX files after running complete-project.sh

**Cause:** Script moved files to `completed/` (expected behavior)

**Location:**
```
Before: projects-bank/active/project-XXX/
After: projects-bank/completed/project-XXX/

All files intact:
  - project.md
  - plan.md
  - tasks/
  - artifacts/
  - logs/
  - retrospective.md (new)
```

**Solution:** Files not lost, just moved to `completed/` folder.

**Prevention:** Check portfolio.md for location of all projects.

---

**For more troubleshooting, see: [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) (if exists)**

---

## Appendix: Quick Reference

### File Structure Cheat Sheet
```
life-os/
├── goals.yaml                           # Strategic goals
├── portfolio.md                         # Dashboard
├── ideas-bank/
│   ├── inbox/                           # New ideas
│   ├── evaluated/                       # Scored ideas
│   ├── planned/                         # Ready to activate
│   └── archive/ (rejected, postponed, activated)
├── projects-bank/
│   ├── active/                          # IN_PROGRESS
│   ├── completed/                       # SUCCESS
│   └── killed/                          # STOPPED
├── data/
│   ├── pdca/                            # PDCA plans (year/quarter/month/week/day)
│   ├── reviews/                         # PDCA reviews (daily/weekly/monthly/quarterly)
│   └── hooks-config.yaml                # Automation config
└── scripts/                             # Lifecycle scripts
```

### Command Cheat Sheet
```bash
# Lifecycle scripts
./scripts/create-project-from-idea.sh <idea-file>  # Activate
./scripts/complete-project.sh <project-name>       # Complete
./scripts/kill-project.sh <project-name>           # Kill
./scripts/archive-idea.sh <idea-file> <reason>     # Archive
./scripts/dashboard.sh                             # Dashboard

# Windows (PowerShell)
.\scripts\create-project-from-idea.ps1 -IdeaFile "<idea-file>"
.\scripts\complete-project.ps1 -ProjectName "<project-name>"
.\scripts\kill-project.ps1 -ProjectName "<project-name>"
.\scripts\archive-idea.ps1 -IdeaFile "<idea-file>" -Reason "<reason>"
.\scripts\dashboard.ps1
```

### Workflow Step Reference
| Step | Name | Duration | Purpose |
|------|------|----------|---------|
| 00 | Goals Discovery | 10-15 min | Define strategic goals |
| 0.5 | Project Stage | 5 min | Determine Точка А |
| 0.6 | Resource Assessment | 5 min | Calculate Speed Multiplier |
| 0.7 | Optimization Intelligence | 5 min | Suggest optimal approaches |
| 01 | Collect Ideas | 5 min | Share idea |
| 02 | Roles Discovery | 5 min | Identify specialists |
| 03 | Specialist Match | 5 min | Confirm specialists |
| 04 | Consilium | 15-30 min | Expert perspectives |
| 04.5 | TRIZ (optional) | 10-60 min | Resolve contradictions |
| 05 | Scoring | 10 min | MCDA scoring |
| 06 | PDCA Planning | 10 min | Goal cascade |
| 07 | PDCA Review | 5 min - 2h | Progress tracking |
| 08 | Deep Plan | 10-60 min | L1-L6 plan |
| 08.5 | Final Polish | 10 min | Review and refine |
| X-01 | Kickoff | 10-15 min | Activate project |
| X-02 | Weekly Pulse | 5 min | Progress check |
| X-03 | Milestone Gate | 10 min | Milestone review |
| X-04 | Pivot-or-Kill | 30 min | Stop decision |
| 09 | Complete | 5 min | Wrap up |

### Track Comparison
| Track | Duration | Steps | Use Case |
|-------|----------|-------|----------|
| Quick | 15-20 min | 01, 04-lite, 05 | Simple ideas, low stakes |
| Standard | 55-75 min | 01-05, 08 (L1-L3) | Moderate complexity |
| Deep | 2-4 hours | 00-08.5, X-01 | High-stakes, strategic |

---

**End of User Guide**

For technical reference, see: [workflow.md](../workflow.md)
For changelog, see: [CHANGELOG.md](./CHANGELOG.md)
