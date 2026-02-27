# 🚀 Life OS TODO Generator - Установка и Настройка

## Краткое описание

Система каскадной генерации ежедневных TODO из недельных целей:

```
Weekly Goals (goals.yaml)
    ↓
Daily TODO Files (Mon-Fri)
    ↓
Calendar Events (.ics)
    ↓
Metrics & Reports (JSON)
```

## 📦 Что включено

### Основные компоненты
1. **generate-daily-todo.py** - Основной генератор (Python)
2. **generate-daily-todo.sh** - Bash обёртка с удобным CLI
3. **todo-config.yaml** - Конфигурационный файл
4. **goals.yaml** - Шаблон недельных целей

### Дополнительно
- README.md - Руководство пользователя
- EXAMPLE-*.md - Пример сгенерированного TODO
- generate-daily-todo.md - Полная техническая документация

## ⚡ Быстрая установка (3 минуты)

### Шаг 1: Проверка зависимостей

```bash
# Проверить Python (требуется 3.8+)
python3 --version

# Должно быть: Python 3.8.x или выше
```

### Шаг 2: Установка PyYAML

```bash
pip install pyyaml
```

### Шаг 3: Первичная настройка

```bash
cd automation
bash generate-daily-todo.sh --setup
```

Скрипт автоматически:
- ✅ Проверит все зависимости
- ✅ Создаст todo-config.yaml (если отсутствует)
- ✅ Создаст пример goals.yaml
- ✅ Создаст выходные директории

### Шаг 4: Первый запуск

```bash
# Валидация конфигурации
bash generate-daily-todo.sh --validate

# Генерация TODO на текущую неделю
bash generate-daily-todo.sh
```

Результат в `../output/todos/`:
- `2026-02-10-mon.md`
- `2026-02-11-tue.md`
- `2026-02-12-wed.md`
- `2026-02-13-thu.md`
- `2026-02-14-fri.md`

## 🎯 Настройка goals.yaml

### Минимальная конфигурация

```yaml
week_focus:
  week_number: 6
  theme: "Ваша главная тема недели"

goals:
  - id: "project.task"
    title: "Название проекта"
    priority: high              # high | medium | low
    estimated_hours: 10
    deadline: "2026-02-14"
    tasks:
      - title: "Задача 1"
        estimated_hours: 4
      - title: "Задача 2"
        estimated_hours: 6
```

### Полная структура с опциями

```yaml
week_focus:
  week_number: 6
  dates: "2026-02-10 - 2026-02-14"
  theme: "Завершение проекта X"
  key_results:
    - "KR 1: Релиз версии 3.0"
    - "KR 2: Документация 100%"

goals:
  - id: "dev.project.feature"
    title: "Разработка Feature X"
    description: "Детальное описание"
    priority: high
    estimated_hours: 20
    deadline: "2026-02-14"

    tags:
      - development
      - critical

    dependencies:
      - another.goal.id  # Какие цели должны быть сделаны первыми

    tasks:
      - title: "Задача 1"
        description: "Подробности задачи"
        estimated_hours: 4
        tags: [coding, backend]
        complexity: high      # high | medium | low

      - title: "Задача 2"
        estimated_hours: 6
        tags: [testing]
        complexity: medium
```

## ⚙️ Настройка todo-config.yaml

### Ключевые параметры

```yaml
calendar:
  work_hours_per_day: 8           # Рабочих часов в день
  buffer_percentage: 15           # Резервное время (%)
  deep_work_block_duration: 4     # Длина deep work блока

task_distribution:
  strategy: "balanced"            # balanced | frontload | backload
  max_tasks_per_day: 6            # Максимум задач в день
  max_high_priority_per_day: 3    # Максимум High priority в день

output:
  language: "ru"                  # Язык (ru | en)
  include_metrics: true           # Включить метрики
  include_calendar_blocks: true   # Включить блоки календаря
```

### Добавление регулярных встреч

```yaml
calendar:
  recurring_blocks:
    - name: "Daily Standup"
      duration: 0.5  # часы
      days: [mon, tue, wed, thu, fri]
      time: "09:00"
      priority: high

    - name: "Weekly Planning"
      duration: 1.0
      days: [mon]
      time: "10:00"
      priority: high
```

Эти блоки вычитаются из доступного времени при распределении задач.

## 📅 Использование

### Основные команды

```bash
# Справка
bash generate-daily-todo.sh --help

# Валидация goals.yaml
bash generate-daily-todo.sh --validate

# Генерация на текущую неделю
bash generate-daily-todo.sh

# Генерация на конкретную дату
bash generate-daily-todo.sh --date 2026-02-10

# Генерация на конкретную неделю
bash generate-daily-todo.sh --week 2026-W07

# С экспортом в .ics календарь
bash generate-daily-todo.sh --export-ics

# С экспортом метрик
bash generate-daily-todo.sh --export-metrics
```

### Python API (для продвинутых)

```python
from generate_daily_todo import TodoGenerator
from datetime import datetime

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

# Кастомная приоритизация
def custom_priority(task, goal):
    if 'critical' in task.get('tags', []):
        return 'high'
    return 'medium'

gen.calculate_priority = custom_priority
```

## 📊 Вывод и метрики

### Структура TODO файла

```markdown
# TODO - 2026-02-10 (Понедельник)

## 🎯 Week Focus: [Тема недели]

### ⚡ High Priority (Must Do)
- [ ] Задача (4ч) → [09:00-13:00] (goal: project.id)

### 🟡 Medium Priority (Should Do)
- [ ] Задача (2ч) → [14:00-16:00]

### 🔵 Low Priority (Nice to Have)
- [ ] Задача (1ч) → [Buffer time]

## 📅 Calendar Blocks
09:00-13:00: [Project] Задача

## 📊 Daily Metrics
- Запланировано часов: 8
- Focus time блоки: 3
- Deep work сессии: 2
- Приоритетных задач: 2
```

### Метрики (JSON)

Файл: `output/metrics/week-06-metrics.json`

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
  "daily_breakdown": [
    {
      "date": "2026-02-10",
      "weekday": "Понедельник",
      "tasks": 4,
      "hours": 10,
      "high": 2,
      "medium": 1,
      "low": 1
    }
  ]
}
```

## 🔗 Интеграция с календарём

### Экспорт в Google Calendar

```bash
# 1. Генерация .ics файлов
bash generate-daily-todo.sh --export-ics

# 2. Файлы создаются в output/todos/ics/
ls ../output/todos/ics/

# 3. Импорт в Google Calendar
# Google Calendar → Settings → Import → Select file
```

### Импорт в Outlook

```bash
# 1. Генерация
bash generate-daily-todo.sh --export-ics

# 2. Outlook → File → Open → Import → iCalendar (.ics)
# 3. Выбрать файл из output/todos/ics/
```

### Автоматическая синхронизация

См. `calendar-sync.md` для двусторонней синхронизации (TODO ↔ Calendar).

## 🔄 Автоматизация

### Cron (Linux/macOS)

```bash
# Редактировать crontab
crontab -e

# Добавить строку (каждое воскресенье в 18:00)
0 18 * * 0 cd /path/to/automation && bash generate-daily-todo.sh

# Проверить установку
crontab -l
```

### Task Scheduler (Windows)

```powershell
# PowerShell (от администратора)
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 6PM
$action = New-ScheduledTaskAction -Execute "bash.exe" -Argument "D:\path\to\generate-daily-todo.sh"
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries

Register-ScheduledTask -TaskName "LifeOS-TodoGen" `
  -Trigger $trigger `
  -Action $action `
  -Settings $settings `
  -Description "Weekly TODO generation"
```

## 🛠️ Troubleshooting

### Проблема: PyYAML не установлен

```bash
# Симптом
ModuleNotFoundError: No module named 'yaml'

# Решение
pip install pyyaml
# или
pip3 install pyyaml
```

### Проблема: goals.yaml не найден

```bash
# Симптом
FileNotFoundError: [Errno 2] No such file or directory: '../data/goals.yaml'

# Решение 1: Создать через setup
bash generate-daily-todo.sh --setup

# Решение 2: Скопировать шаблон
cp goals.yaml.example ../data/goals.yaml
```

### Проблема: Пустые TODO файлы

```bash
# Валидация goals.yaml
bash generate-daily-todo.sh --validate

# Проверка структуры
python3 -c "import yaml; print(yaml.safe_load(open('../data/goals.yaml')))"

# Возможные причины:
# - goals.yaml пуст
# - Неверная структура YAML
# - Нет задач (tasks) в целях
```

### Проблема: Скрипт не запускается

```bash
# Сделать исполняемым
chmod +x generate-daily-todo.sh
chmod +x generate-daily-todo.py

# Проверить путь к Python
which python3

# Проверить права на директории
ls -la ../output/todos
```

### Проблема: Неравномерное распределение задач

```yaml
# Увеличить доступное время в конфиге
calendar:
  work_hours_per_day: 10  # Вместо 8

# ИЛИ уменьшить estimated_hours в goals.yaml
```

## 📚 Дополнительная документация

- **README.md** - Руководство пользователя
- **generate-daily-todo.md** - Полная техническая документация
- **calendar-sync.md** - Двусторонняя синхронизация с календарями
- **goals-schema.md** - Схема goals.yaml
- **EXAMPLE-*.md** - Примеры сгенерированных TODO

## 🎓 Примеры использования

### Пример 1: Стандартная рабочая неделя

```yaml
week_focus:
  week_number: 6
  theme: "Фокус на Feature Development"

goals:
  - id: "dev.feature.auth"
    title: "Разработка аутентификации"
    priority: high
    estimated_hours: 20
    deadline: "2026-02-14"
    tasks:
      - title: "JWT токены"
        estimated_hours: 6
      - title: "OAuth2 интеграция"
        estimated_hours: 8
      - title: "Тесты"
        estimated_hours: 6
```

### Пример 2: С learning tasks

```yaml
goals:
  - id: "learning.ai"
    title: "Изучение AI agents"
    priority: low
    estimated_hours: 5
    tasks:
      - title: "Прочитать статьи"
        estimated_hours: 2
      - title: "Эксперименты"
        estimated_hours: 3
```

### Пример 3: С зависимостями

```yaml
goals:
  - id: "design.architecture"
    title: "Проектирование"
    priority: high
    estimated_hours: 8
    tasks: [...]

  - id: "dev.implementation"
    title: "Разработка"
    priority: high
    estimated_hours: 20
    dependencies:
      - design.architecture  # Сначала проектирование
    tasks: [...]
```

## 🚀 Roadmap

**v1.1.0** (планируется):
- AI-powered приоритизация через Claude API
- Web UI для визуализации
- Автоматический перенос незавершённых задач
- Интеграция с Notion/Todoist
- Mobile app (PWA)

## 📞 Поддержка

- Документация: См. файлы в директории `automation/`
- Примеры: `../examples/`
- Issues: GitHub Issues
- Email: support@lifeos.example

---

**Готово! Теперь у вас есть полностью настроенная система каскадной генерации TODO.**

**Следующие шаги:**
1. Отредактировать `goals.yaml` под свои цели
2. Запустить `bash generate-daily-todo.sh`
3. Просмотреть сгенерированные TODO в `output/todos/`
4. Настроить автоматизацию (cron/Task Scheduler)
5. Интегрировать с календарём

**Happy planning! 📋✨**
