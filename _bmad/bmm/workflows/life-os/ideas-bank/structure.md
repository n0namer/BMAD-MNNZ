# Ideas Bank: Organizational Structure

**Purpose:** Centralized system for capturing, evaluating, and activating ideas across all life spheres (health, wealth, relationships, growth, contribution).

**Philosophy:** Ideas are assets. Systematic evaluation prevents good ideas from getting lost while ensuring only high-impact ideas become projects.

---

## Directory Structure

```
ideas-bank/
├── structure.md                    # This file - organizational guide
├── README.md                       # Quick reference and statistics
├── inbox/                          # New ideas (not yet evaluated)
│   ├── IDEA-2025-001.md
│   ├── IDEA-2025-002.md
│   └── ...
├── evaluated/                      # Evaluated ideas (decided not to pursue now)
│   ├── rejected/                   # Ideas rejected after evaluation
│   │   ├── IDEA-2024-015.md
│   │   └── ...
│   ├── postponed/                  # Good ideas but wrong timing
│   │   ├── IDEA-2025-003.md
│   │   └── ...
│   └── accepted/                   # Ideas approved to move to planning
│       ├── IDEA-2025-005.md
│       └── ...
├── planned/                        # Ideas in planning (becoming projects)
│   ├── IDEA-2025-008.md
│   ├── IDEA-2025-009.md
│   └── ...
├── active/                         # Ideas activated as projects
│   ├── PROJ-2025-001/              # Linked to active project
│   │   └── idea-source.md          # Reference back to original idea
│   ├── PROJ-2025-002/
│   └── ...
├── completed/                      # Completed projects (from ideas)
│   ├── PROJ-2024-042/              # Project completion record
│   │   ├── idea-source.md
│   │   └── retrospective.md
│   └── ...
├── killed/                         # Projects killed mid-way
│   ├── PROJ-2024-035/              # Kill decision record
│   │   ├── idea-source.md
│   │   └── kill-decision.md
│   └── ...
└── archive/                        # Bulk storage for old ideas (>2 years)
    ├── YYYY/
    └── ...
```

---

## Idea Lifecycle

### 1. INBOX → Captured Not Yet Evaluated

**Status:** `status: inbox`

**What belongs here:**
- Raw ideas just captured
- Quick thoughts not yet developed
- Initial impulses to explore

**Requirements:**
- [ ] File named: `IDEA-YYYY-NNN.md`
- [ ] Frontmatter with: `id`, `title`, `sphere`, `created`, `status: inbox`, `tags`
- [ ] Quick capture (1-3 sentences)
- [ ] Context (optional but recommended)

**Action:**
- Add to ideas-bank/inbox/
- Review weekly in evaluation session
- Move to evaluated/ with decision

**Duration:** 1-4 weeks in inbox (ideas age out if not reviewed)

---

### 2. INBOX → EVALUATED (Decision Point #1)

**Evaluation Criteria:**

Each idea is scored on 4 dimensions (1-5 scale):

1. **Impact** - How significant are the benefits?
2. **Alignment** - How well does it support core goals?
3. **Effort** - How much time/resources required? (inverted scoring: lower effort = higher score)
4. **Timing** - Is now the right time?

**Scoring Formula:**
```
Total Score = Impact + Alignment + Effort + Timing
Score Range: 4-20
Threshold: 12+ for serious consideration
```

**Evaluation Process:**

```
1. Time: 15-20 minutes per idea
2. Reflect on each dimension
3. Assign scores and reasoning
4. Calculate total
5. Decision: accept/reject/postpone

Decision Logic:
- Score 16-20: "ACCEPT" → Move to planned/
- Score 12-15: "MAYBE" → Move to postponed/ OR discussed with stakeholder
- Score <12: "REJECT" → Move to rejected/
```

**Status After Evaluation:**
- Move to `evaluated/accepted/` if accepted
- Move to `evaluated/postponed/` if deferring
- Move to `evaluated/rejected/` if rejected

**Frontmatter Updates:**
```yaml
status: evaluated  # or accepted/postponed/rejected
evaluation:
  impact: 4        # (1-5)
  alignment: 5     # (1-5)
  effort: 4        # (5=minimal, 1=extreme)
  timing: 3        # (1-5)
  total-score: 16
decision:
  outcome: [accepted|postponed|rejected]
  reason: "Clear strategic alignment with GOAL-2025-001..."
  date: 2025-02-06
```

---

### 3. EVALUATED/ACCEPTED → PLANNED (Decision Point #2)

**Status:** `status: accepted` → `status: planned`

**What happens:**
- Write detailed Implementation Plan section
- Create project if moving to active

**Requirements for Planning:**
- [ ] Objective defined (success in 1 sentence)
- [ ] Approach (3-5 high-level steps)
- [ ] Resources needed (time, money, tools, people)
- [ ] Success criteria (2-4 measurable criteria)
- [ ] Risks identified with mitigations
- [ ] Timeline estimate (start, end, duration)

**Planning Session:**
```
1. Time: 30-60 minutes
2. Develop full implementation plan
3. Assess if ready for activation or should be postponed
4. Document decision
```

**Outcomes:**
- [ ] Activate immediately → Move to active/
- [ ] Schedule for activation → Move to planned/
- [ ] Reconsider timing → Move back to postponed/

**Frontmatter Updates:**
```yaml
status: planned
planning:
  objective: "Establish daily 30-min health routine tracking habit..."
  resources:
    time: "40 hours"
    money: null
    tools: ["Habit tracker app", "Health metrics dashboard"]
  success_criteria:
    - "Daily tracking maintained 30+ days"
    - "Health metrics baseline established"
  activation_planned: 2025-03-01
```

---

### 4. PLANNED → ACTIVE (Decision Point #3)

**Status:** `status: planned` → Becomes project: `PROJ-YYYY-NNN`

**What happens:**
- Idea becomes a formal project
- Create project directory with plan, tasks, artifacts
- Assign owner/lead
- Link back to original idea

**Activation Checklist:**
- [ ] Resources confirmed available
- [ ] Timeline agreed
- [ ] Owner and lead assigned
- [ ] First week's tasks defined
- [ ] Success criteria clear

**Project Linkage:**
```
ideas-bank/active/PROJ-2025-001/
├── idea-source.md          # Link to original idea
└── project-reference.md    # Link to projects/PROJ-2025-001/

projects/PROJ-2025-001/
└── idea-origin.md          # Back-reference to ideas-bank
```

**Frontmatter Updates:**
```yaml
status: active
project-id: PROJ-2025-001
activation:
  date: 2025-03-01
  owner: [person]
  lead: [person]
```

---

### 5a. ACTIVE → COMPLETED

**Status:** Completed project transferred

**Process:**
1. Project finishes with all success criteria met
2. Copy original idea file to ideas-bank/completed/PROJ-YYYY-NNN/idea-source.md
3. Add completion summary
4. Extract learnings

**Frontmatter Updates:**
```yaml
status: completed
project-id: PROJ-2025-001
completion:
  date: 2025-05-15
  final-status: "Success - exceeded goals"
  duration: "74 days"
  resources-actual: "38 hours"
  impact: "15% improvement in health metrics"
```

**Artifacts:**
```
ideas-bank/completed/PROJ-2025-001/
├── idea-source.md              # Original idea
├── project-summary.md          # What was built
├── retrospective.md            # What was learned
└── metrics-final.md            # Final results
```

---

### 5b. ACTIVE → KILLED

**Status:** Project terminated mid-way

**Process:**
1. Document kill decision with reasoning
2. Copy original idea to ideas-bank/killed/PROJ-YYYY-NNN/
3. Preserve learnings from partial work
4. Note what went wrong

**Kill Decision Reasons:**
- [ ] Out of alignment with current priorities
- [ ] Blocked by external dependencies
- [ ] Better alternative solution found
- [ ] Resource constraints
- [ ] Scope creep beyond viability
- [ ] Team capacity changed
- [ ] Problem solved by different approach
- [ ] Learnings achieved (partial success)

**Frontmatter Updates:**
```yaml
status: killed
project-id: PROJ-2025-001
kill:
  date: 2025-04-20
  reason: "Better alternative solution found"
  decision-owner: [person]
  work-preserved: "4 reusable components in artifacts/"
```

**Artifacts:**
```
ideas-bank/killed/PROJ-2025-001/
├── idea-source.md              # Original idea
├── kill-decision.md            # Why it was killed
├── work-done.md                # What was completed (40% of project)
├── learnings.md                # What was learned
└── salvageable-components/     # Reusable work preserved
```

---

### 6. ARCHIVE → Long-term Storage (>2 years old)

**Status:** Ideas archived when 2+ years old and not activated

**Process:**
1. Move old ideas to archive/
2. Keep for historical reference
3. Can resurrect if circumstances change

**Directory:**
```
ideas-bank/archive/
├── 2023/
│   ├── IDEA-2023-001.md
│   └── ...
├── 2024/
│   ├── IDEA-2024-001.md
│   └── ...
└── README-archive.md    # Why these were archived
```

---

## File Naming Conventions

### Idea Files

**Format:** `IDEA-YYYY-NNN.md`

**Components:**
- `IDEA` - Constant prefix
- `YYYY` - Year created (2025)
- `NNN` - Sequential number (001, 002, 003...)

**Examples:**
- `IDEA-2025-001.md` - First idea of 2025
- `IDEA-2025-042.md` - 42nd idea of 2025
- `IDEA-2024-099.md` - From prior year

**Numbering:**
- Restart at 001 each year
- Use sequential numbers
- Reserve range 001-999 per year

### Project Links

**When idea becomes project:**
- Original: `ideas-bank/inbox/IDEA-2025-005.md`
- Becomes: `projects/PROJ-2025-001/` (separate numbering)
- Link: Cross-reference with `project-id: PROJ-2025-001` in idea frontmatter

---

## Metadata Requirements (Frontmatter)

### Required Fields (All Ideas)

```yaml
---
id: IDEA-YYYY-NNN
title: [Concise title, 3-8 words]
sphere: [health|wealth|relationships|growth|contribution]
created: YYYY-MM-DD
status: [inbox|evaluated|accepted|postponed|rejected|planned|active|completed|killed]
tags: []
---
```

### Evaluation Fields (After Evaluation)

```yaml
evaluation:
  impact: [1-5 or null]          # Significance of benefits
  alignment: [1-5 or null]       # Support for goals
  effort: [1-5 or null]          # Time/resources (inverted)
  timing: [1-5 or null]          # Right time? (1-5)
  total-score: [4-20 or null]    # Sum of above
decision:
  outcome: [accepted|postponed|rejected]
  reason: "..."
  date: YYYY-MM-DD
```

### Planning Fields (When Planned)

```yaml
planning:
  objective: "..."
  resources:
    time: "X hours"
    money: "$X"
    tools: [...]
    people: [...]
  success-criteria:
    - "Criterion 1"
    - "Criterion 2"
  activation-planned: YYYY-MM-DD
```

### Project Linkage Fields

```yaml
project-id: PROJ-YYYY-NNN       # When activated
project-status: [active|completed|killed]
project-completion: YYYY-MM-DD
```

---

## Content Structure Template

All ideas follow this structure:

```markdown
---
[FRONTMATTER - see above]
---

# [Idea Title]

## Quick Capture
[1-3 sentences]

## Context
[Why? What problem? What opportunity?]

## Initial Thoughts
[Optional early ideas]

---

## Evaluation Criteria
[Completed after initial evaluation]

### Impact (1-5)
### Alignment (1-5)
### Effort (1-5, inverted)
### Timing (1-5)

**Total Score**: __/20

---

## Implementation Plan
[Completed before activation]

### Objective
### Approach
### Resources Needed
### Success Criteria
### Risks & Mitigations
### Timeline Estimate

---

## Decision Log

### Evaluation Decision
### Planning Decision

---

## Notes
[Any additional thoughts]

## Related Ideas
[Links to connected ideas]

## References
[Sources and inspiration]
```

---

## Workflow: Weekly Evaluation Session

**Cadence:** Every Sunday evening (or chosen day)

**Duration:** 45-60 minutes

**Process:**

```
1. COLLECT (5 min)
   - Review ideas in inbox/
   - Count total ideas waiting

2. EVALUATE (30-40 min)
   - Spend ~15-20 min per idea
   - Score on 4 dimensions
   - Make decision: accept/postpone/reject
   - Move to appropriate folder

3. ARCHIVE (5 min)
   - Check for 2+ year old ideas
   - Move to archive/ if appropriate

4. PLAN ACTIVATION (10 min)
   - Review planned/ folder
   - Decide which to activate next
   - Move to active/ and create project

5. SUMMARY (5 min)
   - Update README.md with stats
   - Note trends (inbox size, acceptance rate)
   - Plan for next week
```

**Session Output:**
- `inbox/` reviewed and cleared (target: <10 ideas waiting)
- Decisions documented
- Files moved to appropriate folders
- README.md updated with current counts
- Next week's activation planned

---

## Workflow: Monthly Metrics & Planning

**Cadence:** First of each month

**Duration:** 1-2 hours

**Metrics to Track:**

```
Total Ideas:
- Total captured (lifetime): ___
- Active in inbox: ___
- Evaluated this month: ___
- Accepted (cumulative): ___
- Activated as projects: ___
- Completed projects (from ideas): ___
- Killed projects: ___

Conversion Rates:
- Evaluation acceptance rate: __% (accepted / evaluated)
- Activation rate: __% (activated / accepted)
- Completion rate: __% (completed / activated)
- Overall success rate: __% (completed / accepted)

Quality Metrics:
- Average time inbox to decision: ___ days
- Average time decision to activation: ___ days
- Average project duration: ___ days
```

**Plan Next Month:**
- [ ] Ideas to prioritize for evaluation
- [ ] Target activation dates for planned ideas
- [ ] Projects approaching completion or risk
- [ ] Patterns in accepted vs rejected (what works?)

---

## Tips for Success

### Capture: Don't Lose Ideas

✅ **DO:**
- Capture immediately when idea strikes
- Use template to ensure consistency
- Add context while fresh
- Tag with sphere for later filtering

❌ **DON'T:**
- Store ideas in email or scattered notes
- Procrastinate filing them (batch weekly)
- Skip the template (consistency matters)
- Assume you'll remember details later

### Evaluate: Make Confident Decisions

✅ **DO:**
- Use the 4-dimension scoring system
- Set minimum score threshold (12+)
- Block time for evaluation (don't rush)
- Document reasoning for decisions

❌ **DON'T:**
- Evaluate too quickly (most ideas need 15+ min)
- Skip evaluation (ideas accumulate, become overwhelmed)
- Change decision criteria mid-month
- Keep ideas in limbo (make a clear decision)

### Plan: Prepare for Success

✅ **DO:**
- Write detailed implementation plan before activation
- Confirm resources available
- Define clear success criteria
- Set realistic timeline

❌ **DON'T:**
- Activate without a plan
- Overcommit (activate too many simultaneously)
- Skip timeline estimates (they inform scheduling)
- Assume "I'll figure it out" during execution

### Execute: Stay Accountable

✅ **DO:**
- Create formal project when activating
- Assign clear owner
- Track progress with metrics
- Update status regularly

❌ **DON'T:**
- Activate then disappear (ideas need monitoring)
- Abandon halfway (make explicit kill decision)
- Lose original idea context (keep backlink)
- Skip post-project learning (capture lessons)

---

## FAQ: Ideas Bank Management

**Q: How many ideas should I have in inbox?**
A: Target: <10. If >15, you need an evaluation session immediately. Ideas sitting >4 weeks need decisions.

**Q: What if an idea fails evaluation but seems good?**
A: If score <12, put in postponed/ not rejected/. Revisit monthly. Revisiting might reveal why it failed; might be wrong timing.

**Q: Can I activate multiple ideas simultaneously?**
A: Yes, if capacity exists. Typical: 3-5 active projects. More than that = high risk of none succeeding.

**Q: What happens to ideas in postponed/?**
A: Review monthly in planning session. If conditions change (more resources, goal shift, better timing), promote to planned. If still not right, archive after 1 year.

**Q: How do I avoid ideas in inbox languishing?**
A: Weekly evaluation session is mandatory. Anything >4 weeks old gets forced decision (evaluate or delete).

**Q: When I complete a project, where does the idea go?**
A: Copy to completed/PROJ-YYYY-NNN/ with completion summary and retrospective. Keep original idea in ideas-bank/ for reference, mark as `status: completed`.

---

## Tooling

### File Organization
- **Tool:** Markdown files + folder structure
- **Storage:** ideas-bank/ subdirectory
- **Version Control:** Commit to git weekly

### Tracking
- **Tool:** README.md with monthly metrics
- **Stats:** Track ideas by sphere, status, completion rate
- **Trends:** Identify patterns (what types of ideas work?)

### Linking
- **Forward:** Ideas → Projects (project-id in frontmatter)
- **Backward:** Projects → Ideas (link in project.md)
- **Cross:** Related ideas section in each file

### Search & Retrieval
- **By Status:** ls ideas-bank/{inbox|evaluated|planned|active}/
- **By Sphere:** grep "sphere:" ideas-bank/**/*.md
- **By Tag:** grep "tags:" ideas-bank/**/*.md
- **By Score:** grep "total-score:" ideas-bank/**/*.md

---

## Related Documents

- [Idea Template](../idea.template.md) - Template for new ideas
- [Project Activation Workflow](../workflow.md) - How ideas become projects
- [Goals Framework](../goals.template.yaml) - Strategic goals that guide evaluation
- [Decision Log](../decision-log.template.md) - Document decisions about ideas
- [Metrics Template](../metrics.template.md) - Track project outcomes

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2025-02-06 | Initial structure documentation |

---

## Questions & Improvements

If you notice gaps or have ideas about improving this system, add to "Ideas for the Ideas System" (meta, yes!) and bring to monthly review session.
