# BMAD Skill: Add Requirements

## Skill Overview

**Purpose:** Стандартизированный процесс добавления новых требований в правильном BMAD-формате для agents-md-generator-workflow.

**Role:** Requirements Manager Agent
**Input:** Новое требование от пользователя
**Output:** Форматированный файл требования + обновленные checklists

## Skill Configuration

```yaml
name: "add-requirements"
description: "Add new requirements to agents-md-generator-workflow in BMAD-compliant format"
version: "1.0"
workflow: "agents-md-generator-workflow"
```

## Usage

### Command Format
```
/skill add-requirements [requirement_description]
```

### Parameters
- `requirement_description`: Текстовое описание нового требования
- `type`: Тип требования (FR/NFR) - определяется автоматически
- `priority`: Приоритет (обязательное по умолчанию)

## Process Flow

### Step 1: Requirement Analysis
1. **Parse Input:** Анализ описания требования
2. **Determine Type:** Автоматическое определение типа (FR/NFR)
3. **Generate ID:** Автоматическая нумерация (001, 002, 003...)

### Step 2: File Creation
1. **Create Requirement File:** Создание файла в `requirements/` с форматом:
   - `001-feature-name.md`
   - `002-performance.md`
   - и т.д.

2. **Template Structure:**
   ```markdown
   # Requirement: [ID] - [Title]
   
   ## Description
   [Detailed description]
   
   ## Type
   [FR/NFR]
   
   ## Acceptance Criteria
   - [ ] Criterion 1
   - [ ] Criterion 2
   - [ ] Criterion 3
   
   ## Integration Points
   - [Workflow integration]
   - [Dependencies]
   
   ## Priority
   [Mandatory]
   ```

### Step 3: Checklist Update
1. **Update Main Checklist:** Добавление требования в `checklist.md`
2. **Format:** `- [ ] [ID] - [Title]`
3. **Organization:** По алфавиту/нумерации

### Step 4: Integration
1. **Update PRD:** При необходимости обновление PRD-agents-md-generator.md
2. **Workflow Integration:** Связь с workflow steps
3. **Validation:** Проверка на дубликаты и конфликты

## Templates

### Requirement Template
**Path:** `templates/requirement-template.md`

### Checklist Template
**Path:** `templates/checklist-template.md`

## Examples

### Example 1: Functional Requirement
**Input:** "Need dynamic requirements loading from _bmad/implementation/2-planning/agents-md-requirements/"

**Output:** `001-dynamic-loading.md`

### Example 2: Non-Functional Requirement
**Input:** "File size must be optimized for performance"

**Output:** `002-size-optimization.md`

## Validation Rules

### Naming Convention
- Format: `[NNN]-[description].md`
- Numbers: 001, 002, 003...
- Description: lowercase, hyphens

### Content Requirements
- Description: Minimum 50 words
- Acceptance Criteria: 3-5 items
- Integration Points: Required
- Priority: Mandatory (default)

### Checklist Requirements
- Format: `- [ ] [ID] - [Title]`
- Alphabetical/numerical order
- No duplicates

## Integration with Workflow

### Workflow Steps Integration
1. **Step 01:** Requirements Loading
2. **Step 02:** Requirements Validation
3. **Step 03:** Requirements Processing

### PRD Integration
- Automatic updates to PRD-agents-md-generator.md
- Cross-references between files
- Consistency validation

## Error Handling

### Duplicate Detection
- Check for existing requirements
- Suggest modifications if duplicate found
- Prevent duplicate entries

### Format Validation
- Validate file structure
- Check template compliance
- Ensure proper naming

### Integration Validation
- Verify workflow integration
- Check PRD consistency
- Validate checklist updates

## Success Criteria

### File Creation
- [ ] Requirement file created in correct location
- [ ] File follows template format
- [ ] Proper naming convention used

### Checklist Update
- [ ] Requirement added to checklist
- [ ] Proper formatting maintained
- [ ] No duplicates introduced

### Integration
- [ ] Workflow integration verified
- [ ] PRD updated if needed
- [ ] All validation checks passed

## Usage Examples

### Basic Usage
```
/skill add-requirements "Need hybrid parallel-sequential architecture"
```

### With Type Specification
```
/skill add-requirements "File size optimization required" --type NFR
```

### Batch Processing
```
/skill add-requirements --batch requirements-list.txt
```

## Maintenance

### Regular Tasks
- Review checklist for completeness
- Validate requirement integration
- Update templates as needed

### Version Control
- Track changes to requirements
- Maintain requirement history
- Document modifications

---

**Skill Version:** 1.0
**Last Updated:** 2026-01-24
**Workflow:** agents-md-generator-workflow
**Status:** Active