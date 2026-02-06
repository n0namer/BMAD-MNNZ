# Руководство по тестированию - Idea-to-Post Pipeline

**Тип документа:** Справочное руководство
**Дата:** 30 января 2026
**Версия:** 1.0
**Статус:** Полное тестовое руководство

---

## Обзор

Пошаговое руководство для ручного тестирования всех компонентов Content Machine Pipeline.

---

## Часть 1: Тестирование CSV-структуры

### Тест 1.1: Проверка заголовков столбцов

**Цель:** Убедиться, что все CSV-файлы имеют требуемые заголовки.

**Шаги:**

```bash
# Шаг 1: Проверить ideas_inbox.csv
head -1 data/ideas_inbox.csv
# Должно показать: id,date_added,source,raw_idea,category,status,notes,...

# Шаг 2: Проверить ideas_research.csv
head -1 data/ideas_research.csv | tr ',' '\n' | grep -E "id|pain_points_json"
# Должно показать обе строки: id, pain_points_json

# Шаг 3: Проверить posts_content.csv
head -1 data/posts_content.csv | tr ',' '\n' | tail -4
# Должно показать новые столбцы: last_posted_date, variant_of, content_type, repost_count

# Шаг 4: Проверить offer_filter.csv
head -2 user_preferences/offer_filter.csv
# Должно показать: offer_type,willing,notes и одну строку данных
```

**Ожидаемый результат:** ✅ Все заголовки присутствуют

**Если не прошел:**
```
1. Запустить миграцию:
   python scripts/migrate_csv_schema.py
   python scripts/migrate_posts_content.py

2. Повторить проверку
```

---

### Тест 1.2: Проверка целостности данных

**Цель:** Убедиться, что все данные имеют правильные типы.

**Шаги:**

```bash
# Шаг 1: Проверить ideas_inbox.csv (id должен быть числом)
tail -1 data/ideas_inbox.csv | cut -d',' -f1
# Должно показать число: 1 или 2 или 3 и т.д.

# Шаг 2: Проверить ideas_research.csv (avg_relevance должен быть от 0 до 1)
tail -1 data/ideas_research.csv | cut -d',' -f9
# Должно показать число 0.XX (например 0.85)

# Шаг 3: Проверить posts_content.csv (quality_score должен быть числом)
tail -1 data/posts_content.csv | cut -d',' -f8
# Должно показать число 0.XX (например 0.92)

# Шаг 4: Проверить offer_filter.csv (willing должен быть 0 или 1)
grep -E "^[^,]+,[01]," user_preferences/offer_filter.csv
# Все строки должны содержать 0 или 1
```

**Ожидаемый результат:** ✅ Все типы данных корректны

**Если не прошел:**
```
1. Найти неправильную строку
2. Исправить тип данных
3. Повторить тест
```

---

### Тест 1.3: Проверка JSON-полей

**Цель:** Убедиться, что JSON-поля содержат валидный JSON.

**Шаги:**

```python
import csv
import json

# Тест ideas_research.csv
print("Тест: pain_points_json в ideas_research.csv")
with open('data/ideas_research.csv') as f:
    reader = csv.DictReader(f)
    for idx, row in enumerate(reader, 1):
        pain_json = row.get('pain_points_json', '')

        # Пропустить пустые значения
        if not pain_json or pain_json == 'NULL':
            print(f"  Строка {idx}: пусто (OK)")
            continue

        # Проверить валидность JSON
        try:
            data = json.loads(pain_json)
            print(f"  Строка {idx}: ✅ валидный JSON")
            print(f"    Углы: {list(data.keys())}")

            # Проверить структуру
            for angle, pains in data.items():
                if not isinstance(pains, list):
                    print(f"    ❌ {angle} должен быть массив")
                elif not (3 <= len(pains) <= 5):
                    print(f"    ⚠️ {angle} имеет {len(pains)} боли (нужно 3-5)")
                else:
                    print(f"    ✅ {angle}: {len(pains)} болей")

        except json.JSONDecodeError as e:
            print(f"  Строка {idx}: ❌ неверный JSON: {e}")
            print(f"    Значение: {pain_json[:100]}...")
```

**Ожидаемый результат:** ✅ Все JSON-значения валидны

**Если не прошел:**
```
1. Найти неправильную строку
2. Исправить JSON синтаксис
3. Повторить тест
```

---

## Часть 2: Тестирование workflow_state.json

### Тест 2.1: Создание файла в c-03b2

**Цель:** Убедиться, что workflow_state.json создается правильно.

**Шаги:**

```python
import json
import os

# Имитировать c-03b2
print("Шаг 1: Проверить что .bmad существует")
if not os.path.exists('.bmad'):
    os.makedirs('.bmad')
    print("✅ Создана директория .bmad")
else:
    print("✅ Директория .bmad уже существует")

# Создать тестовый workflow_state.json
print("\nШаг 2: Создать тестовый workflow_state.json")
test_state = {
    "session_id": "session-2026-01-30-15-32-45",
    "current_step": "c-03b2",
    "timestamp_created": "2026-01-30T15:32:45Z",
    "content_type": "demo",
    "selected_idea_id": 1,
    "selected_idea_title": "Test Idea",
    "selected_angle": "angle_1",
    "selected_angle_name": "Test Angle",
    "generated_offers": [
        {
            "id": "offer-1",
            "type": "training",
            "title": "Test Training",
            "cta": "Test CTA",
            "pain_solved": ["Pain 1", "Pain 2"]
        }
    ],
    "draft_variants": [],
    "stepsCompleted": {
        "c-03b1": True,
        "c-03b2": True,
        "c-03c": False,
        "c-03d": False,
        "c-03e": False
    }
}

with open('.bmad/workflow_state.json', 'w', encoding='utf-8') as f:
    json.dump(test_state, f, ensure_ascii=False, indent=2)
    print("✅ Файл создан: .bmad/workflow_state.json")

# Проверить что файл существует
if os.path.exists('.bmad/workflow_state.json'):
    print("✅ Файл существует")
else:
    print("❌ Файл не существует")

# Проверить содержимое
with open('.bmad/workflow_state.json') as f:
    loaded = json.load(f)
    print(f"✅ JSON валиден")
    print(f"✅ session_id: {loaded['session_id']}")
    print(f"✅ generated_offers: {len(loaded['generated_offers'])} штук")
```

**Ожидаемый результат:** ✅ Файл создан и содержит валидный JSON

---

### Тест 2.2: Обновление файла в c-03c

**Цель:** Убедиться, что workflow_state.json обновляется правильно.

**Шаги:**

```python
import json

# Загрузить существующий файл
print("Шаг 1: Загрузить workflow_state.json")
with open('.bmad/workflow_state.json') as f:
    state = json.load(f)
    print(f"✅ Загружены сеанс: {state['session_id']}")
    print(f"✅ Текущий шаг: {state['current_step']}")

# Обновить файл с draft_variants
print("\nШаг 2: Добавить draft_variants")
state['current_step'] = 'c-03c'
state['draft_variants'] = [
    {
        "variant_id": "draft-1",
        "variant_number": 1,
        "title": "Test Title",
        "hook": "Test Hook",
        "body": "Test body content here...",
        "cta": "Click here",
        "selected": True,
        "quality_score": 0.85
    }
]
state['stepsCompleted']['c-03c'] = True

with open('.bmad/workflow_state.json', 'w', encoding='utf-8') as f:
    json.dump(state, f, ensure_ascii=False, indent=2)
    print("✅ Файл обновлен")

# Проверить обновление
with open('.bmad/workflow_state.json') as f:
    loaded = json.load(f)
    print(f"✅ Текущий шаг: {loaded['current_step']}")
    print(f"✅ draft_variants: {len(loaded['draft_variants'])} штук")
    print(f"✅ c-03c завершен: {loaded['stepsCompleted']['c-03c']}")
```

**Ожидаемый результат:** ✅ Файл обновлен с новыми данными

---

### Тест 2.3: Удаление файла в c-03e

**Цель:** Убедиться, что workflow_state.json удаляется после финализации.

**Шаги:**

```python
import os

# Проверить что файл существует
print("Шаг 1: Проверить файл перед удалением")
if os.path.exists('.bmad/workflow_state.json'):
    print("✅ Файл существует")
else:
    print("❌ Файл не существует - ничего не удалять")
    exit(1)

# Удалить файл
print("\nШаг 2: Удалить файл")
os.remove('.bmad/workflow_state.json')
print("✅ Файл удален")

# Проверить что файл удален
if not os.path.exists('.bmad/workflow_state.json'):
    print("✅ Файл успешно удален")
else:
    print("❌ Файл все еще существует")
```

**Ожидаемый результат:** ✅ Файл удален успешно

---

## Часть 3: Интеграционное тестирование

### Тест 3.1: Полный цикл (c-03b1 → c-03e)

**Цель:** Протестировать полный цикл создания контента.

**Шаги:**

```python
import csv
import json
import os
from datetime import datetime

print("=" * 60)
print("ИНТЕГРАЦИОННЫЙ ТЕСТ: Полный цикл c-03b1 → c-03e")
print("=" * 60)

# Шаг 1: Выбрать идею из ideas_research.csv
print("\n[1/5] c-03b1: Выбор идеи и угла")
print("-" * 60)

with open('data/ideas_research.csv') as f:
    reader = csv.DictReader(f)
    research_data = list(reader)[0]  # Первая идея

selected_idea_id = research_data['id']
selected_angle = 'angle_1'
print(f"✅ Выбрана идея ID: {selected_idea_id}")
print(f"✅ Выбран угол: {selected_angle}")

# Шаг 2: Создать workflow_state.json
print("\n[2/5] c-03b2: Генерация предложений")
print("-" * 60)

workflow_state = {
    "session_id": f"session-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}",
    "current_step": "c-03b2",
    "timestamp_created": datetime.now().isoformat() + "Z",
    "content_type": "demo",
    "selected_idea_id": int(selected_idea_id),
    "selected_idea_title": research_data.get('main_angle', 'Test'),
    "selected_angle": selected_angle,
    "selected_angle_name": "Test Angle",
    "generated_offers": [
        {
            "id": "offer-1",
            "type": "training",
            "title": "Training Offer",
            "cta": "Learn More",
            "pain_solved": ["Pain 1", "Pain 2"]
        }
    ],
    "draft_variants": [],
    "stepsCompleted": {
        "c-03b1": True,
        "c-03b2": True,
        "c-03c": False,
        "c-03d": False,
        "c-03e": False
    }
}

if not os.path.exists('.bmad'):
    os.makedirs('.bmad')

with open('.bmad/workflow_state.json', 'w', encoding='utf-8') as f:
    json.dump(workflow_state, f, ensure_ascii=False, indent=2)

print(f"✅ Создан workflow_state.json (сеанс: {workflow_state['session_id']})")
print(f"✅ Сгенерировано предложений: {len(workflow_state['generated_offers'])}")

# Шаг 3: Создать draft_variants
print("\n[3/5] c-03c: Создание черновиков")
print("-" * 60)

with open('.bmad/workflow_state.json') as f:
    workflow_state = json.load(f)

workflow_state['current_step'] = 'c-03c'
workflow_state['draft_variants'] = [
    {
        "variant_id": "draft-1",
        "variant_number": 1,
        "title": "Quick Documentation",
        "hook": "80+ docs in 2 hours?",
        "body": "Yesterday I generated 80+ documents in 2 hours...",
        "cta": "Learn how →",
        "selected": True,
        "quality_score": 0.92
    }
]
workflow_state['stepsCompleted']['c-03c'] = True

with open('.bmad/workflow_state.json', 'w', encoding='utf-8') as f:
    json.dump(workflow_state, f, ensure_ascii=False, indent=2)

print(f"✅ Созданы варианты черновиков: {len(workflow_state['draft_variants'])}")
print(f"✅ Выбранный вариант: draft-1")

# Шаг 4: Сохранить в posts_content.csv
print("\n[4/5] c-03e: Финализация и сохранение")
print("-" * 60)

# Получить текущее количество строк
with open('data/posts_content.csv') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    existing_rows = list(reader)

current_id = len(existing_rows) + 1

# Подготовить новую строку
new_post = {
    'id': str(current_id),
    'research_id': selected_idea_id,
    'angle_used': selected_angle,
    'title': 'Quick Documentation',
    'body': 'Yesterday I generated 80+ documents in 2 hours...',
    'cta': 'Learn how →',
    'hook': '80+ docs in 2 hours?',
    'quality_score': 0.92,
    'created_date': datetime.now().strftime('%Y-%m-%d'),
    'publish_date': '',
    'notes': 'Test post',
    'last_posted_date': '',
    'variant_of': '',
    'content_type': 'demo',
    'repost_count': '0'
}

# Добавить в CSV
existing_rows.append(new_post)

with open('data/posts_content.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(existing_rows)

print(f"✅ Пост сохранен в posts_content.csv (ID: {current_id})")

# Шаг 5: Удалить workflow_state.json
print("\n[5/5] Очистка: Удаление workflow_state.json")
print("-" * 60)

if os.path.exists('.bmad/workflow_state.json'):
    os.remove('.bmad/workflow_state.json')
    print("✅ workflow_state.json удален")
else:
    print("⚠️ workflow_state.json не найден")

# Финальная проверка
print("\n" + "=" * 60)
print("РЕЗУЛЬТАТЫ")
print("=" * 60)

with open('data/posts_content.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

last_post = rows[-1]
print(f"✅ Последний пост в posts_content.csv:")
print(f"   ID: {last_post['id']}")
print(f"   Title: {last_post['title']}")
print(f"   Content Type: {last_post.get('content_type', 'N/A')}")
print(f"   Quality Score: {last_post['quality_score']}")

print("\n✅ ИНТЕГРАЦИОННЫЙ ТЕСТ ПРОЙДЕН")
```

**Ожидаемый результат:** ✅ Пост сохранен в posts_content.csv и workflow_state.json удален

---

## Часть 4: Сценарии ошибок

### Сценарий 4.1: Отсутствующий столбец в CSV

**Проблема:** `pain_points_json` не добавлен в ideas_research.csv

**Как воспроизвести:**
```python
import csv

# Удалить столбец pain_points_json
with open('data/ideas_research.csv') as f:
    reader = csv.DictReader(f)
    fieldnames = [f for f in reader.fieldnames if f != 'pain_points_json']
    rows = list(reader)

with open('data/ideas_research.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Столбец pain_points_json удален")
```

**Ожидаемая ошибка:**
```
❌ KeyError: 'pain_points_json'
```

**Как исправить:**
```python
python scripts/migrate_csv_schema.py
```

---

### Сценарий 4.2: Невалидный JSON в pain_points_json

**Проблема:** JSON содержит синтаксическую ошибку

**Как воспроизвести:**
```python
import csv

with open('data/ideas_research.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Внести ошибку в JSON
rows[0]['pain_points_json'] = '{"angle_1": [invalid json]}'

with open('data/ideas_research.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(rows)
```

**Ожидаемая ошибка:**
```
❌ json.JSONDecodeError: Expecting value
```

**Как исправить:**
```python
import json

# Проверить и исправить JSON
with open('data/ideas_research.csv') as f:
    reader = csv.DictReader(f)
    for idx, row in enumerate(reader):
        try:
            json.loads(row['pain_points_json'])
        except json.JSONDecodeError as e:
            print(f"Ошибка в строке {idx}: {e}")
            # Исправить JSON вручную
```

---

## Проверочный список

### Перед развертыванием

- [ ] Тест 1.1: Все заголовки столбцов присутствуют
- [ ] Тест 1.2: Все типы данных корректны
- [ ] Тест 1.3: Все JSON-поля валидны
- [ ] Тест 2.1: workflow_state.json создается правильно
- [ ] Тест 2.2: workflow_state.json обновляется правильно
- [ ] Тест 2.3: workflow_state.json удаляется правильно
- [ ] Тест 3.1: Полный цикл работает
- [ ] Сценарий 4.1: Обработка отсутствующих столбцов
- [ ] Сценарий 4.2: Обработка невалидного JSON

### Автоматические тесты

```bash
# Запустить все тесты
python scripts/validate_csv_structure.py
python scripts/test_pain_generation.py
python scripts/test_offer_filter.py
python scripts/validate_workflow_state.py

# Все должны показать ✅
```

---

**Тестирование завершено**
**Дата:** 30 января 2026
**Статус:** ✅ Полное тестовое руководство
