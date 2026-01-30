# Проверочный список развертывания - Idea-to-Post Pipeline v2

**Тип документа:** Операционный контрольный список
**Дата:** 30 января 2026
**Версия:** 2.0
**Статус:** Готов к развертыванию

---

## Обзор

Проверочный список для гарантии того, что все компоненты v2 правильно установлены и работают перед развертыванием в production.

---

## ФАЗА 0: Предварительные проверки (30 минут)

### 0.1 Проверка окружения

- [ ] Установлен Python 3.8+
  ```bash
  python --version
  # Должно показать Python 3.8 или выше
  ```

- [ ] Установлены необходимые пакеты
  ```bash
  pip list | grep -E "csvkit|jsonschema"
  # Если нет, установить: pip install csvkit jsonschema
  ```

- [ ] Проверен доступ к файлам
  ```bash
  ls -la data/ideas_research.csv
  ls -la data/posts_content.csv
  ls -la user_preferences/offer_filter.csv
  # Все должны существовать и быть доступны для чтения
  ```

- [ ] Проверена директория .bmad
  ```bash
  mkdir -p .bmad
  chmod 755 .bmad
  # Должна быть создана и доступна для записи
  ```

### 0.2 Резервное копирование

- [ ] Создана резервная копия CSV файлов
  ```bash
  mkdir -p backups/2026-01-30
  cp data/*.csv backups/2026-01-30/
  # Должны быть скопированы все CSV файлы
  ```

- [ ] Записано местоположение резервной копии
  ```
  Резервная копия: backups/2026-01-30/
  Дата: 30 января 2026, 15:32
  ```

---

## ФАЗА 1: Миграция CSV-схемы (4 часа)

### 1.1 Миграция ideas_research.csv

- [ ] Запущен скрипт миграции
  ```bash
  python scripts/migrate_csv_schema.py
  # Должно показать: ✅ Добавлен столбец pain_points_json для N строк
  ```

- [ ] Проверена структура файла
  ```bash
  head -1 data/ideas_research.csv | tr ',' '\n' | tail -1
  # Должно показать: pain_points_json
  ```

- [ ] Проверена целостность данных
  ```bash
  python -c "
  import csv
  with open('data/ideas_research.csv') as f:
      reader = csv.DictReader(f)
      rows = list(reader)
      print(f'✅ Всего строк: {len(rows)}')
      print(f'✅ Все строки имеют pain_points_json: {all(\"pain_points_json\" in r for r in rows)}')
  "
  ```

- [ ] Проверена отсутствие потерь данных
  ```bash
  # Сравнить с резервной копией
  diff <(cut -d',' -f1-9 backups/2026-01-30/ideas_research.csv) \
       <(cut -d',' -f1-9 data/ideas_research.csv)
  # Должно быть идентично (кроме нового столбца)
  ```

### 1.2 Миграция posts_content.csv

- [ ] Запущен скрипт миграции
  ```bash
  python scripts/migrate_posts_content.py
  # Должно показать: ✅ Обновлены posts_content.csv (добавлены столбцы)
  ```

- [ ] Проверены новые столбцы
  ```bash
  head -1 data/posts_content.csv | tr ',' '\n' | grep -E "last_posted_date|variant_of|content_type|repost_count"
  # Должны быть найдены все 4 столбца
  ```

- [ ] Проверены значения по умолчанию
  ```bash
  python -c "
  import csv
  with open('data/posts_content.csv') as f:
      reader = csv.DictReader(f)
      for idx, row in enumerate(reader, 1):
          assert row['repost_count'].isdigit(), f'Row {idx}: repost_count не число'
          assert row['content_type'] in ['', 'demo', 'evergreen', 'topical'], f'Row {idx}: неверный content_type'
  print('✅ Все значения по умолчанию корректны')
  "
  ```

### 1.3 Создание user_preferences/offer_filter.csv

- [ ] Создана директория
  ```bash
  mkdir -p user_preferences
  # Должна быть создана
  ```

- [ ] Создан файл offer_filter.csv
  ```bash
  cat user_preferences/offer_filter.csv
  # Должен содержать заголовок и 5 строк (по одной для каждого типа предложения)
  ```

- [ ] Проверена структура файла
  ```bash
  head -1 user_preferences/offer_filter.csv
  # Должно показать: offer_type,willing,notes
  ```

- [ ] Проверены значения
  ```bash
  python -c "
  import csv
  with open('user_preferences/offer_filter.csv') as f:
      reader = csv.DictReader(f)
      rows = list(reader)
      types = [r['offer_type'] for r in rows]
      assert set(types) == {'training', 'setup', 'templates', 'consulting', 'full_dev'}
  print('✅ Все типы предложений присутствуют')
  "
  ```

### 1.4 Обновление .gitignore

- [ ] Проверено содержимое .gitignore
  ```bash
  grep -E "workflow_state|offer_filter" .gitignore
  # Должны быть найдены обе строки
  ```

- [ ] Проверено что файлы не версионируются
  ```bash
  git status --porcelain
  # user_preferences/offer_filter.csv НЕ должен быть в списке
  # .bmad/workflow_state.json НЕ должен быть в списке
  ```

---

## ФАЗА 2: JSON-инфраструктура (1,5 часа)

### 2.1 Создание JSON-схемы валидации

- [ ] Создан скрипт validate_workflow_state.py
  ```bash
  ls -la scripts/validate_workflow_state.py
  # Файл должен существовать и быть читаемым
  ```

- [ ] Проверен синтаксис скрипта
  ```bash
  python -m py_compile scripts/validate_workflow_state.py
  # Должен закончиться без ошибок
  ```

- [ ] Протестирована схема валидации
  ```bash
  python -c "
  from scripts.validate_workflow_state import WORKFLOW_STATE_SCHEMA
  print('✅ JSON-схема успешно загружена')
  print(f'✅ Требуемые поля: {WORKFLOW_STATE_SCHEMA[\"required\"]}')
  "
  ```

### 2.2 Документирование жизненного цикла

- [ ] Добавлено в .gitignore
  ```bash
  grep "workflow_state.json" .gitignore
  # Должно быть найдено
  ```

- [ ] Документирован процесс создания
  ```bash
  grep -A 5 "def create_workflow_state" scripts/validate_workflow_state.py
  # Должна быть функция для создания
  ```

- [ ] Документирован процесс удаления
  ```bash
  grep -A 5 "def cleanup_workflow_state" scripts/validate_workflow_state.py
  # Должна быть функция для удаления
  ```

---

## ФАЗА 3: Валидация (2 часа)

### 3.1 CSV валидация

- [ ] Запущен скрипт validate_csv_structure.py
  ```bash
  python scripts/validate_csv_structure.py
  # Должно показать: ✅ для всех файлов
  ```

- [ ] Проверены все CSV файлы
  ```bash
  # Должны быть проверены:
  # ✅ data/ideas_inbox.csv
  # ✅ data/ideas_research.csv
  # ✅ data/posts_content.csv
  # ✅ user_preferences/offer_filter.csv
  ```

### 3.2 JSON валидация

- [ ] Запущена валидация pain_points_json
  ```bash
  python scripts/test_pain_generation.py
  # Должно показать: ✅ pain_points_json serialization/deserialization works
  # Должно показать: ✅ pain_points_json structure validation works
  ```

- [ ] Запущена валидация offer_filter.csv
  ```bash
  python scripts/test_offer_filter.py
  # Должно показать: ✅ offer_filter.csv loading works
  ```

### 3.3 Интеграционное тестирование

- [ ] Пройден тест 1.1: CSV заголовки
  ```bash
  # Все требуемые столбцы должны быть найдены
  ```

- [ ] Пройден тест 1.2: Целостность данных
  ```bash
  # Все типы данных должны быть корректны
  ```

- [ ] Пройден тест 1.3: JSON-поля
  ```bash
  # Все JSON должны быть валидны
  ```

- [ ] Пройден тест 3.1: Полный цикл
  ```bash
  python TESTING-GUIDE.md (интеграционный тест)
  # Должно показать: ✅ ИНТЕГРАЦИОННЫЙ ТЕСТ ПРОЙДЕН
  ```

---

## ФАЗА 4: Проверка развертывания (30 минут)

### 4.1 Файловая система

- [ ] Все файлы на месте
  ```bash
  echo "CSV файлы:"
  ls -la data/ideas_*.csv data/posts_content.csv

  echo "Пользовательские предпочтения:"
  ls -la user_preferences/offer_filter.csv

  echo "Скрипты валидации:"
  ls -la scripts/validate_*.py scripts/test_*.py

  echo "Временная директория:"
  ls -la .bmad/
  ```

- [ ] Проверены права доступа
  ```bash
  stat data/ideas_research.csv | grep Access
  # Должны быть права для чтения и записи
  ```

### 4.2 Скрипты

- [ ] Все скрипты валидации работают
  ```bash
  python scripts/validate_csv_structure.py 2>&1 | grep -c "✅"
  # Должно быть как минимум 3 чека

  python scripts/test_pain_generation.py 2>&1 | grep -c "✅"
  # Должно быть как минимум 2 чека

  python scripts/test_offer_filter.py 2>&1 | grep -c "✅"
  # Должно быть как минимум 1 чек
  ```

### 4.3 Документация

- [ ] Все 8 документов созданы
  ```bash
  ls -la \
    IMPLEMENTATION-FIXES-SUMMARY.md \
    CSV-SCHEMA-DOCUMENTATION.md \
    JSON-WORKFLOW-STATE-DOCUMENTATION.md \
    DATA-FLOW-DIAGRAM.md \
    TESTING-GUIDE.md \
    DEPLOYMENT-CHECKLIST.md \
    QUICK-START-FOR-TEAM.md \
    TROUBLESHOOTING-GUIDE.md
  # Все файлы должны существовать
  ```

- [ ] Документация полная и понятная
  ```bash
  wc -l IMPLEMENTATION-FIXES-SUMMARY.md CSV-SCHEMA-DOCUMENTATION.md \
        JSON-WORKFLOW-STATE-DOCUMENTATION.md DATA-FLOW-DIAGRAM.md
  # Каждый файл должен быть более 100 строк
  ```

---

## ФАЗА 5: Обучение команды (1 час)

### 5.1 Подготовка материалов

- [ ] Создан QUICK-START-FOR-TEAM.md
  ```bash
  cat QUICK-START-FOR-TEAM.md | head -20
  # Должен содержать обзор изменений
  ```

- [ ] Создан TROUBLESHOOTING-GUIDE.md
  ```bash
  cat TROUBLESHOOTING-GUIDE.md | head -20
  # Должен содержать решения проблем
  ```

### 5.2 Обучение

- [ ] Команда ознакомлена с изменениями
  ```
  Методы доставки:
  ☐ Email с QUICK-START-FOR-TEAM.md
  ☐ Встреча с демонстрацией
  ☐ Документация в общем доступе
  ```

- [ ] Команда может ответить на вопросы
  ```
  Вопросы для проверки:
  ☐ Где добавляется pain_points_json?
  ☐ Когда создается workflow_state.json?
  ☐ Что происходит с workflow_state.json в конце?
  ☐ Где находится offer_filter.csv?
  ```

---

## ФАЗА 6: Финальная проверка (30 минут)

### 6.1 Тестирование в тестовой среде

- [ ] Создана тестовая идея в ideas_inbox.csv
  ```bash
  # Добавить тестовую строку с id=999
  ```

- [ ] Исследована тестовая идея
  ```bash
  # Создать ideas_research.csv запись с pain_points_json
  ```

- [ ] Проведен полный цикл создания контента
  ```bash
  # Следовать шагам c-03b1 → c-03e
  # Проверить что пост появляется в posts_content.csv
  # Проверить что workflow_state.json удален
  ```

- [ ] Проверено что контент готов к публикации
  ```bash
  tail -1 data/posts_content.csv | cut -d',' -f1,2,3,13,14
  # Должны быть видны новые столбцы с правильными значениями
  ```

### 6.2 Документация готовности

- [ ] Все чеки пройдены
  ```
  ☑️ Фаза 0: Предварительные проверки - ПРОЙДЕНО
  ☑️ Фаза 1: Миграция CSV - ПРОЙДЕНО
  ☑️ Фаза 2: JSON-инфраструктура - ПРОЙДЕНО
  ☑️ Фаза 3: Валидация - ПРОЙДЕНО
  ☑️ Фаза 4: Проверка развертывания - ПРОЙДЕНО
  ☑️ Фаза 5: Обучение команды - ПРОЙДЕНО
  ☑️ Фаза 6: Финальная проверка - ПРОЙДЕНО
  ```

- [ ] Рассчитана дата развертывания
  ```
  Дата начала: 30 января 2026
  Ожидаемая дата завершения всех фаз: [ДАТА]
  Дата развертывания в production: [ДАТА]
  ```

---

## GO/NO-GO РЕШЕНИЕ

### Критерии GO

✅ Выполнены все пункты Фазы 1-6
✅ Все тесты прошли
✅ Команда обучена
✅ Резервная копия создана
✅ Документация завершена

### Критерии NO-GO

❌ Любой тест не прошел
❌ CSV файлы содержат ошибки
❌ JSON валидация не прошла
❌ Команда не готова
❌ Документация неполная

---

## ФИНАЛЬНОЕ РЕШЕНИЕ

**Дата проверки:** _______________

**Ответственное лицо:** _______________

**Решение:**

☐ **GO** - Развертывание разрешено
☐ **NO-GO** - Требуются дополнительные исправления

**Причина (если NO-GO):**
```
_________________________________________________________________

_________________________________________________________________

_________________________________________________________________
```

**Замечания:**
```
_________________________________________________________________

_________________________________________________________________

_________________________________________________________________
```

**Подпись:** _______________

**Дата подписи:** _______________

---

## Команда развертывания

| Роль | Имя | Статус |
|------|-----|--------|
| Разработчик | _____________ | ☐ Готов |
| Тестер | _____________ | ☐ Готов |
| DevOps | _____________ | ☐ Готов |
| Product Owner | _____________ | ☐ Готов |

---

## Контакты поддержки

**Во время развертывания:**
- Главный разработчик: _____________ (_____________)
- Техническая поддержка: _____________ (_____________)
- Руководитель проекта: _____________ (_____________)

**После развертывания:**
- Support Team: _____________ (_____________)
- Documentation: _____________ (_____________)
- Bug Reports: _____________ (_____________)

---

## Приложение A: Откат в случае проблем

### Процедура отката

```bash
# 1. Остановить производство
echo "Остановить все процессы Content Machine"

# 2. Восстановить из резервной копии
cp backups/2026-01-30/*.csv data/

# 3. Удалить workflow_state.json если существует
rm -f .bmad/workflow_state.json

# 4. Проверить целостность
python scripts/validate_csv_structure.py

# 5. Возобновить производство
echo "Возобновить все процессы"
```

### Контакт в случае проблем
```
При возникновении проблем после развертывания:
1. Позвонить главному разработчику: _____________
2. Выполнить процедуру отката
3. Отправить отчет об ошибке в: _____________
```

---

**Контрольный список завершен**
**Версия:** 2.0
**Дата:** 30 января 2026
**Статус:** ✅ Готов к развертыванию
