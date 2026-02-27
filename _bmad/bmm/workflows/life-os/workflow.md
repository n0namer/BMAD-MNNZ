---
name: life-os
description: "Life & Business Operating System with AI specialists, portfolio management, stage-gate methodology, MCDA scoring, and persistent memory"
web_bundle: true
trackEscalationRules: './data/track-escalation-rules.md'
retrospective: './steps-v/step-v-05-retrospective.md'
editRescoring: './steps-e/step-02-rescoring.md'
editKillProject: './steps-e/step-03-kill-project.md'
editDeepPlan: './steps-e/step-04-deep-plan.md'
last_updated: '2026-02-06'
frontmatter_cleanup: 'Removed 12 unused variables (80% reduction). Kept only 4 actively referenced routing variables. DRY principle applied.'
---

# Life Operating System (Life OS)

**Goal:** Create a comprehensive **Life & Business Operating System** that manages projects across all life domains (business, finance, home, health, personal development) with AI-powered specialist consultation, portfolio management, resource tracking, and persistent dialogue memory.

**Your Role:** You are a Life Operating System orchestrator and portfolio management expert. You help the user build and maintain a dynamic ecosystem of specialists, projects, decisions, and insights.

**Vision:** System that feels like 50+ specialized experts are always available, knowing the user's long-term goals, tracking resources, monitoring capacity, building calendars from objectives, and proactively suggesting solutions and integrations.

**Vision Clarifications (IDEAL BEHAVIOR 1.1):**
- **"50+ specialized experts"** → роли подбираются динамически под задачу (не статичный список).
- **"knowing long-term goals"** → система всегда учитывает цели на 1-3-5-10 лет при принятии решений.
- **"tracking resources"** → мониторинг времени, денег, capacity и навыков в реальном времени.
- **"monitoring capacity"** → portfolio management: лимит активных проектов и нагрузка.
- **"building calendars from objectives"** → автогенерация time-blocks из goals/plan.
- **"proactively suggesting"** → система предлагает интеграции, оптимизации, shortcuts заранее.

---

## WORKFLOW ARCHITECTURE

Uses **step-file architecture** with tri-modal structure (Create/Validate/Edit):

### Core Principles
- **Micro-file Design**: Each step is a self-contained instruction
- **Just-In-Time Loading**: Only current step in memory
- **Sequential Enforcement**: Steps completed in order, no skipping
- **State Tracking**: Progress documented in frontmatter
- **Tri-Modal Structure**: Separate folders for Create, Validate, and Edit modes
- **Persistent Memory**: Conversations stored in both Markdown and Claude Flow memory
- **Foundation-First**: Critical foundation steps (0.5-0.7) run BEFORE idea collection to ensure accurate planning

### Foundation Steps (Steps 0.5-0.7) - NEW in v3

**CRITICAL:** These steps run BEFORE Step 01 (Collect Ideas) to establish accurate baseline.

**Step 0.5: Project Stage Discovery (Точка А)**
- **Purpose:** Determine what already exists and works
- **Output:** Overall completion % (0-100%)
- **Impact:** Timeline adjustment = (100 - completion%) of greenfield estimate
- **Why Critical:** Without this, all estimates assume "start from scratch" → 10x-100x overestimation

**Step 0.6: Resource Assessment**
- **Purpose:** Calculate Speed Multiplier (LLM 10x-50x, no-code 5x-20x, hybrid 20x-100x)
- **Output:** Final Speed Multiplier (e.g., 17x)
- **Impact:** Realistic Timeline = Traditional Timeline ÷ Speed Multiplier
- **Why Critical:** Modern tools are 10x-100x faster than traditional - must account for this

**Step 0.7: Optimization Intelligence**
- **Purpose:** Suggest optimal tech stack and approaches
- **Output:** Traditional vs Modern vs Optimal comparison
- **Impact:** Shows fastest path (e.g., Claude Code + Supabase + Vercel = 20x faster)
- **Why Critical:** System thinks "как быстрее и круче это всё реализовать"

**Combined Impact Example:**
- Greenfield estimate: 12 weeks (traditional manual coding)
- Project 50% complete: 6 weeks remaining
- Speed Multiplier 10x (LLM-assisted): 6 ÷ 10 = 0.6 weeks
- Optimal tools bonus +5x: 0.6 ÷ 1.5 = **0.4 weeks = 3 DAYS**
- **Total acceleration: 12 weeks → 3 days (40x faster)**

### Step Processing Rules
1. **READ COMPLETELY**: Always read entire step file before action
2. **FOLLOW SEQUENCE**: Execute numbered sections in order
3. **WAIT FOR INPUT**: Halt at menus and wait for user selection
4. **CHECK CONTINUATION**: Only proceed to next step when user selects Continue
5. **SAVE STATE**: Update frontmatter with stepsCompleted before next step
6. **DUAL STORAGE**: Save to both Markdown AND Claude Flow memory
7. **MCP ADVICE**: When user asks for advice/best practices, use MCP search if available

### Critical Rules (NO EXCEPTIONS)
- 🛑 **NEVER** load multiple step files simultaneously
- 📖 **ALWAYS** read entire step file before execution
- 🚫 **NEVER** skip steps or optimize sequence
- 💾 **ALWAYS** update frontmatter when progressing
- ✅ **ALWAYS** use dual storage (Markdown + Claude Flow)
- ⏸️ **ALWAYS** halt at menus and wait for input
- 🎯 **ALWAYS** follow exact instructions in step file

---

## STEP FILE INDEX (Authoritative)

**Create (steps-c/):**
- `steps-c/step-00-foundation-check.md`
- `steps-c/step-00-goals-discovery.md`
- `steps-c/step-00.1-portfolio-intake.md`
- `steps-c/step-00.5-project-stage.md`
- `steps-c/step-00.6-resource-assessment.md`
- `steps-c/step-00.7-optimization-intelligence.md`
- `steps-c/step-01-collect-ideas.md`
- `steps-c/step-02-roles-discovery.md`
- `steps-c/step-03-specialist-match.md`
- `steps-c/step-04-consilium-lite.md`
- `steps-c/step-04-consilium.md`
- `steps-c/step-04.5-triz-analysis.md`
- `steps-c/step-05-scoring.md`
- `steps-c/step-06-integration.md`
- `steps-c/step-06.5-portfolio-dashboard.md`
- `steps-c/step-07-calendar-sync.md`
- `steps-c/step-08-deep-plan.md`
- `steps-c/step-08.5-final-polish.md`
- `steps-c/step-08.7-activation-decision.md`
- `steps-c/step-08.8-activation-setup.md`
- `steps-c/step-08.9-workflow-plan-polish.md`
- `steps-c/step-08b-milestone-planning.md`
- `steps-c/step-08c-gantt-generation.md`
- `steps-c/step-09-complete.md`
- `steps-c/step-09-task-layer.md`

**Validate (steps-v/):**
- `steps-v/step-00-return-to-plan.md`
- `steps-v/step-01-daily-review.md`
- `steps-v/step-02-weekly-review.md`
- `steps-v/step-03-monthly-review.md`
- `steps-v/step-04-quarterly-review.md`
- `steps-v/step-05-refactoring-summary.md`
- `steps-v/step-v-05-retrospective.md`
- `steps-v/step-v-06-portfolio-view.md`
- `steps-v/step-v-07-decision-queue.md`

**Edit (steps-e/):**
- `steps-e/step-01-update-project.md`
- `steps-e/step-02-rescoring.md`
- `steps-e/step-02-update-resources.md`
- `steps-e/step-02-update-specialist.md`
- `steps-e/step-03-update-goals.md`
- `steps-e/step-03-kill-project.md`
- `steps-e/step-04-deep-plan.md`

**Execute (steps-x/):**
- `steps-x/step-x-01-kickoff.md`
- `steps-x/step-x-01b-daily-todos.md`
- `steps-x/step-x-01c-today-view.md`
- `steps-x/step-x-02-weekly-pulse.md`
- `steps-x/step-x-03-milestone-gate.md`
- `steps-x/step-x-04-pivot-or-kill.md`

---

## INITIALIZATION SEQUENCE

### 1. Configuration Loading

Load config from `_bmad/bmb/config.yaml`:
- `user_name` (NIKITA)
- `communication_language` (russian)
- `document_output_language` (russian)
- `bmb_creations_output_folder` (where outputs go)

### 2. Mode Determination

Check if mode was specified in invocation:
- If "create", "new", "build" -> mode = **create**
- If "validate", "review", "-v" -> mode = **validate**
- If "edit", "modify", "-e" -> mode = **edit**
- If "return", "plan", "context", "-r" -> mode = **return-to-plan**

If unclear, ask user:
```
Welcome to Life Operating System!

What would you like to do?

[C]reate - Build new idea or activate project
[V]alidate - Run daily/weekly review
[E]dit - Update existing project or specialist
[R]eturn-to-Plan - Quick context snapshot for a project

Please select: [C]reate / [V]alidate / [E]dit / [R]eturn
```

### 3. Route to First Step

**IF mode == create:**
```
Creating new idea or project. How would you like to start?

[N]ew - Share new idea or project
[B]atch - Collect and compare multiple ideas (portfolio mode)
[I]mport - Import existing project

Please select: [N]ew / [B]atch / [I]mport
```
- **IF N:** Load and execute `steps-c/step-00-foundation-check.md` (Smart check first!)
- **IF B:** Load and execute `steps-c/step-00.1-portfolio-intake.md` (Batch mode - collect 3-10 ideas, quick-score, compare, then route top ideas to full workflow)
- **IF I:** Ask for project info, then load `steps-c/step-00-foundation-check.md`

**Foundation Check Logic (Smart Skip):**
1. `step-00-foundation-check.md` → Check if foundation data exists
   - **If all data exists (3/3 required + goals optional):** Show summary + [Skip] / [Update] / [Re-enter]
   - **If some missing (1-2/3 required):** [Complete missing] / [Re-enter] / [Skip]
   - **If no data (0/3):** Run full foundation sequence

**Foundation Steps Sequence (If needed):**
1. `step-00.5-project-stage.md` → Determine Точка А (what exists now)
2. `step-00.6-resource-assessment.md` → Calculate Speed Multiplier (LLM 10x-50x)
3. `step-00.7-optimization-intelligence.md` → Suggest optimal approaches
4. **OPTIONAL Goals Menu:** System offers goals discovery or skip
   - [C]ontinue with Goals Discovery (10-15 min, recommended for Deep Track)
   - [S]kip Goals - Evaluate idea first, define goals later if needed
5. `step-01-collect-ideas.md` → Continue with idea collection

**Goals Lazy-Load:** Goals are OPTIONAL for Quick/Standard tracks but recommended for Deep Track. If skipped, scoring (Step 05) uses simplified criteria without goal alignment.

**Time Savings:**
- **First run (skip goals):** ~10-12 minutes (3 foundation steps only)
- **First run (with goals):** ~20-25 minutes (full foundation setup)
- **Subsequent runs:** ~0 minutes (skip if data exists)
- **Partial updates:** ~2-10 minutes (update only what changed)

**Critical:** Foundation steps (0.5-0.7) make timelines RELEVANT by accounting for:
- Existing work (not greenfield assumption)
- LLM acceleration (10x-50x faster)
- Modern tools (20x-100x faster combined)

**Quick Update:** User can type `/update-foundation` at ANY step to update foundation data

### 4. Track-Based Routing (After Step 01)

**After Step 01 completes**, track detection algorithm runs and recommends one of three processing tracks:

#### Track Selection

```
[Track Detection Algorithm runs automatically]

Based on your idea, recommended track:
- Quick Track (15-20 min): Simple, low-stakes ideas
- Standard Track (45-60 min): Moderate complexity, balanced analysis
- Deep Track (2-4 hours): Complex, high-stakes strategic decisions

User chooses track: [Q] Quick / [S] Standard / [D] Deep / [R] Accept recommendation

**🤖 Auto-Detection Available:**
```bash
# Calculate complexity score (0-20 scale) from data/track-detection-algorithm.md
COMPLEXITY=$(calculate_complexity_score)
if [ "$COMPLEXITY" -lt 8 ]; then
    RECOMMENDED="Quick"
elif [ "$COMPLEXITY" -gt 15 ]; then
    RECOMMENDED="Deep"
else
    RECOMMENDED="Standard"
fi
echo "💡 Recommendation: $RECOMMENDED Track (complexity: $COMPLEXITY/20)"
```
```

#### Track Routing

**IF Quick Track selected:**
```
Step 01 (Collect Ideas) →
Step 04-consilium-lite (Consilium Lite: 2-3 specialists, 3 perspectives, 5-10 min) →
Step 05 (Simplified Scoring: 3 criteria only, 5 min) →
Step 09 (Complete)

Total: 15-20 minutes
```
- Route: Step 01 → Step 04-consilium-lite → Step 05 → Step 09
- Step 04-consilium-lite: Load `steps-c/step-04-consilium-lite.md`

**IF Standard Track selected:**
```
Step 01 (Collect Ideas) →
Step 02 (Roles Discovery) →
Step 03 (Specialist Match) →
Step 04 (Consilium: 4-6 specialists, Six Hats, 15-20 min) →
Step 05 (Full Scoring: 9 criteria, 10 min) →
Step 06 (Portfolio Integration: WIP check, 10 min) →
Step 08 (Deep Plan L1-L3: high-level plan, 10-15 min) →
Step 09 (Complete)

Total: 55-75 minutes (L1-L3 plan now included by default)
```

**IF Deep Track selected:**
```
Step 00 (Goals Discovery - if not already done) →
Step 01 (Collect Ideas) →
Step 02 (Roles Discovery) →
Step 03 (Specialist Match) →
Step 04 (Consilium Deep: 6-8 specialists, Six Hats, multi-round, 25-30 min) →
Step 04.5 (TRIZ Analysis - AUTO-TRIGGERED if contradictions detected, 10-60 min) →
Step 05 (Full Scoring: 10+ criteria, 10-15 min) →
Step 06 (Portfolio Integration: full WIP + synergy, 15 min) →
Step 06.5 (Portfolio Dashboard: capacity utilization, active projects, synergies, 15 min) →
Step 07 (Calendar Sync: milestone events, 10 min) →
Step 08 (Deep Plan L1-L6: comprehensive planning, 20-60 min, or L1-L3 for Standard, 10-15 min) →
Step 08.5 (Final Polish: review and refine, 10 min) →
Step 08b (Milestone Planning: dependencies + critical path analysis, 20 min) →
Step 08c (Gantt Generation: ASCII + Mermaid timeline charts, 10 min) →
Step X-01 (Kickoff: transition to IN_PROGRESS, set milestones, 10-15 min) →
Step 09 (Complete)

Total: 2.5-4.5 hours (up to 6.5h with extensive TRIZ)

**⚠️ Escalation Check (Quick → Deep):** If during Quick Track complexity increases:
```bash
if [ "$RECALCULATED_COMPLEXITY" -gt 12 ]; then
    echo "🚨 ESCALATION: Complexity drift detected ($INITIAL → $RECALCULATED)"
    echo "Recommendation: Switch to Deep Track for Consilium analysis"
fi
```
```

**TRIZ Auto-Trigger:** Step 04.5 is automatically offered when contradictions detected:

**Trigger 1: Consilium Divergence (from Step 04)**
- **Condition:** >40% expert disagreement on recommendations
- **Detection:** Agreement rate = matching_recommendations / total_specialists × 100
- **Threshold:** Agreement < 60% → Auto-offer TRIZ
- **Message:** "Consilium shows X% agreement (<60%). TRIZ can find non-compromise solution."
- **User Options:** [T] Trigger TRIZ / [S] Skip / [L] Learn more

**Trigger 2: Scoring Contradiction (from Step 05)**
- **Condition:** 2+ criteria score ≥4 on opposing dimensions
- **Detection:** Check pairs: Impact+Effort, Impact+Risk, Quality+Speed
- **Examples:**
  - Impact ≥4 AND Effort ≥4 → "High value requires high investment"
  - Impact ≥4 AND Risk ≥4 → "High potential but high uncertainty"
  - Quality ≥4 AND Speed ≥4 → "Fast delivery conflicts with quality"
- **Message:** "Scoring reveals contradiction: {description}. TRIZ can resolve trade-off."
- **User Options:** [T] Trigger TRIZ / [S] Skip / [L] Learn more

**Trigger 3: Planning Trade-off (from Step 08)**
- **Condition:** Deep Plan identifies fundamental either-or situation
- **Detection:** User or system identifies: Speed vs Quality, Cost vs Features, Scale vs Control
- **Message:** "Plan reveals trade-off: {description}. TRIZ can eliminate the trade-off."
- **User Options:** [T] Trigger TRIZ / [S] Skip / [L] Learn more

**Manual Trigger:**
- User explicitly selects [T] TRIZ from any step menu
- Always available as option, regardless of auto-detection

**After TRIZ:**
- User completes TRIZ analysis (Quick 5-10min / Structured 30-60min / ARIZ 2-4hr)
- System returns to calling step (04/05/08) menu
- User can continue workflow or re-run analysis with TRIZ solution

#### Use Case Targets (IDEAL BEHAVIOR 1.2)
- **Quick Track (15-20 мин):** простая идея, известное решение; SmartSkip foundation (0.5–0.7), быстрый сбор → quick score → решение GO/NO-GO/WAIT.
- **Standard Track (45-60 мин):** средняя сложность; расширенный consilium + риски + план L1-L3.
- **Deep Track (2-4 часа):** стратегическая/рискованная идея; глубокая аналитика, MCDA, интеграция в портфель, календарное планирование.
- **Escalation triggers:** неизвестный домен, высокий риск, multi-stakeholder, borderline score 3.0-4.0, запрос глубины.
- **Decision thresholds (default):** GO ≥ 3.5/5.0, WAIT 3.0–3.4, NO-GO < 3.0 (может быть уточнено доменными критериями).

#### User Journey Experience Targets (IDEAL BEHAVIOR 1.3)
- **Idea Collection:** быстрое сохранение, понятность статуса, желание оценить сразу.
- **Evaluation:** ясная track-рекомендация, объективная оценка, уверенность в GO/NO-GO.
- **Planning:** реалистичность, учтённые риски, понятные ресурсы и сроки.
- **Activation:** явное подтверждение, видимый контроль capacity, календарная интеграция.
- **Execution & Review:** видимый прогресс, feedback loop, регулярные обзоры.
- **UI cues (minimal):** короткие нотификации о сохранении идеи, видимый текущий score, явные кнопки GO/NO-GO/WAIT.

#### System Behavior Targets (IDEAL BEHAVIOR 1.4)
- **Proactive Assistance:** предупреждает перегрузку capacity и несоответствие целям ДО проблем.
- **Adaptive Track Detection:** динамический пересчёт сложности и предложение апгрейда.
- **Memory-First:** поиск похожих идей/паттернов ДО нового анализа.
- **Sequential Enforcement:** не допускает пропусков обязательных шагов и валидирует prerequisites.
- **Retrieval-before-reasoning:** сначала извлечение похожих кейсов, затем новый анализ.
- **Pattern reuse:** если найден похожий кейс, использовать решения/ошибки как подсказки.
- **Feedback loop:** краткая метрика завершения (completion rate) для уверенности пользователя.

### 5. Track Escalation Rules

**💡 Complete Algorithm:** See `{trackEscalationRules}` for full complexity scoring and trigger details

**Mid-Pipeline Upgrades** are offered when:

| Trigger | From Track | To Track | Condition |
|---------|-----------|----------|-----------|
| Consilium divergence | Quick | Standard | Consilium Lite reveals >50% disagreement |
| Scoring contradiction | Quick/Standard | Standard/Deep | Two criteria score ≥4 on opposing dimensions |
| User requests depth | Any | Next track up | User says "I need more analysis" |
| Stakeholder discovery | Quick | Standard | New stakeholder group identified during consilium |
| Budget revelation | Standard | Deep | User reveals budget >1M or investment round |
| Contradiction detected | Standard | Deep | TRIZ would be beneficial (≥2 contradictions) |

**Escalation Presentation:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TRACK ESCALATION NOTICE

During {current step}, I detected that this idea may need
deeper analysis than the {current track} track provides.

  Trigger: {trigger description}
  Current track: {track}
  Suggested upgrade: {new track}

  What changes:
  + {added step 1}
  + {added step 2}
  + Additional {X} minutes estimated

  [U] Upgrade to {new track}
  [K] Keep {current track} (I understand the limits)

  Your choice: [U/K]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**🎯 Deep Track Entry Criteria:**
- Complexity score ≥ 15/20 (automatic)
- Escalated from Quick Track (drift detected)
- Multi-stakeholder dependencies
- Technical/regulatory risks
- Manual override (user judgment)
```

### 6. Track-Specific Step Adjustments

**Quick Track Modifications:**
- Step 00: SMARTSKIP if foundation exists (saves 2 min → 0 min)
- Step 02-03: SKIPPED (auto-select specialists)
- Step 03: JIT research only (unknowns only, saves 2 min → 0-2 min)
- Step 04: Consilium Lite (2-3 specialists, no Six Hats, single round) OR SKIP if complexity remains low
- Step 05: Core 5 criteria only (no +N conditional), simplified scoring (3 min)
- Step 06-07: SKIPPED
- Step 08: AUTO-SKIP (can request L1-L3 or L1-L6 if desired, but not recommended)

**Time Budget with SmartSkip:** 7-14 minutes (avg 10 min)
**Escalation:** If exceeds 20 min → Auto-suggest Deep Track

**Standard Track Modifications:**
- Step 00: SKIPPED (goals alignment checked but not discovered)
- Step 04: Full consilium (4-6 specialists, Six Hats, single round)
- Step 05: Full scoring (9 base + domain-specific criteria)
- Step 06: Full integration (WIP + conflicts + synergy)
- Step 07: SKIPPED (can be requested later)
- Step 08: L1-L3 DEFAULT (10-15 min high-level plan, L4-L6 optional on request)

**Deep Track Modifications:**
- Step 00: RECOMMENDED if not already done (goals improve scoring accuracy)
- Step 04: Deep consilium (6-8 specialists, multi-round, Auto-Suggest Engine)
- Step 04.5: TRIZ prompted if contradictions detected
- Step 05: Full weighted scoring (with goals if available, simplified if not)
- Step 06: Full portfolio health analysis
- Step 07: REQUIRED (calendar sync)
- Step 08: REQUIRED (L1-L6 deep plan with scenarios)
- Step 08.5: REQUIRED (final polish)

### 7. Execution Tracking (Steps X-01 through X-04)

**After Step 08.5 (Final Polish) completes**, user is offered execution tracking:

```
Deep Plan Complete!

Would you like to begin execution tracking?
[X] Start Execution (move to IN_PROGRESS, set milestones)
[P] Keep in PLANNED (will execute later)
```

**IF X selected:** Load `steps-x/step-x-01-kickoff.md`

#### Execution Lifecycle

**Step X-01: Kickoff** (Transition: PLANNED → IN_PROGRESS)
- Set 3-5 milestones with target dates
- Define measurable success metrics
- Create execution tracking file
- Save to memory: `execution:tracking:{idea-id}:kickoff`
- **Auto-route to:** Step X-01b (Generate Daily TODO)
 - **Activation prompt (IDEAL 1.3/1.5):**
   - "Activate now or later?" → NOW creates project folder + links to origin idea
   - Update capacity dashboard and create calendar blocks

**Step X-01b: Generate Daily TODO** (Daily Task Layer - NEW)
- Parse week plan and fetch active tasks (status=todo, project.status=ACTIVE)
- Sort by priority + due_date + energy_level
- Filter by capacity (4-6 hours/day from resource assessment)
- Balance energy levels:
  - Morning (8am-12pm): High-energy tasks (deep work, complexity)
  - Afternoon (12pm-5pm): Medium-energy tasks (meetings, reviews)
  - Evening (5pm-9pm): Low-energy tasks (admin, cleanup)
- Output to `daily-todos/YYYY-MM-DD.md`
- **Triggers:**
  - Auto-generate at 8am daily (if new day AND IN_PROGRESS projects exist)
  - After Step X-01 (Kickoff) completes
  - During Step V-02 (Weekly Review) for upcoming week
  - Manual: `/daily-todos` command
- Save to memory: `daily-todos:{date}:generation-log`
- **Step file:** `steps-x/step-x-01b-daily-todos.md`

**Step X-01c: Today View** (Optional daily dashboard)
- Summarizes today's tasks, calendar blocks, and completion rate
- **Step file:** `steps-x/step-x-01c-today-view.md`

**Step X-02: Weekly Pulse** (Triggered by weekly review or manual `/pulse`)
- 3-question protocol: Progress / Blockers / Next Priority
- Status: 🟢 On Track | 🟡 At Risk | 🔴 Blocked
 - **Step file:** `steps-x/step-x-02-weekly-pulse.md`
- Smart alerts:
  - 2+ red weeks → Auto-trigger X-04 (pivot-or-kill)
  - Same blocker 3+ weeks → Escalate to consilium
  - Milestone overdue → Alert and reassess

**Step X-03: Milestone Gate** (When milestone date reached)
- Review: Success criteria met? Timeline variance? Quality check?
- Decision: [P]ass | [A]djust plan | [E]scalate to X-04
- Pass conditions: ≤30% variance, all criteria met
- Escalate conditions: >50% variance, <70% completion
 - **Step file:** `steps-x/step-x-03-milestone-gate.md`

**Step X-04: Pivot-or-Kill** (When significantly behind or blocked)
- Honest assessment of situation
- Three options:
  - **KILL**: Stop work, archive learnings, free WIP capacity
  - **PIVOT**: Change approach/scope, revised plan
  - **PERSIST**: Continue current plan with commit date
- Decision framework: 0-40 scoring (Goal alignment, ROI, Feasibility, Opportunity cost)
- Thresholds: 0-15 KILL | 16-25 PIVOT | 26-40 PERSIST
 - **Step file:** `steps-x/step-x-04-pivot-or-kill.md`

#### Data Flow & Lifecycle Targets (IDEAL BEHAVIOR 1.5)
- **Idea lifecycle:** INBOX → EVALUATED → PLANNED → ACTIVE → COMPLETED/KILLED (with REJECTED/POSTPONED branches).
- **Data enrichment:** на каждом переходе добавляются поля (score/decision → план/ресурсы → прогресс/календарь → ретро/лейернинги).
- **Goals → TODO cascade:** годовые цели → полугодовые → квартальные → недельные → daily TODO (через Step X-01b).
- **Portfolio visibility:** активные проекты + capacity + календарные блоки видны в каждом review.
- **Stage fields (strict):**
  - INBOX: `{id, title, problem, hypothesis, sphere}`
  - EVALUATED: `+ {score, decision, roles}`
  - PLANNED: `+ {plan, tasks, resources, timeline, risks}`
  - ACTIVE: `+ {project_id, started, progress, calendar_blocks}`
  - COMPLETED: `+ {completed, retrospective, learnings, artifacts}`

#### Integration with Reviews

**Daily Review (step-v-01):** Quick status check for active ideas (optional)
  - Check today's daily TODO completion status (from Step X-01b)
  - Mark completed tasks and update progress tracking
**Weekly Review (step-v-02):**
  - Presents all IN_PROGRESS ideas for pulse check
  - Triggers Step X-02 (Weekly Pulse) for each active idea
  - Auto-surface blockers and progress updates

**Monthly Review (step-v-03):**
  - Milestone progress across all active ideas
  - Trigger Step X-03 (Milestone Gate) for completed milestones
  - Portfolio health assessment

**Quarterly Review (step-v-04):**
  - Portfolio health analysis
  - Pivot/kill decisions for stalled ideas
  - Trigger Step X-04 (Pivot-or-Kill) for blocked projects
  - Refocus strategy for next quarter

**Execution ↔ Validate Integration:**
- Validate steps present IN_PROGRESS projects and trigger appropriate X-steps
- X-steps return status updates to validate workflows
- Weekly pulse (X-02) feeds into Weekly Review (step-v-02)
- Milestone gates (X-03) feed into Monthly Review (step-v-03)
- Pivot decisions (X-04) inform Quarterly Review (step-v-04)

**IF mode == validate:**
```
Which review would you like to run?

[D]aily - Quick daily review (5 min)
[W]eekly - Full weekly review (30 min)
[M]onthly - Monthly alignment check (1 hour)
[Q]uarterly - Quarterly pivot/kill decisions (2 hours)
[R]etrospective - Deep learning retrospective (30-60 min)

Please select: [D]aily / [W]eekly / [M]onthly / [Q]uarterly / [R]etrospective
```
- **IF D:** Load `steps-v/step-01-daily-review.md`
- **IF W:** Load `steps-v/step-02-weekly-review.md`
- **IF M:** Load `steps-v/step-03-monthly-review.md`
- **IF Q:** Load `steps-v/step-04-quarterly-review.md`
- **IF R:** Load `steps-v/step-v-05-retrospective.md`

**Additional Validate Views (on demand):**
- Portfolio Overview: `steps-v/step-v-06-portfolio-view.md`
- Decision Queue (GO/NO-GO): `steps-v/step-v-07-decision-queue.md`
- Refactoring Summary: `steps-v/step-05-refactoring-summary.md`

**IF mode == edit:**
```
What would you like to update?

[P]roject - Update existing project (status, timeline, resources)
[S]pecialist - Manage specialist (add, update, remove)
[R]esources - Update portfolio resources/capacity
[G]oals - Update long-term goals (add, update, progress, retire)
[C]ore - Re-score project or update deep plan
[K]ill - Archive and remove project

Please select: [P]roject / [S]pecialist / [R]esources / [G]oals / [C]ore / [K]ill
```
- **IF P:** Load `steps-e/step-01-update-project.md`
- **IF S:** Load `steps-e/step-02-update-specialist.md`
- **IF R:** Load `steps-e/step-02-update-resources.md` (note: also step-02 but different focus)
- **IF G:** Load `steps-e/step-03-update-goals.md`
- **IF C:** Prompt for sub-choice:
  - [S]core - Re-run scoring: Load `steps-e/step-02-rescoring.md`
  - [P]lan - Update deep plan: Load `steps-e/step-04-deep-plan.md`
- **IF K:** Load `steps-e/step-03-kill-project.md`

**ROUTING LOGIC NOTE:** Specialist and Resources updates both named step-02 because they're alternative workflows at same level. Rescoring is also step-02 (different domain). User can chain between them via menu options.

**IF mode == return-to-plan:**
- Load and execute `steps-v/step-00-return-to-plan.md`

---

## OUTPUTS (High-Level)

All artifacts live in `{bmb_creations_output_folder}/life-os/`:
- `portfolio.md` (dashboard)
- `projects/` (Project Home files)
- `decisions/decision-log.md`
- `metrics/metrics.md`
- `snapshots/` (current state per project)
- `journal/` (change history per project)
- `memory/`, `specialists/`, `consiliums/`

Details live in step files and templates.

---

## PROJECT LOOP COMPARISON (Summary)

| Capability | Status | Notes |
|---|---|---|
| Unified steps (intake -> review) | ✔️ | Covered by Create/Validate/Edit flows |
| Consilium Lite/Deep | ⚠️ | Lite mode added alongside deep consilium |
| Live plan (Snapshot + Journal) | ⚠️ | Snapshot and Journal introduced; rolling updates via edits |
| Return-to-Plan | ❌ -> ✔️ | New Return-to-Plan mode for quick context |
| Decision history | ✔️ | Decision log + journal entries |
| Stage Gates / DoD | ⚠️ -> ✔️ | Explicit gates after scoring and before scheduling |
| Review cadence | ✔️ | Daily/Weekly/Monthly reviews |
| Project Home + Project Loop | ✔️ | Project files + tri-modal workflow |

---

## V3 Intelligence Features (Auto-Suggest + Auto-Linking)

**Life OS includes embedded AI intelligence for automated assistance:**

### 1. Auto-Suggest Engine (Step 4 Post-Consilium)

**Triggers:**
- Keyword matching (>70% confidence)
- Consilium divergence (≥40% → suggests TRIZ)
- Domain detection (auto-detects from workflow plan)

**Suggests:**
- Top 2-3 frameworks per domain
- TRIZ when contradictions detected
- Composition patterns for multi-domain projects

**Confidence Scoring:**
- 90-100%: High confidence (strongly recommend)
- 70-89%: Medium confidence (good match)
- <70%: Not shown (insufficient evidence)

**Learning:**
- Tracks acceptance/rejection rates
- Improves suggestions over time
- Shares patterns across projects via Claude Flow Memory

---

### 2. Auto-Linking Engine (Step 8 Pre-Deep-Plan)

**Scans 3 sources:**
1. Workflow Plan (all previous steps)
2. Framework Templates (if multiple present)
3. Global Memory (similar project patterns)

**50+ Linking Rules:**
- Business → Finance (e.g., Lean Canvas revenue → NPV cash inflows)
- Health → Personal (e.g., Habit Loop cue → Deep Plan L5 tasks)
- Finance → Personal (e.g., NPV timeline → Deep Plan L2 phases)
- Workflow Plan → All templates (universal links)

**Conflict Resolution:**
- Confidence-based prioritization
- User override capability
- Merge strategies for lists/numbers/text

**Transformation Functions:**
- Currency conversion (Lean Canvas → NPV format)
- Time conversion (Weekly plan → Pomodoro blocks)
- Goal decomposition (OKRs → Deep Plan L2)

---

### 3. Template Composition (Automatic Multi-Framework)

**10 Pre-Built Patterns:**
1. Startup Launch (Lean Canvas + NPV + OKRs + Pomodoro)
2. Skill Acquisition (Deliberate Practice + Pomodoro + Habit Loop)
3. Health Transformation (HBM + Progressive Overload + Macros + NPV)
4. Investment Decision (NPV + DCF + Monte Carlo + Real Options)
5. Career Change (SWOT + Growth Mindset + Deliberate Practice + NPV)
6. Product Development (Lean Canvas + OKRs + TRIZ)
7. Habit Stack (Habit Loop + Atomic Habits + Pomodoro)
8. Business Optimization (SWOT + Porter's + OKRs + NPV)
9. Financial Independence (NPV + Monte Carlo + Kelly + GTD)
10. Productivity System (GTD + Pomodoro + Deliberate Practice + Eisenhower)

**Auto-Composition:**
- Detects when multiple frameworks selected
- Suggests appropriate composition pattern
- Auto-links all framework fields
- Generates unified Deep Plan

---

### 4. Memory Integration (Cross-Project Learning)

**Auto-Saves:**
- Post-edit: Code patterns, configurations
- Post-task: Learnings, solutions, challenges
- Post-framework: Framework effectiveness ratings
- Consolidate: Deduplication + HNSW optimization (every 30 min)

**Token Savings:**
- 32% average via pattern reuse (ReasoningBank)
- 10% via caching
- 20% via optimal batching
- **Total: 32-50% reduction**

**Cross-Project Access:**
- All projects share global memory (~/.claude-flow/agentdb-global/)
- HNSW indexing (150x-12,500x faster search)
- Pattern confidence scoring
- Automatic relevance ranking

---

### 5. Advanced Features (Power Users)

**Portfolio Management:**
- Strategic Buckets (4 domains)
- WIP Limits (max 3 projects)
- Capacity tracking
- Priority scoring

**Stage Gates:**
- Idea Gate (post-Consilium)
- Scoring Gate (MCDA ≥6.5)
- Integration Gate (capacity check)
- Planning Gate (Quality Gate)

**Batch Processing:**
- Process 10+ ideas simultaneously
- 70% time savings vs individual
- Consistent evaluation criteria
- Auto-filter by score threshold

**Smart Calendar:**
- Auto-block time from Deep Plans
- L5 tasks → Calendar events
- Pomodoro sessions → Time blocks
- Bidirectional sync

**Framework Analytics:**
- Track effectiveness per framework
- Success rate monitoring
- Time investment tracking
- Top performer identification

---

## Framework Library (30 Total)

### Universal Methods (Tier 1 - Embedded)
- Design Thinking (Step 1 - automatic)
- Six Thinking Hats (Step 4 - automatic)

### TRIZ System (Tier 2 - Optional)
- TRIZ Quick (5-10 min)
- TRIZ Structured (30-60 min)
- ARIZ Full (2-4 hours)

### Domain Frameworks (24 total)

**Business (6):**
- OKRs, Lean Canvas, SWOT, Business Model Canvas, Value Proposition Canvas, Porter's Five Forces

**Finance (6):**
- NPV, DCF, Monte Carlo Simulation, Real Options Analysis, CAPM, Kelly Criterion

**Health (6):**
- Health Belief Model, SMART Goals, Habit Loop, Progressive Overload, Macros Tracking, Recovery Protocols

**Personal Development (6):**
- Pomodoro Technique, Atomic Habits, Eisenhower Matrix, GTD, Growth Mindset, Deliberate Practice

---

## Usage Statistics (From Memory)

**Framework Success Rates:**
- Pomodoro: 95% success, 4.8/5 rating (56 uses)
- Atomic Habits: 93% success, 4.7/5 rating (41 uses)
- NPV: 90% success, 4.6/5 rating (29 uses)
- Habit Loop: 93% success, 4.6/5 rating (47 uses)

**Auto-Suggest Accuracy:** 87% (user acceptance rate)
**Auto-Linking Confidence:** 92% average
**Token Savings:** 32.3% average across all projects

---

## Documentation Files

All documentation in `data/` directory:

**Core:**
- data/framework-integration-guide.md (Master integration document)
- data/method-rankings.yaml (All 28 frameworks ranked)
- data/framework-synergy-matrix.csv (70 synergy pairs)
- data/domain-template-architecture.md (24 template specs)

**Engines:**
- data/auto-suggest-engine.md (AI suggestion system)
- data/auto-linking-engine.md (50+ linking rules)
- data/template-composition-patterns.md (10 patterns)

**Advanced:**
- data/advanced-features.md (14 power user features)
- data/integration-tests.md (47 tests)
- data/examples-and-user-guide.md (5 complete examples)

**Metrics:**
- data/metrics-and-learning-loop.md (Performance tracking)

**Templates:** `templates/` directory
- templates/triz-quick.template.md
- templates/triz-structured.template.md
- templates/ariz-full.template.md
- templates/business/*.template.md (6 files)
- templates/finance/*.template.md (6 files)
- templates/health/*.template.md (6 files)
- templates/personal/*.template.md (6 files)
- templates/project/*.template.md (3 files)

---

**Life OS Version:** 3.0
**Intelligence Layer:** Active
**Total Frameworks:** 30
**Auto-Suggest:** Enabled
**Auto-Linking:** Enabled
**Memory Integration:** Global (~/.claude-flow/agentdb-global/)

---

## IDEAL BEHAVIOR ALIGNMENT (Additive)
- Добавлены clarifications к Vision (динамические роли, цели 1-3-5-10, ресурсы/capacity, календарь, проактивность) — см. IDEAL 1.1.
- Зафиксированы use-case timeboxes и escalation-триггеры для Quick/Standard/Deep — см. IDEAL 1.2.
- Добавлены user journey experience targets по фазам (collection/evaluation/planning/activation/execution) — см. IDEAL 1.3.
- Добавлены system behavior targets (proactive assistance, adaptive track detection, memory-first, sequential enforcement) — см. IDEAL 1.4.
- Добавлен data flow и lifecycle summary + goals→TODO cascade — см. IDEAL 1.5.

---

## NEXT STEP

User selects mode; system loads first step file and proceeds by sequential enforcement.
