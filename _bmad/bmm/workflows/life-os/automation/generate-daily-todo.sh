#!/usr/bin/env bash
# Life OS - Daily TODO Generator (Bash Wrapper)
# Обёртка для Python скрипта с удобным CLI

set -euo pipefail

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Конфигурация
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="${SCRIPT_DIR}/generate-daily-todo.py"
CONFIG_FILE="${SCRIPT_DIR}/todo-config.yaml"
GOALS_FILE="${SCRIPT_DIR}/../data/goals.yaml"

# Функции
print_header() {
    echo -e "${BLUE}╔═══════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║  Life OS - Daily TODO Generator v1.0     ║${NC}"
    echo -e "${BLUE}╚═══════════════════════════════════════════╝${NC}"
    echo ""
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

check_dependencies() {
    # Проверка Python
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 не установлен"
        exit 1
    fi

    # Проверка PyYAML
    if ! python3 -c "import yaml" 2>/dev/null; then
        print_warning "PyYAML не установлен. Установка..."
        pip install pyyaml || {
            print_error "Не удалось установить PyYAML"
            exit 1
        }
    fi

    print_success "Все зависимости установлены"
}

check_goals_file() {
    if [[ ! -f "$GOALS_FILE" ]]; then
        print_warning "goals.yaml не найден: $GOALS_FILE"
        echo ""
        read -p "Создать пример goals.yaml? (y/n): " -n 1 -r
        echo ""

        if [[ $REPLY =~ ^[Yy]$ ]]; then
            create_example_goals
        else
            print_error "goals.yaml необходим для работы"
            exit 1
        fi
    fi
}

create_example_goals() {
    mkdir -p "$(dirname "$GOALS_FILE")"

    cat > "$GOALS_FILE" << 'EOF'
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
      - title: "Завершить Deep Plan автоматизацию"
        estimated_hours: 4
      - title: "Интегрировать TRIZ modes"
        estimated_hours: 6
      - title: "Написать deployment guide"
        estimated_hours: 4
      - title: "Провести end-to-end тестирование"
        estimated_hours: 6

  - id: "demo.lifeos.presentation"
    title: "Подготовить демонстрацию системы"
    priority: high
    estimated_hours: 8
    deadline: "2026-02-14"
    tasks:
      - title: "Создать сценарий презентации"
        estimated_hours: 2
      - title: "Подготовить примеры использования"
        estimated_hours: 3
      - title: "Записать демо-видео"
        estimated_hours: 3

  - id: "docs.update"
    title: "Обновление документации"
    priority: medium
    estimated_hours: 4
    deadline: "2026-02-14"
    tasks:
      - title: "Обновить README"
        estimated_hours: 1
      - title: "Написать API документацию"
        estimated_hours: 2
      - title: "Создать FAQ"
        estimated_hours: 1
EOF

    print_success "Создан пример goals.yaml: $GOALS_FILE"
}

create_example_config() {
    cat > "$CONFIG_FILE" << 'EOF'
# Life OS TODO Generator Configuration

calendar:
  work_days: [mon, tue, wed, thu, fri]
  work_hours_per_day: 8
  deep_work_block_duration: 4
  buffer_percentage: 15

  recurring_blocks:
    - name: "Daily Standup"
      duration: 0.5
      days: [mon, tue, wed, thu, fri]
      time: "09:00"

    - name: "Email Processing"
      duration: 0.5
      days: [mon, wed, fri]
      time: "08:30"

prioritization:
  high_threshold_hours: 3
  deadline_proximity_days: 3

  weights:
    goal_priority: 0.4
    deadline: 0.3
    estimated_hours: 0.2
    dependencies: 0.1

task_distribution:
  strategy: "balanced"
  max_tasks_per_day: 6
  max_high_priority_per_day: 3
  min_buffer_hours: 1

output:
  language: "ru"
  date_format: "%Y-%m-%d"
  time_format: "%H:%M"
  include_metrics: true
  include_calendar_blocks: true
  include_quick_links: true

paths:
  goals_file: "../data/goals.yaml"
  output_dir: "../output/todos"
  templates_dir: "../templates"
EOF

    print_success "Создан конфиг: $CONFIG_FILE"
}

show_usage() {
    cat << EOF
Использование: $(basename "$0") [ОПЦИИ]

ОПЦИИ:
    --help, -h              Показать эту справку
    --date DATE             Дата начала недели (YYYY-MM-DD)
    --week WEEK             Номер недели (YYYY-WXX)
    --export-ics            Экспорт в .ics календарь
    --export-metrics        Экспорт метрик
    --validate              Валидация goals.yaml
    --setup                 Первичная настройка (создание конфигов)

ПРИМЕРЫ:
    $(basename "$0")                          # Текущая неделя
    $(basename "$0") --date 2026-02-10        # Конкретная дата
    $(basename "$0") --week 2026-W07          # Конкретная неделя
    $(basename "$0") --export-ics             # С экспортом в календарь
    $(basename "$0") --validate               # Проверка goals.yaml

АВТОМАТИЗАЦИЯ:
    # Cron Job (каждое воскресенье в 18:00)
    0 18 * * 0 cd $SCRIPT_DIR && bash $(basename "$0")

EOF
}

run_generator() {
    local args=()

    # Передача аргументов в Python скрипт
    for arg in "$@"; do
        case $arg in
            --date=*)
                args+=(--date "${arg#*=}")
                ;;
            --week=*)
                args+=(--week "${arg#*=}")
                ;;
            --export-ics)
                args+=(--export-ics)
                ;;
            --export-metrics)
                args+=(--export-metrics)
                ;;
            --validate)
                args+=(--validate-goals)
                ;;
        esac
    done

    # Запуск Python скрипта
    python3 "$PYTHON_SCRIPT" --config "$CONFIG_FILE" "${args[@]}"
}

setup() {
    print_header
    print_info "Начальная настройка Life OS TODO Generator..."
    echo ""

    # Проверка зависимостей
    check_dependencies
    echo ""

    # Создание конфигурации
    if [[ ! -f "$CONFIG_FILE" ]]; then
        create_example_config
    else
        print_info "Конфиг уже существует: $CONFIG_FILE"
    fi
    echo ""

    # Создание goals.yaml
    check_goals_file
    echo ""

    # Создание выходной директории
    OUTPUT_DIR="${SCRIPT_DIR}/../output/todos"
    mkdir -p "$OUTPUT_DIR"
    print_success "Создана директория для TODO: $OUTPUT_DIR"
    echo ""

    print_success "Настройка завершена!"
    echo ""
    print_info "Теперь можно запустить: bash $(basename "$0")"
}

# Main
main() {
    # Обработка аргументов
    if [[ $# -eq 0 ]]; then
        # Без аргументов - стандартная генерация
        print_header
        check_dependencies
        check_goals_file
        echo ""
        run_generator
        exit 0
    fi

    case "$1" in
        --help|-h)
            show_usage
            exit 0
            ;;
        --setup)
            setup
            exit 0
            ;;
        --validate)
            print_header
            check_dependencies
            print_info "Валидация goals.yaml..."
            run_generator --validate
            exit 0
            ;;
        *)
            print_header
            check_dependencies
            check_goals_file
            echo ""
            run_generator "$@"
            exit 0
            ;;
    esac
}

# Запуск
main "$@"
