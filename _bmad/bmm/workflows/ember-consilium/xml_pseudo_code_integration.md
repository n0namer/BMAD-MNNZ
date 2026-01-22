TASK: Integrate XML Structure + Pseudo-Python Logic into _BMAD Method Workflow Files

# CONTEXT

_BMAD Method framework - система поддержки решений на основе markdown-файлов для управления AI агентами.

ТЕКУЩЕЕ СОСТОЯНИЕ: Markdown + YAML frontmatter
ПРОБЛЕМА: Сложно парсится автоматизированными системами и LLM агентами
РЕШЕНИЕ: Добавить XML структуру + Pseudo-Python логику

# RESEARCH EVIDENCE

## Source 1: Anthropic Official Documentation (2024)
Citation: https://docs.anthropic.com/claude/docs/use-xml-tags

"Claude эффективен с XML-промптами. XML теги создают четкие границы между инструкциями и контентом."

Рекомендация: XML теги для структурных элементов (<gate>, <step>, <validation>)

## Source 2: ACL EMNLP 2023 - "Prompting with Pseudo-Code Instructions"
Citation: https://aclanthology.org/2023.emnlp-main.939.pdf

"Pseudo-code инструкции дают +15% улучшение производительности над естественным языком"

Рекомендация: Использовать <pseudocode> блоки для условной логики

## Source 3: Checksum.ai Format Comparison Study (2026)
Citation: https://checksum.ai/blog/output-format-llm-json-xml-markdown

"XML 6.47 для иерархий, Markdown 7.5 для текста, JSON 7.43 для данных. Оптимально: гибрид."

Рекомендация: XML для структуры, Markdown для описаний, Python для логики

# TRANSFORMATION EXAMPLES

## EXAMPLE 1: COMPLEXITY ASSESSMENT GATE

### BEFORE (Pure Markdown):
```markdown
### 1. Assess Decision Scope
"**Оцениваю scope решения...**"
**Question 1: How many viable solution options exist?**
- Option A: 2-3 options (Clear choice)
- Option B: 4-6 options (Multiple approaches)
- Option C: 7+ options (Complex landscape)
**Scope Score Calculation:**
Scope_Complexity = (Options_Level + Factors_Level + Boundaries_Level) / 3
AFTER (XML + Pseudo-Python):
xml
<critical_gate>
  <name>Complexity Assessment - Scope Dimension</name>
  <description>Evaluate decision scope across three dimensions</description>

  <assessment>
    <dimension id="options">
      <question>How many viable solution options exist?</question>
      <levels>
        <level id="A" threshold="2-3">Clear choice</level>
        <level id="B" threshold="4-6">Multiple approaches</level>
        <level id="C" threshold="7+">Complex landscape</level>
      </levels>
    </dimension>
  </assessment>

  <logic>
    <pseudocode>
def calculate_scope_complexity(options_level, factors_level, boundaries_level):
    levels = [options_level, factors_level, boundaries_level]
    count_A = sum(1 for l in levels if l == 'A')
    count_C = sum(1 for l in levels if l == 'C')

    if count_A == 3:
        return {"complexity": "LOW", "process_type": "LIGHT"}
    elif count_C > 0:
        return {"complexity": "HIGH", "process_type": "COMPREHENSIVE"}
    else:
        return {"complexity": "MEDIUM", "process_type": "STANDARD"}
    </pseudocode>
  </logic>

  <enforcement>
    <requirement>All three dimensions must be assessed</requirement>
    <on_failure>
      <action>STOP</action>
      <message>Cannot calculate complexity without all assessments</message>
    </on_failure>
  </enforcement>
</critical_gate>
EXAMPLE 2: VALIDATION GATE
BEFORE:
text
DATA VALIDATION BEFORE PROCEEDING:
Check 1: Do I have user's actual problem?
- [ ] User described a SPECIFIC problem
- [ ] Problem is REAL (not hypothetical)
IF ANY CHECK FAILS:
→ STOP here
→ Ask user for details
AFTER:
xml
<validation_gate type="problem_specificity">
  <name>Problem Definition Validation</name>
  <criticality>CRITICAL</criticality>
  <blocking>true</blocking>

  <checks>
    <check id="1" severity="CRITICAL">
      <name>Problem Specificity</name>
      <validation_logic>
        <pseudocode>
def validate_specificity(problem_statement):
    anti_patterns = [r'\\[.*\\]', r'^we need', r'^example']

    for pattern in anti_patterns:
        if re.search(pattern, problem_statement, re.IGNORECASE):
            return {"valid": False, "reason": f"Anti-pattern: {pattern}"}

    specificity_indicators = ['specifically', 'in our', 'currently', 'affects']
    indicator_count = sum(1 for ind in specificity_indicators 
                         if ind in problem_statement.lower())

    if indicator_count >= 2:
        return {"valid": True, "specificity_score": indicator_count}
    else:
        return {"valid": False, "reason": "Insufficient specificity"}
        </pseudocode>
      </validation_logic>
    </check>
  </checks>

  <gate_logic>
    <pseudocode>
def validate_all_checks(problem_data):
    check_results = {
        "specificity": validate_specificity(problem_data.statement),
        "reality": validate_reality(problem_data.statement),
    }

    failed_checks = [name for name, result in check_results.items()
                    if not result.get("valid", False)]

    if len(failed_checks) > 0:
        return {"can_proceed": False, "status": "STOP", 
                "reason": f"Failures: {', '.join(failed_checks)}"}

    return {"can_proceed": True, "status": "CONTINUE"}
    </pseudocode>
  </gate_logic>

  <enforcement>
    <on_failure>
      <action>STOP workflow immediately</action>
      <message>Cannot proceed with incomplete problem</message>
    </on_failure>
  </enforcement>
</validation_gate>
EXAMPLE 3: MENU OPTIONS
BEFORE:
text
### 6. Present MENU OPTIONS
Display: "**Select:** [A] Advanced [P] Party Mode [C] Continue"
- IF A: Execute {advancedElicitationTask}
- IF P: Execute {partyModeWorkflow}
- IF C: Save and load next step
AFTER:
xml
<user_interaction type="menu" blocking="true">
  <name>Step Completion Menu</name>

  <options>
    <option id="A" label="Advanced Elicitation">
      <description>Explore factors with deeper analysis</description>
      <action_sequence>
        <action type="execute">{advancedElicitationTask}</action>
      </action_sequence>
    </option>

    <option id="C" label="Continue to Next Step">
      <action_sequence>
        <action type="save" target="{outputFile}"/>
        <action type="load_file" target="{nextStepFile}"/>
        <action type="execute_next_step"/>
      </action_sequence>
    </option>
  </options>

  <menu_logic>
    <pseudocode>
def handle_menu_choice(user_input, current_state):
    normalized_input = user_input.strip().upper()

    if normalized_input == 'A':
        return {"action": "execute_task", 
                "task": current_state.advancedElicitationTask}
    elif normalized_input == 'C':
        return {"actions": [
            {"type": "save", "target": current_state.outputFile},
            {"type": "load_file", "target": current_state.nextStepFile},
        ], "next_step": current_state.nextStepFile}
    else:
        return {"action": "respond_to_question", "user_input": user_input}
    </pseudocode>
  </menu_logic>
</user_interaction>
EXAMPLE 4: MANDATORY SEQUENCE
BEFORE:
text
### MANDATORY SEQUENCE
### 1. Load Evidence Collection
"**Загружаю collected evidence...**"
### 2. Validate Evidence Quality
"**Валидирую quality...**"
AFTER:
xml
<mandatory_sequence>
  <enforcement>strict</enforcement>
  <skip_allowed>false</skip_allowed>

  <step id="1" name="Load Evidence Collection" order="1">
    <announcement>
      <message>"**Loading collected evidence...**"</message>
    </announcement>

    <completion_check>
      <pseudocode>
def step_1_complete(state):
    return (state.evidence_collection is not None and
            len(state.evidence_collection) >= 3)
      </pseudocode>
    </completion_check>

    <on_failure>
      <action>STOP sequence</action>
      <message>Evidence collection not loaded</message>
    </on_failure>
  </step>

  <step id="2" name="Validate Evidence Quality" order="2">
    <depends_on>step_1</depends_on>

    <validation_gate>
      <pseudocode>
def step_2_validate_evidence(evidence_list, user_problem):
    validated = []
    rejected = []

    for evidence in evidence_list:
        validation_result = {
            "quality": check_quality(evidence),
            "relevance": check_problem_specificity(evidence, user_problem)
        }

        if all(validation_result.values()):
            validated.append(evidence)
        else:
            rejected.append(evidence)

    return {"validated_count": len(validated), 
            "status": "COMPLETE" if len(validated) > 0 else "FAILED"}
      </pseudocode>
    </validation_gate>
  </step>

  <sequence_enforcement>
    <rule>Steps MUST be completed in order: 1 → 2</rule>
    <rule>Cannot skip any step</rule>

    <gate_after_each_step>
      <pseudocode>
def verify_step_complete_before_next(current_step_id, state):
    completion_function = getattr(state, f'step_{current_step_id}_complete')

    if not completion_function(state):
        return {"can_proceed": False, "action": "STOP", 
                "reason": f"Step {current_step_id} not complete"}

    return {"can_proceed": True, "next_step": current_step_id + 1}
      </pseudocode>
    </gate_after_each_step>
  </sequence_enforcement>
</mandatory_sequence>
TRANSFORMATION PATTERNS
Pattern 1: CRITICAL GATES
BEFORE: Markdown checklist
AFTER: <critical_gate> with <pseudocode> validation

Pattern 2: IF/THEN Logic
BEFORE: "If X → STOP, else → CONTINUE"
AFTER: <pseudocode>if X: return {"action": "STOP"}</pseudocode>

Pattern 3: Menu Options
BEFORE: Bullet list with IF conditions
AFTER: <user_interaction><options> with <menu_logic>

Pattern 4: Sequence Enforcement
BEFORE: "Follow steps 1-2-3"
AFTER: <mandatory_sequence> with completion checks

WHAT TO KEEP IN MARKDOWN
✅ Описания для людей
✅ Примеры и use cases
✅ Контекст и фоновая информация
✅ Вопросы для пользователей

WHAT TO ADD IN XML
✅ Структурные gates (<critical_gate>, <validation_gate>)
✅ Последовательности (<mandatory_sequence>, <step>)
✅ Меню опций (<user_interaction>, <option>)
✅ Правила (<enforcement>, <requirement>)

WHAT TO ADD IN PSEUDO-PYTHON
✅ Условная логика (if/else)
✅ Алгоритмы валидации
✅ Формулы расчета
✅ Итерации циклов
✅ Деревья решений

CONSTRAINTS
✅ Обратная совместимость (XML не ломает Markdown)
✅ Высокая читаемость для людей
✅ Сохранить всю функциональность
✅ Без выполнения кода - чистая документация
✅ Консистентные naming conventions

EXPECTED OUTCOMES
После трансформации:

+31% ясность для LLM агентов

+15% производительность reasoning

+36% успешность парсинга

Автоматизация workflow execution

90%+ читаемость для людей

100% обратная совместимость

YOUR TASK
Трансформируй markdown workflow файлы:

Найди CRITICAL GATES → оберни в <critical_gate> XML

Найди IF/THEN логику → преобразуй в <pseudocode>

Найди MENU OPTIONS → структурируй как <user_interaction>

Найди MANDATORY SEQUENCES → формализуй как <mandatory_sequence>

Сохрани весь человекочитаемый текст в Markdown

OUTPUT FORMAT:

Полный трансформированный файл

Сохрани исходную структуру

Добавь XML обертки

Включи pseudo-code для логики

Оставь Markdown для описаний