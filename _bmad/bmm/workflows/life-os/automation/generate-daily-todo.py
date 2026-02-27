#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Life OS - Daily TODO Generator
Генерация ежедневных TODO списков из недельных целей

Использование:
    python generate-daily-todo.py                    # Текущая неделя
    python generate-daily-todo.py --date 2026-02-10  # Конкретная дата
    python generate-daily-todo.py --export-ics       # С экспортом в календарь
"""

import yaml
import os
import sys
import argparse
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional
import json


class TodoGenerator:
    """Генератор ежедневных TODO из weekly goals"""

    # Дни недели на русском
    WEEKDAYS_RU = {
        0: "Понедельник",
        1: "Вторник",
        2: "Среда",
        3: "Четверг",
        4: "Пятница",
        5: "Суббота",
        6: "Воскресенье"
    }

    WEEKDAYS_SHORT = {
        0: "mon", 1: "tue", 2: "wed", 3: "thu",
        4: "fri", 5: "sat", 6: "sun"
    }

    def __init__(self, config_path: str = "todo-config.yaml"):
        """Инициализация генератора"""
        self.config = self._load_config(config_path)
        self.goals = None
        self.week_focus = None

    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Загрузка конфигурации"""
        if not os.path.exists(config_path):
            # Дефолтная конфигурация
            return {
                'calendar': {
                    'work_days': ['mon', 'tue', 'wed', 'thu', 'fri'],
                    'work_hours_per_day': 8,
                    'deep_work_block_duration': 4,
                    'buffer_percentage': 15,
                    'recurring_blocks': []
                },
                'prioritization': {
                    'high_threshold_hours': 3,
                    'deadline_proximity_days': 3,
                    'weights': {
                        'goal_priority': 0.4,
                        'deadline': 0.3,
                        'estimated_hours': 0.2,
                        'dependencies': 0.1
                    }
                },
                'task_distribution': {
                    'strategy': 'balanced',
                    'max_tasks_per_day': 6,
                    'max_high_priority_per_day': 3,
                    'min_buffer_hours': 1
                },
                'output': {
                    'language': 'ru',
                    'date_format': '%Y-%m-%d',
                    'time_format': '%H:%M',
                    'include_metrics': True,
                    'include_calendar_blocks': True,
                    'include_quick_links': True
                },
                'paths': {
                    'goals_file': '../data/goals.yaml',
                    'output_dir': '../output/todos',
                    'templates_dir': '../templates'
                }
            }

        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def load_goals(self, goals_path: Optional[str] = None) -> None:
        """Загрузка целей из goals.yaml"""
        if goals_path is None:
            goals_path = self.config['paths']['goals_file']

        if not os.path.exists(goals_path):
            raise FileNotFoundError(f"Goals file not found: {goals_path}")

        with open(goals_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            self.week_focus = data.get('week_focus', {})
            self.goals = data.get('goals', [])

    def calculate_priority(self, task: Dict[str, Any], goal: Dict[str, Any]) -> str:
        """Расчёт приоритета задачи на основе весов"""
        weights = self.config['prioritization']['weights']
        score = 0

        # 1. Приоритет цели
        goal_priority_map = {'high': 30, 'medium': 20, 'low': 10}
        score += goal_priority_map.get(goal.get('priority', 'medium'), 20) * weights['goal_priority']

        # 2. Близость дедлайна
        deadline = goal.get('deadline')
        if deadline:
            days_until = (datetime.strptime(deadline, '%Y-%m-%d') - datetime.now()).days
            if days_until <= self.config['prioritization']['deadline_proximity_days']:
                score += 30 * weights['deadline']
            elif days_until <= 7:
                score += 20 * weights['deadline']
            else:
                score += 10 * weights['deadline']

        # 3. Оценка часов
        est_hours = task.get('estimated_hours', 0)
        if est_hours >= self.config['prioritization']['high_threshold_hours']:
            score += 30 * weights['estimated_hours']
        elif est_hours >= 1.5:
            score += 20 * weights['estimated_hours']
        else:
            score += 10 * weights['estimated_hours']

        # 4. Зависимости (placeholder, требует доп. данных)
        score += 15 * weights['dependencies']

        # Классификация
        if score >= 25:
            return 'high'
        elif score >= 15:
            return 'medium'
        else:
            return 'low'

    def distribute_tasks(self, start_date: datetime) -> Dict[str, List[Dict[str, Any]]]:
        """Распределение задач по дням недели"""
        work_days = self.config['calendar']['work_days']
        hours_per_day = self.config['calendar']['work_hours_per_day']
        buffer_pct = self.config['calendar']['buffer_percentage']

        # Доступные часы в день (с учётом buffer и recurring blocks)
        recurring_hours = sum(
            block['duration'] for block in self.config['calendar'].get('recurring_blocks', [])
        )
        available_hours_per_day = hours_per_day * (1 - buffer_pct / 100) - recurring_hours

        # Подготовка задач
        all_tasks = []
        for goal in self.goals:
            goal_id = goal['id']
            for task_desc in goal.get('tasks', []):
                # Оценка часов (если не указана, дефолт 2ч)
                est_hours = 2.0
                if isinstance(task_desc, dict):
                    task_title = task_desc.get('title', task_desc.get('description', 'Unknown'))
                    est_hours = task_desc.get('estimated_hours', 2.0)
                else:
                    task_title = task_desc

                task = {
                    'title': task_title,
                    'goal_id': goal_id,
                    'goal': goal,
                    'estimated_hours': est_hours,
                    'priority': self.calculate_priority({'estimated_hours': est_hours}, goal)
                }
                all_tasks.append(task)

        # Сортировка по приоритету
        priority_order = {'high': 0, 'medium': 1, 'low': 2}
        all_tasks.sort(key=lambda t: (priority_order[t['priority']], -t['estimated_hours']))

        # Распределение по дням
        day_schedules = {}
        current_date = start_date
        task_idx = 0

        for day_offset in range(5):  # Пн-Пт
            current_date = start_date + timedelta(days=day_offset)
            day_key = current_date.strftime(self.config['output']['date_format'])
            weekday_short = self.WEEKDAYS_SHORT[current_date.weekday()]

            if weekday_short not in work_days:
                continue

            day_schedule = {
                'date': day_key,
                'weekday': self.WEEKDAYS_RU[current_date.weekday()],
                'tasks': [],
                'total_hours': 0,
                'high_count': 0,
                'medium_count': 0,
                'low_count': 0
            }

            # Заполнение дня задачами
            while (task_idx < len(all_tasks) and
                   day_schedule['total_hours'] + all_tasks[task_idx]['estimated_hours'] <= available_hours_per_day and
                   len(day_schedule['tasks']) < self.config['task_distribution']['max_tasks_per_day']):

                task = all_tasks[task_idx]

                # Проверка лимита high priority
                if task['priority'] == 'high' and day_schedule['high_count'] >= self.config['task_distribution']['max_high_priority_per_day']:
                    task_idx += 1
                    continue

                day_schedule['tasks'].append(task)
                day_schedule['total_hours'] += task['estimated_hours']
                day_schedule[f"{task['priority']}_count"] += 1
                task_idx += 1

            day_schedules[day_key] = day_schedule

        return day_schedules

    def generate_time_blocks(self, tasks: List[Dict[str, Any]], start_hour: int = 9) -> List[str]:
        """Генерация временных блоков для календаря"""
        blocks = []
        current_time = datetime.strptime(f"{start_hour:02d}:00", "%H:%M")

        for task in tasks:
            end_time = current_time + timedelta(hours=task['estimated_hours'])
            time_range = f"{current_time.strftime('%H:%M')}-{end_time.strftime('%H:%M')}"

            # Извлечение названия проекта из goal_id
            project_name = task['goal']['title'].split()[0] if task['goal'].get('title') else "Project"

            block = f"**{time_range}**: [{project_name}] {task['title']} (goal: {task['goal_id']})"
            blocks.append(block)

            current_time = end_time

        return blocks

    def generate_todo_content(self, day_schedule: Dict[str, Any]) -> str:
        """Генерация содержимого TODO файла"""
        date = day_schedule['date']
        weekday = day_schedule['weekday']
        tasks = day_schedule['tasks']

        # Группировка по приоритетам
        high_tasks = [t for t in tasks if t['priority'] == 'high']
        medium_tasks = [t for t in tasks if t['priority'] == 'medium']
        low_tasks = [t for t in tasks if t['priority'] == 'low']

        # Генерация календарных блоков
        calendar_blocks = self.generate_time_blocks(tasks)

        # Шаблон TODO
        content = f"""# TODO - {date} ({weekday})

## 🎯 Week Focus: {self.week_focus.get('theme', 'Не указано')}

---

### ⚡ High Priority (Must Do)
"""

        # High priority задачи
        current_time = datetime.strptime("09:00", "%H:%M")
        for task in high_tasks:
            end_time = current_time + timedelta(hours=task['estimated_hours'])
            time_range = f"{current_time.strftime('%H:%M')}-{end_time.strftime('%H:%M')}"
            content += f"- [ ] {task['title']} ({task['estimated_hours']:.0f}ч) → [{time_range}] (goal: {task['goal_id']})\n"
            current_time = end_time

        content += "\n### 🟡 Medium Priority (Should Do)\n"

        # Medium priority задачи
        for task in medium_tasks:
            end_time = current_time + timedelta(hours=task['estimated_hours'])
            time_range = f"{current_time.strftime('%H:%M')}-{end_time.strftime('%H:%M')}"
            content += f"- [ ] {task['title']} ({task['estimated_hours']:.0f}ч) → [{time_range}] (goal: {task['goal_id']})\n"
            current_time = end_time

        content += "\n### 🔵 Low Priority (Nice to Have)\n"

        # Low priority задачи
        for task in low_tasks:
            content += f"- [ ] {task['title']} ({task['estimated_hours']:.0f}ч) → [Buffer time]\n"

        # Календарные блоки
        if self.config['output']['include_calendar_blocks']:
            content += "\n---\n\n## 📅 Calendar Blocks\n\n"
            content += "\n".join(calendar_blocks)

        # Метрики
        if self.config['output']['include_metrics']:
            deep_work_sessions = len([t for t in high_tasks if t['estimated_hours'] >= self.config['calendar']['deep_work_block_duration']])

            content += f"""

---

## 📊 Daily Metrics

- **Запланировано часов**: {day_schedule['total_hours']:.0f}
- **Focus time блоки**: {len(tasks)}
- **Deep work сессии**: {deep_work_sessions}
- **Приоритетных задач**: {len(high_tasks)}
- **Alignment с целями**: {100 if tasks else 0}%
"""

        # Quick Links
        if self.config['output']['include_quick_links']:
            current_date = datetime.strptime(date, self.config['output']['date_format'])
            prev_date = (current_date - timedelta(days=1)).strftime(self.config['output']['date_format'])
            next_date = (current_date + timedelta(days=1)).strftime(self.config['output']['date_format'])
            week_num = self.week_focus.get('week_number', current_date.isocalendar()[1])

            content += f"""

---

## 🔗 Quick Links

- [Week Goals](../data/goals.yaml)
- [Previous Day]({prev_date}-{self.WEEKDAYS_SHORT[current_date.weekday()-1 if current_date.weekday() > 0 else 6]}.md)
- [Next Day]({next_date}-{self.WEEKDAYS_SHORT[(current_date.weekday()+1) % 7]}.md)
- [Weekly Review](../reviews/week-{week_num:02d}.md)
"""

        # Метаданные
        content += f"""

---

**Сгенерировано**: {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Скрипт**: automation/generate-daily-todo.py v1.0
"""

        return content

    def save_todo_file(self, day_schedule: Dict[str, Any], output_dir: str) -> str:
        """Сохранение TODO файла"""
        os.makedirs(output_dir, exist_ok=True)

        date = day_schedule['date']
        current_date = datetime.strptime(date, self.config['output']['date_format'])
        weekday_short = self.WEEKDAYS_SHORT[current_date.weekday()]
        filename = f"{date}-{weekday_short}.md"
        filepath = os.path.join(output_dir, filename)

        content = self.generate_todo_content(day_schedule)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return filepath

    def export_to_ics(self, day_schedules: Dict[str, Dict[str, Any]], output_dir: str) -> None:
        """Экспорт в .ics формат для календарей"""
        ics_dir = os.path.join(output_dir, 'ics')
        os.makedirs(ics_dir, exist_ok=True)

        for date, schedule in day_schedules.items():
            ics_content = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//Life OS//Daily TODO//EN\n"

            current_date = datetime.strptime(date, self.config['output']['date_format'])
            current_time = current_date.replace(hour=9, minute=0)

            for task in schedule['tasks']:
                end_time = current_time + timedelta(hours=task['estimated_hours'])

                ics_content += f"""BEGIN:VEVENT
DTSTART:{current_time.strftime('%Y%m%dT%H%M%S')}
DTEND:{end_time.strftime('%Y%m%dT%H%M%S')}
SUMMARY:{task['title']}
DESCRIPTION:Goal: {task['goal_id']}\\nPriority: {task['priority']}
LOCATION:Focus Time
END:VEVENT
"""
                current_time = end_time

            ics_content += "END:VCALENDAR\n"

            ics_file = os.path.join(ics_dir, f"{date}.ics")
            with open(ics_file, 'w', encoding='utf-8') as f:
                f.write(ics_content)

            print(f"✅ Exported to calendar: {ics_file}")

    def export_metrics(self, day_schedules: Dict[str, Dict[str, Any]], output_dir: str) -> None:
        """Экспорт метрик в JSON"""
        metrics_dir = os.path.join(output_dir, 'metrics')
        os.makedirs(metrics_dir, exist_ok=True)

        week_num = self.week_focus.get('week_number', datetime.now().isocalendar()[1])
        metrics = {
            'week_number': week_num,
            'week_theme': self.week_focus.get('theme'),
            'total_days': len(day_schedules),
            'total_tasks': sum(len(d['tasks']) for d in day_schedules.values()),
            'total_hours': sum(d['total_hours'] for d in day_schedules.values()),
            'avg_hours_per_day': sum(d['total_hours'] for d in day_schedules.values()) / len(day_schedules) if day_schedules else 0,
            'priority_distribution': {
                'high': sum(d['high_count'] for d in day_schedules.values()),
                'medium': sum(d['medium_count'] for d in day_schedules.values()),
                'low': sum(d['low_count'] for d in day_schedules.values())
            },
            'daily_breakdown': [
                {
                    'date': d['date'],
                    'weekday': d['weekday'],
                    'tasks': len(d['tasks']),
                    'hours': d['total_hours'],
                    'high': d['high_count'],
                    'medium': d['medium_count'],
                    'low': d['low_count']
                }
                for d in day_schedules.values()
            ]
        }

        metrics_file = os.path.join(metrics_dir, f"week-{week_num:02d}-metrics.json")
        with open(metrics_file, 'w', encoding='utf-8') as f:
            json.dump(metrics, f, ensure_ascii=False, indent=2)

        print(f"✅ Exported metrics: {metrics_file}")

    def generate(self, start_date: Optional[datetime] = None, export_ics: bool = False, export_metrics_flag: bool = False) -> None:
        """Основной метод генерации"""
        if start_date is None:
            # Понедельник текущей недели
            today = datetime.now()
            start_date = today - timedelta(days=today.weekday())

        print(f"📅 Генерация TODO для недели: {start_date.strftime('%Y-%m-%d')}")

        # Загрузка целей
        self.load_goals()
        print(f"✅ Загружено целей: {len(self.goals)}")

        # Распределение задач
        day_schedules = self.distribute_tasks(start_date)
        print(f"✅ Распределено по дням: {len(day_schedules)}")

        # Сохранение TODO файлов
        output_dir = self.config['paths']['output_dir']
        for day_schedule in day_schedules.values():
            filepath = self.save_todo_file(day_schedule, output_dir)
            print(f"📝 Создан: {filepath}")

        # Экспорт в календарь
        if export_ics:
            self.export_to_ics(day_schedules, output_dir)

        # Экспорт метрик
        if export_metrics_flag:
            self.export_metrics(day_schedules, output_dir)

        print("\n✨ Генерация завершена!")


def main():
    """CLI entrypoint"""
    parser = argparse.ArgumentParser(description='Life OS - Daily TODO Generator')
    parser.add_argument('--date', type=str, help='Дата начала недели (YYYY-MM-DD)')
    parser.add_argument('--week', type=str, help='Номер недели (YYYY-WXX)')
    parser.add_argument('--config', type=str, default='todo-config.yaml', help='Путь к конфигу')
    parser.add_argument('--export-ics', action='store_true', help='Экспорт в .ics календарь')
    parser.add_argument('--export-metrics', action='store_true', help='Экспорт метрик')
    parser.add_argument('--validate-goals', action='store_true', help='Валидация goals.yaml')

    args = parser.parse_args()

    # Определение даты старта
    start_date = None
    if args.date:
        start_date = datetime.strptime(args.date, '%Y-%m-%d')
    elif args.week:
        year, week = args.week.split('-W')
        start_date = datetime.strptime(f"{year}-W{week}-1", "%Y-W%W-%w")

    # Инициализация генератора
    generator = TodoGenerator(args.config)

    # Валидация goals.yaml (если запрошена)
    if args.validate_goals:
        try:
            generator.load_goals()
            print("✅ goals.yaml корректен")
            sys.exit(0)
        except Exception as e:
            print(f"❌ Ошибка валидации: {e}")
            sys.exit(1)

    # Генерация TODO
    try:
        generator.generate(start_date, args.export_ics, args.export_metrics)
    except Exception as e:
        print(f"❌ Ошибка генерации: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
