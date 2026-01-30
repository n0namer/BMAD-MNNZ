# DIVERSITY CHECK ALGORITHM
## Telegram Post Generation Workflow - Repetition Prevention System

---

## EXECUTIVE SUMMARY

This algorithm prevents your Telegram content pipeline from generating similar/repetitive posts. It works **before** post generation by:

1. **Analyzing existing posts database** for similarity patterns
2. **Measuring diversity** across multiple dimensions (angles, pain points, offers, routines)
3. **Suggesting alternatives** to ensure unique content
4. **Enforcing diversity rules** at generation time

**Why it matters:** Your workflow turns routine demonstrations into natively sold products. Without diversity checks, you risk:
- Audience fatigue ("same post, different routine")
- Algorithm suppression (Telegram/social media penalize repetitive content)
- Lost sales opportunities (same angle doesn't resonate with all buyers)

---

## PART 1: SIMILARITY CHECK FRAMEWORK

### 1.1 Fields to Compare (Multi-Dimensional Similarity)

Your posts have these key dimensions. Similarity is measured across all of them:

```
DIMENSION 1: ROUTINE DEMONSTRATED
─────────────────────────────────
Field: `routine_type`
Examples: ClaudeFlow parallel processing, BMAD doc generation, agent role selection
How: Exact match or semantic similarity
Weight: 20% (showing the same routine multiple times = BAD)

DIMENSION 2: PRIMARY PAIN POINT ADDRESSED
─────────────────────────────────────────
Field: `primary_pain`
Examples: "slow document processing", "team lacks expertise", "no process standardization"
How: Semantic similarity (cluster pain points)
Weight: 25% (same pain point = repetitive, boring)

DIMENSION 3: SECONDARY PAIN POINTS
──────────────────────────────────
Field: `secondary_pains` (array)
Examples: ["dependency on key people", "slow scaling", "high hiring costs"]
How: Overlap detection (how many pains in common?)
Weight: 15% (secondary pains provide flavor)

DIMENSION 4: OFFER TYPE
──────────────────────
Field: `offer_type`
Values: "course/training", "done-for-you service", "templates/tools", "consulting", "setup-only"
How: Exact match
Weight: 20% (same offer = same conversion path = less variety)

DIMENSION 5: TARGET PERSONA
───────────────────────────
Field: `target_persona`
Examples: "legal professionals", "small business owners", "HR teams", "marketing teams"
How: Exact match
Weight: 10% (different personas deserve different angles)

DIMENSION 6: NARRATIVE ANGLE
────────────────────────────
Field: `angle`
Examples: "speed/time-saving", "quality/accuracy", "cost reduction", "risk mitigation", "team empowerment"
How: Exact match or thematic clustering
Weight: 10% (same angle with same pain = definitely repetitive)
```

### 1.2 Similarity Threshold Calculation

```
OVERALL SIMILARITY SCORE = Weighted average of all dimensions

Dimension Scores (0-100):
  routine_similarity: 0-100
  pain_match_score: 0-100
  secondary_pain_overlap: 0-100
  offer_match: 0-100
  persona_match: 0-100
  angle_match: 0-100

WEIGHTED SCORE = (
    routine_similarity × 0.20 +
    pain_match_score × 0.25 +
    secondary_pain_overlap × 0.15 +
    offer_match × 0.20 +
    persona_match × 0.10 +
    angle_match × 0.10
) / 100

CLASSIFICATION:

  0-30%   = UNIQUE (✅ Safe to post, very different)
  30-55%  = SIMILAR (⚠️  WARNING, requires review)
  55-75%  = VERY SIMILAR (❌ REJECT, too repetitive)
  75%+    = DUPLICATE (❌ BLOCK, nearly identical)
```

### 1.3 Detailed Similarity Calculation Methods

#### ROUTINE SIMILARITY

```
Input: Current routine, Existing routine
Output: 0-100% similarity

Algorithm:
  IF routine_name == existing_routine_name:
    return 100%

  ELSE IF routine_category == existing_category (e.g., both are "ClaudeFlow demos"):
    score = 60% base
    + adjust based on specific_details_overlap
    return score

  ELSE:
    return 0% (completely different routine)
```

**Example:**
- Current: "ClaudeFlow agent role selection"
- Existing: "ClaudeFlow parallel processing"
- Category match: Both ClaudeFlow demos
- Score: 60% (same tool, different feature)

---

#### PAIN MATCH SCORE

```
Input: Current primary_pain, Existing primary_pain
Output: 0-100% match

Semantic Similarity Groups (cluster pains):

  SPEED/TIME GROUP:
    - "slow document processing"
    - "lengthy decision-making"
    - "inefficient workflows"
    → Any 2 in this group = 85-100% match

  EXPERTISE/KNOWLEDGE GROUP:
    - "lack team expertise"
    - "dependency on key people"
    - "knowledge not documented"
    → Any 2 in this group = 80-95% match

  SCALING GROUP:
    - "hiring costs too high"
    - "can't scale without more people"
    - "difficult to add team members"
    → Any 2 in this group = 85-100% match

  QUALITY/ACCURACY GROUP:
    - "inconsistent quality"
    - "human errors in processing"
    - "poor standardization"
    → Any 2 in this group = 80-90% match

  COST GROUP:
    - "expensive experts"
    - "high payroll costs"
    - "budget constraints"
    → Any 2 in this group = 75-85% match

If pains are in DIFFERENT groups:
  Match score = 20-40% (different pain angles)

If pain is EXACT SAME:
  Match score = 100%
```

**Example:**
- Current pain: "lack team expertise"
- Existing pain: "dependency on key people"
- Both in EXPERTISE GROUP
- Match score: 88%

---

#### SECONDARY PAIN OVERLAP

```
Input: Current secondary_pains[], Existing secondary_pains[]
Output: 0-100% overlap

Algorithm:
  overlap_count = count(matching pains in both arrays)
  max_count = max(len(current), len(existing))

  overlap_percentage = (overlap_count / max_count) × 100

  Examples:
    Current: ["team dependency", "high costs", "no docs"]
    Existing: ["team dependency", "high costs"]
    Overlap: 2/3 = 66%

    Current: ["no documentation"]
    Existing: ["poor process", "no standardization"]
    Overlap: 0/2 = 0%
```

---

#### OFFER MATCH

```
Input: Current offer_type, Existing offer_type
Output: 0-100% match

Exact Match:
  Both "course/training" = 100%
  Both "done-for-you service" = 100%

Category Closeness:
  "course" vs "consulting" = 60% (related but different)
  "done-for-you" vs "setup-only" = 50% (different value props)

Different:
  "course" vs "templates" = 20% (completely different)
```

---

#### PERSONA MATCH

```
Input: Current target_persona, Existing target_persona
Output: 0-100% match

Exact match = 100%
Different personas = 0%

Examples:
  "legal teams" vs "legal teams" = 100%
  "legal teams" vs "HR teams" = 0%
  "small business owners" vs "entrepreneurs" = 70% (conceptually close)
```

---

#### ANGLE MATCH

```
Input: Current angle, Existing angle
Output: 0-100% match

Semantic Grouping:

  SPEED/EFFICIENCY GROUP:
    - "time-saving"
    - "rapid deployment"
    - "quick turnaround"
    → Any 2 = 90-100% match

  QUALITY/EXCELLENCE GROUP:
    - "accuracy improvement"
    - "consistency"
    - "risk reduction"
    → Any 2 = 85-95% match

  ECONOMICS GROUP:
    - "cost reduction"
    - "ROI improvement"
    - "budget optimization"
    → Any 2 = 80-90% match

  EMPOWERMENT GROUP:
    - "independence from experts"
    - "team capability"
    - "democratization"
    → Any 2 = 80-90% match

Different groups = 15-30% match
Same angle exactly = 100%
```

---

### 1.4 Practical Examples

#### EXAMPLE 1: Clear Repetition

```
Post 1 (existing):
  routine: "ClaudeFlow parallel processing"
  primary_pain: "slow document processing"
  secondary_pains: ["dependency on key people"]
  offer_type: "done-for-you service"
  target_persona: "legal teams"
  angle: "time-saving"

Post 2 (candidate):
  routine: "ClaudeFlow parallel processing"
  primary_pain: "lengthy decision-making"
  secondary_pains: ["dependency on key people"]
  offer_type: "done-for-you service"
  target_persona: "legal teams"
  angle: "speed improvement"

CALCULATION:
  routine_sim: 100% (identical)
  pain_match: 90% (both in SPEED group, very close)
  secondary_overlap: 100% (identical)
  offer_match: 100% (identical)
  persona_match: 100% (identical)
  angle_match: 95% (same group)

  WEIGHTED = (100×0.20 + 90×0.25 + 100×0.15 + 100×0.20 + 100×0.10 + 95×0.10) / 100
           = (20 + 22.5 + 15 + 20 + 10 + 9.5) / 100
           = 97%

  RESULT: ❌ DUPLICATE (>75%)
  ACTION: REJECT - Post is too similar to Post 1
```

---

#### EXAMPLE 2: Related but Different

```
Post 1 (existing):
  routine: "ClaudeFlow parallel processing"
  primary_pain: "slow document processing"
  secondary_pains: ["high costs"]
  offer_type: "done-for-you service"
  target_persona: "legal teams"
  angle: "time-saving"

Post 3 (candidate):
  routine: "BMAD documentation generation"
  primary_pain: "no process documentation"
  secondary_pains: ["team dependency", "cannot scale"]
  offer_type: "training course"
  target_persona: "small business owners"
  angle: "empowerment"

CALCULATION:
  routine_sim: 15% (different routines, different tools)
  pain_match: 25% (different pain categories)
  secondary_overlap: 0% (completely different)
  offer_match: 20% (service vs course)
  persona_match: 0% (different personas)
  angle_match: 20% (different groups)

  WEIGHTED = (15×0.20 + 25×0.25 + 0×0.15 + 20×0.20 + 0×0.10 + 20×0.10) / 100
           = (3 + 6.25 + 0 + 4 + 0 + 2) / 100
           = 15.25%

  RESULT: ✅ UNIQUE (0-30%)
  ACTION: APPROVE - Post is sufficiently different
```

---

#### EXAMPLE 3: Similar Angle, Different Everything Else

```
Post 1 (existing):
  routine: "ClaudeFlow role selection"
  primary_pain: "slow hiring process"
  secondary_pains: ["high recruiting costs"]
  offer_type: "consulting"
  target_persona: "HR teams"
  angle: "cost reduction"

Post 4 (candidate):
  routine: "Manual process audit"
  primary_pain: "budget overruns"
  secondary_pains: ["process waste"]
  offer_type: "templates"
  target_persona: "small business owners"
  angle: "budget optimization"

CALCULATION:
  routine_sim: 0% (completely different)
  pain_match: 50% (both cost-related, different context)
  secondary_overlap: 10% (1/2 close)
  offer_match: 30% (consulting vs templates)
  persona_match: 0% (HR vs business owner)
  angle_match: 85% (both economics group)

  WEIGHTED = (0×0.20 + 50×0.25 + 10×0.15 + 30×0.20 + 0×0.10 + 85×0.10) / 100
           = (0 + 12.5 + 1.5 + 6 + 0 + 8.5) / 100
           = 28.5%

  RESULT: ✅ UNIQUE (0-30%, just under threshold)
  ACTION: APPROVE - Despite shared angle, everything else is different
```

---

## PART 2: DIVERSITY RULES

These rules ensure content stays fresh and addresses different audience needs:

### RULE 1: No More Than 1 Post per Routine per Week

```
STATEMENT:
  You cannot post about the same routine more than once per 7 days.

WHY:
  - Audience sees pattern: "they're just showing the same thing again"
  - Diminishing engagement
  - Algorithm suppression on social platforms

ENFORCEMENT:
  Before generating post, query database:
    SELECT COUNT(*) FROM posts
    WHERE routine = current_routine
    AND date_posted >= (TODAY - 7 days)

  IF count > 0:
    BLOCK post generation
    RECOMMEND: "Try a different routine (unused in past 7 days)"

EXCEPTION:
  Different angle + different persona = can post same routine (but rarely)
  Example: "ClaudeFlow for HR" vs "ClaudeFlow for Legal" (different personas)
```

---

### RULE 2: Pain Point Rotation (Maximum 2 Posts Same Pain Category per Month)

```
STATEMENT:
  You cannot address the same pain point category more than 2 times per month.

PAIN CATEGORIES:
  - SPEED/EFFICIENCY: "time-saving", "rapid deployment", "quick execution"
  - QUALITY: "accuracy", "consistency", "risk mitigation"
  - COST: "budget reduction", "expense savings", "ROI"
  - EXPERTISE: "knowledge gap", "team capability", "empowerment"
  - SCALING: "growth without hiring", "parallel processing", "capacity"

WHY:
  - Repetitive pain = repetitive solution
  - Audience has different pain profiles
  - You need to reach different buyer personas

ENFORCEMENT:
  Before generating, count posts by pain category:
    SELECT COUNT(*) FROM posts
    WHERE pain_category = current_category
    AND date_posted >= (TODAY - 30 days)
    AND similarity_score < 55%  (posts must be distinct)

  IF count >= 2:
    WARNING: "You've addressed this pain twice this month"
    RECOMMEND: "Try addressing a different pain category"
    ALLOW: If user confirms and angle is sufficiently different

  IF count >= 3:
    BLOCK: "Maximum pain category frequency exceeded"
```

---

### RULE 3: Offer Type Distribution (At Least 3 Different Types per Month)

```
STATEMENT:
  You must offer variety in what you're selling:
  - At least 1 training/course offer
  - At least 1 done-for-you service offer
  - At least 1 templates/tools offer

  Within 30-day window.

WHY:
  - Different audiences buy different solutions
  - Some want to learn, some want you to do it
  - Maximizes revenue opportunities

OFFER TYPES:
  1. "training" - Course, webinar, educational content
  2. "done-for-you" - Full service delivery
  3. "templates" - Tools, frameworks, self-serve
  4. "consulting" - Advisory, 1:1 guidance
  5. "setup-only" - Partial service, they maintain

ENFORCEMENT:
  Monthly check:
    GROUP BY offer_type, COUNT(*)
    WHERE date_posted >= (TODAY - 30 days)

  RESULTS ANALYSIS:
    All 5 types present? → ✅ EXCELLENT (maximum flexibility)
    3+ types present? → ✅ GOOD (good variety)
    1-2 types present? → ⚠️ WARNING (low variety)
    Only 1 type? → ❌ FIX (you're only selling one way)

  NEXT POST RECOMMENDATION:
    Suggest offer type that's underrepresented
    "You haven't posted a training/course in 15 days. Consider it."
```

---

### RULE 4: Persona Rotation (Reach Different Decision-Makers)

```
STATEMENT:
  Rotate through different personas every 2-3 posts.

PERSONA LIST (examples):
  - Legal teams / Lawyers
  - HR teams / Recruiters
  - Small business owners
  - Entrepreneurs (growth-focused)
  - Marketing teams
  - Financial teams
  - Operations managers

WHY:
  - Same message to same person = wasted breath
  - Different personas have different buying triggers
  - Expands total addressable market (TAM)

ENFORCEMENT:
  Track recent posts by persona:
    SELECT DISTINCT target_persona FROM posts
    ORDER BY date_posted DESC
    LIMIT 5

  DIVERSITY CHECK:
    IF last 3 posts target same persona:
      WARNING: "Switch to different persona"
      RECOMMEND: "[List of underused personas]"

    IF persona appears more than 2x in last 2 weeks:
      SUGGEST: "Mix in different decision-maker"

  PATTERN TO AVOID:
    Posts 1-5: All targeting "legal teams"
    This saturates one segment, ignores others
```

---

### RULE 5: Angle Freshness (Don't Overuse Same Angle)

```
STATEMENT:
  No more than 2 posts using same narrative angle per 2 weeks.

NARRATIVE ANGLES (examples):
  - SPEED/EFFICIENCY: "Do it faster"
  - COST: "Do it cheaper"
  - QUALITY: "Do it better"
  - EMPOWERMENT: "Do it yourself"
  - RISK MITIGATION: "Do it safer"
  - SCALING: "Do it at scale"
  - INDEPENDENCE: "Do it without people"

WHY:
  - Same angle = same mental trigger = boring
  - Audience tunes out repeated messages
  - Different angles reach different psychological profiles

ENFORCEMENT:
  Track angle usage:
    SELECT angle, COUNT(*) FROM posts
    WHERE date_posted >= (TODAY - 14 days)
    GROUP BY angle

  IF any angle appears > 2 times:
    WARNING: "You've used this angle twice in 2 weeks"
    RECOMMEND: "Try a different narrative angle"
    SUGGEST: "[List of underused angles]"
```

---

### RULE 6: Secondary Pain Diversity

```
STATEMENT:
  Every 3 posts, introduce a new secondary pain point.
  Don't keep repeating the same supporting pains.

SECONDARY PAIN EXAMPLES:
  - "Team member dependency"
  - "High hiring costs"
  - "Slow time-to-market"
  - "Quality inconsistency"
  - "Lack of documentation"
  - "Process bottlenecks"
  - "Regulatory compliance"
  - "Knowledge silos"

WHY:
  - People have multiple problems
  - Different posts should speak to different combinations
  - Creates impression of comprehensive solution

ENFORCEMENT:
  Track secondary pain patterns:
    SELECT secondary_pains FROM posts
    ORDER BY date_posted DESC
    LIMIT 5

  DIVERSITY SCAN:
    unique_secondary_pains_in_last_5 = COUNT(DISTINCT secondary_pains)
    IF unique_secondary_pains_in_last_5 < 3:
      WARNING: "You're repeating same secondary pains"
      SUGGEST: "Introduce new secondary pain: [options]"
```

---

## PART 3: IMPLEMENTATION WORKFLOW

### STEP 1: Pre-Generation Check (Before Creating Post)

```
═══════════════════════════════════════════════════════════════════════════
  DIVERSITY CHECK WORKFLOW
═══════════════════════════════════════════════════════════════════════════

INPUT: Candidate post data
  ├─ routine
  ├─ primary_pain
  ├─ secondary_pains[]
  ├─ offer_type
  ├─ target_persona
  └─ angle

STEP 1.1: DATABASE QUERY
─────────────────────────────────────────
Load last 30 posts from database:
  SELECT * FROM posts
  ORDER BY date_posted DESC
  LIMIT 30

STEP 1.2: CALCULATE SIMILARITY SCORES
──────────────────────────────────────
For each existing post:
  1. Calculate routine_similarity
  2. Calculate pain_match_score
  3. Calculate secondary_pain_overlap
  4. Calculate offer_match
  5. Calculate persona_match
  6. Calculate angle_match
  7. Compute weighted OVERALL_SIMILARITY_SCORE

Create similarity matrix:
  Post1: 87% similarity (⚠️ WARNING)
  Post2: 45% similarity (✅ OK)
  Post3: 92% similarity (❌ DUPLICATE)
  Post4: 28% similarity (✅ OK)
  Post5: 18% similarity (✅ OK)

STEP 1.3: APPLY RULE CHECKS
──────────────────────────────────
Check RULE 1: Routine frequency
  ✓ "ClaudeFlow demos" last posted 10 days ago (allowed)

Check RULE 2: Pain category frequency
  ⚠️ "SPEED/EFFICIENCY" posted 2 times in last 30 days
     (warning: at max threshold)

Check RULE 3: Offer type distribution
  ✓ Good balance: training, done-for-you, templates all present

Check RULE 4: Persona rotation
  ⚠️ "Legal teams" posted 3 times in last 2 weeks
     (warning: switch persona)

Check RULE 5: Angle freshness
  ✓ "Time-saving" only 1 time in last 2 weeks

Check RULE 6: Secondary pain diversity
  ✓ Last 5 posts have 4+ different secondary pains

STEP 1.4: GENERATE REPORT
────────────────────────────
Status: ⚠️ PROCEED WITH CAUTION

Issues found:
  1. Post 3 is DUPLICATE (92% similarity) → BLOCK
  2. Pain category at max (2 in 30 days)
  3. Persona overused ("legal teams" - 3 recent posts)

Recommendations:
  → Change target_persona from "legal teams" to "HR teams"
  → Consider different pain angle (try COST or QUALITY)
  → Current angle is OK (time-saving only 1 time)

Suggest modifications:
  ├─ Persona: "legal teams" → "small business owners"
  ├─ Pain angle: Same (already optimal)
  └─ Offer type: Same (good distribution)

STEP 1.5: DECISION POINT
────────────────────────────
User sees options:

[A] APPROVE AS-IS
    (Understanding risks: persona overuse, pain threshold)

[B] APPLY RECOMMENDATIONS
    (Modify persona → re-run checks)

[C] REJECT & TRY DIFFERENT ROUTINE
    (Wait 3-4 days, use different routine demo)

[D] VIEW SIMILAR POSTS
    (See posts 1 & 3 to understand what's similar)
```

---

### STEP 2: If Issues Found - Modification Workflow

```
═══════════════════════════════════════════════════════════════════════════
  MODIFICATION WORKFLOW (When issues detected)
═══════════════════════════════════════════════════════════════════════════

Issue: Persona overuse ("legal teams" - 3 posts in 2 weeks)

ACTION: Suggest persona swap

AVAILABLE PERSONAS (not recently used):
  ├─ Marketing teams (last post: 25 days ago) ✅ GOOD
  ├─ HR teams (last post: 18 days ago) ✅ GOOD
  ├─ Finance teams (last post: 22 days ago) ✅ GOOD
  ├─ Operations managers (last post: 12 days ago) ⚠️ (OK but not ideal)
  └─ Small business owners (last post: 8 days ago) ⚠️ (OK but not ideal)

RECOMMENDATION:
  "Switch target_persona from 'legal teams' to 'marketing teams'"

  Why: Marketing teams haven't seen this message in 25 days
       Pain point (speed/efficiency) is relevant to their challenges too
       Different persona = fresh audience = better engagement

AFTER MODIFICATION:
  Re-run STEP 1.2 (recalculate similarity)

  Previous: 87% similarity with Post 1
  Now: 52% similarity with Post 1
  (Because persona changed from legal→marketing)

  Result: ✅ APPROVED

Display to user:
  ═══════════════════════════════════════════════════════════════
    ✅ DIVERSITY CHECK PASSED

    Similarity to existing posts: 52% (GOOD)
    Routine freshness: ✓ OK (10 days since similar post)
    Pain category: ⚠️ At threshold (2/30 days)
    Persona rotation: ✓ OK (switched to marketing teams)
    Offer type: ✓ OK (good distribution)
    Angle: ✓ OK (fresh)

    RECOMMENDATION:
    This post is ready to go! Fresh audience (marketing teams),
    different from existing posts.
  ═══════════════════════════════════════════════════════════════
```

---

### STEP 3: Post-Generation Quality Metrics

After post is generated, track these metrics:

```
POST ANALYTICS TO TRACK:

1. Engagement Rate (as % of followers)
   - High engagement = good post quality + good timing
   - Low engagement = might be repetitive or poorly timed

2. Comment Quality
   - Posts addressing NEW pain → higher-quality conversations
   - Posts addressing familiar pain → fewer comments

3. Click-through Rate to CTA
   - Different personas → different CTR patterns
   - Same persona repetition → declining CTR

4. Conversion Rate by Offer Type
   - Track which offer types convert best
   - Use data to inform future offer recommendations

MONTHLY DIVERSITY SCORE:
  Calculated as: (unique_routines + unique_pains + unique_personas) / possible_variations

  Example:
    Posted 10 posts last month
    Used: 5 routines (5/8 possible) = 62%
    Covered: 4 pain categories (4/7 possible) = 57%
    Reached: 6 personas (6/8 possible) = 75%

    Diversity Score = (62 + 57 + 75) / 3 = 65%

    Target: 70%+ for healthy content mix
```

---

## PART 4: QUICK REFERENCE - DECISION MATRIX

```
SIMILARITY SCORE → RECOMMENDED ACTION

0-30%    →  ✅ POST IMMEDIATELY
           "This is unique enough"

30-55%   →  ⚠️  PROCEED WITH MODIFICATIONS
           Check specific rules (persona? angle? pain?)
           Apply recommendations
           Re-run check

55-75%   →  ❌ REQUEST CHANGES
           Similar to existing post
           Suggest routine swap, angle change, persona change
           Don't post without modifications

75%+     →  ❌ BLOCK & REJECT
           Near-duplicate detected
           Post must be significantly different
           Wait 7+ days or choose different routine
```

---

## PART 5: DATABASE SCHEMA (Implementation Reference)

```sql
-- Posts table structure for tracking
CREATE TABLE posts (
  id PRIMARY KEY,
  date_posted TIMESTAMP,
  routine_type VARCHAR,
  primary_pain VARCHAR,
  secondary_pains JSON,
  offer_type VARCHAR,
  target_persona VARCHAR,
  angle VARCHAR,
  content_text TEXT,
  engagement_rate FLOAT,
  conversion_rate FLOAT,
  ctr FLOAT
);

-- Diversity tracking table
CREATE TABLE diversity_metrics (
  month DATE,
  unique_routines INT,
  unique_pain_categories INT,
  unique_personas INT,
  offer_type_distribution JSON,
  diversity_score FLOAT,
  recommendations JSON
);

-- Similarity cache (for fast lookups)
CREATE TABLE similarity_cache (
  candidate_post_id VARCHAR,
  existing_post_id VARCHAR,
  similarity_score FLOAT,
  components JSON,  -- {routine: 100, pain: 85, ...}
  check_timestamp TIMESTAMP
);
```

---

## PART 6: RULES SUMMARY TABLE

| Rule | Limit | Window | Weight | Action if Violated |
|------|-------|--------|--------|-------------------|
| **Rule 1** | 1 post per routine | 7 days | HIGH | ❌ BLOCK |
| **Rule 2** | 2 pain categories max | 30 days | HIGH | ⚠️ WARN at 2, ❌ BLOCK at 3 |
| **Rule 3** | 3+ offer types | 30 days | MEDIUM | ⚠️ SUGGEST alternatives |
| **Rule 4** | Rotate personas | Every 2-3 posts | HIGH | ⚠️ WARN, suggest swap |
| **Rule 5** | 2 angles max | 14 days | MEDIUM | ⚠️ SUGGEST fresh angle |
| **Rule 6** | New secondary pain | Every 3 posts | LOW | ℹ️ INFO, can override |

---

## PART 7: PRACTICAL WORKFLOW INTEGRATION

### Where to Insert Diversity Check in Your Pipeline

```
YOUR CURRENT WORKFLOW:
┌─────────────────────────────────────────────────────────┐
│ 1. Show routine (ClaudeFlow, BMAD, etc.)               │
└────────────────┬────────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────────────────────┐
│ 2. Identify business pain points                         │
└────────────────┬────────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────────────────────┐
│ 3. Match to product/offer type                          │
└────────────────┬────────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────────────────────┐
│ 4. Generate post text variants                          │
└────────────────┬────────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────────────────────┐
│ 5. *** DIVERSITY CHECK INSERT HERE ***                  │
│    Before final text generation                         │
└────────────────┬────────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────────────────────┐
│ 6. Finalize & post to Telegram                          │
└─────────────────────────────────────────────────────────┘
```

**PRECISELY: After step 4 (variants generated), BEFORE step 5 (text finalized):**

```
STEP 4.5: DIVERSITY CHECK GATE

Input: Post data (routine, pain, offer, persona, angle)

Gate logic:
  IF similarity_score > 75%:
    BLOCK
    RECOMMEND: "Try different routine/persona/angle"
    RETURN to STEP 1 (show different routine)

  ELSE IF similarity_score > 55%:
    WARN
    SUGGEST modifications
    ASK user: Apply suggestions? [YES] [NO - override]

  ELSE:
    APPROVE
    PROCEED to STEP 6
```

---

## PART 8: ANTI-PATTERNS TO AVOID

```
PATTERN 1: Same Routine Every Day
  ❌ BAD: ClaudeFlow demo, ClaudeFlow demo, ClaudeFlow demo, ...
  ✅ GOOD: ClaudeFlow demo (day 1) → BMAD demo (day 2) → Agent roles (day 3)

PATTERN 2: Hitting Same Pain Point Repeatedly
  ❌ BAD: "Speed saves time" (day 1), "Time management" (day 2), "Fast processing" (day 3)
  ✅ GOOD: Speed (day 1) → Quality (day 2) → Cost (day 3) → Expertise (day 4)

PATTERN 3: Always Selling Same Offer
  ❌ BAD: Always "book a consultation", always "buy the template", always "take the course"
  ✅ GOOD: Consultation (day 1) → Template (day 3) → Course (day 5) → Done-for-you (day 7)

PATTERN 4: Only Reaching One Persona
  ❌ BAD: Always "For lawyers", always "For legal teams"
  ✅ GOOD: Lawyers (day 1) → Entrepreneurs (day 2) → HR teams (day 3)

PATTERN 5: Single Narrative Angle
  ❌ BAD: Always "save time", always "reduce costs"
  ✅ GOOD: Save time (day 1) → Quality (day 2) → Independence (day 3) → Scaling (day 4)
```

---

## IMPLEMENTATION CHECKLIST

- [ ] Database schema created (posts + diversity_metrics tables)
- [ ] Similarity scoring algorithm coded
- [ ] Rule 1-6 enforcement logic implemented
- [ ] Decision matrix visualizer created
- [ ] Modification workflow tested
- [ ] Integration point (step 4.5) added to BMAD workflow
- [ ] Alert/warning system configured
- [ ] Monthly diversity report automated
- [ ] Post analytics tracking enabled
- [ ] User approval flow (for overrides) configured

---

**Version:** 1.0
**Status:** Ready for Integration
**Last Updated:** 2026-01-30
