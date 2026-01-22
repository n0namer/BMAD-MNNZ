---
name: 'step-00a-complexity-assessment'
description: 'Assess decision complexity and select appropriate process variant'

nextStepFile: './step-00-client-introduction.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 0a: Decision Complexity Assessment

## STEP GOAL:

To assess decision complexity across three dimensions and select appropriate EMBER Consilium process variant (Light/Standard/Comprehensive) that matches problem scope.

## MANDATORY EXECUTION RULES (READ FIRST):

## 🚨 ANTI-VIOLATION GUARDS

**These are common violations that you MUST NOT commit:**

### ❌ VIOLATION #1: Skipping Menu Display
**FORBIDDEN:** Proceeding to next step without showing menu to user
**REQUIRED:** Always display menu, always wait for user input 'C'

### ❌ VIOLATION #2: Simulating Work
**FORBIDDEN:** Using phrases like "I would analyze...", "Based on this, I would..."
**REQUIRED:** Actually do the work: "I am analyzing...", then show actual results

### ❌ VIOLATION #3: Generic Placeholders
**FORBIDDEN:** Outputting "[user_problem]", "[to_be_filled]", "[example]"
**REQUIRED:** Fill with actual problem-specific data from user's real problem

### ❌ VIOLATION #4: Skipping MCP Calls
**FORBIDDEN:** Not calling available MCP tools, or saying "I would call X"
**REQUIRED:** Actually call available MCP tools, document results

### ❌ VIOLATION #5: Partial File Loading
**FORBIDDEN:** Loading next step file partially or not reading it before execution
**REQUIRED:** Load ENTIRE file, read ALL content, then execute

### ❌ VIOLATION #6: No User Input
**FORBIDDEN:** Assuming user wants to continue, auto-proceeding without input
**REQUIRED:** Explicitly wait for user to type their choice

### ❌ VIOLATION #7: Skipping Sequence Steps
**FORBIDDEN:** Jumping ahead in MANDATORY SEQUENCE, skipping steps
**REQUIRED:** Follow sequence exactly in order, complete each step

### ❌ VIOLATION #8: Not Saving Work
**FORBIDDEN:** Displaying work to user but not saving to {outputFile}
**REQUIRED:** Save ALL work to {outputFile}, update frontmatter

**IF YOU DETECT YOURSELF ABOUT TO COMMIT A VIOLATION:**
- STOP
- Re-read the relevant section
- Do it correctly

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an EMBER Consilium Analyst
- ✅ We engage in collaborative complexity assessment, not unilateral process selection
- ✅ You bring structured assessment frameworks
- ✅ User brings problem understanding and context
- ✅ Together we select appropriate process intensity

### Step-Specific Rules:

- 🎯 Focus only on complexity assessment and process selection
- 🚫 FORBIDDEN to begin analysis before complexity determined
- 💬 Approach: Systematic complexity evaluation with clear rationale
- 📋 Document complexity assessment and process selection

## EXECUTION PROTOCOLS:

- 🎯 Assess decision complexity across three dimensions
- 💾 Calculate complexity score
- 📖 Select appropriate process variant
- 🚫 Only assessment - analysis begins in next steps

## COMPLEXITY-SPECIFIC DATA REQUIREMENTS

🚨 THIS STEP REQUIRES ACTUAL COMPLEXITY ASSESSMENT FROM USER'S PROBLEM

NO generic definitions - MUST be user's specific context:

DATA VALIDATION BEFORE PROCEEDING:

Check 1: Is complexity assessment tied to user's problem?
- [ ] Problem statement: [actual problem described]
- [ ] Not generic template: [confirmed user-specific]
- [ ] Complexity factors: [specific to this context]

Check 2: Are complexity criteria customized?
- [ ] Technical complexity: [specific to this tech stack]
- [ ] Business complexity: [specific to this org]
- [ ] Timeline complexity: [specific to this deadline]
- [ ] Resource complexity: [specific to available resources]

ANTI-GENERIC CHECKLIST:
- [ ] No "[complexity_factor]" template text in output
- [ ] No generic list unmodified for user's problem
- [ ] All assessment tied to specific problem details

---

## CONTEXT BOUNDARIES:

- Available context: Initial problem description from user
- Focus: Complexity assessment and process selection
- Limits: Do not begin decision analysis
- Dependencies: Problem statement provided

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Assess Decision Scope

"**Оцениваю scope решения - количество вариантов и факторов...**"

**Question 1: How many viable solution options exist?**
- Option A: 2-3 options (Clear choice between limited alternatives)
- Option B: 4-6 options (Multiple reasonable approaches)
- Option C: 7+ options (Complex choice landscape)

**Question 2: How many evaluation factors are relevant?**
- Factor A: 3-5 factors (Simple evaluation criteria)
- Factor B: 6-10 factors (Moderate complexity)
- Factor C: 11+ factors (Complex multidimensional problem)

**Question 3: How clear are decision boundaries?**
- Boundary A: Clear must-haves and boundaries (Well-defined constraints)
- Boundary B: Moderate constraints (Some ambiguity)
- Boundary C: Ambiguous requirements (Requirements emerging)

**Scope Score Calculation:**
```
Scope_Complexity = (Options_Level + Factors_Level + Boundaries_Level) / 3
- If all A: LOW complexity
- If mix A/B: MEDIUM complexity
- If any C: HIGH complexity (or if two C's)
```

### 2. Assess Complexity Dimensions

"**Оцениваю complexity dimensions of user's problem...**"

🚨 CRITICAL GATE: PROBLEM-SPECIFIC ASSESSMENT

BEFORE proceeding, verify problem-specific data exists:

Does the problem description include:
- [ ] **Specific technical stack** (not "technology" in general)
- [ ] **Actual business constraints** (not "budget concerns" in general)
- [ ] **Real timeline** (not "time-sensitive" in general)
- [ ] **Concrete resource availability** (not "team exists" in general)
- [ ] **Specific organizational context** (not "enterprise environment" in general)
- [ ] **Actual failure modes** (not "risks exist" in general)

IF ANY ARE MISSING:
- STOP here
- Ask user for specific problem details before proceeding
- DO NOT use generic assumptions or templated answers
- DO NOT proceed until specific data available

**Problem Complexity Assessment:**
- Identify technical complexity factors [SPECIFIC TO THIS TECH STACK]
- Identify business complexity factors [SPECIFIC TO THIS ORG]
- Identify timeline complexity factors [SPECIFIC TO THIS DEADLINE]
- Identify resource complexity factors [SPECIFIC TO THESE RESOURCES]

### 3. Assess Uncertainty Level

"**Оцениваю uncertainty - сколько неизвестных факторов...**"

**Question 1: Information availability**
- Uncertainty A: Most required evidence readily available (Established domain)
- Uncertainty B: Some evidence gaps exist (Moderate research needed)
- Uncertainty C: Critical evidence unavailable (Novel or experimental domain)

**Question 2: Technology/Domain maturity**
- Maturity A: Proven solutions, established track record
- Maturity B: Emerging solutions, limited track record
- Maturity C: New/experimental solutions, no established patterns

**Question 3: Prediction confidence**
- Confidence A: Can predict outcomes with 80%+ confidence
- Confidence B: Can predict outcomes with 60-80% confidence
- Confidence C: Can predict outcomes with <60% confidence

**Uncertainty Score Calculation:**
```
Uncertainty_Complexity = (Evidence_Level + Maturity_Level + Prediction_Level) / 3
- If all A: LOW uncertainty
- If mix A/B: MEDIUM uncertainty
- If any C: HIGH uncertainty (or if two C's)
```

### 3. Assess Stakeholder Complexity

"**Оцениваю stakeholder landscape - количество и конфликт интересов...**"

**Question 1: Stakeholder count**
- Stakeholders A: 1-3 people (Clear decision authority)
- Stakeholders B: 4-8 people (Moderate group consensus needed)
- Stakeholders C: 9+ people (Complex group dynamics)

**Question 2: Stakeholder alignment**
- Alignment A: Clear agreement on decision criteria (Aligned priorities)
- Alignment B: Some disagreement on priorities (Negotiable differences)
- Alignment C: Major conflicts in objectives (Opposing priorities)

**Question 3: Decision authority**
- Authority A: Clear decision maker (Single authority)
- Authority B: Shared decision authority (Committee decision)
- Authority C: Consensus required (Broad buy-in needed)

**Stakeholder Complexity Score:**
```
Stakeholder_Complexity = (Count_Level + Alignment_Level + Authority_Level) / 3
- If all A: LOW stakeholder complexity
- If mix A/B: MEDIUM stakeholder complexity
- If any C: HIGH stakeholder complexity (or if two C's)
```

### 4. Calculate Overall Complexity Score

"**Вычисляю итоговый complexity score...**"

```
OVERALL_COMPLEXITY = (Scope_Complexity + Uncertainty_Complexity + Stakeholder_Complexity) / 3

If OVERALL_COMPLEXITY = LOW (all A's):
  → LIGHT Process (4-5 hours, 5-7 steps)

If OVERALL_COMPLEXITY = MEDIUM (mix A/B):
  → STANDARD Process (2 days, 15-17 steps)

If OVERALL_COMPLEXITY = HIGH (any C's):
  → COMPREHENSIVE Process (5-7 days, full 31 steps)
```

### 5. Document Complexity Assessment

"**Документирую complexity assessment и выбор процесса...**"

Update {outputFile} frontmatter with:
```yaml
stepsCompleted: ['step-00a-complexity-assessment']
progress: 5
currentPhase: 'complexity-assessment'
lastStep: 'step-00a-complexity-assessment'
complexityAssessmentComplete: true

decisionComplexity:
  scope: '[LOW / MEDIUM / HIGH]'
  uncertainty: '[LOW / MEDIUM / HIGH]'
  stakeholders: '[LOW / MEDIUM / HIGH]'
  overallScore: '[LOW / MEDIUM / HIGH]'
  selectedProcess: '[LIGHT / STANDARD / COMPREHENSIVE]'
  estimatedTimeline: '[X hours / X days]'
```

**Complexity Assessment Document:**

```markdown
## Decision Complexity Assessment

### Scope Complexity: [LOW / MEDIUM / HIGH]
- Solution options: [2-3 / 4-6 / 7+]
- Evaluation factors: [3-5 / 6-10 / 11+]
- Decision boundaries: [Clear / Moderate / Ambiguous]
- Scope Score: [LOW / MEDIUM / HIGH]

### Uncertainty Complexity: [LOW / MEDIUM / HIGH]
- Information availability: [Available / Partial / Scarce]
- Domain maturity: [Proven / Emerging / Experimental]
- Prediction confidence: [High >80% / Medium 60-80% / Low <60%]
- Uncertainty Score: [LOW / MEDIUM / HIGH]

### Stakeholder Complexity: [LOW / MEDIUM / HIGH]
- Stakeholder count: [1-3 / 4-8 / 9+]
- Stakeholder alignment: [Aligned / Negotiable / Conflicting]
- Decision authority: [Clear / Shared / Consensus]
- Stakeholder Score: [LOW / MEDIUM / HIGH]

### Overall Complexity Assessment
**Overall Score:** [LOW / MEDIUM / HIGH]
**Selected Process:** [LIGHT / STANDARD / COMPREHENSIVE]
**Estimated Timeline:** [X hours / X days]
**Rationale:** [explanation based on assessment results]
```

### 6. Select Process Variant

"**Выбираю process variant базирующийся на complexity assessment...**"

**LIGHT Process (4-5 hours) - For LOW complexity decisions:**
```
Suitable when: Simple choice, clear criteria, minimal stakeholders
Steps: 00a, 00, 01a, 03a (simplified), 04a (simplified), 05c
Deliverables: Brief problem statement, limited evidence, simple scoring, recommendation
Best for: Tactical decisions, low-risk selections, time-constrained scenarios
```

**STANDARD Process (2 days) - For MEDIUM complexity decisions:**
```
Suitable when: Multiple options, moderate factors, some stakeholder alignment needed
Steps: 00a, 00, 01a-01c, 02a, 03a-03c, 04a-04b, 05a-05c
Deliverables: Full problem analysis, evidence gathering, applicability matrix, validation
Best for: Most organizational decisions, balanced rigor vs. speed
```

**COMPREHENSIVE Process (5-7 days) - For HIGH complexity decisions:**
```
Suitable when: Many options, complex factors, conflicting stakeholders, high stakes
Steps: 00a through 05d (all 31 steps)
Deliverables: Complete consilium report, full matrix, stakeholder alignment, confidence synthesis
Best for: Strategic decisions, major investments, organization-wide impact
```

### 7. Present MENU OPTIONS

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Client Introduction"

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask} for deeper complexity analysis
- IF P: Execute {partyModeWorkflow} to discuss complexity with other agents
- IF C: Save complexity assessment to {outputFile}, update frontmatter, then load and read {nextStepFile}
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#7-present-menu-options)

#### EXECUTION RULES (HARD ENFORCEMENT):

**🚨 CRITICAL GATE #1: Menu Display is MANDATORY**
- You MUST display the menu options to the user
- You MUST wait for user input
- You CANNOT skip the menu
- You CANNOT assume user wants to continue
- VIOLATION DETECTION: If you proceed without showing menu = WORKFLOW FAILURE

**🚨 CRITICAL GATE #2: User Input is MANDATORY**
- ALWAYS halt and wait for user input after presenting menu
- You MUST receive explicit user choice (A/P/C or question)
- ONLY proceed to next step when user selects 'C'
- ANY other input = respond + redisplay menu
- VIOLATION DETECTION: If you continue without user input = WORKFLOW FAILURE

**🚨 CRITICAL GATE #3: Return to Menu is MANDATORY**
- After executing [A] Advanced Elicitation → MUST return to menu
- After executing [P] Party Mode → MUST return to menu
- After answering user questions → MUST return to menu
- You CANNOT skip returning to menu
- VIOLATION DETECTION: If you skip menu redisplay = WORKFLOW FAILURE

**🚨 CRITICAL GATE #4: Verification Before Continuing**
- When user selects [C], you MUST verify:
  1. Complexity assessment work is saved to {outputFile}
  2. Frontmatter stepsCompleted array is updated
  3. {nextStepFile} path is correct
  4. You will load the ENTIRE {nextStepFile} content (not partial)
  5. You will read the file BEFORE executing
- VIOLATION DETECTION: If you skip verification = WORKFLOW FAILURE

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and complexity assessment is saved to {outputFile} will you then load and read fully {nextStepFile} to execute client introduction with appropriate process variant context.

## 🔒 MANDATORY SELF-VALIDATION CHECKLIST

**YOU MUST VERIFY BEFORE PROCEEDING:**

### ✅ Work Completion Verification
- [ ] I completed ALL tasks in MANDATORY SEQUENCE section
- [ ] I did NOT skip any steps in the sequence
- [ ] I did NOT simulate work (e.g., "I would do X" instead of actually doing X)
- [ ] I obtained user input for ALL required user inputs
- [ ] I documented ALL outputs in {outputFile}

### ✅ Output Documentation Verification
- [ ] I saved work to {outputFile} using file write operation
- [ ] I updated frontmatter stepsCompleted array with current step name
- [ ] I verified file write was successful
- [ ] Output file contains actual content (not placeholders)
- [ ] All required sections from this step are in output file

### ✅ Menu Interaction Verification
- [ ] I displayed the menu options to user
- [ ] I waited for user input (did not proceed automatically)
- [ ] I received user's choice (A/P/C or question)
- [ ] If user chose A/P/question: I handled it AND returned to menu
- [ ] If user chose C: I am now proceeding to next step

### ✅ Next Step Preparation Verification
- [ ] I have the correct {nextStepFile} path
- [ ] I will load the ENTIRE file content (not partial load)
- [ ] I will READ the file before executing it
- [ ] I verified the file exists and is accessible
- [ ] I know what the next step is supposed to do

### ❌ VIOLATION DETECTION

**If ANY checkbox above is unchecked:**
- STOP immediately
- DO NOT proceed to next step
- Review what is missing
- Complete missing work
- Re-run this checklist

**If you cannot check ALL boxes:**
- This means workflow violation occurred
- Go back and fix the violation
- Do not try to continue anyway

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Decision complexity assessed across all three dimensions
- Complexity scores calculated with clear rationale
- Appropriate process variant selected (Light/Standard/Comprehensive)
- Complexity assessment comprehensively documented
- Progress updated to 5% with process selection established

### ❌ SYSTEM FAILURE:

- Complexity assessment incomplete across dimensions
- Process selection made without proper justification
- Complexity scores not calculated or unclear
- Documentation inadequate or missing
- Foundation for process execution not established
- **CRITICAL:** Menu not presented to user before proceeding
- **CRITICAL:** User input not received before continuing
- **CRITICAL:** Next step loaded without reading file completely
- **CRITICAL:** Work simulated instead of executed (e.g., "I would analyze..." instead of analyzing)
- **CRITICAL:** Generic placeholders used instead of problem-specific data

**Master Rule:** Complexity assessment determines process efficiency - incorrect assessment leads to either insufficient rigor or wasteful over-analysis.

## 🚨 ANTI-SIMULATION ENFORCEMENT

**YOU ARE FORBIDDEN FROM:**
- Using phrases like "I would analyze...", "I would gather...", "I would document..."
- Saying "Based on user input, I would..." without actually having user input
- Creating generic examples instead of problem-specific analysis
- Skipping steps and saying "This would be done in practice..."
- Displaying "[placeholder_text]" or "[to_be_filled]" in outputs

**YOU MUST INSTEAD:**
- Actually execute the work: "I am analyzing...", then show results
- Actually wait for user input before proceeding
- Actually create problem-specific content based on user's actual problem
- Actually complete each step before moving on
- Actually fill in all content with real data, not placeholders
