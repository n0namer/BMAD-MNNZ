# Документация JSON Workflow State

**Тип документа:** Техническая справка
**Дата:** 30 января 2026
**Версия:** 1.0
**Статус:** Полная документация

---

## Обзор

Документация структуры и жизненного цикла `.bmad/workflow_state.json`.

Это временный файл, который хранит состояние контента во время его обработки через шаги c-03b2 → c-03e.

---

## Назначение и жизненный цикл

### Когда файл создается
- **Шаг:** c-03b2 (Генерация предложений)
- **Триггер:** Пользователь завершает выбор идеи и угла (c-03b1)
- **Действие:** Создать JSON с начальным состоянием

### Когда файл обновляется
- **Шаг:** c-03c (Создание черновиков)
- **Действие:** Добавить draft_variants в JSON
- **Шаг:** c-03d (Улучшения вариантов)
- **Действие:** Обновить draft_variants с улучшениями

### Когда файл удаляется
- **Шаг:** c-03e (Финализация)
- **Действие:** После сохранения в posts_content.csv удалить workflow_state.json
- **Причина:** Временный файл больше не нужен

---

## Полная схема

```json
{
  "session_id": "session-2026-01-30-15-32-45",
  "current_step": "c-03b2",
  "timestamp_created": "2026-01-30T15:32:45Z",
  "timestamp_updated": "2026-01-30T15:35:20Z",
  "content_type": "demo",
  "selected_idea_id": 1,
  "selected_idea_title": "Быстрая генерация документов с BMAD",
  "selected_angle": "angle_1",
  "selected_angle_name": "Масштабируемость",

  "generated_offers": [
    {
      "id": "offer-1",
      "type": "training",
      "title": "BMAD Documentation Workshop",
      "description": "2-часовой воркшоп по структурированию документов с использованием BMAD",
      "cta": "Запишись на сессию",
      "cta_url": "https://calendly.com/booking",
      "pain_solved": [
        "Медленная документация берёт 2-3 дня на большой объём",
        "Все процессы в голове у одного человека",
        "Нельзя масштабировать без найма новых специалистов"
      ],
      "effort_level": "medium",
      "estimated_price_range": "$500-1000",
      "delivery_format": "1-on-1 online session",
      "duration_hours": 2
    },
    {
      "id": "offer-2",
      "type": "templates",
      "title": "BMAD Document Templates Kit",
      "description": "Готовые шаблоны для документации всех типов",
      "cta": "Получить шаблоны",
      "cta_url": "https://example.com/templates",
      "pain_solved": [
        "Нет стандарта, каждый пишет по-своему",
        "Редактирование и проверка занимают много времени"
      ],
      "effort_level": "low",
      "estimated_price_range": "$50-150",
      "delivery_format": "Digital download",
      "duration_hours": 0.5
    }
  ],

  "draft_variants": [
    {
      "variant_id": "draft-1",
      "variant_number": 1,
      "title": "Быстрая документация с BMAD",
      "hook": "80+ документов за 2 часа?",
      "body": "Вчера за 2 часа сгенерировал 80+ документов, которые обычно занимают 2-3 дня. Вот как.",
      "cta": "Узнай мой способ →",
      "cta_type": "link",
      "selected": false,
      "platform": "linkedin",
      "improvements_applied": ["добавить цифру", "укоротить hook"],
      "quality_score": 0.85,
      "estimated_engagement": {
        "likes": 45,
        "comments": 8,
        "shares": 3
      }
    },
    {
      "variant_id": "draft-2",
      "variant_number": 2,
      "title": "Как я сэкономил 40+ часов на документации",
      "hook": "Рассказываю про инструмент, который сэкономил мне 40+ часов на документации",
      "body": "Использовал BMAD методологию. Результат: вместо 2-3 дней пишу за 2 часа.",
      "cta": "Попробуй сам →",
      "cta_type": "link",
      "selected": true,
      "platform": "twitter",
      "improvements_applied": [],
      "quality_score": 0.88,
      "estimated_engagement": {
        "likes": 52,
        "retweets": 12,
        "replies": 4
      }
    }
  ],

  "stepsCompleted": {
    "c-03b1": true,
    "c-03b2": true,
    "c-03c": false,
    "c-03d": false,
    "c-03e": false
  },

  "metadata": {
    "idea_source": "LinkedIn",
    "research_id": 1,
    "pain_points_json": {
      "angle_1": [
        "Медленная документация берёт 2-3 дня на большой объём",
        "Все процессы в голове у одного человека",
        "Нельзя масштабировать без найма новых специалистов",
        "Непроцессированная информация = нельзя продать бизнес"
      ],
      "angle_2": [
        "Качество документов зависит от того кто их написал",
        "Нет стандарта, каждый пишет по-своему",
        "Редактирование и проверка занимают много времени"
      ]
    },
    "user_preferences": {
      "willing_offers": ["training", "setup", "templates"],
      "unwilling_offers": ["consulting", "full_dev"]
    }
  }
}
```

---

## Описание основных полей

### Идентификация сеанса

| Поле | Тип | Требуемо | Описание |
|------|-----|----------|----------|
| `session_id` | STRING | ✅ | Уникальный ID сеанса. Формат: `session-YYYY-MM-DD-HH-MM-SS` |
| `timestamp_created` | STRING | ✅ | ISO 8601 момент создания файла |
| `timestamp_updated` | STRING | ❌ | ISO 8601 момент последнего обновления |

### Контекст контента

| Поле | Тип | Требуемо | Описание |
|------|-----|----------|----------|
| `current_step` | STRING | ✅ | Текущий шаг: c-03b2, c-03c, c-03d, c-03e |
| `content_type` | STRING | ✅ | Тип контента: demo, evergreen, topical, tutorial |
| `selected_idea_id` | INT | ✅ | ID идеи из ideas_inbox.csv |
| `selected_idea_title` | STRING | ✅ | Название идеи для справки |
| `selected_angle` | STRING | ✅ | Выбранный угол: angle_1, angle_2 и т.д. |
| `selected_angle_name` | STRING | ✅ | Название угла для справки |

### Сгенерированные предложения

| Поле | Тип | Требуемо | Описание |
|------|-----|----------|----------|
| `generated_offers[]` | ARRAY | ✅ | Массив предложений (создается в c-03b2) |
| `generated_offers[i].id` | STRING | ✅ | Уникальный ID предложения: offer-1, offer-2 и т.д. |
| `generated_offers[i].type` | STRING | ✅ | Тип: training, setup, templates, consulting, full_dev |
| `generated_offers[i].title` | STRING | ✅ | Название предложения (10-80 символов) |
| `generated_offers[i].description` | STRING | ❌ | Подробное описание (максимум 300 символов) |
| `generated_offers[i].cta` | STRING | ✅ | Призыв к действию (5-50 символов) |
| `generated_offers[i].cta_url` | STRING | ❌ | URL для CTA (если применимо) |
| `generated_offers[i].pain_solved[]` | ARRAY | ✅ | Какие боли решает это предложение |
| `generated_offers[i].effort_level` | STRING | ❌ | low, medium или high |
| `generated_offers[i].estimated_price_range` | STRING | ❌ | Примерный диапазон цен |
| `generated_offers[i].delivery_format` | STRING | ❌ | Формат доставки (1-on-1, group, digital и т.д.) |
| `generated_offers[i].duration_hours` | FLOAT | ❌ | Продолжительность в часах |

### Варианты черновиков

| Поле | Тип | Требуемо | Описание |
|------|-----|----------|----------|
| `draft_variants[]` | ARRAY | ✅ | Массив вариантов контента (создается в c-03c) |
| `draft_variants[i].variant_id` | STRING | ✅ | Уникальный ID: draft-1, draft-2 и т.д. |
| `draft_variants[i].variant_number` | INT | ✅ | Порядковый номер варианта |
| `draft_variants[i].title` | STRING | ✅ | Заголовок варианта (10-80 символов) |
| `draft_variants[i].hook` | STRING | ✅ | Привлекающий внимание первый момент (5-100 символов) |
| `draft_variants[i].body` | STRING | ✅ | Основной текст поста (50-500 символов) |
| `draft_variants[i].cta` | STRING | ✅ | Призыв к действию (5-50 символов) |
| `draft_variants[i].cta_type` | STRING | ❌ | Тип CTA: link, button, comment, share и т.д. |
| `draft_variants[i].selected` | BOOLEAN | ✅ | Выбран ли этот вариант для финализации |
| `draft_variants[i].platform` | STRING | ❌ | Целевая платформа: linkedin, twitter, instagram и т.д. |
| `draft_variants[i].improvements_applied[]` | ARRAY | ❌ | Какие улучшения применены в этом варианте |
| `draft_variants[i].quality_score` | FLOAT | ❌ | Оценка качества 0-1 |
| `draft_variants[i].estimated_engagement` | OBJECT | ❌ | Прогноз взаимодействия (likes, comments и т.д.) |

### Отслеживание прогресса

| Поле | Тип | Требуемо | Описание |
|------|-----|----------|----------|
| `stepsCompleted` | OBJECT | ✅ | Отслеживание завершения шагов |
| `stepsCompleted.c-03b1` | BOOL | ✅ | Выбор идеи и угла завершен? |
| `stepsCompleted.c-03b2` | BOOL | ✅ | Генерация предложений завершена? |
| `stepsCompleted.c-03c` | BOOL | ✅ | Создание черновиков завершено? |
| `stepsCompleted.c-03d` | BOOL | ✅ | Улучшения вариантов завершены? |
| `stepsCompleted.c-03e` | BOOL | ✅ | Финализация завершена? |

### Метаданные

| Поле | Тип | Требуемо | Описание |
|------|-----|----------|----------|
| `metadata` | OBJECT | ❌ | Дополнительный контекст |
| `metadata.idea_source` | STRING | ❌ | Откуда пришла идея (LinkedIn, клиент и т.д.) |
| `metadata.research_id` | INT | ❌ | Ссылка на ideas_research.csv |
| `metadata.pain_points_json` | OBJECT | ❌ | Копия pain_points_json для справки |
| `metadata.user_preferences` | OBJECT | ❌ | Скопированные предпочтения пользователя |

---

## Примеры по шагам

### После c-03b1 (выбор идеи и угла)

```json
{
  "session_id": "session-2026-01-30-15-32-45",
  "current_step": "c-03b1",
  "timestamp_created": "2026-01-30T15:32:45Z",
  "content_type": "demo",
  "selected_idea_id": 1,
  "selected_idea_title": "Быстрая генерация документов с BMAD",
  "selected_angle": "angle_1",
  "selected_angle_name": "Масштабируемость",
  "generated_offers": [],
  "draft_variants": [],
  "stepsCompleted": {
    "c-03b1": true,
    "c-03b2": false,
    "c-03c": false,
    "c-03d": false,
    "c-03e": false
  }
}
```

### После c-03b2 (генерация предложений)

```json
{
  "session_id": "session-2026-01-30-15-32-45",
  "current_step": "c-03b2",
  "timestamp_created": "2026-01-30T15:32:45Z",
  "timestamp_updated": "2026-01-30T15:35:20Z",
  "content_type": "demo",
  "selected_idea_id": 1,
  "selected_idea_title": "Быстрая генерация документов с BMAD",
  "selected_angle": "angle_1",
  "selected_angle_name": "Масштабируемость",

  "generated_offers": [
    {
      "id": "offer-1",
      "type": "training",
      "title": "BMAD Documentation Workshop",
      "cta": "Запишись на сессию",
      "pain_solved": ["Медленная документация...", "Все процессы..."],
      "effort_level": "medium",
      "estimated_price_range": "$500-1000"
    }
  ],

  "draft_variants": [],
  "stepsCompleted": {
    "c-03b1": true,
    "c-03b2": true,
    "c-03c": false,
    "c-03d": false,
    "c-03e": false
  }
}
```

### После c-03c (создание черновиков)

```json
{
  "session_id": "session-2026-01-30-15-32-45",
  "current_step": "c-03c",
  "timestamp_created": "2026-01-30T15:32:45Z",
  "timestamp_updated": "2026-01-30T15:38:10Z",

  "generated_offers": [ /* ... */ ],

  "draft_variants": [
    {
      "variant_id": "draft-1",
      "variant_number": 1,
      "title": "Быстрая документация с BMAD",
      "hook": "80+ документов за 2 часа?",
      "body": "Вчера за 2 часа сгенерировал...",
      "cta": "Узнай мой способ →",
      "selected": false,
      "quality_score": 0.85
    },
    {
      "variant_id": "draft-2",
      "variant_number": 2,
      "title": "Как я сэкономил 40+ часов на документации",
      "hook": "Рассказываю про инструмент...",
      "body": "Использовал BMAD методологию...",
      "cta": "Попробуй сам →",
      "selected": true,
      "quality_score": 0.88
    }
  ],

  "stepsCompleted": {
    "c-03b1": true,
    "c-03b2": true,
    "c-03c": true,
    "c-03d": false,
    "c-03e": false
  }
}
```

---

## Операции с JSON

### Создание в c-03b2

```python
import json
from datetime import datetime

def create_workflow_state(idea_id, idea_title, angle, angle_name, offers, content_type):
    """Создать workflow_state.json в c-03b2"""

    state = {
        "session_id": f"session-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}",
        "current_step": "c-03b2",
        "timestamp_created": datetime.now().isoformat() + "Z",
        "content_type": content_type,
        "selected_idea_id": idea_id,
        "selected_idea_title": idea_title,
        "selected_angle": angle,
        "selected_angle_name": angle_name,
        "generated_offers": offers,
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
        json.dump(state, f, ensure_ascii=False, indent=2)

    print(f"✅ Создан workflow_state.json (сеанс {state['session_id']})")
    return state
```

### Чтение в c-03c

```python
import json

def load_workflow_state():
    """Загрузить workflow_state.json в c-03c"""

    with open('.bmad/workflow_state.json', 'r', encoding='utf-8') as f:
        state = json.load(f)

    print(f"✅ Загруженны предложения: {len(state['generated_offers'])} штук")
    print(f"✅ Сеанс: {state['session_id']}")

    return state
```

### Обновление в c-03c

```python
import json

def add_draft_variants(state, variants):
    """Обновить workflow_state.json с вариантами черновиков в c-03c"""

    state['current_step'] = 'c-03c'
    state['timestamp_updated'] = datetime.now().isoformat() + "Z"
    state['draft_variants'] = variants
    state['stepsCompleted']['c-03c'] = True

    with open('.bmad/workflow_state.json', 'w', encoding='utf-8') as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

    print(f"✅ Добавлены {len(variants)} вариантов черновиков")
```

### Удаление в c-03e

```python
import os

def cleanup_workflow_state():
    """Удалить workflow_state.json после финализации в c-03e"""

    if os.path.exists('.bmad/workflow_state.json'):
        os.remove('.bmad/workflow_state.json')
        print("✅ Удален workflow_state.json (контент сохранен в posts_content.csv)")
    else:
        print("ℹ️ workflow_state.json не найден (возможно уже удален)")
```

---

## Валидация JSON

### JSON-схема

```python
from jsonschema import validate, ValidationError

WORKFLOW_STATE_SCHEMA = {
    "type": "object",
    "required": [
        "session_id",
        "current_step",
        "timestamp_created",
        "content_type",
        "selected_idea_id",
        "selected_angle",
        "generated_offers",
        "draft_variants",
        "stepsCompleted"
    ],
    "properties": {
        "session_id": {
            "type": "string",
            "pattern": "^session-\\d{4}-\\d{2}-\\d{2}-\\d{2}-\\d{2}-\\d{2}$"
        },
        "current_step": {
            "type": "string",
            "enum": ["c-03b1", "c-03b2", "c-03c", "c-03d", "c-03e"]
        },
        "timestamp_created": {"type": "string"},
        "timestamp_updated": {"type": "string"},
        "content_type": {
            "type": "string",
            "enum": ["demo", "evergreen", "topical", "tutorial"]
        },
        "selected_idea_id": {"type": "integer", "minimum": 1},
        "selected_idea_title": {"type": "string", "minLength": 5},
        "selected_angle": {"type": "string"},
        "selected_angle_name": {"type": "string"},
        "generated_offers": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "type", "title", "cta", "pain_solved"],
                "properties": {
                    "id": {"type": "string", "pattern": "^offer-\\d+$"},
                    "type": {
                        "type": "string",
                        "enum": ["training", "setup", "templates", "consulting", "full_dev"]
                    },
                    "title": {"type": "string", "minLength": 10, "maxLength": 80},
                    "description": {"type": "string", "maxLength": 300},
                    "cta": {"type": "string", "minLength": 5, "maxLength": 50},
                    "cta_url": {"type": "string", "format": "uri"},
                    "pain_solved": {
                        "type": "array",
                        "items": {"type": "string"},
                        "minItems": 1,
                        "maxItems": 5
                    },
                    "effort_level": {
                        "type": "string",
                        "enum": ["low", "medium", "high"]
                    },
                    "estimated_price_range": {"type": "string"},
                    "delivery_format": {"type": "string"},
                    "duration_hours": {"type": "number", "minimum": 0}
                }
            }
        },
        "draft_variants": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["variant_id", "variant_number", "title", "hook", "body", "cta", "selected"],
                "properties": {
                    "variant_id": {"type": "string", "pattern": "^draft-\\d+$"},
                    "variant_number": {"type": "integer", "minimum": 1},
                    "title": {"type": "string", "minLength": 10, "maxLength": 80},
                    "hook": {"type": "string", "minLength": 5, "maxLength": 100},
                    "body": {"type": "string", "minLength": 50, "maxLength": 500},
                    "cta": {"type": "string", "minLength": 5, "maxLength": 50},
                    "cta_type": {"type": "string"},
                    "selected": {"type": "boolean"},
                    "platform": {"type": "string"},
                    "improvements_applied": {"type": "array", "items": {"type": "string"}},
                    "quality_score": {"type": "number", "minimum": 0, "maximum": 1},
                    "estimated_engagement": {"type": "object"}
                }
            }
        },
        "stepsCompleted": {
            "type": "object",
            "required": ["c-03b1", "c-03b2", "c-03c", "c-03d", "c-03e"],
            "properties": {
                "c-03b1": {"type": "boolean"},
                "c-03b2": {"type": "boolean"},
                "c-03c": {"type": "boolean"},
                "c-03d": {"type": "boolean"},
                "c-03e": {"type": "boolean"}
            }
        },
        "metadata": {"type": "object"}
    }
}

def validate_workflow_state(filepath):
    """Валидировать workflow_state.json"""
    try:
        with open(filepath) as f:
            state = json.load(f)
        validate(instance=state, schema=WORKFLOW_STATE_SCHEMA)
        print(f"✅ {filepath} валиден")
        return True
    except ValidationError as e:
        print(f"❌ Ошибка валидации: {e.message}")
        return False
```

---

## Отладка и проблемы

### Проблема: Файл не создается в c-03b2

**Решение:**
```python
# Проверить права доступа
import os
if not os.path.exists('.bmad'):
    os.makedirs('.bmad')

# Проверить синтаксис JSON
import json
try:
    json.dumps(state)
except json.JSONDecodeError as e:
    print(f"❌ JSON ошибка: {e}")
```

### Проблема: Файл не обновляется в c-03c

**Решение:**
```python
# Убедиться, что файл открывается в режиме 'w' (перезапись)
with open('.bmad/workflow_state.json', 'w', encoding='utf-8') as f:
    json.dump(state, f, ensure_ascii=False, indent=2)

# Убедиться, что state правильно загружен
state = load_workflow_state()  # Проверить результат
```

### Проблема: JSON содержит невалидные значения

**Решение:**
```python
# Проверить типы данных
assert isinstance(state['selected_idea_id'], int)
assert isinstance(state['selected_angle'], str)
assert isinstance(state['generated_offers'], list)

# Проверить обязательные поля
required_fields = ['session_id', 'current_step', 'generated_offers', 'stepsCompleted']
for field in required_fields:
    assert field in state, f"Отсутствует обязательное поле: {field}"
```

---

## Проверочный список

- [ ] Файл создается в правильном месте: `.bmad/workflow_state.json`
- [ ] Файл содержит валидный JSON
- [ ] Все требуемые поля присутствуют
- [ ] session_id уникален для каждого запуска
- [ ] timestamp_created в формате ISO 8601
- [ ] Все generated_offers имеют правильный тип
- [ ] Все draft_variants имеют правильную структуру
- [ ] stepsCompleted отслеживает прогресс правильно
- [ ] Файл обновляется в c-03c
- [ ] Файл удаляется после c-03e

---

**Документация завершена**
**Дата:** 30 января 2026
**Статус:** ✅ Полная техническая документация workflow_state.json
