---
name: "step-05-completion-init"
description: "Инициализационный блок завершающего шага: meta, цели и входные требования EXIT phase"
type: "init"
workflow: "agents-md-generator-workflow"
bmad_menu:
  display: true
  handler: "completion"
  execution_rules: "sequential"
  redisplay: false
---

# Step 5A: [INIT] — Completion Phase: Meta & Input Check

**Назначение:** Запуск завершающей фазы, сбор итоговых артефактов, запуск in/out traceability.  
**Роль:** Инициализация, связывание входных файлов для контроля финальных критериев.

---

## Обзор  
Завершающая стадия workflow стартует с проверки полной готовности финальных артефактов (AGENTS.MD, Copilot instructions, compliance reports) и метаданных исполнения.

## Критические входы

- AGENTS.MD и .github/copilot-instructions.md финальной версии
- Валидационные и compliance-отчёты
- Мета-данные хода исполнения (workflow_metadata)

## Шаблон INPUT секции

```json
{
  "inputs": {
    "final_files": ["output/AGENTS.MD", "output/.github/copilot-instructions.md"],
    "validation_reports": [
      "output/final_validation_report.json", 
      "output/compliance_report.md"
    ],
    "workflow_metadata": "output/workflow_summary.md"
  }
}
```

---

## Контрольные критерии (acceptance/checklist)

- [ ] Все финальные файлы присутствуют и валидны
- [ ] Исходные требования и входные отчёты доступны для downstream фаз
- [ ] Все compliance и meta-отчёты загружены для последующего анализа

---

**Переход к фазе**: [MIDDLE] — запуск QA, satisfaction и вывода