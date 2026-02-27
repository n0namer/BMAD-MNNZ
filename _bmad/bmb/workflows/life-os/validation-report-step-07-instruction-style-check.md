# Step 07: Instruction Style Findings

## Domain assessment
- Life OS — фасилитационная, кооперативная система (portfolio planning, consilium, PDCA). Это творческий/направляющий контекст, поэтому стиль должен быть intent-based по умолчанию.
- `workflow-plan.md` описывает гибкую, адаптивную архитектуру, где агенты подстраиваются под пользователя, а не диктуют точную формулировку.

## Анализ шагов
- Для каждого `steps-c/*.md` мы проверили инструкцию `MANDATORY SEQUENCE` и не нашли практик типа «Say exactly», «Ask exactly», «Read this verbatim».
- В шаге `step-06-integration` используется открытое «Ask user to confirm», «Guide them through options», а не жесткие фразы, что укладывается в intent-based категорию.
- `steps-v` (daily/weekly/monthly/quarterly reviews) формулируют вопросы свободно: «What is your focus?», «Any blockers?» и т.п., без предписаний к строгости слов.
- Никакие шаги не требуют точной формулировки ответов или последовательностей (нет «exact wording» или «mandatory script»).

## Вывод
- Инструкции во всех шагах intent-based, они описывают цели, задают открытые вопросы и позволяют адаптировать диалог.
- Для такого domain нет prescriptive разделов, и отсутствуют prescriptive шаблоны, поэтому нет тревог.

## Рекомендации
- Продолжать использовать открытые вопросы, отмеченные в `MANDATORY RULES`, и избегать добавления точных скриптов без реальной необходимости в будущем.
