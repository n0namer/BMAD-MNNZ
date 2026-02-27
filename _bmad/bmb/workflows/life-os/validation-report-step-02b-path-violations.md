# Step 02b: Path Violations Findings

## Извлечённые config-переменные (исключения)
По разделу «Configuration Loading» из `workflow.md` и модульным конфигам определили: `{user_name}`, `{communication_language}`, `{document_output_language}`, `{bmb_creations_output_folder}`, `{output_folder}`, `{planning_artifacts}`, `{implementation_artifacts}`, `{project_knowledge}`. Пути, зависящие от этих переменных, считаются допустимыми (они указывают на пост-инсталляционные выводы).

## Контентные проверки
- Весь текст после фронтматтеров (`steps-c/e/v`) был отсканирован на `{project-root}/` шаблоны, пригодные в content (не в frontmatter). Нарушений не найдено, значит тело шагов не ссылается на абсолютные пути.

## Мёртвые ссылки из frontmatter
Автоматический парсер прошёл по всем шагам и проверил относительные пути (`./`, `../`, `data/`, `docs/` и т.п.). Найдено 5 ссылок, которые не разрешились в существующий файл:

| Файл | Переменная | Значение | Почему не найдено |
| --- | --- | --- | --- |
| `steps-c/step-08.5-final-polish.md` | `requirementsRegistry` | `../REQUIREMENTS-REGISTRY.md` | Файл `REQUIREMENTS-REGISTRY.md` отсутствует в корне workflow (нужна копия или поправить путь)
| `steps-c/step-08.8-activation-setup.md` | `activationScript` | `./scripts/create-project-from-idea.sh` | Скрипт лежит в `../scripts/`, поэтому путь должен быть `../scripts/...`, а не `./scripts/...`
| `steps-c/step-08.9-workflow-plan-polish.md` | `requirementsRegistry` | `../REQUIREMENTS-REGISTRY.md` | Аналогично: файл не найден в repo
| `steps-c/step-08.9-workflow-plan-polish.md` | `coherenceChecksRef` | `../data/workflow-plan-coherence-checks.md` | `data/workflow-plan-coherence-checks.md` отсутствует
| `steps-c/step-08b-milestone-planning.md` | `capacityRef` | `../data/foundation-examples/capacity.example.yaml` | Файл `capacity.example.yaml` не найден в `data/foundation-examples/`

В оставшихся ссылках (`steps-v/step-03-monthly-review.md` и т.п.) были использованы файлы внутри `data/` и шаблонов, они доступны, поэтому в выборке больше не фигурируют.

## Модульная осведомлённость
Поскольку workflow расположен внутри модуля `bmm`, `bmb`-специфичных путей (например, `{project-root}/_bmad/bmb/`) в `steps-v` нет, а `Steps` уже ориентируются на локальные ресурсы. Нарушений модульной осведомлённости не обнаружено.

## Рекомендации
1. Добавить или перенести `REQUIREMENTS-REGISTRY.md` в корень workflow или поправить ссылки на существующий файл.
2. Подправить `activationScript` в `step-08.8` так, чтобы путь указывал на `../scripts/create-project-from-idea.sh` (реальный путь).
3. Создать `data/workflow-plan-coherence-checks.md` и `data/foundation-examples/capacity.example.yaml` или использовать другие файлы, которые уже существуют.
