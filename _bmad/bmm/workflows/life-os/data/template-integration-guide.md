---
document: template-integration-guide
version: 1.0
last_updated: 2026-02-04
purpose: Master integration reference for all Life OS framework templates
templates_count: 30
domains: [business, finance, health, personal_development, universal_methods, project_management]
related_files:
  - domain-template-architecture.md
  - domain-framework-integration.md
  - framework-synergy-matrix.csv
  - deep-plan-templates.md
  - triz-quick-patterns.md
  - roles-base-enhanced.csv
  - method-rankings.yaml
---

# Life OS Template Integration Guide

**Total Templates:** 30

| Category | Count | Templates |
|----------|-------|-----------|
| Universal Methods (TRIZ) | 3 | TRIZ Quick, TRIZ Structured, ARIZ Full |
| Business | 6 | OKRs, Lean Canvas, SWOT, BMC, VPC, Porter's Five Forces |
| Finance | 6 | NPV, DCF, Monte Carlo, Real Options, CAPM, Kelly Criterion |
| Health | 6 | HBM, SMART Goals, Habit Loop, Progressive Overload, Macros, Recovery |
| Personal Development | 6 | Pomodoro, Atomic Habits, Eisenhower, GTD, Growth Mindset, Deliberate Practice |
| Project Management | 4 | Project Plan, Project Journal, Project Snapshot, Project Decisions |

**Purpose:** This document is the master reference for how every template integrates with the Life OS workflow. It covers location mapping, step-by-step integration points, domain detection logic, selection decision trees, synergy patterns, auto-population rules, lifecycle management, quality gates, memory integration, versioning, and common pitfalls.

---

## 1. Template Location Map

### Directory Structure

```
_bmad/bmm/workflows/life-os/templates/
|
|-- Universal Methods (TRIZ)
|   |-- triz-quick.template.md
|   |-- triz-structured.template.md
|   |-- ariz-full.template.md
|
|-- Project Management
|   |-- project-plan.template.md
|   |-- project-journal.template.md
|   |-- project-snapshot.template.md
|   |-- project-decisions.template.md
|
|-- Domain Templates (Phase 2 - to be created)
|   |-- business/
|   |   |-- okrs.template.md
|   |   |-- lean-canvas.template.md
|   |   |-- swot.template.md
|   |   |-- business-model-canvas.template.md
|   |   |-- value-proposition-canvas.template.md
|   |   |-- porters-five-forces.template.md
|   |
|   |-- finance/
|   |   |-- npv.template.md
|   |   |-- dcf.template.md
|   |   |-- monte-carlo.template.md
|   |   |-- real-options.template.md
|   |   |-- capm.template.md
|   |   |-- kelly-criterion.template.md
|   |
|   |-- health/
|   |   |-- health-belief-model.template.md
|   |   |-- smart-goals.template.md
|   |   |-- habit-loop.template.md
|   |   |-- progressive-overload.template.md
|   |   |-- macros-tracking.template.md
|   |   |-- recovery-protocols.template.md
|   |
|   |-- personal/
|       |-- pomodoro.template.md
|       |-- atomic-habits.template.md
|       |-- eisenhower-matrix.template.md
|       |-- gtd.template.md
|       |-- growth-mindset.template.md
|       |-- deliberate-practice.template.md
```

### Template File Naming Convention

- Universal templates: `[method-slug].template.md`
- Domain templates: `[domain]/[framework-slug].template.md`
- Project management: `project-[type].template.md`

### Supporting Data Files

| File | Purpose | Used By |
|------|---------|---------|
| `data/domain-template-architecture.md` | Template specifications for all 24 domain frameworks | All domain templates |
| `data/domain-framework-integration.md` | Decision trees and integration logic | Steps 4, 5, 8 |
| `data/framework-synergy-matrix.csv` | 73 framework pair synergy ratings | Template composition |
| `data/triz-quick-patterns.md` | 40 TRIZ principles with domain examples | Step 4.5, TRIZ templates |
| `data/deep-plan-templates.md` | L1-L6 planning templates by scenario | Step 8 |
| `data/roles-base-enhanced.csv` | 50+ specialists with framework tags | Steps 2, 3 |
| `data/method-rankings.yaml` | Framework rankings by domain | Auto-suggest engine |
| `data/mcda-methodology.md` | Multi-Criteria Decision Analysis details | Step 5 scoring |

---

## 2. Step-by-Step Integration Points

Each Life OS step interacts with specific templates. This section maps every integration point.

### Step 1: Collect Ideas (`steps-c/step-01-collect-ideas.md`)

**Templates that integrate:**

| Template | Integration Type | How |
|----------|-----------------|-----|
| Design Thinking | Embedded (not separate template) | Empathize/Define phases are built into idea collection |
| Health Belief Model | Optional trigger | If idea involves health behavior change, HBM readiness assessment is suggested |
| Growth Mindset | Optional trigger | If idea involves learning or overcoming fear of failure, assess mindset |
| Atomic Habits | Optional trigger | If idea is about building or breaking a habit, flag for later |

**Auto-detect logic:**
- Scan idea description for health keywords -> flag HBM
- Scan for learning/skill keywords -> flag Growth Mindset
- Scan for habit keywords -> flag Atomic Habits
- These flags carry forward to Step 3 (Specialist Match) and Step 4 (Consilium)

---

### Step 2: Roles Discovery (`steps-c/step-02-roles-discovery.md`)

**Templates that integrate:**

| Template | Integration Type | How |
|----------|-----------------|-----|
| roles-base-enhanced.csv | Data source | Enhanced CSV includes framework_expertise column per specialist |
| All domain frameworks | Indirect | Specialist selection informed by which frameworks might be needed |

**Integration mechanism:**
- The enhanced roles CSV includes a `framework_expertise` field
- When a specialist is discovered, their framework expertise tags carry forward
- Example: "Portfolio Manager" has `framework_expertise: [NPV, DCF, Monte Carlo, CAPM, Kelly Criterion]`

---

### Step 3: Specialist Match (`steps-c/step-03-specialist-match.md`)

**Templates that integrate:**

| Template | Integration Type | How |
|----------|-----------------|-----|
| roles-base-enhanced.csv | Primary data source | Framework expertise tags drive specialist-framework matching |
| All domain frameworks | Indirect | Matched specialists inform which frameworks are available |

**Integration mechanism:**
- After specialists are matched, the system knows which frameworks are "on the table"
- This narrowed list feeds into Step 4 (Consilium) where specialists can recommend specific frameworks
- Example: If Financial Analyst and Portfolio Manager are both matched, Finance domain frameworks become high-priority suggestions

---

### Step 4: Consilium (`steps-c/step-04-consilium.md`)

**Templates that integrate:**

| Template | Integration Type | How |
|----------|-----------------|-----|
| Six Thinking Hats | Embedded | Consilium uses Six Hats structure for multi-perspective analysis |
| TRIZ (all 3) | Optional [T] menu | If specialists disagree >40%, TRIZ resolves contradictions |
| SWOT Analysis | Specialist-driven | Business Strategist or Market Analyst populates SWOT quadrants |
| Value Proposition Canvas | Specialist-driven | UX Designer or Product Manager validates product-market fit |
| Porter's Five Forces | Specialist-driven | Market Analyst leads competitive landscape assessment |
| Business Model Canvas | Specialist-driven | Business Strategist maps business model if relevant |
| Health Belief Model | Specialist-driven | Health Coach assesses readiness for behavior change |
| OKRs | Specialist-driven | Strategic Planner frames objectives and key results |

**Key integration point: Specialist disagreement triggers TRIZ:**
- If consilium divergence >40%, present [T] TRIZ option
- TRIZ mode selected based on context (Quick for minor disagreements, Structured for major)
- TRIZ output feeds back into consilium for re-evaluation

---

### Step 4.5: TRIZ Analysis (`steps-c/step-04.5-triz-analysis.md`) - Optional

**Templates that integrate:**

| Template | Integration Type | How |
|----------|-----------------|-----|
| TRIZ Quick (`triz-quick.template.md`) | Mode 1 (5-10 min) | Fast contradiction resolution with top 3 principles |
| TRIZ Structured (`triz-structured.template.md`) | Mode 2 (30-60 min) | Full contradiction matrix + IFR analysis |
| ARIZ Full (`ariz-full.template.md`) | Mode 3 (2-4 hr) | Complete 9-part ARIZ-85C process |
| `data/triz-quick-patterns.md` | Data source | 40 principles with domain examples and 10x10 matrix |

**Called from:** Step 4 (specialist disagreement), Step 5 (scoring conflicts), Step 8 (planning contradictions)

**Output integration:**
- Contradiction resolution document created
- workflow-plan.md updated with TRIZ solution
- If called from Step 8: TRIZ solution becomes L2 structure in deep plan
- Memory stored for future cross-project reuse

---

### Step 5: Scoring (`steps-c/step-05-scoring.md`)

**Templates that integrate:**

| Template | Integration Type | How |
|----------|-----------------|-----|
| MCDA | Embedded | Multi-Criteria Decision Analysis is the core scoring engine |
| TRIZ (all 3) | Optional [T] menu | If scoring criteria conflict, TRIZ resolves |
| OKRs | Criteria source | Strategic Alignment criterion derived from OKR alignment |
| NPV Analysis | Criteria source | Financial Impact criterion uses NPV calculation |
| Real Options | Criteria source | Option Value criterion for high-uncertainty projects |
| Eisenhower Matrix | Criteria source | Urgency criterion from Eisenhower quadrant placement |
| Monte Carlo | Enhancement | Risk scoring enhanced by probability distribution |
| CAPM | Enhancement | Risk-adjusted return provides discount rate context |
| Kelly Criterion | Enhancement | Optimal allocation informs resource commitment |
| DCF Model | Enhancement | Valuation perspective for financial projects |
| SWOT Analysis | Enhancement | Scenario weights from SWOT quadrant analysis |

**Scoring criteria mapping:**

| MCDA Criterion | Primary Framework | How Framework Contributes |
|----------------|-------------------|---------------------------|
| Strategic Alignment | OKRs | Score = % alignment with defined Objectives |
| Financial Impact | NPV, DCF | Score = NPV magnitude relative to investment |
| Risk Level | Monte Carlo, CAPM | Score = P(failure) from simulation, Beta from CAPM |
| Effort / Complexity | Pomodoro, GTD | Score = estimated Pomodoros or GTD complexity |
| Urgency | Eisenhower | Score = quadrant placement (Q1=highest, Q4=lowest) |
| Option Value | Real Options | Score = expanded NPV - traditional NPV |
| Health Impact | HBM | Score = weighted HBM decision matrix total |
| Skill Requirement | Deliberate Practice | Score = gap between current and required proficiency |

---

### Step 6: Integration (`steps-c/step-06-integration.md`)

**Templates that integrate:**

| Template | Integration Type | How |
|----------|-----------------|-----|
| Project Plan (`project-plan.template.md`) | Created/initialized | New project plan document instantiated |
| Strategic Buckets (`data/strategic-buckets.md`) | Data allocation | Project assigned to appropriate strategic bucket |
| Eisenhower Matrix | Prioritization | Project placed in Eisenhower quadrant for portfolio view |
| GTD System | Execution lists | Next Actions, Waiting For, and Projects lists populated |
| Habit Loop | Daily habits | If project requires daily habits, loop defined |
| Atomic Habits | Habit design | 4 Laws applied to design sustainable habits |
| Pomodoro Technique | Time blocking | Tasks estimated in Pomodoro units |
| OKRs | Goal alignment | Project linked to relevant OKR objectives |
| Project Decisions (`project-decisions.template.md`) | Created | Decision log initialized for the project |

**Integration sequence:**
1. Create project-plan.md instance from template
2. Allocate to strategic bucket based on scoring results
3. Generate initial GTD lists (Next Actions for first phase)
4. If habit-based project: design Habit Loop + Atomic Habits 4 Laws
5. Estimate initial Pomodoro counts for first milestone
6. Link project to active OKRs (if any)
7. Initialize project-decisions.md for decision tracking

---

### Step 7: Calendar Sync (`steps-c/step-07-calendar-sync.md`)

**Templates that integrate:**

| Template | Integration Type | How |
|----------|-----------------|-----|
| Pomodoro Technique | Time scheduling | Tasks scheduled in Pomodoro blocks on calendar |
| Deliberate Practice | Practice sessions | Practice sessions mapped to specific time slots |
| Progressive Overload | Training blocks | Training sessions scheduled with rest days |
| Recovery Protocols | Recovery days | Recovery and deload periods blocked on calendar |
| Macro Tracking | Meal prep time | Meal prep and grocery shopping sessions scheduled |
| GTD System | Calendar items | Time-specific commitments from GTD calendar list |
| Time Blocking | Execution | All framework outputs converted to calendar blocks |

**Calendar integration logic:**
1. Extract all time-specific items from active frameworks
2. Map Pomodoro estimates to available calendar slots
3. Schedule Deliberate Practice sessions (recommended: 60-90 min blocks)
4. Insert Progressive Overload training sessions with deload weeks
5. Add Recovery Protocol rest days between intense periods
6. Block meal prep time from Macro Tracking weekly plan
7. Sync GTD calendar items (appointments, deadlines)

---

### Step 8: Deep Plan (`steps-c/step-08-deep-plan.md`)

**Templates that integrate:**

| Template | Integration Type | Deep Plan Level | How |
|----------|-----------------|-----------------|-----|
| TRIZ (all 3) | Optional [T] menu | L2 | Planning contradictions resolved; TRIZ principle becomes L2 node |
| OKRs | L2 structure | L2 | Each Objective becomes a major phase (L2 heading) |
| Business Model Canvas | L3 activities | L3 | Each of 9 BMC blocks generates specific activities |
| DCF Model | L2 phases | L2 | Year-based phases from DCF forecast period |
| SMART Goals | L4 tasks | L4 | Each SMART goal validated at task level |
| GTD System | L4 actions | L4 | Next Actions with contexts at task level |
| Atomic Habits | L5 habits | L5 | Daily habits as atomic subtasks |
| Progressive Overload | L2 blocks | L2 | Training blocks: Foundation, Progressive, Peak, Deload |
| Pomodoro Technique | L5 estimation | L5 | Task duration estimated in Pomodoro units |
| Deliberate Practice | L3 sessions | L3 | Practice sessions mapped to skill sub-areas |
| Lean Canvas | L3 validation | L3 | Validation experiments per canvas section |
| Value Proposition Canvas | L3 activities | L3 | Pain relievers and gain creators as activities |
| NPV Analysis | L2 milestones | L2 | Year-based milestones from cash flow projections |
| Monte Carlo | L3 risk items | L3 | Risk mitigation actions for top variance drivers |
| Real Options | L2 decision pts | L2 | Decision points: expand, abandon, switch |
| Recovery Protocols | L3 recovery | L3 | Recovery modalities scheduled between intense phases |
| Eisenhower Matrix | L4 priority | L4 | Tasks tagged with quadrant for priority sorting |
| Project Plan | Target output | L1-L6 | Deep plan populates the project plan template |

**Deep Plan Level Mapping:**

```
L1: Mission/Role (from workflow-plan.md)
L2: Contribution Areas / Major Phases
    <- OKR Objectives
    <- DCF Year-based phases
    <- Progressive Overload training blocks
    <- TRIZ solution (if contradiction resolved)
    <- Real Options decision points
    <- NPV year milestones
L3: Work Streams / Activities
    <- BMC 9 blocks -> specific activities
    <- Lean Canvas validation experiments
    <- VPC pain relievers + gain creators
    <- Deliberate Practice sessions by sub-skill
    <- Monte Carlo risk mitigation actions
    <- Recovery modalities
L4: Stages / Tasks
    <- SMART goal validation per task
    <- GTD Next Actions with @contexts
    <- Eisenhower quadrant tagging
L5: Subtasks / Habits
    <- Atomic Habits daily habits
    <- Pomodoro estimation per subtask
    <- Habit Loop cue-routine-reward
L6: Atomic Actions / Details
    <- Execution specifics, environment setup, resource links
```

---

### Step 9: Complete (`steps-c/step-09-complete.md`)

**Templates that integrate:**

| Template | Integration Type | How |
|----------|-----------------|-----|
| Project Snapshot (`project-snapshot.template.md`) | Created | Initial baseline snapshot of project state |
| Project Journal (`project-journal.template.md`) | Created | First journal entry documenting project creation |
| Project Decisions (`project-decisions.template.md`) | Updated | Initial decisions from workflow recorded |

**Completion outputs:**
1. Project Snapshot created with initial baseline metrics
2. Project Journal first entry: creation date, key decisions, initial plan summary
3. All framework instances linked to project ID
4. Memory storage: project creation event saved to Claude Flow memory
5. Workflow plan frontmatter updated with `status: active`

---

### Edit Steps (steps-e/)

| Step | Template Integration |
|------|---------------------|
| step-01-update-project.md | Updates Project Plan, Project Journal, any active framework instances |
| step-02-rescoring.md | Re-runs MCDA with updated framework outputs (NPV, SWOT, etc.) |
| step-03-kill-project.md | Archives all framework instances, final Project Snapshot |
| step-04-deep-plan.md | Same as Step 8 create but in edit mode for existing plans |

---

### Validate Steps (steps-v/)

| Step | Template Integration |
|------|---------------------|
| step-01-daily-review.md | Checks GTD lists, Pomodoro completion, Habit tracking |
| step-02-weekly-review.md | Full GTD weekly review, OKR progress check, Eisenhower rebalance |
| step-03-monthly-review.md | Portfolio health via Strategic Buckets, NPV/DCF review, Project Snapshots |

---

### Return-to-Plan Step (steps-v/step-00-return-to-plan.md)

**Templates that integrate:**

| Template | Integration Type | How |
|----------|-----------------|-----|
| Project Plan | Context load | Quick context snapshot from existing project plan |
| Project Snapshot | Status review | Latest snapshot shows current state |
| Project Journal | History review | Recent journal entries for context |

---

## 3. Domain Detection and Auto-Suggest Logic

### Business Domain

**Trigger keywords:** revenue, customers, market, product, business model, value proposition, competition, strategy, launch, startup, b2b, b2c, saas, marketplace, pricing, growth, acquisition, retention, churn, MVP, pivot

**Consilium specialist signals:** Business Strategist, Product Manager, Market Analyst, Growth Lead, UX Designer present in matched specialists

**Auto-suggest tiers:**

| Tier | Framework | When to Suggest |
|------|-----------|-----------------|
| 1 | OKRs | Strategic goal-setting, team alignment needed |
| 1 | Lean Canvas | Startup or new product, problem-solution fit validation |
| 2 | SWOT Analysis | Mature business, competitive positioning, strategic planning |
| 2 | Business Model Canvas | Business model design or redesign question |
| 2 | Value Proposition Canvas | Product-market fit validation, customer understanding |
| 3 | Porter's Five Forces | Industry analysis, competitive landscape deep dive |

**Suggestion limit:** Maximum 2 frameworks from Tier 1-2 for initial suggestion. Tier 3 only if user requests deeper analysis.

---

### Finance Domain

**Trigger keywords:** investment, ROI, NPV, cash flow, valuation, portfolio, property, rental, stock, crypto, fund, budget, financial, return, risk, yield, dividend, debt, equity, mortgage, retirement, savings, compound interest

**Consilium specialist signals:** Portfolio Manager, Financial Analyst, Risk Analyst, Investment Advisor present

**Auto-suggest tiers:**

| Tier | Framework | When to Suggest |
|------|-----------|-----------------|
| 1 | NPV Analysis | Universal investment evaluation, go/no-go decisions |
| 1 | DCF Model | Company or project valuation needed |
| 1 | Monte Carlo | High uncertainty, need probability distributions |
| 2 | Real Options | Decisions can be deferred, staged investments |
| 2 | CAPM | Publicly traded assets, portfolio risk assessment |
| 3 | Kelly Criterion | Position sizing, capital allocation optimization |

**Suggestion limit:** Maximum 2 from Tier 1. Add Tier 2-3 only when project complexity warrants.

---

### Health Domain

**Trigger keywords:** weight loss, fitness, gym, workout, diet, nutrition, health, exercise, muscle, cardio, marathon, body composition, sleep, recovery, strength, endurance, flexibility, injury prevention, wellness, mental health, meditation, stress

**Consilium specialist signals:** Fitness Coach, Nutritionist, Recovery Specialist, Sports Psychologist, Health Coach present

**Auto-suggest tiers:**

| Tier | Framework | When to Suggest |
|------|-----------|-----------------|
| 1 | Progressive Overload | Strength training, physical performance improvement |
| 1 | Habit Loop | Behavior change needed (exercise, diet, sleep) |
| 1 | Health Belief Model | Readiness assessment for new health behavior |
| 2 | Macro Tracking | Nutrition-focused goal (weight loss, muscle gain, performance) |
| 2 | Recovery Protocols | Injury prevention, overtraining risk, deload planning |
| 2 | SMART Goals | Clear health targets with measurable outcomes |

**Suggestion limit:** Maximum 2 from Tier 1. Tier 2 added based on specific sub-domain.

---

### Personal Development Domain

**Trigger keywords:** learn, skill, study, master, practice, productivity, focus, time management, habit, goal, growth, development, reading, writing, career, course, certification, language, instrument, public speaking, discipline

**Consilium specialist signals:** Learning Specialist, Productivity Coach, Career Advisor, Time Management Expert present

**Auto-suggest tiers:**

| Tier | Framework | When to Suggest |
|------|-----------|-----------------|
| 1 | Pomodoro Technique | Time management, focus improvement, task execution |
| 1 | Atomic Habits | Habit building or breaking, behavior design |
| 1 | Eisenhower Matrix | Prioritization, overwhelm management |
| 2 | GTD System | Comprehensive productivity overhaul, many open loops |
| 2 | Deliberate Practice | Skill mastery, specific performance improvement |
| 2 | Growth Mindset | Facing challenges, fear of failure, learning plateaus |

**Suggestion limit:** Maximum 2 from Tier 1. Tier 2 when user shows commitment to deeper system.

---

### Multi-Domain Projects

When a project spans multiple domains, detect the combination and suggest cross-domain framework sets:

| Project Type | Domains | Suggested Frameworks |
|-------------|---------|---------------------|
| Health Coaching Business | Health + Business | Progressive Overload + OKRs + Lean Canvas |
| Rental Property Investment | Finance + Business | NPV + Real Options + SWOT |
| Learn Day Trading | Finance + Personal Dev | Kelly Criterion + Deliberate Practice + Pomodoro |
| Fitness App Startup | Health + Business + Personal | HBM + Lean Canvas + Atomic Habits |
| Career Transition | Personal Dev + Business | Eisenhower + SWOT + Growth Mindset + SMART Goals |
| Investment Portfolio Building | Finance + Personal Dev | CAPM + Monte Carlo + GTD + Pomodoro |
| Weight Loss Journey | Health + Personal Dev | HBM + Progressive Overload + Habit Loop + Atomic Habits |
| Side Business Launch | Business + Personal Dev | Lean Canvas + OKRs + Pomodoro + GTD |

**Rule:** Multi-domain projects may use up to 3-4 frameworks total (1-2 per domain), but never more than 4 active at once.

---

## 4. Template Selection Decision Trees

### Decision Tree 1: By Project Type

```
START: What type of project?
|
|-- New Business / Startup
|   |-- Early stage (idea validation)?
|   |   YES -> Lean Canvas + VPC
|   |   NO  -> BMC + OKRs + Porter's (if competitive market)
|
|-- Investment Decision
|   |-- Single investment?
|   |   YES -> NPV (+ Monte Carlo if uncertain)
|   |   NO  -> CAPM + Kelly + Monte Carlo (portfolio)
|
|-- Health / Fitness Goal
|   |-- Physical performance?
|   |   YES -> Progressive Overload + SMART + Macros
|   |   NO  -> HBM + Habit Loop + Atomic Habits
|
|-- Skill Development
|   |-- Specific measurable skill?
|   |   YES -> Deliberate Practice + Pomodoro + SMART
|   |   NO  -> Growth Mindset + GTD + Eisenhower
|
|-- Productivity Overhaul
|   |-- First time setting up system?
|   |   YES -> GTD + Eisenhower + Pomodoro
|   |   NO  -> Eisenhower (re-prioritize) + Atomic Habits (habit tune-up)
|
|-- Strategic Decision
|   |-- Competitive analysis needed?
|   |   YES -> SWOT + Porter's + BMC
|   |   NO  -> SWOT + OKRs
```

### Decision Tree 2: By Time Available

```
START: How much time can you invest in framework analysis?
|
|-- Under 30 minutes
|   |-- Choose from: Pomodoro (15-20 min), SMART Goals (15-30 min),
|   |   Eisenhower (20-30 min), Habit Loop (20-30 min),
|   |   Growth Mindset (20-30 min), TRIZ Quick (5-10 min)
|
|-- 30-60 minutes
|   |-- Choose from: OKRs (30-45 min), SWOT (30-60 min),
|   |   Atomic Habits (30-45 min), HBM (30-45 min),
|   |   CAPM (30-45 min), TRIZ Structured (30-60 min),
|   |   Lean Canvas (45-75 min), VPC (45-60 min),
|   |   Kelly Criterion (45-60 min)
|
|-- 1-2 hours
|   |-- Choose from: BMC (60-90 min), NPV (60-90 min),
|   |   Progressive Overload (45-60 min), Macro Tracking (60-90 min),
|   |   Deliberate Practice (45-60 min), Recovery Protocols (45-60 min),
|   |   Monte Carlo (90-150 min), Porter's Five Forces (90-120 min),
|   |   GTD Setup (90-120 min)
|
|-- 2-4 hours
|   |-- Choose from: DCF Model (120-180 min),
|   |   Real Options (120-180 min), ARIZ Full (120-240 min)
|
|-- 4+ hours
|   |-- Full portfolio analysis with multiple frameworks
|   |-- Composition patterns (see Section 5)
```

### Decision Tree 3: By Complexity and Uncertainty

```
START: How complex and uncertain is the project?
|
|-- Low complexity, low uncertainty
|   |-- Simple frameworks: SMART, Pomodoro, Eisenhower, Habit Loop
|   |-- Time: 15-30 min per framework
|
|-- Low complexity, high uncertainty
|   |-- Add probabilistic: Monte Carlo, Real Options, HBM
|   |-- Time: 60-120 min total
|
|-- High complexity, low uncertainty
|   |-- Structural frameworks: BMC, OKRs, GTD, Progressive Overload
|   |-- Time: 90-180 min total
|
|-- High complexity, high uncertainty
|   |-- Full analysis: SWOT + Monte Carlo + Real Options + TRIZ
|   |-- Consider composition patterns
|   |-- Time: 3-6 hours total
|
|-- Contradictions detected (any complexity)
|   |-- Add TRIZ (Quick for simple, Structured for complex, ARIZ for strategic)
```

---

## 5. Template Synergy Matrix

### Top 12 Transformative Synergies

These are the highest-rated synergy pairs from `framework-synergy-matrix.csv`, selected for their practical impact on Life OS projects.

#### 1. TRIZ + Business Model Canvas (5 stars)

**Synergy type:** Contradiction resolution

**How they work together:**
- TRIZ resolves contradictions in business model (e.g., speed vs quality, cost vs features)
- BMC structures the resolution into a coherent business model

**Example:** "High quality requires high cost" -> TRIZ Principle #26 (Copying) -> Franchise model standardizes quality at lower marginal cost -> BMC restructures around franchise revenue streams

**When to combine:** Startup facing fundamental business model contradictions

---

#### 2. GTD + SCAMPER (5 stars)

**Synergy type:** Creativity unlock

**How they work together:**
- GTD reduces cognitive load by capturing all open loops -> frees mental space
- SCAMPER during GTD Clarify step generates innovative next actions

**Example:** GTD inbox item "improve team communication" -> SCAMPER Eliminate: "Can I eliminate status meetings entirely?" -> Test async video updates as next action

**When to combine:** Productivity-focused projects needing creative solutions

---

#### 3. Pomodoro + Deliberate Practice (5 stars)

**Synergy type:** Structured execution

**How they work together:**
- 4-6 Pomodoros = ideal deliberate practice session length (60-90 minutes)
- Pomodoro breaks provide spaced repetition advantage
- Timer creates consistent practice trigger

**Example:** Learning async/await in JavaScript: 6 daily Pomodoros targeting weakest coding area, video review feedback after each session set

**When to combine:** Any skill development project

---

#### 4. Growth Mindset + Deliberate Practice (5 stars)

**Synergy type:** Foundation + enabler

**How they work together:**
- Growth Mindset = foundational belief that enables effortful practice
- Removes fear of failure that prevents deliberate practice
- Together they create sustainable skill development

**Example:** Musician struggles with complex piece -> Growth Mindset reframes mistakes as learning data -> commits to 10,000 deliberate reps without self-judgment

**When to combine:** Skill projects where fear of failure is a barrier

---

#### 5. SMART + Progressive Overload (5 stars)

**Synergy type:** Destination + path

**How they work together:**
- SMART defines the measurable destination
- Progressive Overload provides the incremental path to get there
- Together: clear target with systematic progression

**Example:** SMART: "Run 5K in 25 minutes by December" -> Progressive Overload: +5% distance weekly, interval training progression, deload every 4 weeks

**When to combine:** Any physical fitness or measurable performance goal

---

#### 6. Atomic Habits + Health Belief Model (4 stars)

**Synergy type:** Capability + automation

**How they work together:**
- HBM addresses "Am I capable of this?" (Self-Efficacy assessment)
- Atomic Habits provides 4 Laws to make the behavior automatic once capability is established
- HBM diagnoses, Atomic Habits prescribes

**Example:** Exercise habit: HBM reveals low self-efficacy -> address with small wins -> Atomic Habits 2-Minute Rule makes routine automatic via cue-response loop

**When to combine:** Health behavior change projects

---

#### 7. NPV + Monte Carlo (4 stars)

**Synergy type:** Calculation + probability

**How they work together:**
- Monte Carlo generates probability distribution of NPV outcomes
- Quantifies risk: "70% chance NPV > $50K, 10% chance NPV < $0"
- Transforms single-point NPV into risk-adjusted decision

**Example:** Real estate investment: NPV shows $80K profit, but Monte Carlo reveals 15% chance of negative return due to vacancy rate uncertainty -> adjusts decision with risk awareness

**When to combine:** Any financial decision with uncertain variables

---

#### 8. Eisenhower + Pareto / GTD (4-5 stars)

**Synergy type:** Prioritize + execute

**How they work together:**
- Eisenhower identifies what matters (urgent/important classification)
- GTD provides execution system for chosen priorities
- Pareto finds the 20% of important tasks that drive 80% of results
- Together: ruthless prioritization with reliable execution

**Example:** 50 tasks -> Eisenhower: 20 are important -> Pareto: 4 tasks = 80% impact -> GTD: next actions defined with @contexts for the vital 4

**When to combine:** Overwhelmed state or productivity optimization

---

#### 9. Atomic Habits + Progressive Overload (5 stars)

**Synergy type:** Consistency + growth

**How they work together:**
- Atomic Habits builds daily consistency through 4 Laws
- Progressive Overload ensures the habit evolves and avoids plateau
- Together: sustainable habit that keeps getting harder

**Example:** Workout habit established via Atomic Habits -> Progressive Overload: +5% weight monthly keeps the habit progressing toward goals

**When to combine:** Fitness or any skill project requiring daily practice

---

#### 10. PDCA + Deliberate Practice (5 stars)

**Synergy type:** Systematic improvement

**How they work together:**
- PDCA Check phase = analyze performance (what went wrong, what worked)
- PDCA Act phase = adjust technique for next practice cycle
- Accelerates the deliberate practice feedback loop

**Example:** Public speaking: Record talk (Do) -> Review weaknesses (Check) -> Target specific fix in next rep (Act) -> Plan next practice session (Plan)

**When to combine:** Skill mastery with measurable improvement cycles

---

#### 11. Pareto + Deliberate Practice (5 stars)

**Synergy type:** Leverage + mastery

**How they work together:**
- Pareto identifies the 20% of skills that drive 80% of results
- Deliberate Practice masters that high-leverage 20%
- Maximum skill impact with minimum practice time

**Example:** Sales professional: Pareto identifies "objection handling" as top 20% skill -> 10,000 deliberate reps role-playing objections -> 80% improvement in close rate

**When to combine:** Skill development with limited time

---

#### 12. TRIZ + Design Thinking (5 stars)

**Synergy type:** Structured ideation

**How they work together:**
- Design Thinking provides human-centered problem context (Empathize, Define)
- TRIZ Ideate phase uses 40 inventive principles for systematic solution generation
- Together: user needs + systematic creativity

**Example:** Ideate phase stuck -> TRIZ Principle #1 Segmentation: "break user journey into micro-moments, solve each independently" -> breakthrough design solution

**When to combine:** Product design with complex user needs

---

### Complete Synergy Reference

For all 73 framework pair ratings, see `data/framework-synergy-matrix.csv`. Synergy scores:

| Score | Meaning | Action |
|-------|---------|--------|
| 5 stars | Transformative synergy | Strongly recommend combining |
| 4 stars | High synergy | Recommend combining when both domains relevant |
| 3 stars | Moderate synergy | Combine if user explicitly requests |
| 2 stars | Low synergy | Rarely beneficial to combine |
| 1 star | Minimal synergy | Do not suggest combining |

---

## 6. Auto-Population Rules

### Rule 1: Project Metadata from Workflow Plan

**Source:** `workflow-plan.md` frontmatter

**Auto-populated fields in every template:**
```yaml
applied_to_project: "{{workflow-plan.project_id}}"
project_name: "{{workflow-plan.project_name}}"
created_date: "{{TODAY}}"
```

**Trigger:** Template instantiation (when user approves framework creation)

---

### Rule 2: Consilium Specialists -> Framework Recommendations

**Source:** `steps-c/step-04-consilium.md` output

**Mapping:**

| Consilium Specialist | Recommended Frameworks | Rationale |
|----------------------|------------------------|-----------|
| Business Strategist | BMC, OKRs, SWOT | Strategic thinking tools |
| Financial Analyst | NPV, DCF, Monte Carlo, CAPM | Financial evaluation tools |
| Portfolio Manager | Kelly Criterion, CAPM, Real Options | Portfolio optimization |
| UX Designer | VPC, Lean Canvas | Customer-centric validation |
| Data Scientist | Monte Carlo, Kelly Criterion | Probabilistic reasoning |
| Product Manager | Lean Canvas, OKRs, GTD | Product delivery focus |
| Market Analyst | Porter's Five Forces, SWOT | Competitive analysis |
| Health Coach | HBM, SMART, Progressive Overload | Wellness tools |
| Nutritionist | Macro Tracking, Recovery Protocols | Nutrition and recovery |
| Fitness Coach | Progressive Overload, SMART, Recovery | Physical training |
| Productivity Expert | GTD, Pomodoro, Eisenhower | Time and task management |
| Learning Specialist | Deliberate Practice, Growth Mindset | Skill development |
| Career Advisor | Eisenhower, OKRs, SMART | Career planning |

**Auto-population logic:**
1. Parse consilium specialist list
2. Pre-fill `consilium_specialist` field in template
3. Suggest 1-3 frameworks based on specialist type
4. User approves before creation

---

### Rule 3: Scoring Criteria -> Framework Pre-Fill

**Source:** `steps-c/step-05-scoring.md` MCDA output

**Mapping:**

| MCDA Criterion | Framework | Pre-Fill Section |
|----------------|-----------|------------------|
| Financial Return | NPV, DCF | Decision threshold, discount rate |
| Customer Satisfaction | VPC, Lean Canvas | Customer jobs, gains, pains |
| Strategic Fit | SWOT, Porter's | SO strategies, competitive analysis |
| Technical Feasibility | Deliberate Practice | Skill decomposition, practice plan |
| Time Efficiency | Pomodoro, GTD | Task estimates, context lists |
| Health Impact | HBM | Perceived susceptibility, severity |
| Risk Level | Monte Carlo | Variables to simulate |
| Urgency | Eisenhower | Quadrant classification |

---

### Rule 4: Deep Plan Levels -> Framework Outputs

**Source:** `steps-c/step-08-deep-plan.md` L1-L6 structure

**Auto-population logic:**
1. After framework is completed, extract generated headings
2. Inject into deep plan at appropriate level
3. Merge with existing plan structure (no duplicates)

**Example flow:**
```
Business Model Canvas completed:
  -> L2: "Customer Acquisition" (from BMC Channels + Customer Segments)
  -> L2: "Value Delivery" (from BMC Value Propositions + Key Activities)
  -> L2: "Revenue Generation" (from BMC Revenue Streams)
  -> L2: "Cost Management" (from BMC Cost Structure)
  -> L3: Specific actions from each of 9 BMC blocks

Injected into existing deep plan:
  L1: Launch SaaS Product
    L2: Customer Acquisition [from BMC]
      L3: Build landing page [from BMC Channels]
      L3: Set up email marketing [from BMC Channels]
    L2: Value Delivery [from BMC]
      L3: Develop core feature set [from BMC Key Activities]
```

---

### Rule 5: Framework Dates -> Timeline Sync

**Source:** Framework `completed_date` and `time_invested_minutes` fields

**Auto-population logic:**
1. When framework marked complete -> update project timeline
2. Calculate actual time invested -> inform future estimates
3. Update workflow-plan.md phase dates if framework completion triggers phase transition

---

### Rule 6: Cross-Framework Data Flow

**Source:** Linked frameworks (from composition patterns)

**Auto-population examples:**

| From Framework | Field | To Framework | Field |
|---------------|-------|--------------|-------|
| Lean Canvas | Problem (Top 3) | VPC | Pains |
| Lean Canvas | Solution (Top 3) | VPC | Pain Relievers |
| Lean Canvas | Key Metrics | OKRs | Key Results |
| VPC | Customer Jobs | BMC | Customer Segments |
| OKR | Initiatives | GTD | Projects |
| GTD | Next Actions | Pomodoro | Task List |
| SMART | Measurable Target | Progressive Overload | Target Performance |
| HBM | Cues to Action | Habit Loop | Cue |
| HBM | Perceived Benefits | Habit Loop | Reward |
| Habit Loop | Cue | Atomic Habits | Law 1 (Make Obvious) |
| Habit Loop | Reward | Atomic Habits | Law 4 (Make Satisfying) |
| NPV | Cash Flow Projections | DCF | Free Cash Flow inputs |
| DCF | Revenue Growth Rate | Monte Carlo | Variable 1 |
| DCF | Operating Margin | Monte Carlo | Variable 2 |
| Monte Carlo | P(Success) | Kelly Criterion | Win Probability (p) |
| Monte Carlo | Percentiles | Real Options | Decision Tree Scenarios |
| CAPM | Expected Return | NPV | Discount Rate |
| CAPM | Expected Return | DCF | Cost of Equity |
| Progressive Overload | Training Volume | Macro Tracking | Calorie Target |
| Progressive Overload | Deload Protocol | Recovery Protocols | Load Management |
| Macro Tracking | Protein Target | Recovery Protocols | Nutrition for recovery |
| SMART | Measurable Target | Macro Tracking | Weight/body comp target |
| Eisenhower | Q2 Tasks | GTD | Projects |
| Growth Mindset | Strategies to Bridge Gap | Deliberate Practice | Practice Schedule |
| Deliberate Practice | Sub-Skills | Pomodoro | Task List (sessions) |

---

## 7. Template Lifecycle

### Creation Triggers

| Trigger | Template(s) Created | When |
|---------|---------------------|------|
| User selects [T] TRIZ in menu | TRIZ Quick, Structured, or ARIZ Full | Step 4, 5, or 8 |
| Domain detected + framework suggested + user approves | Domain template instance | After Step 4 or 5 |
| Step 6 Integration reached | Project Plan | Step 6 |
| Step 9 Complete reached | Project Snapshot + Project Journal | Step 9 |
| User explicitly requests | Any framework | Any time |
| Composition pattern activated | Multiple frameworks in sequence | After Step 5 |

### Update Triggers

| Event | Templates Updated | What Changes |
|-------|-------------------|--------------|
| Scoring criteria change | NPV, MCDA-linked frameworks | Financial and risk parameters |
| Consilium revised | SWOT, VPC, specialist-driven frameworks | Specialist recommendations |
| Deep Plan evolved | OKRs, Project Plan | L2-L6 structure |
| Weekly Review | GTD lists, Project Journal | Next Actions, Waiting For |
| Monthly Review | Project Snapshot, NPV, Strategic Buckets | Portfolio metrics |
| Milestone reached | Project Snapshot, OKRs | Progress metrics, KR updates |
| TRIZ resolution | Workflow plan, calling step framework | Contradiction resolved |
| Habit tracking update | Habit Loop, Atomic Habits | Streak data, adjustment |
| Training progression | Progressive Overload, Macro Tracking | Volume/intensity changes |

### Archive Triggers

| Event | What Gets Archived | Where |
|-------|-------------------|-------|
| Project completed | All project framework instances | `.bmad/archive/{project_id}/` |
| Template superseded | Old template version | `templates/archive/` |
| Project killed (Step E-03) | All project artifacts + final snapshot | `.bmad/archive/{project_id}/` |
| Experiment abandoned | Framework instance + lessons learned note | `.bmad/archive/{project_id}/` |

---

## 8. Template Quality Gates

### Universal Quality Gate (All Templates)

Before any template instance is finalized, verify:

- [ ] YAML frontmatter complete (all required fields populated)
- [ ] All placeholder fields filled: `{Project Name}`, `{date}`, `{user_name}`
- [ ] Integration sections reference actual workflow steps (not placeholder text)
- [ ] Linked to `workflow-plan.md` via `applied_to_project` field
- [ ] At least one Next Action defined
- [ ] Scoring contribution section completed (if applicable)
- [ ] Deep plan contribution section completed (if applicable)

### Domain-Specific Quality Gates

**Business Domain:**

| Framework | Quality Checks |
|-----------|---------------|
| OKRs | All Objectives have 3-5 Key Results; KRs are measurable with baselines |
| Lean Canvas | All 9 blocks populated; Problem-Solution linkage clear |
| SWOT | All 4 quadrants populated; TOWS strategies derived (SO, ST, WO, WT) |
| BMC | All 9 building blocks filled; Revenue Streams justified |
| VPC | Customer Profile and Value Map both complete; Fit analysis done |
| Porter's Five Forces | All 5 forces assessed with evidence; Strategic implications stated |

**Finance Domain:**

| Framework | Quality Checks |
|-----------|---------------|
| NPV | Discount rate justified; Cash flows have documented assumptions; Sensitivity analysis done |
| DCF | Revenue projections have growth rate rationale; Terminal value method justified; WACC calculated |
| Monte Carlo | At least 3 variables identified; Distributions justified; 10K+ iterations; Percentiles documented |
| Real Options | At least 2 option types evaluated; Decision tree drawn; Expanded NPV calculated |
| CAPM | Risk-free rate source cited; Beta justified; Expected return compared to project return |
| Kelly Criterion | Win probability has evidence basis; Fractional Kelly calculated; Portfolio context provided |

**Health Domain:**

| Framework | Quality Checks |
|-----------|---------------|
| HBM | All 6 constructs rated; Decision matrix completed; Action plan addresses lowest-scoring construct |
| SMART Goals | All 5 SMART criteria explicitly addressed; Final goal statement includes all 5 elements |
| Habit Loop | Cue is specific and actionable; Routine is step-by-step; Reward is immediate |
| Progressive Overload | Baseline measured; Progression schedule has deload weeks; Plateau protocol defined |
| Macro Tracking | TDEE calculated with method shown; Macro split justified for goal; Adjustment protocol defined |
| Recovery Protocols | At least 3 recovery modalities planned; Red flags defined; Metrics tracking set up |

**Personal Development Domain:**

| Framework | Quality Checks |
|-----------|---------------|
| Pomodoro | Task estimates in Pomodoro units; Distraction tracking planned; Daily summary format defined |
| Atomic Habits | All 4 Laws applied; Identity statement written; 2-Minute Rule version defined |
| Eisenhower | All tasks classified; Q2 time target set (60%+ goal); Delegation plan for Q3 |
| GTD | 5 inboxes identified; Next Actions have @contexts; Weekly review scheduled |
| Growth Mindset | Recent challenge analyzed; Fixed -> Growth reframe documented; Evidence of progress planned |
| Deliberate Practice | Skill decomposed into sub-skills; Feedback mechanism defined; Practice schedule with focus areas |

### TRIZ Quality Gates

| Template | Quality Checks |
|----------|---------------|
| TRIZ Quick | Contradiction classified (Technical/Physical/Administrative); At least 2 principles suggested; 1+ solution documented |
| TRIZ Structured | Contradiction Matrix consulted; IFR defined; At least 2 principles applied with 2+ solutions each; Selected solution documented |
| ARIZ Full | All 9 ARIZ parts completed; IFR-1 and IFR-2 defined; VPR analysis done; Solution checked against IFR |

---

## 9. Memory Integration

### Storage Namespace Structure

All template-related knowledge stores to Claude Flow Memory using this namespace hierarchy:

```
shared-knowledge:life-os:templates:{domain}:{framework}:{project_id}:{date}
```

**Examples:**
```
shared-knowledge:life-os:templates:business:okrs:PROJ-001:2026-02-04
shared-knowledge:life-os:templates:finance:npv:PROJ-002:2026-02-04
shared-knowledge:life-os:templates:health:progressive-overload:PROJ-003:2026-02-04
shared-knowledge:life-os:templates:universal:triz-quick:PROJ-001:2026-02-04
shared-knowledge:life-os:templates:project:plan:PROJ-001:2026-02-04
```

### Storage Content Schema

```json
{
  "template": "{framework_name}",
  "domain": "{business|finance|health|personal|universal|project}",
  "project_id": "{id}",
  "project_name": "{name}",
  "completion_date": "{YYYY-MM-DD}",
  "outputs": ["{file1.md}", "{file2.md}"],
  "effectiveness_rating": "{1-5 stars - post-project}",
  "time_invested_minutes": "{number}",
  "roi": "{outcome achieved description}",
  "lessons_learned": "{what worked, what did not}",
  "would_use_again": true,
  "recommended_for_similar": ["{project_type1}", "{project_type2}"],
  "synergies_discovered": ["{framework_pair1}", "{framework_pair2}"],
  "contradictions_resolved": ["{contradiction description if TRIZ used}"]
}
```

### Auto-Save Events

| Event | Memory Action | Namespace Key |
|-------|---------------|---------------|
| Template created | Store creation event | `life-os:templates:{domain}:{framework}:{project_id}:created` |
| Template completed | Store completion + outputs | `life-os:templates:{domain}:{framework}:{project_id}:completed` |
| TRIZ resolution | Store contradiction + solution | `life-os:methods:triz:{project_id}:{date}` |
| Post-project rating | Store effectiveness | `life-os:templates:{domain}:{framework}:{project_id}:rated` |
| Framework synergy discovered | Store synergy pattern | `life-os:synergies:{framework1}:{framework2}` |

### Retrieval Commands

```bash
# Find all uses of a specific framework
npx claude-flow@v3alpha memory search -q "template:okrs effectiveness"

# Find Business domain patterns
npx claude-flow@v3alpha memory search -q "domain:business roi lessons"

# Find TRIZ successes
npx claude-flow@v3alpha memory search -q "triz contradiction resolution"

# Find similar project patterns
npx claude-flow@v3alpha memory search -q "project_type:startup frameworks used"

# Find synergy patterns
npx claude-flow@v3alpha memory search -q "synergy framework combination"

# Find effectiveness ratings
npx claude-flow@v3alpha memory search -q "effectiveness_rating:5 template"
```

### Learning Loop

Memory enables continuous improvement:

1. **Before framework selection:** Search memory for similar projects -> find which frameworks worked best
2. **During framework use:** Reference past instances for pre-fill data and lessons learned
3. **After project completion:** Rate framework effectiveness -> store for future reference
4. **Cross-project learning:** Discover new synergy patterns from multi-project data

---

## 10. Template Versioning

### Version Numbering

**Template definition files** (`templates/*.template.md`):
- Major version: v1.0, v2.0 (structure changes, new sections)
- Minor version: v1.1, v1.2 (content improvements, bug fixes)
- Format: Tracked in template YAML frontmatter `template_version` field

**Template instances** (user-created documents):
- Date-based naming: `{YYYY-MM-DD}-{framework-slug}-{project_id}.md`
- Example: `2026-02-04-okrs-PROJ-001.md`
- Instance versions not tracked separately (use project journal for history)

### Update Protocol

1. Identify improvement needed (user feedback, new research, bug discovery)
2. Determine version increment:
   - **Patch (v1.0.1):** Typo fix, minor wording improvement
   - **Minor (v1.1):** New optional section added, improved examples
   - **Major (v2.0):** Structure change, formula update, integration point change
3. Update template definition file
4. Add changelog entry to template
5. Store update event in Claude Flow memory
6. Existing instances are NOT auto-updated (preserves historical context)

### Breaking Changes (Major Version)

Examples of breaking changes requiring v2.0:
- SWOT adds a 5th dimension (e.g., environmental)
- NPV changes discount rate calculation method
- Template integration point changes (e.g., moved from Step 5 to Step 4)
- YAML frontmatter structure changes
- Required section added or removed

### Backwards Compatibility

- Old template versions kept in `templates/archive/` directory
- Claude can still read and process old instances
- Recommendation: Migrate to new version if project is ongoing (>30 days)
- No forced migration; user decides when to upgrade

---

## 11. Composition Patterns

### Pattern 1: Startup Launch (Business Domain)

**Sequence:** Lean Canvas -> Value Proposition Canvas -> OKRs -> Business Model Canvas -> GTD

**Time estimate:** 4-6 hours total

**Data flow:**
1. Lean Canvas "Problem" -> VPC "Pains" (copy top 3 problems)
2. Lean Canvas "Solution" -> VPC "Pain Relievers" (copy solutions)
3. Lean Canvas "Key Metrics" -> OKR "Key Results" (transform to measurable KRs)
4. VPC "Customer Jobs" -> BMC "Customer Segments" (sync customer profiles)
5. OKR "Initiatives" -> GTD "Projects" (create project per initiative with next action)

**Expected outcome:** Complete business strategy from problem validation to daily execution

---

### Pattern 2: Skill Acquisition (Personal Domain)

**Sequence:** Growth Mindset Reflection -> Deliberate Practice -> Pomodoro Technique -> Atomic Habits

**Time estimate:** 2-3 hours total

**Data flow:**
1. Growth Mindset "Strategies to Bridge Gap" -> Deliberate Practice "Practice Schedule"
2. Deliberate Practice "Sub-Skills" -> Pomodoro "Task List" (each session = Pomodoro)
3. Deliberate Practice "Practice Schedule" -> Atomic Habits "Implementation Intention"
4. Pomodoro "Daily Completion Rate" -> Atomic Habits "Habit Tracking"

**Expected outcome:** Structured skill development with daily accountability

---

### Pattern 3: Health Transformation (Health Domain)

**Sequence:** Health Belief Model -> SMART Goals -> Progressive Overload -> Macro Tracking -> Habit Loop

**Time estimate:** 3-4 hours total

**Data flow:**
1. HBM "Perceived Benefits" -> SMART "Relevant (Why)" (benefits = goal rationale)
2. HBM "Cues to Action" -> Habit Loop "Cue" (external cues = habit triggers)
3. SMART "Measurable Target" -> Progressive Overload "Target" (fitness goal = training target)
4. Progressive Overload "Training Sessions" -> Macro Tracking "Meal Plan" (nutrition timing)
5. Macro Tracking "Daily Target" -> Habit Loop "Routine" (meal prep = daily habit)

**Expected outcome:** Behavior change supported by belief, structure, and habit

---

### Pattern 4: Financial Decision (Finance Domain)

**Sequence:** NPV Analysis -> DCF Model -> Monte Carlo Simulation -> Real Options -> Kelly Criterion

**Time estimate:** 6-10 hours total

**Data flow:**
1. NPV "Cash Flow Projections" -> DCF "Free Cash Flow" inputs
2. DCF "Revenue Growth Rate" -> Monte Carlo "Variable 1"
3. DCF "Operating Margin" -> Monte Carlo "Variable 2"
4. Monte Carlo "10th/50th/90th Percentile" -> Real Options "Decision Tree Scenarios"
5. Real Options "Expanded NPV" -> Kelly Criterion "Win Probability"

**Expected outcome:** Risk-adjusted investment decision with optimal sizing

---

### Pattern 5: Product Development (Business + Personal)

**Sequence:** Business Model Canvas -> OKRs -> GTD -> Pomodoro -> Growth Mindset

**Time estimate:** 4-5 hours total

**Data flow:**
1. BMC "Key Activities" -> OKR "Initiatives"
2. OKR "Key Results" -> GTD "Projects"
3. GTD "Next Actions" -> Pomodoro "Task List"
4. Pomodoro "Daily Summary" -> OKR "Progress Tracking"
5. OKR "Setbacks" -> Growth Mindset "Reflection"

**Expected outcome:** Strategic product goals executed daily with continuous learning

---

### Pattern 6: Competitive Analysis (Business)

**Sequence:** SWOT Analysis -> Porter's Five Forces -> Business Model Canvas

**Time estimate:** 3-5 hours total

**Data flow:**
1. SWOT "Threats" -> Porter's "Competitive Rivalry" assessment
2. SWOT "Opportunities" -> Porter's "Threat of New Entrants" analysis
3. Porter's "Bargaining Power of Suppliers" -> BMC "Key Partnerships" strategy
4. Porter's "Strategic Implications" -> SWOT "TOWS Strategies" refinement
5. BMC "Cost Structure" -> SWOT "Weaknesses" (if high cost identified)

**Expected outcome:** Comprehensive competitive positioning with actionable strategies

---

### Pattern 7: Athletic Performance (Health)

**Sequence:** SMART Goals -> Progressive Overload -> Macro Tracking -> Recovery Protocol -> Habit Loop

**Time estimate:** 3-4 hours total

**Data flow:**
1. SMART "Measurable Target" -> Progressive Overload "Target Performance"
2. Progressive Overload "Volume/Intensity Schedule" -> Macro Tracking "Calorie Target"
3. Progressive Overload "Deload Protocol" -> Recovery Protocol "Load Management"
4. Macro Tracking "Meal Plan" -> Habit Loop "Routine"
5. Recovery Protocol "Sleep Target" -> Habit Loop "Cue (Bedtime)"

**Expected outcome:** Peak performance through training, nutrition, and recovery integration

---

### Pattern 8: Time Management Overhaul (Personal)

**Sequence:** Eisenhower Matrix -> GTD -> Pomodoro -> Atomic Habits

**Time estimate:** 3-4 hours total

**Data flow:**
1. Eisenhower "Q2 (Important, Not Urgent)" -> GTD "Projects"
2. Eisenhower "Q3 (Urgent, Not Important)" -> GTD "Waiting For (Delegate)"
3. GTD "Next Actions" -> Pomodoro "Task List"
4. Pomodoro "Daily Plan" -> Eisenhower "Weekly Analysis" (time-per-quadrant)
5. Eisenhower "Q2 Time Target" -> Atomic Habits "Make It Obvious" (block Q2 time)

**Expected outcome:** Shift from reactive (Q1/Q3) to proactive (Q2) work

---

### Pattern 9: Investment Portfolio (Finance)

**Sequence:** CAPM -> Kelly Criterion -> Monte Carlo -> Real Options

**Time estimate:** 4-6 hours total

**Data flow:**
1. CAPM "Expected Return" -> Kelly "Win Payoff (b)"
2. CAPM "Beta" -> Monte Carlo "Variable (Volatility)"
3. Monte Carlo "P(Success)" -> Kelly "Win Probability (p)"
4. Kelly "Optimal %" -> Real Options "Initial Investment Size"
5. Real Options "Expansion NPV" -> Kelly "Recalculate after new info"

**Expected outcome:** Optimal portfolio allocation with staged investment strategy

---

### Pattern 10: Habit Formation (Personal + Health)

**Sequence:** Health Belief Model -> Habit Loop -> Atomic Habits -> Pomodoro

**Time estimate:** 2-3 hours total

**Data flow:**
1. HBM "Cues to Action" -> Habit Loop "Cue"
2. HBM "Perceived Benefits" -> Habit Loop "Reward"
3. Habit Loop "Cue-Routine-Reward" -> Atomic Habits "4 Laws" mapping
4. Atomic Habits "2-Minute Rule" -> Pomodoro "Minimum task size"
5. Pomodoro "Daily Completion" -> Atomic Habits "Habit Tracker"

**Expected outcome:** Sustainable behavior change with daily execution

---

## 12. Common Pitfalls and Solutions

### Pitfall 1: Template Overload

**Problem:** User tries to apply too many frameworks to one project, creating analysis paralysis and excessive overhead.

**Solution:** Enforce a soft limit of 3 active framework templates per project:
- 1 universal method (TRIZ if contradictions detected)
- 1 domain-specific framework (primary analysis tool)
- 1 project management template (Project Plan always active)

**Exception:** Multi-domain projects may use 2 domain frameworks (one per domain, maximum 4 total).

**Detection:** If user requests 4+ frameworks, suggest: "Consider focusing on the 2-3 most impactful frameworks first. You can always add more later."

---

### Pitfall 2: Premature Template Selection

**Problem:** User selects a framework before the domain is clear or before enough context is gathered from consilium.

**Solution:** Enforce step sequencing. Do not suggest domain frameworks until:
- Step 1-3 complete (idea collected, roles discovered, specialists matched)
- Step 4 consilium provides specialist recommendations
- Exception: TRIZ can be suggested at any point when contradictions are detected

**If user requests early:** "Great choice. Let us complete the consilium first so we can pre-populate the template with specialist insights. This saves you 30-50% of manual input."

---

### Pitfall 3: Template as Bureaucracy

**Problem:** User perceives templates as paperwork rather than thinking tools. Fills in minimum to "check the box."

**Solution:**
- Emphasize auto-population: User provides 20% input, system generates 80%
- Show value proposition: "This NPV analysis will feed directly into your scoring and deep plan, saving 2 hours of manual work later."
- Offer condensed mode: For simple projects, allow abbreviated template fills (required fields only)
- Never force optional templates

---

### Pitfall 4: Outdated Template Instances

**Problem:** User references an old template instance that uses obsolete practices or formulas.

**Solution:**
- Claude checks template version on load
- If template definition has been updated since instance creation, suggest upgrade:
  "This OKR instance was created with template v1.0. Version v1.1 adds better KR measurement guidance. Would you like to upgrade?"
- Never auto-upgrade; always ask user

---

### Pitfall 5: No Feedback Loop

**Problem:** Templates are used once and never evaluated for effectiveness. No learning happens.

**Solution:** Post-project prompt sequence:
1. "Rate this template's effectiveness (1-5 stars)"
2. "What worked well? What did not?"
3. "Would you use this framework again for similar projects?"
4. Store responses in Claude Flow memory
5. Use ratings to improve future suggestions (lower-rated frameworks suggested less)

---

### Pitfall 6: Ignoring Synergies

**Problem:** User uses frameworks in isolation, missing transformative combinations.

**Solution:**
- After first framework is selected, check synergy matrix for high-rated pairs
- Suggest complementary framework: "Your NPV analysis would be 40% more powerful with Monte Carlo simulation. It takes 90 minutes and quantifies the risk of your assumptions. Add it?"
- Only suggest 5-star and 4-star synergy pairs

---

### Pitfall 7: Skipping TRIZ When Contradictions Exist

**Problem:** User encounters contradictions (speed vs quality, cost vs features) but settles for compromise instead of resolution.

**Solution:**
- Auto-detect contradiction signals: "but", "however", "trade-off", "versus", "conflict between"
- Proactively suggest: "I notice a contradiction: {X} conflicts with {Y}. TRIZ Quick Pattern takes 5-10 minutes and often finds a resolution that avoids compromise."
- Frame TRIZ as fast (5-10 min for Quick mode), not as heavy methodology

---

### Pitfall 8: Disconnected Templates

**Problem:** Multiple frameworks filled out but not linked together. Data duplicated manually between templates.

**Solution:**
- Follow composition patterns (Section 11) for sequenced framework use
- Use auto-population rules (Section 6) for cross-framework data flow
- When creating second framework in a project, check for linkable data from first framework
- Show user the data flow: "I can pre-fill your VPC Pains section from your Lean Canvas Problems. Proceed?"

---

## 13. Quick Reference Tables

### Template Selection by Scenario

| Scenario | Recommended Templates | Est. Time |
|----------|----------------------|-----------|
| Launching a startup | Lean Canvas + OKRs + TRIZ Quick | 2-3 hours |
| Losing 20kg weight | HBM + Habit Loop + Progressive Overload | 1.5-2 hours |
| Learning a new skill | Deliberate Practice + Pomodoro + Growth Mindset | 1-1.5 hours |
| Evaluating an investment | NPV + Monte Carlo + Real Options | 3-5 hours |
| Career change decision | Eisenhower + SWOT + HBM + SMART Goals | 2-3 hours |
| Building a daily habit | Atomic Habits + Habit Loop + Project Journal | 45-60 min |
| Competitive market entry | SWOT + Porter's Five Forces + BMC | 4-5 hours |
| Productivity overhaul | GTD + Eisenhower + Pomodoro + Atomic Habits | 3-4 hours |
| Portfolio optimization | CAPM + Kelly Criterion + Monte Carlo | 3-4 hours |
| Training for marathon | SMART + Progressive Overload + Macros + Recovery | 3-4 hours |
| Side project validation | Lean Canvas + VPC + Pomodoro | 2-3 hours |
| Resolving a dilemma | TRIZ Quick or Structured + Eisenhower | 30-90 min |

### Template Integration Matrix: Template x Life OS Step

| Template | Step 1 | Step 2 | Step 3 | Step 4 | Step 4.5 | Step 5 | Step 6 | Step 7 | Step 8 | Step 9 |
|----------|--------|--------|--------|--------|----------|--------|--------|--------|--------|--------|
| **TRIZ Quick** | | | | [T] | Mode 1 | [T] | | | [T] | |
| **TRIZ Structured** | | | | [T] | Mode 2 | [T] | | | [T] | |
| **ARIZ Full** | | | | [T] | Mode 3 | | | | [T] | |
| **OKRs** | | | | Spec | | Criteria | Goal | | L2 | |
| **Lean Canvas** | | | | Spec | | Criteria | | | L3 | |
| **SWOT** | | | | Spec | | Scenarios | | | L2 | |
| **BMC** | | | | Spec | | Criteria | | | L3 | |
| **VPC** | | | | Spec | | Criteria | | | L3 | |
| **Porter's** | | | | Spec | | Criteria | | | L3 | |
| **NPV** | | | | | | Criteria | | | L2 | |
| **DCF** | | | | | | Enhance | | | L2 | |
| **Monte Carlo** | | | | | | Enhance | | | L3 | |
| **Real Options** | | | | | | Criteria | | | L2 | |
| **CAPM** | | | | | | Enhance | | | L3 | |
| **Kelly** | | | | | | Enhance | | | L3 | |
| **HBM** | Flag | | | Spec | | Criteria | | | L3 | |
| **SMART** | | | | | | | | | L4 | |
| **Habit Loop** | Flag | | | | | | Habits | | L5 | |
| **Prog. Overload** | | | | Spec | | | | Blocks | L2 | |
| **Macros** | | | | | | | | Meals | L3 | |
| **Recovery** | | | | | | | | Rest | L3 | |
| **Pomodoro** | | | | | | | Time | Schedule | L5 | |
| **Atomic Habits** | Flag | | | | | | Habits | | L5 | |
| **Eisenhower** | | | | | | Criteria | Priority | | L4 | |
| **GTD** | | | | | | | Lists | GTD cal | L4 | |
| **Growth Mindset** | Flag | | | | | | | | L3 | |
| **Delib. Practice** | | | | | | | | Sessions | L3 | |
| **Project Plan** | | | | | | | Create | | Target | |
| **Project Journal** | | | | | | | | | | Create |
| **Project Snapshot** | | | | | | | | | | Create |
| **Project Decisions** | | | | | | | Create | | | Update |

**Legend:**
- Flag = Auto-detect flag set for later steps
- Spec = Specialist-driven input
- [T] = Optional TRIZ menu item
- Mode 1/2/3 = TRIZ analysis modes
- Criteria = Provides MCDA scoring criteria
- Enhance = Enhances scoring with additional data
- Scenarios = Provides scenario analysis
- Create = Template instance created at this step
- Target = Output target for deep plan
- L2-L5 = Deep plan level contribution
- Lists/Habits/Time/etc. = Specific integration type

### Template Complexity Ranking

| Tier | Frameworks | Time Range | Cognitive Load |
|------|-----------|------------|----------------|
| **Simple** (30-60 min) | Pomodoro, Eisenhower, SMART, Habit Loop, Growth Mindset, TRIZ Quick, CAPM | 15-60 min | Low |
| **Moderate** (1-2 hr) | OKRs, SWOT, Lean Canvas, VPC, Atomic Habits, NPV, Kelly Criterion, HBM, Progressive Overload, Macro Tracking, Recovery, Deliberate Practice | 30-120 min | Medium |
| **Complex** (2-4 hr) | BMC, Porter's Five Forces, DCF, Monte Carlo, Real Options, GTD Setup, TRIZ Structured, ARIZ Full | 90-240 min | High |
| **Intensive** (4+ hr) | Full portfolio analysis with multiple frameworks, Complete composition pattern | 4-10 hours | Very High |

---

## 14. Future Enhancements

### Phase 3: Auto-Suggest Engine (Planned: 3-4 weeks)

- Automatic template suggestion based on keywords, consilium output, and scoring results
- Confidence scoring for suggestions (e.g., "85% confidence OKRs is right for this project")
- A/B testing of suggestion algorithms using memory feedback data
- Learns from user acceptance/rejection patterns

### Phase 4: Full Ecosystem (Planned: 4-6 weeks)

- Template composition orchestrator: automatically sequences frameworks in optimal order
- Cross-template data flows: VPC -> Lean Canvas auto-link with one click
- Template marketplace: community-contributed domain-specific variations
- Industry-specific adaptations (e.g., "SaaS-specific BMC", "Marathon-specific Progressive Overload")

### Machine Learning Integration (Future)

- Learn from user template selections -> personalized recommendations
- Predict template effectiveness before use: "OKRs have 85% success rate for projects like yours"
- Auto-tune templates: "Your NPV discount rate is typically 12% based on past analyses, pre-fill?"
- Cross-user learning (anonymized): "Projects similar to yours used Lean Canvas + OKRs 73% of the time"

### Template Analytics Dashboard (Future)

- Framework usage frequency across all projects
- Average effectiveness rating per framework
- Time invested vs. value generated correlation
- Most common synergy patterns discovered by users
- Contradiction types most frequently resolved by TRIZ

---

## Appendix A: Framework Complexity Matrix

| Framework | Domain | Complexity | Est. Time | Recommended For | Prerequisites |
|-----------|--------|------------|-----------|-----------------|---------------|
| **Business Model Canvas** | Business | Medium | 60-90 min | Startup, new product | None |
| **OKR Framework** | Business | Low | 30-45 min | Goal setting, alignment | None |
| **SWOT Analysis** | Business | Low | 30-60 min | Strategic planning | None |
| **Lean Canvas** | Business | Medium | 45-75 min | Lean startup, MVP | None |
| **Value Proposition Canvas** | Business | Medium | 45-60 min | Product-market fit | Lean Canvas (optional) |
| **Porter's Five Forces** | Business | High | 90-120 min | Competitive analysis | Industry research |
| **NPV Analysis** | Finance | Medium | 60-90 min | Investment decision | Cash flow projections |
| **DCF Model** | Finance | High | 120-180 min | Valuation | Financial modeling skills |
| **Monte Carlo Simulation** | Finance | High | 90-150 min | Risk analysis | NPV or DCF |
| **Real Options** | Finance | High | 120-180 min | Flexibility valuation | NPV, probability theory |
| **CAPM** | Finance | Low | 30-45 min | Required return | Basic finance |
| **Kelly Criterion** | Finance | Medium | 45-60 min | Position sizing | Probability estimates |
| **Health Belief Model** | Health | Low | 30-45 min | Behavior change | None |
| **SMART Goals** | Health | Low | 15-30 min | Goal setting | None |
| **Habit Loop** | Health | Low | 20-30 min | Habit formation | None |
| **Progressive Overload** | Health | Medium | 45-60 min | Training plan | Fitness baseline |
| **Macro Tracking** | Health | Medium | 60-90 min | Nutrition plan | Body metrics |
| **Recovery Protocol** | Health | Medium | 45-60 min | Recovery optimization | Training program |
| **Pomodoro Technique** | Personal | Low | 15-20 min | Daily planning | Task list |
| **Atomic Habits** | Personal | Low | 30-45 min | Habit building | None |
| **Eisenhower Matrix** | Personal | Low | 20-30 min | Prioritization | Task list |
| **GTD System** | Personal | High | 90-120 min | Productivity system | Commitment to process |
| **Growth Mindset** | Personal | Low | 20-30 min | Reflection, learning | Recent challenge |
| **Deliberate Practice** | Personal | Medium | 45-60 min | Skill development | Skill baseline |
| **TRIZ Quick** | Universal | Low | 5-10 min | Fast contradiction wins | Identified contradiction |
| **TRIZ Structured** | Universal | Medium | 30-60 min | Important contradictions | Identified contradiction |
| **ARIZ Full** | Universal | High | 120-240 min | Strategic contradictions | Deep domain knowledge |
| **Project Plan** | Project Mgmt | Medium | 30-60 min | Every project | Scoring complete |
| **Project Journal** | Project Mgmt | Low | 5-10 min/entry | Every project | Project plan exists |
| **Project Snapshot** | Project Mgmt | Low | 10-15 min | Status reviews | Project plan exists |

---

## Appendix B: Template YAML Frontmatter Reference

Every framework template instance must include this standard frontmatter:

```yaml
---
# METADATA (Auto-populated from workflow plan)
framework: "[Framework Name]"
framework_slug: "[kebab-case-name]"
domain: "[business|finance|health|personal|universal|project]"
template_version: "1.0"
applied_to_project: "[project_id from workflow-plan.md]"
project_name: "[Auto-filled]"
created_date: "[YYYY-MM-DD]"
completed_date: "[YYYY-MM-DD or null]"

# INTEGRATION HOOKS
integration_step: "[1|4|4.5|5|6|7|8|9]"
time_invested_minutes: 0
consilium_specialist: "[Matched from step-04 if applicable]"

# SCORING IMPACT
scoring_contribution:
  provides_criteria: [true|false]
  provides_weights: [true|false]
  provides_scenarios: [true|false]
  mcda_dimensions: ["Dimension 1", "Dimension 2"]

# DEEP PLAN IMPACT
deep_plan_contribution:
  generates_l2_headings: [true|false]
  generates_l3_tasks: [true|false]
  generates_milestones: [true|false]

# COMPOSITION
linked_frameworks: []
prerequisite_frameworks: []
follows_frameworks: []
---
```

---

## Appendix C: Cross-Reference Index

### Files That Reference This Guide

| File | How It Uses This Guide |
|------|----------------------|
| `workflow.md` | Main workflow routes to templates via step instructions |
| `steps-c/step-04-consilium.md` | Uses specialist-framework mapping (Section 6, Rule 2) |
| `steps-c/step-04.5-triz-analysis.md` | Uses TRIZ integration points (Section 2, Step 4.5) |
| `steps-c/step-05-scoring.md` | Uses scoring criteria mapping (Section 2, Step 5) |
| `steps-c/step-06-integration.md` | Uses template creation triggers (Section 7) |
| `steps-c/step-08-deep-plan.md` | Uses deep plan level mapping (Section 2, Step 8) |
| `steps-c/step-09-complete.md` | Uses completion triggers (Section 2, Step 9) |
| `data/domain-template-architecture.md` | Detailed template specifications referenced here |
| `data/domain-framework-integration.md` | Decision trees referenced in Section 4 |
| `data/framework-synergy-matrix.csv` | Synergy data referenced in Section 5 |

### Files This Guide References

| File | What This Guide Uses From It |
|------|------------------------------|
| `data/domain-template-architecture.md` | Template structure, framework specifications, composition patterns |
| `data/framework-synergy-matrix.csv` | 73 synergy pair ratings |
| `data/triz-quick-patterns.md` | 40 TRIZ principles, contradiction matrix |
| `data/deep-plan-templates.md` | L1-L6 planning templates |
| `data/roles-base-enhanced.csv` | Specialist framework expertise tags |
| `data/method-rankings.yaml` | Framework rankings by domain |
| `data/strategic-buckets.md` | Portfolio allocation buckets |
| `data/mcda-methodology.md` | Scoring criteria definitions |
| `data/integration-patterns.md` | Project integration patterns |
| `workflow-plan.md` | Project metadata for auto-population |

---

**Guide Version:** 1.0
**Last Updated:** 2026-02-04
**Next Review:** After Phase 3 Auto-Suggest Engine implementation
**Maintained By:** Life OS workflow system
