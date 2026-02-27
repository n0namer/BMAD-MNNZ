---
name: 'step-04-consilium'
description: 'Assemble specialist consilium and capture recommendations'
nextStepFile: './step-05-scoring.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 4: Consilium

## STEP GOAL

Assemble focused consilium (Lite or Deep), capture recommendations, record consensus summary.

💡 **References:**
- Quality examples: `../data/validation-examples.md`
- Six Hats methodology: `../data/six-hats-protocol.md`
- Specialist questions: `../data/consilium-questions.md`
- Output templates: `../data/consilium-output-templates.md`

**Quality Standards:** See templates for Lite (200-300 words) vs Deep (500-800 words)

## MODE SELECTION

| Mode | Use For | Time | Output |
|------|---------|------|--------|
| **Lite** | Simple ideas, quick decisions | 5-10 min | 2-3 line recommendation |
| **Deep** | Complex decisions, strategic planning | 15-30 min | Multi-perspective consensus |

**Auto-Selection:** Quick track → Lite, Deep track → Full Six Hats

## MANDATORY RULES

- 🛑 NEVER generate content without user input - YOU ARE A FACILITATOR
- 📖 Read complete step file before action
- 🔄 When loading next step with 'C', read entire file
- ✅ Speak output in `{communication_language}`
- 🎯 Focus ONLY on consilium assembly and recommendations
- 🚫 FORBIDDEN to score or prioritize in this step
- 💬 Confirm each specialist's input
- 🎯 Use subprocess for consilium reference files (Pattern 3)
- 💬 Return ONLY mode-relevant sections, not full 6 reference files

**Protocols:**
- Search Orchestrator: `data/mcp_search_system_prompt_xml.md`
- 💾 Append consilium to {workflowPlanFile}
- 📘 Record decisions in project decisions file (if exists)

## MANDATORY SEQUENCE

### 1. Load Specialist List
Open {workflowPlanFile}, locate "Specialist Matching" section, summarize to user.

### 2. Determine Mode (Automatic)

**Quick Track** (simple/fast/straightforward) → **Lite Mode** (3 perspectives, 1-2 specialists, 5-10 min)
**Deep Track** (complex/strategic/comprehensive) → **Six Hats** (6 perspectives, 4-8 specialists, 15-30 min)

**If ambiguous:** Search Orchestrator (CLI memory → Local MD → Web/MCP)
**Default:** High priority roles exist → Deep, otherwise → Lite

Announce mode + specialists, then proceed.

### 3. Gather Recommendations

#### **LITE MODE** (Quick Track - 5-10 min)

**3 Perspectives:**
- ⚪ **Facts** - What do we know? (2-3 key facts/data/constraints)
- ⚫ **Risks** - What could go wrong? (2-3 critical risks)
- 🟢 **Opportunities** - Upside + creative solutions? (2-3 opportunities/innovations)

**Execution:**
1. Select 1-2 specialists
2. Ask all 3 questions per specialist (see `../data/consilium-questions.md`)
3. Keep 2-3 bullets per perspective
4. Total: 5-10 min

Before finishing, search `shared-knowledge` for similar ideas and note the pattern in memory—IDEAL 1.4 (memory-first reasoning) expects those insights to inform scoring and escalation decisions.

#### Consilium Reference Files Loading (Subprocess - Pattern 3)

**Launch a subprocess that:**
1. Detects mode: Lite or Deep (from step 2 determination)
2. Loads ONLY relevant sections from 6 reference files:
   - **six-hats-protocol.md** - If Deep mode: methodology section (~100 lines), if Lite: skip
   - **consilium-questions.md** - Mode-specific section: Lite = 3 perspectives questions (~30 lines), Deep = 6 hats questions (~60 lines)
   - **consilium-output-templates.md** - Matching mode template: Lite template (~20 lines) OR Deep template (~40 lines)
   - **comparative-ranking-protocol.md** - If multiple options detected: ranking protocol (~50 lines), else: skip
   - **auto-suggest-engine.md** - Framework detection rules (always load, ~30 lines)
   - **six-hats-consilium-reference.md** - If Deep mode with Six Hats: hat assignments (~60 lines), else: skip
3. Returns ONLY mode-appropriate content (~200-300 lines total instead of 2,200+ full files)

**Subprocess returns:**
- Lite Mode: ~80-100 lines (questions + template + framework detection)
- Deep Mode: ~250-300 lines (six hats protocol + questions + template + assignments + framework detection)

**Graceful fallback:** If subprocess unavailable, load minimal sections from each file in main context based on detected mode

**Context Savings:** ~2,200 lines (6 full reference files) → ~80-300 lines (mode-filtered excerpts) = ~1,900-2,120 lines saved

💡 **Questions reference:** `../data/consilium-questions.md` (Lite Mode section)

---

#### **DEEP MODE** (Full Six Hats - 15-30 min)

**Six Hats:**
- ⚪ White (Facts) → Market Analyst, Data, Finance
- 🔴 Red (Intuition) → UX, Psychologist
- ⚫ Black (Risks) → Risk, Security, Legal
- 🟡 Yellow (Benefits) → Portfolio, Growth
- 🟢 Green (Creativity) → Innovation, Creative
- 🔵 Blue (Process) → Strategy, Operations

**Execution:**
1. Auto-assign hat to each specialist (4-8 total)
2. Ask hat-specific questions (see reference file)
3. Confirm user input per specialist
4. Record with hat color prefix

💡 **Full methodology:** `../data/six-hats-protocol.md`
💡 **Questions bank:** `../data/consilium-questions.md` (Six Hats section)

### 4. Synthesize Consensus

#### **LITE MODE:**
Synthesize 2-3 line recommendation: "Based on analysis, recommend [DECISION] because [RATIONALE]. Key: [TOP RISK/OPPORTUNITY]."

Confirm with user.

#### **DEEP MODE:**
Balance all 6 hats (⚪ facts, 🔴 intuition, ⚫ risks, 🟡 benefits, 🟢 creativity, 🔵 process).

Ask user to confirm 2-4 bullet consensus view.

💡 **Output templates:** `../data/consilium-output-templates.md`

### 5. Auto-Suggest Framework

After consilium, AI suggests frameworks (keyword >70%, divergence ≥40% → TRIZ, domain detection).

💡 **Reference:** `../data/auto-suggest-engine.md`

### 6. Append to Workflow Plan

Use templates from `../data/consilium-output-templates.md`:
- **Lite:** Facts/Risks/Opportunities + 2-3 line synthesis
- **Deep:** All 6 hats + balanced consensus view

Append to {workflowPlanFile}.

### 7. Quality Self-Validation

**Check against standards:**

**Lite:** ☐ 1-2 specialists ☐ 3 perspectives ☐ 2-3 bullets each ☐ 2-3 line recommendation ☐ 200-300 words
**Deep:** ☐ 4-8 specialists ☐ 6 hats ☐ 2-3 paragraphs/specialist ☐ Risks+mitigations ☐ GO/NO GO ☐ 500-800 words

**Options:**
[I] Improve (return to step 3)
[A] Accept as-is (show ⚠️ warning, proceed if Y)
[R] Show examples (`validation-examples.md`)
[C] Continue (standards met)

💡 **Quality reference:** `../data/validation-examples.md`

---

### 8. Track Escalation Check

**💡 Reference:** See `../data/track-escalation-rules.md` for complete algorithm

**After consensus synthesis, check for escalation triggers:**

```bash
# TRIGGER 1: Consilium Divergence (>50% disagreement)
TOTAL_SPECIALISTS=$(count_all_specialists)
CONSENSUS_RECOMMENDATIONS=$(count_matching_recommendations)
AGREEMENT=$(echo "$CONSENSUS_RECOMMENDATIONS / $TOTAL_SPECIALISTS * 100" | bc)

if [ "$AGREEMENT" -lt 50 ] && [ "$CURRENT_TRACK" = "Quick" ]; then
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "⚠️ TRACK ESCALATION NOTICE"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "During consilium, I detected significant disagreement"
    echo "among specialists (agreement: $AGREEMENT%)."
    echo ""
    echo "  Trigger: Consilium Divergence"
    echo "  Current track: Quick Track"
    echo "  Suggested upgrade: Standard Track"
    echo ""
    echo "  What changes:"
    echo "  + Full Six Hats analysis (all perspectives)"
    echo "  + Extended scoring (9 criteria vs 3)"
    echo "  + Portfolio integration check"
    echo "  + Additional 40-60 minutes"
    echo ""
    echo "  [U] Upgrade to Standard Track"
    echo "  [K] Keep Quick Track (I understand the limits)"
    echo ""
fi

# TRIGGER 4: Stakeholder Discovery (Quick Track only)
INITIAL_STAKEHOLDERS=$(get_initial_stakeholder_count)
CONSILIUM_STAKEHOLDERS=$(count_stakeholders_from_consilium)

if [ "$CONSILIUM_STAKEHOLDERS" -gt "$((INITIAL_STAKEHOLDERS * 2))" ] && [ "$CURRENT_TRACK" = "Quick" ]; then
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "⚠️ TRACK ESCALATION NOTICE"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "During consilium, new stakeholder groups were identified."
    echo "Initial: $INITIAL_STAKEHOLDERS → Current: $CONSILIUM_STAKEHOLDERS stakeholders"
    echo ""
    echo "  Trigger: Stakeholder Discovery"
    echo "  Current track: Quick Track"
    echo "  Suggested upgrade: Standard Track"
    echo ""
    echo "  What changes:"
    echo "  + Multi-stakeholder coordination analysis"
    echo "  + Full Six Hats (all perspectives captured)"
    echo "  + Additional 40-60 minutes"
    echo ""
    echo "  [U] Upgrade to Standard Track"
    echo "  [K] Keep Quick Track (I understand the limits)"
    echo ""
fi

# TRIZ Auto-Trigger (if consensus still low after potential upgrade)
if [ "$AGREEMENT" -lt 60 ]; then
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "🚨 TRIZ RECOMMENDED: Consilium Divergence Detected"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "Agreement rate: $AGREEMENT% (<60% threshold)"
    echo "Experts show significant disagreement on approach."
    echo ""
    echo "TRIZ can help find a non-compromise solution that"
    echo "satisfies all perspectives without trade-offs."
    echo ""
    echo "[T] Trigger TRIZ analysis (5-120 min)"
    echo "[S] Skip TRIZ - Accept compromise"
    echo "[L] Learn more about TRIZ"
    echo ""
    echo "Your choice: [T/S/L]"
fi
```

**If user selects [T]:** Load and execute `./step-04.5-triz-analysis.md`, then return to menu below

**If user selects [L]:**
```
TRIZ (Theory of Inventive Problem Solving) resolves contradictions
rather than compromising. When specialists disagree, it's usually
because there's a hidden contradiction (X improves but Y worsens).

TRIZ provides 40 principles to eliminate the contradiction entirely.

Example:
- Problem: Need fast delivery (6 weeks) BUT speed reduces quality
- TRIZ: Principle 1 (Segmentation) → Phase 1: fast MVP, Phase 2: quality refinement
- Result: Both speed AND quality achieved

Would you like to run TRIZ analysis? [Y/N]
```

**If agreement ≥60%:** Skip TRIZ check, proceed to menu

---

### 9. Present MENU OPTIONS

Display: "**Select an Option:** [T] TRIZ [A] Advanced Elicitation [P] Party Mode [C] Continue"

**[T] TRIZ** - Resolve contradictions (Step 4.5: Quick 5-10min / Structured 30-60min / ARIZ 2-4hr)
**[A] Advanced Elicitation** - 50+ techniques (see `../data/advanced-elicitation-methods.md`)
**[P] Party Mode** - Creative brainstorming ({partyModeWorkflow})
**[C] Continue** - Proceed with recommendations

#### Menu Handling Logic:
- IF T: Execute Step 4.5 TRIZ analysis, when finished redisplay the menu
- IF A: Load `../data/advanced-elicitation-methods.md`, execute, when finished redisplay the menu
- IF P: Read {partyModeWorkflow}, execute, when finished redisplay the menu
- IF C: Save content to {workflowPlanFile}, update frontmatter, then load, read entire file, then execute {nextStepFile}
- IF Any other: help user, then [Redisplay Menu Options](#9-present-menu-options)

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After T/A/P execution, return to this menu

---

## 📊 Quick Feedback (Optional)

👍 Helpful | 😐 OK | 👎 Frustrating | [Enter to skip]

Save to memory: `user-context:feedback:step-04-consilium:{timestamp}`

---

## ADVANCED ELICITATION MODE

**Selected:** [A] Advanced Elicitation

**Subprocess:** Load and read entire `../data/advanced-elicitation-methods.md`, execute, return to menu.

**Methods:**
- [S] SCAMPER - 7 creative prompts (5-10 min)
- [5] Five Whys - Root cause analysis (5 min)
- [D] Devil's Advocate - Challenge assumptions (10 min)
- [B] Back to consilium menu

Auto-saves results to workflow plan + global memory.

💡 **Complete protocol:** `../data/advanced-elicitation-methods.md`

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- All specialists accounted for
- Recommendations captured and confirmed
- Consensus recorded in {workflowPlanFile}

### ❌ SYSTEM FAILURE:
- Skipping specialist input
- Scoring or prioritizing prematurely
- Not appending to plan before continuing

**Master Rule:** Consilium captures expert guidance only; no scoring here.




