# Руководство по устранению неполадок

**Тип документа:** Справочное руководство
**Дата:** 30 января 2026
**Версия:** 1.0
**Статус:** Полное руководство

---

## Обзор

Решения для распространённых проблем, которые могут возникнуть при использовании Idea-to-Post Pipeline v2.

---

## РАЗДЕЛ A: CSV-файлы

### Проблема A.1: "Столбец не найден" (KeyError)

**Ошибка:**
```
KeyError: 'pain_points_json'
KeyError: 'variant_of'
KeyError: 'content_type'
```

**Причина:** Столбец не добавлен в CSV файл при миграции.

**Решение:**

```bash
# Шаг 1: Проверить какие столбцы есть
head -1 data/ideas_research.csv | tr ',' '\n' | grep pain_points

# Если не найдено, запустить миграцию
python scripts/migrate_csv_schema.py

# Для posts_content.csv
python scripts/migrate_posts_content.py

# Шаг 2: Проверить что столбец добавлен
head -1 data/ideas_research.csv | grep pain_points_json
# Должно быть: pain_points_json
```

**Если это не помогло:**

```python
# Ручное добавление столбца
import csv

input_file = 'data/ideas_research.csv'
rows = []

with open(input_file) as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames or [])

    if 'pain_points_json' not in fieldnames:
        fieldnames.append('pain_points_json')

    for row in reader:
        if 'pain_points_json' not in row:
            row['pain_points_json'] = ''
        rows.append(row)

with open(input_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("✅ Столбец добавлен")
```

---

### Проблема A.2: "Невалидная дата" (ValueError)

**Ошибка:**
```
ValueError: time data '2026-1-30' does not match format '%Y-%m-%d'
```

**Причина:** Дата в неправильном формате (нужен YYYY-MM-DD).

**Решение:**

```python
import csv
from datetime import datetime

input_file = 'data/ideas_inbox.csv'
rows = []

with open(input_file) as f:
    reader = csv.DictReader(f)
    for idx, row in enumerate(reader, 1):
        try:
            # Проверить формат даты
            datetime.strptime(row['date_added'], '%Y-%m-%d')
        except ValueError as e:
            print(f"❌ Ошибка в строке {idx}: {e}")
            print(f"   Значение: {row['date_added']}")

            # Исправить (если возможно)
            try:
                parsed = datetime.strptime(row['date_added'], '%Y-%m-%d')
                row['date_added'] = parsed.strftime('%Y-%m-%d')
                print(f"   ✅ Исправлено на: {row['date_added']}")
            except ValueError:
                print(f"   ❌ Не удалось исправить автоматически")
                print(f"   Исправьте вручную в CSV")

        rows.append(row)

with open(input_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(rows)
```

**Правильный формат:** `2026-01-30` (YYYY-MM-DD)

---

### Проблема A.3: "Дублирование ID"

**Ошибка:**
```
AssertionError: ID не уникален
```

**Причина:** Два поста имеют одинаковый ID.

**Решение:**

```python
import csv

# Проверить дублирования
csv_file = 'data/posts_content.csv'
ids = []

with open(csv_file) as f:
    reader = csv.DictReader(f)
    for idx, row in enumerate(reader, 1):
        post_id = row['id']
        if post_id in ids:
            print(f"❌ ID {post_id} повторяется (строка {idx})")
        ids.append(post_id)

# Исправить ID
rows = []
max_id = 0

with open(csv_file) as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames

    for row in reader:
        try:
            current_id = int(row['id'])
            if current_id > max_id:
                max_id = current_id
        except ValueError:
            pass

# Переписать с уникальными ID
with open(csv_file) as f:
    reader = csv.DictReader(f)
    rows = list(reader)

for idx, row in enumerate(rows, 1):
    row['id'] = str(idx)  # Пересчитать ID

with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("✅ ID пересчитаны (теперь уникальные)")
```

---

## РАЗДЕЛ B: JSON-файлы

### Проблема B.1: "Невалидный JSON синтаксис"

**Ошибка:**
```
json.JSONDecodeError: Expecting value: line 1 column X
```

**Причина:** JSON содержит синтаксическую ошибку.

**Решение:**

```python
import json
import csv

# Проверить pain_points_json в ideas_research.csv
csv_file = 'data/ideas_research.csv'

issues = []

with open(csv_file) as f:
    reader = csv.DictReader(f)
    for idx, row in enumerate(reader, 1):
        json_str = row.get('pain_points_json', '')

        # Пропустить пустые
        if not json_str or json_str == 'NULL':
            continue

        # Проверить синтаксис
        try:
            json.loads(json_str)
        except json.JSONDecodeError as e:
            issues.append({
                'row': idx,
                'error': str(e),
                'value': json_str[:100]
            })

if issues:
    print(f"❌ Найдено {len(issues)} ошибок JSON:")
    for issue in issues:
        print(f"\n   Строка {issue['row']}: {issue['error']}")
        print(f"   Значение: {issue['value']}...")
        print(f"\n   Исправьте в CSV вручную или используйте валидатор JSON")
else:
    print("✅ Все JSON значения валидны")

# Помощник: Проверить структуру JSON
def validate_pain_points_structure(json_str):
    """Проверить что JSON соответствует формату"""
    try:
        data = json.loads(json_str)

        # Проверить что это объект
        if not isinstance(data, dict):
            return False, "Должен быть объект {}, не массив []"

        # Проверить что ключи - это углы
        for key, value in data.items():
            if not isinstance(value, list):
                return False, f"{key} должен быть массив, не {type(value).__name__}"
            if not (3 <= len(value) <= 5):
                return False, f"{key} должен иметь 3-5 болей, найдено {len(value)}"
            if not all(isinstance(v, str) for v in value):
                return False, f"{key} должен содержать только строки"

        return True, "OK"

    except json.JSONDecodeError as e:
        return False, str(e)

# Пример использования
json_test = '{"angle_1": ["Pain 1", "Pain 2", "Pain 3"]}'
valid, msg = validate_pain_points_structure(json_test)
print(f"{'✅' if valid else '❌'} {msg}")
```

---

### Проблема B.2: "workflow_state.json не создается"

**Ошибка:**
```
FileNotFoundError: [Errno 2] No such file or directory: '.bmad/workflow_state.json'
```

**Причина:** Директория `.bmad` не существует или не доступна для записи.

**Решение:**

```bash
# Шаг 1: Создать директорию
mkdir -p .bmad

# Шаг 2: Проверить права
ls -la .bmad
# Должны быть права для чтения и записи (rwx для владельца)

# Шаг 3: Исправить права если нужно
chmod 755 .bmad

# Шаг 4: Проверить что можно писать
touch .bmad/test.txt && rm .bmad/test.txt
# Должно работать без ошибок
```

---

### Проблема B.3: "workflow_state.json содержит неправильные данные"

**Ошибка:**
```
KeyError: 'generated_offers'
ValueError: expected string or buffer
```

**Причина:** workflow_state.json был повреждён или содержит невалидный JSON.

**Решение:**

```python
import json
import os

json_file = '.bmad/workflow_state.json'

# Шаг 1: Проверить валидность JSON
try:
    with open(json_file) as f:
        state = json.load(f)
    print("✅ JSON валиден")
except json.JSONDecodeError as e:
    print(f"❌ Ошибка JSON: {e}")

    # Шаг 2: Удалить повреждённый файл
    os.remove(json_file)
    print(f"✅ Удален повреждённый файл")

    # Шаг 3: Начать заново с c-03b1
    print("⚠️ Необходимо начать заново с c-03b1")

# Проверить обязательные поля
required_fields = [
    'session_id',
    'current_step',
    'selected_idea_id',
    'selected_angle',
    'generated_offers',
    'draft_variants',
    'stepsCompleted'
]

with open(json_file) as f:
    state = json.load(f)

missing = [f for f in required_fields if f not in state]
if missing:
    print(f"❌ Отсутствуют поля: {missing}")
    print("⚠️ Необходимо начать заново с c-03b1")
else:
    print("✅ Все требуемые поля присутствуют")
```

---

### Проблема B.4: "workflow_state.json не удаляется в c-03e"

**Симптом:** После завершения c-03e файл всё ещё в `.bmad/workflow_state.json`

**Причина:** Код в c-03e не выполнил удаление.

**Решение:**

```bash
# Ручное удаление
rm -f .bmad/workflow_state.json

# Проверить что удален
ls -la .bmad/workflow_state.json 2>&1
# Должно показать: No such file or directory (или ошибка)

# Если файл не удалась удалить
# Проверьте права:
ls -la .bmad/
chmod 755 .bmad/  # Исправить права
rm -f .bmad/workflow_state.json
```

---

## РАЗДЕЛ C: offer_filter.csv

### Проблема C.1: "Файл offer_filter.csv не существует"

**Ошибка:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'user_preferences/offer_filter.csv'
```

**Причина:** Файл не был создан.

**Решение:**

```bash
# Шаг 1: Создать директорию
mkdir -p user_preferences

# Шаг 2: Создать файл (текстовый редактор или команда)
cat > user_preferences/offer_filter.csv << 'EOF'
offer_type,willing,notes
training,1,Предлагаю 1-on-1 коучинг и менторинг сессии
setup,1,Могу проектировать процессы и рабочие потоки для клиентов
templates,1,Есть готовые шаблоны методологии и руководства
consulting,0,Может быть позже - сейчас ограничения по времени
full_dev,0,Не могу полностью разрабатывать на текущем этапе
EOF

# Шаг 3: Проверить
cat user_preferences/offer_filter.csv
# Должны быть видны 5 строк после заголовка
```

---

### Проблема C.2: "Невалидные значения в willing"

**Ошибка:**
```
AssertionError: willing должно быть 0 или 1
```

**Причина:** В столбце `willing` не-булева значение.

**Решение:**

```python
import csv

csv_file = 'user_preferences/offer_filter.csv'
rows = []

with open(csv_file) as f:
    reader = csv.DictReader(f)
    for idx, row in enumerate(reader, 1):
        willing = row['willing'].strip()

        # Проверить
        if willing not in ['0', '1']:
            print(f"❌ Строка {idx}: willing='{willing}' (должно быть 0 или 1)")
            # Исправить
            willing = '1' if willing.lower() in ['yes', 'true', '1'] else '0'
            row['willing'] = willing
            print(f"   ✅ Исправлено на: {willing}")

        rows.append(row)

# Сохранить исправления
with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("✅ Значения исправлены")
```

---

### Проблема C.3: "Неправильные типы предложений"

**Ошибка:**
```
AssertionError: offer_type не в ['training', 'setup', ...]
```

**Причина:** В `offer_type` опечатка или неправильное значение.

**Решение:**

```python
import csv

csv_file = 'user_preferences/offer_filter.csv'
VALID_TYPES = {'training', 'setup', 'templates', 'consulting', 'full_dev'}

rows = []

with open(csv_file) as f:
    reader = csv.DictReader(f)
    for idx, row in enumerate(reader, 1):
        offer_type = row['offer_type'].strip()

        if offer_type not in VALID_TYPES:
            print(f"❌ Строка {idx}: offer_type='{offer_type}' не распознан")
            print(f"   Допустимые: {VALID_TYPES}")
            # Исправить похожее значение
            similar = [t for t in VALID_TYPES if t.startswith(offer_type[0])]
            if similar:
                row['offer_type'] = similar[0]
                print(f"   ✅ Исправлено на: {similar[0]}")
            else:
                print(f"   ❌ Исправьте вручную")

        rows.append(row)

with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(rows)
```

---

## РАЗДЕЛ D: Процесс создания контента (c-03)

### Проблема D.1: "pain_points_json не заполнен в c-02"

**Симптом:** В ideas_research.csv столбец `pain_points_json` пуст

**Причина:** Шаг c-02c не заполнил значение.

**Решение:**

```python
import json
import csv
from datetime import datetime

csv_file = 'data/ideas_research.csv'
rows = []

with open(csv_file) as f:
    reader = csv.DictReader(f)
    for idx, row in enumerate(reader, 1):
        # Проверить пусто ли
        if not row.get('pain_points_json') or row['pain_points_json'] == 'NULL':
            print(f"Строка {idx}: pain_points_json пусто")

            # Сгенерировать пример (или попросить пользователя заполнить)
            example_pains = {
                "angle_1": [
                    "Проблема 1 для первого угла",
                    "Проблема 2 для первого угла",
                    "Проблема 3 для первого угла"
                ],
                "angle_2": [
                    "Проблема 1 для второго угла",
                    "Проблема 2 для второго угла"
                ]
            }

            row['pain_points_json'] = json.dumps(example_pains, ensure_ascii=False)
            print(f"  ✅ Заполнено примером (отредактируйте в CSV)")

        rows.append(row)

# Сохранить
with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("✅ Заполнены пустые значения")
```

---

### Проблема D.2: "Предложения не генерируются в c-03b2"

**Симптом:** workflow_state.json создается но `generated_offers` пусто

**Причина:**
1. pain_points_json пуст или невалиден
2. offer_filter.csv все значения = 0

**Решение:**

```python
import json
import csv

# Проверка 1: pain_points_json
print("Проверка 1: pain_points_json")
with open('data/ideas_research.csv') as f:
    reader = csv.DictReader(f)
    row = list(reader)[-1]  # Последняя строка

pain_json = row.get('pain_points_json', '')
if not pain_json or pain_json == 'NULL':
    print("❌ pain_points_json пуст - РЕШЕНИЕ: Заполните в c-02")
else:
    try:
        data = json.loads(pain_json)
        print(f"✅ pain_points_json валиден ({len(data)} углов)")
    except json.JSONDecodeError as e:
        print(f"❌ pain_points_json невалиден: {e}")

# Проверка 2: offer_filter.csv
print("\nПроверка 2: offer_filter.csv")
willing_count = 0
with open('user_preferences/offer_filter.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['willing'] == '1':
            willing_count += 1
            print(f"  ✅ {row['offer_type']}: готовы генерировать")
        else:
            print(f"  ❌ {row['offer_type']}: не готовы")

if willing_count == 0:
    print("❌ Нет типов предложений которые вы готовы генерировать")
    print("   РЕШЕНИЕ: Измените willing=1 для нужных типов в offer_filter.csv")
else:
    print(f"✅ Готовы генерировать {willing_count} типов предложений")
```

---

### Проблема D.3: "Черновики не сохраняются в posts_content.csv"

**Симптом:** После c-03e пост НЕ появляется в posts_content.csv

**Причина:** Код в c-03e не выполнил сохранение

**Решение:**

```python
import csv
import json

# Проверка 1: Есть ли workflow_state.json?
import os
if os.path.exists('.bmad/workflow_state.json'):
    with open('.bmad/workflow_state.json') as f:
        state = json.load(f)
    print(f"✅ workflow_state.json существует")
    print(f"   Текущий шаг: {state.get('current_step')}")
    print(f"   Вариантов черновиков: {len(state.get('draft_variants', []))}")

    # Проверка 2: Есть ли выбранный вариант?
    selected = [d for d in state.get('draft_variants', []) if d.get('selected')]
    if selected:
        print(f"✅ Выбранный вариант найден: {selected[0]['variant_id']}")
    else:
        print(f"❌ Нет выбранного варианта (selected: true)")
        print(f"   РЕШЕНИЕ: Отметьте один вариант как selected: true в c-03c")
else:
    print("❌ workflow_state.json не существует")
    print("   РЕШЕНИЕ: Начните с c-03b1")

# Проверка 3: Сохранен ли пост в CSV?
with open('data/posts_content.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"\nВсего постов в posts_content.csv: {len(rows)}")
if rows:
    last_post = rows[-1]
    print(f"Последний пост:")
    print(f"  ID: {last_post['id']}")
    print(f"  Title: {last_post['title'][:50]}...")
    print(f"  quality_score: {last_post.get('quality_score')}")
```

---

## РАЗДЕЛ E: Общие системные проблемы

### Проблема E.1: "Python скрипты не работают"

**Ошибка:**
```
ModuleNotFoundError: No module named 'csv'
SyntaxError: invalid syntax
```

**Решение:**

```bash
# Проверить версию Python
python --version
# Должно быть 3.8 или выше

# Проверить синтаксис скрипта
python -m py_compile scripts/migrate_csv_schema.py
# Должно работать без ошибок

# Если ошибка ModuleNotFoundError
pip install csvkit jsonschema

# Запустить скрипт с полным путём
cd _bmad/bmm/workflows/idea-to-post-pipeline
python scripts/migrate_csv_schema.py
```

---

### Проблема E.2: "Файлы в неправильной кодировке"

**Симптом:** Русские символы отображаются как ???? или иероглифы

**Причина:** CSV файл сохранен в неправильной кодировке (не UTF-8)

**Решение:**

```bash
# Проверить кодировку
file -i data/ideas_research.csv
# Должно показать: charset=utf-8

# Если не UTF-8, исправить
iconv -f ISO-8859-1 -t UTF-8 data/ideas_research.csv > temp.csv
mv temp.csv data/ideas_research.csv

# На Windows (PowerShell)
python -c "
import csv
rows = []
with open('data/ideas_research.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('data/ideas_research.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys() if rows else [])
    writer.writeheader()
    writer.writerows(rows)

print('✅ Файл переконвертирован в UTF-8')
"
```

---

## Проверочный список для диагностики

Если столкнулись с проблемой:

1. **Какая ошибка?**
   - [ ] KeyError (отсутствует столбец)
   - [ ] ValueError (неправильный тип данных)
   - [ ] JSONDecodeError (невалидный JSON)
   - [ ] FileNotFoundError (файл не существует)
   - [ ] Другое: _________________

2. **В каком файле?**
   - [ ] ideas_inbox.csv
   - [ ] ideas_research.csv
   - [ ] posts_content.csv
   - [ ] offer_filter.csv
   - [ ] workflow_state.json
   - [ ] Скрипт Python

3. **На каком шаге?**
   - [ ] c-01 (добавление идеи)
   - [ ] c-02 (исследование)
   - [ ] c-03b1 (выбор)
   - [ ] c-03b2 (предложения)
   - [ ] c-03c (черновики)
   - [ ] c-03d (улучшения)
   - [ ] c-03e (финализация)

4. **Поиск решения:**
   - [ ] Найдите номер раздела (A, B, C, D, E)
   - [ ] Найдите номер проблемы
   - [ ] Следуйте решению
   - [ ] Если не помогло, отправьте отчет об ошибке

---

## Контакты поддержки

**Если проблема не решена:**

1. Запишите:
   - Номер раздела и проблемы
   - Полный текст ошибки
   - Какой файл затронут
   - На каком шаге произошла ошибка

2. Отправьте отчет:
   ```
   Адрес: [support email]
   Тема: "Idea-to-Post Pipeline v2 - [Проблема A.1]"
   ```

3. Приложите:
   - Первые 5 строк проблемного CSV файла
   - Содержимое workflow_state.json (если применимо)
   - Вывод скрипта валидации

---

**Руководство завершено**
**Дата:** 30 января 2026
**Версия:** 1.0
**Статус:** ✅ Полное руководство по устранению неполадок
