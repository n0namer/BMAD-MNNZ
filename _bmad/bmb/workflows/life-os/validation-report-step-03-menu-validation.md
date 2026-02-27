# Step 03: Menu Handling Validation Findings

## Методология
- Загрузили `data/menu-handling-standards.md` (запрещённые буквы, структура Display → Menu Handling → EXECUTION RULES, A/P только там, где нужно).
- Скриптом прошли по всем `steps-c/*.md` и определили, какие шаги содержат секцию `Present MENU OPTIONS`.
- Для каждого проверили: наличие заголовка `Menu Handling Logic`, наличие `EXECUTION RULES`, наличие фразы `halt and wait` (или аналога), а также упоминание `redisplay menu` для опций, отличных от `C`.
- Обнаружили 9 menu-ориентированных шагов (два варианта для `step-02`, `step-04`, `step-08.*` и по одному для `step-03`, `step-06`, `step-06.5`, `step-07`).

## Выводы
- За исключением `step-06-integration`, все меню содержат обязательные разбивки (Display, `#### Menu Handling Logic`, `#### EXECUTION RULES`), включают фразу «halt and wait» и уточняют, что A/P-опции возвращают меню.
- `step-06-integration.md` использует `**Logic:**`/`**Rules:**` вместо требуемых заголовков и не включает точную инструкцию «ALWAYS halt and wait for user input after presenting menu». Триггеры A/P и политика возвращения на меню присутствуют, однако необходимо привести формат в соответствие с `menu-handling-standards.md` (добавить `#### Menu Handling Logic:` / `#### EXECUTION RULES:` и цитировать «halt and wait»).
- Заданы альтернативные опции A/P там, где ожидаются (см. `step-02`, `step-03`, `step-04`, `step-08.*`), и все они упоминают redisplay после команды, когда это требуется.

## Рекомендации
- Переписать нижнюю часть `step-06-integration.md`, чтобы перечисленные секции использовали заголовки `#### Menu Handling Logic:` и `#### EXECUTION RULES:` и чтобы правила явно сказали «ALWAYS halt and wait for user input after presenting menu». Это устранит нарушение стандарта при следующей валидации.
