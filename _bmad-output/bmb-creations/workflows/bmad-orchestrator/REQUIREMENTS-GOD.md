# REQUIREMENTS GOD — Все хотелки для bmad-orchestrator

**Статус:** Активный документ для сверки  
**Дата создания:** 2026-02-26  
**Назначение:** Полный список требований к workflow

---

## 🎯 ГЛАВНАЯ ЦЕЛЬ

Создать **bmad-orchestrator** — meta-workflow, который:
- Динамически подбирает и вызывает BMAD workflow из библиотеки
- Работает с большими файлами без переполнения контекста
- Поддерживает параллельное выполнение с конфликт-детекцией
- Синхронизирует документы по каскаду

---

## 📋 ПОЛНЫЙ СПИСОК ТРЕБОВАНИЙ

### 1. ИНТЕГРАЦИЯ ВСЕХ BMAD WORKFLOW

**ВСЕ workflow из .clinerules/workflows/ должны быть доступны для вызова:**

#### BMM Workflows (Software Development)
- [ ] `bmad-bmm-generate-project-context` — Создать project-context.md
- [ ] `bmad-bmm-create-prd` — Создать PRD
- [ ] `bmad-bmm-create-ux-design` — UX Design
- [ ] `bmad-bmm-create-architecture` — Архитектура
- [ ] `bmad-bmm-create-epics-and-stories` — Эпики и стории
- [ ] `bmad-bmm-create-story` — Отдельная история
- [ ] `bmad-bmm-sprint-planning` — Планирование спринта
- [ ] `bmad-bmm-sprint-status` — Статус спринта
- [ ] `bmad-bmm-check-implementation-readiness` — Проверка готовности
- [ ] `bmad-bmm-dev-story` — Разработка истории
- [ ] `bmad-bmm-code-review` — Code review
- [ ] `bmad-bmm-retrospective` — Ретроспектива
- [ ] `bmad-bmm-qa-generate-e2e-tests` — E2E тесты
- [ ] `bmad-bmm-document-project` — Документирование проекта
- [ ] `bmad-bmm-quick-spec` — Быстрый spec
- [ ] `bmad-bmm-quick-dev` — Быстрая разработка
- [ ] `bmad-bmm-market-research` — Маркетинговое исследование
- [ ] `bmad-bmm-technical-research` — Техническое исследование
- [ ] `bmad-bmm-domain-research` — Доменное исследование
- [ ] `bmad-bmm-create-product-brief` — Product brief
- [ ] `bmad-bmm-edit-prd` — Редактирование PRD
- [ ] `bmad-bmm-validate-prd` — Валидация PRD
- [ ] `bmad-bmm-correct-course` — Корректировка курса

#### BMB Workflows (Module Building)
- [ ] `bmad-bmb-create-agent` — Создать агента
- [ ] `bmad-bmb-create-module` — Создать модуль
- [ ] `bmad-bmb-create-workflow` — Создать workflow
- [ ] `bmad-bmb-create-module-brief` — Module brief
- [ ] `bmad-bmb-edit-agent` — Редактировать агента
- [ ] `bmad-bmb-edit-module` — Редактировать модуль
- [ ] `bmad-bmb-edit-workflow` — Редактировать workflow
- [ ] `bmad-bmb-rework-workflow` — Переработать workflow
- [ ] `bmad-bmb-validate-agent` — Валидировать агента
- [ ] `bmad-bmb-validate-module` — Валидировать модуль
- [ ] `bmad-bmb-validate-workflow` — Валидировать workflow
- [ ] `bmad-bmb-validate-max-parallel-workflow` — MAX-PARALLEL валидация

#### CIS Workflows (Creative/Innovation)
- [ ] `bmad-cis-design-thinking` — Design thinking
- [ ] `bmad-cis-innovation-strategy` — Инновационная стратегия
- [ ] `bmad-cis-problem-solving` — Problem solving
- [ ] `bmad-cis-storytelling` — Storytelling
- [ ] `bmad-brainstorming` — Brainstorming

#### Review Workflows
- [ ] `bmad-review-adversarial-general` — Adversarial review
- [ ] `bmad-editorial-review-prose` — Editorial review (prose)
- [ ] `bmad-editorial-review-structure` — Editorial review (structure)

#### Utility Workflows
- [ ] `bmad-index-docs` — Индексация документов
- [ ] `bmad-shard-doc` — Разбиение документа
- [ ] `bmad-party-mode` — Party mode
- [ ] `bmad-help` — Help

#### TEA Workflows (Testing)
- [ ] `bmad-tea-teach-me-testing` — Обучение тестированию
- [ ] `bmad-tea-testarch-atdd` — ATDD
- [ ] `bmad-tea-testarch-automate` — Автоматизация тестов
- [ ] `bmad-tea-testarch-ci` — CI pipeline
- [ ] `bmad-tea-testarch-framework` — Test framework
- [ ] `bmad-tea-testarch-nfr` — NFR assessment
- [ ] `bmad-tea-testarch-test-design` — Test design
- [ ] `bmad-tea-testarch-test-review` — Test review
- [ ] `bmad-tea-testarch-trace` — Traceability matrix

---

### 1a. ИНТЕЛЛЕКТУАЛЬНОЕ ИСПОЛЬЗОВАНИЕ BMAD CSV МАНИФЕСТОВ

**Использовать встроенные CSV списки BMAD для data-driven orchestration:**

#### Основные CSV манифесты (decision-support database):
- [x] `workflow-manifest.csv` — 52+ workflow (для выбора workflow в step-02)
- [x] `agent-manifest.csv` — агенты с персонами (для routing к агентам)
- [x] `task-manifest.csv` — задачи (для декомпозиции больших эпиков)
- [x] `tool-manifest.csv` — доступные инструменты
- [x] `bmad-help.csv` — справка по командам

#### Специализированные методы CSV:
- [ ] `advanced-elicitation/methods.csv` — 50+ методов (collaboration, technical, creative, etc.)
- [ ] `problem-solving/solving-methods.csv` — 31+ методов решения (diagnosis, analysis, synthesis)
- [ ] `design-thinking/design-methods.csv` — 31+ методов дизайна (empathize, ideate, prototype)
- [ ] `innovation-strategy/innovation-frameworks.csv` — 31+ фреймворков (disruption, business model)
- [ ] `storytelling/story-types.csv` — 26+ типов историй
- [ ] `brainstorming/brain-methods.csv` — 62+ техник (collaborative, creative, structured)

#### Архитектура data-driven selection:
- [x] Создан `/data/manifest-integration-guide.md` — паттерны интеграции CSV
- [x] Step-02 использует `workflow-manifest.csv` для выбора workflow
- [x] Step-02 может использовать `methods.csv` для Advanced Elicitation
- [ ] Step-03 использует `tool-manifest.csv` для выбора инструментов
- [ ] Все CSV загружаются и анализируются через semantic matching

---

### 1b. ИНТЕЛЛЕКТУАЛЬНЫЙ ПОИСК BEST PRACTICES ЧЕРЕЗ MCP

**Использовать встроенные MCP инструменты для поиска и изучения best practices:**

#### MCP Search Sources (Priority Order):
- [x] **CLI Claude Flow Memory** — `npx claude-flow@v3alpha memory search -q "{query}"` (локальная база знаний)
- [x] **OctoCode MCP** — `githubSearchCode`, `githubViewRepoStructure`, `githubGetFileContent` (реальные примеры кода)
- [x] **Brave Search MCP** — `brave_web_search`, `brave_local_search` (текущая информация, паттерны)
- [x] **Web Search MCP** — `tavily_search`, `tavily_extract`, `tavily_crawl` (комплексный поиск, документация)
- [x] **Context7 MCP** — `resolve-library-id`, `query-docs` (документация библиотек)

#### Архитектура MCP Search:

**Step-02 (Workflow Selection):**
- [ ] При выборе workflow → поискать примеры в OctoCode (real patterns)
- [ ] При выборе инструмента → поискать best practices через Brave/Web Search
- [ ] Результаты интегрировать в confidence score для workflow selection

**Step-03 (Orchestration Planning):**
- [ ] При выборе parallel zones → поискать conflict detection patterns (OctoCode)
- [ ] При выборе tools → поискать latest documentation (Context7)
- [ ] При выборе strategy → поискать comparative analysis (Brave Search)

**Step-04 (Execution Loop):**
- [ ] During execution → search for error recovery patterns (OctoCode + Memory)
- [ ] When encountering failures → lookup solution patterns in Memory/Web
- [ ] Post-execution → store learnings in Claude Flow Memory

**Step-05 (Cascade Sync):**
- [ ] При синхронизации → поискать merge conflict resolution patterns
- [ ] Сравнить с best practices (Web Search + Memory)

**Step-06 (Validation):**
- [ ] При валидации → поискать quality assessment patterns
- [ ] Сравнить результаты с industry standards (Context7 docs)

#### Процесс CONSILIUM через MCP (из mcp_search_system_prompt_xml.md):

```
1. RETRIEVE фаза:
   - Поиск в Memory (локальные знания)
   - OctoCode search (реальные примеры)
   - Web Search (актуальная информация)
   - Результаты ранжируются по релевантности

2. JUDGE фаза:
   - LLM-as-judge оценивает каждый результат
   - Присваивает confidence score
   - Фильтрует по threshold (>0.7)

3. CONSILIUM фаза:
   - Конвокация 2-4 экспертных perspectives
   - Обсуждение через Party Mode
   - Ранжирование опций по pros/cons

4. DECISION фаза:
   - Выбор best option или ask-user
   - Если confidence LOW → Advanced Elicitation
   - Если confidence HIGH → auto-proceed
```

#### Confidence Levels (для auto-decision):

| Level | Criteria | Action |
|-------|----------|--------|
| HIGH (≥0.8) | 2+ strong sources, consistent findings | Auto-proceed, log decision |
| MEDIUM (0.5-0.8) | 1 strong + 1 weak source, partial alignment | Present options, ask user |
| LOW (<0.5) | Conflicting sources or weak evidence | Advanced Elicitation, deep analysis |

#### MCP Tools Configuration:

**OctoCode Integration:**
- `githubSearchCode` — поиск примеров по keywords (pattern matching)
- `githubViewRepoStructure` — изучение архитектуры проектов
- `githubGetFileContent` — анализ реальных реализаций
- Use case: "Как реализуют parallel execution в TypeScript?"

**Brave Search Integration:**
- `brave_web_search` — текущие best practices и тренды
- `brave_local_search` — локальные решения и примеры
- Use case: "Current best practices for conflict-free parallel execution 2026"

**Web Search (Tavily) Integration:**
- `tavily_search` — быстрый поиск по миру
- `tavily_extract` — извлечение контента из документации
- `tavily_crawl` — глубокий анализ сайтов и документов
- Use case: "Latest TypeScript patterns for orchestration frameworks"

**Context7 Integration:**
- `resolve-library-id` — поиск информации о библиотеке
- `query-docs` — запросить документацию по конкретной теме
- Use case: "Node.js cluster management best practices"

#### Хранение найденных Best Practices:

```bash
# После каждого MCP поиска сохранять в Claude Flow Memory:
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge:best-practices" \
  --key "pattern:{domain}:{pattern-name}" \
  --content "{description + confidence + sources + timestamp}"

# Пример:
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge:best-practices" \
  --key "pattern:parallel-execution:conflict-detection" \
  --content "Read-Write conflict detection using dependency graph..."
```

#### Quality Gates для MCP Results:

- [ ] Минимум 2 независимых источника для уверенности (confidence HIGH)
- [ ] Проверка актуальности (не старше 6 месяцев для web results)
- [ ] Соответствие проекта требованиям (фильтр по версиям, языкам)
- [ ] Consensus проверка (если разные источники contradicting → Advanced Elicitation)

---

### 2. РАБОТА С БОЛЬШИМИ ФАЙЛАМИ

- [x] **Range Read** — чтение только необходимых диапазонов
- [x] **Append-Only Building** — постепенное создание документов
- [x] **Context Management** — контроль использования контекста
- [ ] **Chunked Processing** — обработка файлов по частям (если >4000 строк)
- [ ] **Smart Caching** — кэширование уже прочитанных секций

---

### 3. ПАРАЛЛЕЛЬНОЕ ВЫПОЛНЕНИЕ

- [x] **Conflict Detection** — детекция конфликтов (read-after-write, write-after-write)
- [x] **Parallel Zones** — разметка безопасных параллельных зон
- [x] **Sequential Dependencies** — определение последовательных зависимостей
- [x] **Multi-runtime** — поддержка Cline / Claude Code / Codex
- [ ] **Dynamic Load Balancing** — динамическое распределение нагрузки
- [ ] **Auto-scaling** — автоматическое масштабирование subagents

---

### 4. ПРОМЕЖУТОЧНЫЕ ФАЙЛЫ (для возобновления и валидации)

#### На каких этапах создавать промежуточные файлы:

**После step-01-discovery:**
- [ ] `orchestration-session-{timestamp}.md` — Сессия с метаданными
- [ ] `inputs-discovered.json` — Обнаруженные входные данные

**После step-02-workflow-selection:**
- [ ] `workflow-selection.md` — Выбранные workflow с обоснованием
- [ ] `workflow-dependencies.graph` — Граф зависимостей

**После step-03-orchestration-plan:**
- [ ] `orchestration-plan.md` — План с Parallel/Sequential зонами
- [ ] `conflict-analysis.md` — Анализ конфликтов
- [ ] `execution-timeline.md` — Временная шкала выполнения

**Во время step-04-execution-loop (после каждой фазы):**
- [ ] `checkpoint-phase-{N}.md` — Чекпоинт после каждой фазы
- [ ] `execution-log.md` — Лог выполнения
- [ ] `subagent-results/` — Результаты subagents

**После step-05-cascade-sync:**
- [ ] `sync-report.md` — Отчёт о синхронизации
- [ ] `changes-propagated.json` — Список изменений

**После step-06-validation:**
- [ ] `traceability-matrix.md` — Матрица трассировки
- [ ] `validation-report.md` — Отчёт о валидации
- [ ] `final-artifacts.json` — Итоговые артефакты

---

### 5. ВАЛИДАЦИЯ РЕЗУЛЬТАТОВ

- [x] **Consistency Check** — проверка консистентности документов
- [x] **Traceability Matrix** — генерация матрицы трассировки
- [ ] **Cross-reference Validation** — проверка перекрёстных ссылок
- [ ] **Metadata Validation** — валидация frontmatter
- [ ] **Content Quality Gates** — пороги качества контента
- [ ] **Automated Diff Checks** — автоматическая проверка изменений

---

### 6. ADVANCED ELICITATION И PARTY MODE

- [x] **На каждом шаге** — [A] Advanced Elicitation | [P] Party Mode | [C] Continue
- [ ] **Conditional Triggering** — автоматический запуск AE при сложных решениях
- [ ] **Post-execution Analysis** — анализ результатов через AE
- [ ] **Party Mode for Conflicts** — обсуждение конфликтов через Party Mode

---

### 7. РЕЖИМЫ РАБОТЫ

- [x] **Режим A: BMAD Cascade** — Brief → PRD → UX → Arch → Epics → Stories → Tests → Code → Matrix
- [x] **Режим B: Universal Multi-Source** — Файл 1,2,3...N → Файл N
- [ ] **Режим C: Selective Sync** — выборочная синхронизация
- [ ] **Режим D: Batch Processing** — пакетная обработка множества файлов
- [ ] **Режим E: YOLO Mode** — автоматическое выполнение всех шагов с best practices

#### YOLO Mode (You Only Orchestrate Once) — Автоматический режим с best practices:

**Принцип:** Все шаги выполняются автоматически согласно best practices, выбор методов обсуждается через Party Mode и Advanced Elicitation.

**Поведение:**
- [x] Step-01: Автоматический анализ задачи (no menus, auto-proceed)
- [ ] Step-02: Автоматический выбор workflow (без меню, best match из CSV)
- [ ] Step-03: Автоматическое построение плана (без user confirmation, default strategy)
- [ ] Step-04: Автоматическое выполнение (without checkpoints, continuous execution)
- [ ] Step-05: Автоматическая синхронизация (auto-apply all changes)
- [ ] Step-06: Автоматическая валидация (no user approval required)

**Параметры настройки YOLO Mode:**
- [ ] `yolo_level: [1-5]` — уровень автоматизации (1=max control, 5=max auto)
- [ ] `approval_method: [party-mode | advanced-elicitation | none]` — способ обсуждения выбора
- [ ] `fallback_on_ambiguity: [ask-user | pick-best | abort]` — как действовать при неоднозначности
- [ ] `parallel_execution: [true | false]` — распределять ли на parallel subagents
- [ ] `save_checkpoints: [always | on-error | never]` — сохранять ли промежуточные checkpoints

**Процесс Party Mode / Advanced Elicitation в YOLO Mode:**
- Step-02 workflow selection обсуждается через [P] Party Mode (multi-agent discussion)
- Параллельные конфликты обсуждаются через [P] Party Mode
- Best practices выбираются через [A] Advanced Elicitation методы
- Пользователь видит итоговый план ПЕРЕД выполнением (но без меню, auto-accept)

**Примеры YOLO Mode использования:**
- `orchestrate --yolo 5 --method party-mode` — полностью auto, обсуждение через PM
- `orchestrate --yolo 3 --method advanced-elicitation` — частичная auto, глубокий анализ
- `orchestrate --yolo 1 --method none` — минимальная auto, ask-user на каждом шаге

---

### 8. ИНТЕГРАЦИЯ С MCP

- [ ] **GitHub MCP** — работа с PR, issues, repo
- [ ] **File System MCP** — расширенная работа с файлами
- [ ] **Web Search MCP** — поиск актуальной информации
- [ ] **Context7 MCP** — доступ к документации библиотек
- [ ] **Sequential Thinking MCP** — для сложных аналитических задач

---

### 9. БЕЗОПАСНОСТЬ И ОТКАЗОУСТОЙЧИВОСТЬ

- [ ] **Backup Before Writes** — резервное копирование перед изменениями
- [ ] **Rollback Capability** — возможность отката изменений
- [ ] **Transaction Support** — атомарные операции
- [ ] **Graceful Degradation** — graceful degradation при ошибках subagent
- [ ] **Retry Logic** — повторные попытки при failures

---

### 10. UI/UX УЛУЧШЕНИЯ

- [ ] **Progress Visualization** — визуализация прогресса (ASCII/Unicode)
- [ ] **ETA Estimation** — оценка времени выполнения
- [ ] **Real-time Status Updates** — обновления статуса в реальном времени
- [ ] **Interactive Debugging** — интерактивная отладка
- [ ] **Notification System** — уведомления о завершении

---

### 11. АНАЛИТИКА И МЕТРИКИ

- [ ] **Execution Metrics** — метрики выполнения (время, токены, стоимость)
- [ ] **Performance Dashboard** — дашборд производительности
- [ ] **Historical Comparison** — сравнение с предыдущими запусками
- [ ] **Optimization Suggestions** — предложения по оптимизации

---

## 📊 СТАТУС ВЫПОЛНЕНИЯ

**Создано базовых компонентов:** 8/11 шагов (73%)
- [x] workflow-bmad-orchestrator.md
- [x] step-01-discovery.md
- [x] step-02-workflow-selection.md
- [x] step-03-orchestration-plan.md
- [x] step-04-execution-loop.md
- [x] step-05-cascade-sync.md
- [x] step-06-validation.md
- [x] step-01b-continue.md
- [ ] Интеграция всех workflow
- [ ] Промежуточные файлы
- [ ] Расширенная валидация

**Новые требования добавлены (2026-02-26):**
- [x] Интеграция встроенных BMAD CSV манифестов (section 1a)
- [x] MCP Search Integration для learning best practices (section 1b) — OctoCode + Brave/Web Search + Context7 + Claude Flow Memory
- [x] YOLO Mode для автоматического выполнения (section 7, режим E)

**Всего требований:** ~130 пунктов (+60 новых)
**Выполнено:** ~40 пунктов (31%)
**Приоритеты на реализацию (Priority 1):**
- [1] CSV манифесты + MCP Search в step-02 (data-driven workflow selection)
- [2] YOLO Mode + Party Mode/Advanced Elicitation в step-01/02/03
- [3] Confidence scoring + CONSILIUM protocol для MCP results
**В процессе:**
- Интеграция CSV манифестов + MCP Search для intelligent workflow selection
- Реализация YOLO Mode с configurable automation levels
- Архитектура CONSILIUM protocol для best practices discovery

---

## 🚨 INCOMPLETE PHASE 2 ARCHITECTURE WORK (2026-02-26)

**Context:** Architecture Workflow Steps 1-3 completed, but Step 4+ requires user decision.

### 5 Critical Phase 2 Architectural Decisions (PENDING USER SELECTION):

**1️⃣ Rocket Bucket Capital Allocator (FR72-FR74)**
- Status: ❌ PENDING DECISION
- Issue: Как переработать Capital Manager для новой модели (≤10% NAV, 60% per rocket)?
- Substeps: State storage, rebalance triggers, 20/80 transfer model
- Blocks: Risk Manager updates, Executor sizing

**2️⃣ Adaptive Scaling State Machine (FR76) — GREEN/YELLOW/RED/BLACK**
- Status: ❌ PENDING DECISION
- Issue: Где реализовать state transitions? (Risk Manager или отдельный модуль?)
- Substeps: Trigger computation (core DD, rocket losses, correlation), state-driven sizing
- Blocks: Executor layer, signal selection

**3️⃣ Parameter Profiles System (≤70 active params per profile)**
- Status: ❌ PENDING DECISION
- Issue: Как маппировать profile → active params? (YAML, code, database?)
- Substeps: Conditional search space, Optuna define-by-run, profile selection UI
- Blocks: Optimizer configuration, parameter taxonomy

**4️⃣ Multi-Timeframe Parallel Execution (6 independent caches)**
- Status: ❌ PENDING DECISION
- Issue: Как организовать 6 parallel Optuna studies? (один процесс или workers?)
- Substeps: 1m/5m/15m/1h/4h/1d studies, result aggregation, independent reporting
- Blocks: Executor parallelization, result merging

**5️⃣ Wave 4 Parameter Taxonomy (115 total parameters)**
- Status: ❌ PENDING DECISION
- Issue: Как организовать параметры по группам? (Signal, DFF, Risk, Money, Executive)
- Substeps: DFF flat structure (6 types), per-role validation, conditional activation
- Blocks: Optimizer search space, configuration schema

### Files That Need Phase 2 Alignment:

**Phase 1 → Phase 2 Required Changes:**
- [ ] `katana-v-04-architecture-2026-01-19.md` — adapt existing architecture for Phase 2 decisions
- [ ] `katana-v-03-ux-design-specification-2026-01-19.md` — update UI for rocket bucket, state machine, profiles
- [ ] `katana-v-05-epics.md` — add Phase 2 epics for 5 architectural decisions

**Alignment Strategy (не реализовано, нужна стратегия):**
- Decide architecture first (Step 4: select [1], [2], [3], [4], or [5])
- Create Phase 2 architecture doc with decisions
- Update epics to reflect new architecture
- Update UX/UI specs for new components (Rocket Bucket panel, State Machine dashboard, Profile manager)

**Next Action:** AWAITING USER INPUT on architectural decision priority

---

---

## 🎯 СЛЕДУЮЩИЕ ШАГИ

**ПРИОРИТЕТ 1: CSV Integration + YOLO Mode (NEW)**
1. **Интегрировать BMAD CSV манифесты** — использовать встроенные CSV для intelligent routing
   - Реализовать manifest-integration-guide.md паттерны в step-02
   - Добавить поддержку methods.csv, frameworks.csv, brainstorm-methods.csv
   - Реализовать semantic matching для выбора лучших методов

2. **Реализовать YOLO Mode** — автоматическое выполнение с best practices
   - Step-01: Auto-analyze task (no menus)
   - Step-02: Auto-select workflows (CSV-based, best match)
   - Step-03: Auto-create plan (no user approval)
   - Step-04: Auto-execute (parallel where safe)
   - Step-05: Auto-sync (no review options)
   - Step-06: Auto-validate (no approval needed)
   - Добавить параметры настройки (yolo_level, approval_method, etc.)

**ПРИОРИТЕТ 2: Workflow Integration**
3. **Интегрировать вызов всех BMAD workflow** — добавить в step-02 полный список
4. **Создать систему промежуточных файлов** — для каждого шага определить артефакты
5. **Добавить валидационные проверки** — cross-reference, metadata, quality gates

**ПРИОРИТЕТ 3: Advanced Features**
6. **Реализовать MCP интеграции** — GitHub, Web Search, Context7
7. **Улучшить отказоустойчивость** — backup, rollback, retry

---

**Последнее обновление:** 2026-02-26  
**Владелец:** God  
**Статус:** Активная разработка
