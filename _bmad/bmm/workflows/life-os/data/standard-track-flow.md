---
name: 'standard-track-flow'
version: '1.0'
track: 'Standard'
target_duration: '45-60 minutes'
purpose: 'Balanced evaluation for medium-complexity ideas with moderate stakes'
consumedBy:
  - step-01-collect-ideas.md
  - track-detection-algorithm.md
  - step-02-roles-discovery.md
  - step-04-consilium.md
whenToUse: 'Ideas requiring structured analysis but not deep planning'
---

# Standard Track Flow

## Overview

The Standard Track is the **balanced middle path** between Quick Track's rapid validation and Deep Track's exhaustive analysis. It provides structured specialist input, full scoring, and portfolio integration without the time commitment of deep planning and calendar synchronization.

**Target Time:** 45-60 minutes
**Ideal For:** Freelance projects, small business initiatives, moderate-stakes software projects, ideas with some unknowns that warrant proper evaluation.

---

## Pipeline Steps

The Standard Track follows this 7-step pipeline:

```
Step 01 (Collect) → Step 02 (Roles) → Step 03 (Specialists) → Step 04 (Consilium) →
Step 05 (Scoring) → Step 06 (Integration) → Step 09 (Complete)
```

### Skipped Steps (Compared to Deep Track)

- **Step 00 (Goals Discovery):** Deferred. Goals alignment checked but not discovered.
- **Step 04.5 (TRIZ):** Available on request but not prompted proactively.
- **Step 07 (Calendar Sync):** Deferred. User can request later if project moves forward.
- **Step 08 (Deep Plan):** L1-L3 DEFAULT (10-15 min high-level plan). L4-L6 available on request but rarely needed.
- **Step 08.5 (Final Polish):** Skipped for L1-L3 plans (only needed for full L1-L6).

---

## Step-by-Step Breakdown with Time Estimates

### 1. Step 01: Collect Ideas (5 minutes)
**Purpose:** Capture the idea with sufficient detail for evaluation.

**Process:**
1. Run standard Collect Ideas process (domain, timeline, resources, context)
2. Track detection algorithm triggers after save
3. System recommends Standard Track based on scoring/rules
4. User confirms or overrides track selection

**Output:**
- Idea record saved to memory
- Track selection confirmed
- Workflow plan initialized with Standard track flag

**Time Allocation:** 5 minutes

---

### 2. Step 02: Roles Discovery (5 minutes)
**Purpose:** Identify roles the user will play in this project.

**Process:**
1. Extract roles from idea description automatically
2. Auto-generate 3-5 key roles based on domain
3. User reviews and confirms roles
4. Save roles to workflow plan

**Standard Track Adjustments:**
- Auto-role generation is MORE aggressive (fewer manual prompts)
- User confirmation is streamlined (accept/reject batch)
- Time target: 5 minutes MAX (vs 8-10 min in Deep Track)

**Output:**
- 3-5 confirmed roles
- Roles saved to idea record

**Time Allocation:** 5 minutes

---

### 3. Step 03: Specialist Matching (5 minutes)
**Purpose:** Map roles to specialist types for consilium.

**Process:**
1. Auto-match roles to specialists using GDS-CONSILIUM-SPECIALISTS.md
2. Add 1-2 cross-functional specialists for broader perspective
3. Present 4-6 specialists total
4. User confirms specialist selection

**Standard Track Adjustments:**
- Specialist count: **4-6** (vs 6-8 in Deep Track)
- Auto-match confidence threshold: **75%** (higher than Deep's 65%)
- User must only confirm/override; no manual search

**Output:**
- 4-6 specialists selected
- Specialists saved to workflow plan

**Time Allocation:** 5 minutes

---

### 4. Step 04: Consilium (15-20 minutes)
**Purpose:** Multi-perspective analysis with structured Six Hats thinking.

**Process:**
1. Assign Six Thinking Hats to specialists
2. Each specialist provides recommendations in their hat's perspective
3. Synthesize consilium results into actionable recommendations
4. Identify consensus points and divergent views
5. Save consilium output to workflow plan

**Standard Track Adjustments:**

| Aspect | Standard Track | Deep Track | Quick Track |
|--------|----------------|------------|-------------|
| **Specialists** | 4-6 | 6-8 | 2-3 (no hats) |
| **Six Hats** | YES (full) | YES (full) | NO |
| **Rounds** | Single round | Multi-round if contradictions | Single recommendation |
| **TRIZ** | Available on request, NOT prompted | Auto-prompted if contradictions | Not available |
| **Auto-Suggest Engine** | NOT triggered | Triggered after consilium | Not triggered |
| **Elicitation Methods** | Standard menu (no Advanced) | Full menu + Advanced | No menu |
| **Party Mode** | Available | Available | Not available |
| **Synthesis Depth** | 1-2 paragraphs per hat + 3-5 recommendations | 2-3 paragraphs per hat + 8-10 recommendations | 1-2 bullet points total |

**Six Hats Assignment:**
- White Hat (Facts/Data): 1 specialist
- Red Hat (Emotions/Intuition): 1 specialist
- Black Hat (Risks/Caution): 1 specialist
- Yellow Hat (Benefits/Optimism): 1 specialist
- Green Hat (Creativity/Alternatives): 1 specialist
- Blue Hat (Process/Meta-thinking): Automatically assigned to System

**Output Format:**
```markdown
## Consilium Results

### Specialist Recommendations

#### [Hat Color] - [Specialist Name]
[1-2 paragraph recommendation focused on hat's perspective]

### Synthesis
[2-3 paragraphs integrating all perspectives]

### Key Recommendations
1. [Actionable recommendation]
2. [Actionable recommendation]
3. [Actionable recommendation]

### Divergence Points
- [Any major disagreements between specialists]
```

**Time Allocation:** 15-20 minutes

---

### 5. Step 05: Scoring (10 minutes)
**Purpose:** Quantitative evaluation using MCDA (Multi-Criteria Decision Analysis).

**Process:**
1. Load standard 9 criteria: Impact, Effort, Alignment, Risk, Market Viability, Resource Availability, Learning Value, Urgency, Strategic Fit
2. Auto-add 1-2 domain-specific criteria if applicable
3. User scores each criterion (0-5 scale)
4. System calculates weighted total and normalizes to 100-point scale
5. Generate recommendation based on score thresholds

**Standard Track Adjustments:**
- Full scoring (all 9 base criteria + domain-specific)
- No simplification (vs Quick Track's 3-criteria only)
- Criteria weights: STANDARD profile (balanced, not domain-optimized like Deep Track)
- Auto-score suggestions based on consilium findings

**Standard Criteria Weights:**

| Criterion | Weight | Rationale |
|-----------|--------|-----------|
| Impact | 15% | Moderate importance (not as high as Deep Track's 20%) |
| Alignment | 15% | Moderate importance (goals assumed mostly aligned) |
| Effort | 12% | Important but not dominant |
| Risk | 12% | Balanced risk consideration |
| Market Viability | 10% | Important for business ideas |
| Resource Availability | 10% | Practical constraint check |
| Learning Value | 8% | Nice-to-have |
| Urgency | 8% | Moderate time pressure |
| Strategic Fit | 10% | Medium-term perspective |

**Score Interpretation (Standard Track):**

| Total Score | Recommendation | Action |
|-------------|---------------|--------|
| 80-100 | **GO** (Strong) | Proceed immediately. High confidence. |
| 65-79 | **GO** (Conditional) | Proceed with risk mitigation from Black Hat. |
| 50-64 | **EVALUATE** | Address top 2-3 weaknesses before deciding. |
| 35-49 | **DEFER** | Not ready. Revisit after 1-2 months. |
| 0-34 | **NO-GO** | Reject or pivot significantly. |

**Output:**
- Scored criteria table
- Weighted total (0-100)
- Recommendation (GO/EVALUATE/DEFER/NO-GO)
- Top 3 strengths and top 3 weaknesses

**Time Allocation:** 10 minutes

---

### 6. Step 06: Portfolio Integration (10 minutes)

**NOTE:** Step 08 (Deep Plan L1-L3) is NOW INCLUDED in Standard Track by default. See section 6.5 below.

### 6.5. Step 08: Deep Plan L1-L3 (10-15 minutes) - NEW DEFAULT

**Purpose:** Create high-level roadmap with major phases and key milestones.

**Standard Track Change (v3.1):**
- **OLD:** Step 08 completely skipped
- **NEW:** Step 08 L1-L3 included by default (10-15 min)
- **Impact:** Standard Track time increases from 45-60 min to 55-75 min
- **Benefit:** Users get actionable plan without full L1-L6 time investment

**What's Included in L1-L3:**
- **L1: High-Level Overview** (2-3 paragraphs)
  - What: Brief description of what we're building
  - Why: Why this approach, key decisions
  - How: High-level technical approach
- **L2: Major Phases** (3-5 phases)
  - Phase name, duration estimate, goal, key activities
- **L3: Key Milestones** (5-8 milestones)
  - Milestone name, target date, success criteria, deliverables

**What's NOT Included (L4-L6):**
- L4: Stages for each work stream (detailed breakdown)
- L5: Tasks for each stage (task-level detail)
- L6: Atomic actions (step-by-step instructions)

**Process:**
1. System detects Standard Track from workflow plan
2. Presents depth selection menu:
   ```
   Deep Plan Depth Selection:

   [A]ccept L1-L3 (recommended for Standard track) - 10-15 min
   [F]ull L1-L6 (comprehensive deep plan) - 20-60 min
   [S]kip Deep Plan (not recommended)

   Your choice: [A/F/S]
   ```
3. If [A]ccept: Load L1-L3 template, build basic plan
4. If [F]ull: Show warning, confirm intent, load L1-L6 template
5. If [S]kip: Confirm skip, mark `deep_plan_skipped: true`

**Override Warning (if user selects [F]):**
```
⚠️ You selected Standard Track but requested L1-L6 Deep Plan.

This adds 40-50 minutes. Consider:
- L1-L3 is sufficient for most Standard Track ideas
- L4-L6 adds detailed task breakdowns (100+ tasks)
- You can always return later to deepen the plan

Proceed with L1-L6?
[Y]es, I need full detail
[N]o, use L1-L3 (recommended)
```

**Output:**
- Plan saved to workflow plan under "Deep Plan (L1-L3)"
- Summary includes: total duration, critical path, top 3 risks
- Quality metrics: phases count, milestones count

**Time Allocation:** 10-15 minutes

---

### 7. Step 06: Portfolio Integration (10 minutes) - RENUMBERED
**Purpose:** Ensure this idea fits within the user's broader project portfolio.

**Process:**
1. Check portfolio health (WIP count, active projects)
2. Load existing goals from memory (if Step 00 was done in past)
3. Evaluate alignment with goals (quick check, not full discovery)
4. Check for conflicts with active projects
5. Generate integration recommendation

**Standard Track Adjustments:**

| Check | Standard Track | Deep Track | Quick Track |
|-------|----------------|------------|-------------|
| **WIP Limit** | Check & warn if exceeded | Full WIP analysis + rebalancing | Skipped |
| **Goals Alignment** | Quick check (if goals exist) | Full goal discovery if missing | Skipped |
| **Active Project Conflicts** | Check for resource/time conflicts | Full dependency mapping | Skipped |
| **Strategic Fit** | Inferred from scoring | Deep strategic roadmap analysis | Skipped |
| **Recommendation** | GO/DEFER/ADJUST (simple) | GO/DEFER/ADJUST/ESCALATE (complex) | Not applicable |

**Portfolio Health Checks:**
1. **WIP Count:** How many active projects? (Warn if >5)
2. **Resource Overlap:** Does this compete with existing projects for time/money?
3. **Goal Alignment:** Does it support existing goals (if goals were discovered)?
4. **Timeline Conflicts:** Any calendar conflicts (inferred from descriptions)?

**Integration Outcomes:**

| Outcome | Meaning | Action |
|---------|---------|--------|
| **CLEAR** | No conflicts, portfolio is healthy | Proceed with idea |
| **ADJUST** | Minor conflict (e.g., WIP limit) | Suggest deprioritizing one current project |
| **DEFER** | Major conflict (e.g., same resource needed) | Wait until current project completes |

**Output:**
```markdown
## Portfolio Integration Check

**WIP Status:** {N} active projects (Limit: 5)
**Resource Conflicts:** {Yes/No - description}
**Goal Alignment:** {Aligned/Neutral/Misaligned}
**Recommendation:** {CLEAR/ADJUST/DEFER}

{If ADJUST or DEFER, explain what needs to change}
```

**Time Allocation:** 10 minutes

---

### 7. Step 09: Complete Idea (1 minute)
**Purpose:** Finalize workflow plan and save all outputs.

**Process:**
1. Mark workflow plan as COMPLETE
2. Append final summary to workflow plan
3. Save workflow plan to memory
4. Present final summary to user

**Output:**
```markdown
## Final Summary (Standard Track)

**Idea:** {title}
**Track:** Standard
**Time Spent:** {actual_minutes} minutes
**Score:** {total}/100
**Recommendation:** {GO/EVALUATE/DEFER/NO-GO}

**Key Findings:**
- {Top consilium recommendation}
- {Top strength from scoring}
- {Top risk from Black Hat}

**Next Steps:**
{If GO: suggest starting with Step 07 (Calendar) or Step 08 (Deep Plan) if user wants detail}
{If EVALUATE: list the 2-3 things to address}
{If DEFER/NO-GO: explain why and when to revisit}

**Outputs Created:**
- Consilium results ({N} specialists, Six Hats analysis)
- Scoring report (9 criteria + {N} domain-specific)
- Portfolio integration check

**Workflow plan saved to:**
life-os:workflow:{IDEA_ID}
```

**Time Allocation:** 1 minute

---

## Total Time Breakdown

| Step | Time Estimate | Cumulative |
|------|--------------|------------|
| Step 01 (Collect) | 5 min | 5 min |
| Track Detection | 1 min | 6 min |
| Step 02 (Roles) | 5 min | 11 min |
| Step 03 (Specialists) | 5 min | 16 min |
| Step 04 (Consilium) | 15-20 min | 31-36 min |
| Step 05 (Scoring) | 10 min | 41-46 min |
| Step 06 (Integration) | 10 min | 51-56 min |
| Step 09 (Complete) | 1 min | **52-57 min** |

**Target Range:** 45-60 minutes
**Typical Completion:** 52-57 minutes (falls within target)

---

## Comparison to Other Tracks

### Standard vs Quick Track

| Aspect | Quick Track | Standard Track |
|--------|-------------|----------------|
| **Time** | 15-20 min | 45-60 min |
| **Specialists** | 2-3 (auto-selected) | 4-6 (confirmed by user) |
| **Six Hats** | NO | YES |
| **Scoring Criteria** | 3 (simplified) | 9 base + domain-specific |
| **Portfolio Integration** | Skipped | Full check |
| **TRIZ** | Not available | Available on request |
| **Output Depth** | 1-2 bullet points | 3-5 recommendations + synthesis |
| **When to Use** | Simple, low-risk ideas | Medium complexity, moderate stakes |

### Standard vs Deep Track

| Aspect | Standard Track | Deep Track |
|--------|----------------|------------|
| **Time** | 45-60 min | 2-4 hours |
| **Goals Discovery** | Skipped (assumes existing) | Full discovery if missing |
| **Consilium Depth** | Single round, 4-6 specialists | Multi-round, 6-8 specialists |
| **TRIZ** | On request, not prompted | Auto-prompted if contradictions |
| **Auto-Suggest Engine** | Not triggered | Triggered post-consilium |
| **Deep Plan (Step 08)** | Skipped | Full L1-L6 breakdown |
| **Calendar Sync** | Skipped | Full integration |
| **Scenario Mapping** | No | Yes |
| **When to Use** | Medium complexity | High-stakes, complex projects |

---

## When to Use Standard Track

### Ideal Scenarios

1. **Freelance Projects**
   - Building a portfolio website
   - Launching a new service offering
   - Productizing a consulting practice
   - Creating online courses

2. **Small Business Initiatives**
   - Opening a second location
   - Launching a new product line
   - Implementing a CRM system
   - Hiring the first employee

3. **Software Projects (Moderate Scope)**
   - Building an MVP for a known market
   - Refactoring a legacy system
   - Adding a major feature to existing product
   - Migrating to a new tech stack

4. **Personal Projects with Stakes**
   - Writing and publishing a book
   - Creating a YouTube channel for education
   - Building a rental property portfolio
   - Learning a high-value skill (e.g., ML engineering)

### Signal Patterns

The track detection algorithm recommends Standard Track when:

**Scoring Matrix:**
- Total score: **5.1 to 12.0 points**
- Most common profile: domain=freelance/small-business/software, complexity=standard-analysis, resource=solo-focused/small-team

**Deterministic Rules:**
- No explicit "quick" or "deep" request from user
- Domain is NOT personal/hobby AND NOT enterprise
- Budget is medium (100K-1M RUB)
- Stakeholder count is 2-3
- Novelty is adaptation (not proven-model, not breakthrough)

### User Language Patterns

Users likely to need Standard Track say things like:
- "I want to evaluate this properly"
- "Need to understand if this is worth pursuing"
- "Want structured feedback before committing"
- "Should I build this or not?"
- "Need to convince myself (or a partner) this makes sense"

---

## Output Templates

### 1. Consilium Output Template (Standard Track)

```markdown
# Consilium Results: [Idea Title]

**Date:** {ISO date}
**Track:** Standard
**Specialists:** {N}
**Duration:** {actual_minutes} min

---

## Specialist Recommendations

### 🤍 White Hat - [Specialist Name] (Facts & Data)
[1-2 paragraphs: What are the objective facts? Market data? Resources needed? Constraints?]

**Key Facts:**
- {Fact 1}
- {Fact 2}
- {Fact 3}

---

### ❤️ Red Hat - [Specialist Name] (Emotions & Intuition)
[1-2 paragraphs: How does this feel? Gut reactions? Excitement or concern? User's emotional readiness?]

**Emotional Signals:**
- {Signal 1}
- {Signal 2}

---

### 🖤 Black Hat - [Specialist Name] (Risks & Caution)
[1-2 paragraphs: What could go wrong? Risks? Downsides? Realistic challenges?]

**Top Risks:**
1. {Risk 1}
2. {Risk 2}
3. {Risk 3}

---

### 💛 Yellow Hat - [Specialist Name] (Benefits & Optimism)
[1-2 paragraphs: Why this could succeed? Opportunities? Unique advantages? Upside potential?]

**Key Benefits:**
- {Benefit 1}
- {Benefit 2}
- {Benefit 3}

---

### 💚 Green Hat - [Specialist Name] (Creativity & Alternatives)
[1-2 paragraphs: Creative alternatives? Pivots? Unexpected approaches? Blue-sky thinking?]

**Creative Options:**
1. {Alternative approach 1}
2. {Alternative approach 2}

---

### 💙 Blue Hat - System (Process & Meta-Thinking)
[1 paragraph: How is this consilium going? Are we covering everything? What's missing?]

**Process Notes:**
- {Meta-observation 1}
- {Meta-observation 2}

---

## Synthesis

[2-3 paragraphs integrating all hat perspectives into a coherent view]

**Consensus Points:**
- {Point where all hats agree}
- {Another consensus point}

**Divergent Views:**
- {Where specialists disagree and why}

---

## Key Recommendations

1. **[Actionable Recommendation 1]**
   - From: [Hat colors]
   - Rationale: {1 sentence}

2. **[Actionable Recommendation 2]**
   - From: [Hat colors]
   - Rationale: {1 sentence}

3. **[Actionable Recommendation 3]**
   - From: [Hat colors]
   - Rationale: {1 sentence}

---

## Next Steps

- Proceed to Step 05 (Scoring) with these insights
- Consider {specific recommendation} from consilium before scoring
```

---

### 2. Scoring Report Template (Standard Track)

```markdown
# Scoring Report: [Idea Title]

**Date:** {ISO date}
**Track:** Standard
**Criteria:** 9 base + {N} domain-specific
**Scoring Method:** MCDA (Multi-Criteria Decision Analysis)

---

## Criteria Scores

| Criterion | Weight | Score (0-5) | Weighted Score | Notes |
|-----------|--------|-------------|----------------|-------|
| Impact | 15% | {X} | {X * 0.15} | {Brief justification} |
| Alignment | 15% | {X} | {X * 0.15} | {Brief justification} |
| Effort | 12% | {X} | {X * 0.12} | {Brief justification} |
| Risk | 12% | {X} | {X * 0.12} | {Brief justification} |
| Market Viability | 10% | {X} | {X * 0.10} | {Brief justification} |
| Resource Availability | 10% | {X} | {X * 0.10} | {Brief justification} |
| Learning Value | 8% | {X} | {X * 0.08} | {Brief justification} |
| Urgency | 8% | {X} | {X * 0.08} | {Brief justification} |
| Strategic Fit | 10% | {X} | {X * 0.10} | {Brief justification} |
| {Domain-Specific 1} | {%} | {X} | {weighted} | {Brief justification} |

---

## Total Score

**Raw Score:** {sum of weighted scores} / 5.0
**Normalized (0-100):** {total} / 100

---

## Interpretation

**Recommendation:** {GO/EVALUATE/DEFER/NO-GO}

{If GO:}
This idea scores well across most criteria. Proceed with confidence.
Address these minor risks: {list from Black Hat}.

{If EVALUATE:}
This idea has potential but needs work in these areas:
1. {Weakness 1}: {How to address}
2. {Weakness 2}: {How to address}
3. {Weakness 3}: {How to address}

Revisit scoring after addressing these gaps.

{If DEFER:}
Not ready yet. Key blockers:
- {Blocker 1}
- {Blocker 2}
Revisit in {N} months when {condition}.

{If NO-GO:}
This idea does not meet the threshold. Consider:
- Pivoting to {alternative approach from Green Hat}
- Dropping this idea and focusing on {higher-priority project}

---

## Strengths (Top 3)

1. **{Criterion with highest score}:** {Why this is a strength}
2. **{Second-highest criterion}:** {Why this is a strength}
3. **{Third-highest criterion}:** {Why this is a strength}

---

## Weaknesses (Top 3)

1. **{Criterion with lowest score}:** {Why this is a weakness and how to improve}
2. **{Second-lowest criterion}:** {Why this is a weakness and how to improve}
3. **{Third-lowest criterion}:** {Why this is a weakness and how to improve}

---

## Consilium Alignment Check

{Compare scoring results with consilium recommendations. Are they consistent?}

**Consistency:** {High/Medium/Low}
{If Low: explain the discrepancy and which source to trust more}

---

## Next Steps

- Proceed to Step 06 (Portfolio Integration)
- {If EVALUATE: Address weaknesses before moving forward}
- {If DEFER/NO-GO: Archive this idea or pivot}
```

---

### 3. Portfolio Integration Report Template (Standard Track)

```markdown
# Portfolio Integration Check: [Idea Title]

**Date:** {ISO date}
**Track:** Standard
**Current WIP:** {N} active projects

---

## Portfolio Health

| Metric | Status | Notes |
|--------|--------|-------|
| **Active Projects (WIP)** | {N} / 5 | {✅ Healthy / ⚠️ At limit / ❌ Overloaded} |
| **Resource Availability** | {Available/Constrained/Blocked} | {Details} |
| **Goal Alignment** | {Aligned/Neutral/Misaligned} | {If goals exist, reference them} |
| **Timeline Conflicts** | {None/Minor/Major} | {Details} |

---

## Active Projects

1. **{Project 1}:** {Status} - {Brief description}
2. **{Project 2}:** {Status} - {Brief description}
3. **{Project 3}:** {Status} - {Brief description}

---

## Conflict Analysis

### Resource Conflicts
{Does this idea compete for time/money/attention with existing projects?}

**Result:** {No conflicts / Minor overlap / Major conflict}

{If conflict exists:}
- Conflicting project: {name}
- Resource: {time/money/skills}
- Severity: {Low/Medium/High}

---

### Goal Alignment
{If goals were discovered in Step 00:}

**Primary Goal:** {Goal from memory}
**Alignment:** {This idea supports/is neutral to/conflicts with this goal}

{If goals NOT discovered:}
Goals have not been discovered in this session.
Alignment check deferred.

---

### Timeline Assessment
{Are there scheduling conflicts based on idea timelines?}

**This Idea Timeline:** {From Step 01}
**Potential Conflicts:** {Yes/No - details}

---

## Integration Recommendation

**Outcome:** {CLEAR / ADJUST / DEFER}

{If CLEAR:}
✅ No conflicts detected. This idea fits well in your current portfolio.
Proceed with implementation planning (or request Step 08 Deep Plan).

{If ADJUST:}
⚠️ Minor adjustment needed:
- {Action 1}: {e.g., Deprioritize Project X to make room}
- {Action 2}: {e.g., Delay start by 2 weeks to avoid resource conflict}

{If DEFER:}
❌ Major conflict detected. Recommend deferring this idea until:
- {Condition 1}: {e.g., Project X completes (estimated {date})}
- {Condition 2}: {e.g., Budget frees up after Q2}

---

## Next Steps

{If CLEAR:}
- Mark idea as READY
- Proceed to Step 09 (Complete)
- Optionally request Step 07 (Calendar Sync) or Step 08 (Deep Plan)

{If ADJUST:}
- Make recommended adjustments
- Re-check integration
- Then proceed to Step 09

{If DEFER:}
- Archive this idea with DEFERRED status
- Set reminder for {date}
- Focus on completing {blocking project}
```

---

## Examples of Standard Track Ideas

### Example 1: Freelance Design Portfolio Website

**Idea:** "I want to build a portfolio website for my freelance design business to attract enterprise clients. Budget around 200K RUB."

**Why Standard Track:**
- Domain: freelance (1 pt * 2.0 = 2.0)
- Complexity: standard-analysis (1 pt * 3.0 = 3.0)
- Resource: solo-focused (1 pt * 1.5 = 1.5)
- Budget: medium (1 pt * 1.5 = 1.5)
- Stakeholders: 2-3 (1 pt * 1.0 = 1.0)
- Novelty: proven-model (0 pt * 1.0 = 0.0)
- **Total: 9.0** → Standard Track

**What Standard Track Provides:**
- 4-6 specialists (Web Designer, Business Advisor, UX Strategist, SEO Specialist, Brand Consultant)
- Six Hats consilium (addresses both design AND business strategy)
- Full scoring (Impact, Alignment, Effort, Risk, Market Viability, etc.)
- Portfolio integration (does this fit with other freelance commitments?)
- Output: Clear GO/NO-GO with actionable recommendations

**What's Skipped (vs Deep Track):**
- No Step 00 Goals Discovery (assumes freelancer knows their goals)
- No Step 08 Deep Plan L1-L6 (portfolio site doesn't need 6-month breakdown)
- No Step 07 Calendar Sync (freelancer can schedule themselves)

**Time:** 52 minutes (vs 2+ hours in Deep Track)

---

### Example 2: Online Course on Russian Cuisine

**Idea:** "I want to create an online course teaching Russian cuisine. I'm a professional chef. Thinking about Udemy or my own platform. Maybe a small team of 2."

**Why Standard Track:**
- Domain: small-business (1 pt * 2.0 = 2.0)
- Complexity: standard-analysis (1 pt * 3.0 = 3.0)
- Resource: small-team (2 pts * 1.5 = 3.0)
- Budget: low (0 pts * 1.5 = 0.0)
- Stakeholders: 2-3 (1 pt * 1.0 = 1.0)
- Novelty: adaptation (1 pt * 1.0 = 1.0)
- **Total: 10.0** → Standard Track

**What Standard Track Provides:**
- Specialists: Education Specialist, Market Analyst, Content Strategist, Tech Advisor, Brand Consultant
- Six Hats perspective on Udemy vs own platform decision
- Scoring that balances effort (creating content) vs impact (revenue potential)
- Portfolio check (does chef have time alongside current restaurant work?)
- Output: Platform recommendation + go/no-go

**Escalation Potential:**
If during consilium the chef reveals they want to build a full edtech platform (not just a course), track escalation trigger fires and system offers Deep Track upgrade.

**Time:** 55 minutes

---

### Example 3: Implementing a CRM for Small Business

**Idea:** "Our small business (10 employees) needs a CRM system. Looking at HubSpot or Salesforce. Budget is ~500K RUB for setup + first year."

**Why Standard Track:**
- Domain: small-business (1 pt * 2.0 = 2.0)
- Complexity: standard-analysis (1 pt * 3.0 = 3.0)
- Resource: small-team (2 pts * 1.5 = 3.0)
- Budget: medium (1 pt * 1.5 = 1.5)
- Stakeholders: 4+ (10 employees) (2 pts * 1.0 = 2.0)
- Novelty: proven-model (0 pts * 1.0 = 0.0)
- **Total: 11.5** → Standard Track (near Deep boundary)

**What Standard Track Provides:**
- Specialists: CRM Consultant, Tech Integration Specialist, Change Management Advisor, Finance Analyst
- Six Hats analysis of HubSpot vs Salesforce
- Scoring that weighs employee adoption (Change Hat) vs technical fit (Tech Hat)
- Portfolio check (is business ready for this disruption now or after Q1?)
- Output: CRM vendor recommendation + implementation readiness

**Why Not Deep Track:**
- CRM implementations are well-understood (proven-model)
- No breakthrough innovation required
- Small team can make decisions quickly
- Total score is 11.5 (below 12.1 Deep threshold)

**Time:** 58 minutes

---

## Escalation Scenarios

The Standard Track can escalate to Deep Track mid-pipeline if:

### Trigger 1: Consilium Reveals Hidden Complexity
**Example:** During Six Hats discussion of the online course idea, the Education Specialist reveals that launching on Udemy requires competing with 1000+ existing courses, and building own platform would require custom learning management system, payment processing, and marketing funnel.

**System Response:**
```
---------------------------------------------------
TRACK ESCALATION NOTICE

During Step 04 (Consilium), I detected that this idea
may need deeper analysis than the Standard track provides.

  Trigger: Platform decision involves complex trade-offs
  Current track: Standard
  Suggested upgrade: Deep Track

  What changes:
  + Step 08 (Deep Plan) added: L1-L6 breakdown for platform build
  + Step 07 (Calendar Sync) added: Timeline for content creation
  + Additional 90-120 minutes estimated

  [U] Upgrade to Deep Track
  [K] Keep Standard Track (I'll decide platform later)

  Your choice: [U/K]
---------------------------------------------------
```

### Trigger 2: Budget Revelation
**Example:** User initially said "500K RUB" for CRM, but during scoring reveals they secured 3M RUB budget and plan to hire a dedicated CRM admin.

**System Response:** Track escalation offered (budget jump triggers Deep Track rules).

---

## Integration with Track Detection Algorithm

The Standard Track flow is invoked when:

1. **User chooses Standard** from track selection menu (Step 01)
2. **Algorithm recommends Standard** with HIGH confidence (≥75%)
3. **User escalates from Quick** mid-pipeline
4. **User de-escalates from Deep** (chooses lighter track)

**Routing:**
- **FROM Step 01:** Load Step 02 (Roles Discovery) with `track: standard` flag
- **FROM Step 04:** Consilium runs in standard mode (4-6 specialists, full Six Hats, no auto-TRIZ prompt)
- **FROM Step 05:** Full 9-criteria scoring
- **FROM Step 06:** Full portfolio integration
- **TO Step 09:** Skip Steps 07 and 08, go straight to Complete

**Memory Storage:**
After Standard Track completes, save to memory:
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:standard-track:{IDEA_ID}" \
  --content "{idea_title, track, duration, score, recommendation, consilium_summary}"
```

---

## Summary

The Standard Track is the **balanced workhorse** of Life OS:

| Aspect | Summary |
|--------|---------|
| **Purpose** | Structured evaluation without exhaustive planning |
| **Time** | 45-60 minutes |
| **Steps** | 7 (Collect, Roles, Specialists, Consilium, Scoring, Integration, Complete) |
| **Specialists** | 4-6 with full Six Hats |
| **Scoring** | Full 9 criteria + domain-specific |
| **Portfolio Check** | YES |
| **Deep Planning** | NO (deferred) |
| **Ideal For** | Freelance, small business, moderate software projects |
| **Output** | GO/EVALUATE/DEFER/NO-GO + actionable recommendations |

**When in doubt between Quick and Standard:** Choose Standard. The extra 30-40 minutes provides significantly more confidence and structure. The cost of a bad decision on a 6-month project far exceeds 40 minutes of planning.

**When in doubt between Standard and Deep:** If the idea involves >1M RUB budget, 4+ stakeholders, OR you need a detailed execution plan (L1-L6), upgrade to Deep. Otherwise, Standard is sufficient.
