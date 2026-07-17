# BMAD Orchestrator

**Meta-workflow для динамической оркестрации BMAD workflow с параллельным выполнением, детекцией конфликтов и поддержкой больших файлов.**

---

## 🎯 Что делает этот workflow

BMAD Orchestrator — это meta-workflow, который:

1. **Анализирует** вашу задачу и выбирает подходящие BMAD workflow из библиотеки
2. **Планирует** оркестрацию с определением параллельных зон и детекцией конфликтов
3. **Выполняет** workflow параллельно (через subagents) или последовательно
4. **СинХРОНИЗИРУЕТ** связанные документы в каскаде
5. **Валидирует** результаты и генерирует матрицу трассировки

---

## 🚀 Быстрый старт

### Запуск с нуля

1. Откройте `workflow-bmad-orchestrator.md`
2. Выберите **[F]rom scratch**
3. Следуйте инструкциям step-by-step

### Продолжение сессии

1. Откройте `workflow-bmad-orchestrator.md`
2. Выберите **[C]ontinue**
3. Orchestrator восстановит состояние и продолжит с последнего checkpoint

---

## 📋 Структура workflow

### Phase 1: ANALYZE (Анализ)
- **step-01-discovery** — Понять задачу и собрать файлы
- **step-02-workflow-selection** — Выбрать подходящие BMAD workflow

### Phase 2: PLAN (Планирование)
- **step-03-orchestration-plan** — Построить граф зависимостей, детектировать конфликты, разметить параллельные зоны

### Phase 3: EXECUTE (Исполнение)
- **step-04-execution-loop** — Выполнить workflow (параллельно через subagents)
- **step-05-cascade-sync** — Синхронизировать связанные документы
- **step-06-validation** — Проверить целостность и сгенерировать матрицу трассировки

### Continuation (Продолжение)
- **step-01b-continue** — Возобновить сессию с последнего checkpoint

---

## ✨ Ключевые возможности

### 🎭 Два режима работы

**Режим A: BMAD Cascade**
```
Brief → PRD → UX → Arch → Epics → Stories → Tests → Code → Traceability Matrix
```

**Режим B: Universal Multi-Source**
```
Файл 1, 2, 3...N → Файл N (консолидированный с best practices)
```

### ⚡ Параллельное выполнение
- **Conflict Detection** — автоматическое определение конфликтов (read-after-write, write-after-write)
- **Parallel Zones** — безопасное параллельное выполнение через subagents
- **Multi-runtime** — поддержка Cline, Claude Code, Codex

### 📄 Large File Safe
- **Range Read** — чтение только необходимых диапазонов файла
- **Append-Only Building** — постепенное создание документов
- **Context Management** — контроль использования контекста

### 🧠 Advanced Elicitation + Party Mode
- Доступны на **каждом шаге** через меню [A/P/C]
- 50+ методов Advanced Elicitation
- Party Mode для обсуждения с multiple agents

### 🔄 Continuable
- Сохранение прогресса после каждого шага
- Возможность прерваться и продолжить позже
- Автоматическое восстановление состояния

---

## 🛠️ Использование

### Пример 1: Создать PRD и связанные документы

```
Пользователь: "У меня есть brief.md, нужно создать PRD, архитектуру и эпики"

Orchestrator:
1. Анализирует brief.md
2. Предлагает: bmad-bmm-create-prd, bmad-bmm-create-architecture, bmad-bmm-create-epics-and-stories
3. Строит план: PRD → Arch → Epics (sequential, т.к. зависимости)
4. Выполняет workflow
5. СинХРОНИЗИРУЕТ связанные документы
6. Генерирует матрицу трассировки
```

### Пример 2: Консолидировать несколько источников

```
Пользователь: "У меня файлы research-1.md, research-2.md, research-3.md — нужен единый consolidated.md"

Orchestrator:
1. Анализирует все источники
2. Предлагает режим Universal Multi-Source
3. Извлекает best practices из каждого файла
4. Создаёт consolidated.md
5. Применяет Advanced Elicitation для качества
```

### Пример 3: Параллельная работа

```
Пользователь: "Нужно создать UX и Architecture параллельно (они не зависят друг от друга)"

Orchestrator:
1. Анализирует задачу
2. Определяет: UX и Arch независимы → Parallel Zone
3. Запускает оба workflow одновременно через subagents
4. Собирает результаты
5. СинХРОНИЗИРУЕТ с PRD
```

---

## 📁 Файлы workflow

```
bmad-orchestrator/
├── workflow-bmad-orchestrator.md    # Основной workflow файл
├── workflow-plan-bmad-orchestrator.md  # Plan документ сессии
├── README.md                         # Этот файл
├── steps-c/                          # Create mode steps
│   ├── step-01-discovery.md
│   ├── step-02-workflow-selection.md
│   ├── step-03-orchestration-plan.md
│   ├── step-04-execution-loop.md
│   ├── step-05-cascade-sync.md
│   ├── step-06-validation.md
│   └── step-01b-continue.md
├── steps-e/                          # Edit mode steps (placeholder)
└── steps-v/                          # Validate mode steps (placeholder)
```

---

## 🔧 Требования

- BMAD framework установлен
- Доступ к workflow библиотеке (`.clinerules/workflows/`)
- Для параллельного выполнения: поддержка subagents (Cline/Claude/Codex)

---

## 📊 Статус workflow

- **Версия:** 1.0
- **Статус:** Готов к использованию
- **Классификация:** Tri-Modal (Create + Edit + Validate)
- **Continuable:** Да
- **Document-Producing:** Да

---

## 🤝 Участие в развитии

Для предложений по улучшению используйте Advanced Elicitation или Party Mode на любом шаге workflow.

---

**Создано:** 2026-02-26
**Автор:** BMAD Orchestrator Creation Workflow
