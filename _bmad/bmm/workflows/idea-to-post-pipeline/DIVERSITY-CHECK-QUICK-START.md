# DIVERSITY CHECK - QUICK START GUIDE
## Implementation in 30 Minutes

---

## THE ONE-PAGE SUMMARY

**Problem:** Your Telegram content pipeline can generate similar/repetitive posts from different routines.

**Solution:** A pre-generation gate that measures post similarity across 6 dimensions and enforces diversity rules.

**Threshold:** Block if > 75% similar, warn if > 55% similar.

---

## THREE KEY CONCEPTS

### 1. SIMILARITY SCORE (0-100%)

Measures how similar a candidate post is to existing posts:

```
FORMULA:
  Score = (routine×20% + pain×25% + secondary_pain×15% + offer×20% + persona×10% + angle×10%)

INTERPRETATION:
  0-30%   = Unique ✅ Post it
  30-55%  = Similar ⚠️  Modify it
  55-75%  = Very similar ❌ Reject it
  75%+    = Duplicate ❌ Block it
```

**Example:** If candidate post is:
- Same routine as existing (100%)
- Same pain point (100%)
- Different offer type (0%)
- Different persona (0%)

Score = 100×20% + 100×25% + 0×15% + 0×20% + 0×10% + 0×10% = 45%

Result: ⚠️ Similar - apply modifications

---

### 2. SIX DIVERSITY RULES

These prevent repetition:

| # | Rule | Limit |
|---|------|-------|
| 1 | Same routine | Max 1x per 7 days |
| 2 | Same pain category | Max 2x per 30 days |
| 3 | Offer type variety | Min 3 types per 30 days |
| 4 | Persona rotation | Switch every 2-3 posts |
| 5 | Angle freshness | Max 2x per 14 days |
| 6 | Secondary pain mix | New pain every 3 posts |

---

### 3. DECISION FLOW

```
Candidate Post Created
         ↓
Query last 30 posts
         ↓
Calculate similarity to each
         ↓
       Are any >75%?
        /         \
      YES          NO
       ↓            ↓
    BLOCK      Check Rules 1-6
       ↓            ↓
    Reject      Any violated?
               /          \
             YES           NO
              ↓             ↓
           WARN         APPROVE
        (suggest         (post it)
         changes)
```

---

## MINIMAL CSV TRACKING

Store these fields for each post:

```csv
date_posted,routine,primary_pain,secondary_pains,offer_type,target_persona,angle,engagement_rate
2026-01-30,"ClaudeFlow parallel","slow documents","team_dependency|high_costs","done-for-you","legal_teams","time-saving",4.2%
2026-01-28,"BMAD documentation","no_documentation","scaling_issues|high_costs","training","small_business","empowerment",3.8%
2026-01-26,"ClaudeFlow roles","lack_expertise","team_dependency","consulting","hr_teams","quality",3.1%
```

---

## QUICK FIELD DEFINITIONS

### Primary Pain (Pick 1)
- `slow_documents` - Takes too long to process
- `no_documentation` - Processes not described
- `lack_expertise` - Team missing skills
- `high_costs` - Too expensive
- `inconsistent_quality` - Output varies
- `scaling_bottleneck` - Can't grow without hiring

### Offer Type (Pick 1)
- `training` - Course/webinar
- `done-for-you` - Full service
- `templates` - Self-serve tools
- `consulting` - Advisory
- `setup-only` - Partial service

### Target Persona (Pick 1)
- `legal_teams`
- `hr_teams`
- `small_business_owners`
- `entrepreneurs`
- `marketing_teams`
- `finance_teams`
- `operations_managers`

### Angle (Pick 1)
- `time-saving` - Do it faster
- `cost-reduction` - Do it cheaper
- `quality-improvement` - Do it better
- `empowerment` - Do it yourself
- `risk-mitigation` - Do it safer
- `scaling` - Do it at scale
- `independence` - Without key people

---

## STEP-BY-STEP IMPLEMENTATION

### Phase 1: Database Setup (5 min)

Create Google Sheets or simple CSV:

```
Columns needed:
1. date_posted (auto: today)
2. routine
3. primary_pain
4. secondary_pains (comma-separated)
5. offer_type
6. target_persona
7. angle
8. engagement_rate (post-publication)
9. conversion_rate (post-publication)
```

**[Template provided below in Part 2]**

---

### Phase 2: Similarity Calculator (10 min)

Create simple scoring (in Google Sheets or Python):

```python
def calc_similarity(candidate, existing_post):
    scores = {
        'routine': 100 if candidate['routine'] == existing_post['routine'] else 0,
        'pain': 100 if candidate['pain'] == existing_post['pain'] else 50 if in_same_group(candidate['pain'], existing_post['pain']) else 0,
        'secondary': overlap_count(candidate['secondary'], existing_post['secondary']) / max(len(candidate['secondary']), len(existing_post['secondary'])) * 100,
        'offer': 100 if candidate['offer'] == existing_post['offer'] else 0,
        'persona': 100 if candidate['persona'] == existing_post['persona'] else 0,
        'angle': 100 if candidate['angle'] == existing_post['angle'] else 50 if in_same_group(candidate['angle'], existing_post['angle']) else 0,
    }

    weighted = (
        scores['routine'] * 0.20 +
        scores['pain'] * 0.25 +
        scores['secondary'] * 0.15 +
        scores['offer'] * 0.20 +
        scores['persona'] * 0.10 +
        scores['angle'] * 0.10
    )

    return weighted
```

---

### Phase 3: Rules Engine (10 min)

Check 6 rules before posting:

```python
def check_rules(candidate):
    last_30 = get_posts(days=30)

    # Rule 1: Same routine?
    same_routine_count = count(r for r in last_30 if r.routine == candidate.routine and r.date > today - 7)
    if same_routine_count > 0:
        return "BLOCK: Same routine posted in last 7 days"

    # Rule 2: Pain category frequency?
    pain_category = get_category(candidate.pain)
    pain_count = count(r for r in last_30 if get_category(r.pain) == pain_category)
    if pain_count >= 2:
        return "WARN: This pain category already 2x this month"

    # Rule 3: Offer type distribution?
    offer_counts = group_by(last_30, 'offer_type')
    unique_types = len(offer_counts)
    if unique_types < 3:
        return "SUGGEST: Try different offer type (low diversity)"

    # Rule 4: Persona rotation?
    last_3 = get_posts(limit=3)
    if all(p.persona == candidate.persona for p in last_3):
        return "WARN: Same persona 3 times. Switch personas."

    # Rule 5: Angle freshness?
    same_angle = count(r for r in last_14 if r.angle == candidate.angle)
    if same_angle >= 2:
        return "SUGGEST: Try different angle (used 2x in 2 weeks)"

    # Rule 6: Secondary pain diversity?
    secondary_in_recent = all_secondary_pains(last_5)
    unique_secondary = len(set(secondary_in_recent))
    if unique_secondary < 3:
        return "INFO: Introduce new secondary pain"

    return "APPROVED"
```

---

### Phase 4: Approval Workflow (5 min)

Before you generate the post:

1. **Fill candidate post data** (routine, pain, offer, persona, angle)
2. **Run similarity check** against last 30 posts
3. **Run rule checks**
4. **Show results to user:**

```
═══════════════════════════════════════════════════════════════
  DIVERSITY CHECK RESULT
═══════════════════════════════════════════════════════════════

Similarity Score: 42% (GOOD ✅)

Rule Checks:
  Rule 1 (Routine frequency): ✅ PASS
  Rule 2 (Pain category): ✅ PASS
  Rule 3 (Offer variety): ⚠️ WARNING - Add 1 more offer type this month
  Rule 4 (Persona rotation): ✅ PASS
  Rule 5 (Angle freshness): ✅ PASS
  Rule 6 (Secondary pain): ✅ PASS

RECOMMENDATION:
  Post is ready! Good diversity overall.
  (Minor: Consider more offer type variety next post)

[APPROVE] [MODIFY] [VIEW SIMILAR POSTS]
═══════════════════════════════════════════════════════════════
```

---

## INTEGRATION POINTS

### In Your BMAD Workflow

Add this gate after post variants are generated (step 4) and before final text generation:

```
Step 3: Match to Product/Offer
         ↓
Step 4: Generate Post Variants
         ↓
[NEW] Step 4.5: DIVERSITY CHECK  ← INSERT HERE
         ├─ Load post data from step 4
         ├─ Calculate similarity
         ├─ Check rules
         ├─ If issues: suggest modifications
         └─ Get approval before proceeding
         ↓
Step 5: Finalize Text
         ↓
Step 6: Post to Telegram
```

---

## MONTHLY CHECKUP

Run once a month:

```
DIVERSITY DASHBOARD (30-day window)

Posts created: 10
Routines used: 4 (40% of possible)
Pain categories: 3 (43% of possible)
Personas reached: 5 (71% of possible)
Offer types: 2 ⚠️ (Need 3 minimum)
Unique angles: 5 (71% of possible)

DIVERSITY SCORE: 65% (Target: 70%+)

Action items:
1. Increase offer type variety (need 1 more type this month)
2. Reach new personas (legal teams not addressed in 35 days)
3. Cover more pain categories (only 3/7 addressed)

Recommendations for next 10 posts:
  - Include more "templates" offer type
  - Target "legal_teams" or "finance_teams"
  - Cover "independence" or "risk_mitigation" angles
```

---

## WHAT TO DO IF YOU HIT A LIMIT

### Scenario 1: "Same Routine Posted 7 Days Ago"

You want to post about ClaudeFlow again, but it was posted 7 days ago.

**Options:**
1. **Wait** - Post tomorrow (8 days passed)
2. **Switch angle** - Same routine, different pain/persona/angle
3. **Switch routine** - Use BMAD or Agent roles demo instead

**Recommended:** Switch to different routine. More variety = better engagement.

---

### Scenario 2: "Pain Category at Max (Already 2x this Month)"

You want to post about "speed/efficiency" but it's already been posted twice.

**Options:**
1. **Switch pain** - Address "quality" or "cost" instead
2. **Wait** - Wait until next month
3. **Override** - If angle/persona/offer are very different (rare)

**Recommended:** Switch pain. Audience has more than one problem to solve.

---

### Scenario 3: "Only 2 Offer Types This Month (Need 3)"

Your posts are all "training" and "done-for-you". Missing "templates".

**Next post recommendation:** Use "templates" offer type

You can force this:
```
Candidate post:
  routine: "ClaudeFlow"
  pain: "lack_expertise"
  offer_type: "templates"  ← Force this
  persona: "small_business"
```

This increases offer type diversity automatically.

---

### Scenario 4: "Legal Teams Posted 3 Times Recently"

Your last 3 posts all targeted legal teams.

**Next post:** Switch to different persona

```
Recent posts:
  1. Legal teams
  2. Legal teams
  3. Legal teams

Next: Switch to "HR teams" or "marketing teams"
```

---

## EXAMPLE: BEFORE & AFTER

### BEFORE Diversity Check

```
Post 1: ClaudeFlow demo → Speed pain → Done-for-you → Legal teams
Post 2: ClaudeFlow demo → Speed pain → Done-for-you → Legal teams ❌ REPETITIVE
Post 3: ClaudeFlow demo → Quality pain → Done-for-you → Legal teams ❌ REPETITIVE
Post 4: BMAD demo → Speed pain → Training → HR teams
Post 5: BMAD demo → Speed pain → Training → HR teams ❌ REPETITIVE

Audience reaction: "This guy keeps saying the same thing..."
```

### AFTER Diversity Check

```
Post 1: ClaudeFlow demo → Speed pain → Done-for-you → Legal teams
Post 2: BMAD demo → Quality pain → Templates → Small business
Post 3: Agent roles → Cost pain → Consulting → Marketing teams
Post 4: ClaudeFlow demo → Independence pain → Training → Entrepreneurs
Post 5: BMAD demo → Scaling pain → Done-for-you → Finance teams

Audience reaction: "Interesting! Each post speaks to a different problem..."
```

---

## MONITORING METRICS

Track these over time:

```
Weekly:
  - Similarity score (should average 20-40%)
  - Rule violations (should be 0)
  - Posts needing modifications (should be <10%)

Monthly:
  - Diversity score (target: 70%+)
  - Engagement rate by routine
  - Conversion rate by offer type
  - Which personas convert best

Quarterly:
  - Which pain points resonate most?
  - Which angles drive clicks?
  - Which offers convert best?
  - Patterns in successful posts
```

---

## COMMON QUESTIONS

**Q: Can I post same routine twice in one month?**
A: Only if it's different personas + different pain + different offer. Example: ClaudeFlow for legal (day 1) vs ClaudeFlow for HR (day 12). But typically better to diversify routines.

**Q: What if my secondary_pains repeat?**
A: It's lower priority (only 15% weight), but aim for variety. Every 3 posts, introduce new secondary pain.

**Q: How do I know which pain points work best?**
A: Track engagement_rate in your CSV. After 10 posts, you'll see patterns. Use that to guide future posts.

**Q: Can I override the diversity check?**
A: Yes, but understand the cost. If similarity > 75%, you're essentially reposting. Low engagement is likely.

**Q: What if I only know 2 offer types well?**
A: Your current answer "training" + "done-for-you" are great. Over time:
  - Month 1-2: Just these 2 types
  - Month 3-4: Add "templates"
  - Month 4-5: Add "consulting"

You'll grow your offerings as you go.

---

## NEXT STEPS

1. **Copy the CSV template** (provided below)
2. **Implement similarity calculator** (Python or Google Sheets formula)
3. **Add rules engine** (10 minutes of logic)
4. **Integrate into your BMAD workflow** (insert at step 4.5)
5. **Start checking before every post**
6. **Review monthly for patterns**

---

## TEMPLATE: POSTS TRACKING CSV

```csv
date_posted,routine,primary_pain,secondary_pains,offer_type,target_persona,angle,engagement_rate,conversion_rate,notes
2026-01-30,"ClaudeFlow parallel processing","slow_documents","team_dependency,high_costs","done-for-you","legal_teams","time-saving",4.2%,2.1%,"Mentioned contract processing"
2026-01-28,"BMAD documentation","no_documentation","scaling_issues,high_costs","training","small_business","empowerment",3.8%,1.9%,"Good discussion in comments"
2026-01-26,"ClaudeFlow role selection","lack_expertise","team_dependency","consulting","hr_teams","quality",3.1%,0.8%,"Lower conversion on consulting"
2026-01-24,"Agent hierarchy demo","slow_documents","high_costs,quality_issues","templates","marketing_teams","cost-reduction",5.1%,3.2%,"Best performing post so far"
```

---

**Ready to implement? Start with Phase 1 (CSV setup), then add Phase 2-4 gradually.**

