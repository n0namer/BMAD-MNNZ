# Step 05: Output Format Validation Findings

## Документ и шаблон
- Основной выводной документ — `workflow-plan.md` — строится на шаблоне `templates/workflow-plan.template.md`, который имеет frontmatter с полями `stepsCompleted`, `status`, `workflowName` и свободную структуру (free-form). Это соответствует типу Free-form (progressive append) из `data/output-format-standards.md`.
- В шаблоне нет жесткой структуры, он логично разбит на разделы, и фронтматтер обеспечивает трекинг прогресса.
- Для дублей `portfolio-overview`, `project-plan`, `project-snapshot` и др. существуют соответствующие шаблоны в `templates/`, которые используются в шагах 06.5/07 и т.д., и они также удовлетворяют требованиям шаблонного формата.

## Final Polish
- Финальная полировка осуществляется шагами `step-08.*` (deep plan, final polish, etc.). Они загружают и оптимизируют итоговые файлы (workflow plan, portfolio dashboard) перед завершением.
- Эти шаги явно читают весь документ, проверяют flow и координацию секций (описано в тексте шагов), что соответствует требованию Free-form + Final Polish из стандартов.

## Step-to-output mapping
- Каждый middle-шаг содержит `workflowPlanFile` или другой `outputFile` в frontmatter и логически сохраняет результаты перед переходом дальше (см. `step-02-roles-discovery`, `step-04-consilium`, `step-06-integration`, `step-06.5`, `step-07`). Меню-опция `C` в этих шагах перечисляет сохранение документа и загрузку следующего шага.
- Финальный шаг `step-09-complete.md` не имеет `nextStepFile`, содержит сообщение об окончании, и не пытается типировать вывод — это соответствует типу Final.
- Специальные шаги (6.5, 7) сохраняют вывод в `portfolioOutputFile` и дополнительные каталоги (plan, snapshots), что соответствует кросс-ссылкам в шаблонах.

## Рекомендации
- Поддерживать текущую free-form политику и следить, чтобы новые шаги записывали `outputFile` перед переходом (как уже сделано в существующих шагах).
