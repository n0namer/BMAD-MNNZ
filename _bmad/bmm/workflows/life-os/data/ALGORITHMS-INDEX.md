# Life OS Algorithms Index

**Purpose:** Central registry of all core algorithms used in the Life OS workflow system.

**Last Updated:** 2026-02-06
**Status:** Complete (4/4 algorithms documented)

---

## Algorithm Directory

### 1. Track Detection Algorithm
**File:** `data/track-detection-algorithm.md`
**Purpose:** Auto-detect idea complexity and recommend processing track (Quick/Standard/Deep)
**Size:** 23 KB | 582 lines

**Quick Facts:**
- Uses 6 input signals (domain, complexity_signal, resource_level, budget_range, stakeholder_count, novelty)
- Applies weighted scoring matrix (0-20 points total)
- Decision thresholds: Quick (0-5), Standard (5.1-12), Deep (12.1-20)
- Includes deterministic decision tree with 6 override rules
- Confidence calculation accounts for signal clarity and boundary proximity

**When Used:**
- Step 01: Collect Ideas (immediately after idea is captured)
- Transition point: Determines routing to Step 02 (Standard), Step 04 (Quick), or Step 00 (Deep)

**Key Outputs:**
- Recommended track (Quick, Standard, or Deep)
- Confidence level (50-99%)
- Scoring breakdown showing contribution of each signal
- Track escalation opportunities identified mid-pipeline

**Integration:**
- Called from Step 01 transition logic
- Feeds into `track-escalation-rules.md` for mid-pipeline upgrades
- Uses `specialist-auto-selection-algorithm.md` for Quick Track consilium lite

---

### 2. Track Escalation Rules
**File:** `data/track-escalation-rules.md`
**Purpose:** Define when and how to escalate ideas from Quick/Standard track to deeper track during pipeline execution
**Size:** 16 KB | 474 lines

**Quick Facts:**
- 6 escalation triggers (Consilium Divergence, Scoring Contradiction, User Request, Stakeholder Discovery, Budget Revelation, Contradiction Detection)
- Complexity scoring recalculated at Step 04 and Step 05
- Each trigger includes detection logic, user presentation template, and action plan
- Escalation always optional; user can decline with rationale recorded

**When Used:**
- Step 04: Post-Consilium (triggers 1, 4)
- Step 05: Post-Scoring (triggers 2, 3, 5, 6)
- Step 06: Integration check (trigger 5 budget re-check)
- Anytime: User explicit request (trigger 3)

**Key Outputs:**
- Escalation trigger detection (which rule fired)
- Escalation offer to user (with time impact and added steps)
- User override option (accept, decline, or request)
- Workflow metadata update if escalated

**Integration:**
- Implements the Track Escalation section of workflow.md
- References `track-detection-algorithm.md` for initial routing
- Uses specialist selection from `specialist-auto-selection-algorithm.md` for escalated tracks

---

### 3. Role Matching Algorithm
**File:** `data/role-matching-algorithm.md`
**Purpose:** Intelligently suggest specialist roles based on idea keywords, domain detection, and contextual factors
**Size:** 13 KB | 479 lines

**Quick Facts:**
- Extracts keywords from idea title + description
- Detects primary domain(s) from 9 categories (business, tech, design, finance, health, personal, legal, creative, community)
- Matches keywords to roles using scoring formula with priority bonuses
- Applies contextual refinement based on budget, timeline, complexity, and project stage
- Deduplicates and merges overlapping role suggestions

**When Used:**
- Step 02: Roles Discovery (after user-defined roles collected, auto-suggest complementary roles)
- Step 03: Specialist Match (confirmed roles guide specialist selection)

**Key Outputs:**
- Ranked list of suggested roles (2-8 depending on complexity)
- Rationale for each suggestion (keywords matched, relevance score, contribution)
- Optional roles for later consideration
- Interactive refinement interface for user modifications

**Integration:**
- Runs after Step 02 user input (sphere detection → domain mapping)
- Feeds into Step 03 specialist matching
- Uses role database in `data/roles-descriptions.md` and `data/roles-templates.md`

---

### 4. SaaS Autonomy Rubric
**File:** `data/saas-autonomy-rubric.md`
**Purpose:** Detailed scoring anchors for evaluating SaaS autonomous operation capability (6th MCDA criterion for SaaS/software projects)
**Size:** 21 KB | 200+ lines

**Quick Facts:**
- 4 pillars of autonomy (Self-Signup, Self-Billing, Self-Service Support, Autonomous Operation)
- Each pillar scored 1-5 scale with detailed behavioral anchors
- Weighted formula: (Self_Signup×0.25) + (Self_Billing×0.30) + (Self_Service_Support×0.30) + (Autonomous_Operation×0.15)
- Includes team implications and real-world examples (Salesforce, Notion, Vercel, etc.)
- Critical for solo founders and small teams evaluating operational overhead

**When Used:**
- Step 05: Scoring (ONLY when `domain = 'saas'` or `domain = 'software'`)
- Applied as 6th scoring criterion (after Impact, Effort, Alignment, Risk, Feasibility)

**Key Outputs:**
- Autonomy score (1-5 scale, consistent with other MCDA criteria)
- Clear understanding of what operational overhead the product requires
- Strategic guidance on product-led growth vs. high-touch sales model

**Integration:**
- Integrates into Step 05 scoring rubric for SaaS domain
- Referenced in `scoring-examples.md` for SaaS examples
- Used in Deep Track (Step 08) financial planning for operational cost modeling

---

## Algorithm Usage Matrix

### By Step

| Step | Algorithm(s) Used | Trigger Point |
|------|-------------------|---------------|
| **Step 00** | - | (no algorithms) |
| **Step 01** | Track Detection | After idea collection, before routing |
| **Step 02** | Role Matching | After user-defined roles, before confirmation |
| **Step 03** | Role Matching (input), Specialist Auto-Selection | Role confirmation → specialist selection |
| **Step 04** | Track Escalation (Triggers 1, 4) | Post-consilium, divergence check |
| **Step 05** | Track Escalation (Triggers 2, 3, 5, 6) | Post-scoring, contradiction detection + SaaS Autonomy |
| **Step 06** | Track Escalation (Trigger 5 re-check) | Budget validation |
| **Step 07** | - | (no algorithms) |
| **Step 08** | SaaS Autonomy (for cost modeling) | Deep Plan financial section |
| **Step 09** | - | (no algorithms) |

---

## References & Related Files

### Supporting Data Files
- `data/specialist-roles.yaml` — Database of 50+ specialist types with keywords
- `data/roles-descriptions.md` — Full role descriptions and qualifications
- `data/specialist-auto-selection-algorithm.md` — How specialists are ranked given confirmed roles

### Workflow References
- `workflow.md` — Main workflow with algorithm references in frontmatter
- `steps-c/step-01-collect-ideas.md` — Implements Track Detection Algorithm
- `steps-c/step-02-roles-discovery.md` — Implements Role Matching Algorithm
- `steps-c/step-04-consilium.md` — Checks Escalation Triggers 1, 4
- `steps-c/step-05-scoring.md` — Checks Escalation Triggers 2, 3, 5, 6; applies SaaS Autonomy

---

**Last Maintained:** 2026-02-06
**Status:** Complete - All 4 algorithms documented
