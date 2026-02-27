# Автоматическая Генерация Daily TODO из Weekly Goals

## 📋 Обзор

Система автоматической генерации ежедневных TODO списков на основе недельных целей из `goals.yaml`. Обеспечивает каскадное планирование: Недельные Цели → Ежедневные Задачи → Календарные Блоки.

## 🎯 Функциональность

### Основные возможности
1. **Чтение weekly focus** из `goals.yaml`
2. **Генерация TODO.md** файлов (Пн-Пт)
3. **Распределение задач** по неделе (time-boxing)
4. **Календарная интеграция** (маркеры для импорта в Google Calendar/Outlook)
5. **Приоритизация** (High/Med/Low) на основе alignment с целями
6. **Трекинг** через goal_id для метрик и отчетности

### Дополнительные функции
- Автоматический расчёт доступного времени
- Учёт регулярных встреч и блоков
- Балансировка нагрузки по дням
- Генерация резервного времени (buffer)
- Поддержка русского языка для UX

## 📂 Структура

```
life-os/
├── automation/
│   ├── generate-daily-todo.md         # Эта документация
│   ├── generate-daily-todo.py         # Python-скрипт генерации
│   ├── generate-daily-todo.sh         # Bash-обёртка
│   └── todo-config.yaml               # Конфигурация системы
├── data/
│   └── goals.yaml                     # Недельные цели (источник)
└── output/
    └── todos/
        ├── 2026-02-10-mon.md
        ├── 2026-02-11-tue.md
        └── ...
```

## 🔧 Установка

### Требования
- Python 3.8+ (для `.py` скрипта)
- Bash 4.0+ (для `.sh` обёртки)
- PyYAML (`pip install pyyaml`)

### Быстрый старт

```bash
# 1. Установить зависимости
pip install pyyaml

# 2. Настроить конфигурацию
cd automation
cp todo-config.yaml.example todo-config.yaml
# Отредактировать под свои нужды

# 3. Создать goals.yaml (если отсутствует)
cd ../data
cat > goals.yaml << 'EOF'
week_focus:
  week_number: 6
  dates: "2026-02-10 - 2026-02-14"
  theme: "Завершение Life OS v3.0 + Подготовка демо"

goals:
  - id: "dev.lifeos.v3"
    title: "Life OS v3.0 Final Release"
    priority: high
    estimated_hours: 20
    deadline: "2026-02-14"
    tasks:
      - "Завершить Deep Plan автоматизацию"
      - "Интегрировать TRIZ modes"
      - "Написать deployment guide"
      - "Провести end-to-end тестирование"

  - id: "demo.lifeos.presentation"
    title: "Подготовить демонстрацию системы"
    priority: high
    estimated_hours: 8
    deadline: "2026-02-14"
    tasks:
      - "Создать сценарий презентации"
      - "Подготовить примеры использования"
      - "Записать демо-видео"
EOF

# 4. Запустить генерацию
bash generate-daily-todo.sh
```

## 📖 Формат Daily TODO

Каждый ежедневный TODO файл следует единообразному шаблону:

```markdown
# TODO - 2026-02-10 (Понедельник)

## 🎯 Week Focus: Завершение Life OS v3.0 + Подготовка демо

---

### ⚡ High Priority (Must Do)
- [ ] Завершить Deep Plan автоматизацию (4ч) → [09:00-13:00] (goal: dev.lifeos.v3)
- [ ] Создать сценарий презентации (2ч) → [14:00-16:00] (goal: demo.lifeos.presentation)

### 🟡 Medium Priority (Should Do)
- [ ] Code review для TRIZ integration (1ч) → [16:00-17:00] (goal: dev.lifeos.v3)

### 🔵 Low Priority (Nice to Have)
- [ ] Обновить документацию API (1ч) → [Buffer time]

---

## 📅 Calendar Blocks

**09:00-13:00**: [Life OS v3.0] Завершить Deep Plan автоматизацию (goal: dev.lifeos.v3)
**14:00-16:00**: [Demo Prep] Создать сценарий презентации (goal: demo.lifeos.presentation)
**16:00-17:00**: [Life OS v3.0] Code review для TRIZ integration (goal: dev.lifeos.v3)

---

## 📊 Daily Metrics

- **Запланировано часов**: 8
- **Focus time блоки**: 3
- **Deep work сессии**: 2 × 4ч
- **Приоритетных задач**: 2
- **Alignment с целями**: 100%

---

## 🔗 Quick Links

- [Week Goals](../data/goals.yaml)
- [Previous Day](2026-02-07-fri.md)
- [Next Day](2026-02-11-tue.md)
- [Weekly Review](../reviews/week-06.md)

---

**Сгенерировано**: 2026-02-08 10:30
**Скрипт**: automation/generate-daily-todo.py v1.0
```

## ⚙️ Конфигурация

Файл `todo-config.yaml` управляет поведением генератора:

```yaml
# Календарные настройки
calendar:
  work_days: [mon, tue, wed, thu, fri]
  work_hours_per_day: 8
  deep_work_block_duration: 4  # часы
  buffer_percentage: 15  # % резервного времени

  # Регулярные блоки (вычитаются из доступного времени)
  recurring_blocks:
    - name: "Daily Standup"
      duration: 0.5
      days: [mon, tue, wed, thu, fri]
      time: "09:00"

    - name: "Email Processing"
      duration: 0.5
      days: [mon, wed, fri]
      time: "08:30"

# Приоритизация
prioritization:
  high_threshold_hours: 3  # Задачи >3ч → High
  deadline_proximity_days: 3  # Deadline <3 дней → High

  # Весы для расчёта приоритета
  weights:
    goal_priority: 0.4
    deadline: 0.3
    estimated_hours: 0.2
    dependencies: 0.1

# Распределение задач
task_distribution:
  strategy: "balanced"  # balanced | frontload | backload
  max_tasks_per_day: 6
  max_high_priority_per_day: 3
  min_buffer_hours: 1

# Форматирование вывода
output:
  language: "ru"
  date_format: "%Y-%m-%d"
  time_format: "%H:%M"
  include_metrics: true
  include_calendar_blocks: true
  include_quick_links: true

# Пути
paths:
  goals_file: "../data/goals.yaml"
  output_dir: "../output/todos"
  templates_dir: "../templates"
```

## 🐍 Python Скрипт

См. файл `generate-daily-todo.py` (создаётся далее).

## 🔗 Интеграция с Календарём

### Google Calendar Import

```bash
# Экспорт в .ics формат
python generate-daily-todo.py --export-ics

# Файлы .ics создаются в output/todos/ics/
# Импортировать в Google Calendar через UI или API
```

### Outlook Integration

```bash
# Генерация .msg файлов для Outlook
python generate-daily-todo.py --export-outlook

# Или копировать Calendar Blocks секцию в Outlook
```

### CLI команды

```bash
# Генерация на текущую неделю
bash generate-daily-todo.sh

# Генерация на конкретную неделю
bash generate-daily-todo.sh --week 2026-W07

# Только один день
python generate-daily-todo.py --date 2026-02-10

# С экспортом в календарь
bash generate-daily-todo.sh --export-ics
```

## 📊 Метрики и Отчётность

Система автоматически собирает метрики:

- **Task Completion Rate** по goal_id
- **Time Tracking** (план vs факт)
- **Priority Accuracy** (соответствие приоритетов)
- **Load Balancing** (распределение по дням)

Экспорт метрик:

```bash
python generate-daily-todo.py --export-metrics
# → output/metrics/week-06-metrics.json
```

## 🔄 Автоматизация

### Cron Job (Linux/macOS)

```bash
# Генерация каждое воскресенье в 18:00
0 18 * * 0 cd /path/to/life-os/automation && bash generate-daily-todo.sh
```

### Task Scheduler (Windows)

```powershell
# PowerShell скрипт для Task Scheduler
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 6PM
$action = New-ScheduledTaskAction -Execute "bash.exe" -Argument "D:\path\to\generate-daily-todo.sh"
Register-ScheduledTask -TaskName "LifeOS-TodoGen" -Trigger $trigger -Action $action
```

## 🛠️ Кастомизация

### Добавление новых приоритетных правил

Редактировать `generate-daily-todo.py`:

```python
def calculate_priority(task, goal):
    score = 0

    # Существующие правила
    score += goal['priority_weight'] * 0.4
    score += deadline_score(task['deadline']) * 0.3

    # Новое правило: теги важности
    if 'critical' in task.get('tags', []):
        score += 20

    return classify_priority(score)
```

### Изменение формата TODO

Редактировать шаблон в `templates/daily-todo.md.j2` (Jinja2).

## 📝 Примеры Использования

### Сценарий 1: Стандартная неделя

```bash
# Воскресенье вечером
cd automation
bash generate-daily-todo.sh

# Результат: 5 файлов TODO (Пн-Пт)
# Задачи равномерно распределены
# Приоритеты основаны на goals.yaml
```

### Сценарий 2: Изменение планов mid-week

```bash
# Среда, изменились приоритеты
# 1. Обновить goals.yaml
vim ../data/goals.yaml

# 2. Регенерировать оставшиеся дни
python generate-daily-todo.py --from-date 2026-02-12

# Результат: Чт-Пт перегенерированы
```

### Сценарий 3: Экспорт для команды

```bash
# Генерация с экспортом в календарь
bash generate-daily-todo.sh --export-ics --share

# Результат:
# - TODO.md файлы
# - .ics календари
# - Shared link для команды
```

## 🐛 Troubleshooting

### Проблема: Пустые TODO файлы

**Причина**: goals.yaml некорректен или пуст

**Решение**:
```bash
# Валидация goals.yaml
python -c "import yaml; yaml.safe_load(open('../data/goals.yaml'))"

# Проверка структуры
python generate-daily-todo.py --validate-goals
```

### Проблема: Неравномерное распределение

**Причина**: Слишком много задач на неделю

**Решение**:
```yaml
# Увеличить work_hours_per_day в config
calendar:
  work_hours_per_day: 10  # Вместо 8

# Или уменьшить estimated_hours в goals.yaml
```

### Проблема: Неверный формат календарных блоков

**Причина**: Некорректная конфигурация времени

**Решение**:
```yaml
# Проверить time_format в config
output:
  time_format: "%H:%M"  # 24-часовой формат
```

## 📚 Связанные Документы

- [goals.yaml Schema](../data/goals-schema.md)
- [Life OS Automation Guide](../docs/automation-guide.md)
- [Calendar Integration Manual](../docs/calendar-integration.md)
- [Metrics Dashboard](../dashboards/productivity-metrics.md)

## 🔄 Версионирование

**v1.0.0** (2026-02-08)
- Первая версия с базовым функционалом
- Поддержка Python и Bash
- Календарная интеграция
- Русский язык UX

**Roadmap v1.1.0**:
- AI-powered приоритизация через Claude
- Интеграция с TRIZ для решения блокеров
- Автоматический перенос незавершённых задач
- Web UI для визуализации

---

**Автор**: Life OS Automation System
**Лицензия**: MIT
**Поддержка**: [GitHub Issues](https://github.com/your-org/life-os/issues)
