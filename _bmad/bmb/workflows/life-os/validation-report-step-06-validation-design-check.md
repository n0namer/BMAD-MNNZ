# Step 06: Validation Design Check Findings

## Требуется ли validation?
- Сценарий Life OS связан с управлением портфелем, compliance-подходами и PDCA-отчетами → validation критична, так как выходы влияют на ресурсы, сроки и качество. Поэтому работа по шагам `steps-v/` необходима для контроля и подстраховки.

## Валидационные шаги (steps-v)
- В папке `steps-v` есть отдельные validation steps: `step-01-daily-review` (опциональный «standup»), `step-02-weekly-review`, `step-03-monthly-review`, `step-04-quarterly-review`, `step-v-06-portfolio-view` и другие. Каждый шаг:
  * Загружает данные из `data/` (например, `{weekly-pulse-protocol}`, `{monthly-review-protocol}`, `{monthly-metrics-analysis}`, `{calendar-sync-protocols}`, `{portfolio-health}` и т.п.)
  * Содержит системную последовательность (skip prompt, subprocessом формируется summary, append metrics, auto-proceed)
  * Обозначает, что validation должна быть «не ленивой» (в тексте шагов много напоминаний «это опционально, но если вы делаете — делайте аккуратно», в шаге 01 есть раздел «MANDATORY EXECUTION RULES» и пошаговые проверки)
  * Следует три-модальной структуре: валидация вынесена в `steps-v`, отдельно от `steps-c`, так что она может запуститься независимо.

## Данные для проверки
- Файлы стандартов и протоколов (например, `data/weekly-review-protocol.md`, `data/monthly-review-protocol.md`, `data/monthly-metrics-analysis.md`, `data/quarterly-review-swot.md`, `data/wip-enforcement.md`, `data/portfolio-health.md`) существуют и используются в соответствующих шагах. Валидационные шаги ссылочно подключают эти файлы и перерабатывают ключевые метрики.
- Шаги записывают результаты в `portfolioFile`/`metricsFile`, а при пропуске (например, daily review) предлагают незамедлительно перейти к weekly — то есть логика проверки соблюдена.

## Выводы
- Validation critical, и структура `steps-v` соответствует требованиям: они загружают валидационные данные, выполняют системные проверки, не импровизируют и описывают pass/fail критерии.
- Анти-ленивый тон присутствует в разделе «MANDATORY EXECUTION RULES» и последовательности, а сама папка `steps-v` отделена от create flow, что соответствует `trimodal` требованию.
- Нарушений, отсутствующих файлов или отсутствующих последовательностей не обнаружено.

## Рекомендации
- Продолжать держать `steps-v` отдельно и поддерживать базу протоколов `data/weekly-review-protocol.md`, `data/monthly-review-protocol.md` и т.п., чтоб validation всегда имела конкретные данные и не упиралась в «примерные» инструкции.
