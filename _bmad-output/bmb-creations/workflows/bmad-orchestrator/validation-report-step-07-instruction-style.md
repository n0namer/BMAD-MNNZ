---
validationStep: 'step-07-instruction-style-check'
validatedDate: '2026-02-26'
workflowName: 'bmad-orchestrator'
targetPath: '_bmad-output/bmb-creations/workflows/bmad-orchestrator/'
status: 'COMPLETE'
---

# Validation Report: Instruction Style Check (Step 07)

**Workflow:** bmad-orchestrator
**Validation Date:** 2026-02-26
**Validator:** Code Review Agent
**Total Steps Analyzed:** 7 (6 creation steps + 1 continuation step)

---

## Domain Classification

**Workflow Domain:** BMAD Orchestration / Meta-workflow
**Domain Type:** Mixed (Collaborative Facilitation + Prescriptive Execution)
**Appropriate Instruction Style:** **Mixed** (Intent-based for discovery/planning, Prescriptive for execution)

**Reasoning:**
- Primary purpose: Dynamically orchestrate BMAD workflows and manage execution
- User interaction: Collaborative dialogue (discovery, selection, planning) + autonomous execution
- Requires: Clear guidance structure for phase transitions, intentional facilitation for decision-making
- Domain classification supports the mixed instruction style found in the workflow

---

## Instruction Style Analysis by Step

### Step 01: Discovery

**File:** `steps-c/step-01-discovery.md`

**Style Classification:** **INTENT-BASED (with prescribed structure)**

**Style Indicators Observed:**
- Uses facilitative language: "Tell me about your task", "Let me understand better"
- Multi-turn conversation encouraged: "Ask 1-2 questions at a time, think about their response"
- Goal-oriented not script-oriented: "Focus ONLY on understanding the orchestration task"
- Probe language: "Think about their response before asking more", "ask follow-ups"
- Flexible guidance: "Ask about specific workflow selections yet" (FORBIDDEN), allowing adaptive conversation

**Evidence of Intent-Based Approach:**
```markdown
### 2. Listen and Probe

As they describe their task:

**DO:**
- Listen carefully
- Ask 1-2 follow-up questions at a time
- Think about their response before asking more
- Probe for: What files? What's the goal? What's the current state?

**DON'T:**
- Ask about specific workflow selections yet
- Rapid-fire questions
- Jump to solutions
```

**Appropriateness Assessment:** ✅ **PASS**
- Intent-based style appropriate for discovery phase
- Facilitates collaborative understanding
- Encourages multi-turn dialogue
- Aligns with workflow's collaborative goal
- No inappropriate prescriptive elements

**Quality Notes:**
- Excellent use of DO/DON'T guidance
- Clear role reinforcement ("YOU ARE A FACILITATOR, not a content generator")
- Multi-turn conversation explicitly enabled

---

### Step 02: Workflow Selection

**File:** `steps-c/step-02-workflow-selection.md`

**Style Classification:** **INTENT-BASED (with structured presentation)**

**Style Indicators Observed:**
- Uses analytical language: "Analyze task and match to BMAD workflow patterns"
- Presentation-oriented: "Present 2-4 workflow options with clear reasoning"
- User-confirming: "Let user confirm or adjust selections"
- Flexible decision-making: "You can... Select one... Request workflows... Search... Combine... Auto-select"
- No prescriptive scripts; reasoning-based presentation

**Evidence of Intent-Based Approach:**
```markdown
### 2. Analyze Task Against Patterns

Based on discovery from Step 1, analyze:

"**Let me analyze your task and match it to BMAD workflow patterns from our library of 75+ workflows...**

Your task involves:
- [Task type from discovery: creating/updating/synchronizing/analyzing]
- [Domain from discovery: PRD/UX/Arch/Testing/etc.]
- [File types mentioned]

**Scanning workflow library for matches...**"

Present 2-4 options from appropriate categories:
```

**Appropriateness Assessment:** ✅ **PASS**
- Intent-based style appropriate for selection phase
- Presents options with reasoning, not scripts
- Multiple pathways offered (user can select, search, auto-select, combine)
- Facilitates informed decision-making
- Aligns with collaborative orchestration workflow

**Quality Notes:**
- Good balance between guidance and flexibility
- Clear option presentation with "Why" reasoning
- User agency preserved throughout

---

### Step 03: Orchestration Plan

**File:** `steps-c/step-03-orchestration-plan.md`

**Style Classification:** **MIXED (Intent-based planning + Prescriptive for technical analysis)**

**Style Indicators Observed:**
- Intent-based sections: "Build dependency graph", "Analyze workflow dependencies"
- Structured but flexible: "Analyze workflows: [list], Target files: [list]" - variables not exact scripts
- User confirmation required: "Does this plan look correct? Any adjustments needed?"
- References external documentation: "See `/data/conflict-detection-patterns.md`" (pattern-based analysis)
- Prescriptive elements: "FOR each workflow, identify inputs, outputs, dependencies" (task instruction, not user dialogue)

**Mixed Style Example:**
```markdown
### 1. Build Dependency Graph

"**Building orchestration plan...**

Analyzing workflows: [list selected workflows]
Target files: [list files from discovery]

**Dependency Analysis:**"

For each workflow, identify inputs, outputs, dependencies.
See `/data/conflict-detection-patterns.md` for examples.
```

**Appropriateness Assessment:** ✅ **PASS**
- Mixed style appropriate for orchestration planning phase
- Intent-based for user interaction and confirmation
- Prescriptive only for technical analysis (not user communication)
- Balance reflects domain requirements: collaborative decision + technical precision
- No inappropriate prescriptive user dialogue

**Quality Notes:**
- Good separation between "what to do" (prescriptive/internal) and "how to communicate" (intent-based/user-facing)
- References external technical patterns appropriately
- User decision points clearly marked

---

### Step 04: Execution Loop

**File:** `steps-c/step-04-execution-loop.md`

**Style Classification:** **MIXED (Prescriptive for execution, Intent-based for user interaction)**

**Style Indicators Observed:**
- Task execution prescriptive: "Follow the plan precisely", "Execute according to orchestration plan"
- Plan adherence critical: "FORBIDDEN to deviate from plan without user approval"
- Progress reporting intent-based: "Report progress after each phase"
- Checkpoint flexibility: "Allow [C] Continue or pause at each checkpoint"
- User choices preserved: Menu options for Advanced Elicitation, Party Mode, Continue

**Prescriptive Execution Pattern (Appropriate):**
```markdown
### Step-Specific Rules:

- 🎯 Execute according to orchestration plan
- 🚫 FORBIDDEN to deviate from plan without user approval
- 💬 Report progress after each phase
- 🚪 Allow [C] Continue or pause at each checkpoint

## EXECUTION PROTOCOLS:

- 🎯 Follow dependency graph from orchestration plan
- 💬 Execute parallel zones via subagents
- 📖 Update frontmatter stepsCompleted after each phase
- 🚫 FORBIDDEN to skip phases or change order
```

**Appropriateness Assessment:** ✅ **PASS**
- Mixed style appropriate for execution phase
- Prescriptive adherence necessary (prevents execution drift)
- Intent-based user communication (checkpoint menus, progress reports)
- Prescriptive elements appropriately applied to workflow execution, not user dialogue
- User retains control via checkpoint menus

**Quality Notes:**
- Clear distinction between autonomous execution (prescriptive) and user interaction (intent-based)
- Appropriate prescriptiveness for execution safety
- Checkpoint system provides user agency

---

### Step 05: Cascade Synchronization

**File:** `steps-c/step-05-cascade-sync.md`

**Style Classification:** **INTENT-BASED (with prescriptive structure for technical analysis)**

**Style Indicators Observed:**
- Collaborative language: "Propagate changes with minimal conflicts", "Maintain document consistency across cascade"
- User choice at each sync: "[A] Apply all changes automatically [R] Review each change [S] Skip [E] Edit changes"
- Facilitative approach: "Let user edit, then apply"
- Flexible handling: "Handle response: IF A: Apply... IF R: Show each... IF S: Document skip... IF E: Let user edit"
- Not prescriptive scripts; descriptive patterns

**Evidence of Intent-Based Approach:**
```markdown
### 3. Synchronize Each Related Document

For each related document:

"**Synchronizing: [dependent-file.md]**

Changes to propagate:
- [Change 1] — from master section [X]
- [Change 2] — metadata update

**Options:**
[A] Apply all changes automatically
[R] Review each change
[S] Skip this document
[E] Edit changes before applying

What would you like? [A/R/S/E]"

**Handle response:**
- IF A: Apply changes, document, move to next
- IF R: Show each change, ask confirm/skip/edit
- IF S: Document skip reason, move to next
- IF E: Let user edit, then apply
```

**Appropriateness Assessment:** ✅ **PASS**
- Intent-based style appropriate for cascade synchronization
- User agency maximized: multiple options at each sync point
- Facilitative communication throughout
- Technical tasks (change detection, propagation) use structural patterns, not user scripts
- Aligns with collaborative workflow design

**Quality Notes:**
- Excellent user choice preservation
- Clear communication of "what's changing and why"
- Flexible handling accommodates different user preferences

---

### Step 06: Validation

**File:** `steps-c/step-06-validation.md`

**Style Classification:** **INTENT-BASED (with prescriptive structure for technical validation)**

**Style Indicators Observed:**
- Verification-focused language: "Validate orchestration results", "Verify document consistency", "Check integrity"
- User confirmation at end: "User confirmed completion"
- Menu-based completion: "[A] Advanced Elicitation [P] Party Mode [C] Finish"
- Descriptive validation process: References external templates ("See `/data/validation-templates.md`")
- Not prescriptive dialogue; structured validation framework

**Evidence of Intent-Based Approach:**
```markdown
### 1. Orchestration Summary

"**FINAL VALIDATION PHASE**

**Orchestration Summary:**
- Workflows executed: [N]
- Documents created/updated: [M]
- Cascade synchronized: [Yes/No]

**Validating results...**"

### 10. Completion Confirmation

"**🎉 ORCHESTRATION COMPLETE!**

Your BMAD workflows have been successfully orchestrated!

**What you can do now:**
- Review the generated documents
- Check the traceability matrix
- Use `[A] Advanced Elicitation` for deeper analysis
- Use `[P] Party Mode` for team discussion
```

**Appropriateness Assessment:** ✅ **PASS**
- Intent-based style appropriate for final validation
- User agency preserved via Advanced Elicitation and Party Mode options
- Technical validation process uses structural patterns (from external templates), not scripts
- Completion confirmation conversational, not prescriptive
- Aligns with collaborative workflow completion

**Quality Notes:**
- Positive, collaborative tone for completion
- Options for further exploration (Advanced Elicitation, Party Mode)
- Session properly positioned for potential continuation

---

### Step 01b: Continue Orchestration

**File:** `steps-c/step-01b-continue.md`

**Style Classification:** **INTENT-BASED (with prescriptive state restoration)**

**Style Indicators Observed:**
- State restoration prescriptive: "Load previous plan document", "Restore context and state" (procedural, internal)
- User interaction intent-based: "Present Resume Options", "What would you like to do?"
- User agency maximized: "[C] Continue [R] Review and adjust [S] Start over [A] Advanced Elicitation"
- Flexible resumption: "IF user selects [C]... IF R: Show... IF S: Confirm... IF A: Run"
- Restoration dialogue collaborative: "Allow user to adjust before resuming"

**Evidence of Mixed Approach:**
```markdown
### 3. Determine Next Step

Based on `stepsCompleted` array in frontmatter:

**IF stepsCompleted includes:**
- `step-01-discovery` only → Next: `step-02-workflow-selection`
- `step-02-workflow-selection` → Next: `step-03-orchestration-plan`
...

### 4. Present Resume Options

"**RESUME OPTIONS**

**Current State:**
- Last completed: [step name]
- Next step: [step name]
- Progress: [X] of 6 steps

**What would you like to do?**

[C] Continue from next step ([step name])
[R] Review and adjust plan
[S] Start over (new session)
[A] Advanced Elicitation on current state

Select: [C/R/S/A]"
```

**Appropriateness Assessment:** ✅ **PASS**
- Mixed style appropriate for continuation step
- Prescriptive state restoration (internal procedure) well-separated from user interaction (intent-based)
- User choices clearly presented
- State restoration logic correct and sequenced properly
- Conversation pattern conversational, not prescriptive

**Quality Notes:**
- Good state restoration logic with clear conditionals
- Handles edge case of already-completed sessions ("SESSION ALREADY COMPLETE")
- User given options for new session, review, or restart

---

## Overall Instruction Style Assessment

### Workflow Domain Analysis

**Classification: MIXED (Collaborative Facilitation + Prescriptive Execution)**

The bmad-orchestrator workflow appropriately uses:
- **Intent-based style:** Discovery, workflow selection, cascade synchronization, validation, and continuation (user-facing dialogue)
- **Prescriptive structure:** Execution phases, internal procedural steps, technical analysis (non-dialogue elements)

This mixture is **APPROPRIATE** because:
1. Discovery/selection phases require flexible, collaborative dialogue (intent-based)
2. Execution phases require adherence to planned dependencies (prescriptive structure)
3. User maintains agency through checkpoint menus at each phase
4. Technical validation uses templates and patterns (prescriptive framework), not user scripts

### Style Consistency Assessment

**Pattern Consistency:** ✅ **CONSISTENT ACROSS WORKFLOW**

| Phase | Style | Consistency | Notes |
|-------|-------|-------------|-------|
| Discovery | Intent-based | Excellent | Facilitates dialogue |
| Selection | Intent-based | Excellent | Supports decision-making |
| Planning | Mixed | Excellent | Intent-based dialogue + prescriptive technical analysis |
| Execution | Mixed | Excellent | Prescriptive adherence + intent-based progress reporting |
| Sync | Intent-based | Excellent | User choice at each sync point |
| Validation | Intent-based | Excellent | Supports final review |
| Continue | Mixed | Excellent | Prescriptive state restoration + intent-based options |

---

## Step-by-Step Style Findings Summary

| Step | File | Style | Appropriateness | Issues |
|------|------|-------|-----------------|--------|
| 1 | step-01-discovery.md | Intent-based | ✅ PASS | None identified |
| 2 | step-02-workflow-selection.md | Intent-based | ✅ PASS | None identified |
| 3 | step-03-orchestration-plan.md | Mixed | ✅ PASS | None - appropriate mix |
| 4 | step-04-execution-loop.md | Mixed | ✅ PASS | None - appropriate mix |
| 5 | step-05-cascade-sync.md | Intent-based | ✅ PASS | None identified |
| 6 | step-06-validation.md | Intent-based | ✅ PASS | None identified |
| 1b | step-01b-continue.md | Mixed | ✅ PASS | None - appropriate mix |

---

## Positive Findings

### Excellent Instruction Style Implementations

1. **Step 01 Discovery - Facilitative Excellence**
   - "YOU ARE A FACILITATOR, not a content generator" — clear role definition
   - DO/DON'T structure makes expectations explicit
   - Multi-turn conversation explicitly encouraged ("Ask 1-2 questions at a time, think about their response")
   - Blocks premature workflow selection ("FORBIDDEN to propose workflow selections in this step")

2. **Step 04 Execution Loop - Appropriate Prescriptiveness**
   - Prescriptive execution necessary (prevents drift)
   - Applied to workflow execution, not user dialogue
   - Checkpoint menus preserve user agency ("Allow [C] Continue or pause at each checkpoint")
   - Clear separation of internal rules from user communication

3. **Step 05 Cascade Sync - User Agency Maximized**
   - Multiple options at each sync point ([A] Apply [R] Review [S] Skip [E] Edit)
   - "What would you like?" asks for user preference
   - Flexible handling accommodates different user preferences
   - Technical process uses structural patterns, not scripts

4. **Step 06 Validation - Collaborative Tone**
   - Completion message celebratory ("🎉 ORCHESTRATION COMPLETE!")
   - Offers continuation options (Advanced Elicitation, Party Mode, Review)
   - Positions session for future continuation
   - User remains engaged through options

5. **Consistent DO/DON'T Patterns**
   - Used effectively in Steps 1, 2, 3 to clarify expectations
   - Separates prescriptive rules from facilitative dialogue
   - Clear communication of role constraints

---

## Issues Identified

### Critical Issues

**None identified.** All steps use appropriate instruction styles for their domains.

### Minor Observations (Not Issues, but Worth Noting)

1. **Step 04 Execution Loop - Assumed Complexity**
   - Instructions reference external `execution-patterns.md` without embedding patterns
   - **Not an issue** — design follows pattern of referencing data files
   - Benefit: Keeps step files focused on logic, not exhaustive pattern documentation

2. **Step 06 Validation - Similar Reference Pattern**
   - Instructions reference `/data/validation-templates.md` for specifics
   - **Not an issue** — consistent with workflow's documentation strategy
   - Benefit: Centralizes technical validation patterns in one location

### Style Inconsistencies

**None identified.** Instruction style remains consistently appropriate throughout the workflow.

---

## Domain Appropriateness Validation

### Intent-Based Sections (Discovery, Selection, Sync, Validation)
✅ **Appropriate for creative/collaborative domains**
- Users engage in dialogue to clarify goals
- Multiple valid approaches supported
- LLM adapts based on user input
- No exact scripts required

### Prescriptive Structure (Planning, Execution, State Restoration)
✅ **Appropriate for technical orchestration phases**
- Internal procedural steps need consistency
- Execution phases need adherence to prevent conflicts
- State restoration needs logical sequencing
- Not applied to user-facing dialogue

### Mixed Approach (Steps 3, 4, 1b)
✅ **Appropriate for transitions and complex phases**
- Technical precision where needed (dependency analysis, state restoration)
- Collaborative dialogue for user decisions
- Clear separation between internal and user-facing instructions
- Balance reflects domain requirements

---

## Context Boundaries Met

✅ **PASS - All Context Boundaries Properly Observed**

- Discovery focused on understanding (no workflow proposals) ✅
- Workflow selection doesn't plan execution ✅
- Planning doesn't execute workflows ✅
- Execution follows plan strictly ✅
- Sync doesn't validate ✅
- Validation confirms completion ✅
- Continuation properly restores state ✅

---

## Quality Metrics

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Steps with appropriate style | 100% | 7/7 | ✅ PASS |
| Intent-based dialogue preserved | 100% | Yes | ✅ PASS |
| Prescriptive elements appropriate | 100% | Yes | ✅ PASS |
| User agency maintained | 100% | Yes | ✅ PASS |
| DO/DON'T clarity | High | Excellent | ✅ PASS |
| Role reinforcement | Clear | Explicit | ✅ PASS |
| Context boundaries honored | 100% | Yes | ✅ PASS |
| Instruction style consistency | High | Consistent | ✅ PASS |

---

## Recommendations

### Improvements (Not Required, but Consider for Future Versions)

1. **Consider adding instruction style legend at workflow root**
   - Quick reference for readers
   - Explains why each step has its specific style
   - Could improve comprehension for new users

2. **Embed short pattern examples in steps**
   - Instead of only referencing external files
   - Would improve step self-containment
   - Keep references as full documentation

3. **Add session restoration checklist in step-01b**
   - Could make continuation process more transparent
   - Let user verify restored state before proceeding
   - Minor usability enhancement

---

## Final Assessment

### Overall Status

**✅ VALIDATION PASSED**

**Instruction Style Quality: EXCELLENT**

The bmad-orchestrator workflow demonstrates **exemplary instruction style implementation**:

1. **Appropriate domain classification** — Recognizes mixed nature of orchestration work
2. **Consistent application** — Intent-based for dialogue, prescriptive for execution
3. **User agency preserved** — Multiple options at decision points, checkpoint menus
4. **Clear role definitions** — Facilitator vs. executor roles explicitly stated
5. **Well-organized structure** — DO/DON'T patterns, mandatory sequences
6. **Professional tone** — Collaborative, clear, inclusive language throughout
7. **Technical soundness** — Execution adherence balanced with user flexibility
8. **Completion quality** — Validation and continuation properly handled

**No critical issues identified. Workflow ready for implementation.**

---

## Next Steps

**For Validation Process:**
- Proceed to Step 08: Collaborative Experience Check ✅
- This step completes instruction style validation ✅
- Ready to advance to cooperative/user experience validation ✅

**For Workflow Implementation:**
- Instruction style solid; focus implementation on execution patterns
- Consider embedding short examples (recommendation #2)
- Monitor first few sessions for user feedback on clarity

---

**Report Generated:** 2026-02-26
**Validation Step:** 07 of 09
**Status:** ✅ COMPLETE - Ready for Next Validation Step

*This validation confirms that the bmad-orchestrator workflow uses appropriate instruction styles that match the domain requirements, maintain user agency, and provide clear guidance for both AI facilitators and human users.*
