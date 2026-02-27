---
created: 2026-02-05
status: BACKLOG
---

# Доработки системы Life OS

## Доработка: Указание сферы в названии файлов идей

**Что:** Добавить префикс сферы в название файлов идей для быстрой идентификации

**Текущий формат:** `idea-XXX-name.md`
**Новый формат:** `idea-XXX-sphere-name.md`

**Примеры:**
- `idea-001-finance-katana-vectorbt.md`
- `idea-002-business-maps-auto-reply.md`
- `idea-007-business-beauty-franchise.md`

**Сферы:**
- `finance` - Финансы
- `business` - Бизнес
- `software` - Софт (может быть комбо с бизнесом)
- `health` - Здоровье
- `personal` - Личное развитие
- `content` - Контент/Медиа

**Преимущества:**
- ✅ Быстрая фильтрация по сфере через `ls` или проводник
- ✅ Группировка связанных идей
- ✅ Упрощение поиска при большом количестве идей

**Приоритет:** LOW (удобство, не критично)
**Когда внедрить:** При следующем рефакторинге структуры файлов

---

## Доработка: Сбор долгосрочных целей (КРИТИЧНО)

**Что:** Добавить Step 0 (pre-Step 1) для сбора долгосрочных целей пользователя на 1-3-5-10 лет

**Проблема:**
- Сейчас Life OS оценивает идеи БЕЗ понимания долгосрочных целей пользователя
- Strategic Alignment оценивается "вслепую" - непонятно, с чем align'имся
- Невозможно правильно приоритезировать идеи без контекста целей

**Решение:**
Создать `step-00-goals-discovery.md` который запускается:
- При первом использовании Life OS (один раз)
- При явном запросе обновления целей (раз в 6-12 месяцев)

**Что собирать:**
1. **1-Year Goals (текущий год):**
   - Финансы (доход, сбережения, инвестиции)
   - Карьера (должность, навыки, проекты)
   - Здоровье (вес, фитнес, питание)
   - Личное (отношения, хобби, образование)

2. **3-Year Goals (среднесрочные):**
   - Бизнес-цели (запуск компании, масштабирование)
   - Капитал (накопления, портфель, passive income)
   - Экспертиза (стать экспертом в области X)
   - Lifestyle (переезд, путешествия, work-life balance)

3. **5-10-Year Vision (долгосрочные):**
   - Legacy goals (что оставить после себя)
   - Financial independence (FIRE, пассивный доход)
   - Impact goals (кому помочь, какую проблему решить)
   - Personal fulfillment (что сделает жизнь наполненной)

**Формат хранения:**
```yaml
goals:
  1_year:
    finance: "Доход ₽X млн/год, инвестиции ₽Y млн"
    career: "Запустить 2 profitable проекта"
    health: "Вес Z кг, бег 10 км без остановки"
    personal: "Выучить английский C1"
  3_year:
    business: "Компания с оборотом ₽XX млн/год"
    capital: "Портфель ₽YY млн, passive income ₽Z тыс/мес"
    expertise: "Топ-10 эксперт в области AI/trading"
    lifestyle: "Remote work, 3 месяца/год travel"
  5_10_year:
    legacy: "Создать образовательную платформу для X"
    financial_independence: "FIRE к возрасту Y, passive income ₽Z млн/год"
    impact: "Помочь N людям достичь финансовой независимости"
    fulfillment: "Баланс работы, семьи, творчества"
updated: 2026-02-05
next_review: 2026-08-05
```

**Использование в Life OS:**
- **Step 02 (Roles):** Подбор ролей на основе целей
- **Step 05 (Scoring):** Strategic Alignment считается относительно goals
- **Step 06 (Integration):** Portfolio buckets отражают distribution целей
- **Step 08 (Deep Plan):** Timeline согласован с milestone'ами целей

**Преимущества:**
- ✅ Правильная приоритизация идей (какие работают на долгосрочные цели)
- ✅ Фильтрация "шумных" идей (интересно, но не по целям)
- ✅ Мотивация (видишь, как проект приближает к цели)
- ✅ Review прогресса (раз в 6 месяцев: где я vs где должен быть)

**Приоритет:** 🔴 **CRITICAL** (влияет на качество всех решений)

**Когда внедрить:**
- Краткосрочно: Спросить у пользователя цели прямо сейчас (ad-hoc)
- Долгосрочно: Создать step-00-goals-discovery.md в следующей версии

**Временное решение (для текущей сессии):**
Спросить 3 вопроса:
1. Главная цель на 2026 год? (1 предложение)
2. Чего хочешь достичь к 2029 году? (3 года)
3. Какая твоя ultimate vision (5-10 лет)? (legacy/impact/lifestyle)

Ответы сохранить в `goals.md` и использовать для оценки идей.

---

## Доработка: PDCA цикл + Унифицированная система планирования (КРИТИЧНО)

**Что:** Внедрить PDCA (Plan-Do-Check-Act) цикл с интеграцией целей, todo листа и календаря

**Проблема:**
- Цели на год/полгода/квартал/месяц/неделю существуют отдельно
- Todo лист на день не связан с долгосрочными целями
- Календарь не синхронизирован с приоритетами
- Нет систематического review цикла (Check + Act отсутствуют)

**PDCA Framework:**

### 📋 PLAN (Планирование)
**Иерархия целей:**
```
Год (2026)
├── Полугодие 1 (H1: Jan-Jun)
│   ├── Квартал 1 (Q1: Jan-Mar)
│   │   ├── Месяц 1 (Январь)
│   │   │   ├── Неделя 1
│   │   │   │   └── День 1 (TODO)
│   │   │   └── Неделя 2-4
│   │   └── Месяц 2-3
│   └── Квартал 2 (Q2: Apr-Jun)
└── Полугодие 2 (H2: Jul-Dec)
```

**Формат хранения:**
```yaml
goals:
  year_2026:
    finance: "Доход ₽X млн, passive income ₽Y тыс/мес"
    business: "2 profitable проекта, $50k MRR"
    health: "Вес Z кг, бег 10 км"
    personal: "Английский C1, 10 книг"

  h1_2026:
    finance: "Katana 2 Scaled-Live, Автоответчик 100 clients"
    business: "MVP обоих проектов, PMF validated"
    health: "Минус 5 кг, пробежать полумарафон"
    personal: "50 lessons английского"

  q1_2026:
    finance: "Katana Epic L complete, Автоответчик funding $36.5k"
    business: "Katana Paper Trading, Автоответчик MVP"
    health: "Минус 2 кг, бег 3x/неделю"
    personal: "20 lessons"

  jan_2026:
    week_1:
      focus: "Katana Epic L + Автоответчик funding"
      todos:
        - "Complete Epic L Story 2"
        - "Research funding options"
        - "Create pitch deck"
    week_2:
      focus: "Innovation Sprint setup"
      todos: [...]
```

### ✅ DO (Выполнение)
**Daily TODO система:**
- Генерируется из недельных целей автоматически
- Приоритизация по Eisenhower Matrix (urgent/important)
- Time-blocking в календаре (каждая задача = calendar event)
- Tracking: TodoWrite с метками (goal_id, week, priority)

**Интеграция с календарём:**
```
08:00-10:00 → [Katana] Epic L Story 2 (goal: q1_2026.finance)
10:00-12:00 → [Автоответчик] Funding research (goal: q1_2026.finance)
14:00-16:00 → [Health] Тренировка (goal: q1_2026.health)
16:00-18:00 → Deep work time
```

### 🔍 CHECK (Проверка)
**Review cadence:**

**Daily (5 мин, end of day):**
- ✅ Что сделано из TODO?
- ⏸️ Что не сделано и почему?
- 📝 Что блокирует прогресс?
- ⏭️ Перенос незавершённого на завтра

**Weekly (30 мин, воскресенье):**
- ✅ Прогресс по недельным целям (%)
- 🎯 Соответствие квартальным целям
- 📊 Метрики (hours worked, tasks completed, blockers)
- 🔄 Adjustments на следующую неделю

**Monthly (1 час, последнее воскресенье):**
- ✅ Прогресс по месячным целям (%)
- 🎯 Trajectory к квартальным целям (on track / behind / ahead)
- 📈 Trend analysis (velocity, quality, burnout risk)
- 🔄 Adjustments к квартальному плану

**Quarterly (2 часа, конец квартала):**
- ✅ Достижение квартальных целей (yes/no + %)
- 🎯 Прогресс к годовым целям (%)
- 🔬 Deep dive: что работает, что нет
- 🔄 Replanning Q2 на основе Q1 learnings

### 🔄 ACT (Корректировка)
**Automated adjustments:**
- Если недельный прогресс <50% → increase time allocation next week
- Если месячный velocity падает → review blockers, reduce scope
- Если квартальные цели off-track >20% → replanning meeting

**Manual interventions:**
- Weekly: adjust priorities на основе review
- Monthly: update квартальный план (scope/timeline/resources)
- Quarterly: pivot strategy если нужно

---

### 🛠️ Техническая реализация

**Файловая структура:**
```
_bmad-output/bmb-creations/life-os/
├── goals.yaml (иерархия целей: год → H1/H2 → Q1-Q4 → месяцы → недели)
├── calendar/ (интеграция с Google Calendar/Outlook)
│   ├── sync-config.yaml
│   └── time-blocks/
├── todos/ (daily todo lists)
│   ├── 2026-02-05.md (сегодня)
│   └── archive/ (completed)
├── reviews/ (PDCA Check фаза)
│   ├── daily/
│   ├── weekly/
│   ├── monthly/
│   └── quarterly/
└── metrics/ (tracking)
    ├── velocity.csv
    ├── completion-rate.csv
    └── burnout-risk.yaml
```

**Автоматизация:**
1. **Goal Cascade:** Год → Недели (автоматическая декомпозиция)
2. **TODO Generation:** Недельные цели → Daily TODO (каждое воскресенье)
3. **Calendar Sync:** TODO → Time blocks (двусторонняя синхронизация)
4. **Review Reminders:** Автоматические напоминания (daily EOD, weekly Sunday, monthly last Sunday)
5. **Metrics Dashboard:** Real-time прогресс по всем уровням

**Workflow Integration:**
- Life OS Step 06 (Integration) → проверяет соответствие goals.yaml
- Life OS Step 07 (Calendar Sync) → автоматически создаёт time blocks
- Life OS Validate mode → использует reviews/ для ежедневных/еженедельных check-ins

---

### 📊 Пример использования

**Сценарий:** Katana + Автоответчик (002+001 parallel)

**Годовая цель (2026):**
```yaml
finance: "Passive income ≥₽100k/мес (Katana 2 Scaled-Live + Автоответчик $50k MRR)"
```

**Q1 цель:**
```yaml
finance: "Katana Epic L complete + Paper Trading started, Автоответчик funding + MVP"
```

**Неделя 1 (Feb 6-12):**
```yaml
focus: "Katana Epic L completion + Автоответчик funding"
todos:
  monday: ["Katana Story 2 coding", "Research investors"]
  tuesday: ["Katana Story 2 testing", "Create pitch deck"]
  wednesday: ["Katana Story 3 start", "Outreach investors"]
  thursday: ["Katana Story 3 coding", "F&F meeting"]
  friday: ["Weekly review", "Plan Week 2"]
```

**Daily TODO (2026-02-06, Monday):**
```markdown
# TODO - 2026-02-06 (Monday)

## 🎯 Week Focus: Katana Epic L + Автоответчик funding

### High Priority (Must Do Today)
- [ ] Katana Story 2: Code data integration layer (2h) → [08:00-10:00]
- [ ] Research 5 potential investors for Автоответчик (1h) → [10:00-11:00]
- [ ] Daily review (5min) → [18:00]

### Medium Priority (Should Do)
- [ ] Katana: Write tests for Story 2 (1h)
- [ ] Update portfolio dashboard (30min)

### Low Priority (Nice to Have)
- [ ] Read article on LLM cost optimization

## 📅 Calendar
08:00-10:00: [Katana] Story 2 coding (goal: q1_2026.finance.katana_epic_l)
10:00-11:00: [Автоответчик] Investor research (goal: q1_2026.finance.funding)
11:00-12:00: Break
14:00-15:00: [Katana] Story 2 testing
18:00-18:05: Daily review
```

**Daily Review (EOD):**
```markdown
# Daily Review - 2026-02-06

## ✅ Completed
- Katana Story 2 coding (2h) ✅
- Investor research (5 потенциальных) ✅

## ⏸️ Not Done
- Katana tests (перенос на завтра)

## 🚧 Blockers
- Нет блокеров

## 📝 Learnings
- Data integration проще чем думал (+30 мин savings)

## ⏭️ Tomorrow
- Finish Katana Story 2 tests
- Create pitch deck
```

---

### 🎯 Преимущества PDCA интеграции

1. ✅ **Alignment:** Каждая дневная задача связана с годовой целью
2. ✅ **Focus:** Недельный focus предотвращает распыление
3. ✅ **Accountability:** Daily/weekly reviews = continuous check
4. ✅ **Adaptability:** Act фаза позволяет корректировать курс
5. ✅ **Visibility:** Dashboard показывает прогресс на всех уровнях
6. ✅ **Burnout prevention:** Metrics отслеживают overload risk

---

### 🚀 Когда внедрить

**Приоритет:** 🔴 **CRITICAL** (основа для всего Life OS)

**Фазы:**
1. **Phase 1 (немедленно):** Собрать годовые цели + Q1 цели (30 мин)
2. **Phase 2 (эта неделя):** Создать Week 1 plan + daily TODO (1 час)
3. **Phase 3 (2 недели):** Автоматизация Goal Cascade + Calendar Sync (4-6 часов)
4. **Phase 4 (1 месяц):** Полная PDCA система с metrics dashboard (8-12 часов)

**Временное решение (прямо сейчас):**
- Использовать простой markdown файл `goals.yaml`
- Manual TODO creation каждое утро
- Manual daily review каждый вечер
- Weekly review воскресенье

---

## Доработка: Автоматический Swarm и параллельное выполнение (КРИТИЧНО)

**Что:** Внедрить автоматический вызов swarm координации для всех consilium шагов с параллельным выполнением агентов

**Проблема:**
- Сейчас swarm вызывается только по явному запросу пользователя ("используй swarm")
- MCP инструмент `mcp__claude-flow__swarm_init` не всегда доступен (tool_use_error)
- Fallback к последовательному Task выполнению теряет преимущество параллелизма
- В Step 04 (Consilium) нет автоматической инициализации swarm координации

**Что УЖЕ РАБОТАЕТ (✅ Текущая реализация):**

### Task-Based Hierarchical Coordination
```javascript
// Используется иерархический подход через Task tool Claude Code
Task("coordinator", "Master orchestrator", "hierarchical-coordinator")
Task("researcher", "Team dynamics analysis", "researcher")
Task("analyst", "Finance analysis", "finance-analyst")
Task("risk", "Risk assessment", "risk-manager")
Task("operations", "Operations analysis", "operations-consultant")
Task("franchise", "Franchise model evaluation", "franchise-consultant")
Task("strategic", "Strategic synthesis", "strategic-advisor")
```

**Пример успешного использования:**
- **Проект:** DepylBrazil Franchise Consilium (Feb 6, 2026)
- **Агенты:** 6 специализированных (Team Researcher, Finance Analyst, Risk Manager, Operations Consultant, Franchise Consultant, Strategic Advisor)
- **Результаты:**
  - Team Dynamics: 1,847-word comprehensive assessment
  - Financial Model: 60-90K BRL payment structure with milestone triggers
  - Risk Assessment: 7 identified risks with mitigation strategies
  - Timeline Analysis: 45d optimistic, 60-75d realistic projections
  - Final Recommendation: CONDITIONAL GO with specific conditions
- **Время выполнения:** 6 агентов параллельно через Task tool
- **Качество:** Полный consilium отчёт с consensus recommendation

**Что РАБОТАЕТ в текущем подходе:**
- ✅ Hierarchical topology (coordinator + 6 specialized workers)
- ✅ Каждый агент выполняется через отдельный Task call
- ✅ Результаты синтезируются coordinator агентом
- ✅ Graceful fallback when swarm MCP unavailable
- ✅ Parallel execution через Task tool (не последовательное)

**Что НУЖНО доработать:**

### 1. Автоматическая инициализация swarm
**Текущее поведение:**
```markdown
Step 04 (Consilium) → User input → Manual swarm init (если попросят)
```

**Желаемое поведение:**
```markdown
Step 04 (Consilium) → Auto-detect consilium mode → Auto swarm init → Parallel agents
```

**Триггеры для auto-swarm:**
- Consilium mode: Deep (6 hats) → ALWAYS use swarm
- Consilium mode: Lite (3 perspectives) → Consider swarm if complex
- TRIZ analysis requested → Use swarm for contradiction resolution
- Advanced Elicitation selected → Use swarm for SCAMPER/Five Whys

### 2. Нативная интеграция swarm MCP
**Проблема:**
```javascript
mcp__claude-flow__swarm_init({ topology: "hierarchical" })
// Error: No such tool available: mcp__claude-flow__swarm_init
```

**Нужно:**
- Проверка доступности swarm MCP tool
- Graceful fallback к Task-based approach (как сейчас)
- Logging когда используется fallback vs native swarm

### 3. Параллельное выполнение агентов
**Текущий метод:** Task tool с 6+ параллельными вызовами ✅ РАБОТАЕТ
**Улучшение:** Если swarm MCP доступен, использовать его для true parallel coordination

### 4. Интеграция в Step 04 workflow
**Добавить в `step-04-consilium.md` после Step 2 (Mode Determination):**
```markdown
### 2.5. Initialize Swarm Coordination (Automatic)

**If Deep Mode:**
```javascript
// Try native swarm first
try {
  mcp__claude-flow__swarm_init({
    topology: "hierarchical",
    maxAgents: 8,
    strategy: "specialized"
  })
} catch {
  // Fallback to Task-based coordination (proven to work)
  // Launch 6+ specialized agents via Task tool
}
```

**If Lite Mode:**
- Skip swarm for simple 3-perspective analysis
- Use direct prompting for 1-2 specialists
```

---

### 🔧 Техническая спецификация

**Swarm Configuration для Consilium:**
```yaml
topology: hierarchical  # Queen (coordinator) + specialized workers
maxAgents: 6-8         # Consilium needs 4-8 specialists
strategy: specialized  # Clear roles (Finance, Risk, Operations, etc.)
consensus: raft        # Leader-based for authoritative synthesis
memory_backend: hybrid # Share findings via memory
```

**Agent Roles для Deep Consilium:**
| Agent Type | Hat | Responsibility |
|-----------|-----|----------------|
| hierarchical-coordinator | 🔵 Blue | Process control, synthesis |
| researcher | ⚪ White | Facts, data, team assessment |
| finance-analyst | ⚪ White | Financial model, ROI |
| risk-manager | ⚫ Black | Risks, mitigation strategies |
| operations-consultant | 🔵 Blue | Timeline, feasibility |
| franchise-consultant | 🟡 Yellow | Business model, scalability |
| strategic-advisor | 🟢 Green | Creative solutions, recommendation |

**Memory Coordination:**
```bash
# Each agent stores findings in shared memory
npx claude-flow@v3alpha memory store \
  --namespace "consilium:session-{id}" \
  --key "{agent-type}:findings" \
  --content "{analysis}"

# Coordinator synthesizes from memory
npx claude-flow@v3alpha memory search -q "consilium session {id}"
```

---

### 📊 Приоритет и внедрение

**Приоритет:** 🔴 **CRITICAL** (влияет на качество consilium и скорость анализа)

**Обоснование:**
- Consilium — ключевой шаг для принятия решений
- Параллельное выполнение экономит 50-70% времени (6 агентов параллельно vs последовательно)
- Swarm coordination улучшает качество синтеза (shared memory, consensus protocols)

**Фазы внедрения:**

**Phase 1 (✅ СДЕЛАНО):**
- Task-based hierarchical coordination
- 6+ specialized agents для Deep consilium
- Coordinator для synthesis
- Proven to work (DepylBrazil Feb 6, 2026)

**Phase 2 (В ПРОЦЕССЕ):**
- Документирование текущего подхода ✅ (этот файл)
- Best practices для Task-based swarm

**Phase 3 (НУЖНО СДЕЛАТЬ):**
- Автоматическая инициализация в Step 04
- Интеграция swarm MCP (когда доступен)
- Fallback logic (try swarm → fallback to Task)
- Timing: 2-4 недели

**Phase 4 (БУДУЩЕЕ):**
- Adaptive topology (mesh для brainstorming, hierarchical для analysis)
- Load balancing между агентами
- Performance metrics (consilium completion time, quality scores)
- Timing: 1-2 месяца

---

### 🎯 Success Criteria

**Критерии успеха Phase 3:**
- [ ] Step 04 автоматически инициализирует swarm для Deep mode
- [ ] Graceful fallback к Task-based approach если swarm unavailable
- [ ] 6+ specialized agents запускаются параллельно
- [ ] Consilium completion time <10 минут (vs 20-30 мин sequential)
- [ ] Quality score ≥8.5/10 (specialist consensus)

**Критерии успеха Phase 4:**
- [ ] Adaptive topology selection (зависит от задачи)
- [ ] Load balancing (распределение работы между агентами)
- [ ] Performance dashboard (время, качество, cost)
- [ ] A/B testing: swarm vs single-agent consilium (quality comparison)

---

### 📝 Notes

**Дата добавления:** 2026-02-06
**Автор:** Nikita (user request)
**Контекст:** После successful consilium для DepylBrazil с 6 агентами через Task tool
**Reference:** DepylBrazil Consilium (Feb 6, 2026) - proof of concept для Task-based swarm coordination

---

## Доработка: Session State Management (Управление состоянием между сессиями)

**Что:** Стандартизировать процесс сохранения и восстановления состояния проекта между сессиями

**Проблема:**
- Сейчас в workflow.md есть только базовые правила: "Update frontmatter" и "DUAL STORAGE"
- НЕТ чётких инструкций КАК документировать "где остановились"
- НЕТ Resume Point секции (как продолжить в следующей сессии)
- НЕТ правил для Pause/Wait states (когда ждём внешнего ответа)
- НЕТ стандартных memory keys для session state

**Последствия:**
- AI ассистент делает это интуитивно (inconsistent approach)
- Пользователь может забыть контекст между сессиями
- Нет стандартного "точки входа" для возобновления работы

---

### Что УЖЕ РАБОТАЕТ (✅ Proof of Concept)

**Пример:** idea-007 (DepylBrazil Franchise, Feb 6, 2026)

**Реализованные элементы:**

1. **Frontmatter расширен:**
```yaml
status: PAUSED
pauseReason: Waiting for team decision (Galina/Violetta/Maria)
pauseDate: 2026-02-06
decisionDeadline: 2026-02-13
completionPercentage: 25
stepsCompleted:
  - step-04-consilium (6 specialists, CONDITIONAL GO)
```

2. **Resume Point секция добавлена:**
```markdown
## 🔄 RESUME POINT (For Next Session)
**Last Updated:** 2026-02-06
**Current Status:** ⏸️ PAUSED

### Where We Are:
- Life OS Progress: steps completed
- Current Score: 8.0/10
- Key Findings: consilium summary
- Waiting For: team decision
- Outputs Created: 3 files (05, 06, 07)
- Todo List: req-25 (8 tasks)

### How to Resume:
- IF response by Feb 13 → Step 05 (Scoring)
- IF no response → Archive, focus Katana
- Command to Resume: "Продолжаем Life OS для idea-007"
```

3. **Global Memory сохранение:**
```bash
Key: shared-knowledge:life-os:idea-007:session-2026-02-06
Value: Session state summary (566 bytes, vectorized)
```

4. **Task Manager интеграция:**
- Request ID: req-25
- 8 tasks с дедлайнами
- Critical task: task-146 (decision by Feb 13)

**Результат:** Полная воспроизводимость сессии при возобновлении

---

### Что НУЖНО доработать

#### 1. Добавить в workflow.md секцию "Session State Management"

**Место:** После "Step Processing Rules" (строка 82+)

**Содержание:**
```markdown
### Session State Management (Between Sessions)

**When pausing work on project:**

Triggers:
- User says "wait", "pause", "ждём"
- External dependency (waiting for response, approval, etc.)
- Session ending with incomplete work

Actions:
1. **Update Frontmatter:**
   - status: PAUSED (if waiting) or IN_PROGRESS (if can continue)
   - pauseReason: "[why paused]"
   - pauseDate: YYYY-MM-DD
   - decisionDeadline: YYYY-MM-DD (if applicable)
   - completionPercentage: XX%
   - stepsCompleted: [list of completed steps]

2. **Add Resume Point Section (at end of idea file):**
   ```markdown
   ## 🔄 RESUME POINT (For Next Session)
   **Last Updated:** [date]
   **Current Status:** [PAUSED/WAITING/IN_PROGRESS]

   ### Where We Are:
   - Life OS Progress: [steps completed + current step]
   - Current Score: [X.X/10] (if scored)
   - Key Findings: [1-2 sentence summary]
   - Waiting For: [what blocks progress] (if applicable)
   - Outputs Created: [list key files in idea-XXX-outputs/]
   - Todo List: [task manager request ID if exists]

   ### How to Resume:
   - IF [condition A] → [action X]
   - IF [condition B] → [action Y]
   - Command to Resume: "[exact phrase user should say]"
   - Quick Context Reload: [pointer to key files]
   ```

3. **Save to Global Memory:**
   ```bash
   npx claude-flow@v3alpha memory store \
     --namespace "shared-knowledge" \
     --key "life-os:[idea-id]:session-[YYYY-MM-DD]" \
     --value "[compact session summary: status, score, next action, deadline]"
   ```

4. **Task Manager (if tasks active):**
   - Document request ID in Resume Point
   - Mark critical deadlines
   - Note next task to execute

**When resuming:**
1. User invokes: "Продолжаем [idea-XXX]" or "Продолжаем Life OS для [project]"
2. AI reads Resume Point section
3. AI loads from global memory (optional, for quick summary)
4. AI asks: "Any updates since [pauseDate]?"
5. AI continues from documented state
```

---

#### 2. Стандартизировать Memory Keys

**Текущий подход:** Ad-hoc naming

**Предлагаемый стандарт:**
```
Global Memory Keys:
- life-os:[idea-id]:session-[date] → Session state snapshot
- life-os:[idea-id]:step-[XX]-complete → Step completion record
- life-os:[idea-id]:score-history → Scoring changes over time
- life-os:[idea-id]:decision-[date] → Major decisions logged

Examples:
- life-os:idea-007:session-2026-02-06
- life-os:idea-007:step-04-consilium-complete
- life-os:idea-007:score-history
- life-os:idea-007:decision-2026-02-06-conditional-go
```

---

#### 3. Обновить Step Files (Templates)

**Каждый step-XX-*.md должен включать:**

```markdown
## STEP COMPLETION PROTOCOL

When this step is complete:

1. Update idea frontmatter:
   - Add step to stepsCompleted: [step-XX-name]
   - Increment completionPercentage: +YY%
   - Update updated: [date]

2. Save step output:
   - File: idea-XXX-outputs/[step-number]-[description]-[date].md
   - Content: [step-specific output format]

3. Global memory:
   - Key: life-os:[idea-id]:step-XX-complete
   - Value: "[brief summary + key outputs]"

4. If pausing after this step:
   - Add Resume Point section (see workflow.md Session State Management)
   - Document next step to execute
```

---

### 📊 Приоритет и внедрение

**Приоритет:** 🟡 **MEDIUM-HIGH** (улучшает UX, но система работает и без этого)

**Обоснование:**
- Session continuity критична для Deep Track (2-4 часа работы, может быть split на несколько дней)
- Текущий ad-hoc подход работает, но inconsistent
- Стандартизация упростит onboarding и уменьшит cognitive load

**Фазы внедрения:**

**Phase 1 (✅ СДЕЛАНО - Proof of Concept):**
- idea-007 как пример (Resume Point, global memory, task manager)
- Доказано: подход работает и воспроизводим

**Phase 2 (НУЖНО СДЕЛАТЬ - 2-4 часа):**
- Добавить "Session State Management" секцию в workflow.md
- Стандартизировать memory keys naming convention
- Создать Resume Point template (в templates/)

**Phase 3 (БУДУЩЕЕ - 4-8 часов):**
- Обновить все step-XX-*.md с "STEP COMPLETION PROTOCOL"
- Создать automation script (auto-generate Resume Point)
- Интеграция с Task Manager (auto-link tasks to Resume Point)

**Phase 4 (ОПЦИОНАЛЬНО - 8-12 часов):**
- Dashboard для паузированных проектов
- Auto-reminder если deadline approaching (decision deadlines)
- Cross-project Resume Points view

---

### 🎯 Success Criteria

**Phase 2 Complete когда:**
- [ ] workflow.md содержит Session State Management секцию
- [ ] Memory keys стандартизированы (naming convention documented)
- [ ] Resume Point template создан в templates/
- [ ] 2-3 проекта используют новый подход (validation)

**Phase 3 Complete когда:**
- [ ] Все 15+ step files обновлены с completion protocol
- [ ] Automation script работает (optional)
- [ ] Task Manager auto-links работают

**User Experience Success:**
- User может возобновить работу через N месяцев без потери контекста
- AI ассистент instantly понимает где остановились
- Zero ambiguity про next action

---

### 📝 Notes

**Дата добавления:** 2026-02-06
**Автор:** Nikita (user request: "прописано ли в workflow фиксировать этап?")
**Контекст:** После создания Resume Point для idea-007 (DepylBrazil, PAUSED waiting for team)
**Reference:** idea-007-business-beauty-franchise.md (строки 151-199) - working example

**Связанные улучшения:**
- Improvement #2 (Goals Discovery) - требует session state если goals discovery занимает >1 сессию
- Improvement #3 (PDCA цикл) - weekly/monthly reviews требуют session continuity

---

## Другие потенциальные доработки

(Для будущего сбора)
