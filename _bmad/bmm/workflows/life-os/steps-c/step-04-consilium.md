---
name: 'step-04-consilium'
description: 'Assemble specialist consilium and capture recommendations'
nextStepFile: './step-05-scoring.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 4: Consilium

## STEP GOAL:

Assemble a focused consilium of specialists (Lite or Deep), capture their recommendations, and record a consensus summary.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', read entire file
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Step-Specific Rules:
- 🤝 Proactive guidance: highlight risks, opportunities, and next best actions based on current context
- 🧭 If WIP/kill criteria or portfolio risks appear, surface them early with a brief recommendation
- ✅ Ask for user confirmation before taking any proactive action that changes scope or priorities
- 🎯 Focus ONLY on consilium assembly and recommendations
- 🚫 FORBIDDEN to score or prioritize in this step
- 💬 Ask the user to confirm each specialist’s input

## EXECUTION PROTOCOLS:

### Proactive Advice & Best Practices (MCP)
- If the user asks for advice, best practices, or recommendations, use MCP search (if available) to retrieve current guidance.
- Summarize findings concisely and cite sources when possible.
- If MCP search is unavailable, provide best-effort guidance and note the limitation.

### Search Orchestrator Protocol (Required)
- Follow data/mcp_search_system_prompt_xml.md.
- Execute: CLI memory search -> local MD (rg) -> web/MCP.
- Convene consilium to rank 2–4 options with pros/cons and recommendation.
- Ask user to choose before proceeding.

### Semantic Decision Support
If a decision or prioritization remains unclear, use Search Orchestrator to rank 2–3 options.

- 🎯 Identify the selected specialists from the workflow plan
- 💾 Append consilium notes to {workflowPlanFile}
- 📖 Keep recommendations concise and attributable
- 🧾 Record evidence snapshot in journal or workflow plan
- 📘 Record decision in project decisions file (if exists)

## CONTEXT BOUNDARIES:

- Available context: workflow plan content
- Focus: specialist recommendations and consensus
- Dependencies: step-03 specialist match must be complete

## MANDATORY SEQUENCE

### 1. Load Specialist List

Open {workflowPlanFile} and locate the "Specialist Matching" section.
Summarize the selected specialists to the user.

### 2. Determine Consilium Mode (Automatic, Semantic)

Use Search Orchestrator to confirm best mode and specialist subset:
1) CLI memory search (prior cases)
2) Local MD search (existing consilium logs)
3) Web/MCP if ambiguity remains

Default rule:
- If any **high** priority roles exist, use **Deep** with those roles + 1–2 medium.
- Otherwise use **Lite** with top 1–2 medium roles.

Announce the chosen mode and selected specialists, then proceed.

### 3. Gather Recommendations (Six Thinking Hats - Auto-Assign)

**Six Thinking Hats Integration (Universal Method - Embedded):**

Claude will automatically assign Six Thinking Hats roles to specialists based on their expertise:

| Specialist Type | Hat Color | Perspective |
|----------------|-----------|-------------|
| **Market Analyst, Data Scientist, Finance** | ⚪ White Hat | Facts, data, information |
| **User Researcher, Psychologist, Recovery** | 🔴 Red Hat | Emotions, intuition, gut feelings |
| **Risk Advisor, Security, Legal** | ⚫ Black Hat | Caution, risks, weaknesses |
| **Portfolio Manager, Growth Lead, Fitness Coach** | 🟡 Yellow Hat | Benefits, optimism, opportunities |
| **Innovation Expert, Growth/GTM, Creative** | 🟢 Green Hat | Creativity, alternatives, new ideas |
| **Product Strategist, Operations, Facilitator** | 🔵 Blue Hat | Process, organization, meta-thinking |

**How it works:**
1. For each selected specialist, auto-assign hat based on role
2. Guide specialist to provide recommendations FROM THAT PERSPECTIVE
3. If specialist falls outside categories, assign based on context

**Prompt format for each specialist:**

"{Specialist Name} ({Hat Color} Hat - {Perspective}), please share your view:
- {Hat-specific question}

Keep recommendations focused on your hat's perspective."

**Hat-specific questions:**
- ⚪ White: "What facts and data do we have? What's missing?"
- 🔴 Red: "What's your gut feeling? What emotions does this evoke?"
- ⚫ Black: "What could go wrong? What risks do we need to mitigate?"
- 🟡 Yellow: "What are the benefits? Why is this worth doing?"
- 🟢 Green: "What creative alternatives exist? How can we innovate?"
- 🔵 Blue: "How should we structure this? What's the right process?"

**Execution:**

For each selected specialist:
1. Auto-assign hat color based on specialist type (use table above)
2. Present hat-specific question from their perspective
3. Ask user to provide or confirm their input
4. Record each recommendation as a short bullet list with hat color prefix

Ask 1–2 specialists at a time and adapt based on the user's response.

### 4. Synthesize Consensus (Balanced Multi-Perspective)

**After gathering all perspectives, synthesize consensus by balancing:**
- ⚪ White Hat facts (data-driven insights)
- 🔴 Red Hat intuition (emotional/gut responses)
- ⚫ Black Hat cautions (risks and concerns)
- 🟡 Yellow Hat benefits (opportunities and value)
- 🟢 Green Hat creativity (alternatives and innovation)
- 🔵 Blue Hat structure (process and organization)

This creates a **balanced, multi-perspective decision** vs single-viewpoint bias.

Ask the user to confirm a 2–4 bullet "consensus view" that captures shared guidance across all hat perspectives.

### 5. Auto-Suggest Framework (Embedded Intelligence)

**After consilium completes, AI analyzes and suggests frameworks:**

**Triggers for Auto-Suggest:**
1. **Keyword Match** (confidence >70%)
   - Business keywords → Lean Canvas, BMC, SWOT
   - Finance keywords → NPV, DCF, Monte Carlo
   - Health keywords → HBM, Habit Loop, Progressive Overload
   - Personal keywords → Pomodoro, Atomic Habits, GTD

2. **Consilium Divergence** (≥40%)
   - High divergence indicates contradiction
   - Auto-suggest TRIZ for systematic resolution

3. **Domain Detection**
   - Scans workflow plan for domain indicators
   - Suggests 2-3 top frameworks per domain

**Suggestion Format:**
```
💡 **Framework Suggestion**

Based on your project ({detected pattern}), I recommend **{Framework Name}**.

**Why this framework:**
- {Reason 1 from consilium or keywords}
- {Reason 2 from past successful patterns}
- {Reason 3 from domain best practices}

**Time investment:** {quick|moderate|intensive}
**Confidence:** {percentage}% match

[✅ Use {Framework}] [⏭️ Skip] [ℹ️ Tell me more]
```

**If multiple frameworks suggested:**
Show top 3 with confidence scores, let user select 1-3.

**Memory integration:**
```bash
# Log suggestion acceptance
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "auto-suggest:{framework}:accepted:{project_id}" \
  --content "Confidence {%}, User accepted, Domain {domain}"
```

### 7. Append to Workflow Plan

Append:
```markdown
## Consilium Recommendations (Six Hats)

**Mode:** {Lite/Deep}
**Specialists Consulted:**
- {Specialist 1} ({Hat Color} Hat - {Perspective}): {key recommendations}
- {Specialist 2} ({Hat Color} Hat - {Perspective}): {key recommendations}
- {Specialist 3} ({Hat Color} Hat - {Perspective}): {key recommendations}

**Consensus View (Balanced):**
- {synthesis balancing all hat perspectives}
- {key decision informed by multi-perspective input}
```

### 8. Present MENU OPTIONS

💡 **Method Options Available:**

**[T] TRIZ - Contradiction Resolution (Optional)**
- **When to use:** Consilium revealed contradictions (e.g., "Speed vs Quality", "Cost vs Performance")
- **What happens:** Launch Step 4.5 - TRIZ Analysis with 3 modes (Quick 5-10min / Structured 30-60min / Full ARIZ 2-4hr)
- **Outputs:** Resolved contradiction using TRIZ principles, updated consilium view
- **Skip if:** No clear contradictions, or contradiction is acceptable

**[A] Advanced Elicitation**
- Deep dive with 50+ elicitation techniques

**[P] Party Mode**
- Creative brainstorming session with specialist personas

**Choose next action:**

**[T] TRIZ** - Resolve contradictions (if consilium reveals conflicts)
**[A] Advanced Elicitation** - Get more specialist perspectives
**[P] Party Mode** - Celebrate divergence
**[C] Continue** - Proceed with current recommendations

➡️ **Your choice:** [T/A/P/C]

#### Menu Handling Logic:
- IF T: Proceed to Step 4.5: TRIZ Analysis (optional). After TRIZ completes, return here and redisplay the menu
- IF A: Enter Advanced Elicitation Mode (see section below), then redisplay the menu after completion
- IF P: Read fully and follow: {partyModeWorkflow} to explore additional perspectives, then redisplay the menu
- IF C: Save content to {workflowPlanFile}, update frontmatter, then load, read entire file, then execute {nextStepFile}
- IF Any other: help user respond, then redisplay menu

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After A/P execution, return and redisplay this menu

---

## ADVANCED ELICITATION MODE

### Entry Point

**You selected:** [A] Advanced Elicitation

This mode adds structured creativity techniques to the consilium process, helping generate breakthrough insights beyond standard expert recommendations.

**Choose elicitation method:**

**[S] SCAMPER** - 7 creative prompts for innovation (5-10 min)
**[5] Five Whys** - Root cause analysis (5 min)
**[D] Devil's Advocate** - Challenge assumptions (10 min)
**[B] Back to Consilium** - Return to main menu

➡️ **Your choice:** [S/5/D/B]

---

### [S] SCAMPER Creative Prompts

**SCAMPER** = 7 systematic prompts to generate innovative alternatives.

**Purpose:** Transform existing consilium recommendations into breakthrough innovations by systematically exploring substitution, combination, adaptation, modification, alternative uses, elimination, and reversal.

**For each specialist recommendation, apply SCAMPER:**

| Prompt | Question | Purpose |
|--------|----------|---------|
| **S**ubstitute | Что можно заменить? (What can be replaced?) | Replace component/process |
| **C**ombine | Что можно объединить? (What can be combined?) | Merge with something else |
| **A**dapt | Что можно адаптировать? (What can be adapted?) | Borrow from other contexts |
| **M**odify | Что можно изменить? (What can be changed?) | Alter size/shape/attribute |
| **P**ut to another use | Как еще можно использовать? (How else can this be used?) | Repurpose |
| **E**liminate | Что можно убрать? (What can be removed?) | Remove non-essential |
| **R**everse/Rearrange | Что можно перевернуть/переставить? (What can be reversed/rearranged?) | Change order/direction |

---

#### SCAMPER Application Process

**Step 1: Select Recommendations**

Review the consilium recommendations captured earlier. Ask the user:

"Which 1-2 specialist recommendations would you like to enhance with SCAMPER creative prompts? (Enter specialist names or recommendation numbers)"

Wait for user selection.

---

**Step 2: Apply SCAMPER to Selected Recommendation**

For each selected recommendation, systematically ask all 7 SCAMPER questions.

**Template:**

```markdown
### SCAMPER Analysis: {Specialist Name} Recommendation

**Original Recommendation:**
"{specialist recommendation text}"

**SCAMPER Creative Exploration:**

#### S - Substitute
**Question:** "What if we replaced {key component X} with {alternative Y}?"

**User brainstorm (2-3 ideas):**
1. {Substitution idea 1}
2. {Substitution idea 2}
3. {Substitution idea 3}

---

#### C - Combine
**Question:** "What if we combined this recommendation with {another approach/tool/process Z}?"

**User brainstorm (2-3 ideas):**
1. {Combination idea 1}
2. {Combination idea 2}
3. {Combination idea 3}

---

#### A - Adapt
**Question:** "What similar problem has been solved in {other domain/industry}? How can we adapt that solution here?"

**User brainstorm (2-3 ideas):**
1. {Adaptation from domain 1}
2. {Adaptation from domain 2}
3. {Adaptation from domain 3}

---

#### M - Modify
**Question:** "What if we made it {bigger/smaller/faster/slower/more frequent/less frequent}?"

**User brainstorm (2-3 ideas):**
1. {Modification idea 1}
2. {Modification idea 2}
3. {Modification idea 3}

---

#### P - Put to Another Use
**Question:** "What else could this solution accomplish? What other problems could it solve?"

**User brainstorm (2-3 ideas):**
1. {Alternative use 1}
2. {Alternative use 2}
3. {Alternative use 3}

---

#### E - Eliminate
**Question:** "What happens if we remove {component/step/constraint}? Can we simplify?"

**User brainstorm (2-3 ideas):**
1. {Elimination idea 1}
2. {Elimination idea 2}
3. {Elimination idea 3}

---

#### R - Reverse/Rearrange
**Question:** "What if we did {X} before {Y} instead of after? What if we reversed the order or direction?"

**User brainstorm (2-3 ideas):**
1. {Reversal/rearrangement idea 1}
2. {Reversal/rearrangement idea 2}
3. {Reversal/rearrangement idea 3}

---
```

**Execution Notes:**
- Present ONE SCAMPER prompt at a time
- Wait for user to provide 2-3 ideas before moving to next prompt
- Encourage creative thinking without immediate judgment
- If user struggles, offer domain-specific examples

---

**Step 3: Identify Top SCAMPER Innovations**

After completing all 7 prompts, ask the user:

"From all the SCAMPER ideas generated, which 2-3 stand out as most innovative or promising?"

**Capture top ideas:**

```markdown
### Best SCAMPER Ideas

From all 7 prompts, the top innovative ideas are:

1. **{Innovative idea 1}** - from {S/C/A/M/P/E/R} prompt
   - **Why promising:** {brief explanation}

2. **{Innovative idea 2}** - from {S/C/A/M/P/E/R} prompt
   - **Why promising:** {brief explanation}

3. **{Innovative idea 3}** - from {S/C/A/M/P/E/R} prompt
   - **Why promising:** {brief explanation}
```

---

**Step 4: Create Enhanced Recommendation**

Synthesize the original recommendation with top SCAMPER innovations.

```markdown
### Enhanced Recommendation

**Original ({Specialist Name}):**
{original specialist recommendation}

**SCAMPER-Enhanced Version:**
{original recommendation PLUS integrated top SCAMPER ideas}

**Innovation Level:** {Incremental / Significant / Breakthrough}

**Key Innovations Added:**
- {Innovation 1} - via {SCAMPER prompt}
- {Innovation 2} - via {SCAMPER prompt}
- {Innovation 3} - via {SCAMPER prompt}

**Implementation Considerations:**
- {Any new constraints or requirements introduced}
- {Any new risks to evaluate}
- {Any new opportunities unlocked}
```

Ask user to confirm this enhanced recommendation before proceeding.

---

**Step 5: Append to Workflow Plan**

Add SCAMPER analysis results to the workflow plan:

```markdown
## SCAMPER Analysis (Advanced Elicitation)

**Applied to:** {Specialist Name}'s recommendation

**Original Recommendation:**
{original text}

**Top 3 SCAMPER Innovations:**
1. {Idea 1} - from {S/C/A/M/P/E/R} prompt
2. {Idea 2} - from {S/C/A/M/P/E/R} prompt
3. {Idea 3} - from {S/C/A/M/P/E/R} prompt

**Enhanced Recommendation:**
{Final recommendation incorporating SCAMPER insights}

**Innovation Level:** {Incremental / Significant / Breakthrough}

**Time Invested:** {X minutes}

**Next Steps:**
- Evaluate enhanced recommendation in scoring phase
- Consider SCAMPER innovations as separate opportunities
```

---

**Step 6: Store in Global Memory**

Execute CLI command to preserve SCAMPER insights for future projects:

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:methods:scamper:{project_id}:{timestamp}" \
  --content "{
    mode: 'SCAMPER',
    specialist: '{specialist_name}',
    original_recommendation: '{original text}',
    scamper_innovations: [
      '{idea1}',
      '{idea2}',
      '{idea3}'
    ],
    innovation_level: '{Incremental|Significant|Breakthrough}',
    time_invested_minutes: {X},
    domain: '{Business|Finance|Health|Personal}',
    effectiveness_rating: 'TBD_post_implementation'
  }"
```

---

**Step 7: Repeat or Return**

Ask the user:

"SCAMPER analysis complete for {Specialist Name}'s recommendation.

Would you like to:
- **[R]** Repeat SCAMPER for another recommendation
- **[C]** Continue to Advanced Elicitation menu
- **[B]** Back to Consilium main menu"

Wait for user choice and execute accordingly.

---

### Integration Notes: SCAMPER + Six Thinking Hats

**Complementary Relationship:**
- **Six Hats** = Different perspectives (White facts, Red emotions, Black risks, Yellow benefits, Green creativity, Blue process)
- **SCAMPER** = Specific innovation prompts within perspectives

**Synergy Opportunities:**
1. **Green Hat + SCAMPER:** Green Hat specialists naturally align with SCAMPER - use their creative recommendations as SCAMPER input
2. **Black Hat + Eliminate:** Black Hat risk analysis pairs well with SCAMPER's "Eliminate" prompt
3. **Yellow Hat + Combine:** Yellow Hat benefits thinking complements SCAMPER's "Combine" prompt
4. **White Hat + Modify:** White Hat data can inform what to modify (size, frequency, scale)

**Best Practice:**
- Use Six Hats first to gather diverse perspectives
- Apply SCAMPER to 1-2 most promising recommendations that need breakthrough thinking
- Return enhanced recommendations to consilium consensus

---

### [5] Five Whys Root Cause Analysis

**Status:** Template placeholder - to be implemented

**Purpose:** Drill down to root causes by asking "Why?" 5 times iteratively.

**Time:** ~5 minutes per recommendation

**Future Integration:** Similar structure to SCAMPER with iterative questioning, user input collection, and enhanced recommendation output.

---

### [D] Devil's Advocate Challenge

**Status:** Template placeholder - to be implemented

**Purpose:** Systematically challenge assumptions and explore worst-case scenarios.

**Time:** ~10 minutes per recommendation

**Future Integration:** Similar structure to SCAMPER with challenge questions, user responses, and strengthened recommendation output.

---

### Advanced Elicitation Exit

After completing any elicitation method (SCAMPER, Five Whys, Devil's Advocate), ALWAYS return to Advanced Elicitation menu:

**[S] SCAMPER** - 7 creative prompts for innovation (5-10 min)
**[5] Five Whys** - Root cause analysis (5 min)
**[D] Devil's Advocate** - Challenge assumptions (10 min)
**[B] Back to Consilium** - Return to main menu

This allows stacking multiple elicitation techniques on the same or different recommendations before returning to consilium scoring.

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




