---
description: Validate ideas for specificity, researchability, audience clarity, uniqueness
name: step-v-07b-checks
nextStepFile: ./v-07c-report.md
type: automated-validation
---

# VALIDATE V-07B: Idea Validation Checks

## STEP GOAL:

Validate raw ideas before research phase: Is it specific enough? Researchable? Clear audience? Not duplicate? Has engaging potential?

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Validation Start

```
═══════════════════════════════════════════════════════════════

  🔍 VALIDATING IDEA VIABILITY

  Анализирую 47 идей по критериям валидации...

═══════════════════════════════════════════════════════════════
```

### 2. Run Validation Checks

For each idea, evaluate:

#### CHECK 1: Specific Enough?
- ✅ Good: Clear topic, defined angle, narrow focus
- ⚠️ Okay: Somewhat specific, needs clarification
- ❌ Poor: Too vague, too broad, unclear focus

#### CHECK 2: Researchable?
- ✅ Good: Available research, examples, data exist
- ⚠️ Okay: Some research available, needs creative sourcing
- ❌ Poor: Limited sources, hard to research

#### CHECK 3: Clear Audience?
- ✅ Good: Specific audience identified
- ⚠️ Okay: Potential audience, needs clarification
- ❌ Poor: No clear audience

#### CHECK 4: Not Duplicate?
- ✅ Good: Unique angle, new perspective
- ⚠️ Okay: Similar to existing posts but different angle
- ❌ Poor: Already covered extensively

#### CHECK 5: Engaging Potential?
- ✅ Good: Inherently interesting/valuable
- ⚠️ Okay: Potentially engaging with right angle
- ❌ Poor: Difficult to make engaging

### 3. Generate Validation Results

```
Validating ideas...

Idea #1: "The Future of AI in Education"
├─ Specific enough: ✅ Clear topic, education angle
├─ Researchable: ✅ Abundant research + case studies
├─ Clear audience: ✅ Educators, students, parents
├─ Not duplicate: ✅ Novel AI + education angle
└─ Engaging potential: ✅ High (trending topic)
STATUS: ✅ PROCEED — Ready for research

Idea #2: "How to Build Better Habits"
├─ Specific enough: ⚠️ Generic (needs angle specified)
├─ Researchable: ✅ Very researchable
├─ Clear audience: ⚠️ General, could be more specific
├─ Not duplicate: ❌ Very common topic
└─ Engaging potential: ⚠️ Depends on angle
STATUS: ⚠️ REVISE — Clarify angle and audience first

Idea #3: "Why Remote Work is Failing"
├─ Specific enough: ✅ Clear topic + perspective
├─ Researchable: ✅ Available research
├─ Clear audience: ✅ Managers, remote workers
├─ Not duplicate: ⚠️ Similar posts exist (new angle?)
└─ Engaging potential: ✅ High (controversial)
STATUS: ✅ PROCEED — Proceed with caution (research diff)

Idea #4: "Something about marketing"
├─ Specific enough: ❌ Too vague
├─ Researchable: ⚠️ Depends on final topic
├─ Clear audience: ❌ Not clear
├─ Not duplicate: ❓ Unknown (need specificity)
└─ Engaging potential: ⚠️ Unknown (need specificity)
STATUS: ❌ SKIP — Too vague, needs clarification

...Processing 43 more ideas...
```

### 4. Summary Statistics

```
IDEA VALIDATION SUMMARY (47 ideas):

✅ Proceed: 38 ideas (81%)
   Ready for research phase without changes

⚠️  Revise: 6 ideas (13%)
   Clarify angle/audience before research

❌ Skip: 3 ideas (6%)
   Too vague or not viable at this time

OVERALL VIABILITY: 81% of ideas are research-ready
```

### 5. Breakdown by Validation Criteria

```
SPECIFIC ENOUGH:
  ✅ Clear: 40 ideas (85%)
  ⚠️ Needs clarification: 5 ideas (11%)
  ❌ Too vague: 2 ideas (4%)

RESEARCHABLE:
  ✅ Easily researchable: 42 ideas (89%)
  ⚠️ Some research available: 4 ideas (9%)
  ❌ Difficult to research: 1 idea (2%)

CLEAR AUDIENCE:
  ✅ Clear audience: 41 ideas (87%)
  ⚠️ Potential audience: 5 ideas (11%)
  ❌ No audience: 1 idea (2%)

NOT DUPLICATE:
  ✅ Unique: 38 ideas (81%)
  ⚠️ Similar but different angle: 6 ideas (13%)
  ❌ Duplicate topic: 3 ideas (6%)

ENGAGING POTENTIAL:
  ✅ High engagement: 39 ideas (83%)
  ⚠️ Moderate engagement: 6 ideas (13%)
  ❌ Low engagement: 2 ideas (4%)
```

### 6. Progress

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Idea Validation: 100% Complete (47/47 ideas)
Ready for research: 38 ideas ✅
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## SAVED DATA

Store idea validation results:
```json
{
  "validation_type": "idea_validation",
  "ideas_validated": 47,
  "proceed": 38,
  "revise": 6,
  "skip": 3,
  "viability_rate": 81,
  "results": [
    {
      "idea_id": 1,
      "title": "The Future of AI in Education",
      "specific": true,
      "researchable": true,
      "clear_audience": true,
      "not_duplicate": true,
      "engaging": true,
      "status": "proceed"
    },
    ...
  ]
}
```

---

## NEXT STEP

Generate idea validation report with recommendations

