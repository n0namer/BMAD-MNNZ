---
name: "step-10-evolution-init"
description: "INIT-блок эволюционного шага: frontmatter, входные критерии, статус готовности к стратегиям Future Development"
type: "init"
workflow: "agents-md-generator-workflow"
bmad_menu:
  display: true
  handler: "evolution"
  execution_rules: "sequential"
  redisplay: false
---

# Step 10A: [INIT] — Evolution Phase: Meta, Inputs & Readiness Check

**Назначение:** Запуск фазы эволюции/развития workflow, сбор необходимых state-файлов, целей и статуса readiness для start Future Development planning.

---

## Обзор  
Фаза эволюции начинается с аудита статуса исполненного workflow, сбора метрик производительности, требований к развитию и бизнес-ориентированных целей.

## Критические входы

- Полностью реализованный workflow AGENTS.MD
- Аналитика производительности, usage/feedback
- Тренды технологий и индустрии; конкуретный анализ (опционально)
- User/business requirements и стратегии будущего роста

## INPUT-секция (шаблон, формат JSON)

```json
{
  "inputs": {
    "workflow_dir": "путь_к_основному_workflow",
    "performance_analytics": "analytics/performance_data.json",
    "technology_trends": "research/technology_trends.json",
    "user_requirements": "requirements/user_requirements.json",
    "business_objectives": "strategy/business_objectives.json"
  }
}
```

---

## Acceptance/Checklist

- [ ] Все необходимые входные артефакты доступны и валидны
- [ ] Метрики и цели собраны для downstream phase
- [ ] Readiness/статус “готов к Future Development/Evolution” зафиксирован

---

**Переход к фазе**: MIDDLE — запуск построения эволюционных стратегий, feature roadmap и innovation framework.