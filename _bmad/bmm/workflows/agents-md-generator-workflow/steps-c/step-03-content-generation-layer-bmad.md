---
name: 'step-03-content-generation-layer-bmad'
description: 'BMAD Protocol Layer — управление фазами, спецификация входов/выходов, комплаенс'
layer: 'bmad'
menu:
  next: step-03-content-generation-layer-phase-workflows.md
  back: step-03-content-generation-layer-ux.md
handler: C
---

# Step 3: Content Generation — BMAD Protocol Layer

## Phase Management

**Phase 1: Discovery**
- Назначение: Выявить требования и ограничения
- Входы: требования пользователя, текущая документация
- Выходы: анализ требований, определение scope
- Инструменты: расширенное выяснение, мозговой штурм

**Phase 2: Planning**
- Назначение: Спроектировать архитектуру и план реализации
- Входы: результаты Discovery, требования BMAD
- Выходы: проект архитектуры, план реализации
- Инструменты: Party Mode, Sub-Agents

**Phase 3: Implementation**
- Назначение: Выполнить реализацию по плану
- Входы: результаты Planning, task templates
- Выходы: сгенерированный контент, промежуточные файлы
- Инструменты: File I/O, Sub-Processes

**Phase 4: Validation**
- Назначение: Проверить результаты и соответствие критериям BMAD
- Входы: результаты Implementation, KR требования
- Выходы: финальные файлы, compliance report
- Инструменты: фреймворки валидации, quality gates

---

## Input/Output Specification

**Обязательные входы:**
- Каталог требований BMAD
- PRD файл
- User preferences
- North star описание

**Дополнительные входы:**
- Кастомные требования
- Дополнительный контекст
- Preferences по оформлению

**Выходные файлы:**
- AGENTS.MD (~100 слов)
- .github/copilot-instructions.md (~80 слов)

**Формат выходных данных:**
- Markdown
- BMAD-структура
- Совместимость с GitHub Copilot

---

## Compliance Check

### BMAD KR Requirements

- [ ] KR-1: Binary identical files
- [ ] KR-2: BMAD phase understanding
- [ ] KR-3: GitHub Copilot compatibility
- [ ] KR-4: Content preservation
- [ ] KR-5: Realistic examples
- [ ] KR-6: Task templates
- [ ] KR-7: Steering guide
- [ ] KR-8: Agent autonomy
- [ ] KR-9: XML + pseudo-code
- [ ] KR-10: Advanced features