# CREATE C-04D: Diversity Check Gate

## STEP GOAL:

Before finalizing post text, verify that it's sufficiently different from existing posts. Prevent repetitive/similar content.

**This step intercepts after offer selection (step 4) and before final text generation.**

---

## EXECUTION RULES

- ALWAYS run diversity check before approving post generation
- BLOCK posts with >75% similarity to recent posts
- WARN posts with 55-75% similarity
- SUGGEST modifications when issues detected
- NEVER skip this step

---

## STEP INSTRUCTIONS

### 1. Collect Candidate Post Data

Display the post parameters collected so far:

```
═══════════════════════════════════════════════════════════════
  📋 DIVERSITY CHECK - POST SUMMARY
═══════════════════════════════════════════════════════════════

Candidate Post Parameters:
  Routine: [from step 1]
  Primary Pain: [from step 2]
  Secondary Pains: [from step 2]
  Offer Type: [from step 3]
  Target Persona: [user selection]
  Narrative Angle: [user selection]

═══════════════════════════════════════════════════════════════
```

### 2. Load Recent Posts Database

Query the posts CSV/database:

```
Loading last 30 posts...
✓ Found 28 posts in database
✓ Filtering for relevant comparisons...
```

### 3. Calculate Similarity Scores

For each recent post, calculate:

```
═══════════════════════════════════════════════════════════════
  SIMILARITY ANALYSIS
═══════════════════════════════════════════════════════════════

Comparing to Post 1 (posted 3 days ago)
  ├─ Routine similarity: 100% (same routine)
  ├─ Pain match: 95% (same pain category)
  ├─ Secondary pain overlap: 50%
  ├─ Offer match: 0% (different offer)
  ├─ Persona match: 0% (different persona)
  └─ Angle match: 95% (same angle)

  WEIGHTED SCORE: 62% ⚠️ SIMILAR

Comparing to Post 2 (posted 5 days ago)
  ├─ Routine similarity: 0% (different routine)
  ├─ Pain match: 30% (different category)
  ├─ Secondary pain overlap: 0%
  ├─ Offer match: 30% (similar but different)
  ├─ Persona match: 100% (same persona)
  └─ Angle match: 15% (different angle)

  WEIGHTED SCORE: 28% ✅ UNIQUE

Comparing to Post 3 (posted 6 days ago)
  ├─ Routine similarity: 100% (same routine)
  ├─ Pain match: 100% (exact pain match)
  ├─ Secondary pain overlap: 100%
  ├─ Offer match: 100% (same offer)
  ├─ Persona match: 100% (same persona)
  └─ Angle match: 100% (same angle)

  WEIGHTED SCORE: 100% ❌ DUPLICATE

═══════════════════════════════════════════════════════════════

MAX SIMILARITY SCORE: 100% (Post 3)
→ Status: ❌ DUPLICATE DETECTED
```

### 4. Run Rule Checks

Check all 6 diversity rules:

```
═══════════════════════════════════════════════════════════════
  DIVERSITY RULES CHECK
═══════════════════════════════════════════════════════════════

Rule 1: Same routine frequency (Max 1 per 7 days)
  ├─ Candidate routine: ClaudeFlow parallel
  ├─ Last ClaudeFlow post: 3 days ago
  ├─ Status: ❌ VIOLATION
  └─ Action: Cannot post same routine within 7 days

Rule 2: Pain category frequency (Max 2 per 30 days)
  ├─ Candidate pain: SPEED category
  ├─ SPEED posts in last 30 days: 2
  ├─ Status: ⚠️ AT THRESHOLD
  └─ Action: Warning - at maximum allowed

Rule 3: Offer type distribution (Min 3 types per 30 days)
  ├─ Offer types used (last 30 days): training, done-for-you, templates
  ├─ Status: ✅ PASS
  └─ Action: OK - good variety

Rule 4: Persona rotation (Switch every 2-3 posts)
  ├─ Last 3 posts: Legal, Legal, Legal
  ├─ Candidate: Legal
  ├─ Status: ❌ VIOLATION
  └─ Action: Same persona 4 times - switch required

Rule 5: Angle freshness (Max 2 per 14 days)
  ├─ Candidate angle: Time-saving
  ├─ Time-saving posts in last 14 days: 2
  ├─ Status: ✅ AT LIMIT (OK)
  └─ Action: OK - can use once more

Rule 6: Secondary pain diversity (New pain every 3 posts)
  ├─ Last 5 posts secondary pains: diverse
  ├─ Status: ✅ PASS
  └─ Action: OK - good diversity

═══════════════════════════════════════════════════════════════

RULE VIOLATIONS SUMMARY: 2 violations found
  ❌ Rule 1: Routine frequency
  ❌ Rule 4: Persona overuse
  ⚠️  Rule 2: At pain threshold
```

### 5. Generate Recommendations

Based on violations, suggest modifications:

```
═══════════════════════════════════════════════════════════════
  📋 RECOMMENDATIONS
═══════════════════════════════════════════════════════════════

Issue 1: Duplicate Post (100% similarity to Post 3)
  └─ This is nearly identical to a post from 6 days ago
     Recommendation: REJECT and try different routine

Issue 2: Routine Too Soon (ClaudeFlow posted 3 days ago)
  └─ Rule 1 violation: Need 7+ days between same routine
     Recommendation:
     ✓ Wait 4 more days, OR
     ✓ Use different routine (BMAD, Agent roles, etc.)

Issue 3: Persona Overused (Legal personas 4 times)
  └─ Rule 4 violation: Switch personas every 2-3 posts
     Recommendation:
     ✓ Change target_persona to: HR teams, Marketing, Finance
     ✓ These personas haven't been used recently

Issue 4: Pain Category at Max (Speed already 2x this month)
  └─ Rule 2 at threshold: Only 1 more Speed post allowed
     Recommendation:
     ✓ Change primary_pain to: Cost, Quality, or Expertise
     ✓ Or wait until next month for more Speed posts

═══════════════════════════════════════════════════════════════

STRONGEST RECOMMENDATION:
  Use BMAD routine instead (ClaudeFlow too soon)
  Target HR teams instead (Legal overused)
  Address Cost pain instead (Speed at threshold)

  This would make post unique and follow all rules.
```

### 6. Present Decision Options

```
═══════════════════════════════════════════════════════════════
  🎯 WHAT WOULD YOU LIKE TO DO?
═══════════════════════════════════════════════════════════════

[A] APPLY RECOMMENDATIONS
    └─ Modify: routine → BMAD, persona → HR, pain → Cost
       Re-run check (will likely APPROVE)

[B] OVERRIDE & POST ANYWAY
    └─ Ignore warnings and post as-is
       ⚠️ Warning: High duplicate risk (100% to Post 3)
       Likely low engagement

[C] MODIFY SPECIFIC FIELDS
    ├─ Change routine? [BMAD / Agent roles / Manual]
    ├─ Change persona? [HR / Marketing / Finance / Entrepreneurs]
    ├─ Change pain? [Cost / Quality / Expertise / Scaling]
    └─ Change angle? [Cost-reduction / Quality / Empowerment]

[D] REJECT & START OVER
    └─ Cancel this post and try different routine
       Suggestion: Wait 4 days before trying ClaudeFlow again

[E] VIEW SIMILAR POSTS
    └─ Show me posts 1 & 3 to understand what's similar

[M] BACK
    └─ Return to previous step

═══════════════════════════════════════════════════════════════
```

### 7. Handle User Response

**If [A] APPLY RECOMMENDATIONS:**

```
Applying modifications:
  ✓ Routine: ClaudeFlow → BMAD ✓
  ✓ Persona: Legal → HR ✓
  ✓ Pain: Speed → Cost ✓

Re-running diversity check...

═══════════════════════════════════════════════════════════════
  ✅ DIVERSITY CHECK PASSED
═══════════════════════════════════════════════════════════════

NEW SIMILARITY SCORES:
  vs Post 1: 28% ✅ OK
  vs Post 2: 42% ✅ OK
  vs Post 3: 15% ✅ UNIQUE

RULE CHECKS:
  Rule 1: ✅ PASS (different routine)
  Rule 2: ✅ PASS (different pain)
  Rule 3: ✅ PASS (good offer distribution)
  Rule 4: ✅ PASS (persona switched)
  Rule 5: ✅ PASS (angle OK)
  Rule 6: ✅ PASS (secondary pains diverse)

STATUS: ✅ APPROVED - Post is ready to proceed!

═══════════════════════════════════════════════════════════════

Proceeding to step 5 (finalize text)...
```

**If [B] OVERRIDE:**

```
⚠️  WARNING: OVERRIDE SELECTED

You're posting despite:
  • 100% similarity to recent post
  • Rule 1 violation (routine too soon)
  • Rule 4 violation (persona overuse)

Risks:
  ├─ Low engagement (audience fatigue)
  ├─ Algorithm suppression (platform penalties)
  ├─ Wasted opportunity (similar message doesn't reach new audience)
  └─ Conversion loss (same angle doesn't resonate with all)

User confirms? [YES, PROCEED] [NO, APPLY RECOMMENDATIONS]

If YES:
  Proceeding to step 5 with marked risk...
  Note: Logging override for analysis
```

**If [C] MODIFY SPECIFIC FIELDS:**

```
FIELD MODIFICATION MENU:

Routine:
  [1] BMAD documentation
  [2] Agent role selection
  [3] Manual process audit
  [4] Keep ClaudeFlow

Persona:
  [1] HR teams
  [2] Marketing teams
  [3] Finance teams
  [4] Entrepreneurs
  [5] Keep Legal

Pain:
  [1] Cost reduction
  [2] Quality improvement
  [3] Expertise gap
  [4] Scaling issues
  [5] Keep Speed

Select modifications: [1,1,1]

Recalculating...
✓ New similarity: 22% ✅ APPROVED
```

**If [D] REJECT:**

```
Post rejected.

Returning to step 2 (select routine)...

SUGGESTION:
  "Try a different routine. ClaudeFlow again in 4+ days."

  Available routines:
  ├─ BMAD documentation (never used)
  ├─ Agent role selection (5 days ago)
  ├─ Manual process audit (2 weeks ago)
  └─ ClaudeFlow parallel (3 days - too soon)

[Select routine to try] [Back to menu]
```

**If [E] VIEW SIMILAR:**

```
═══════════════════════════════════════════════════════════════
  SIMILAR POST #1
═══════════════════════════════════════════════════════════════
Posted: 3 days ago
Routine: ClaudeFlow parallel
Pain: Speed efficiency
Persona: Legal teams
Offer: Done-for-you service
Angle: Time-saving
Content: "ClaudeFlow processed 80 documents in 2 hours..."
Engagement: 4.2%

═══════════════════════════════════════════════════════════════
  DUPLICATE POST #3
═══════════════════════════════════════════════════════════════
Posted: 6 days ago
Routine: ClaudeFlow parallel (IDENTICAL)
Pain: Speed efficiency (IDENTICAL)
Persona: Legal teams (IDENTICAL)
Offer: Done-for-you (IDENTICAL)
Angle: Time-saving (IDENTICAL)
Content: "ClaudeFlow processed 90 contracts..."
Engagement: 4.1%

═══════════════════════════════════════════════════════════════

THIS IS WHY THEY'RE 100% SIMILAR:
  Same routine + pain + persona + offer + angle = duplicate
  Different only: number of documents (80 vs 90)

Recommendation: REJECT this post, try completely different angle

[BACK] [APPLY RECOMMENDATIONS] [OVERRIDE]
```

---

## SUCCESS CRITERIA

✓ Candidate post data collected
✓ Similarity scores calculated for all relevant posts
✓ All 6 diversity rules checked
✓ Recommendations generated (if issues)
✓ User makes informed decision
✓ Final decision recorded

---

## NEXT STEP

- If ✅ APPROVED: Load `./step-c-05a-select-post.md` (next major step)
- If ❌ REJECTED: Return to step 2 (select new routine)
- If ⚠️ MODIFIED: Re-run this step with new data

---

## NOTES FOR IMPLEMENTATION

1. **Database:** Requires posts CSV/table from previous posts
2. **Calculation:** Can be Python script, Google Sheets formula, or custom code
3. **Storage:** Save this check result with final post for analytics
4. **Analytics:** Track: similarity scores, rule violations, override decisions
5. **Monthly:** Review patterns to understand what works best

---

## REFERENCE DOCUMENTS

For detailed methodology:
- **DIVERSITY-CHECK-ALGORITHM.md** - Complete technical reference
- **DIVERSITY-CHECK-QUICK-START.md** - Implementation guide
- **DIVERSITY-CHECK-REFERENCE-CARD.md** - Quick lookup

---

**This gate ensures your content stays fresh and engaging. Don't skip it!**

