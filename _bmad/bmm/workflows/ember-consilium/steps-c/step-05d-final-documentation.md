---
name: 'step-05d-final-documentation'
description: 'Complete final documentation with alternatives analysis and solution selection'

nextStepFile: './step-06-post-decision-review.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Data references
solutionSelectionTemplates: '../data/solution-selection-templates.md'
---

# Step 5d: Final Documentation & Selection

## STEP GOAL:

To complete final documentation with comprehensive alternative options analysis, implementation readiness assessment, and formal solution selection completion.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an EMBER Consilium Analyst
- ✅ We engage in collaborative finalization, not unilateral completion
- ✅ You bring documentation frameworks and final validation
- ✅ User brings final acceptance and implementation preferences
- ✅ Together we complete comprehensive solution selection

### Step-Specific Rules:

- 🎯 Focus only on final documentation and solution selection completion
- 🚫 FORBIDDEN to provide implementation details or timelines yet
- 💬 Approach: Comprehensive documentation with all alternatives considered
- 📋 Complete solution selection with full transparency

## EXECUTION PROTOCOLS:

- 🎯 Document alternative options with detailed comparison
- 💾 Assess implementation readiness comprehensively
- 📖 Complete solution selection documentation
- 🚫 Only documentation - implementation comes next

## CONTEXT BOUNDARIES:

- Available context: Confidence synthesis and recommendation from step-5b1
- Focus: Final documentation completion with alternatives and readiness
- Limits: Do not provide implementation details or next steps
- Dependencies: Recommendation synthesis completed with confidence validation

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Synthesis Results

"**Загружаю synthesis results из предыдущего шага...**"

Load confidence synthesis from {outputFile}:
- Overall confidence calculation
- Primary recommendation synthesis
- Critical success factors identified

### 2. Document Alternative Options

"**Документирую alternative options с detailed comparison...**"

For each significant alternative from evaluation:

Secondary Option [Alternative Name]:
Comparative Analysis:
- Performance Gap: [score difference] vs primary
- Risk Differential: [risk comparison] vs primary
- Confidence Differential: [confidence comparison] vs primary
- Switching Considerations: [ease of change]
  - Time Required: [days/weeks]
  - Cost Impact: [budget impact]
- Best Applied When: [optimal use cases]
- Contingency Value: [backup plan utility]

Tertiary Option [Alternative Name]:
- Niche Applications: [specific use cases]
- Contingency Planning: [when to consider]
- Future Evolution: [technology maturity factors]

### 3. Prepare Implementation Readiness Assessment

"**Оцениваю implementation readiness для selected solution...**"

Implementation Readiness Dimensions:

Technical Readiness [score/5]:
- Infrastructure Assessment: [readiness level]
- Capabilities Assessment: [readiness level]
- Dependencies Assessment: [readiness level]

Team Readiness [score/5]:
- Skills Availability: [readiness level]
- Resource Allocation: [readiness level]
- Training Needs: [readiness level]

Organizational Readiness [score/5]:
- Change Management: [readiness level]
- Stakeholder Alignment: [readiness level]
- Process Adaptation: [readiness level]

Overall Readiness Score: [composite/5]
Readiness Level: [High/Medium/Low]
Readiness Recommended Actions: [preparation steps needed]

Implementation Monitoring Framework:
- Key Metrics: [measurement framework]
- Review Triggers: [performance thresholds]
- Review Cycle: [annual/semi-annual/quarterly]

### 4. Document Solution Selection

"**Документирую comprehensive solution selection в consilium report...**"

Update {outputFile} with final solution selection analysis:

```markdown
### Alternative Options Analysis

#### 🥈 **Secondary Option: [Alternative Name]**
**Comparative Analysis:**
- **Performance Gap:** [score_difference] vs primary
- **Risk Differential:** [risk_comparison] vs primary
- **Confidence Differential:** [confidence_comparison] vs primary
- **Switching Considerations:** [ease_of_change] - [time_required] - [cost_impact]

**Best Applied When:** [optimal_use_cases]
**Contingency Value:** [backup_plan_utility]

#### 🥉 **Tertiary Option: [Alternative Name]**
**Niche Applications:** [specific_use_cases]
**Contingency Planning:** [when_to_consider]
**Future Evolution:** [technology_maturity_factors]

### Implementation Readiness Assessment

#### Technical Readiness: [score]/5
- **Infrastructure:** [assessment] - [readiness_level]
- **Capabilities:** [assessment] - [readiness_level]
- **Dependencies:** [assessment] - [readiness_level]

#### Team Readiness: [score]/5
- **Skills Availability:** [assessment] - [readiness_level]
- **Resource Allocation:** [assessment] - [readiness_level]
- **Training Needs:** [assessment] - [readiness_level]

#### Organizational Readiness: [score]/5
- **Change Management:** [assessment] - [readiness_level]
- **Stakeholder Alignment:** [assessment] - [readiness_level]
- **Process Adaptation:** [assessment] - [readiness_level]

#### Overall Readiness Score: [composite_score]/5
**Readiness Level:** [High/Medium/Low Readiness]
**Recommended Actions:** [preparation_steps_needed]

### Decision Authority & Monitoring

#### Decision Authority
**Decision Maker:** [name/role]
**Decision Date:** [current_date]
**Review Cycle:** [frequency - annual/semi-annual/etc.]

#### Decision Monitoring Framework
**Key Metrics:** [measurement_framework]
**Review Triggers:** [performance_thresholds]
**Adjustment Protocols:** [change_management_process]

#### Documentation Archive
**Location:** [archive_path]
**Retention:** [time_period]
**Access:** [authorized_personnel]

### MCP-Enhanced Final Recommendations

**MCP Validation Summary:**
- **Technical Validation:** [MCP-verified technical feasibility score]
- **Market Intelligence:** [MCP-researched market conditions and trends]
- **Implementation Benchmarks:** [MCP-sourced implementation timelines and costs]
- **Risk Mitigation Strategies:** [MCP-identified risk patterns and solutions]

**MCP-Enhanced Confidence Score:** [Original Score + MCP Validation Boost]
**MCP Evidence Sources:** [List of MCP servers used and key insights]

### 5. Update Consilium Progress

Update {outputFile} frontmatter:
```yaml
stepsCompleted: ['step-01-problem-analysis', 'step-02-decision-block-v2', 'step-03a-evidence-collection', 'step-03b-evidence-validation', 'step-04a-matrix-setup', 'step-04b1-weighted-scoring', 'step-04b2-final-rankings', 'step-05a1-criteria-validation', 'step-05a2-decision-validation', 'step-05b1-confidence-synthesis', 'step-05b2-final-documentation']
progress: 75
currentPhase: 'solution-selection'
lastStep: 'step-05b2-final-documentation'
solutionSelected: true
finalRecommendation: '[selected_option]'
recommendationConfidence: '[confidence_score]'
```

### 6. Present MENU OPTIONS

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Implementation Planning"

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask} for deeper documentation analysis
- IF P: Execute {partyModeWorkflow} to discuss final documentation with other agents
- IF C: Save solution selection to {outputFile}, update frontmatter stepsCompleted, then only then load, read entire file, then execute {nextStepFile}
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#6-present-menu-options)

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu
- User can chat or ask questions - always respond and then end with display again of the menu options

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and solution selection is saved to {outputFile} will you then load and read fully {nextStepFile} to execute and begin implementation planning.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Alternative options properly analyzed and documented with comparisons
- Implementation readiness assessed across all dimensions comprehensively
- Solution selection documentation completed with full transparency
- Final recommendation documented with confidence scoring and rationale
- Progress updated to 75% with complete solution selection

### ❌ SYSTEM FAILURE:

- Alternative analysis inadequate or missing comparative details
- Readiness assessment incomplete or superficial
- Documentation inadequate or missing critical elements
- Recommendation transparency insufficient or incomplete

**Master Rule:** Final documentation provides complete decision record - all alternatives must be analyzed and readiness fully assessed.
