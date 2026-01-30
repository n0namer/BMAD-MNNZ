---
description: Audit copywriting quality (action verbs, data specificity, benefits, language, CTA)
name: step-v-04b-audit
nextStepFile: ./v-04c-report.md
type: automated-analysis
---

# VALIDATE V-04B: Copywriting Quality Audit

## STEP GOAL:

Audit copywriting quality across multiple dimensions: strong action verbs, specific numbers/data, clear benefits, compelling language, CTA clarity.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Audit Start

```
═══════════════════════════════════════════════════════════════

  🔍 AUDITING COPYWRITING QUALITY

  Анализирую 22 поста по качеству копирайтинга...

═══════════════════════════════════════════════════════════════
```

### 2. Run Copy Audit Checks

For each post, evaluate:

#### CHECK 1: Strong Action Verbs
- ✅ Good: "Transform", "Discover", "Master", "Unlock", "Build"
- ⚠️ Weak: "Learn", "Know", "See", "Get", "Try"
- ❌ Poor: "Talk about", "Discuss", "Share"

#### CHECK 2: Specific Numbers/Data
- ✅ Good: "5 ways", "3x faster", "2,340 users", "47% increase"
- ⚠️ Okay: "Many people", "Several studies", "Recently"
- ❌ Poor: "Some", "Recently", No data

#### CHECK 3: Clear Benefits
- ✅ Good: Specific, measurable outcomes stated
- ⚠️ Okay: Benefits implied but not explicit
- ❌ Poor: Benefits unclear or missing

#### CHECK 4: Compelling Language
- ✅ Good: Emotional + logical appeal, vivid words
- ⚠️ Okay: Straightforward but not compelling
- ❌ Poor: Boring, generic language

#### CHECK 5: CTA Clarity
- ✅ Good: Explicit, action-oriented CTA
- ⚠️ Okay: CTA present but could be stronger
- ❌ Poor: No CTA or vague

### 3. Generate Audit Results

```
Auditing copy quality...

Post #1: "5 Ways to Transform Your Productivity"
├─ Action verbs: ✅ Transform, Unlock, Master (strong)
├─ Specificity: ✅ "5 Ways", "3x faster", "2,340 users"
├─ Benefits: ✅ Clear ("Save 10 hours/week", "Achieve more")
├─ Language: ✅ Compelling ("Game-changing", "Breakthrough")
└─ CTA: ✅ Explicit ("Save this post", "Start implementing")
SCORE: 5/5 ⭐⭐⭐⭐⭐ EXCELLENT

Post #2: "Common Mistake When Learning React"
├─ Action verbs: ✅ Avoid, Master, Prevent (good)
├─ Specificity: ⚠️ "Common mistake" only (needs numbers)
├─ Benefits: ⚠️ Implied benefits, not explicit
├─ Language: ✅ Good ("Avoid pitfalls", "Accelerate learning")
└─ CTA: ⚠️ Weak ("Let me know your thoughts")
SCORE: 3/5 ⭐⭐⭐ ACCEPTABLE

Post #3: "Why Most People Fail at Fitness"
├─ Action verbs: ❌ Talk about, Discuss (weak)
├─ Specificity: ❌ No numbers or data
├─ Benefits: ❌ Benefits not clearly stated
├─ Language: ⚠️ Generic ("achieve goals", "get fit")
└─ CTA: ❌ No explicit CTA
SCORE: 1/5 ⭐ POOR

...Processing 19 more posts...
```

### 4. Summary Statistics

```
COPY AUDIT SUMMARY (22 posts):

Excellent (5/5): 8 posts (36%) 🏆
Good (4/5): 10 posts (45%) ✅
Acceptable (3/5): 3 posts (14%) ⚠️
Poor (<3/5): 1 post (5%) ❌

Average Score: 4.1 / 5.0 (82% quality)

DIMENSION BREAKDOWN:

Action Verbs:
  ✅ Strong: 18 posts (82%)
  ⚠️ Weak: 3 posts (14%)
  ❌ Poor: 1 post (4%)

Specificity (Numbers/Data):
  ✅ Specific: 16 posts (73%)
  ⚠️ Generic: 5 posts (23%)
  ❌ Missing data: 1 post (4%)

Clear Benefits:
  ✅ Clear: 19 posts (86%)
  ⚠️ Implied: 2 posts (9%)
  ❌ Unclear: 1 post (5%)

Compelling Language:
  ✅ Compelling: 17 posts (77%)
  ⚠️ Okay: 4 posts (18%)
  ❌ Boring: 1 post (5%)

CTA Clarity:
  ✅ Explicit: 20 posts (91%)
  ⚠️ Weak: 2 posts (9%)
  ❌ Missing: 0 posts (0%)
```

### 5. Progress

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Copy Audit: 100% Complete (22/22 posts)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## SAVED DATA

Store copy audit results:
```json
{
  "validation_type": "copy_audit",
  "posts_audited": 22,
  "average_score": 4.1,
  "summary": {
    "excellent": 8,
    "good": 10,
    "acceptable": 3,
    "poor": 1
  },
  "dimension_scores": {
    "action_verbs": 82,
    "specificity": 73,
    "benefits": 86,
    "language": 77,
    "cta": 91
  },
  "results": [...]
}
```

---

## NEXT STEP

Generate detailed copy audit report with improvement suggestions

