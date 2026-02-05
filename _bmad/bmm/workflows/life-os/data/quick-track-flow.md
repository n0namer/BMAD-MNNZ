---
name: 'quick-track-flow'
version: '1.0'
track: 'Quick'
target_duration: '15-20 minutes'
purpose: 'Fast evaluation for simple ideas, low stakes, and rapid go/no-go decisions'
consumedBy:
  - track-detection-algorithm.md
  - step-01-collect-ideas.md
  - step-04-consilium.md
  - step-05-scoring.md
  - step-09-complete.md
---

# Quick Track Flow

## Purpose

The Quick Track is designed for simple, low-stakes ideas that need rapid validation.
Instead of the full 100+ minute pipeline, Quick Track delivers a go/no-go decision
in 15-20 minutes while preserving analytical rigor for what matters.

**Who it's for:**
- Personal projects and hobbies
- Solo-developer spare-time ideas
- Proven business models
- Low-budget experiments
- Single-person accountability

**What you get:**
- Quick expert review (3 perspectives)
- Simple scorecard (10-15 lines)
- Go/NoGo recommendation
- 2-3 key risks identified
- Clear next action

---

## Pipeline Steps

The Quick Track includes only 4 steps from the full 9-step pipeline:

```
Step 01: Collect Ideas (5 min)
    ↓
Step 04lite: Consilium Lite (5-10 min)
    ↓
Step 05: Simplified Scoring (5 min)
    ↓
Step 09: Complete (1 min)
```

**Total time:** 16-21 minutes

### Step 08: Deep Plan Handling (Quick Track)

**Default behavior:** AUTO-SKIP

When Quick Track reaches Step 08, system automatically skips Deep Plan with this message:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 08: DEEP PLAN (QUICK TRACK)

Quick Track ideas don't need Deep Plan.
This is a simple idea - proceed straight to completion.

[C]ontinue to completion (recommended)
[P]lan anyway (L1-L3 basic plan, +10-15 min)
[F]ull plan (L1-L6 comprehensive, +20-60 min)

Your choice: [C/P/F]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Handling user choices:**

**IF [C]ontinue (recommended):**
- Skip Deep Plan entirely
- Mark `deep_plan_skipped: true` in workflow plan
- Proceed directly to Step 09 (Complete)
- **Time saved:** 20-60 minutes

**IF [P]lan anyway:**
- Show warning: "This is a simple idea. Deep Plan may be overkill."
- Confirmation: "Add L1-L3 plan (+10-15 min)? [Y/N]"
- If Y: Load L1-L3 template, build basic plan
- If N: Return to [C]ontinue option

**IF [F]ull plan:**
- Show warning: "Quick Track + L1-L6 = 35-80 min total (defeats Quick purpose)"
- Confirmation: "Continue with full L1-L6? [Y/N]"
- If Y: Load full L1-L6 template
- If N: Offer [P] or [C] instead

**Why auto-skip is default:**
- Quick Track is for rapid validation (15-20 min)
- Deep Plan adds 20-60+ min (defeats purpose)
- Simple ideas don't benefit from detailed planning
- User can always return later to add Deep Plan

---

### Step Flow Details

#### Step 1: Collect Ideas (5 min)
**Purpose:** Capture the idea and basic context.

**Process:**
1. User describes idea (title, description, domain)
2. System captures:
   - What problem does this solve?
   - Who is it for?
   - What resources are available? (time, budget, team)
3. System saves idea to memory
4. System runs track detection algorithm

**Output:**
- Idea record in `life-os:ideas:{id}`
- Track recommendation (Quick/Standard/Deep)

**Time:** 5 minutes

---

#### Step 2: Consilium Lite (5-10 min)
**Purpose:** Get 3 quick expert perspectives without deep analysis.

**How it differs from full Consilium:**
| Full Consilium (Step 04) | Consilium Lite (Quick Track) |
|--------------------------|------------------------------|
| 3-5 specialists, user-selected | 2-3 specialists, auto-selected |
| Six Thinking Hats assignment | No hats, direct recommendations |
| Multi-round discussion | Single-round only |
| Full synthesis (3-5 paragraphs) | Brief consensus (1-2 bullet points) |
| Auto-Suggest Engine available | No auto-suggest |
| TRIZ offered if contradictions | No TRIZ |
| 15-30 min | 5-10 min |

**Auto-Selection Rules (Domain-to-Specialist Map):**

| Domain | Specialists Auto-Selected |
|--------|---------------------------|
| personal, hobby | Life Coach + General Advisor |
| freelance | Business Advisor + Market Analyst |
| small-business | Business Advisor + Finance Analyst + Market Analyst |
| software | Tech Architect + Product Strategist |
| saas | Product Strategist + Growth Lead |
| ai-ml | AI Specialist + Tech Architect |

**Process:**
1. System auto-selects 2-3 specialists based on domain
2. Each specialist provides ONE recommendation (2-3 sentences):
   - What they like about the idea
   - What they're concerned about
   - Their verdict (Go / NoGo / Conditional)
3. System generates brief consensus:
   - Agreement level (unanimous / majority / split)
   - Key insight (1 sentence)
   - Primary risk to watch (1 sentence)

**Output:**
- 3 specialist recommendations (9-12 sentences total)
- Brief consensus (3 sentences)
- Primary risk flag

**No user menu.** System proceeds automatically to Step 05.

**Time:** 5-10 minutes

**Example (VK Recipes Bot):**

```
---
CONSILIUM LITE RESULTS

Specialists consulted: Tech Architect, Product Strategist

Tech Architect:
  ✓ Simple tech stack (Telegram API + VK API). Low complexity.
  ⚠ Risk: VK API rate limits could block daily sends.
  Verdict: GO (with rate limit handling)

Product Strategist:
  ✓ Clear value prop (daily recipes = habit building).
  ⚠ Risk: User retention after novelty wears off (week 2-3).
  Verdict: GO (consider engagement hooks)

Consensus: MAJORITY GO
  Agreement: Both recommend proceeding.
  Key insight: Technically simple, but retention requires engagement design.
  Primary risk: User drops off after 2-3 weeks. Plan a retention hook.
---
```

---

#### Step 3: Simplified Scoring (5 min)
**Purpose:** Quick quantitative evaluation using 3 core criteria.

**How it differs from full Scoring:**
| Full Scoring (Step 05) | Simplified Scoring (Quick Track) |
|------------------------|----------------------------------|
| 5-7 criteria (Impact, Effort, Alignment, Risk, Demand, Uniqueness, Timing) | 3 criteria only (Impact, Effort, Alignment) |
| Domain-specific criteria added (2-3 more) | No domain-specific criteria |
| Detailed 1-5 scale with justifications | Quick 1-5 scale, minimal justification |
| 10-15 min | 5 min |

**Criteria (Quick Track):**

1. **Impact (1-5):** How much does this improve your life/business/users?
   - 1 = Negligible, 3 = Moderate, 5 = Transformative

2. **Effort (1-5):** How much time/resources are required?
   - 1 = Massive, 3 = Moderate, 5 = Minimal

3. **Alignment (1-5):** How well does this align with your current goals/capacity?
   - 1 = Conflicts, 3 = Neutral, 5 = Perfect fit

**Scoring Logic:**
```
Total Score = (Impact + Effort + Alignment) / 3
```

**Recommendation Thresholds:**
- **4.0-5.0:** GO (high confidence)
- **3.0-3.9:** GO WITH CONDITIONS (address primary risk from consilium)
- **2.0-2.9:** NO-GO (low score, not worth effort)
- **1.0-1.9:** STRONG NO-GO (clear mismatch)

**Output:**
- 3 scores (1 line each)
- Total score (1-5 scale)
- Go/NoGo recommendation
- 1-2 conditions (if conditional)

**Time:** 5 minutes

**Example (VK Recipes Bot):**

```
---
QUICK SCORECARD

Impact: 3/5 (Moderate - helpful daily habit, not life-changing)
Effort: 5/5 (Minimal - APIs exist, Telegram bot frameworks ready)
Alignment: 4/5 (Good - fits spare time, matches cooking interest)

Total Score: 4.0/5.0

Recommendation: GO
Conditions:
  - Add retention hook (e.g., user voting on recipes)
  - Handle VK API rate limits (cache daily recipes)
---
```

---

#### Step 4: Complete (1 min)
**Purpose:** Save results, mark idea as evaluated.

**Process:**
1. Save full evaluation to memory:
   ```
   life-os:ideas:{id}:evaluation
     - track: Quick
     - consilium_consensus: {text}
     - score: {total}
     - recommendation: {GO/NOGO}
     - conditions: [{list}]
     - timestamp: {ISO}
   ```

2. Present final summary to user

**Output:**
- Saved evaluation record
- Summary card (10-15 lines)

**Time:** 1 minute

**Example Summary:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUICK TRACK EVALUATION COMPLETE

Idea: VK Recipes Telegram Bot
Track: Quick (17 minutes)

Recommendation: ✅ GO
Score: 4.0/5.0

Key insight:
  Technically simple, good alignment, but needs retention hook
  to prevent user drop-off after 2-3 weeks.

Next actions:
  1. Build MVP (Telegram bot + VK API integration)
  2. Add user voting feature for retention
  3. Implement rate limit caching

Primary risk to manage:
  User retention after novelty wears off (week 2-3)

Evaluation saved to: life-os:ideas:vk-recipes-001
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Step Adjustments Summary

| Step | Status | Modifications |
|------|--------|---------------|
| Step 00 (Goals) | ❌ SKIPPED | Not needed for simple ideas |
| Step 01 (Collect) | ✅ INCLUDED | Full collection (5 min) |
| Step 02 (Roles) | ❌ SKIPPED | No role discovery needed |
| Step 03 (Specialists) | ❌ SKIPPED | Auto-selected in Consilium Lite |
| Step 04 (Consilium) | ✅ LITE MODE | 2-3 specialists, no hats, single-round (5-10 min) |
| Step 04.5 (TRIZ) | ❌ SKIPPED | No TRIZ analysis |
| Step 05 (Scoring) | ✅ SIMPLIFIED | 3 criteria only (Impact/Effort/Alignment) (5 min) |
| Step 06 (Integration) | ❌ SKIPPED | No portfolio integration |
| Step 07 (Calendar) | ❌ SKIPPED | No calendar sync |
| Step 08 (Deep Plan) | ❌ AUTO-SKIP | Not needed for Quick Track (can request if desired) |
| Step 08.5 (Polish) | ❌ SKIPPED | No polish step |
| Step 09 (Complete) | ✅ INCLUDED | Save and summarize (1 min) |

**Time saved:** 80-100 minutes (vs full pipeline)

---

## Output Template

### Quick Track Summary Card

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUICK TRACK EVALUATION

Idea: {title}
Domain: {domain}
Track: Quick ({actual_time} minutes)

───────────────────────────────────────
CONSILIUM LITE (2-3 specialists)

{Specialist 1 Name}:
  ✓ {positive point}
  ⚠ {concern}
  Verdict: {GO/NOGO/CONDITIONAL}

{Specialist 2 Name}:
  ✓ {positive point}
  ⚠ {concern}
  Verdict: {GO/NOGO/CONDITIONAL}

Consensus: {UNANIMOUS GO / MAJORITY GO / SPLIT / MAJORITY NOGO}
  {1-2 sentence key insight}

───────────────────────────────────────
SCORECARD

Impact: {X}/5 ({justification})
Effort: {X}/5 ({justification})
Alignment: {X}/5 ({justification})

Total Score: {average}/5.0

───────────────────────────────────────
RECOMMENDATION: {✅ GO / ⚠️ CONDITIONAL GO / ❌ NO-GO}

{If conditional:}
Conditions to address:
  - {condition 1}
  - {condition 2}

Primary risk to manage:
  {top risk from consilium}

Next actions:
  1. {action 1}
  2. {action 2}
  3. {action 3}

───────────────────────────────────────
Evaluation saved to: life-os:ideas:{id}
Timestamp: {ISO datetime}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Examples

### Example 1: VK Recipes Telegram Bot (Hobby Project)

**Idea Description:**
"I want to make a Telegram bot that sends me a daily recipe from VK cooking communities. Just for myself, to try new dishes."

**Track Detection:**
- Domain: personal/hobby
- Complexity: quick-evaluation
- Resources: solo-spare-time
- Budget: zero
- Stakeholders: 1 (just user)
- Novelty: proven-model

**Result:** Quick Track (score 0.0, confidence 95%)

**Quick Track Evaluation:**

**Consilium Lite (7 min):**
- Tech Architect: GO (simple APIs, low complexity, watch rate limits)
- Product Strategist: GO (clear value, retention risk after 2-3 weeks)
- Consensus: MAJORITY GO

**Scorecard:**
- Impact: 3/5 (helpful daily habit)
- Effort: 5/5 (minimal, APIs ready)
- Alignment: 4/5 (good fit for spare time)
- **Total: 4.0/5.0**

**Recommendation:** ✅ GO
**Conditions:**
- Add retention feature (voting/favorites)
- Cache recipes to handle rate limits

**Total time:** 17 minutes

---

### Example 2: Personal Fitness Tracking Habit (Ultra-Simple)

**Idea Description:**
"I just want to start tracking my workouts. Nothing fancy, maybe a spreadsheet or simple app."

**Track Detection:**
- Domain: personal
- Complexity: quick-evaluation ("nothing fancy")
- Resources: solo-spare-time
- Budget: zero
- Stakeholders: 1
- Novelty: proven-model

**Result:** Quick Track (score 0.0, confidence 97%)

**Quick Track Evaluation:**

**Consilium Lite (5 min):**
- Life Coach: GO (clear habit goal, start simple)
- General Advisor: GO (spreadsheet works, don't overcomplicate)
- Consensus: UNANIMOUS GO

**Scorecard:**
- Impact: 4/5 (high for personal health)
- Effort: 5/5 (spreadsheet = 30 min setup)
- Alignment: 5/5 (personal priority)
- **Total: 4.7/5.0**

**Recommendation:** ✅ GO (strong)
**Next actions:**
1. Create spreadsheet template (exercises, sets, reps, date)
2. Set daily reminder
3. Track for 2 weeks, review habit

**Total time:** 15 minutes

---

### Example 3: Freelance Portfolio Website (Boundary Case)

**Idea Description:**
"I need a portfolio site for my freelance design work. Want to attract enterprise clients. Budget around 200K RUB."

**Track Detection:**
- Domain: freelance
- Complexity: standard-analysis (inferred from "enterprise clients")
- Resources: solo-focused
- Budget: medium (200K)
- Stakeholders: 2-3 (freelancer + target clients)
- Novelty: proven-model

**Result:** Standard Track (score 9.0, confidence 87%)

**Note:** User could override to Quick Track, but system recommends Standard because:
- Enterprise clients = higher stakes (needs specialist input on positioning)
- 200K budget = non-trivial investment (needs risk analysis)

**If user chooses Quick Track anyway:**

System shows brief risk notice:
```
⚠️ Note: Quick track skips role discovery and portfolio integration.
   For enterprise positioning, Standard track is recommended.

   Proceed with Quick Track? [Y/N]
```

If user confirms Y:

**Consilium Lite (8 min):**
- Business Advisor: CONDITIONAL (enterprise needs case studies, testimonials)
- Market Analyst: CONDITIONAL (positioning unclear, research competitors)
- Consensus: MAJORITY CONDITIONAL

**Scorecard:**
- Impact: 4/5 (critical for business growth)
- Effort: 3/5 (moderate with 200K budget)
- Alignment: 4/5 (matches business need)
- **Total: 3.7/5.0**

**Recommendation:** ⚠️ CONDITIONAL GO
**Conditions:**
- Research 3-5 competitors (enterprise positioning)
- Gather 2-3 case studies / testimonials first
- Define clear enterprise value proposition

**Total time:** 19 minutes

**Escalation trigger:** During Consilium, if user reveals they're unsure about platform choice (Webflow vs custom), system offers upgrade to Standard Track for deeper analysis.

---

### Example 4: Daily Journaling Habit (Ultra-Quick)

**Idea Description:**
"Want to journal daily. Just bullet points, nothing structured."

**Track Detection:**
- Domain: personal
- Complexity: quick-evaluation
- Resources: solo-spare-time
- Budget: zero
- Stakeholders: 1
- Novelty: proven-model

**Result:** Quick Track (score 0.0, confidence 97%)

**Quick Track Evaluation:**

**Consilium Lite (5 min):**
- Life Coach: GO (proven habit, start immediately)
- General Advisor: GO (use any tool, consistency matters more)
- Consensus: UNANIMOUS GO

**Scorecard:**
- Impact: 4/5 (high for mental clarity)
- Effort: 5/5 (5 min daily)
- Alignment: 5/5 (fits any schedule)
- **Total: 4.7/5.0**

**Recommendation:** ✅ GO (strong)
**Next actions:**
1. Pick tool (paper notebook OR notes app)
2. Set daily reminder (evening)
3. Start tonight (3 bullet points minimum)

**Total time:** 15 minutes

---

## Integration with Track Detection Algorithm

### When Quick Track is Triggered

Quick Track is selected when:
1. **Score 0.0-5.0** in track detection algorithm
2. **OR** User explicitly requests "quick evaluation"
3. **OR** Deterministic Rule 4 matches (personal/hobby + solo-spare-time + zero budget)

### Routing After Step 01

After Step 01 completes and track is selected:

```
IF user_choice == "Quick Track":
  workflow_plan.track = "quick"
  workflow_plan.steps = [1, "4lite", 5, 9]
  workflow_plan.estimated_time = "15-20 min"

  LOAD step-04-consilium.md WITH flag: track="quick"
  # Step 04 detects "quick" flag and runs Consilium Lite mode
```

### Memory Storage

After Quick Track completes, save to memory:

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:ideas:{id}:quick-evaluation" \
  --content "{
    \"track\": \"quick\",
    \"duration_minutes\": {actual_time},
    \"consilium_consensus\": \"{consensus_text}\",
    \"score\": {total_score},
    \"recommendation\": \"{GO/NOGO/CONDITIONAL}\",
    \"conditions\": [{conditions}],
    \"primary_risk\": \"{risk}\",
    \"timestamp\": \"{ISO}\"
  }"
```

---

## Success Criteria

### Quick Track is Successful When:

1. ✅ **Time target met:** 15-20 minutes end-to-end
2. ✅ **Clear decision:** User gets unambiguous GO/NOGO/CONDITIONAL
3. ✅ **Actionable output:** User knows exactly what to do next
4. ✅ **Risk identified:** Primary risk flagged (even if simple)
5. ✅ **No regret:** User doesn't feel they "missed" deep analysis

### Quality Gates

| Gate | Check | Pass Criteria |
|------|-------|---------------|
| Consilium quality | Specialists relevant to domain | Auto-selection matches domain map |
| Consilium quality | Consensus is clear | Agreement level stated (unanimous/majority/split) |
| Scoring quality | Scores justified | Each score has 1-sentence justification |
| Recommendation clarity | Next actions are concrete | 2-3 specific actions listed |
| Risk visibility | Primary risk flagged | At least 1 risk identified |

### When Quick Track Should Escalate

If during Quick Track execution any of these occur, offer upgrade to Standard Track:

1. **Consilium divergence:** Specialists disagree >50% (e.g., one GO, one NOGO)
2. **Hidden complexity revealed:** User mentions investors, team, or >500K budget
3. **User requests depth:** User asks "can we analyze this more?"
4. **Ambiguous domain:** System can't confidently auto-select specialists

---

## Appendix: Quick Track Time Breakdown

| Step | Minimum | Maximum | Average |
|------|---------|---------|---------|
| Step 01 (Collect) | 3 min | 7 min | 5 min |
| Track detection & selection | 1 min | 2 min | 1 min |
| Step 04lite (Consilium Lite) | 4 min | 12 min | 7 min |
| Step 05 (Simplified Scoring) | 3 min | 7 min | 5 min |
| Step 09 (Complete) | 1 min | 2 min | 1 min |
| **TOTAL** | **12 min** | **30 min** | **19 min** |

**Target:** 15-20 minutes (achieved in 85% of cases based on time estimates)

**Note:** Actual time may vary if:
- User asks clarifying questions during consilium
- Specialists reveal unexpected complexity (triggers escalation)
- User takes time to read recommendations

---

## Appendix: Comparison to Full Pipeline

| Aspect | Full Pipeline | Quick Track | Savings |
|--------|---------------|-------------|---------|
| **Steps** | 9 steps (or 11 with Deep) | 4 steps | -56% |
| **Time** | 100+ minutes | 15-20 minutes | -80-85% |
| **Specialists** | 3-5, user-selected | 2-3, auto-selected | -40% |
| **Scoring criteria** | 7-10 criteria | 3 criteria | -60% |
| **Output length** | 500-1000 lines | 50-100 lines | -80-90% |
| **Depth** | Full analysis | Key insights only | Focused |

**Use Quick Track when:** You need speed and the idea is simple.
**Use Standard Track when:** You need specialist input and moderate depth.
**Use Deep Track when:** You need full planning and the stakes are high.
