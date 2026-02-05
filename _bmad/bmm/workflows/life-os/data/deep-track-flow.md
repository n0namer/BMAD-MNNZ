---
name: 'deep-track-flow'
track: 'Deep'
target_duration: '2-4 hours (up to 6h with TRIZ)'
purpose: 'Comprehensive evaluation for complex projects, high stakes, strategic decisions'
version: '1.0'
consumedBy:
  - step-01-collect-ideas.md (routing decision)
  - step-00-goals-discovery.md (pre-requisite)
  - step-04-consilium.md (deep mode flag)
  - step-04.5-triz-analysis.md (prompted if contradictions detected)
  - step-08-deep-plan.md (full L1-L6 mode)
---

# Deep Track Flow

## Purpose

The **Deep Track** is the comprehensive, no-shortcuts analysis path for complex, high-stakes projects requiring:

- **Full strategic planning** (goals alignment, resource allocation, milestone planning)
- **Deep specialist analysis** (consilium deep mode with Six Hats)
- **Optional TRIZ** for creative problem-solving
- **L1-L6 deep plan** with scenario mapping and auto-intelligence
- **Calendar integration** and timeline planning
- **Complete documentation** (200+ line comprehensive output)

**Target projects:** Enterprise SaaS, AI/ML platforms, funded startups, franchise expansion, major career shifts, high-budget initiatives, breakthrough innovations.

---

## Pipeline Steps (Full Flow)

### Step 00: Goals Discovery [REQUIRED]
**Duration:** 10-15 minutes
**Purpose:** Establish high-level strategic context before diving into this specific idea.

**Activities:**
- Discover user's top-level goals (career, financial, lifestyle, impact)
- Define current priorities and constraints
- Identify goal hierarchies (L0 → L1 goals)
- Save to goals.yaml for cross-project alignment

**Output:**
- `goals.yaml` with structured goal hierarchy
- Priority scores and relationships

**Why Deep Track needs this:**
Complex projects must align with strategic goals. Without this context, Deep Plan (Step 08) cannot map idea → goals → resources properly.

**Skip condition:** If goals were discovered in a prior session (check for `goals.yaml`).

---

### Step 01: Collect Ideas [REQUIRED]
**Duration:** 5 minutes
**Purpose:** Capture the idea with full context and trigger track detection.

**Activities:**
- Same as Standard/Quick tracks (no modification)
- Collect idea title, description, domain, resources, timeline
- Save to memory and workflow plan

**Output:**
- Idea record with all metadata
- Track detection signals extracted

**Transition:**
- After save, track detection algorithm runs
- User is presented with recommendation: "Deep Track (2-4 hours)"
- User confirms (or overrides)

---

### Track Detection Checkpoint
**Duration:** 1 minute

**User sees:**
```
---------------------------------------------------
TRACK RECOMMENDATION

Based on your idea "{title}":

  Recommended track: DEEP
  Confidence: {percentage}% (HIGH)
  Estimated time: 2-4 hours (up to 6h with TRIZ)

  Key factors:
  - Domain: {enterprise/saas/ai-ml} (contributes to Deep)
  - Resources: {funded-team} (contributes to Deep)
  - Stakeholder count: {4+} (contributes to Deep)

  Steps included: All 9 steps (0→1→2→3→4→4.5→5→6→7→8→9)

  [Q] Quick Track (15-20 min)
  [S] Standard Track (45-60 min)
  [D] Deep Track (2-4 hours) ← RECOMMENDED
  [R] Accept recommendation (Deep)

  Your choice: [Q/S/D/R]
---------------------------------------------------
```

**If user chooses Deep (or presses R):**
Proceed to Step 02.

---

### Step 02: Roles Discovery [REQUIRED]
**Duration:** 5 minutes
**Purpose:** Identify all the perspectives needed to evaluate this complex idea.

**Activities:**
- Analyze idea domain, stakeholders, novelty
- Generate 5-8 required roles (e.g., "Tech Architect", "Finance Analyst", "Risk Advisor")
- No modification from Standard Track (Deep gets full role discovery)

**Output:**
- List of 5-8 roles with brief rationale for each

---

### Step 03: Specialist Matching [REQUIRED]
**Duration:** 5 minutes
**Purpose:** Assign AI specialists to the roles discovered in Step 02.

**Activities:**
- Same as Standard Track (full specialist matching)
- Each role → specialist with expertise bio
- User confirms or swaps specialists

**Output:**
- Consilium roster: 5-8 specialists with names, expertise, and assigned roles

---

### Step 04: Consilium Deep Mode [REQUIRED]
**Duration:** 25-30 minutes
**Purpose:** Full structured specialist discussion with Six Thinking Hats.

**Deep Mode Characteristics:**
- **Six Thinking Hats FORCED:** Each specialist cycles through multiple perspectives (White facts → Red intuition → Black risks → Yellow benefits → Green creativity → Blue meta)
- **Multi-round synthesis:** Not just one-shot recommendations; specialists respond to each other
- **Advanced elicitation available:** Party Mode, Advanced Elicitation Menu offered proactively
- **Contradiction detection:** If specialists disagree significantly (>50% variance in recommendations), TRIZ is offered
- **Auto-Suggest Engine triggered:** For all specialists (not optional in Deep)

**Output:**
- 6-8 sections (one per hat color)
- Per-specialist detailed recommendations
- Consensus section (2-4 paragraphs)
- Contradiction report (if applicable)
- TRIZ recommendation (if contradictions detected)

**Menu options shown:**
```
[C] Continue to Scoring
[T] Run TRIZ Analysis (recommended if contradictions detected)
[A] Advanced Elicitation (ask deeper clarifying questions)
[P] Party Mode (free-form brainstorm)
[R] Re-run consilium with different specialists
```

**Transition:**
If user chooses [T] → Step 04.5 (TRIZ)
Otherwise → Step 05

---

### Step 04.5: TRIZ Analysis [OPTIONAL, PROMPTED]
**Duration:** 10-60 minutes (depends on depth of contradictions)
**Purpose:** Resolve contradictions using 40 Inventive Principles.

**When prompted:**
- Consilium revealed 2+ contradictions (e.g., "need fast time-to-market BUT need high quality")
- Scoring shows opposing high scores (e.g., Impact=5, Risk=5)
- User explicitly requests "creative problem-solving"

**Activities:**
- Identify contradictions from consilium output
- Map contradictions to TRIZ principles
- Generate 3-5 inventive solutions per contradiction
- Synthesize recommendations

**Output:**
- Contradiction matrix (what conflicts with what)
- 3-5 TRIZ-derived solutions
- Revised consilium consensus (if TRIZ changes the direction)

**Skip condition:**
If no contradictions detected OR user chooses [C] Continue (skips TRIZ).

---

### Step 05: Scoring [REQUIRED]
**Duration:** 10-15 minutes
**Purpose:** Quantify the idea across all evaluation dimensions.

**Deep Track Scoring:**
- **Full criteria:** All 10+ criteria (Impact, Effort, Risk, Alignment, Novelty, Market Fit, Strategic Value, etc.)
- **Domain-specific criteria auto-added:** For enterprise, adds "Compliance Risk"; for AI/ML, adds "Data Availability"
- **Weighted scoring:** Criteria are weighted based on goals.yaml priorities
- **Scenario-aware:** If TRIZ was run, scores account for post-TRIZ adjustments

**Output:**
- Detailed scoring matrix (1-5 scale for each criterion)
- Total weighted score
- Radar chart data (for visualization)
- Recommendation: GO / REVISIT / NO-GO with rationale

---

### Step 06: Portfolio Integration [REQUIRED]
**Duration:** 15 minutes
**Purpose:** Evaluate how this idea fits into the user's current portfolio of active projects.

**Deep Track Integration:**
- **Full WIP check:** Review all active projects, calculate WIP load
- **Resource conflict analysis:** Check if this idea conflicts with existing commitments
- **Goal alignment check:** Compare idea's goals to portfolio goals
- **Synergy detection:** Identify if this idea can share resources or learnings with other projects
- **Health metrics:** Portfolio balance (personal vs. professional, short-term vs. long-term)

**Output:**
- WIP count and recommendation (should be ≤3 active projects)
- Resource conflict warnings
- Synergy opportunities (if any)
- Portfolio health assessment

---

### Step 07: Calendar Sync [REQUIRED]
**Duration:** 10 minutes
**Purpose:** Plan specific milestones and calendar events for this project.

**Deep Track Calendar:**
- **Milestone extraction:** From Deep Plan (Step 08) or manual if Deep Plan not run yet
- **Calendar event generation:** One event per milestone with title, date, description
- **Dependency mapping:** If Milestone B depends on Milestone A, calendar reflects order
- **Time allocation check:** Does the user have bandwidth in their calendar for these events?

**Output:**
- 3-10 calendar events (`.ics` format)
- Milestone timeline visualization (text-based Gantt)
- Bandwidth check result

---

### Step 08: Deep Plan (L1-L6) [REQUIRED]
**Duration:** 20-60 minutes
**Purpose:** Create a comprehensive execution plan with 6 levels of detail.

**Deep Plan Structure:**

**L1 (Strategic Objective):**
- One-sentence goal (what success looks like)

**L2 (Themes/Phases):**
- 3-5 high-level themes (e.g., "MVP Development", "Market Validation", "Scale to 100 customers")

**L3 (Epics):**
- 5-10 major initiatives (e.g., "Build authentication system", "Run beta program")

**L4 (Features/Milestones):**
- 10-30 concrete deliverables (e.g., "Login page", "Password reset flow", "20 beta users onboarded")

**L5 (Tasks):**
- 30-100 actionable tasks (e.g., "Design login UI mockup", "Implement OAuth provider", "Send beta invite emails")

**L6 (Sub-tasks/Specs):**
- 100-300 detailed steps (optional, for critical paths)

**Auto-Intelligence Integration:**
- **Auto-Suggest Engine:** Suggests tasks based on similar past projects
- **Scenario mapping:** "What if budget is cut by 50%?" (alternative L4-L5 plans)
- **Dependency graph:** Tasks that block other tasks
- **Resource allocation:** Which tasks need external help vs. solo work

**Output:**
- Full L1-L6 plan (200+ lines)
- Dependency matrix
- 2-3 scenario plans (optimistic, realistic, pessimistic)
- Estimated effort per phase
- Risk hotspots flagged

**Deep Plan Auto-Intelligence Features (from `deep-plan-auto-intelligence.md`):**
- Memory-based pattern matching: "Similar projects took X months for Y phase"
- Complexity heuristics: Auto-detects if a task is underestimated
- Resource auto-allocation: Suggests when to hire/outsource
- Calendar integration: L4 milestones → calendar events automatically

---

### Step 08.5: Final Polish [REQUIRED]
**Duration:** 10 minutes
**Purpose:** Review, refine, and finalize all outputs before completion.

**Activities:**
- Review entire workflow plan for gaps or inconsistencies
- Ensure all templates are filled (goals.yaml, workflow plan, deep plan)
- Generate final summary (executive summary of the entire Deep Track analysis)
- Check cross-references (e.g., do calendar events match Deep Plan milestones?)

**Output:**
- Final summary (2-3 paragraphs)
- Quality checklist (all required outputs present?)
- Next steps recommendation (start execution, defer, revisit)

---

### Step 09: Complete [REQUIRED]
**Duration:** 1 minute
**Purpose:** Mark the workflow complete and save all artifacts.

**Activities:**
- Same as Standard/Quick tracks
- Save final state to memory
- Mark workflow as COMPLETED
- Display completion message with artifact links

**Output:**
- Completion timestamp
- Link to workflow plan
- Link to deep plan
- Link to calendar events

---

## When to Use Deep Track

### Automatic Recommendation Criteria

The track detection algorithm recommends Deep Track when:

1. **Domain is complex:**
   - Enterprise SaaS, AI/ML, franchise, large-scale software

2. **Resources are significant:**
   - Funded team (seed/pre-seed/Series A)
   - Budget >1M RUB or investment round
   - Team of 4+ people

3. **Stakeholders are many:**
   - 4+ people directly affected (team, investors, customers, partners)

4. **Novelty is high:**
   - New-in-domain (e.g., "first AI sales QA platform in Russian market")
   - Breakthrough (e.g., "paradigm shift in how X is done")

5. **User explicitly requests:**
   - "I need a full plan"
   - "Deep dive"
   - "Strategic decision"
   - "Comprehensive analysis"

### Confidence Levels

| Confidence | Scenario | Action |
|------------|----------|--------|
| 90-99% (HIGH) | Multiple criteria match Deep (e.g., enterprise + funded + 4+ stakeholders) | Auto-recommend, user can override to Standard/Quick if desired |
| 75-89% (MEDIUM) | Some criteria match Deep, some don't | Recommend Deep but show Standard as viable alternative |
| 50-74% (LOW) | Ambiguous signals | Present all three tracks equally, ask user to choose |

### Override Scenarios

**User chooses Deep even though Quick/Standard recommended:**
- ✅ **Always allowed.** More analysis is never harmful.
- No warning shown.

**User chooses Standard/Quick even though Deep recommended:**
- ⚠️ **Warning shown:** "Note: This idea has high complexity/stakes. Quick/Standard tracks skip Deep Plan, calendar sync, and optional TRIZ. Proceed anyway?"
- If user confirms, proceed with chosen track.

---

## Output Template

### Comprehensive Output Includes

**1. Goals Alignment Report** (from Step 00)
- Top 3 user goals
- How this idea maps to each goal
- Goal priority scores

**2. Idea Record** (from Step 01)
- Title, description, domain
- Resources, timeline, budget
- Track selection rationale

**3. Roles & Specialists** (from Steps 02-03)
- 5-8 roles identified
- Specialist roster with expertise

**4. Consilium Deep Report** (from Step 04)
- Six Thinking Hats analysis (6 sections)
- Per-specialist detailed recommendations (5-8 specialists × 200-400 words each)
- Consensus synthesis (2-4 paragraphs)
- Contradiction report (if applicable)

**5. TRIZ Analysis** (from Step 04.5, if run)
- Contradictions identified
- TRIZ principles applied
- 3-5 inventive solutions

**6. Scoring Matrix** (from Step 05)
- Full criteria breakdown (10+ criteria)
- Weighted total score
- GO/REVISIT/NO-GO recommendation

**7. Portfolio Integration** (from Step 06)
- WIP analysis
- Resource conflicts
- Synergy opportunities
- Portfolio health metrics

**8. Calendar & Milestones** (from Step 07)
- 3-10 calendar events (`.ics` files)
- Milestone timeline
- Bandwidth check

**9. Deep Plan L1-L6** (from Step 08)
- 200+ lines of structured plan
- Dependency matrix
- 2-3 scenario plans
- Risk hotspots

**10. Final Summary** (from Step 08.5)
- Executive summary (2-3 paragraphs)
- Next steps
- Quality checklist

**Total output size:** 200-500 lines (depending on TRIZ and Deep Plan depth)

---

## Examples of Deep Track Projects

### Example 1: Enterprise SaaS Platform (AI-Powered Sales QA)

**Idea:**
"Building an AI-powered sales quality assurance platform for enterprise clients. We have a team of 5, $200K pre-seed funding, and need to plan full architecture and go-to-market strategy."

**Why Deep Track:**
- ✅ Domain: enterprise + saas (4.0 pts)
- ✅ Complexity signal: "full architecture and go-to-market" = deep-analysis (6.0 pts)
- ✅ Resource level: funded-team (3.0 pts)
- ✅ Budget: investment-round (3.0 pts)
- ✅ Stakeholders: 4+ (team + investors + enterprise customers) (2.0 pts)
- ✅ Novelty: new-in-domain (2.0 pts)
- **Total: 20.0 / 20.0 (maximum)**

**Confidence:** 99% (HIGH)

**Deep Track value:**
- **Step 00 (Goals):** Align with founder's long-term vision (e.g., "exit in 5 years", "build category leader")
- **Step 04 (Consilium Deep):** Tech Architect + Product Strategist + Risk Advisor + Finance Analyst + Growth Lead + Legal Advisor (6 specialists) discuss architecture, compliance, pricing, GTM
- **Step 04.5 (TRIZ):** Likely triggered due to contradiction: "need enterprise-grade security (slow to build) BUT need fast MVP for fundraising"
- **Step 08 (Deep Plan):** L1-L6 plan covering MVP → beta → 10 customers → Series A → scale. 300+ tasks.
- **Step 07 (Calendar):** 10 milestones over 18 months (MVP launch, beta completion, first 10 customers, Series A pitch, etc.)

**Time:** 4-6 hours (including TRIZ)

---

### Example 2: AI/ML Research Project (Breakthrough Innovation)

**Idea:**
"Developing a new neural architecture for real-time multimodal reasoning. Academic research project with potential startup spin-off. Team of 3 researchers, grant funding $100K."

**Why Deep Track:**
- ✅ Domain: ai-ml (4.0 pts)
- ✅ Complexity signal: "new neural architecture" = deep-analysis (inferred) (6.0 pts)
- ✅ Resource level: small-team (3.0 pts)
- ✅ Budget: medium (grant $100K) (1.5 pts)
- ✅ Stakeholders: 2-3 (researchers + grant agency) (1.0 pt)
- ✅ Novelty: breakthrough (2.0 pts)
- **Total: 17.5 / 20.0**

**Confidence:** 92% (HIGH)

**Deep Track value:**
- **Step 00 (Goals):** Align with academic career goals (publications, citations, tenure) AND startup goals (commercialization, exit)
- **Step 04 (Consilium Deep):** AI Specialist + Research Methodologist + IP Lawyer + Commercialization Advisor + Data Scientist (5 specialists) discuss feasibility, publication strategy, patent potential, compute requirements
- **Step 04.5 (TRIZ):** Contradiction detected: "need novel architecture (high risk of failure) BUT need publishable results within 12 months (grant deadline)"
  - TRIZ solution: "Principle 15 (Dynamism): Start with simpler variant, publish incremental results, iterate toward breakthrough"
- **Step 08 (Deep Plan):** L1-L6 covering literature review → prototype → experiment design → paper writing → conference submission → patent filing → startup formation
- **Step 07 (Calendar):** 8 milestones (prototype ready, experiment 1 done, paper draft, submission, patent filed, etc.)

**Time:** 3-4 hours

---

### Example 3: Major Career Pivot (High Personal Stakes)

**Idea:**
"Quitting my corporate job to start a freelance design studio. Family depends on my income. Need to plan transition carefully over 6-12 months."

**Why Deep Track:**
- ❓ Domain: freelance (2.0 pts) — not inherently Deep
- ✅ Complexity signal: "need to plan transition carefully" = deep-analysis (inferred) (6.0 pts)
- ✅ Resource level: solo-focused (1.5 pts) — transitioning to full-time
- ❓ Budget: low (no external funding) (0.0 pts)
- ✅ Stakeholders: 2-3 (freelancer + family) (1.0 pt)
- ❓ Novelty: proven-model (freelance studios exist) (0.0 pts)
- **Total: 10.5 / 20.0**

**Confidence:** 68% (MEDIUM-LOW, boundary case)

**Algorithm recommends Standard, but user might choose Deep due to high personal stakes.**

**If user chooses Deep:**

**Deep Track value:**
- **Step 00 (Goals):** Critical alignment check: Does freelance studio align with long-term career goals? Financial goals? Lifestyle goals?
- **Step 04 (Consilium Deep):** Career Coach + Finance Advisor + Risk Advisor + Business Strategist + Family Therapist (5 specialists) discuss financial runway, client acquisition, risk mitigation, family impact
- **Step 04.5 (TRIZ):** Contradiction: "need stable income for family (keep job) BUT need time to build freelance client base (quit job)"
  - TRIZ solution: "Principle 10 (Preliminary Action): Build client base WHILE still employed, then transition when revenue reaches 50% of salary"
- **Step 08 (Deep Plan):** L1-L6 covering parallel client acquisition (months 1-6 while employed) → part-time transition (months 7-9) → full freelance (month 10+)
- **Step 07 (Calendar):** 6 milestones (first client signed, 3 clients, revenue = 50% salary, resign, full freelance, etc.)

**Time:** 2-3 hours

**This is a great example of when Deep Track is valuable even though the idea is not "enterprise SaaS" or "funded startup" — the personal stakes are high.**

---

### Example 4: Franchise Expansion (Multi-Location Business)

**Idea:**
"Expanding my successful cafe from 1 location to 5 locations across the city over 2 years. Franchise model. Budget 10M RUB."

**Why Deep Track:**
- ✅ Domain: franchise (4.0 pts)
- ✅ Complexity signal: "franchise model" + "2 years" + "5 locations" = deep-analysis (6.0 pts)
- ✅ Resource level: funded-team (will need to hire) (3.0 pts)
- ✅ Budget: high (10M RUB) (3.0 pts)
- ✅ Stakeholders: 4+ (owner + employees + investors + franchise partners) (2.0 pts)
- ✅ Novelty: adaptation (franchise model is proven, but applying to this cafe is new) (1.0 pt)
- **Total: 19.0 / 20.0**

**Confidence:** 97% (HIGH)

**Deep Track value:**
- **Step 00 (Goals):** Align with business goals (revenue target? exit plan? lifestyle? build a brand?)
- **Step 04 (Consilium Deep):** Business Advisor + Real Estate Expert + Finance Analyst + Legal Advisor + Operations Manager + Brand Strategist (6 specialists) discuss location selection, franchise contracts, financing, supply chain, brand consistency
- **Step 04.5 (TRIZ):** Contradiction: "need consistent brand across all locations (tight control) BUT need local franchisees to have autonomy (flexibility)"
  - TRIZ solution: "Principle 3 (Local Quality): Standardize core (menu, branding, SOPs) but allow local customization (decor, events, partnerships)"
- **Step 08 (Deep Plan):** L1-L6 covering franchise contract design → location scouting → pilot location 2 → optimize → locations 3-5 → ongoing operations
- **Step 07 (Calendar):** 10 milestones over 24 months (contract finalized, location 2 opened, break-even, location 3 opened, etc.)

**Time:** 3-5 hours

---

## Integration with Track Detection Algorithm

### Routing Logic

**From Step 01 (after idea saved):**

```
IF track_detection_score >= 12.1 AND confidence >= 75%:
  RECOMMEND: Deep Track
  PRESENT: Track selection menu (with Deep highlighted)

  IF user chooses Deep:
    IF goals.yaml exists:
      ROUTE: Step 02 (Roles Discovery)
    ELSE:
      ROUTE: Step 00 (Goals Discovery) → Step 02

  ELSE IF user chooses Standard:
    SHOW WARNING: "This idea has high complexity. Deep Track includes Goals Alignment, Deep Plan, and Calendar Sync which are skipped in Standard."
    IF user confirms:
      ROUTE: Step 02 (Standard flow)

  ELSE IF user chooses Quick:
    SHOW WARNING: "This idea has high complexity/stakes. Quick Track skips specialist consilium, deep plan, and calendar sync."
    IF user confirms:
      ROUTE: Step 04 (Consilium Lite)
```

### Workflow Plan Metadata

When Deep Track is selected, append to workflow plan:

```markdown
## Track Selection (Auto-Detected)

**Recommended Track:** Deep
**Confidence:** {percentage}% (HIGH)
**Selected Track:** Deep
**Override:** No

**Scoring Breakdown:**
- domain: enterprise (4.0 pts)
- complexity_signal: deep-analysis (6.0 pts)
- resource_level: funded-team (3.0 pts)
- budget_range: investment-round (3.0 pts)
- stakeholder_count: 4+ (2.0 pts)
- novelty: new-in-domain (2.0 pts)
- **Total:** 20.0 / 20.0

**Steps Included:** 0 → 1 → 2 → 3 → 4 → 4.5 (if TRIZ) → 5 → 6 → 7 → 8 → 8.5 → 9

**Estimated Time:** 2-4 hours (up to 6h with TRIZ)
```

---

## Step Adjustments (Deep Track)

| Step | Modification from Standard |
|------|---------------------------|
| **Step 00** | **ADDED.** Goals Discovery runs if not already done. |
| **Step 01** | Unchanged. |
| **Step 02** | Unchanged (full role discovery). |
| **Step 03** | Unchanged (full specialist matching). |
| **Step 04** | **DEEP MODE FORCED.** Six Hats required. Auto-Suggest Engine triggered. Multi-round synthesis. TRIZ offered if contradictions detected. |
| **Step 04.5** | **PROMPTED if contradictions detected.** Full TRIZ analysis with 40 Inventive Principles. |
| **Step 05** | **FULL SCORING.** All criteria + domain-specific criteria + weighted scoring based on goals.yaml. |
| **Step 06** | **FULL INTEGRATION.** WIP check, resource conflicts, synergy detection, portfolio health. |
| **Step 07** | **ADDED.** Calendar sync with milestone extraction, event generation, bandwidth check. |
| **Step 08** | **ADDED.** Full L1-L6 deep plan with auto-intelligence, scenario mapping, dependency graph. |
| **Step 08.5** | **ADDED.** Final polish: review, refine, quality check. |
| **Step 09** | Unchanged (completion). |

---

## Success Criteria

**Deep Track is successful if:**

1. ✅ **All required steps completed** (0, 1, 2, 3, 4, 5, 6, 7, 8, 8.5, 9)
2. ✅ **TRIZ run if contradictions detected** (Step 04.5 triggered when appropriate)
3. ✅ **Deep Plan has L1-L6 structure** (not just L1-L3)
4. ✅ **Calendar events generated** (3-10 events matching Deep Plan milestones)
5. ✅ **Comprehensive output produced** (200+ lines total across all steps)
6. ✅ **User understands the full picture** (goals alignment, risks, timeline, resource needs)
7. ✅ **Actionable next steps identified** (GO/REVISIT/NO-GO with rationale)

---

## Time Budget Breakdown

| Step | Min (minutes) | Max (minutes) | Notes |
|------|--------------|--------------|-------|
| Step 00 (Goals) | 10 | 15 | Skip if goals.yaml exists |
| Step 01 (Collect) | 5 | 5 | Same as other tracks |
| Track Detection | 1 | 1 | Algorithm + user choice |
| Step 02 (Roles) | 5 | 5 | Full role discovery |
| Step 03 (Specialists) | 5 | 5 | Full specialist matching |
| Step 04 (Consilium Deep) | 25 | 30 | Six Hats + multi-round |
| Step 04.5 (TRIZ) | 0 | 60 | Optional, depends on contradictions |
| Step 05 (Scoring) | 10 | 15 | Full criteria + weighted |
| Step 06 (Integration) | 15 | 15 | WIP + synergy + health |
| Step 07 (Calendar) | 10 | 10 | Milestone → events |
| Step 08 (Deep Plan) | 20 | 60 | L1-L6 + scenarios |
| Step 08.5 (Polish) | 10 | 10 | Final review |
| Step 09 (Complete) | 1 | 1 | Save and mark done |
| **TOTAL (no TRIZ)** | **117 min** | **172 min** | **2.0-2.9 hours** |
| **TOTAL (with TRIZ)** | **127 min** | **232 min** | **2.1-3.9 hours** |

**Realistic range:** 2-4 hours (most projects land around 2.5-3 hours; TRIZ adds 0.5-1 hour if needed).

---

## Notes

- **Deep Track is NOT overkill for high-stakes projects.** A $200K investment, a major career change, or a 5-location franchise expansion DESERVES 3-4 hours of strategic analysis.

- **Quick/Standard tracks are NOT inferior.** They are optimized for their use cases (quick validation, moderate analysis). Deep Track is ONLY for when the complexity and stakes justify the time investment.

- **TRIZ is optional even in Deep Track.** It is only prompted when contradictions are detected. If consilium is harmonious, TRIZ is skipped.

- **Deep Plan (Step 08) is the crown jewel.** This is what separates Deep Track from Standard. L1-L6 planning with auto-intelligence and scenario mapping is what enables strategic execution.

- **Calendar Sync (Step 07) is critical for accountability.** Without calendar events, the Deep Plan is just a document. With calendar events, the user has concrete deadlines.

- **Goals Discovery (Step 00) is non-negotiable for Deep Track.** Complex projects MUST align with strategic goals. This step ensures that.

---

## Future Enhancements

**Possible future additions to Deep Track:**

1. **Step 08.6 (Resource Allocation):** Auto-assign tasks to team members based on skills (if team roster is available)
2. **Step 08.7 (Budget Breakdown):** Financial planning per phase (especially for funded projects)
3. **Step 08.8 (Risk Mitigation Plans):** For each risk identified, a mitigation strategy
4. **Integration with external tools:** Export Deep Plan to Jira/Asana, Calendar events to Google Calendar/Outlook

---

**END OF DEEP TRACK FLOW DEFINITION**
