# DIVERSITY CHECK ALGORITHM - EXECUTIVE SUMMARY

---

## WHAT PROBLEM DOES THIS SOLVE?

Your Telegram post generation workflow turns routine demonstrations into natively-sold products. Without diversity checks, you risk:

1. **Audience fatigue** - "He keeps saying the same thing"
2. **Algorithm suppression** - Social platforms penalize repetitive content
3. **Lost sales** - Same angle doesn't resonate with all buyers
4. **Engagement decline** - CTR drops on repetitive posts

**Solution:** Pre-generation gate that measures similarity and enforces diversity rules.

---

## CORE CONCEPT: SIMILARITY SCORING

Before you post, the system calculates how similar your candidate post is to existing posts across 6 dimensions:

```
SIMILARITY SCORE =
  routine_match (20% weight) +
  pain_point_match (25%) +
  secondary_pains_overlap (15%) +
  offer_type_match (20%) +
  target_persona_match (10%) +
  narrative_angle_match (10%)

Result: 0-100% similarity
```

**Interpretation:**
- **0-30%** = Unique ✅ Post it
- **30-55%** = Similar ⚠️ Modify it
- **55-75%** = Very Similar ❌ Reject it
- **75%+** = Duplicate ❌ Block it

---

## 6 DIVERSITY RULES

These ensure your content stays fresh:

| Rule | Constraint | Rationale |
|------|-----------|-----------|
| **Rule 1** | Max 1 same routine per 7 days | Prevent obvious repetition |
| **Rule 2** | Max 2 same pain category per 30 days | Different people have different problems |
| **Rule 3** | Min 3 offer types per 30 days | Variety in what you're selling |
| **Rule 4** | Rotate personas every 2-3 posts | Different decision-makers, different triggers |
| **Rule 5** | Max 2 same angle per 14 days | Same narrative angle = same mental trigger |
| **Rule 6** | New secondary pain every 3 posts | Show comprehensive solution |

---

## HOW IT WORKS IN YOUR WORKFLOW

```
Step 1: You show a routine (ClaudeFlow demo, BMAD generation, etc.)
         ↓
Step 2: Identify business pain points it addresses
         ↓
Step 3: Match to offer type (training, done-for-you, templates, etc.)
         ↓
Step 4: Generate post text variants
         ↓
[NEW] Step 4.5: DIVERSITY CHECK GATE
         ├─ Load recent posts from database
         ├─ Calculate similarity to each
         ├─ Check all 6 rules
         ├─ If issues detected: suggest modifications
         └─ Get user approval before proceeding
         ↓
Step 5: Finalize text and post to Telegram
```

---

## MINIMAL IMPLEMENTATION

You need 3 things:

### 1. CSV Database
Track each post with these fields:
```
date_posted, routine, primary_pain, secondary_pains,
offer_type, target_persona, angle, engagement_rate
```

### 2. Similarity Calculator
```
For each existing post:
  - Compare candidate vs existing on each dimension
  - Assign similarity scores (0-100)
  - Weight and sum them
  - Output overall similarity %
```

### 3. Rules Checker
```
Before posting, verify:
  ✓ Same routine not posted in last 7 days?
  ✓ Pain category not repeated > 2x in 30 days?
  ✓ Offer types varied (3+ types in 30 days)?
  ✓ Personas rotated (switch every 2-3)?
  ✓ Angle not overused (max 2x in 14 days)?
  ✓ Secondary pains show variety?
```

---

## FIELD DEFINITIONS

### Routine (What you're demonstrating)
- ClaudeFlow parallel processing
- BMAD documentation generation
- Agent role selection
- Manual process audit
- etc.

### Primary Pain (Main business problem)
**Speed Group:** slow_documents, lengthy_decisions, inefficient_workflows
**Expertise Group:** lack_expertise, team_dependency, no_documentation
**Scaling Group:** high_hiring_costs, cant_scale_without_people
**Quality Group:** inconsistent_quality, human_errors, poor_standardization
**Cost Group:** expensive_experts, high_payroll, budget_constraints

### Offer Type (What you're selling)
- `training` - Course/webinar/education
- `done-for-you` - Full service delivery
- `templates` - Self-serve tools/frameworks
- `consulting` - Advisory/1:1 guidance
- `setup-only` - Partial service (they maintain)

### Target Persona (Who you're speaking to)
- legal_teams, hr_teams, small_business_owners, entrepreneurs, marketing_teams, finance_teams, operations_managers

### Narrative Angle (How you're positioning it)
- time-saving, cost-reduction, quality-improvement, empowerment, risk-mitigation, scaling, independence

### Secondary Pains (Supporting problems)
- team_dependency, high_costs, scaling_issues, no_documentation, slow_execution, quality_issues

---

## PRACTICAL EXAMPLES

### Example 1: Clear Duplicate

```
Post A (existing):
  ClaudeFlow demo → Speed pain → Done-for-you → Legal teams → Time-saving

Post B (candidate):
  ClaudeFlow demo → Speed pain → Done-for-you → Legal teams → Speed improvement

Similarity: 97% → ❌ BLOCK "Too similar to Post A from 3 days ago"
```

### Example 2: Same Angle, Different Everything Else

```
Post A (existing):
  ClaudeFlow → Speed pain → Done-for-you → Legal teams → Time-saving

Post C (candidate):
  BMAD → Cost pain → Templates → Entrepreneurs → Cost-reduction

Similarity: 13% → ✅ APPROVE "Unique enough"
```

### Example 3: Similar but Fixable

```
Post A (existing):
  ClaudeFlow → Speed pain → Done-for-you → Legal teams → Time-saving

Post D (candidate):
  ClaudeFlow → Speed pain → Done-for-you → HR teams → Time-saving

Similarity: 61% → ⚠️ WARN "Similar, but persona is different"
Recommendation: "Same routine + pain + offer + angle. Only difference: persona.
               Proceed if confident, or change to a different pain point."
```

---

## QUICK START (30 minutes)

**Phase 1:** Create CSV with post database (5 min)
**Phase 2:** Build similarity calculator (10 min)
**Phase 3:** Implement rules checker (10 min)
**Phase 4:** Add approval workflow (5 min)

---

## WHAT CHANGES FOR YOU

### Before Diversity Check
- Post whatever comes to mind
- Risk: Audience sees repetition
- Result: Declining engagement over time

### After Diversity Check
- Quick pre-post check (1 minute)
- Get suggestions if too similar
- Modify if needed
- Post with confidence
- Result: Consistent engagement + happy audience

---

## METRICS TO TRACK

**Weekly:**
- Avg similarity score (target: <40%)
- Rule violations (target: 0)

**Monthly:**
- Diversity score (target: 70%+)
- Engagement by routine
- Conversion by offer type
- CTR by persona

**Quarterly:**
- Best-performing routine
- Best-performing pain point
- Best-performing offer type
- Best-performing persona

---

## RULES AT A GLANCE

```
RULE 1: Routine Frequency
  └─ Max 1 per 7 days
  └─ BLOCK if violated

RULE 2: Pain Category Frequency
  └─ Max 2 per 30 days
  └─ WARN at 2, BLOCK at 3

RULE 3: Offer Type Variety
  └─ Min 3 types per 30 days
  └─ SUGGEST alternatives if missing

RULE 4: Persona Rotation
  └─ Switch every 2-3 posts
  └─ WARN if repeating same persona

RULE 5: Angle Freshness
  └─ Max 2 per 14 days
  └─ SUGGEST different angle if overused

RULE 6: Secondary Pain Diversity
  └─ New pain every 3 posts
  └─ INFO only (can override)
```

---

## HOW TO USE THIS SYSTEM

### For Each Post:

1. **Fill candidate post data** (routine, pain, offer, persona, angle)
2. **Click "Check Diversity"** (system calculates similarity)
3. **Review results:**
   - If ✅: Post immediately
   - If ⚠️: Review suggestions and modify
   - If ❌: Change routine or core parameter
4. **Get approval** before finalizing

### Monthly Review:

1. **Calculate diversity score** (unique_routines + unique_pains + unique_personas) / 3
2. **Check offer type distribution** (should have 3+ types)
3. **Identify patterns** (which pain points convert best?)
4. **Plan next month's content** based on what worked

---

## ANTI-PATTERNS TO AVOID

```
❌ Same Routine Every Day
✅ Rotate: ClaudeFlow → BMAD → Agent roles → ClaudeFlow (day 4+)

❌ Same Pain Point Repeatedly
✅ Rotate: Speed → Quality → Cost → Expertise → Scaling

❌ Always Selling Same Offer Type
✅ Rotate: Training → Templates → Done-for-you → Consulting

❌ Only Reaching One Persona
✅ Rotate: Legal → HR → Small business → Entrepreneurs

❌ Single Narrative Angle
✅ Rotate: Time-saving → Cost reduction → Quality → Empowerment
```

---

## FILES PROVIDED

1. **DIVERSITY-CHECK-ALGORITHM.md** (Comprehensive)
   - Complete methodology
   - Detailed calculations
   - Implementation workflows
   - Database schema

2. **DIVERSITY-CHECK-QUICK-START.md** (Practical)
   - 30-minute implementation
   - Code examples
   - CSV templates
   - Troubleshooting

3. **DIVERSITY-CHECK-REFERENCE-CARD.md** (Cheat Sheet)
   - Decision tables
   - Quick calculations
   - One-page lookup
   - Common scenarios

4. **DIVERSITY-CHECK-SUMMARY.md** (This file)
   - Executive overview
   - Core concepts
   - Quick reference

---

## NEXT STEPS

1. **Read DIVERSITY-CHECK-ALGORITHM.md** for full context
2. **Copy DIVERSITY-CHECK-QUICK-START.md** template
3. **Implement Phase 1-4** (30 min total)
4. **Integrate into your workflow** at step 4.5
5. **Start checking every post**
6. **Review monthly** for patterns

---

## SUCCESS METRICS

After 1 month with diversity checks:

```
Expected results:
✅ Similarity scores average 20-40% (down from ~60%)
✅ Rule violations near 0% (blocking obvious repetition)
✅ Engagement rates stabilize/increase (audience less fatigued)
✅ Conversion rates improve by persona (targeting right buyers)
✅ Diversity score 70%+ (comprehensive content mix)

After 3 months:
✅ Data shows which routines perform best
✅ Data shows which pain points resonate most
✅ Data shows which offer types convert best
✅ Data shows which personas are most responsive
✅ You can predict which post types will succeed
```

---

## QUESTIONS?

**Q: How much time does the check add?**
A: 1-2 minutes per post (after database is set up).

**Q: Can I override the check?**
A: Yes, but understand the cost. Posts >75% similar get low engagement.

**Q: What if I want to post same routine twice?**
A: Use different pain, offer, angle, or persona to differentiate.

**Q: How long until I see results?**
A: After 10 posts you'll see patterns. After 30 posts, clear data on what works.

**Q: What if my audience is very specific?**
A: Start with what you have (2-3 personas), expand as you learn what converts.

---

## TLDR

**Problem:** Routine demos can become repetitive without diversity checks.

**Solution:** Pre-generation gate measuring similarity across 6 dimensions + enforcing 6 diversity rules.

**Result:** Consistent engagement, happy audience, better conversions.

**Implementation:** 30 minutes, ongoing 1-2 min per post.

**Expected Impact:** Similarity scores drop 50% + engagement stabilizes + revenue increases from better targeting.

---

**Ready to implement? Start with the QUICK-START guide.**

