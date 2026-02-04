---
framework: "Pomodoro Technique"
framework_slug: "pomodoro"
domain: personal_development
applied_to_project: "{{project_id}}"
project_name: "{{project_name}}"
created_date: "{{YYYY-MM-DD}}"
completed_date: null

integration_step: "8-deep-plan"
time_invested_minutes: 0
consilium_specialist: "Productivity Expert"

scoring_contribution:
  provides_criteria: true
  provides_weights: false
  provides_scenarios: false
  mcda_dimensions: ["Task Completion Rate", "Focus Quality", "Time Efficiency"]

deep_plan_contribution:
  generates_l2_headings: true
  generates_l3_tasks: true
  generates_milestones: true

linked_frameworks: ["deliberate-practice", "gtd", "eisenhower-matrix", "atomic-habits"]
prerequisite_frameworks: []
follows_frameworks: ["eisenhower-matrix"]

tier: 1
personal_score: "46/50"
research_basis: "Francesco Cirillo, 1980s"
meta_analysis: "46/50 in productivity research meta-analysis (2020-2024, n=180)"
---

# Pomodoro Technique - {{project_name}}

> **Applied to Project**: {{project_name}}
> **Domain**: Personal Development
> **Tier**: 1 (tied #1, 46/50)
> **Time to fill**: ~15-20 min
> **Completed**: {{completed_date}}

---

## Research Basis

**Author:** Francesco Cirillo (1980s, Italy)

> "The Pomodoro Technique is about more than just a timer. It's a way to develop a sustainable relationship with time." -- Francesco Cirillo

**Psychological foundation:**
- **Ultradian rhythms**: the brain naturally cycles between 90-120 min of high and low alertness (Peretz Lavie, 1985)
- **Time boxing** reduces Parkinson's Law ("work expands to fill the time available")
- **Zeigarnik effect**: incomplete tasks create mental tension, motivating completion within pomodoro
- **Attention restoration**: short breaks prevent cognitive fatigue (Kaplan, 1995)

**Common misunderstanding:** Pomodoro is not for all types of work. Creative flow states (Csikszentmihalyi) should not be interrupted by the timer. If you are in flow -- extend the pomodoro.

---

## Framework Input

### Daily Work Plan

**Date**: {YYYY-MM-DD}
**Available work hours**: {X} hrs
**Total available pomodoros**: {X hrs * 2} (each pomodoro = 30 min block)

### Pomodoro Parameters

| Parameter | Standard | Adjusted (if needed) |
|-----------|----------|---------------------|
| Focus time | 25 min | {15-50 min} |
| Short break | 5 min | {3-10 min} |
| Long break | 15-30 min | {10-45 min} |
| Pomodoros before long break | 4 | {3-6} |

**Instruction / Инструкция:** Начинающим -- строго придерживайтесь стандартного формата 25/5. Менять параметры только после 2+ недель практики, когда будете чувствовать свой ритм.

### Task Estimation (Pomodoro Estimates)

| # | Task | Priority (Eisenhower Q) | Est. Pomodoros | Actual | Status |
|---|------|------------------------|----------------|--------|--------|
| 1 | {task} | {Q1/Q2/Q3} | {1-8} | | {pending} |
| 2 | {task} | {Q1/Q2/Q3} | {1-8} | | {pending} |
| 3 | {task} | {Q1/Q2/Q3} | {1-8} | | {pending} |

**Estimation guide / Руководство по оценке:**
- 1 pomodoro (25 min) -- simple, routine task (email, quick review)
- 2-3 pomodoros (50-75 min) -- medium complexity (write a section, code a feature)
- 4-6 pomodoros (100-150 min) -- complex task (design, deep analysis)
- 7+ pomodoros -- break into subtasks, each with its own pomodoro estimate

**Rule / Правило:** If a task takes more than 7 pomodoros, it is a project, not a task. Decompose it.

### Pomodoro Session Log

#### Session 1 (Pomodoros 1-4)

| Pom # | Start | Task | Internal Interruptions | External Interruptions | Completed? |
|-------|-------|------|----------------------|----------------------|------------|
| 1 | {time} | {task} | {count} | {count} | {Y/N} |
| 2 | {time} | {task} | {count} | {count} | {Y/N} |
| 3 | {time} | {task} | {count} | {count} | {Y/N} |
| 4 | {time} | {task} | {count} | {count} | {Y/N} |

**Long Break**: {start_time} -- {duration} min

#### Session 2 (Pomodoros 5-8)

| Pom # | Start | Task | Internal Int. | External Int. | Completed? |
|-------|-------|------|--------------|--------------|------------|
| 5 | {time} | {task} | {count} | {count} | {Y/N} |
| 6 | {time} | {task} | {count} | {count} | {Y/N} |
| 7 | {time} | {task} | {count} | {count} | {Y/N} |
| 8 | {time} | {task} | {count} | {count} | {Y/N} |

### Interruption Handling Protocol

**Internal interruptions** (your own thoughts, urges):
1. Mark apostrophe (') on the sheet -- record the distraction
2. Write it down on "Unplanned & Urgent" list
3. Return to the pomodoro immediately
4. Process the list during the break

**External interruptions** (someone asks you something):
1. **Inform**: "I'm in the middle of something, can I get back to you in {X} min?"
2. **Negotiate**: Propose a callback time
3. **Schedule**: Write it on the interruption list
4. **Call back**: During the break, respond to all deferred items

> "Every time you give in to an interruption, you lose not just the time of the interruption but also the focus recovery time (23 min on average)." -- Gloria Mark, UC Irvine

### Tools

| Tool | Platform | Best For |
|------|----------|---------|
| Forest App | iOS/Android | Gamification, phone distraction blocking |
| Toggl Track | Web/Desktop/Mobile | Time tracking with reports |
| Physical timer | Desk | Tactile feedback, no digital distraction |
| Focus To-Do | Cross-platform | Pomodoro + task management combined |
| Be Focused | macOS/iOS | Apple ecosystem integration |

---

## Synergy: Pomodoro + Deliberate Practice

> "Deliberate practice sessions of 60-90 minutes (4-6 pomodoros) represent the ideal focused practice window." -- Anders Ericsson

**Structure for practice sessions:**
- Pomodoros 1-2: Warm-up, targeted drills on weak sub-skills
- Pomodoros 3-4: Peak intensity, push beyond comfort zone
- Long break: Reflect, review feedback
- Pomodoros 5-6 (optional): Consolidation, integration exercises

**Instruction / Инструкция:** Если используете Pomodoro для Deliberate Practice -- во время перерывов записывайте инсайты и обратную связь, а не отвлекайтесь на соцсети.

---

## Daily Summary

| Metric | Value |
|--------|-------|
| Planned pomodoros | {X} |
| Completed pomodoros | {Y} |
| Completion rate | {Y/X * 100}% |
| Tasks finished | {count} |
| Total internal interruptions | {count} |
| Total external interruptions | {count} |
| Estimation accuracy | {avg actual / avg estimated * 100}% |

**Reflection / Рефлексия:**
- What went well: {observation}
- What to improve: {observation}
- Estimation adjustments for tomorrow: {note}

---

## Life OS Integration

### Step 6 (Calendar Sync)
- Daily schedule built in pomodoro blocks (e.g., 08:00-10:00 = 4 pomodoros for Q2 tasks)
- Calendar events converted to pomodoro estimates

### Step 8 (Deep Plan, L5: Tasks)
- Each L5 task has a pomodoro estimate
- Sprint planning: sum of pomodoros per week must not exceed available pomodoro budget

### Scoring Impact (Step 5)
```yaml
criteria_from_framework:
  - name: "Focus Quality"
    weight: 0.3
    rationale: "Tasks requiring deep work benefit most from structured focus"
  - name: "Estimation Accuracy"
    weight: 0.2
    rationale: "Better estimates lead to realistic planning"
```

### Deep Plan Contribution (Step 8)

**L2 Headings Generated:**
- Daily Execution Blocks
- Focus Session Structure
- Interruption Management

**L3 Tasks Generated:**
- Set up pomodoro tool and workspace
- Create daily task-to-pomodoro mapping
- Establish interruption handling protocol
- Weekly review of estimation accuracy

---

## Progress Tracking

| Week | Avg Pomodoros/Day | Completion Rate | Avg Interruptions | Estimation Accuracy |
|------|-------------------|-----------------|-------------------|---------------------|
| 1 | {X} | {%} | {count} | {%} |
| 2 | {X} | {%} | {count} | {%} |
| 3 | {X} | {%} | {count} | {%} |
| 4 | {X} | {%} | {count} | {%} |

**Target:** 10-12 focused pomodoros per day (experienced), 6-8 for beginners.

---

## Next Actions

- [ ] Choose pomodoro tool (physical timer recommended for first week)
- [ ] Create tomorrow's task list with pomodoro estimates
- [ ] Set up interruption handling protocol with colleagues/family
- [ ] Track for 1 week, then review estimation accuracy
- [ ] After 2 weeks, consider adjusting pomodoro duration if needed

---

## Metadata

**Framework Version**: 1.0
**Life OS Version**: 2.0
**Template Last Updated**: 2026-02-04
