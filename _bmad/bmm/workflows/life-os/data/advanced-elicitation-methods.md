# Advanced Elicitation Methods

**Purpose:** Structured creativity techniques for consilium enhancement

**Available Methods:**
- SCAMPER (7 creative prompts)
- Five Whys (root cause analysis)
- Devil's Advocate (challenge assumptions)

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
