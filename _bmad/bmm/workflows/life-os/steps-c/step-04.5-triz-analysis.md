---
name: 'step-04.5-triz-analysis'
description: 'TRIZ contradiction analysis: optional step called from Step 4, 5 or 8'
mode: create
type: optional
estimatedTime: '5-120 minutes (depends on mode)'
requires:
  - workflow-plan.md (must exist)
  - At least one identified contradiction
outputs:
  - contradiction-resolution.md
  - Updated workflow-plan.md with TRIZ solution
calledFrom:
  - step-04-consilium
  - step-05-scoring
  - step-08-deep-plan
templates:
  quick: '../templates/triz-quick.template.md'
  structured: '../templates/triz-structured.template.md'
  ariz: '../templates/ariz-full.template.md'
dataRef: '../data/triz-quick-patterns.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
---

# Step 4.5: TRIZ Contradiction Analysis (Optional)

## STEP GOAL:

Resolve contradictions blocking progress using TRIZ principles. Find a solution that eliminates the contradiction, not a compromise.

## MANDATORY EXECUTION RULES:

### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 READ the complete step file before taking action
- 🔄 YOU ARE A FACILITATOR, not a content generator
- ✅ ALWAYS speak in `{communication_language}` from config

### Step-Specific Rules:
- This step is called ONLY from other steps (4, 5, 8)
- ALWAYS return control to calling step after completion
- Document ALL results in workflow-plan.md
- Save to memory for reuse
- 🎯 Use subprocess for TRIZ template loading based on mode (Pattern 3)
- 💬 Return ONLY selected mode template, not all 3 templates

## WHEN TO USE:

| Situation | Source | Example |
|----------|----------|--------|
| Experts strongly disagree (>40% divergence) | Step 4 (Consilium) | "3 of 5 experts against chosen approach" |
| Criteria conflict during scoring | Step 5 (Scoring) | "High Impact + High Effort simultaneously" |
| Trade-off detected during planning | Step 8 (Deep Plan) | "Speed vs Quality, Budget vs Features" |
| User explicitly chose [T] TRIZ | Any step | Menu selection |

**Mandatory Prerequisites:**
- Contradiction identified (X conflicts with Y)
- Workflow plan exists with project context
- Data file available: `data/triz-quick-patterns.md`

---

## SECTION 1: Context Definition

**Ask the user:**

1. "Where are you coming from?"
   - [4] Step 4: Consilium (expert disagreement)
   - [5] Step 5: Scoring (criteria conflict)
   - [8] Step 8: Deep Plan (planning trade-off)

2. "What is the contradiction?"
   - Format: "We need X, but X causes problem Y"
   - Example: "We need fast delivery (6 weeks), but speed reduces quality"

**Record context in working notes before continuing.**

---

## SECTION 2: Mode Selection

📖 **Reference:** Complete decision tree and mode comparison in `data/triz-modes-execution.md`

| Mode | Time | Use For |
|------|------|---------|
| **Quick** | 5-10 min | Fast solutions, simple contradictions |
| **Structured** | 30-60 min | Important projects, complex contradictions |
| **Full ARIZ** | 2-4 hours | Strategic projects, fundamental contradictions |

**Ask:** "Which mode? [Q] Quick  [S] Structured  [F] Full ARIZ"

#### TRIZ Template Loading (Subprocess - Pattern 3)

**Launch a subprocess that:**
1. User selects mode: Quick / Structured / Full ARIZ
2. Loads ONLY the corresponding template:
   - **Quick:** `../templates/triz-quick.template.md` (~100 lines)
   - **Structured:** `../templates/triz-structured.template.md` (~300 lines)
   - **Full ARIZ:** `../templates/ariz-full.template.md` (~600 lines)
3. Also loads relevant section from `../data/triz-quick-patterns.md` (pattern library subset)
4. Returns ONLY selected template + relevant patterns (~100-600 lines instead of 1,500+ all templates)

**Subprocess returns:** Mode-specific template + matching TRIZ patterns

**Graceful fallback:** If subprocess unavailable, load only selected template in main context based on user choice

**Context Savings:** ~1,500 lines (3 full templates + full pattern library → 1 selected template + subset)

---

## SECTION 3: Execute Selected Mode

📖 **Detailed Protocols:** `data/triz-modes-execution.md`

**Execute chosen mode following the protocol:**
- **Quick:** Classify → Top-3 principles → Brainstorm → Select → Document
- **Structured:** Technical contradiction → Matrix → IFR → Apply → Evaluate → Document
- **Full ARIZ:** 9 parts (Problem Analysis → Solution Organization)

---

## SECTION 4: Integration & Documentation

📖 **Integration Protocols:** `data/triz-modes-execution.md`
📖 **Output Template:** `data/triz-modes-execution.md`
📖 **Memory Protocol:** `data/triz-modes-execution.md`

**Integration by calling step:**
- **Step 4:** Present solution → Measure consensus → Update workflow-plan.md
- **Step 5:** Recalculate MCDA → Update Stage Gate
- **Step 8:** Integrate into L2 structure → Update Quality Gate

**Documentation:** Add TRIZ section to workflow-plan.md with date, mode, contradiction, solution, principles, IFR%, plan, criteria, status

**Memory:** Auto-save to `shared-knowledge:life-os:methods:triz:{project}:{date}` for pattern reuse

---

## SECTION 7: Return to Main Workflow

**Show return menu:**

```
TRIZ analysis complete.

Solution: {summary}
Contradiction resolved: {Yes / Partially / No}

Next:
[R] Return to Step {X} (where you came from)
[4] Repeat Consilium with TRIZ solution
[5] Recalculate Scoring with new criteria
[8] Continue Deep Plan with TRIZ structure
```

**Process choice and route back to appropriate step.**

---

## SUCCESS METRICS

### Completion Criteria (all mandatory):
- Contradiction clearly defined
- At least 1 TRIZ principle applied
- Concrete solution documented (not just theory)
- Solution recorded in workflow-plan.md
- Memory saved for future use

### Quality Check:
- Does solution truly resolve contradiction? (not compromise!)
- Is solution feasible with available resources?
- Does IFR guide solution (approaching ideal)?

### Anti-patterns (avoid):
- **Bad:** "Make medium speed and medium quality" (compromise)
- **Good:** "Phase 1: fast MVP + Phase 2: quality refinement" (resolution via Principle 1: Segmentation)

---

## SYSTEM METRICS

### SUCCESS:
- Contradiction identified and classified
- Mode selected consciously (via decision tree)
- Solution documented and confirmed by user
- Results saved in workflow-plan.md and memory
- Return to calling step executed correctly

### FAILURE:
- Skipped contradiction identification
- Generated solutions without user participation
- Failed to return to calling step
- Missing result documentation

**Main Rule:** TRIZ resolves contradictions, not creates compromises. Focus on IFR (Ideal Final Result).

---

**End of Step 4.5**

Return to: [Step 4: Consilium](./step-04-consilium.md) | [Step 5: Scoring](./step-05-scoring.md) | [Step 8: Deep Plan](./step-08-deep-plan.md)
