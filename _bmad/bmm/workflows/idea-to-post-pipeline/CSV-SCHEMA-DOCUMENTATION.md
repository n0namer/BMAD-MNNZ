# Документация CSV-схемы Idea-to-Post Pipeline

**Тип документа:** Справочная документация
**Дата:** 30 января 2026
**Версия:** 2.0
**Статус:** Полная документация

---

## Обзор

Документация по всем 5 CSV-файлам используемых в Content Machine Pipeline.

---

## 1. ideas_inbox.csv

**Назначение:** Входящая коробка для новых идей
**Место:** `data/ideas_inbox.csv`
**Использование:** Шаг c-01 (добавление идеи)

### Структура

| Столбец | Тип | Требуемо | Пример | Назначение |
|---------|-----|----------|--------|-----------|
| `id` | INT | ✅ | 1 | Уникальный идентификатор идеи |
| `date_added` | DATE | ✅ | 2026-01-30 | Дата добавления идеи |
| `source` | STRING | ✅ | Разговор с клиентом | Источник идеи |
| `raw_idea` | STRING | ✅ | "Нужен способ быстрой генерации документов" | Необработанная идея |
| `category` | STRING | ✅ | Процесс | Категория (Процесс/Инструмент/Сервис/Опыт) |
| `status` | STRING | ✅ | новая | Статус (новая/в_обработке/отклонена/завершена) |
| `notes` | STRING | ❌ | Подходит для BMAD | Дополнительные заметки |
| `idea_metadata` | JSON | ❌ | {"tags": ["bmad", "docs"]} | Дополнительные метаданные |
| `duplicate_count` | INT | ❌ | 0 | Сколько раз встречается похожая идея |
| `related_ideas` | STRING | ❌ | 5, 7, 12 | ID похожих идей через запятую |
| `content_type` | STRING | ❌ | demo | Предполагаемый тип контента |

### Правила валидации

```
✅ id: Уникальное целое число > 0
✅ date_added: Дата в формате YYYY-MM-DD
✅ source: Длина 3-100 символов
✅ raw_idea: Длина 10-500 символов
✅ category: Одно из: Процесс, Инструмент, Сервис, Опыт
✅ status: Одно из: новая, в_обработке, отклонена, завершена
✅ notes: Опционально, макс 200 символов
✅ idea_metadata: Если не пусто, то валидный JSON
✅ duplicate_count: Целое число >= 0
✅ related_ideas: Если не пусто, ID через запятую (1,2,3)
✅ content_type: Если не пусто, одно из: demo, evergreen, topical
```

### Примеры данных

**Пример 1: Простая идея**
```csv
1,2026-01-30,Разговор с клиентом,Нужен способ быстрой генерации документов,Процесс,новая,Подходит для BMAD,,,
```

**Пример 2: Идея с метаданными**
```csv
2,2026-01-28,LinkedIn,Как масштабировать документацию,Процесс,в_обработке,На основе опыта с 3 проектами,"{""tags"": [""scale"", ""docs""], ""priority"": ""high""}",0,1;3,demo
```

### Миграция данных

```python
import csv
from datetime import datetime

def migrate_ideas_inbox():
    """Добавить недостающие столбцы в ideas_inbox.csv"""

    input_file = 'data/ideas_inbox.csv'
    rows = []

    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])

        # Добавить недостающие столбцы
        new_columns = ['idea_metadata', 'duplicate_count', 'related_ideas', 'content_type']
        for col in new_columns:
            if col not in fieldnames:
                fieldnames.append(col)

        # Читать и заполнить данные
        for row in reader:
            if 'idea_metadata' not in row:
                row['idea_metadata'] = ''
            if 'duplicate_count' not in row:
                row['duplicate_count'] = '0'
            if 'related_ideas' not in row:
                row['related_ideas'] = ''
            if 'content_type' not in row:
                row['content_type'] = 'evergreen'

            rows.append(row)

    # Записать обновленный файл
    with open(input_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Обновлено {len(rows)} строк")

if __name__ == '__main__':
    migrate_ideas_inbox()
```

---

## 2. ideas_research.csv

**Назначение:** Результаты исследования идей
**Место:** `data/ideas_research.csv`
**Использование:** Шаг c-02 (исследование), c-03b1 (выбор для создания)
**Новое:** Добавлен столбец `pain_points_json` в v2

### Структура

| Столбец | Тип | Требуемо | Пример | Назначение |
|---------|-----|----------|--------|-----------|
| `id` | INT | ✅ | 1 | Уникальный ID исследования |
| `original_idea_id` | INT | ✅ | 1 | ID исходной идеи из ideas_inbox |
| `research_date` | DATE | ✅ | 2026-01-30 | Дата проведения исследования |
| `main_angle` | STRING | ✅ | Масштабируемость | Основной угол рассмотрения |
| `sub_angles_count` | INT | ✅ | 3 | Количество раскрытых углов |
| `best_angle_id` | STRING | ✅ | angle_1 | ID лучшего угла |
| `angles_list` | STRING | ✅ | angle_1;angle_2;angle_3 | Список всех углов через ; |
| `sources_count` | INT | ✅ | 5 | Количество источников |
| `avg_relevance` | FLOAT | ✅ | 0.85 | Средняя релевантность (0-1) |
| `pain_points_json` | JSON | ❌ | {"angle_1": [...], ...} | Точки боли по углам ⭐ NEW |

### Правила валидации

```
✅ id: Уникальное целое число > 0
✅ original_idea_id: Ссылается на ideas_inbox.id
✅ research_date: Дата в формате YYYY-MM-DD
✅ main_angle: Строка 5-100 символов
✅ sub_angles_count: Целое число 1-10
✅ best_angle_id: Одно из angle_1, angle_2, ..., angle_N
✅ angles_list: angle_1;angle_2;... (соответствует best_angle_id)
✅ sources_count: Целое число 1-50
✅ avg_relevance: Число 0.0-1.0
✅ pain_points_json: Если не пусто, то валидный JSON (см. формат ниже)
```

### Формат pain_points_json ⭐ NEW

```json
{
  "angle_1": [
    "Боль 1 по первому углу",
    "Боль 2 по первому углу",
    "Боль 3 по первому углу",
    "Боль 4 по первому углу"
  ],
  "angle_2": [
    "Боль 1 по второму углу",
    "Боль 2 по второму углу",
    "Боль 3 по второму углу"
  ]
}
```

**Требования:**
- Ключи должны соответствовать углам в `angles_list`
- Каждый угол должен иметь 3-5 точек боли
- Каждая точка боли - это строка 10-200 символов
- Все на русском языке
- JSON должен быть валидным и эскейпированным

### Примеры данных

**Пример 1: С pain_points_json**
```csv
1,1,2026-01-30,Масштабируемость,3,angle_1,angle_1;angle_2;angle_3,5,0.85,"{""angle_1"": [""Медленная документация берёт 2-3 дня"", ""Все процессы в голове у одного"", ""Нельзя масштабировать"", ""Непроцессированная информация = нельно продать""], ""angle_2"": [""Качество зависит от человека"", ""Нет стандарта"", ""Редактирование занимает много времени""]}"
```

**Пример 2: Без pain_points_json (NULL)**
```csv
2,2,2026-01-29,Качество,2,angle_1,angle_1;angle_2,3,0.75,
```

### Миграция данных

```python
import csv
import json

def add_pain_points_column():
    """Добавить столбец pain_points_json в ideas_research.csv"""

    input_file = 'data/ideas_research.csv'
    output_file = input_file

    rows = []
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])

        # Проверить наличие столбца
        if 'pain_points_json' not in fieldnames:
            fieldnames.append('pain_points_json')

        # Читать и заполнить данные
        for row in reader:
            if 'pain_points_json' not in row:
                row['pain_points_json'] = ''  # NULL - заполняется позже в c-02c
            rows.append(row)

    # Записать обновленный файл
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Добавлен столбец pain_points_json для {len(rows)} строк")

if __name__ == '__main__':
    add_pain_points_column()
```

---

## 3. angles_library.csv

**Назначение:** Библиотека углов для идей
**Место:** `data/angles_library.csv` (если используется)
**Использование:** Справочник для исследования (c-02c)

### Структура

| Столбец | Тип | Требуемо | Пример | Назначение |
|---------|-----|----------|--------|-----------|
| `angle_id` | STRING | ✅ | angle_1 | Уникальный ID угла |
| `idea_id` | INT | ✅ | 1 | ID исходной идеи |
| `angle_name` | STRING | ✅ | Масштабируемость | Название угла |
| `description` | STRING | ✅ | Как сделать процесс масштабируемым | Описание угла |
| `target_audience` | STRING | ✅ | Руководители отделов | Целевая аудитория |
| `keywords` | STRING | ✅ | масштаб,рост,процесс | Ключевые слова |
| `angle_type` | STRING | ❌ | проблема | Тип угла (проблема/решение/опыт) |

### Правила валидации

```
✅ angle_id: Формат angle_N где N - целое число
✅ idea_id: Ссылается на ideas_inbox.id
✅ angle_name: Строка 5-50 символов
✅ description: Строка 20-200 символов
✅ target_audience: Строка 5-100 символов
✅ keywords: Слова через запятую (2-10 слов)
✅ angle_type: Если не пусто, одно из: проблема, решение, опыт
```

---

## 4. posts_content.csv

**Назначение:** Созданный контент и посты
**Место:** `data/posts_content.csv`
**Использование:** Шаг c-03e (финализация и сохранение)
**Новое:** Добавлены 4 столбца в v2

### Структура

| Столбец | Тип | Требуемо | Пример | Назначение |
|---------|-----|----------|--------|-----------|
| `id` | INT | ✅ | 1 | Уникальный ID поста |
| `research_id` | INT | ✅ | 1 | Ссылка на ideas_research.id |
| `angle_used` | STRING | ✅ | angle_1 | Какой угол использован |
| `title` | STRING | ✅ | Быстрая документация с BMAD | Заголовок поста |
| `body` | TEXT | ✅ | Вчера за 2 часа сгенерировал 80+ документов... | Основной текст поста |
| `cta` | STRING | ✅ | Узнай как → | Призыв к действию |
| `hook` | STRING | ✅ | 80+ документов за 2 часа? | Привлекающий крючок |
| `quality_score` | FLOAT | ✅ | 0.92 | Оценка качества 0-1 |
| `created_date` | DATE | ✅ | 2026-01-30 | Дата создания |
| `publish_date` | DATE | ❌ | 2026-02-01 | Дата публикации |
| `notes` | TEXT | ❌ | Для LinkedIn | Заметки |
| `last_posted_date` | DATE | ❌ | 2026-02-05 | Дата последней публикации ⭐ NEW |
| `variant_of` | INT | ❌ | 5 | ID исходного поста если это вариант ⭐ NEW |
| `content_type` | STRING | ❌ | demo | Тип контента ⭐ NEW |
| `repost_count` | INT | ❌ | 2 | Количество переопубликаций ⭐ NEW |

### Правила валидации

```
✅ id: Уникальное целое число > 0
✅ research_id: Ссылается на ideas_research.id
✅ angle_used: Одно из angle_1, angle_2, ...
✅ title: Строка 5-200 символов
✅ body: Строка 50-5000 символов
✅ cta: Строка 5-100 символов
✅ hook: Строка 5-150 символов
✅ quality_score: Число 0.0-1.0
✅ created_date: Дата в формате YYYY-MM-DD
✅ publish_date: Опционально, дата в формате YYYY-MM-DD
✅ notes: Опционально, макс 500 символов
✅ last_posted_date: Опционально, дата в формате YYYY-MM-DD ⭐ NEW
✅ variant_of: Опционально, ссылается на posts_content.id ⭐ NEW
✅ content_type: Если не пусто, одно из: demo, evergreen, topical, tutorial ⭐ NEW
✅ repost_count: Опционально, целое число >= 0 ⭐ NEW
```

### Примеры данных

**Пример 1: Исходный пост**
```csv
1,1,angle_1,Быстрая документация с BMAD,Вчера за 2 часа сгенерировал 80+ документов...,Узнай как →,80+ документов за 2 часа?,0.92,2026-01-30,2026-02-01,Для LinkedIn,2026-02-05,,demo,0
```

**Пример 2: Вариант существующего поста**
```csv
2,1,angle_1,Документация BMAD: 2 часа вместо 2 дней,Быстро создавать качественную документацию просто...,Начни сейчас →,2 часа вместо 2 дней?,0.88,2026-01-30,2026-02-02,Вариант для Twitter,2026-02-06,1,evergreen,0
```

### Миграция данных

```python
import csv
from datetime import datetime

def add_posts_content_columns():
    """Добавить новые столбцы в posts_content.csv"""

    input_file = 'data/posts_content.csv'
    output_file = input_file

    rows = []
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])

        # Определить какие столбцы добавить
        new_columns = {
            'last_posted_date': lambda row: row.get('publish_date', datetime.now().strftime('%Y-%m-%d')),
            'variant_of': lambda row: '',
            'content_type': lambda row: 'demo' if 'demo' in row.get('notes', '').lower() else 'evergreen',
            'repost_count': lambda row: '0'
        }

        # Добавить недостающие столбцы
        for col in new_columns:
            if col not in fieldnames:
                fieldnames.append(col)

        # Читать и заполнить данные
        for row in reader:
            for col, default_fn in new_columns.items():
                if col not in row or not row[col]:
                    row[col] = default_fn(row)
            rows.append(row)

    # Записать обновленный файл
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Добавлены столбцы в posts_content.csv для {len(rows)} строк")

if __name__ == '__main__':
    add_posts_content_columns()
```

---

## 5. offer_filter.csv ⭐ NEW FILE

**Назначение:** Фильтр предложений пользователя (личные предпочтения)
**Место:** `user_preferences/offer_filter.csv`
**Использование:** Шаг c-03b2 (генерация предложений)
**Тип:** Конфигурация пользователя

### Структура

| Столбец | Тип | Требуемо | Пример | Назначение |
|---------|-----|----------|--------|-----------|
| `offer_type` | STRING | ✅ | training | Тип предложения |
| `willing` | INT | ✅ | 1 | Готов ли генерировать такие предложения (1/0) |
| `notes` | STRING | ✅ | Предлагаю 1-on-1 коучинг и менторинг | Причина включения/исключения |

### Допустимые типы предложений

```
✅ training      - Обучение, коучинг, менторинг, мастер-классы
✅ setup         - Настройка процессов, проектирование методологии
✅ templates     - Готовые шаблоны, руководства, методики
✅ consulting    - Консультирование, аудит, анализ
✅ full_dev      - Полная разработка, проектирование, реализация
```

### Правила валидации

```
✅ offer_type: Одно из: training, setup, templates, consulting, full_dev
✅ willing: Одно из: 0 (нет) или 1 (да)
✅ notes: Строка 5-200 символов (объяснение выбора)
```

### Примеры данных

**Стандартный профиль:**
```csv
offer_type,willing,notes
training,1,Предлагаю 1-on-1 коучинг и менторинг сессии
setup,1,Могу проектировать процессы и рабочие потоки для клиентов
templates,1,Есть готовые шаблоны методологии и руководства
consulting,0,Может быть позже - сейчас ограничения по времени
full_dev,0,Не могу полностью разрабатывать на текущем этапе
```

**Минимальный профиль (только основное):**
```csv
offer_type,willing,notes
training,1,Доступен для сессий
setup,0,Недостаточно опыта
templates,1,Есть шаблоны
consulting,0,Не готов
full_dev,0,Нет ресурсов
```

### Миграция данных

Этот файл создается вручную один раз и больше не меняется.

```python
def create_offer_filter():
    """Создать файл offer_filter.csv с начальными значениями"""

    import csv

    filepath = 'user_preferences/offer_filter.csv'

    # Стандартные типы предложений
    default_offers = [
        ('training', 1, 'Предлагаю 1-on-1 коучинг и менторинг сессии'),
        ('setup', 1, 'Могу проектировать процессы и рабочие потоки для клиентов'),
        ('templates', 1, 'Есть готовые шаблоны методологии и руководства'),
        ('consulting', 0, 'Может быть позже - сейчас ограничения по времени'),
        ('full_dev', 0, 'Не могу полностью разрабатывать на текущем этапе')
    ]

    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['offer_type', 'willing', 'notes'])
        writer.writerows(default_offers)

    print(f"✅ Создан файл {filepath}")

if __name__ == '__main__':
    create_offer_filter()
```

---

## Матрица зависимостей столбцов

```
ideas_inbox.csv
    └─→ id: уникальный ID идеи

ideas_research.csv
    ├─→ original_idea_id: ссылается на ideas_inbox.id
    └─→ pain_points_json: используется в c-03b2 для генерации предложений

angles_library.csv
    └─→ idea_id: ссылается на ideas_inbox.id

posts_content.csv
    ├─→ research_id: ссылается на ideas_research.id
    ├─→ variant_of: ссылается на posts_content.id (опционально)
    └─→ last_posted_date, content_type, repost_count: отслеживание жизненного цикла

offer_filter.csv (статический)
    └─→ используется для фильтрации предложений в c-03b2
```

---

## Проверочный список целостности данных

```bash
# Проверить ideas_inbox.csv
✅ id уникален
✅ date_added в формате YYYY-MM-DD
✅ status одно из: новая, в_обработке, отклонена, завершена
✅ category одна из: Процесс, Инструмент, Сервис, Опыт

# Проверить ideas_research.csv
✅ original_idea_id существует в ideas_inbox.id
✅ best_angle_id одно из: angle_1, angle_2, ...
✅ avg_relevance число между 0.0 и 1.0
✅ pain_points_json валидный JSON если не пусто

# Проверить posts_content.csv
✅ research_id существует в ideas_research.id
✅ quality_score число между 0.0 и 1.0
✅ variant_of существует в posts_content.id если указано
✅ content_type одно из: demo, evergreen, topical, tutorial

# Проверить offer_filter.csv
✅ offer_type одно из: training, setup, templates, consulting, full_dev
✅ willing одно из: 0, 1
✅ notes длина между 5 и 200 символов
```

---

## Инструменты для валидации

```python
# Использовать scripts/validate_csv_structure.py
python scripts/validate_csv_structure.py

# Использовать scripts/test_pain_generation.py
python scripts/test_pain_generation.py

# Использовать scripts/test_offer_filter.py
python scripts/test_offer_filter.py
```

---

**Документация завершена**
**Версия:** 2.0 (с новыми столбцами для v2)
**Дата:** 30 января 2026
**Статус:** ✅ Полная документация всех 5 CSV-файлов
