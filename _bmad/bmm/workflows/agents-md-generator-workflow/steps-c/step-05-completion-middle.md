---
name: "step-05-completion-middle"
description: "Средний блок шага Completion: автоматизированное QA, удовлетворённость пользователя, итоговая сводка главных результатов workflow"
type: "middle"
workflow: "agents-md-generator-workflow"
bmad_menu:
  display: false
  handler: "completion"
  execution_rules: "sequential"
  redisplay: false
---

# Step 5B: [MIDDLE] — QA, Satisfaction Validation & Workflow Summary

**Назначение:** Выполнить автоматическую проверку качества, формирование отчёта удовлетворённости пользователя и генерацию итоговой сводки хода работы.

---

## Процедуры и скрипты

### 1. Качественная экспертиза (QA)

- Проверка целостности итоговых файлов (AGENTS.MD, Copilot instructions)
- Проверка структуры, размеров, наличия ключевых секций, BMAD coverage
- Формирование отчёта: `output/quality_assurance_report.md`

### 2. Валидация удовлетворённости пользователя

- Автоматизированная генерация отчёта по satisfaction, расчёт score
- Фиксация: `output/user_satisfaction_report.md`
- Критерии: KR-1…KR-10 = 100%, BMAD ≥ 95%, размеры в пределах лимита, feedback ≥ 4,5

### 3. Итоговая сводка workflow

- Генерация итогового отчёта по всем стадиям: `output/workflow_summary.md`
- Рефлексия достижений, закрытие целей, перечисление всех artefacts
- Сводный compliance matrix и status

---

## Типовые OUTPUT секции

```json
{
  "outputs": {
    "quality_assurance_report": "output/quality_assurance_report.md",
    "user_satisfaction_report": "output/user_satisfaction_report.md",
    "workflow_summary": "output/workflow_summary.md"
  }
}
```

---

### Контрольные критерии (acceptance для middle-фазы):

- [ ] Экспертиза QA заверешена без ошибок (quality_assurance_report.md)
- [ ] Итоговый satisfaction score ≥ 95% (user_satisfaction_report.md)
- [ ] Все артефакты и статус workflow зафиксированы в сводке

---

**Переход к финальной фазе**: [FINAL] — задеплоить инструкции и проверить доступность всех файлов