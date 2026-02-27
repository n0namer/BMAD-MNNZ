# 📋 Life OS - Daily TODO Generator

Система автоматической генерации ежедневных задач из недельных целей с интеграцией календаря и метриками.

## 🚀 Быстрый старт

### 1. Установка зависимостей

```bash
# Python 3.8+
pip install pyyaml
```

### 2. Первичная настройка

```bash
cd automation
bash generate-daily-todo.sh --setup
```

Эта команда:
- ✅ Проверит зависимости
- ✅ Создаст конфигурационные файлы
- ✅ Создаст пример goals.yaml
- ✅ Создаст выходные директории

### 3. Настройка целей

Отредактируйте `../data/goals.yaml`:

```yaml
week_focus:
  week_number: 6
  theme: "Ваша тема недели"

goals:
  - id: "project.feature"
    title: "Название проекта"
    priority: high
    estimated_hours: 20
    deadline: "2026-02-14"
    tasks:
      - title: "Задача 1"
        estimated_hours: 4
      - title: "Задача 2"
        estimated_hours: 6
```

### 4. Генерация TODO

```bash
# Стандартная генерация (текущая неделя)
bash generate-daily-todo.sh

# Конкретная дата
bash generate-daily-todo.sh --date 2026-02-10

# С экспортом в календарь
bash generate-daily-todo.sh --export-ics

# С метриками
bash generate-daily-todo.sh --export-metrics
```

## 📂 Структура проекта

```
automation/
├── generate-daily-todo.md      # Документация системы
├── generate-daily-todo.py      # Python генератор
├── generate-daily-todo.sh      # Bash обёртка
├── todo-config.yaml            # Конфигурация
├── calendar-sync.md            # 🆕 Документация Calendar Sync
├── calendar_sync.py            # 🆕 Двусторонняя синхронизация
├── calendar-sync-config.template.yaml  # 🆕 Конфиг шаблон
├── requirements.txt            # 🆕 Python зависимости
├── scripts/
│   ├── setup_google_oauth.py   # 🆕 Настройка Google OAuth
│   └── setup_outlook_oauth.py  # 🆕 Настройка Outlook OAuth
└── README.md                   # Этот файл

data/
└── goals.yaml                  # Недельные цели (ИСТОЧНИК)

output/
└── todos/
    ├── 2026-02-10-mon.md      # Ежедневные TODO
    ├── 2026-02-11-tue.md
    ├── ...
    ├── ics/                    # Календарные файлы
    └── metrics/                # Метрики выполнения
```

## ⚙️ Конфигурация

### Основные параметры (todo-config.yaml)

```yaml
calendar:
  work_hours_per_day: 8         # Рабочих часов в день
  buffer_percentage: 15          # Резервное время

prioritization:
  high_threshold_hours: 3        # Задачи >3ч → High

task_distribution:
  strategy: "balanced"           # balanced | frontload | backload
  max_tasks_per_day: 6          # Максимум задач в день
```

### Календарная интеграция

```yaml
calendar_integration:
  type: "ical"                   # google | outlook | ical
  timezone: "Europe/Moscow"
  add_reminders: true
  reminder_minutes: [15, 60]
```

## 📖 Формат TODO файлов

Каждый ежедневный TODO содержит:

```markdown
# TODO - 2026-02-10 (Понедельник)

## 🎯 Week Focus: Тема недели

### ⚡ High Priority (Must Do)
- [ ] Задача 1 (4ч) → [09:00-13:00] (goal: project.id)

### 🟡 Medium Priority (Should Do)
- [ ] Задача 2 (2ч) → [14:00-16:00]

### 🔵 Low Priority (Nice to Have)
- [ ] Задача 3 (1ч) → [Buffer time]

## 📅 Calendar Blocks
09:00-13:00: [Project] Задача 1

## 📊 Daily Metrics
- Запланировано часов: 8
- Focus time блоки: 3
- Приоритетных задач: 2
```

## 🔧 Использование

### Базовые команды

```bash
# Помощь
bash generate-daily-todo.sh --help

# Валидация goals.yaml
bash generate-daily-todo.sh --validate

# Генерация на конкретную неделю
bash generate-daily-todo.sh --week 2026-W07
```

### Python API

```python
from generate_daily_todo import TodoGenerator

# Инициализация
gen = TodoGenerator("todo-config.yaml")

# Загрузка целей
gen.load_goals("../data/goals.yaml")

# Генерация
gen.generate(
    start_date=datetime(2026, 2, 10),
    export_ics=True,
    export_metrics_flag=True
)
```

## 📊 Метрики

После генерации доступны метрики:

```json
{
  "week_number": 6,
  "total_tasks": 18,
  "total_hours": 49,
  "priority_distribution": {
    "high": 8,
    "medium": 6,
    "low": 4
  },
  "daily_breakdown": [...]
}
```

## 🔗 Интеграция с календарём

### 🆕 Calendar Sync (Two-Way Sync) - РЕКОМЕНДУЕТСЯ

**Автоматическая двусторонняя синхронизация с Google Calendar и Outlook!**

```bash
# Полная документация
cat calendar-sync.md

# Быстрый старт
pip install -r requirements.txt
python scripts/setup_google_oauth.py  # Настройка Google
python calendar_sync.py --setup google
python calendar_sync.py --sync --dry-run
python calendar_sync.py --sync

# Автосинхронизация каждые 15 минут
python calendar_sync.py --daemon
```

**Что умеет Calendar Sync:**
- ✅ TODO → Calendar (автоматическое создание событий)
- ✅ Calendar → TODO (синхронизация изменений обратно)
- ✅ Цветовое кодирование по доменам (finance=зелёный, business=синий)
- ✅ Умное разрешение конфликтов
- ✅ Связь событий с целями через goal_id
- ✅ Недельные отчёты

**Читать:** [calendar-sync.md](calendar-sync.md)

### Google Calendar (Manual Import)

```bash
# 1. Генерация с экспортом
bash generate-daily-todo.sh --export-ics

# 2. Импорт .ics файлов
# → output/todos/ics/*.ics
# → Google Calendar → Settings → Import
```

### Outlook (Manual Copy)

```bash
# Копировать Calendar Blocks секцию
# → Вставить в Outlook Calendar
```

## 🔄 Автоматизация

### Cron Job (Linux/macOS)

```bash
# Каждое воскресенье в 18:00
0 18 * * 0 cd /path/to/automation && bash generate-daily-todo.sh
```

### Task Scheduler (Windows)

```powershell
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 6PM
$action = New-ScheduledTaskAction -Execute "bash.exe" -Argument "D:\path\to\generate-daily-todo.sh"
Register-ScheduledTask -TaskName "LifeOS-TodoGen" -Trigger $trigger -Action $action
```

## 🐛 Troubleshooting

### Проблема: Пустые TODO файлы

```bash
# Проверить goals.yaml
bash generate-daily-todo.sh --validate

# Проверить структуру
python3 -c "import yaml; print(yaml.safe_load(open('../data/goals.yaml')))"
```

### Проблема: PyYAML не установлен

```bash
pip install pyyaml
# или
pip3 install pyyaml
```

### Проблема: Скрипт не запускается

```bash
# Сделать исполняемым
chmod +x generate-daily-todo.sh
chmod +x generate-daily-todo.py

# Проверить путь к Python
which python3
```

## 📚 Дополнительная документация

- [TODO Generator - Полная документация](generate-daily-todo.md)
- [Calendar Sync - Полная документация](calendar-sync.md) 🆕
- [Схема goals.yaml](../data/goals-schema.md)
- [Календарная интеграция](../docs/calendar-integration.md)

## 🆕 Версии

**v1.0.0** (2026-02-08)
- ✅ Базовая генерация TODO из goals.yaml
- ✅ Распределение задач по дням
- ✅ Календарная интеграция (.ics)
- ✅ Метрики и отчётность
- ✅ Приоритизация задач
- ✅ Русский язык UI

## 📞 Поддержка

- Документация: `generate-daily-todo.md`
- Примеры: `../examples/`
- Issues: GitHub Issues

---

## 🆕 Template Usage Tracking

**Purpose:** Track when templates are used, filled, and completed. Identify popular templates and deprecation candidates.

### Quick Start

```bash
# Install tracking system
bash install-template-tracking.sh

# View usage statistics
node template-tracker.js --stats

# List unused templates
node template-tracker.js --list-unused

# Manual tracking (if needed)
node template-tracker.js --template lean-canvas --action fill
```

### Files

| File | Purpose |
|------|---------|
| `template-tracker.js` | Core tracking module with CLI |
| `hooks-template-integration.js` | Integration with claude-flow hooks |
| `install-template-tracking.sh` | Installation script |

### Documentation

See [`../docs/template-usage-tracking.md`](../docs/template-usage-tracking.md) for complete documentation.

### How It Works

```
User edits template → post-edit hook fires → auto-detection →
tracking event stored in global memory → queryable via CLI
```

**Storage:** `~/.claude-flow/agentdb-global/` (shared across all projects)

**Namespace:** `shared-knowledge:template-usage:*`

**Performance:** <50ms overhead, non-blocking

---

**Made with ❤️ by Life OS Team**
