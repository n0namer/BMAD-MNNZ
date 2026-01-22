---
name: 'step-06-post-decision-review'
description: 'Conduct post-decision review and learning feedback loop'

outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'
reviewDate: 'T+30/60/90 days'

# Data references
confidenceCriteria: '../data/confidence-criteria.md'
---

# Step 06: Post-Decision Review & Learning Feedback

## STEP GOAL:

To conduct post-decision learning review, calibrate confidence thresholds, and improve future decision frameworks based on actual outcome vs. predicted outcome.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an EMBER Consilium Analyst
- ✅ We engage in collaborative learning review, not unilateral judgment
- ✅ You bring structured review frameworks and calibration methodology
- ✅ User brings real outcomes and implementation insights
- ✅ Together we extract learning to improve future decisions

### Step-Specific Rules:

- 🎯 Focus only on learning and framework improvement
- 🚫 FORBIDDEN to make excuses or rationalize poor recommendations
- 💬 Approach: Honest outcome assessment and systematic learning
- 📋 Document learning for organizational knowledge base

### Honest Outcome Assessment (Проблема #20)

**FORBIDDEN BEHAVIORS:**
- ❌ Rationalizing poor predictions as "unforeseeable circumstances"
- ❌ Blaming external factors rather than framework limitations
- ❌ Overstating partial successes as complete wins
- ❌ Ignoring evidence of systematic bias in decision-making

**REQUIRED APPROACH:**
- ✅ Honestly assess what actually drove success/failure
- ✅ Identify when framework predictions were systematically wrong
- ✅ Document specific ways the decision process could be improved
- ✅ Extract learning that will prevent similar issues in future decisions

## EXECUTION PROTOCOLS:

- 🎯 Compare predicted outcomes to actual results
- 💾 Assess which factors actually drove success/failure
- 📖 Calibrate confidence scoring for future decisions
- 🚫 Only learning - do not retry decision or blame factors

## CONTEXT BOUNDARIES:

- Available context: Original decision recommendation and confidence scores
- Focus: Outcome assessment and learning extraction
- Timeline: 30 days (quick feedback), 60 days (mid-term), 90 days (comprehensive)
- Dependencies: Decision implemented and outcomes observable

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Original Decision Documentation

"**Загружаю оригинальное decision recommendation и predicted outcomes...**"

From {outputFile} retrieve:
- **Recommended Solution:** [Option name]
- **Predicted Value:** [quantitative expectation]
- **Predicted Risks:** [expected failure modes]
- **Confidence Level:** [original 0.0-1.0 score]
- **Critical Success Factors:** [factors predicted to drive success]
- **Key Assumptions:** [assumptions underlying recommendation]

### 2. Assess Actual Outcomes (30/60/90 Day Review)

"**Оцениваю actual outcomes сравнивая с predictions...**"

**Review Timeframe Selection:**
- **Day 30 (Quick Feedback):** Early signs, implementation quality, quick wins/failures
- **Day 60 (Mid-term):** Trend establishment, user adoption, integration issues
- **Day 90 (Comprehensive):** Full impact assessment, risk realization, value delivery

**Outcome Assessment:**

```markdown
## Predicted vs. Actual Comparison

### Value Delivery
**Predicted Value:** [quantitative metric] (Confidence: [X]%)
**Actual Value (at Day X):** [measured result]
**Variance:** [+/- percentage]
**Status:** [Exceeded / Met / Underperformed / Failed]

### Risk Realization
**Predicted Risks:** [list of expected failure modes]
- Risk A: Predicted probability [X]% → Actual: [occurred/did not occur]
- Risk B: Predicted probability [X]% → Actual: [occurred/did not occur]
- Risk C: Predicted probability [X]% → Actual: [occurred/did not occur]

**Unexpected Risks Encountered:**
- Risk X: [description of unanticipated problem]
- Risk Y: [description of unanticipated problem]

### Critical Success Factors - Actual Importance
**Predicted Critical Factors:** [from original analysis]
- Factor A (predicted weight X%): Actual importance [actually was critical / minor / irrelevant]
- Factor B (predicted weight X%): Actual importance [actually was critical / minor / irrelevant]
- Factor C (predicted weight X%): Actual importance [actually was critical / minor / irrelevant]

**Actual Critical Factors (unexpected):**
- Factor X: [turned out to be more critical than predicted]
- Factor Y: [turned out to be more critical than predicted]

### Implementation Quality
**Predicted Implementation Time:** [estimate]
**Actual Implementation Time:** [actual duration]
**Predicted Implementation Risk:** [X]%
**Actual Implementation Difficulty:** [severity assessment]
**Implementation Surprises:** [what went differently]

### User Adoption & Satisfaction
**Predicted Adoption Rate:** [target]
**Actual Adoption Rate:** [measured at Day X]
**Predicted User Satisfaction:** [target score]
**Actual User Satisfaction:** [measured score]
**User Feedback:** [key themes from user input]

### Strategic Alignment Achievement
**Predicted Strategic Benefit:** [original strategy contribution]
**Actual Strategic Benefit:** [measured contribution]
**Organizational Impact:** [broader consequences]
```

### 3. Conduct Confidence Calibration Analysis

"**Калибрирую confidence scoring на основе actual outcomes...**"

**Confidence Assessment:**
```
Original Confidence Level: [0.XX]
Confidence Thresholds Used:
  - Exceptional (>0.90): [count decisions]
  - High (0.80-0.90): [count decisions]
  - Moderate (0.60-0.79): [count decisions]
  - Low (0.40-0.59): [count decisions]

Outcome by Confidence Level:
  - Exceptional confidence decisions: [X]% success rate
  - High confidence decisions: [X]% success rate
  - Moderate confidence decisions: [X]% success rate
  - Low confidence decisions: [X]% success rate

CALIBRATION FINDING:
If 90% confidence decisions actually succeed 85-92% of time → WELL-CALIBRATED
If 90% confidence decisions actually succeed 70% of time → OVERCONFIDENT
If 90% confidence decisions actually succeed 98% of time → UNDERCONFIDENT
```

**Confidence Adjustment Recommendations:**
```
Current Scoring Formula Result: [score]
Calibration Correction: +/- [X] points
Recommended New Threshold: [new score]
Justification: [why adjustment needed]
```

### 4. Identify Factor Importance Reality Check

"**Определяю какие факторы РЕАЛЬНО вождили success или failure...**"

**Compare Predicted vs. Actual Factor Importance:**

```markdown
## Factor Importance Calibration

### Predicted vs. Actual Weight Accuracy

| Factor | Predicted Weight | Actual Importance | Variance | Learning |
|--------|-----------------|-------------------|----------|----------|
| [Factor A] | 25% | 35% | +10% | Was more critical than expected |
| [Factor B] | 20% | 8% | -12% | Was less critical than expected |
| [Factor C] | 15% | 18% | +3% | Prediction accurate |
| [Factor D] | 10% | 2% | -8% | Overweighted in analysis |

### Critical Success Factors Actually Realized
1. **[Factor X]** (Predicted importance: [Y]%) → Actual: CRITICAL
   - Evidence: [specific outcome impact]
   - Learning: [implication for future decisions]

2. **[Factor Y]** (Predicted importance: [Y]%) → Actual: MINIMAL
   - Evidence: [specific outcome impact]
   - Learning: [implication for future decisions]

### Unknown Factors That Became Critical
1. **[Unpredicted Factor A]** → Actual criticality: HIGH
   - Evidence: [how it affected outcome]
   - Learning: [how to identify this in future decisions]

2. **[Unpredicted Factor B]** → Actual criticality: HIGH
   - Evidence: [how it affected outcome]
   - Learning: [how to identify this in future decisions]
```

### 5. Extract Organizational Learning

"**Извлекаю learning для улучшения будущих решений...**"

**Decision Framework Improvements:**

```markdown
## Organizational Learning from This Decision

### Framework Improvements
1. **New Evaluation Factor to Add**
   - Factor: [name]
   - Why: [evidence from this decision]
   - Weight recommendation: [X]%
   - How to measure: [assessment methodology]

2. **Factor Weight to Adjust**
   - Factor: [name]
   - Current weight: [X]% → Recommended: [Y]%
   - Evidence: [why adjustment needed]

3. **Risk to Increase Probability Assessment**
   - Risk: [name]
   - Previous estimate: [X]% → Recommended: [Y]%
   - Evidence: [actual probability from this decision]

### Evidence Gathering Improvements
1. **New Evidence Source Category**
   - Type: [category]
   - Rationale: [why needed based on this decision]
   - Implementation: [how to gather]

2. **Evidence Quality Improvements**
   - Current approach: [what was used]
   - Problem identified: [what was insufficient]
   - Recommended enhancement: [how to improve]

### Confidence Threshold Adjustments
1. **Confidence Score Recalibration**
   - Current threshold for [X]% confidence: [calculation]
   - Recommended adjustment: [new calculation]
   - Evidence: [this decision's confidence vs. outcome]

### Decision Process Improvements
1. **Stakeholder Engagement Enhancement**
   - Issue: [what went differently with stakeholders]
   - Improvement: [how to handle this better]

2. **Timeline/Resource Allocation**
   - Issue: [unexpected timeline or resource requirements]
   - Improvement: [how to estimate better]
```

### 6. Document Learning for Future Decisions

"**Документирую learning в organizational decision knowledge base...**"

**Create Learning Record:**

```markdown
## Post-Decision Learning Record

**Decision:** [Name of decision from original analysis]
**Review Date:** [Day 30/60/90]
**Analyst:** [Name]
**Organization:** [Department]

### Executive Summary
[1-2 paragraph summary of outcome vs. prediction]

### Key Outcomes
- Predicted outcome: [metric and value]
- Actual outcome: [metric and value]
- Success assessment: [Exceeded / Met / Underperformed / Failed]

### Critical Learning Points
1. [Most important learning]
2. [Second most important]
3. [Third most important]

### Confidence Calibration Data
- Original confidence: [X.XX]
- Actual success: [Yes/Partial/No]
- Confidence adjustment: [+/- X points]

### Factor Importance Corrections
- [Factor A]: Predicted [X]% → Actual [Y]% (adjust future weight by +/- Z%)
- [Factor B]: Predicted [X]% → Actual [Y]% (adjust future weight by +/- Z%)

### New Framework Elements Identified
- [Element 1]: Description and recommended implementation
- [Element 2]: Description and recommended implementation

### Organizational Recommendations
1. [Process improvement for next decision]
2. [Framework enhancement to apply]
3. [Evidence gathering enhancement]

### Confidence Scoring Update for Future Decisions
```
Original Formula: [old calculation]
Calibration Finding: [how formula performed]
Recommended Update: [new calculation]
```
```

### 7. Update Consilium Knowledge Base

Update {outputFile} with Learning Record reference:
```yaml
stepsCompleted: [...all previous steps..., 'step-06-post-decision-review']
progress: 100
currentPhase: 'post-decision-learning'
lastStep: 'step-06-post-decision-review'
postDecisionReviewComplete: true

decisionOutcome:
  success: '[Yes / Partial / No]'
  confidenceAccuracy: '[Calibrated / Overconfident / Underconfident]'
  learningRecordLocation: '[path to learning record file]'
  frameworkImprovementsIdentified: '[count]'
```

## CRITICAL STEP COMPLETION NOTE

Post-decision review creates organizational learning that improves all future EMBER Consilium decisions. This is not optional—it is how the framework improves over time.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Actual outcomes assessed honestly against predictions
- Confidence scoring calibration performed
- Critical success factors vs. predicted factors compared
- Unexpected factors identified and documented
- Organizational learning extracted and documented
- Framework improvements recommended for future use
- Learning record integrated into knowledge base

### ❌ SYSTEM FAILURE:

- Outcomes assessed with rationalization rather than honesty
- Confidence calibration not performed
- Learning not documented
- Framework not improved based on findings
- Post-decision review skipped
- No organizational knowledge capture

### Post-Decision Review as Learning System

🚨 THIS IS NOT OPTIONAL
🚨 THIS IS HOW THE FRAMEWORK IMPROVES OVER TIME

Master Rule:
Post-decision review is what transforms EMBER Consilium from
static methodology to adaptive learning system.
Skip this step and all other improvements mean nothing.

---

**Master Rule:** Post-decision review is what transforms EMBER Consilium from static methodology to adaptive learning system. Skip this step and all other improvements mean nothing.
