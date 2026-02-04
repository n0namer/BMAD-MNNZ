---
framework: "Getting Things Done (GTD)"
framework_slug: "gtd"
domain: personal_development
applied_to_project: "{{project_id}}"
project_name: "{{project_name}}"
created_date: "{{YYYY-MM-DD}}"
completed_date: null

integration_step: "6-calendar-sync|8-deep-plan"
time_invested_minutes: 0
consilium_specialist: "Productivity Expert"

scoring_contribution:
  provides_criteria: true
  provides_weights: false
  provides_scenarios: false
  mcda_dimensions: ["Inbox Zero Achievement", "Next Action Clarity", "Project Momentum"]

deep_plan_contribution:
  generates_l2_headings: true
  generates_l3_tasks: true
  generates_milestones: true

linked_frameworks: ["eisenhower-matrix", "pomodoro", "atomic-habits"]
prerequisite_frameworks: []
follows_frameworks: ["eisenhower-matrix"]

tier: 2
personal_score: "41/50"
research_basis: "David Allen, 2001"
meta_analysis: "41/50 in productivity research meta-analysis (2020-2024, n=180)"
---

# Getting Things Done (GTD) - {{project_name}}

> **Applied to Project**: {{project_name}}
> **Domain**: Personal Development
> **Tier**: 2 (41/50)
> **Time to fill**: ~90-120 min (initial setup), then ~15 min/day
> **Completed**: {{completed_date}}

---

## Research Basis

**Author:** David Allen, "Getting Things Done: The Art of Stress-Free Productivity" (2001, revised 2015)

> "Your mind is for having ideas, not holding them." -- David Allen

> "You can do anything, but not everything." -- David Allen

**Psychological foundation:**
- **Cognitive load theory** (Sweller, 1988): unprocessed "open loops" consume working memory
- **Zeigarnik effect**: incomplete tasks occupy mental bandwidth until captured in a trusted system
- **Decision fatigue** (Baumeister, 2011): pre-deciding "next actions" reduces daily decision count
- **External cognition**: offloading mental inventory to a system frees the mind for creative thinking

**Common misunderstanding:** GTD is NOT just a to-do list. It is a complete workflow for processing all incoming commitments. Many people try GTD, create lists, but skip the Clarify and Reflect steps -- and then blame the system. The Weekly Review is the engine that makes GTD work.

> "GTD is not about getting everything done. It's about appropriately engaging with your world." -- David Allen

---

## Framework Input

### The 5 Steps of GTD

---

### Step 1: CAPTURE (Collect everything)

**Inboxes (where things land):**
- [ ] Physical inbox (papers, notes on desk)
- [ ] Email inbox ({email_address})
- [ ] Notes app ({app_name})
- [ ] Voice memos / Quick capture
- [ ] Browser tabs and bookmarks
- [ ] {other_inbox}

**Mind Sweep / Brain Dump:**

Write EVERYTHING that has your attention -- no filtering, no organizing, just dump:

1. {open loop}
2. {commitment}
3. {idea}
4. {worry}
5. {task}
6. {thing you said you'd do}

**Instruction / Инструкция:** Сбор ("capture") -- это не только задачи. Это ВСЕ, что занимает ваше внимание: неотвеченное письмо, идея для проекта, обещание другу, беспокойство о здоровье. Если оно в голове -- выгрузите на бумагу.

**Rule / Правило:** Capture tools must be with you at all times. If you cannot capture an idea within 60 seconds, the system breaks.

---

### Step 2: CLARIFY (Process each item)

**For each captured item, ask this decision tree:**

```
Is it actionable?
├── NO:
│   ├── Trash (delete/discard)
│   ├── Someday/Maybe (incubate)
│   └── Reference (file for retrieval)
│
└── YES:
    ├── What's the NEXT physical action?
    │   ├── Takes <2 min? → DO IT NOW
    │   ├── Am I the best person? → NO → DELEGATE (Waiting For)
    │   └── YES → Is it one action or multiple?
    │       ├── One action → NEXT ACTIONS list
    │       └── Multiple actions → PROJECT (define outcome + next action)
```

> "If it takes less than two minutes, do it now. The two-minute rule is the cornerstone of GTD efficiency." -- David Allen

**Processed items:**

| Item | Actionable? | Next Action | Destination |
|------|-------------|-------------|-------------|
| {item 1} | {Y/N} | {specific physical action} | {Next Actions / Project / Waiting For / Someday / Trash / Reference} |
| {item 2} | {Y/N} | {action} | {destination} |
| {item 3} | {Y/N} | {action} | {destination} |

---

### Step 3: ORGANIZE (Put everything in the right place)

#### Next Actions (by context)

**@Computer:**
- [ ] {action 1}
- [ ] {action 2}

**@Phone/Calls:**
- [ ] {action 1}

**@Errands:**
- [ ] {action 1}

**@Home:**
- [ ] {action 1}

**@Office/Work:**
- [ ] {action 1}

**@Anywhere:**
- [ ] {action 1}

**Instruction / Инструкция:** Контексты (@) -- это ключ к GTD. Когда вы дома -- смотрите только список @Home. Когда у компьютера -- только @Computer. Не пытайтесь видеть все задачи одновременно.

#### Projects (outcomes requiring 2+ actions)

| # | Project Name | Desired Outcome | Next Action | Status |
|---|-------------|----------------|-------------|--------|
| 1 | {project} | {what "done" looks like} | {specific next action} | {Active/Stalled} |
| 2 | {project} | {outcome} | {next action} | {Active/Stalled} |
| 3 | {project} | {outcome} | {next action} | {Active/Stalled} |

**Rule / Правило:** Every project MUST have at least one Next Action defined. A project without a Next Action is stalled.

#### Waiting For (delegated or blocked items)

| Item | Waiting On | Date Delegated | Follow-up Date |
|------|-----------|---------------|----------------|
| {item} | {person} | {date} | {date} |

#### Someday/Maybe (not committed yet)

- {idea for later}
- {book to read}
- {trip to take}
- {skill to learn}

#### Calendar (time-specific only)

- {date/time}: {hard appointment}
- {deadline date}: {deliverable}

**Rule / Правило:** The calendar is sacred. ONLY put time-specific commitments here. Do NOT use the calendar as a to-do list.

#### Reference (non-actionable information)

- {document/link/note storage location}

---

### Step 4: REFLECT (Weekly Review)

> "The Weekly Review is the master key to maintaining your system. If you skip it, GTD collapses within 2-3 weeks." -- David Allen

**Weekly Review Checklist (every {day} at {time}):**

**Get Clear:**
- [ ] Collect all loose papers and materials
- [ ] Process ALL inboxes to zero (email, notes, physical)
- [ ] Empty your head (additional brain dump)

**Get Current:**
- [ ] Review Next Actions lists -- mark completed, add new
- [ ] Review Projects list -- ensure each has a Next Action
- [ ] Review Waiting For -- follow up on overdue items
- [ ] Review Calendar (past week) -- anything to capture?
- [ ] Review Calendar (next 2 weeks) -- any prep needed?

**Get Creative:**
- [ ] Review Someday/Maybe -- promote any to Active?
- [ ] Review Goals and long-term horizons
- [ ] Brainstorm new ideas or improvements

**Estimated time**: 60-90 min (first few times), 30-45 min (experienced)

---

### Step 5: ENGAGE (Choose what to do now)

**4 Criteria for Choosing Actions (in this order):**

1. **Context**: Where am I? What tools do I have?
   - Current context: {@ context}

2. **Time Available**: How long until my next commitment?
   - Available: {X} minutes

3. **Energy Level**: What's my mental/physical capacity?
   - Current energy: {High / Medium / Low}

4. **Priority**: Given context + time + energy, what matters most?
   - Chosen action: {specific next action}

---

## Synergy: GTD + Eisenhower Matrix

| Eisenhower Quadrant | GTD Integration |
|--------------------|----------------|
| Q1 (Urgent + Important) | Next Actions with HIGH priority flag |
| Q2 (Important, Not Urgent) | Projects --> scheduled in Calendar time blocks |
| Q3 (Urgent, Not Important) | Waiting For (delegate) or batch-process |
| Q4 (Not Urgent/Important) | Trash during Clarify step |

**Instruction / Инструкция:** Eisenhower определяет ЧТО важно. GTD определяет КАК это организовать и выполнить. Используйте оба: сначала классифицируйте задачу по матрице, затем обработайте через GTD workflow.

---

## Current State Snapshot

| List | Items Count | Status |
|------|-------------|--------|
| Inbox | {X} | Last processed: {date} |
| Next Actions | {Y} | Contexts: {N} |
| Projects (Active) | {Z} | Stalled: {count} |
| Waiting For | {W} | Oldest: {date} |
| Someday/Maybe | {V} | Last reviewed: {date} |
| Calendar (next 2 weeks) | {U} | |

---

## Life OS Integration

### Step 6 (Calendar Sync)
- GTD Calendar items sync with Life OS calendar
- Project deadlines mapped to milestones
- Weekly Review scheduled as recurring Q2 event

### Step 8 (Deep Plan, L4: Next Actions)
- Each L4 task is a GTD-compliant Next Action
- Projects decomposed into Next Actions with contexts
- Waiting For items tracked for dependencies

### Scoring Impact (Step 5)
```yaml
criteria_from_framework:
  - name: "Execution Readiness"
    weight: 0.3
    rationale: "Projects with clear next actions execute faster"
  - name: "System Reliability"
    weight: 0.2
    rationale: "Trusted system reduces cognitive overhead"
```

### Deep Plan Contribution (Step 8)

**L2 Headings Generated:**
- System Setup (Capture + Organize)
- Weekly Review Rhythm
- Active Project Execution
- Context-Based Daily Flow

**L3 Tasks Generated:**
- Set up all inboxes and capture tools
- Create context lists (@Computer, @Phone, etc.)
- Define all projects with outcomes and next actions
- Schedule Weekly Review as recurring event
- Process inbox to zero daily

**Milestones:**
- Week 1: All inboxes identified, first brain dump complete
- Week 2: First Weekly Review completed
- Week 4: Inbox zero achieved 3+ times
- Week 8: Weekly Review habit established (never miss twice)

---

## Progress Tracking

| Week | Inbox Zero Days | Weekly Review Done? | Active Projects | Stalled Projects | Notes |
|------|----------------|---------------------|-----------------|-----------------|-------|
| 1 | {/7} | {Y/N} | {count} | {count} | {observations} |
| 2 | {/7} | {Y/N} | {count} | {count} | |
| 3 | {/7} | {Y/N} | {count} | {count} | |
| 4 | {/7} | {Y/N} | {count} | {count} | |

---

## Next Actions

- [ ] Do a full brain dump (capture everything in your head)
- [ ] Set up your capture tools (at least 2: physical + digital)
- [ ] Process all items through the Clarify decision tree
- [ ] Create context-based Next Actions lists
- [ ] Define all active projects with outcomes
- [ ] Schedule first Weekly Review (block 90 min)
- [ ] Process inbox to zero today

---

## Metadata

**Framework Version**: 1.0
**Life OS Version**: 2.0
**Template Last Updated**: 2026-02-04
