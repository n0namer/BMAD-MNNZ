---
description: AI predicts engagement potential (urgency, curiosity, specificity, emotional appeal, social proof)
name: step-v-05b-predict
nextStepFile: ./step-v-05c-report.md
type: ai-analysis
---

# VALIDATE V-05B: Engagement Potential Prediction

## STEP GOAL:

Use AI to predict engagement potential of posts based on content factors: urgency level, curiosity factor, specificity, emotional appeal, social proof potential.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Prediction Start

```
═══════════════════════════════════════════════════════════════

  🔮 PREDICTING ENGAGEMENT POTENTIAL

  AI анализирует 18 постов по факторам взаимодействия...

═══════════════════════════════════════════════════════════════
```

### 2. Prediction Framework

For each post, score 5 engagement factors (0-1 scale):

#### FACTOR 1: Urgency Level
- Does headline/opening create time pressure?
- Examples: "before X", "limited time", "now", "immediately"
- High (0.8-1.0): Explicit deadline, scarcity, FOMO
- Medium (0.4-0.7): Some urgency signals
- Low (0-0.3): No urgency, evergreen content

#### FACTOR 2: Curiosity Factor
- Does post hook engage curiosity?
- Examples: "Why...", "Secret to...", "Hidden...", numbers
- High (0.8-1.0): Strong curiosity-gap, surprising angle
- Medium (0.4-0.7): Some curiosity appeal
- Low (0-0.3): Straightforward, no mystery

#### FACTOR 3: Specificity
- Is content specific vs generic?
- Examples: "5 ways", "47% increase", "2-hour method"
- High (0.8-1.0): Very specific, numbers/data
- Medium (0.4-0.7): Some specificity
- Low (0-0.3): Generic, vague

#### FACTOR 4: Emotional Appeal
- Does content trigger emotional response?
- Examples: Fear, excitement, aspiration, relatability
- High (0.8-1.0): Strong emotional trigger
- Medium (0.4-0.7): Some emotional resonance
- Low (0-0.3): Purely informational

#### FACTOR 5: Social Proof Potential
- Is content shareable/provable?
- Examples: Data, quotes, research, common experience
- High (0.8-1.0): Strong social proof built in
- Medium (0.4-0.7): Some proof elements
- Low (0-0.3): No proof elements

### 3. Generate Predictions

```
Analyzing engagement factors...

Post #1: "5 Ways to Transform Your Productivity"
├─ Urgency: 0.7 (Medium - implicit deadline)
├─ Curiosity: 0.8 (High - "Ways" format intriguing)
├─ Specificity: 0.9 (Very High - "5 ways", specific benefits)
├─ Emotional: 0.8 (High - aspiration trigger)
└─ Social Proof: 0.7 (Medium - tips are shareable)
ENGAGEMENT SCORE: (0.7 + 0.8 + 0.9 + 0.8 + 0.7) / 5 = 0.78
STARS: ⭐⭐⭐⭐ (4 stars) ✅ PASS (≥0.6)

Post #2: "Common Mistake When Learning React"
├─ Urgency: 0.4 (Low-medium - no explicit urgency)
├─ Curiosity: 0.7 (Medium - "mistake" creates interest)
├─ Specificity: 0.5 (Medium - mentions topic but vague error)
├─ Emotional: 0.6 (Medium - relatable frustration)
└─ Social Proof: 0.4 (Low - personal anecdote only)
ENGAGEMENT SCORE: (0.4 + 0.7 + 0.5 + 0.6 + 0.4) / 5 = 0.52
STARS: ⭐⭐⭐ (3 stars) ⚠️ MARGINAL (≥0.6)

Post #3: "Why Most People Fail at Fitness"
├─ Urgency: 0.3 (Low - no time pressure)
├─ Curiosity: 0.5 (Medium - "why" question)
├─ Specificity: 0.2 (Low - "most people" too vague)
├─ Emotional: 0.7 (High - failure fear/aspiration)
└─ Social Proof: 0.3 (Low - no data or proof)
ENGAGEMENT SCORE: (0.3 + 0.5 + 0.2 + 0.7 + 0.3) / 5 = 0.40
STARS: ⭐⭐ (2 stars) ❌ FAIL (<0.6)

...Processing 15 more posts...
```

### 4. Summary Results

```
ENGAGEMENT PREDICTION SUMMARY (18 posts):

5 Stars (0.85-1.0): 2 posts (11%) 🌟 EXCELLENT
4 Stars (0.70-0.84): 8 posts (44%) ✅ GOOD
3 Stars (0.55-0.69): 6 posts (33%) ⚠️ MARGINAL
2 Stars (0.40-0.54): 2 posts (11%) ❌ POOR
1 Star (<0.40): 0 posts (0%)

Average Score: 0.68 / 1.0 (68%) → ⭐⭐⭐ 3.4 stars

PASS RATE: 16/18 posts (89%) score ≥3 stars
CONCERN: 2 posts score <3 stars

STRONG ENGAGEMENT SIGNALS:
  • Specificity very strong (avg 0.76)
  • Emotional appeal strong (avg 0.71)
  • Curiosity strong (avg 0.69)

WEAK SIGNALS:
  • Social proof average (avg 0.54)
  • Urgency moderate (avg 0.55)
```

### 5. Progress

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Engagement Prediction: 100% Complete (18/18 posts)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## SAVED DATA

Store engagement predictions:
```json
{
  "validation_type": "engagement_check",
  "posts_predicted": 18,
  "average_score": 0.68,
  "pass_rate": 89,
  "predictions": [
    {
      "post_id": 1,
      "title": "...",
      "urgency": 0.7,
      "curiosity": 0.8,
      "specificity": 0.9,
      "emotional": 0.8,
      "social_proof": 0.7,
      "engagement_score": 0.78,
      "stars": 4,
      "pass": true
    },
    ...
  ]
}
```

---

## NEXT STEP

Generate engagement prediction report with recommendations

