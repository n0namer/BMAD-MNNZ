# IDEAL BEHAVIOR REFERENCE - Life OS Workflow System

**Created:** 2026-02-06
**Purpose:** Permanent reference document describing ideal behavior of Life OS system from all perspectives
**Use:** Reference for validation, critique, and future improvements

---

## 1.1 North Star Vision (Видение)

**Цитата из workflow.md:20-26:**
> "System that feels like 50+ specialized experts are always available, knowing the user's long-term goals, tracking resources, monitoring capacity, building calendars from objectives, and proactively suggesting solutions and integrations."

**Расшифровка идеального состояния:**
- 🎯 **"50+ specialized experts"** → Роли подбираются динамически под задачу (не статичный список)
- 🧠 **"knowing long-term goals"** → System ВСЕГДА знает цели на 1-3-5-10 лет и принимает решения на их основе
- 📊 **"tracking resources"** → Real-time monitoring: время, деньги, capacity, навыки
- 🔍 **"monitoring capacity"** → Portfolio management: сколько active projects (2/5 = 40% capacity)
- 📅 **"building calendars from objectives"** → Автогенерация time-blocks из goals.yaml
- 💡 **"proactively suggesting"** → System сам предлагает интеграции, оптимизации, shortcuts

---

## 1.2 Use Cases (Все случаи использования)

### USE CASE 1: Quick Track (15-20 мин)
**Когда:** Простая идея с известным решением, не требует deep research

**Идеальное поведение:**
1. **Foundation (5 мин):**
   - SmartSkip logic проверяет existing foundation data
   - Если данные есть → skip steps 0.5-0.7
   - Если нет → быстрый single-question сбор (Point A: X%, Speed: Yx, Tools: optimal)

2. **Collect Ideas (2 мин):**
   - Быстрый input идеи (title, problem, hypothesis)
   - Сохранение в `ideas-bank/inbox/idea-XXX-sphere-name.md`

3. **Roles (2 мин):**
   - AI подбирает 2-3 роли автоматически на основе keywords
   - User review и корректировка (опционально)

4. **Quick Scorecard (5 мин):**
   - 5+N критериев (5 базовых + domain-specific) оцениваются по 3-point scale (low/med/high)
   - Автоматический расчёт скора
   - Decision: GO/NO-GO/WAIT (на основе threshold 3.5/5.0)

5. **Output (1 мин):**
   - Если GO → Move to `ideas-bank/evaluated/`
   - Если NO-GO → Archive to `ideas-bank/archive/rejected/`
   - Если WAIT → Archive to `ideas-bank/archive/postponed/`

**Результат:** Идея оценена и принято решение за **15-20 минут**

**Triggers для escalation:**
- Complexity signals detected (unknown domain, high risk, multi-stakeholder)
- User requests deeper analysis ("нужен детальный план")
- Score borderline (3.0-4.0) → need more certainty

---

### USE CASE 2: Standard Track (45-60 мин)
**Когда:** Идея средней сложности, требует планирования и risk analysis

**Идеальное поведение:**
1. **Foundation (5-10 мин):**
   - SmartSkip или quick re-validation
   - Alignment check: идея vs goals.yaml

2. **Collect Ideas (5 мин):**
   - Detailed input (problem, solution, value proposition, constraints)
   - Sphere classification

3. **Roles (10 мин):**
   - AI предлагает 4-6 специалистов
   - User dialogue: "нужен ли X specialist?" → contextual suggestions
   - Finalization

4. **Deep Scorecard (20 мин):**
   - 5+N критериев с подробным обоснованием (1-5 scale)
   - Risk analysis: технический, рыночный, ресурсный
   - Dependencies check: блокеры, prerequisites

5. **Deep Planning (20 мин):**
   - Task breakdown (high-level)
   - Resource estimation (time, budget, skills)
   - Timeline (milestones)
   - Success metrics

6. **Decision + Next Steps (5 мин):**
   - GO → Move to `ideas-bank/planned/`
   - NO-GO/WAIT → Archive with learnings
   - If GO → Prompt: "Activate now or later?" (L2-S3)

**Результат:** Идея полностью оценена, есть готовый план за **45-60 минут**

---

### USE CASE 3: Deep Track (2-4 часа)
**Когда:** Сложная идея (стратегическая, высокий риск, инновационная)

**Идеальное поведение:**
1. **Foundation (15-20 мин):**
   - FULL run steps 0.5-0.7
   - Точная Point A оценка (50% vs 10% = 5x difference in timeline)
   - Speed Multiplier + Optimal Tools analysis

2. **Collect Ideas (10 мин):**
   - Comprehensive brief: problem, solution, alternatives, constraints, assumptions

3. **Roles (30 мин):**
   - AI предлагает 8-12 специалистов (включая domain experts)
   - Multi-round dialogue для refining team
   - Cross-functional roles (PM, UX, Tech Lead, QA, DevOps, Legal, Finance)

4. **Deep Scorecard (40-60 мин):**
   - 6 критериев + sub-criteria (детализация до 3 уровней)
   - MCDA (Multi-Criteria Decision Analysis) с весами
   - Risk modeling (Monte Carlo simulation для timeline uncertainty)
   - Sensitivity analysis (как изменение assumptions влияет на score)

5. **Deep Planning (60-90 мин):**
   - Epic breakdown → Stories → Tasks
   - Detailed resource planning (по ролям, по неделям)
   - Dependencies graph (critical path analysis)
   - Contingency plans (Plan B, Plan C)
   - Success criteria + KPIs + tracking plan

6. **Integration Planning (30 мин):**
   - Portfolio fit: как идея влияет на existing projects
   - Capacity check: есть ли resources (2/5 active → 3 slots available)
   - Calendar integration: когда можно начать (constraints)
   - Synergies: интеграция с existing projects

7. **Decision + Activation (10 мин):**
   - GO → Move to `ideas-bank/planned/`
   - Activation decision: NOW vs LATER (based on priority + capacity)
   - If NOW → Trigger L2-S3 (create project from idea)

**Результат:** Идея глубоко исследована, готова к немедленной активации за **2-4 часа**

---

## 1.3 User Journey Perspectives (Взгляд пользователя)

### PERSPECTIVE 1: Idea Collection Phase
**Что видит пользователь:**
- Simple form для input идеи (title, problem, hypothesis)
- AI instantly предлагает sphere classification
- Auto-save в `ideas-bank/inbox/`
- Notification: "Idea saved! Ready to evaluate when you are."

**Что должен чувствовать:**
- 😊 Легко и быстро (не более 2-5 минут)
- 🎯 Понятно, что идея сохранена и не потеряется
- 🚀 Желание сразу оценить (если Quick Track) или отложить на потом

---

### PERSPECTIVE 2: Evaluation Phase
**Что видит пользователь:**
- Track detection: "Эта идея кажется Quick/Standard/Deep. Подтверждаешь?"
- Roles suggestion: "Для этой идеи нужны: PM, Developer, Marketer. Добавить кого-то?"
- Scoring interface: Simple sliders (Quick) или detailed forms (Deep)
- Real-time score calculation: "Current score: 4.2/5.0 (HIGH priority)"

**Что должен чувствовать:**
- 🧠 "System понимает мою идею"
- ⚡ Процесс быстрый (не перегружен вопросами)
- 🎯 Оценка объективная (не моё субъективное мнение, а данные)
- ✅ Confidence в решении (GO/NO-GO основано на facts)

---

### PERSPECTIVE 3: Planning Phase
**Что видит пользователь:**
- Task breakdown: AI предлагает структуру, user refines
- Resource estimation: "Нужно 40 часов, 2 недели, $500 budget"
- Timeline visualization: Gantt chart или roadmap
- Risk highlights: "⚠️ Dependency on external API (risk: medium)"

**Что должен чувствовать:**
- 📋 "План реалистичный и выполнимый"
- 🔍 "Все риски учтены"
- 🚀 "Я готов начать"

---

### PERSPECTIVE 4: Activation Phase (Idea → Project)
**Что видит пользователь:**
- Prompt: "Ready to activate? This will create project folder and archive idea."
- Confirmation: "Project created! Origin idea: idea-007, New project: project-002"
- Dashboard update: "Active projects: 3/5 (60% capacity)"
- Calendar integration: "Time-blocks created for next 2 weeks"

**Что должен чувствовать:**
- 🎉 "Началось! Теперь это реальный проект"
- 📊 "Вижу, что capacity под контролем"
- 📅 "Время уже забронировано в календаре"

---

### PERSPECTIVE 5: Execution & Review Phase
**Что видит пользователь:**
- Daily TODO list: генерируется из week plan
- Progress tracking: "Story 2/9 complete (22%)"
- Daily review prompt: "End of day! Quick 5-min review?"
- Weekly review: "Week summary: 7/10 tasks done (70%)"

**Что должен чувствовать:**
- ✅ "Прогресс виден"
- 🎯 "Я не сбился с курса"
- 🔄 "Есть feedback loop, могу корректировать"

---

## 1.4 System Behavior Perspectives (Взгляд системы)

### BEHAVIOR 1: Proactive Assistance
**Что система делает:**
- Detects complexity signals → "Рекомендую Deep Track для этой идеи"
- Detects capacity overload → "У тебя уже 5/5 active projects. Завершить что-то перед активацией новой?"
- Detects alignment issue → "Эта идея не align'ится с твоими целями на 2026 год (Strategic Alignment: 2.0/5.0)"
- Suggests integrations → "Эта идея может использовать наработки из project-001 (synergy)"

**Принципы:**
- 🎯 Non-intrusive: предложения, не навязывание
- 🧠 Context-aware: знает goals, capacity, existing projects
- ⚡ Timely: предупреждает ДО проблемы, не после

---

### BEHAVIOR 2: Adaptive Track Detection
**Что система делает:**
- Анализирует keywords, domain, риски
- Scores complexity (0-100)
- Suggests track: <30 = Quick, 30-70 = Standard, >70 = Deep
- User может override: "Нет, хочу Quick для этой идеи"
- Auto-escalation: если в процессе Quick появляются complexity signals → "Рекомендую перейти на Standard"

**Принципы:**
- 📊 Data-driven: не guess, а анализ
- 🔄 Dynamic: может меняться в процессе
- 👤 User override: система предлагает, user решает

---

### BEHAVIOR 3: Memory-First Workflow
**Что система делает:**
- Каждый output сохраняется в dual storage (Markdown + Claude Flow memory)
- Retrieval BEFORE reasoning: "Искал похожие идеи → нашёл idea-003 (similar problem)"
- Pattern matching: "Прошлая идея из той же сферы была rejected (reason: ...). Применимо?"
- Learning: "У тебя 87% completion rate. Продолжай!"

**Принципы:**
- 💾 Never lose data
- 🔍 Reuse patterns (saves 32% tokens)
- 📈 Learn from history

---

### BEHAVIOR 4: Sequential Enforcement (BMAD)
**Что система делает:**
- Не позволяет skip шаги: "Step 02 cannot run until Step 01 complete"
- Validates prerequisites: "Roles list empty → cannot proceed to Step 04"
- Updates frontmatter: `stepsCompleted: [01, 02, 03]`
- Tri-modal routing: Create → Validate → Edit (чёткое разделение)

**Принципы:**
- 🚫 No shortcuts: качество > скорость
- ✅ Completeness: каждый шаг fully done
- 🔄 Can always go back (Edit mode)

---

## 1.5 Data Flow Perspectives (Взгляд на данные)

### FLOW 1: Idea Lifecycle
```
INPUT (User) → INBOX → EVALUATED → PLANNED → ACTIVE (Project) → COMPLETED/KILLED
                ↓         ↓            ↓
            REJECTED   POSTPONED   ACTIVATED
```

**Ключевые переходы:**
- INBOX → EVALUATED: После L1-S3 (scoring complete)
- EVALUATED → PLANNED: После L2-S1 (plan ready)
- PLANNED → ACTIVE: После L2-S3 (activation decision)
- ACTIVE → COMPLETED: После L3-S1 (retrospective done)
- ACTIVE → KILLED: После X-04 (kill decision)

**Данные на каждом этапе:**
- INBOX: `{id, title, problem, hypothesis, sphere}`
- EVALUATED: `+ {score, decision, roles}`
- PLANNED: `+ {plan, tasks, resources, timeline, risks}`
- ACTIVE: `+ {project_id, started, progress, calendar_blocks}`
- COMPLETED: `+ {completed, retrospective, learnings, artifacts}`

---

### FLOW 2: Goals → TODO Cascade
```
YEAR (2026 Goals)
    ↓ decompose
H1/H2 (6-month goals)
    ↓ decompose
Q1-Q4 (quarterly goals)
    ↓ decompose
MONTH (monthly goals)
    ↓ decompose
WEEK (weekly focus)
    ↓ generate
DAY (daily TODO)
    ↓ execute
COMPLETED TASKS
    ↓ review
WEEKLY REVIEW → adjust next week
```

**Критическая связь:**
- Каждая daily task имеет `goal_id` → трейсим back to year goal
- Weekly review проверяет прогресс к quarterly goal
- Quarterly review корректирует trajectory к year goal

---

### FLOW 3: Memory Storage & Retrieval
```
USER ACTION → HOOK TRIGGER → MEMORY STORE
                                   ↓
                        HNSW INDEX (150x faster search)
                                   ↓
                        RETRIEVAL (before reasoning)
                                   ↓
                        AI DECISION (pattern-informed)
```

**Namespaces:**
- `shared-knowledge:patterns:*` → Code/workflow patterns
- `shared-knowledge:bmad:*` → BMAD best practices
- `life-os:ideas:*` → Ideas data
- `life-os:projects:*` → Projects data
- `life-os:goals:*` → User goals
- `life-os:reviews:*` → PDCA reviews

---

## 1.6 Quality Perspectives (Взгляд на качество)

### QUALITY 1: Output Standards
**Для каждого типа output:**

**Ideas (evaluated):**
- ✅ Score обоснован (не просто число, а reasoning)
- ✅ Roles relevant to problem domain
- ✅ Decision clear (GO/NO-GO/WAIT + why)
- ✅ Сохранено в memory (retrieval possible)

**Plans (planned ideas):**
- ✅ Tasks SMART (Specific, Measurable, Achievable, Relevant, Time-bound)
- ✅ Resources реалистичны (не underestimate, не overestimate)
- ✅ Risks идентифицированы (+ mitigation strategies)
- ✅ Timeline с contingency (buffer 20%)

**Projects (active):**
- ✅ Progress tracked (не просто "в работе", а X%)
- ✅ Blockers documented (если есть)
- ✅ Calendar synced (time-blocks exist)
- ✅ Linked to origin idea (traceability)

**Retrospectives (completed/killed):**
- ✅ Learnings captured (что сработало, что нет)
- ✅ Metrics documented (duration, effort, outcome)
- ✅ Recommendations (что делать в следующий раз)

---

### QUALITY 2: Validation Gates
**После каждого key step:**

**L1-S3 (Evaluate):**
- Gate: Можно ли принять GO/NO-GO решение на основе score?
- Если нет → escalate to Standard/Deep

**L2-S1 (Plan):**
- Gate: План достаточно детальный для исполнения?
- Если нет → добавить tasks/risks

**L2-S3 (Activate):**
- Gate: Есть ли capacity? (< 5 active projects)
- Если нет → prompt: "Finish existing project first?"

**L3-S1 (Retrospective):**
- Gate: Все learnings captured?
- Если нет → prompt: "What did you learn?"

---

## 1.7 Integration Perspectives (Взгляд на интеграции)

### INTEGRATION 1: Ideas ↔ Projects
**Связь:**
- Идея (файл) → Проект (папка)
- `origin-idea: idea-007` в project.md
- `became_project: project-002` в archived idea
- Memory: `life-os:projects:project-002` → `{origin: idea-007}`

**Traceability:**
- Из проекта можно вернуться к идее (см. initial reasoning)
- Из идеи видно, стала ли она проектом (и каким)
- Portfolio dashboard показывает connections

---

### INTEGRATION 2: Goals ↔ Ideas ↔ Projects
**Связь:**
- Goal (year/quarter) → Idea (Strategic Alignment score)
- Idea → Project (activation)
- Project → Goal (progress tracking)

**Alignment check:**
- При оценке идеи: "Как эта идея помогает достичь goals?"
- При активации проекта: "Какой goal этот проект продвигает?"
- При review: "Прогресс к goal X: 40% (on track)"

---

### INTEGRATION 3: Memory ↔ Workflow
**Связь:**
- Workflow step → Hook trigger → Memory store
- Memory retrieval → AI reasoning → Better decisions
- Pattern matching → Reuse solutions (-32% tokens)

**Примеры:**
- "Нашёл похожую идею из прошлого → её результат был X"
- "Прошлая идея из этой сферы заняла Y недель (estimate)"
- "У тебя 87% completion rate на Standard Track"

---

## 1.8 North Star Alignment Verification (Проверка соответствия видению)

**Проверочные вопросы для каждого use case:**

| North Star Element | Verification Question | Expected Answer |
|--------------------|----------------------|-----------------|
| "50+ specialized experts" | Подбираются ли роли динамически под задачу? | ✅ YES (AI suggests based on keywords + domain) |
| "knowing long-term goals" | Учитываются ли goals.yaml при оценке идей? | ✅ YES (after Goals Discovery implementation) |
| "tracking resources" | Видит ли user capacity, budget, time? | ✅ YES (portfolio dashboard: 3/5 projects) |
| "monitoring capacity" | Предупреждает ли system о перегрузке? | ✅ YES (prompt: "5/5 projects, finish one first") |
| "building calendars" | Генерируются ли time-blocks из goals? | ✅ YES (after PDCA integration) |
| "proactively suggesting" | Предлагает ли system integrations/optimizations? | ✅ YES (detects synergies, suggests track escalation) |

**Целевой статус соответствия North Star:**
- 🎯 **6/6 элементов полностью реализованы** (после v3.0.0 implementation)

---

## 1.9 Configuration Specifications (Спецификации конфигурации)

### 1.9.1 Sphere & Domain Registry (Классификация сфер)

**3 Classification Systems (используются на разных этапах):**

| Classification | Purpose | Values | When Used |
|----------------|---------|--------|-----------|
| **Life Spheres** | Idea capture | Health, Wealth, Relationships, Growth, Contribution | Step 01 (Collect Ideas) |
| **Goal Domains** | Goals organization | Finance, Business, Health, Personal Dev | Step 00 (Goals Discovery) |
| **Project Domains** | Scoring & planning | personal, hobby, freelance, small-business, software, saas, ai-ml, franchise, enterprise | Step 05 (Scoring) |

**Mapping (Life Spheres ↔ Goal Domains):**
- **Wealth** → Finance + Business
- **Health** → Health
- **Growth** → Personal Dev
- **Relationships** → Personal Dev
- **Contribution** → Personal Dev + Business

**Why Different Classifications:**
- **Life Spheres (5):** Natural way humans think about life areas during brainstorming
- **Goal Domains (4):** Standard framework for structured annual/quarterly planning
- **Project Domains (9):** Granular categories for scoring weights and resource estimation

**Cross-Reference:**
- 📖 Complete domain definitions: `data/goals-examples/goals-4-domains-reference.md`
- 📖 D/F/V/C goal domain weights: `data/dfvc-criteria-rubric.part-01.md`

---

### 1.9.2 Scoring Criteria (5+N Criteria System)

**System Overview:** Life OS uses **"5+N criteria"** not a fixed 6 or 7.

**Base Criteria (4–6 depending on context):**

**Always included (4):** Impact, Confidence, Effort, Risk
**Conditionally included (+1–2):** Strategic Alignment (only if goals.yaml exists), SaaS Autonomy (only if domain='saas' or 'software')

| # | Criterion | Weight | Type | When Applied |
|---|-----------|--------|------|--------------|
| 1 | **Impact** | 0.25 | Positive | Always |
| 2 | **Confidence** | 0.15 | Positive | Always |
| 3 | **Effort** | -0.20 | Negative | Always |
| 4 | **Strategic Alignment** | 0.25 | Positive | ONLY if goals.yaml exists |
| 5 | **Risk** | -0.15 | Negative | Always |
| 6 | **SaaS Autonomy** | 0.15 | Positive | ONLY if domain='saas' or 'software' |

**+N Domain-Specific Criteria (Auto-Added by Goal Domain):**

| Goal Domain | Additional Criteria | Weights |
|-------------|-------------------|---------|
| **Business** | Traffic Feasibility (CAC Proxy), Unit Economics (ARPA × Gross Margin), Time to First Revenue (TFR) | 0.10, 0.12, 0.08 |
| **Finance** | Expected Value, Option Value | 0.15, 0.10 |
| **Health** | Readiness (HBM), Sustainability | 0.10 each |
| **Personal Dev** | Skill Impact, Time Commitment | 0.10 each |

### 1.9.2.1 Business-Specific Criteria Details

#### Traffic Feasibility (CAC Proxy) — Реалистичность трафика (CAC-прокси)
**Definition:** Can we reliably acquire leads/users at a cost that makes the business viable?
**RU:** Можно ли стабильно добывать лиды/пользователей по цене, которая оставляет прибыль?

**Scoring Anchors (1–5):**
- **1:** Канал неясен. CAC неизвестен. Доступ к ЦА не подтверждён.
- **3:** Есть 1–2 канала + приблизительный CAC proxy (стоимость лида/контакта) + план микро-теста.
- **5:** Канал проверен (хотя бы микро-тестом). Понятна экономика трафика. Есть путь к масштабированию.

#### Unit Economics (ARPA × Gross Margin) — Юнит-экономика (ARPA × валовая маржа)
**Definition:** Does the model generate profit after variable costs (including support and LLM/API costs)?
**RU:** Остаются ли деньги после переменных затрат (включая поддержку и LLM/API-косты)?

**Scoring Anchors (1–5):**
- **1:** Маржа отрицательная/сомнительная. Переменные затраты (support/LLM) убивают модель.
- **3:** На бумаге сходится. Маржа положительная, но есть риски по cost-to-serve.
- **5:** Высокая маржа при реальном usage. Cost-to-serve контролируем. Есть запас на рост CAC.

#### Time to First Revenue (TFR) — Время до первых денег (TFR)
**Definition:** How quickly can we reach the first paid transaction/pilot?
**RU:** Сколько времени до первой оплаты/пилота?

**Scoring Anchors (1–5):**
- **1:** > 90 дней до первых денег
- **3:** 30–90 дней
- **5:** ≤ 30 дней до первой оплаты/пилота

**SaaS Autonomy Sub-Criteria (Criterion #6):**

| Sub-Criterion | Weight | What It Measures | Scale |
|--------------|--------|------------------|-------|
| Self-Signup | 0.25 | Can users sign up without sales calls? | 1-5 |
| Self-Billing | 0.30 | Automated payment and provisioning? | 1-5 |
| Self-Service Support | 0.30 | Can users solve problems without agents? | 1-5 |
| Autonomous Operation | 0.15 | Can product run without manual intervention? | 1-5 |

**Formula:**
```
SaaS_Autonomy = (Self_Signup × 0.25) + (Self_Billing × 0.30) +
                (Self_Service × 0.30) + (Autonomous_Op × 0.15)

Integration: Applied as 6th base criterion OR as Viability multiplier
Viability_adjusted = Viability × (SaaS_Autonomy / 5.0)
```

**Weight Normalization Rules (Critical for Score Comparability):**

Due to **negative weights** (Effort, Risk), normalization follows these rules:

```
Method: Separate normalization of positive and negative weights

Step 1: Sum positive weights
W_positive = Impact + Confidence + Strategic_Alignment + SaaS_Autonomy + [Domain-specific]

Step 2: Sum absolute values of negative weights
W_negative = |Effort| + |Risk|

Step 3: Normalize each group to target allocation
- Positive weights normalized to sum = 0.70 (70% of total score)
- Negative weights normalized to sum = 0.30 (30% penalty capacity)

Step 4: Compute raw score
Raw_Score = (Σ normalized_positive × values) - (Σ normalized_negative × values)

Step 5: Clamp to UI range
Score = max(0.0, min(5.0, Raw_Score))

Result: Final Score range = 0.0 to 5.0 (clamped)
```

**Example:**
- Assumptions: goals.yaml NOT found → skip Strategic Alignment; domain != 'saas'/'software' → skip SaaS Autonomy; no domain-specific criteria → positives = Impact+Confidence, negatives = Effort+Risk
- Impact: 4/5, Confidence: 3/5, Effort: 4/5, Risk: 3/5
- Normalized weights (70/30): Impact = 0.35, Confidence = 0.35, Effort = 0.15, Risk = 0.15
- Positive contribution: (4 × 0.35) + (3 × 0.35) = 2.45
- Negative penalty: (4 × 0.15) + (3 × 0.15) = 1.05
- Raw Score: 2.45 - 1.05 = 1.40
- **Final Score (clamped 0.0–5.0): 1.40/5.0** (LOW priority)

**Why This Method:**
- ✅ Caps penalty influence to 30% of weight mass (prevents penalties from dominating the score)
- ✅ Ensures final score is comparable in UI by clamping to 0.0–5.0
- ✅ Maintains comparability across different domain-specific criteria sets
- ✅ Explicit: positive/negative balance is 70/30 by design

**Conditional Logic:**
- If `goals.yaml` NOT found → Use 4 base criteria (skip Strategic Alignment)
- If `domain != 'saas'/'software'` → Use 5 base criteria (skip SaaS Autonomy)
- Domain-specific criteria are ALWAYS added automatically

**Cross-Reference:**
- 📖 Full criteria definitions: `data/mcda-criteria-detailed.md`
- 📖 Strategic Alignment formula: `steps-c/step-05-scoring.md` (lines 89-100)

---

### 1.9.3 D/F/V/C Rubrics by Goal Domain

**D/F/V/C Framework:** Desirability, Feasibility, Viability, Competition (used in Deep Track only)

**Goal-Domain-Specific Weight Adjustments (defaults):**

| Goal Domain | Market Size | Need Intensity | WTP | Competitive Advantage | Rationale |
|-------------|-------------|----------------|-----|-----------------------|-----------|
| **Business** | 0.25 | 0.35 | 0.30 | 0.10 | Market size and monetization critical |
| **Finance** | 0.15 | 0.30 | 0.40 | 0.15 | ROI and pricing power key |
| **Health** | 0.10 | 0.60 | 0.20 | 0.10 | Impact on well-being dominates |
| **Personal Dev** | 0.05 | 0.50 | 0.10 | 0.35 | Learning + fulfillment dominate (market size irrelevant) |

**Overrides (optional):**
- Project Domain can override these defaults (e.g., creative/hobby/product) via `data/dfvc-criteria-rubric.part-*.md`

**Track Usage:**
- **Deep Track:** Full D/F/V/C rubrics with sub-criteria scoring (1-10 scales)
- **Standard Track:** Simplified scoring (aggregate D/F/V/C scores)
- **Quick Track:** Does not use D/F/V/C (uses base criteria only)

**Cross-Reference:**
- 📖 Complete D/F/V/C rubrics: `data/dfvc-criteria-rubric.part-01.md` through `part-07.md`
- 📖 Sub-criteria definitions and scoring scales in above files

---

### 1.9.4 Developer Profile & Speed Multipliers

**Speed Multiplier Adjustment Formula:**
```
Final_Multiplier = Base_Multiplier + Bonuses - Penalties

Where:
- Base_Multiplier = 10x (LLM solo) or 20x (LLM team) or 5x (no-code)
- Bonuses: +0.2 to +2.0x (existing code reuse), +0.5 to +2.0x (infrastructure ready)
- Penalties: -0.2 to -1.0x (skill gaps), -0.2 to -0.5x (budget constraints),
            -0.5 to -1.0x (time pressure)
```

**Skill Gap Penalties:**
- **Major skill gaps** (new language, framework, domain): **-1.0x** multiplier
- **Moderate gaps** (learning required, 2-3 months): **-0.5x** multiplier
- **Minor gaps** (documentation available, 2-4 weeks): **-0.2x** multiplier

**Example Impact:**
- **Scenario A:** Solo dev, LLM-assisted, no skill gaps → 15x speedup
  - Timeline: 12 weeks ÷ 15 = **0.8 weeks** (4.8 days)
- **Scenario B:** Same setup but major skill gap → 15 - 1.0 = 14x speedup
  - Timeline: 12 weeks ÷ 14 = **0.86 weeks** (6.1 days)
- **Difference:** +1.3 days due to skill gap penalty

**When to Apply:**
- Step 00.6 (Resource Assessment): Evaluate skill gaps
- Step 00.7 (Optimization Intelligence): Calculate final multiplier
- Step 08 (Deep Plan): Adjust timeline estimates based on multiplier

**Cross-Reference:**
- 📖 Complete resource assessment: `steps-c/step-00.6-resource-assessment.md`
- 📖 Speed multiplier examples: `steps-c/step-00.7-optimization-intelligence.md`

---

## 1.10 SaaS Autonomy Gate (Оценка автономности SaaS)

### 1.10.1 The 4 Autonomy Pillars

**Purpose:** Explicit criteria for evaluating SaaS autonomous operation capability.

**Critical Note:** This is a **6th base criterion** applied ONLY when `domain = 'saas'` or `domain = 'software'`.

**4 Pillars (weights sum to 1.0):**

| Pillar | Weight | What It Measures | Scoring Scale (1-5) |
|--------|--------|------------------|---------------------|
| **Self-Signup** | 0.25 | Can users sign up without sales calls? | 1 (enterprise sales) → 5 (1-click signup) |
| **Self-Billing** | 0.30 | Automated payment and provisioning? | 1 (manual invoicing) → 5 (usage-based auto-billing) |
| **Self-Service Support** | 0.30 | Can users solve problems without human agents? | 1 (dedicated CSM) → 5 (<1% support contact rate) |
| **Autonomous Operation** | 0.15 | Can product run without manual team intervention? | 1 (heavy manual work) → 5 (fully automated) |

**Scoring Anchors for Each Pillar:**

**Self-Signup (0.25 weight):**
- **1:** Enterprise sales process (demos, RFPs, contracts)
- **2:** Sales-assisted signup (demo → trial → manual provisioning)
- **3:** Self-service trial with manual approval
- **4:** Instant trial, credit card for upgrade
- **5:** 1-click signup, instant access, no approval

**Self-Billing (0.30 weight):**
- **1:** Manual invoicing (monthly POs, wire transfers)
- **2:** Automated invoicing (PDF invoices, manual payment)
- **3:** Recurring credit card billing (monthly/annual)
- **4:** Usage-based billing (per user/per event, automated)
- **5:** Fully automated (usage metering + billing + dunning + recovery)

**Self-Service Support (0.30 weight):**
- **1:** Dedicated CSM or account manager required
- **2:** Email/ticket support with 24-48h response
- **3:** Knowledge base + community forum (50% self-service rate)
- **4:** In-app help + chatbot + docs (80% self-service rate)
- **5:** AI-powered support + proactive issue detection (<1% contact rate)

**Autonomous Operation (0.15 weight):**
- **1:** Heavy manual ops (daily admin work, manual provisioning)
- **2:** Some automation (weekly admin work, semi-automated provisioning)
- **3:** Mostly automated (monthly admin, alerts for issues)
- **4:** Highly automated (quarterly check-ins, self-healing systems)
- **5:** Fully autonomous (zero admin, 99.9% uptime, auto-scaling)

---

### 1.10.2 Autonomy Score Formula

```
Autonomy_Score = (Self_Signup × 0.25) + (Self_Billing × 0.30) +
                 (Self_Service_Support × 0.30) + (Autonomous_Operation × 0.15)

Result: 1.0-5.0 scale (like other criteria)
```

**Thresholds & Interpretation:**
- **4.5-5.0:** Highly autonomous (ideal for solo founder, passive income potential)
- **3.5-4.4:** Moderately autonomous (small team of 2-5 required)
- **2.5-3.4:** Limited autonomy (team of 5-10 required)
- **1.0-2.4:** Low autonomy (essentially managed service, 10+ team)

---

### 1.10.3 Integration with Scoring

**When Applied:** Step 05 (Scoring), ONLY if `domain = 'saas'` or `domain = 'software'`

**Method 1: As 6th Base Criterion (0.15 weight)**
```
Total_Score = (Impact × 0.25) + (Confidence × 0.15) + (Effort × -0.20) +
              (Strategic_Alignment × 0.25) + (Risk × -0.15) +
              (SaaS_Autonomy × 0.15)
```

**Method 2: As Viability Modifier (affects unit economics)**
```
Viability_adjusted = Viability × (Autonomy_Score / 5.0)

Rationale: Low autonomy = high support costs = worse unit economics
Example: Viability 4.0/5, Autonomy 2.0/5 → Viability_adjusted = 4.0 × (2.0/5.0) = 1.6/5
```

**System Recommendation:**
- If `Autonomy_Score < 3.0` → Flag "⚠️ High Support Load Risk"
- If `Autonomy_Score < 2.0` → Recommend "Consider B2B enterprise model instead of self-service"

---

### 1.10.4 Real-World Example

**Project:** SaaS tool for project management

**Scoring:**
- Self-Signup: 5/5 (instant signup, no approval)
- Self-Billing: 4/5 (recurring billing, basic dunning)
- Self-Service: 3/5 (knowledge base + email support, 60% self-service rate)
- Autonomous Op: 4/5 (mostly automated, weekly monitoring)

**Calculation:**
```
Autonomy_Score = (5 × 0.25) + (4 × 0.30) + (3 × 0.30) + (4 × 0.15)
               = 1.25 + 1.20 + 0.90 + 0.60
               = 3.95/5 (Moderately Autonomous)
```

**Interpretation:** Small team of 3-5 needed, not fully passive but manageable for small business.

---

### 1.10.5 Workflow Integration

**Step 01 (Collect Ideas):** Detect if domain = 'saas' or 'software'
**Step 05 (Scoring):** Apply SaaS Autonomy Gate as 6th criterion
**Step 08 (Deep Plan):** Include support/ops planning based on Autonomy Score

**Risk Flags:**
- `Autonomy < 3.0` → Warn about high operational overhead
- `Autonomy < 2.0` → Suggest pivoting to enterprise/managed service model

---

## 1.11 Implementation Profile (Профиль реализации)

### 1.11.1 Core Architecture: Markdown-First Principle

**Philosophy:** All data in `.md` files (not database) until scale requires external storage.

**Storage Structure:**
```
Markdown-First Data Layer:
├── All ideas in .md files (YAML frontmatter for metadata)
├── All projects in .md + folder structure
├── Git for version control
├── Claude Flow memory for cross-session patterns (HNSW indexing)
└── Optional: Supabase sync when 100+ items or external UI needed
```

**Why Markdown-First:**
- ✅ Human-readable and git-friendly
- ✅ No vendor lock-in (portable to any tool)
- ✅ Zero infrastructure overhead (files on disk)
- ✅ AI-native (Claude/LLMs can directly read/edit)
- ✅ Obsidian/Logseq compatible (if user wants visual UI)

**When to Add Database:**
- 100+ ideas/projects (file system becomes slow)
- External web UI needed (team collaboration)
- Real-time sync across devices
- Advanced search/filtering (beyond grep)

---

### 1.11.2 Recommended Tech Stack

**3-Phase UI Evolution:**

**Phase 1: MVP (CLI-First) - Week 1**

| Layer | Technology | Why |
|-------|-----------|-----|
| Interface | Claude Code (this system) | Zero setup, AI-native, fast iteration |
| Data | Markdown files + Git | Version control, backup, portable |
| Memory | Claude Flow (SQLite + AgentDB) | HNSW indexing (150x faster search) |
| Visualization | Optional: Obsidian/Logseq | View ideas as graph/kanban |

**Cost:** $0-20/month (Claude API only)

---

**Phase 2: Production Web UI - Weeks 2-4**

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| Frontend | Next.js 14 (App Router) | v0.dev compatible, full-stack, edge runtime |
| UI Components | shadcn/ui + Tailwind CSS | Accessible (WCAG 2.1 AA), customizable, copy-paste |
| Backend | Supabase (PostgreSQL + Auth + Storage) | Instant APIs, built-in auth, zero-config vector search |
| Deployment | Vercel (Edge Functions) | Zero-config deploy from Git, global CDN |
| AI Integration | Claude API + Vercel AI SDK | Streaming responses, function calling |
| Memory | Claude Flow + Supabase pgvector | Hybrid: local HNSW + cloud PostgreSQL |

**Cost:** $50-150/month (Vercel Pro + Supabase Pro + Claude API)

---

**Phase 3: Mobile (Optional) - Weeks 5-8**

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| Framework | React Native + Expo | Code reuse with web, OTA updates |
| Backend | Same (Supabase) | Shared APIs, no duplication |
| Offline-First | WatermelonDB | SQLite sync, works offline |

**Cost:** +$0 (same backend), app stores $100/year

---

### 1.11.2.1 Deployment Variants (Global / RU / Offline)

**Variant Selection Criteria:**
- **Global Stack:** Default for international use, fastest deployment, no geo-restrictions
- **RU Stack:** Required if data must stay in Russia (compliance, latency, sanctions)
- **Offline-Only:** For privacy-first users, air-gapped environments, or no cloud budget

---

**Variant 1: Global Stack (Recommended)**

| Layer | Technology | Location |
|-------|-----------|----------|
| Frontend Hosting | Vercel Edge Network | Global CDN (100+ locations) |
| Database | Supabase PostgreSQL | AWS us-east-1 (primary), eu-west-1 (replica) |
| Object Storage | Supabase Storage (S3) | AWS us-east-1 |
| Auth | Supabase Auth | Global |
| AI API | Claude API (Anthropic) | US/EU endpoints |

**Pros:** ✅ Zero-config, fastest setup, auto-scaling, global CDN
**Cons:** ❌ Data in US/EU only, subject to US export controls
**Cost:** $50-150/month (Phase 2)

---

**Variant 2: RU Stack (Data Localization)**

| Layer | Technology | Location |
|-------|-----------|----------|
| Frontend Hosting | VK Cloud (VK Cloud Solutions) OR Selectel | Russia (Moscow/SPb datacenters) |
| Database | PostgreSQL (self-hosted or managed) | VK Cloud / Selectel / Yandex Cloud |
| Object Storage | S3-compatible (VK Cloud Object Storage) | Russia |
| Auth | Custom (Keycloak or OAuth) | Self-hosted in Russia |
| AI API | YandexGPT OR GigaChat (Sber) OR self-hosted LLM | Russia |

**Pros:** ✅ Full data sovereignty, GDPR-like compliance (152-ФЗ), no sanctions risk
**Cons:** ❌ Manual setup, no Vercel/Supabase convenience, AI quality trade-offs
**Cost:** $100-300/month (Phase 2, includes VPS + managed DB + storage)

**Key Differences from Global:**
- **AI Integration:** Replace Claude API with YandexGPT (similar API structure)
- **Deployment:** Manual server setup or VK Cloud PaaS
- **Database:** Use managed PostgreSQL from VK Cloud/Selectel/Yandex
- **CDN:** Use Selectel CDN or Yandex Cloud CDN for static assets
- **Auth:** Self-host Keycloak or use VK ID OAuth

**Migration Path:**
- Phase 1 (CLI) works identically (Markdown-first)
- Phase 2: Replace Vercel → VK Cloud, Supabase → Postgres+custom auth
- Phase 3: Use VK Mini Apps SDK instead of React Native for mobile

---

**Variant 3: Offline-Only (Maximum Privacy)**

| Layer | Technology | Location |
|-------|-----------|----------|
| Frontend | None (CLI only) OR local Electron app | User's machine |
| Database | SQLite (via Claude Flow AgentDB) | Local filesystem |
| Object Storage | Local filesystem (ideas-bank/ folder) | User's machine |
| Auth | None (single-user) | N/A |
| AI API | Local LLM (Ollama + Llama 3) OR API on-demand | User's machine OR pay-per-use API |

**Pros:** ✅ Zero monthly cost, complete privacy, works offline, no vendor lock-in
**Cons:** ❌ No collaboration, manual backups, lower AI quality with local LLMs
**Cost:** $0-20/month (only if using Claude API on-demand)

**Key Differences:**
- **No Web UI:** Use CLI only (Claude Code interface)
- **No External Sync:** All data in `.md` files + Git for backups
- **AI Optional:** Can work without AI (manual scoring/planning)
- **Backups:** Git push to private repo (GitHub, GitLab, Gitea self-hosted)

**Best For:**
- Solo users who don't need collaboration
- Privacy-focused individuals (no cloud at all)
- Budget-constrained users ($0 infrastructure)
- Developers comfortable with CLI workflows

---

**Variant Comparison Matrix:**

| Feature | Global | RU | Offline |
|---------|--------|----|----|
| **Setup Time** | 1 hour | 4-8 hours | 15 minutes |
| **Monthly Cost** | $50-150 | $100-300 | $0-20 |
| **Data Location** | US/EU | Russia | Local only |
| **AI Quality** | Claude (best) | YandexGPT (good) | Llama 3 (acceptable) |
| **Collaboration** | ✅ Yes | ✅ Yes | ❌ No |
| **Offline Work** | ❌ No | ❌ No | ✅ Yes |
| **Maintenance** | ✅ Minimal | ⚠️ Moderate | ✅ Minimal |
| **Vendor Lock-in** | ⚠️ Vercel/Supabase | ⚠️ VK Cloud | ✅ None |

**Recommendation:**
- **Start with Global** if no compliance requirements (fastest to production)
- **Switch to RU** if data must stay in Russia or sanctions become issue
- **Use Offline** for MVP/testing or if $0 budget is hard constraint

---

### 1.11.3 Component Library (shadcn/ui Mapping)

**Life OS UI Components:**

| Feature | Component | Use Case |
|---------|-----------|----------|
| Idea collection form | `Form` + `Input` + `Textarea` | Step 01 (Collect Ideas) |
| Track selection | `Tabs` | Quick/Standard/Deep selection |
| Scoring sliders | `Slider` + `Label` | Step 05 (Scoring) |
| Dashboard widgets | `Card` + `CardHeader` + `CardContent` | Portfolio overview |
| Ideas/projects table | `Table` + `DataTable` | Filterable, sortable lists |
| Edit dialogs | `Dialog` + `DialogContent` | Modal for editing |
| Status badges | `Badge` | INBOX/EVALUATED/PLANNED/ACTIVE |
| Progress bars | `Progress` | Project completion % |
| Calendar integration | `Calendar` + `DatePicker` | Time-block scheduling |
| Goal tree view | `Accordion` + `TreeView` | Nested goals display |

**Accessibility:**
- WCAG 2.1 AA compliance (all shadcn/ui components)
- Keyboard navigation (Tab, Enter, Esc)
- Screen reader support (ARIA labels)
- High contrast mode

---

### 1.11.4 Architecture Diagram

```
┌─────────────────────────────────────────────────┐
│             User (Browser/CLI)                  │
└─────────────────────┬───────────────────────────┘
                      │
          ┌───────────▼────────────┐
          │   Next.js Frontend     │
          │   (Vercel Edge)        │
          └───────────┬────────────┘
                      │
        ┌─────────────┼─────────────┐
        │             │             │
┌───────▼────────┐    │    ┌────────▼────────┐
│  Supabase      │    │    │  Claude API     │
│  (PostgreSQL   │    │    │  (Anthropic)    │
│   + Auth       │    │    │                 │
│   + Storage)   │    │    └─────────────────┘
└────────────────┘    │
                      │
              ┌───────▼──────────┐
              │  Claude Flow     │
              │  Memory          │
              │  (HNSW indexing) │
              └──────────────────┘
```

---

### 1.11.5 Deployment Instructions

**Development Setup:**
```bash
# 1. Clone repo
git clone <your-repo>
cd life-os

# 2. Install dependencies
npm install

# 3. Start Claude Flow daemon
npx claude-flow@v3alpha daemon start

# 4. Run dev server
npm run dev

# Open http://localhost:3000
```

**Production Deployment (Vercel):**
```bash
# 1. Connect repo to Vercel
vercel link

# 2. Set environment variables (Vercel dashboard)
ANTHROPIC_API_KEY=sk-ant-...
NEXT_PUBLIC_SUPABASE_URL=https://...
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...

# 3. Deploy
vercel --prod

# Auto-deploy on git push to main
```

**Environment Variables:**
- `ANTHROPIC_API_KEY`: Claude API key (required)
- `NEXT_PUBLIC_SUPABASE_URL`: Supabase project URL (required for web UI)
- `NEXT_PUBLIC_SUPABASE_ANON_KEY`: Supabase public key (required)
- `CLAUDE_FLOW_MEMORY_PATH`: Custom memory path (optional)

---

### 1.11.6 Performance Targets

**Lighthouse Scores (Target):**
- Performance: >90
- Accessibility: 100 (WCAG 2.1 AA)
- Best Practices: >90
- SEO: >90

**Core Web Vitals:**
- LCP (Largest Contentful Paint): <2.5s
- FID (First Input Delay): <100ms
- CLS (Cumulative Layout Shift): <0.1

**API Response Times:**
- Ideas list: <200ms (client-side filtering)
- Scoring calculation: <500ms (MCDA computation)
- Claude API (streaming): First token <1s, full response <10s

---

### 1.11.7 Cost Estimates (Monthly)

**Phase 1 (CLI-First):**
- Claude API: $10-20/month (based on usage)
- Git hosting: Free (GitHub/GitLab)
- **Total:** $10-20/month

**Phase 2 (Web UI, 100-1K users):**
- Vercel Pro: $20/month
- Supabase Pro: $25/month
- Claude API: $30-50/month (increased usage)
- Domain: $12/year (~$1/month)
- **Total:** $76-96/month

**Phase 3 (Scale, 1K-10K users):**
- Vercel Team: $100/month (multiple team members)
- Supabase Team: $150/month (higher database limits)
- Claude API: $200-500/month (high volume)
- CDN (Cloudflare): $20/month
- **Total:** $470-770/month

**Cost Comparison vs. Traditional Stack:**
- Traditional (AWS EC2 + RDS + Engineers): $2,000-5,000/month
- Life OS Stack: $76-770/month (3x-65x cheaper)

**Note:** Stack is **recommended, not mandatory**. Adapt to team preferences. Markdown-first architecture works with any tool (Obsidian, VS Code, CLI).

---

## 1.12 Task Layer Specification (Контракт системы задач)

### 1.12.1 Task Data Model (Source of Truth)

**Primary Storage:** Markdown files in project folders (Phase 1-2) OR Supabase tasks table (Phase 3)

**Task Schema:**
```yaml
task_id: string          # Unique ID (e.g., "task-001-setup-db")
project_id: string       # Parent project (e.g., "project-002")
goal_id: string          # Linked goal from goals.yaml (e.g., "2026-business-q1-1")
title: string            # Task title (max 100 chars)
description: string      # Detailed description (markdown)
status: enum             # [todo, in_progress, blocked, done, cancelled]
priority: enum           # [critical, high, medium, low]
due_date: date|null      # Optional. ISO 8601 (e.g., "2026-02-15"). If null → scheduled via week plan or calendar
estimate_hours: number   # Effort estimate (0.5 - 40 hours)
actual_hours: number     # Actual time spent (tracked)
energy_level: enum       # [high, medium, low] - required mental energy
dependencies: string[]   # Other task_ids that must complete first
tags: string[]           # Labels (e.g., ["coding", "frontend", "urgent"])
created_at: timestamp
updated_at: timestamp
completed_at: timestamp  # Set when status = done
```

**Mandatory Fields:**
- `task_id`, `project_id`, `goal_id`, `title`, `status`, `estimate_hours`, `energy_level`

**Optional Fields:**
- `due_date`, `description`, `actual_hours`, `dependencies`, `tags`, `completed_at`

---

### 1.12.2 Storage Options & Sync Rules

**Phase 1 (Markdown-First):**
- **Location:** `projects/project-XXX/tasks/task-YYY.md`
- **Format:** YAML frontmatter + markdown body
- **Sync:** None (local only)
- **Source of Truth:** Markdown files

**Phase 2 (Hybrid with Todoist):**
- **Primary:** Markdown files (authoritative)
- **Mirror:** Todoist (for mobile/calendar integration)
- **Sync Direction:** **One-way (Markdown → Todoist)**
  - Create/update tasks in Todoist via API
  - Completions marked in Todoist → webhook updates Markdown
  - **Conflict Resolution:** Markdown always wins
- **Sync Frequency:** On task create/update (immediate)

**Phase 3 (Supabase Database):**
- **Primary:** Supabase `tasks` table (authoritative)
- **Mirror:** Markdown files (for git history, optional)
- **Sync Direction:** **Two-way (Supabase ↔ Todoist)**
  - Supabase triggers update Todoist
  - Todoist completions update Supabase
- **Conflict Resolution:** Last-write-wins with timestamp check

---

### 1.12.3 Task ↔ Project ↔ Goal Linkage

**Hierarchical Structure:**
```
Goal (goals.yaml)
  ↓ decomposed into
Project (project.md)
  ↓ broken down into
Tasks (task-XXX.md)
  ↓ executed as
Daily TODO (generated)
```

**Traceability Rules:**
1. Every task MUST have `project_id` (orphan tasks not allowed)
2. Every project SHOULD link to `goal_id` (unless one-off)
3. Goal progress (primary) = done_tasks / (done_tasks + open_tasks) for all tasks linked to goal
   Goal progress (secondary) = Σ(task.actual_hours) / Σ(task.estimate_hours) for forecasting/capacity

**Validation Gates:**
- Task creation: Project must exist and be ACTIVE
- Task completion: Updates project progress percentage
- Project completion: All tasks must be done/cancelled (no open tasks)

---

### 1.12.4 Daily TODO Generation Rules

**Source Data:**
- Week plan (from `projects/project-XXX/week-plan.md`)
- Task due dates (from `task.due_date`)
- Energy levels (from `task.energy_level`)
- User capacity (from Step 00.6 resource assessment)

**Generation Algorithm:**
```
For target_date in [today]:
0. Parse week plan to get week_plan_tasks (task_ids scheduled for the current week)

1. Fetch all tasks where:
   - status = todo OR in_progress
   - project.status = ACTIVE
   - ((due_date IS NOT NULL AND due_date <= target_date) OR task_id in week_plan_tasks)

2. Sort by:
   - priority (critical → low)
   - due_date (earliest first; nulls last)
   - energy_level (match time of day preference)

3. Filter by capacity:
   - Sum estimate_hours <= daily_capacity (default: 4-6 hours)
   - Balance high/medium/low energy tasks

4. Output format:
   - Morning (high energy): 2-3 high-energy tasks
   - Afternoon (medium): 3-4 medium-energy tasks
   - Evening (low): 1-2 low-energy tasks (optional)
```

**Output Location:** `_output/daily-todos/YYYY-MM-DD.md`

---

### 1.12.5 Task Completion Definition

**A task is considered "done" when:**
1. `status = done` (set explicitly by user or system)
2. `completed_at` timestamp is set
3. `actual_hours` recorded (can be 0 if instant)
4. Linked project progress updated

**Automatic Triggers on Task Completion:**
- Update `project.progress` percentage
- Check if project milestone reached (notify user)
- Generate next task suggestions (if applicable)
- Update goal progress tracking
- Log in memory: `life-os:tasks:{task_id}:completed`

**Blocked Task Rules:**
- Task with `status = blocked` cannot be worked on
- Must specify `dependencies` field (which tasks block this)
- Auto-unblock when all dependencies are done
- Show in "Blocked Queue" dashboard view

---

### 1.12.6 Integration with Calendar (Time Blocks)

**Time Block Creation:**
- Triggered by: Daily TODO generation OR manual task scheduling
- Default duration: `task.estimate_hours` converted to calendar blocks
- Placement: Respects `energy_level` and user's work hours preference

**Calendar Event Fields:**
```yaml
event_id: string         # Unique calendar event ID
task_id: string          # Linked task
title: string            # Task title
start: datetime          # ISO 8601 with timezone
end: datetime            # start + estimate_hours
calendar: string         # "Work" or "Personal"
color: string            # Priority-based (critical=red, high=orange, etc.)
reminders: number[]      # Minutes before [15, 60] (15min, 1hour)
```

**Sync with External Calendar:**
- **Phase 1:** No external sync (Markdown-only)
- **Phase 2:** One-way (Life OS → Google Calendar via API)
- **Phase 3:** Two-way (calendar reschedule updates task.due_date)

**Conflict Resolution:**
- If task completed before calendar event → delete event
- If calendar event deleted → mark task as "unscheduled" (not cancelled)

---

## 1.13 UI Minimum Screens v1 (Обязательные экраны)

### 1.13.1 Portfolio Dashboard (Главная страница)

**Purpose:** Overview of all active projects, capacity, and priorities.

**Data Requirements:**
```sql
SELECT
  projects.id,
  projects.title,
  projects.status,
  projects.progress_percent,
  projects.priority,
  projects.due_date,
  COUNT(tasks.id) as total_tasks,
  SUM(CASE WHEN tasks.status = 'done' THEN 1 ELSE 0 END) as completed_tasks,
  projects.origin_idea_id
FROM projects
LEFT JOIN tasks ON tasks.project_id = projects.id
WHERE projects.status IN ('ACTIVE', 'PLANNED')
GROUP BY projects.id
ORDER BY projects.priority DESC, projects.due_date ASC
```

**UI Components:**
- **Header:** "Portfolio: {X}/{Y} active projects ({Z}% capacity)"
- **Filters:** Status (ALL/ACTIVE/PLANNED), Priority (ALL/HIGH/MEDIUM/LOW), Sphere
- **Sort:** Priority, Due Date, Progress, Created Date
- **Project Cards:** Title, Progress bar, Due date badge, Priority badge, Task count
- **Actions:** [View Details] [Edit] [Archive]

**Example View:**
```
Portfolio Dashboard                                    3/5 Active (60% capacity)
───────────────────────────────────────────────────────────────────────────────
[Filters: Status ▼] [Priority ▼] [Sphere ▼]        [Sort: Priority ▼]

┌─────────────────────────────────────────────────────────────────────┐
│ 🔴 Life OS v3.0 Implementation                        Progress: 67% │
│ Due: 2026-03-15 · Business · 12/18 tasks done                       │
│ [View Details] [Edit]                                               │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ 🟠 Personal Finance Dashboard                         Progress: 45% │
│ Due: 2026-02-28 · Finance · 5/11 tasks done                         │
│ [View Details] [Edit]                                               │
└─────────────────────────────────────────────────────────────────────┘
```

---

### 1.13.2 Decision Queue (Готовые к принятию решений)

**Purpose:** Show all evaluated ideas waiting for GO/NO-GO decision.

**Data Requirements:**
```sql
SELECT
  ideas.id,
  ideas.title,
  ideas.sphere,
  ideas.score,
  ideas.decision_status,
  ideas.evaluated_at,
  ideas.track_type
FROM ideas
WHERE ideas.status = 'EVALUATED'
  AND ideas.decision_status IS NULL
ORDER BY ideas.score DESC, ideas.evaluated_at ASC
```

**UI Components:**
- **Header:** "Decision Queue: {N} ideas waiting"
- **Filters:** Track (ALL/QUICK/STANDARD/DEEP), Sphere, Score range
- **Sort:** Score (DESC), Evaluated date (ASC)
- **Idea Cards:** Title, Score badge (color-coded), Sphere badge, Track type, Date evaluated
- **Actions:** [Make Decision] [View Details] [Re-evaluate]

**Decision Button Actions:**
- **GO** → Move to `ideas-bank/planned/`
- **NO-GO** → Archive to `ideas-bank/archive/rejected/`
- **WAIT** → Archive to `ideas-bank/archive/postponed/`

**Example View:**
```
Decision Queue                                           5 ideas waiting
───────────────────────────────────────────────────────────────────────────────
[Filters: Track ▼] [Sphere ▼] [Score ▼]               [Sort: Score ▼]

┌─────────────────────────────────────────────────────────────────────┐
│ SaaS Project Management Tool                          Score: 4.5/5.0 │
│ 🟢 HIGH Priority · Business · Deep Track · Evaluated: 2 days ago     │
│ [GO ✅] [NO-GO ❌] [WAIT ⏸️] [View Details]                          │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ Health Tracking App                                   Score: 3.2/5.0 │
│ 🟡 MEDIUM Priority · Health · Standard · Evaluated: 5 days ago       │
│ [GO ✅] [NO-GO ❌] [WAIT ⏸️] [View Details]                          │
└─────────────────────────────────────────────────────────────────────┘
```

---

### 1.13.3 Today View (План на сегодня)

**Purpose:** Daily TODO list with time blocks and progress tracking.

**Data Requirements:**
```sql
SELECT
  tasks.id,
  tasks.title,
  tasks.project_id,
  projects.title as project_title,
  tasks.status,
  tasks.priority,
  tasks.estimate_hours,
  tasks.energy_level,
  tasks.due_date,
  calendar_events.start_time,
  calendar_events.end_time
FROM tasks
LEFT JOIN projects ON projects.id = tasks.project_id
LEFT JOIN calendar_events ON calendar_events.task_id = tasks.id
WHERE projects.status = 'ACTIVE'
  AND tasks.status IN ('todo','in_progress','blocked')
  AND (
    (tasks.due_date IS NOT NULL AND tasks.due_date <= CURRENT_DATE)
    OR calendar_events.start_time::date = CURRENT_DATE
  )
ORDER BY calendar_events.start_time ASC, tasks.priority DESC
```

**UI Components:**
- **Header:** "Today: {DATE} · {X}/{Y} tasks done · {Z} hours planned"
- **Time Blocks:** Hourly calendar view (8am - 8pm)
- **Task List:** Grouped by time of day (Morning/Afternoon/Evening)
- **Energy Indicators:** 🔴 High, 🟡 Medium, 🔵 Low
- **Actions:** [Mark Done ✅] [Reschedule ⏰] [Start Timer ▶️]

**Example View:**
```
Today: Thursday, Feb 6, 2026                          3/8 tasks done · 6h planned
───────────────────────────────────────────────────────────────────────────────
Morning (High Energy)                                              8:00 - 12:00
┌─────────────────────────────────────────────────────────────────────┐
│ ✅ Review PR #142 (Life OS v3.0)                      2h · 🔴 High   │
│ Started: 8:30am · Completed: 10:15am                               │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ ⏳ Implement Section 1.9 (Life OS v3.0)               3h · 🔴 High   │
│ Scheduled: 10:30am - 1:30pm                    [Mark Done] [Start] │
└─────────────────────────────────────────────────────────────────────┘

Afternoon (Medium Energy)                                        2:00 - 6:00
┌─────────────────────────────────────────────────────────────────────┐
│ 📝 Update documentation (Life OS v3.0)                1h · 🟡 Medium │
│ Scheduled: 2:00pm - 3:00pm                     [Mark Done] [Start] │
└─────────────────────────────────────────────────────────────────────┘
```

---

### 1.13.4 Calendar View (Временные блоки)

**Purpose:** Visual timeline of all scheduled tasks across weeks/months.

**Data Requirements:**
```sql
SELECT
  calendar_event.id,
  calendar_event.task_id,
  tasks.title,
  tasks.project_id,
  projects.title as project_title,
  projects.color,
  calendar_event.start_time,
  calendar_event.end_time,
  calendar_event.calendar_type
FROM calendar_events
LEFT JOIN tasks ON tasks.id = calendar_event.task_id
LEFT JOIN projects ON projects.id = tasks.project_id
WHERE calendar_event.start_time >= :start_date
  AND calendar_event.start_time <= :end_date
ORDER BY calendar_event.start_time ASC
```

**UI Components:**
- **Views:** Day / Week / Month / Agenda
- **Filters:** Calendar type (Work/Personal), Project, Priority
- **Time Blocks:** Color-coded by project (draggable for reschedule)
- **Sidebar:** Unscheduled tasks list
- **Actions:** [Create Event] [Drag to Schedule] [Edit] [Delete]

**Example Week View:**
```
Week of Feb 3 - Feb 9, 2026                               [Day][Week][Month]
───────────────────────────────────────────────────────────────────────────────
         Mon 3      Tue 4      Wed 5      Thu 6      Fri 7      Sat 8  Sun 9
8:00  ┌─────────┐
      │ PR #142 │
10:00 └─────────┘  ┌─────────┐  ┌─────────┐  ┌─────────┐
                   │Section   │  │Testing  │  │Deploy   │
12:00              │1.9       │  │         │  │         │
                   └─────────┘  └─────────┘  └─────────┘
```

---

### 1.13.5 Project Detail Page (Детали проекта)

**Purpose:** Complete project information with plan, risks, tasks, and progress.

**Data Requirements:**
```sql
-- Main project data
SELECT * FROM projects WHERE id = :project_id;

-- Tasks breakdown
SELECT
  task.status,
  COUNT(*) as count,
  SUM(task.estimate_hours) as total_hours,
  SUM(task.actual_hours) as spent_hours
FROM tasks
WHERE task.project_id = :project_id
GROUP BY task.status;

-- Linked goal
SELECT * FROM goals WHERE id = (SELECT goal_id FROM projects WHERE id = :project_id);

-- Origin idea
SELECT * FROM ideas WHERE id = (SELECT origin_idea_id FROM projects WHERE id = :project_id);

-- Recent activity
SELECT * FROM activity_log WHERE project_id = :project_id ORDER BY created_at DESC LIMIT 10;
```

**UI Components:**
- **Header:** Project title, Status badge, Priority badge, Progress bar
- **Tabs:** Overview / Tasks / Plan / Risks / Timeline / Activity
- **Overview Tab:** Description, Goal link, Origin idea link, Key metrics
- **Tasks Tab:** Kanban board (TODO / IN PROGRESS / BLOCKED / DONE)
- **Plan Tab:** Milestones, Dependencies graph
- **Risks Tab:** Risk register (likelihood × impact matrix)
- **Timeline Tab:** Gantt chart with critical path
- **Activity Tab:** Changelog (who did what when)

**Example View:**
```
Life OS v3.0 Implementation                            🔴 HIGH · ⏳ ACTIVE
Progress: ████████████████████░░░░ 67% (12/18 tasks)  Due: Mar 15, 2026
───────────────────────────────────────────────────────────────────────────────
[Overview] [Tasks] [Plan] [Risks] [Timeline] [Activity]

Overview
────────
📊 Key Metrics
  • Tasks: 12/18 done (6 remaining)
  • Time: 48h spent / 72h estimated (67%)
  • Budget: $1,200 / $2,000 (60%)

🎯 Linked Goal
  → 2026-business-q1-1: "Ship v3.0 by Q1 end"
  → Progress to goal: 67% (on track)

💡 Origin Idea
  → idea-042: "Complete Life OS system with memory + UI"
  → Score: 4.7/5.0 (evaluated 2025-12-20)

Recent Activity
───────────────
• 2h ago: Task "Review PR #142" marked as done by @user
• 5h ago: Task "Implement Section 1.9" started by @user
• 1d ago: Risk "UI complexity" severity reduced (HIGH → MEDIUM)
```

---

### 1.13.6 Query Optimization Notes

**Critical Queries (Must Be <200ms):**
1. Portfolio Dashboard: Index on `(project.status, project.priority, project.due_date)`
2. Decision Queue: Index on `(idea.status, idea.score DESC, idea.evaluated_at)`
3. Today View: Index on `(task.due_date, task.priority, calendar_event.start_time)`
4. Calendar View: Index on `(calendar_event.start_time, calendar_event.calendar_type)`
5. Project Detail: Index on `(project.id)` + denormalized task counts

**Caching Strategy:**
- Portfolio Dashboard: Cache 5 minutes (invalidate on project create/update)
- Today View: No cache (real-time)
- Calendar View: Cache 10 minutes (invalidate on event create/update)

---

## 1.14 Planning Data Model (Источник правды для диаграмм)

### 1.14.1 Milestone Schema (Основные вехи проекта)

**Purpose:** Define key checkpoints in project timeline (used for Gantt chart generation).

**Milestone Data Model:**
```yaml
milestone_id: string       # Unique ID (e.g., "milestone-001-mvp")
project_id: string         # Parent project
title: string              # Milestone name (e.g., "MVP Launch")
description: string        # What defines this milestone as complete
target_date: date          # Planned completion date (ISO 8601)
actual_date: date          # Actual completion (null if not reached)
status: enum               # [not_started, in_progress, completed, missed]
progress_percent: number   # 0-100 (calculated from linked tasks)
dependencies: string[]     # Other milestone_ids that must complete first
critical_path: boolean     # Is this on critical path? (auto-calculated)
deliverables: string[]     # List of artifacts expected (files, features, etc.)
validation_criteria: string[] # How to verify milestone is truly done
created_at: timestamp
updated_at: timestamp
```

**Mandatory Fields:**
- `milestone_id`, `project_id`, `title`, `target_date`, `status`

**Storage:**
- **Phase 1-2:** `projects/project-XXX/milestones.yaml` (single file with array)
- **Phase 3:** Supabase `milestones` table

---

### 1.14.2 Task Dependency Schema (Связи между задачами)

**Purpose:** Define execution order constraints for tasks (used for critical path calculation).

**Dependency Types:**
```
1. finish_to_start (FS): Task B cannot start until Task A finishes (most common)
2. start_to_start (SS): Task B cannot start until Task A starts (parallel dependency)
3. finish_to_finish (FF): Task B cannot finish until Task A finishes (synchronization)
4. start_to_finish (SF): Task B cannot finish until Task A starts (rare)
```

**Dependency Data Model:**
```yaml
dependency_id: string      # Unique ID (e.g., "dep-001-task-a-to-b")
project_id: string         # Parent project
predecessor_id: string     # Task that must happen first
successor_id: string       # Task that depends on predecessor
dependency_type: enum      # [FS, SS, FF, SF] (default: FS)
lag_days: number           # Additional delay (e.g., 2 = wait 2 days after predecessor)
lead_days: number          # Allow early start (e.g., -1 = start 1 day before)
is_hard: boolean           # Hard constraint (cannot violate) vs soft (prefer but not strict)
created_at: timestamp
```

**Validation Rules:**
- No circular dependencies (detect with DFS/topological sort)
- Predecessor and successor must belong to same project
- Lag/lead cannot both be non-zero (mutually exclusive)

**Storage:**
- **Phase 1-2:** `projects/project-XXX/dependencies.yaml`
- **Phase 3:** Supabase `task_dependencies` table

---

### 1.14.3 Gantt Chart Generation Algorithm

**Input Data:**
- Milestones (with target dates)
- Tasks (with estimate_hours and dependencies)
- Project start_date
- Team capacity (from resource assessment)

**Algorithm Steps:**

```
1. Build Dependency Graph
   - Create nodes for all tasks
   - Create edges for all dependencies (respecting type: FS/SS/FF/SF)
   - Detect cycles (error if found)

2. Topological Sort
   - Order tasks so dependencies are respected
   - Identify parallel tracks (tasks with no dependencies between them)

3. Forward Pass (Calculate Earliest Start/Finish)
   For each task in topological order:
     - Earliest_Start = MAX(dependency.finish + lag) OR project.start_date
     - Earliest_Finish = Earliest_Start + task.estimate_hours / team_capacity
     - Store in task metadata

4. Backward Pass (Calculate Latest Start/Finish)
   For each task in reverse topological order:
     - Latest_Finish = MIN(dependent.start - lag) OR project.due_date
     - Latest_Start = Latest_Finish - task.estimate_hours / team_capacity
     - Store in task metadata

5. Calculate Slack (Float)
   For each task:
     - Total_Slack = Latest_Start - Earliest_Start
     - Free_Slack = MIN(successor.Earliest_Start - task.Earliest_Finish)

6. Identify Critical Path
   - Critical tasks = tasks where Total_Slack = 0
   - Critical path = longest sequence of critical tasks from start to end
   - Mark milestones on critical path with critical_path = true

7. Generate Gantt Bars
   - X-axis: Calendar dates (start_date to due_date)
   - Y-axis: Tasks (grouped by milestone or assignee)
   - Bar length: Earliest_Start to Earliest_Finish
   - Bar color: Critical (red), High priority (orange), Normal (blue)
   - Dependencies: Arrows connecting bars
```

**Output Format (JSON for UI):**
```json
{
  "project_id": "project-002",
  "start_date": "2026-02-01",
  "end_date": "2026-03-15",
  "critical_path_duration_days": 32,
  "total_slack_days": 5,
  "tasks": [
    {
      "task_id": "task-001",
      "title": "Setup database",
      "earliest_start": "2026-02-01",
      "earliest_finish": "2026-02-03",
      "latest_start": "2026-02-01",
      "latest_finish": "2026-02-03",
      "total_slack_days": 0,
      "is_critical": true,
      "dependencies": []
    },
    {
      "task_id": "task-002",
      "title": "Build API",
      "earliest_start": "2026-02-03",
      "earliest_finish": "2026-02-10",
      "latest_start": "2026-02-05",
      "latest_finish": "2026-02-12",
      "total_slack_days": 2,
      "is_critical": false,
      "dependencies": ["task-001"]
    }
  ],
  "critical_path": ["task-001", "task-003", "task-007", "task-012"]
}
```

---

### 1.14.4 Roadmap Generation (High-Level Timeline)

**Purpose:** Show milestone-based timeline for stakeholder communication (less granular than Gantt).

**Input Data:**
- Milestones (with target_date and deliverables)
- Project phases (if defined)

**Generation Rules:**

```
1. Group milestones by phase (if phases exist)
   - Example phases: Discovery, Design, Development, Testing, Launch

2. Place milestones on timeline
   - X-axis: Calendar months/quarters
   - Y-axis: Project streams (if multiple projects)
   - Milestone markers: Diamond shapes at target_date

3. Show dependencies between milestones
   - Dotted arrows connecting dependent milestones
   - Color-code by status (not_started=gray, in_progress=yellow, completed=green)

4. Highlight current period
   - Vertical line showing "Today"
   - Shade past (gray), present (blue), future (white)

5. Add progress indicators
   - % complete per milestone
   - On track / At risk / Delayed status
```

**Output Format (Markdown for simple view):**
```markdown
# Project Roadmap: Life OS v3.0

Q1 2026
───────────────────────────────────────────────────────────────
◆ Jan 15: Foundation Complete (✅ 100%)
    └─ Deliverables: Resource assessment, goals.yaml, speed multipliers

◆ Feb 15: Core Workflow Complete (⏳ 67%)
    └─ Deliverables: L1-L2 steps, BMAD integration, memory system
    └─ Dependencies: Foundation Complete

◆ Mar 15: MVP Launch (⏸️ 0%)
    └─ Deliverables: CLI + Web UI, documentation, first user onboarding
    └─ Dependencies: Core Workflow Complete

Legend: ✅ Done | ⏳ In Progress | ⏸️ Not Started | ⚠️ At Risk
```

---

### 1.14.5 Source of Truth Hierarchy

**For Gantt Chart:**
1. **Primary:** Task dependencies (task-level detail)
2. **Secondary:** Milestone target dates (high-level checkpoints)
3. **Constraints:** Project start_date, due_date, team capacity

**For Roadmap:**
1. **Primary:** Milestone target dates (strategic view)
2. **Secondary:** Milestone dependencies (sequencing)
3. **Context:** Project phases (if applicable)

**Update Triggers:**
- Task dependency added/removed → Regenerate Gantt (recalculate critical path)
- Milestone date changed → Regenerate Roadmap (adjust dependent milestones)
- Task estimate changed → Regenerate Gantt (recalculate finish dates)
- Task completed → Update milestone progress (auto-calculate % from tasks)

**Validation Rules:**
- Milestone target_date must be >= latest task.earliest_finish for all tasks linked to milestone
- Project due_date must be >= latest milestone.target_date
- Critical path duration cannot exceed (due_date - start_date)

**Error Handling:**
- If critical path exceeds project timeline → Flag "⚠️ Timeline at Risk" + suggest compression:
  - Add resources (increase team capacity)
  - Reduce scope (remove non-critical tasks)
  - Extend deadline (negotiate due_date)

---

### 1.14.6 Integration with UI (Section 1.13)

**Project Detail Page → Timeline Tab:**
- Display Gantt chart (generated from Section 1.14.3 algorithm)
- Show critical path highlighted in red
- Allow drag-and-drop to reschedule tasks (updates dependencies)
- Display milestone markers on timeline

**Portfolio Dashboard → Roadmap View:**
- Display roadmap across all active projects (generated from Section 1.14.4)
- Filter by project, phase, or status
- Show cross-project dependencies (if any)

**Today View → Dependency Warnings:**
- If task has unmet dependencies → Show "⚠️ Blocked by: [task-xxx]"
- Suggest alternative tasks from same project (no blockers)

---

## 1.15 Mass Deep Planning Mode (Batch, Cross-sphere)
**Goal:** Batch deep research and planning for any sphere of life using a shared mode that supports iterative depth up to L6 and responds to new facts without SaaS bias.

### 1.15.1 Menu
```
Mass Deep Plan Mode
[B] Batch Reevaluate
[N] New Inputs Intake
[R] Rebuild Plan (L1–L6)
[S] Snapshot & Drift Check
[C] Capacity & Calendar Sync
[X] Exit
```

### 1.15.2 Flow
```
IDLE -> INTAKE -> EVALUATE -> DECIDE -> PLAN_L1L6 -> GATES -> INTEGRATE -> FINALIZE -> IDLE
```

### 1.15.3 Triggers
- New facts change timeline/resources >20%
- Drift between plan and actual exceeds 30%
- Resource/capacity updates or blockers >3 days
- Alignment <3/5 against goals.yaml
- Weekly review flags burnout or overcommit

### 1.15.4 Iterative depth
- L1: Intent and strategic outcome
- L2: Key results/milestones
- L3: Epics or phases
- L4: Stories or outcomes
- L5: Tasks
- L6: Steps and checklists

### 1.15.5 Artifacts
- `ideas-bank/idea-XXX-sphere-*.md`
- `projects/.../plan.md`, `milestones.yaml`, `dependencies.yaml`
- `portfolio.md`, `decision-log.md`, `snapshot-YYYY-MM-DD.md`, `metrics/metrics.md`
- Memory keys `mass-deep:batch-{date}` and `life-os:idea-XXX:plan-history`

### 1.15.6 Automation mode
- YOLO-style automation is confined to Mass Deep Plan Mode; quality gates remain enforced
- Failed gate auto-triggers `PIVOT` or `WAIT`

## 1.16 Goals Discovery + PDCA Cascade
### 1.16.1 Goals discovery (Step 00)
- Capture 1y, 3y, 5–10y targets per sphere (health, wealth, relationships, growth, contribution)
- Store `goals.yaml` with finance/business/career/health/personal/legacy/impact buckets
- Feed goals into Strategic Alignment, role selection, scoring thresholds

### 1.16.2 Goal cascade
Year -> H1/H2 -> Quarter -> Month -> Week -> Day (TODO); every task references `goal_id` and weekly reviews validate trajectory

### 1.16.3 PDCA reviews
- Daily (5 min): completion, blockers, carryovers
- Weekly (30 min): focus vs quarterly goals, velocity, blockers
- Monthly (60 min): trends, capacity, burnout risk
- Quarterly (120 min): strategy pivot, backlog grooming, hypothesis testing

### 1.16.4 Metrics & auto-adjust
- velocity, completion_rate, burnout_risk, capacity_utilization
- Weekly velocity <50% → reallocate time
- Monthly drift >20% → scale back scope
- Quarterly off-track → replan with new hypotheses

## 1.17 Session State Management
### 1.17.1 Frontmatter contract
Each idea/workflow file tracks `status`, `pauseReason`, `pauseDate`, `decisionDeadline`, `completionPercentage`, `stepsCompleted`

### 1.17.2 Resume block template
```
## Resume Point
Last Updated: YYYY-MM-DD
Current Status: PAUSED/IN_PROGRESS
Where We Are: steps, score
Waiting For: approvals/data
Outputs: files created
How To Resume: actions/commands, next step
```

### 1.17.3 Memory keys
- `life-os:idea-XXX:session-YYYY-MM-DD`
- `life-os:idea-XXX:step-XX-complete`
- `life-os:idea-XXX:score-history`
- `life-os:idea-XXX:decision-YYYY-MM-DD`

### 1.17.4 Pause/resume flow
1. User pauses or waits for data
2. Update frontmatter, resume block, global memory
3. On resume: load block, query memory, ask for updates, continue from documented state

## 1.18 Swarm + Consilium Orchestration
### 1.18.1 When to autostart
- Deep/Batch/Mass deep planning invokes swarm automatically
- Lite Quick/Standard skip swarm unless complexity >70%
- TRIZ, Advanced Elicitation, stakeholder consilium force swarm coordination

### 1.18.2 Configuration
Hierarchical topology, maxAgents 6–8, strategy specialized, consensus raft; roles include coordinator, researcher, finance analyst, risk manager, operations, integration leads

### 1.18.3 Fallback
If MCP swarm unavailable, fall back to Task-tool parallel agents; log agent IDs and memory entries under `consilium:session-{id}`

### 1.18.4 SLOs
- Completion time <10 minutes vs 20–30 sequential
- Quality score ≥8.5/10
- Memory summaries stored per agent for synthesis

## 1.19 Artifact Architecture
- `goals.yaml` (1y/3y/5–10y hierarchy)
- `mass-deep-plan.md` (mode definition, menu, triggers)
- PDCA review templates (daily/weekly/monthly/quarterly)
- Resume block template and memory key references
- `swarm/orchestration.yaml` describing auto-service
- Cross-links to `step-00`, `step-04`, `step-05`, `step-07`, etc.

## 1.20 Execution Plan
1. Proofread this document and align numbering
2. Update relevant `step-*.md` files (step-00, step-04, etc.) to reference new sections
3. Validate gating, goals, and memory rules via checklist
4. Add CI check: ensure IDEAL is cited before workflows mark completion

## 1.21 Validation & Max Parallel Mode
**Цель:** Зафиксировать требования к методу `validate-max-parallel`, чтобы каждый запуск проверки фиксировал IDEAL-совместимость и снабжал агрегированный отчет фрагментами с шагами, которые сольются в единый вывод.

### 1.21.1 Pipeline Overview
- Стартует из `_bmad/bmb/workflows/workflow/workflow.md` по команде `validate workflow MAX-PARALLEL` или `--validate-max`. Конфиг загружается, session запускается, а затем запускаются 11 (плюс план) параллельных шагов:
  1. `step-01b-structure.md` – структура и лимиты по длине
  2. `step-02-frontmatter-validation.md` – переменные и пути
  3. `step-02b-path-violations.md` – контентные путевые нарушения
  4. `step-03-menu-validation.md` – меню и хэндлеры
  5. `step-04-step-type-validation.md` – типы шагов
  6. `step-05-output-format-validation.md` – шаблоны и финальный полир
  7. `step-06-validation-design-check.md` – проект валидации/качества
  8. `step-07-instruction-style-check.md` – тон и стиль
  9. `step-08-collaborative-experience-check.md` – фасилитация
 10. `step-08b-subprocess-optimization.md` – оптимизация subprocess
 11. `step-09-cohesive-review.md` – когезивная оценка
 12. При наличии `workflow-plan.md` запускается `step-11-plan-validation.md`.
Каждый шаг пишет собственный файл `validation-report-step-XX-...md` и возвращает результат, который затем включается в финальный агрегированный `validation-report-{datetime}.md`.

### 1.21.2 Reporting & Remediation
- Записывайте ссылки на все промежуточные отчеты и включайте их в карточки действий — они содержат предупреждения о размере, неиспользованных фронтматтер-переменных, мёртвых ссылках, отсутствующих redisplay-инструкциях и несовместимости выходных файлов.
- Сводный отчет обновляет `validationStatus` до `COMPLETE` и добавляет финальную секцию «Summary» со статусами всех шагов. `Consilium Plan` (см. Section 1.21.4) хранит привязки ошибок к IDEAL-разделам.
- Если скрипт выдаёт критические ошибки, остановитесь, исправьте файлы, перезапустите `validate-max-parallel`. Не используйте альтернативную, более медленную последовательную проверку без явной команды пользователя.

### 1.21.3 IDEAL Alignment by Step
- **Step 01b – Structure:** выбирает системное поведение и архитектуру (Sections 1.4, 1.19). Проверяйте, что структура шагов отражает North Star, а folders/docs/ описывают цели, оценку и outputs.
- **Step 02/02b – Frontmatter & Paths:** опираются на конфигурацию (Section 1.9) и хранение артефактов (Section 1.19). Frontmatter должен ссылаться на `goals.yaml`, `stepsCompleted` и относительные пути.
- **Step 03 – Menu:** проверяет фасилитацию (Section 1.3 и 1.18). Меню обязаны перечислять роли и манипуляции, описанные в IDEAL use cases.
- **Step 04 – Step Type:** выравнивает реализацию с профилем (Section 1.11) и SaaS Autonomy Gate (Section 1.10). Валидация подтверждает, что init/branch/validation-шаги оформлены правильно.
- **Step 05 – Output Format:** опирается на план/модель (Section 1.14) и гарантирует, что шаблон и шаги заканчиваются финальным полиром.
- **Step 06 – Validation Design:** проверяет PDCA и цели (Section 1.16) на предмет четких шагов и данных.
- **Step 07 – Instruction Style:** сверяет с пользовательским путешествием и intent-based подходом (Section 1.3 и 1.4).
- **Step 08/08b – Collaborative & Optimization:** оценивают фасилитацию и subprocess-архитектуру (Sections 1.3, 1.18).
- **Step 09 – Cohesive Review:** подтверждает, что весь поток достигает North Star (Section 1.1).
- **Step 10 – Report Complete:** сопровождает Execution Plan (Section 1.20) и finalizes summary.
- **Step 11 – Plan Validation (если есть):** используется для проверки Session State и Plan Quality (Section 1.17).

### 1.21.4 Consilium Coaching Loop
- После каждого прогона `validate-max-parallel` обновляйте `consilium-plan.md` ссылками на фрагменты, приводите действия в порядке приоритета, и сохраняйте вывод в глобальную память (`shared-knowledge:learnings:life-os-validation`) для долговременного использования.
- Если одна из частичных проверок возвращает WARN/FAIL, напишите короткую заметку: какой шаг нарушен, какая секция IDEAL (см. пункты 1.2–1.20) от него зависит, и когда планируете повторный запуск.
- `Consilium Plan` рассматривает Section 1.21 как стандарт выполнения: после чистого прогона соответствующая оценка переходит в «Deployment ready», а в отчете фиксируется версия (например, `validation-report-2026-02-09-000252.md`).
## How to Use This Document

**For Validation:**
- Compare actual system behavior against ideal behavior described here
- Check each use case, perspective, flow, and quality standard
- Identify gaps: what's missing, what's incorrect, what's incomplete

**For Critique:**
- Use North Star Alignment Verification table to validate each element
- Check if all 6 North Star elements are present and working
- Verify data flows match the diagrams

**For Future Improvements:**
- Use as baseline for new features
- Ensure new features align with ideal behavior
- Update this document when North Star vision evolves

**For User Training:**
- Show users what to expect from the system
- Set correct expectations for each track (Quick/Standard/Deep)
- Explain system behavior principles

**For Implementation:**
- Use **Section 1.9** as source of truth for sphere/domain/criteria configurations
  - 1.9.1: Sphere & Domain Registry (life spheres, goal domains, project domains)
  - 1.9.2: Scoring criteria (5+N system with SaaS Autonomy)
  - 1.9.3: D/F/V/C rubrics by goal domain
  - 1.9.4: Developer profile adjustments
- Apply **Section 1.10** (SaaS Autonomy Gate) when evaluating SaaS/software ideas
- Follow **Section 1.11** for recommended tech stack and deployment architecture
  - 1.11.2.1: Choose deployment variant (Global/RU/Offline) based on requirements
  - Note: Stack is recommended, not mandatory - adapt to team preferences
  - Markdown-first architecture works with any tool (Obsidian, VS Code, CLI)
- Implement **Section 1.12** (Task Layer Spec) as contract for task system
  - Source of truth: Markdown (Phase 1-2) or Supabase (Phase 3)
  - Sync rules: One-way (Phase 2) or Two-way (Phase 3)
  - Daily TODO generation algorithm
- Build **Section 1.13** (UI Minimum Screens) as mandatory interface requirements
  - 5 core screens: Portfolio, Decision Queue, Today, Calendar, Project Detail
  - Query requirements and caching strategies included
- Use **Section 1.14** (Planning Data Model) for Gantt/roadmap generation
  - Milestone schema and task dependencies
  - Critical path calculation algorithm
  - Roadmap generation rules

---

**Document Status:** ✅ PERMANENT REFERENCE + IMPLEMENTATION GUIDE
**Last Updated:** 2026-02-06 (v2.1: Added Sections 1.12-1.14, fixed weight normalization wording, added deployment variants, clarified scoring + UI queries)
**Version:** 2.1 (Patch: Fixed terminology clarity + execution contracts)

**Version History:**
- **v2.1** (2026-02-06): Added execution contracts - Task Layer (1.12), UI Screens (1.13), Planning Data Model (1.14), Weight Normalization fix (1.9.2), Deployment Variants (1.11.2.1)
- **v2.0** (2026-02-06): Added implementation specifications - Configuration Specs (1.9), SaaS Autonomy Gate (1.10), Implementation Profile (1.11)
- **v1.0** (2026-02-06): Initial - North Star, Use Cases, User/System/Data/Quality/Integration perspectives

**Next Review:** When major architectural changes proposed OR tech stack evolution (e.g., Phase 3 mobile)
