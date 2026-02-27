---
validationDate: 2026-02-09
workflowName: Life OS Docs Validation
workflowPath: D:/Users/NIKITA/Documents/DEV/BMAD-MNNZ/_bmad/bmm/workflows/life-os
validationStatus: COMPLETE
completionDate: 2026-02-09
---

# Validation Report: Life OS Docs Validation

**Validation Started:** 2026-02-09 01:10:29
**Validator:** BMAD Workflow Validation System
**Standards Version:** BMAD Workflow Standards

## Contents
- [step-01b-structure (File Structure & Size)](#step-01b-structure-file-structure--size)
- [step-02-frontmatter-validation](#step-02-frontmatter-validation)
- [step-02b-path-violations](#step-02b-path-violations)
- [step-03-menu-validation](#step-03-menu-validation)
- [step-04-step-type-validation](#step-04-step-type-validation)
- [step-05-output-format-validation](#step-05-output-format-validation)
- [step-06-validation-design-check](#step-06-validation-design-check)
- [step-07-instruction-style-check](#step-07-instruction-style-check)
- [step-08-collaborative-experience-check](#step-08-collaborative-experience-check)
- [step-08b-subprocess-optimization](#step-08b-subprocess-optimization)
- [step-09-cohesive-review](#step-09-cohesive-review)

## step-01b-structure (File Structure & Size)
Подробный анализ структуры и размеров находится в validation-report-step-01b-structure.md. Проверены каталоги workflow.md, steps-c/e/v/x, docs и supporting folders, плюс вычислены длины всех step-файлов. Превышают лимит (>250 строк): step-00-goals-discovery, step-00.5-project-stage, step-00.7-optimization-intelligence, step-05-scoring.

## step-02-frontmatter-validation
Верифицировано по правилам data/frontmatter-standards.md: скриптом просмотрены все steps-c/e/v, запрещённые шаблоны workflow_path, 	hisStepFile, workflowFile отсутствуют, переменные используются через {variable} или служебно нужны шаблону. Детали: validation-report-step-02-frontmatter-validation.md.

## step-02b-path-violations
Проверили редакции контента и frontmatter-ссылки; {project-root}/ в теле отсутствуют, но в steps-c обнаружены 5 dead-link ссылок (requirementsRegistry → ../REQUIREMENTS-REGISTRY.md, activationScript → ./scripts/create-project-from-idea.sh, coherenceChecksRef → ../data/workflow-plan-coherence-checks.md, capacityRef → ../data/foundation-examples/capacity.example.yaml). Детали — validation-report-step-02b-path-violations.md.

## step-03-menu-validation
Проверили меню всех шагов steps-c: все команды Present MENU OPTIONS содержат Handler + EXECUTION RULES, halt and wait и указание redisplay, за исключением step-06-integration, где используется **Logic:**/Rules:** вместо стандартных заголовков и отсутствует точная формулировка ALWAYS halt and wait.... Подробности и рекомендации — validation-report-step-03-menu-validation.md.

## step-04-step-type-validation
Сопоставили каждый step c doc workflow-plan.md и шаблонами из data/step-type-patterns.md: init/continuation-шага (step-00/01), middle-шага (step-02...step-07), final polish (step-08.*) и финального шага (step-09) реализованы в соответствии с ожидаемым паттерном. Все шаги выводят нужные menus/handler/execution rules и, кроме step-09, указывают 
extStepFile. См. validation-report-step-04-step-type-validation.md.

## step-05-output-format-validation
Проверили шаблон 	emplates/workflow-plan.template.md и финальные полировки step-08.*; все step-выводы записываются в workflowPlanFile/portfolioOutputFile, а финальный шаг step-09 не содержит 
extStepFile. Подробно: validation-report-step-05-output-format-validation.md.

## step-06-validation-design-check
Validation критична (портфель, PDCA, качества) и реализована в отдельной папке steps-v (daily/weekly/monthly/quarterly reviews). Каждый step загружает данные из data/, выполняет системные проверки и содержит явные execution rules, а анти-ленивый тон положен в mandatory rules. Детали — validation-report-step-06-validation-design-check.md.

## step-07-instruction-style-check
Life OS — intent-based/фасилитационное окружение, и инструкции всех steps-c/steps-v описаны гибко (вопросы, цели, guidance) без prescriptive паттернов как Say exactly или Ask exactly. Детали в validation-report-step-07-instruction-style-check.md.

## step-08-collaborative-experience-check
Все steps-c ведут диалогово: 1-2 вопроса, фасилитация, явное подтверждение (пример: step-02, step-07, step-08.*). Нет laundry list или form-filling; поток построен по этапам. Подробно — validation-report-step-08-collaborative-experience-check.md.

## step-08b-subprocess-optimization
Проверили subprocess-паттерны: single g для {project-root}/, per-file deep analysis (меню/учёта типов/стиля), data-операции (dead links) и рекомендации по параллельности. См. validation-report-step-08b-subprocess-optimization.md.

## step-09-cohesive-review
Весь workflow читается последовательно: discovery → consilium → integration → calendar → polish → validation. Голос, цели и завершение согласованы; единственные замечания — недостающие файлы из Step 02b и Handler/Rules в step-06. Общая рекомендация — GOOD/READY. Подробности — validation-report-step-09-cohesive-review.md.












## Summary
- Overall status: ⚠️ WARN — структура последовательна, но есть несколько критичных недочётов (см. Step 02b и Step 03).
- Critical issues: отсутствуют файлы REQUIREMENTS-REGISTRY.md, data/workflow-plan-coherence-checks.md, data/foundation-examples/capacity.example.yaml, и путь step-08.8 указывает на ./scripts/create-project-from-idea.sh вместо ../scripts/...; а также step-06-integration не соответствует menu-handling-standards без явных Menu Handling Logic/EXECUTION RULES и фразы «halt and wait». Эта информация подтверждена в validation-report-step-02b-path-violations.md и validation-report-step-03-menu-validation.md.
- Next steps: добавьте недостающие файлы или обновите ссылки, выровняйте step-06 меню по стандарту, рефакторьте сверхдлинные step-файлы по желанию, затем обновите status в отчёте и снова запустите Step 10 (см. validation-report-step-10-report-complete.md для итоговой структуры).

