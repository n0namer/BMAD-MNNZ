---
name: "step-05-completion-final"
description: "Финальный блок Step 5: деплой, итоговая проверка доступности и финализация статуса workflow"
type: "final"
workflow: "agents-md-generator-workflow"
bmad_menu:
  display: false
  handler: "completion"
  execution_rules: "sequential"
  redisplay: false
---

# Step 5C: [FINAL] — Deployment, Verification & Workflow Closure

**Назначение:** Автоматизированный выпуск/деплой итоговых файлов, финальная пост-валидация готовности и фиксация “COMPLETED” статуса для всего workflow.

---

## Процедуры и инструкции

### 1. Деплой файлов и публикация

- Генерация и публикация файлов деплоя: `output/deployment_guide.md`
- Копирование финальных артефактов в целевые каталоги/репозиторий
- Контроль корректного расположения: AGENTS.MD (root), .github/copilot-instructions.md (.github/)

### 2. Финальная верификация

- Скрипты проверки целостности файлов (ls, head, grep секций)
- Финальный чек: присутствие BMAD, Copilot, 8-уровней архитектуры
- Итоговая отметка Ready for Deployment

### 3. Завершение статуса

- Вывод заключительного статуса “COMPLETED SUCCESSFULLY”
- Подготовка итоговой поддерживающей информации: куда обращаться при issue (KNOWN_ISSUES, TROUBLESHOOTING, support team)

---

## OUTPUT секция

```json
{
  "outputs": {
    "deployment_guide": "output/deployment_guide.md"
  },
  "final_status": {
    "workflow_completion": "SUCCESS",
    "compliance_status": "100%",
    "quality_status": "PASSED",
    "satisfaction_score": "100%",
    "deployment_ready": true
  }
}
```

---

## Acceptance/Checklist

- [ ] Все итоговые файлы корректно задеплоены и доступны (ls, cat, head, grep)
- [ ] deployment_guide.md сгенерирован и актуален
- [ ] Финальный статус COMPLETED SUCCESSFULLY зафиксирован
- [ ] В справочные секции добавлены KNOWN_ISSUES, support

---

**Workflow COMPLETION:** после этого шага все цели workflow считаются достигнутыми, и процесс готов к поддержке/итерациям.