---
name: 'step-03d-evidence-validation'
description: 'Evidence quality assessment and validation using credibility frameworks'

nextStepFile: './step-03e-mcp-evidence-enhancement.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Data references
evaluationCriteria: '../data/evaluation-criteria.md'
---

# Step 3d: Evidence Validation

## STEP GOAL:

To validate collected evidence quality, assess credibility and recency, and establish confidence levels for each evidence source supporting the decision analysis.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an EMBER Consilium Analyst
- ✅ We engage in collaborative evidence validation, not unilateral quality assessment
- ✅ You bring credibility assessment frameworks and validation methodologies
- ✅ User brings domain expertise and source familiarity
- ✅ Together we establish validated evidence foundation

### Step-Specific Rules:

- 🎯 Focus only on evidence validation and quality assessment
- 🚫 FORBIDDEN to make recommendations or draw conclusions yet
- 💬 Approach: Systematic quality assessment with confidence scoring
- 📋 Document validation results and credibility assessments

## EXECUTION PROTOCOLS:

- 🎯 Validate each evidence source using credibility framework
- 💾 Calculate confidence levels and quality metrics
- 📖 Complete evidence analysis for matrix evaluation
- 🚫 Only validate evidence - evaluation comes next

## CONTEXT BOUNDARIES:

- Available context: Evidence collected in step-3a
- Focus: Quality assessment, credibility validation, confidence scoring
- Limits: Do not evaluate options or make recommendations
- Dependencies: Evidence collection completed comprehensively

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 0. CRITICAL GATE: Evidence Problem-Specificity Validation

"**Validating that evidence corresponds to THIS problem, not generic...**"

🚨 CRITICAL: Evidence must be problem-specific

For each evidence piece, verify:

Check 1: Problem Specificity
- Is this evidence applicable to user's specific problem? [Yes/No]
- Does it address user's actual constraints? [Yes/No]
- Is it customized or generic? [Specific / Generic]
- If generic: Can it be applied to this problem? [Yes/No]

Check 2: Context Alignment
- User's context: [technical/business/timeline/resource specifics]
- Evidence context: [what context does this come from?]
- Alignment: [High/Medium/Low]
- If Low: Is evidence still relevant? [Yes/No]

Check 3: Temporal Validity
- Evidence date: [when collected]
- Problem timeline: [when needed]
- Is evidence current enough for this decision? [Yes/No]
- If old: How has situation changed? [analysis required]

GATE RULE:
If evidence fails problem-specificity check:
→ Flag as "contextually questionable"
→ Lower confidence score
→ Note limitation: "[Evidence limitation: generic/outdated/mismatched context]"

**Quality Assessment Criteria:**
- Source credibility [AND problem-specificity]
- Recency and relevance [TO THIS PROBLEM]
- Applicability to decision context [VERIFIED AGAINST USER CONSTRAINTS]

### 1. Load Evidence Collection

"**Loading collected evidence from previous step...**"

Load evidence collection from {outputFile}:
- Technical evidence sources
- Business evidence sources
- Operational evidence sources
- Risk evidence sources

**Validate completeness:**
- All categories represented
- Sources properly documented
- Findings systematically recorded

### 2. Validate Evidence Quality

"**Validating quality of each evidence source...**"

Load {evaluationCriteria} for validation:

**Explicit Credibility Scoring Criteria:**

**Source Credibility (1-5 scale):**
- **5/5:** Peer-reviewed research, n>100 sample size, published <1 year, multiple citations
- **4/5:** Industry research report, n>50 sample, documented methodology, <2 years old
- **3/5:** Professional publication, verified author credentials, documented sources, <3 years
- **2/5:** Blog/article by known expert, single author opinion, limited verification
- **1/5:** Anecdotal evidence, unverified source, no supporting documentation

**Evidence Recency (1-5 scale):**
- **5/5:** Published within last 6 months
- **4/5:** Published 6-12 months ago
- **3/5:** Published 1-2 years ago
- **2/5:** Published 2-3 years ago
- **1/5:** Published >3 years ago

**Information Completeness (1-5 scale):**
- **5/5:** Addresses 90-100% of decision factors
- **4/5:** Addresses 70-89% of decision factors
- **3/5:** Addresses 50-69% of decision factors
- **2/5:** Addresses 30-49% of decision factors
- **1/5:** Addresses <30% of decision factors

**Relevance to Decision (1-5 scale):**
- **5/5:** Directly applicable to exact problem context
- **4/5:** Applicable with minor adjustments
- **3/5:** Applicable to similar context, requires interpretation
- **2/5:** Tangentially related, limited applicability
- **1/5:** Marginally related, low applicability

**Quality Assessment per Source:**
- **Source Credibility:** [1-5 scale] - USE EXPLICIT CRITERIA ABOVE
- **Evidence Recency:** [1-5 scale] - USE EXPLICIT CRITERIA ABOVE
- **Information Completeness:** [1-5 scale] - USE EXPLICIT CRITERIA ABOVE
- **Relevance to Decision:** [1-5 scale] - USE EXPLICIT CRITERIA ABOVE

**Validation Process:**
- Cross-reference multiple sources
- Assess information consistency
- Evaluate source reliability
- Determine evidence strength

### 3. Document Evidence Validation

"**Documenting evidence validation results in consilium report...**"

Update {outputFile} with comprehensive evidence analysis:

```markdown
## Evidence Analysis

### Evidence Overview
**Total Sources Identified:** [count]
**Sources by Category:** [technical/business/operational/risk breakdown]
**Collection Date:** [current date]

### Technical Evidence

#### Source: [Source Name 1]
**Type:** [internal/external/expert/data]
**Credibility:** [score]/5 ([rating])
**Recency:** [score]/5 ([description])
**Completeness:** [score]/5 ([assessment])
**Relevance:** [score]/5 ([justification])

**Key Findings:** [summary of major findings]

**Source Validation:**
- Consistency with other sources: [assessment]
- Potential biases identified: [list]
- Confidence in accuracy: [high/medium/low]

#### [Additional technical sources...]

### Business Evidence

#### Source: [Business Source 1]
[... same structure as technical ...]

#### [Additional business sources...]

### Operational Evidence

#### Source: [Operational Source 1]
[... same structure as technical ...]

#### [Additional operational sources...]

### Risk Evidence

#### Source: [Risk Source 1]
[... same structure as technical ...]

#### [Additional risk sources...]

### Evidence Quality Summary

#### Overall Quality Metrics
**Average Credibility Score:** [score]/5
**Average Recency Score:** [score]/5
**Average Completeness Score:** [score]/5
**Average Relevance Score:** [score]/5

#### Quality Distribution
- **High Quality Sources (4-5):** [count] ([percentage]%)
- **Medium Quality Sources (3-4):** [count] ([percentage]%)
- **Low Quality Sources (1-2):** [count] ([percentage]%))

#### Evidence Gaps Identified
1. **[Gap Category]:** [description] - Impact: [severity] - Recommended Action: [mitigation]

#### Evidence Strength Assessment
- **Strong Evidence Areas:** [list well-supported areas]
- **Moderate Evidence Areas:** [list moderately supported areas]
- **Weak Evidence Areas:** [list poorly supported areas]

### Evidence Validation Methodology
**Cross-Reference Analysis:** [method used]
**Consistency Assessment:** [approach used]
**Bias Mitigation:** [techniques applied]
**Quality Thresholds:** [criteria used]

### Evidence Gap Analysis

**CRITICAL VALIDATION CHECK:**
For each evidence category (Technical, Business, Operational, Risk):
```
IF (source_count < 3) OR (average_credibility < 3.5) THEN
  FLAG: Evidence gap detected
  ACTION: Reduce confidence by 15% for this category
  RECOMMENDATION: Acquire additional evidence before final decision
ELSE
  PASS: Evidence sufficient for category
```

**Evidence Gap Summary:**
- Technical Evidence: [SUFFICIENT / GAP DETECTED] - [action required]
- Business Evidence: [SUFFICIENT / GAP DETECTED] - [action required]
- Operational Evidence: [SUFFICIENT / GAP DETECTED] - [action required]
- Risk Evidence: [SUFFICIENT / GAP DETECTED] - [action required]

**Overall Evidence Completeness:** [percentage]%
**Confidence Adjustment:** -[X]% due to evidence gaps
```

### 4. Update Consilium Progress

Update {outputFile} frontmatter:
```yaml
stepsCompleted: ['step-01-problem-analysis', 'step-02-decision-block-v2', 'step-03a-evidence-collection', 'step-03b-evidence-validation']
progress: 45
currentPhase: 'evidence-validation'
lastStep: 'step-03b-evidence-validation'
evidenceValidationComplete: true
```

### 5. Present MENU OPTIONS

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Matrix Setup"

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask} for deeper evidence validation
- IF P: Execute {partyModeWorkflow} to discuss evidence quality with other agents
- IF C: Save evidence validation to {outputFile}, update frontmatter stepsCompleted, then only then load, read entire file, then execute {nextStepFile}
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#5-present-menu-options)

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu
- User can chat or ask questions - always respond and then end with display again of the menu options

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and evidence validation is saved to {outputFile} will you then load and read fully {nextStepFile} to execute and begin matrix setup.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Evidence validated using credibility and quality frameworks
- Each source assessed using systematic criteria
- Quality metrics calculated and documented
- Evidence gaps identified and prioritized
- Validation results comprehensively documented in consilium report
- Progress updated to 45% with validated evidence foundation

### ❌ SYSTEM FAILURE:

- Evidence not validated using systematic criteria
- Source assessment incomplete or missing
- Quality metrics not calculated or inadequate
- Evidence gaps not identified or documented
- Validation documentation inadequate or missing

**Master Rule:** Evidence validation establishes the quality foundation for decision making - all sources must be systematically assessed and confidence-established.
