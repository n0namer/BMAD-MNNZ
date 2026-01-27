# AGENTS.MD Generator Workflow

**Version:** 6.0.0-alpha.23
**Created:** 2026-01-24
**Module:** BMM (BMAD software development workflows)
**Type:** Document-Producing, Continuable, Tri-Modal
**Target:** AGENTS.MD 2.0 generation with dual file architecture

## Overview

Этот workflow создает AGENTS.MD 2.0 - главный методологический и операционный манифест для LLM в репозитории. Workflow является single source of truth для BMAD-совместимой работы через GitHub Copilot Agents Tab.

## Architecture

### Flow Pattern: Branching + Looping Hybrid

**Phase 1: Initialization** (Sequential)
- Welcome user, explain the workflow
- Load BMAD requirements из `_bmad/implementation/2-planning/agents-md-requirements/`
- Gather North star description и PRD
- Initialize dual file architecture (AGENTS.MD + .github/copilot-instructions.md)

**Phase 2: Foundation Setup** (P0 - Parallel)
- Requirements Loading: Dynamic loading всех 40 FR требований
- Basic Structure Setup: 8-слойной архитектуры
- KR Requirements Parsing: 10 KR compliance requirements

**Phase 3: Content Generation** (P1 - Parallel)
- AGENTS.MD Content Generation: 8 слоев (UX, BMAD protocol, phase workflows, task templates, examples, reasoning frameworks, session monitoring, best practices)
- Copilot Instructions Generation: .github/copilot-instructions.md (~80 слов)
- Examples & Templates Creation: 5+ realistic examples, 8 parameterized /task templates
- Reasoning Frameworks Development: XML + pseudo-code structured thinking

**Phase 4: Assembly & Validation** (P2 - Sequential)
- Content Merge & Optimization: Hybrid parallel-sequential assembly
- File Size Validation & Modularization: Size limits (AGENTS.MD ≤ 100KB, Copilot Instructions ≤ 50KB)
- Final Validation & Export: 10 KR requirements compliance check

**Phase 5: Completion** (Sequential)
- Generate final AGENTS.MD и .github/copilot-instructions.md
- Quality assurance и compliance verification
- User satisfaction validation

## Configuration

### Required Tools

- **MCP Brave Search** - для real-time информации
- **Party Mode** - для collaborative generation
- **Advanced Elicitation** - для quality gates
- **Brainstorming** - для архитектуры
- **File I/O** - для создания файлов
- **Sub-Agents** - для parallel generation
- **Sub-Processes** - для parallel workflows
- **Sidecar File** - для session continuity

### Input Requirements

**Required:**
- BMAD requirements из `_bmad/implementation/2-planning/agents-md-requirements/`
- North star description
- PRD из `_bmad/implementation/2-planning/PRD-agents-md-generator.md`

**Optional:**
- Custom requirements
- Additional context

**Prerequisites:**
- BMAD Core Platform v6.0+
- GitHub Copilot Agents Tab access
- Existing AGENTS.MD для reference

### Output Specifications

**Files:**
- **AGENTS.MD** (~100 слов) - универсальный контракт для всех агентов
- **.github/copilot-instructions.md** (~80 слов) - специфично для GitHub Copilot

**Structure:**
- 8-слойная структура (UX, BMAD protocol, phase workflows, task templates, examples, reasoning frameworks, session monitoring, best practices)
- 11 разделов
- File size limits: AGENTS.MD ≤ 100KB, Copilot Instructions ≤ 50KB

## Success Criteria

**Completion Rate:** 100% KR-1 to KR-10 satisfied
**Quality Score:** 95%+ compliance с requirements
**User Satisfaction:** 4.5/5 rating от beta users
**Time to Generate:** <2 hours для full AGENTS.MD
**Maintenance Effort:** <30 minutes для requirement updates

**KR Requirements:**
- KR-1: Binary identical agents.md ↔ .github/copilot-instructions.md
- KR-2: Agents понимают BMAD phases, inputs, outputs
- KR-3: GitHub Copilot Agents Tab совместимость
- KR-4: Content preservation существующего AGENTS.MD
- KR-5: 5+ realistic example outputs
- KR-6: 8 parameterized /task templates
- KR-7: Steering guide с cost optimization
- KR-8: Agent autonomy с reasoning frameworks
- KR-9: XML + pseudo-code structured thinking
- KR-10: Advanced features validation

## Usage

### Quick Start

```bash
# Запустить workflow
claude workflow agents-md-generator-workflow

# Или через BMAD CLI
bmad workflow start agents-md-generator-workflow
```

### Session Management

**Continuable workflow:**
- Progress сохраняется в `stepsCompleted` array
- Resume через `step-01b-continue.md`
- Session continuity через Sidecar File

### Tool Integration

**MCP Brave Search:**
```bash
# Поиск BMAD documentation
brave_web_search --query "BMAD Core Platform v6.0 documentation"

# Поиск GitHub Copilot features
brave_web_search --query "GitHub Copilot Agents Tab latest features"
```

**Party Mode:**
```bash
# Collaborative generation
party_mode --phase "Content Generation" --participants "user,ai"
```

## Development

### Adding New Steps

1. Create step file in `steps-c/`, `steps-e/`, or `steps-v/`
2. Update workflow.md with new step description
3. Add step to appropriate phase
4. Update success criteria if needed

### Testing

```bash
# Тестирование workflow
bmad workflow test agents-md-generator-workflow

# Валидация output
bmad workflow validate agents-md-generator-workflow
```

### Debugging

```bash
# Debug mode
bmad workflow debug agents-md-generator-workflow --verbose

# Check progress
bmad workflow status agents-md-generator-workflow
```

## Maintenance

### Regular Updates

- **Monthly:** Review and update BMAD requirements
- **Quarterly:** Update GitHub Copilot compatibility
- **Annually:** Full compliance audit

### Version History

- **v6.0.0-alpha.23** (2026-01-24): Initial release
- **v6.0.0-alpha.24**: Planned improvements

## Support

For issues and support:
- Check `docs/KNOWN_ISSUES.md`
- Review `docs/TROUBLESHOOTING.md`
- Contact BMAD support team