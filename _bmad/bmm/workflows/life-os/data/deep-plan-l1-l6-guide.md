# Deep Plan L1-L6 Detailed Guide

## L1-L6 Structure Overview

### L1: High-Level Overview / Role/Mission
**Purpose:** Define the top-level goal, role, or mission for the project

**L1-L3 Track:**
- 2-3 paragraphs describing what, why, and how
- High-level technical approach
- Key strategic decisions

**L1-L6 Track:**
- Clear role definition or mission statement
- Why this role/approach is chosen
- Overall contribution philosophy

**Examples:**
- L1: Technical Advisor - Guide architecture decisions and code reviews
- L1: Research Lead - Coordinate research efforts and synthesize findings
- L1: Product Owner - Define features and prioritize backlog

---

### L2: Major Phases / Contribution Areas
**Purpose:** Break the mission into 2-5 major areas or phases

**L1-L3 Track:**
- 3-5 major phases with duration estimates
- Phase name, goal, key activities
- Sequential or parallel execution noted

**L1-L6 Track:**
- 2-5 distinct contribution areas
- Each area represents a different type of work
- Can run in parallel or sequentially

**Examples:**
- L2: Architecture Design (Weeks 1-3)
- L2: Code Review & Quality (Ongoing)
- L2: Knowledge Transfer (Weeks 8-10)

**Auto-Linking Opportunity:**
- Business goals → Finance frameworks (NPV, ROI)
- Health goals → Personal frameworks (Habit Loop)
- Learning goals → Knowledge frameworks (Spaced Repetition)

---

### L3: Work Streams / Key Milestones
**Purpose:** Define specific streams of work within each area

**L1-L3 Track:**
- 5-8 key milestones across all phases
- Milestone name, target date, success criteria
- Deliverables per milestone

**L1-L6 Track:**
- 2-4 work streams per L2 area
- Each stream is a focused effort
- Clear boundaries between streams

**Examples (for Architecture Design):**
- L3: System Design Documentation
- L3: Database Schema Planning
- L3: API Contract Definitions

---

### L4: Stages
**Purpose:** Break each work stream into sequential stages

**L1-L6 Track Only:**
- 2-5 stages per work stream
- Each stage represents a phase of completion
- Dependencies between stages mapped

**Examples (for System Design Documentation):**
- L4: Initial Draft (Week 1)
- L4: Review & Feedback (Week 2)
- L4: Final Revision (Week 3)

**Critical Path Identification:**
- Mark stages on critical path
- Note parallel stages that can run concurrently

---

### L5: Tasks
**Purpose:** Break stages into actionable tasks

**L1-L6 Track Only:**
- 3-10 tasks per stage
- Each task is a distinct work unit
- 1-4 hours per task typically

**Examples (for Initial Draft stage):**
- L5: Research existing architecture patterns
- L5: Draft high-level component diagram
- L5: Document data flow between components
- L5: Define integration points

**Auto-Linking Opportunity:**
- Tasks from Habit Loop sequences
- Tasks from Pomodoro work blocks
- Tasks from OKR key results

---

### L6: Atomic Actions
**Purpose:** Break tasks into smallest executable steps

**L1-L6 Track Only:**
- 2-5 atomic actions per task
- Each action takes <30 minutes
- Fully executable without decisions

**Examples (for "Draft component diagram"):**
- L6: Open diagramming tool
- L6: Create database layer box
- L6: Create API layer box
- L6: Draw connections between layers
- L6: Add labels and annotations

---

## Scenario-Based Templates

### Tech Expert Template
**Use when:** Contributing technical expertise to existing project

**L1:** Technical Advisor/Expert
**L2:** Code Review, Architecture Guidance, Performance Optimization
**L3:** (per area) Specific review types or optimization targets
**L4:** Stages of review/optimization cycle
**L5:** Specific review/optimization tasks
**L6:** Individual analysis steps

**Load from:** `.part-techexpert.md`

---

### Research Template
**Use when:** Leading or contributing to research efforts

**L1:** Research Lead/Contributor
**L2:** Literature Review, Data Collection, Analysis, Synthesis
**L3:** (per area) Specific research streams
**L4:** Research phases (planning, execution, reporting)
**L5:** Research tasks (reading papers, running experiments)
**L6:** Individual research actions

**Load from:** `.part-research.md`

---

### Ops/Support Template
**Use when:** Handling operations, maintenance, or support

**L1:** Operations Lead/Engineer
**L2:** Monitoring, Incident Response, Maintenance, Documentation
**L3:** (per area) Specific operational streams
**L4:** Operational cycles or phases
**L5:** Operational tasks (checks, updates, fixes)
**L6:** Individual operational actions

**Load from:** `.part-ops.md`

---

### Product Template
**Use when:** Defining product features and requirements

**L1:** Product Owner/Manager
**L2:** Discovery, Definition, Prioritization, Delivery
**L3:** (per area) Feature sets or user journeys
**L4:** Product development stages
**L5:** Product tasks (specs, wireframes, user stories)
**L6:** Individual product actions

**Load from:** `.part-product.md`

---

### Invited Role (Fallback)
**Use when:** Role is unclear or doesn't match above

**L1:** Contributor (role to be defined)
**L2:** Discovery, Execution, Review, Handoff
**L3:** (per area) General contribution streams
**L4:** Generic stages
**L5:** Flexible task structure
**L6:** Minimal atomic actions

**Load from:** `.part-invited.md`

---

## Quality Standards by Depth

### L1-L3 Quality Requirements
- ✅ Clear high-level structure
- ✅ 3-5 major phases defined
- ✅ 5-8 key milestones identified
- ✅ Phase durations specified (weeks, not "soon")
- ✅ 20-30 tasks outlined across all milestones
- ✅ Top 3 risks identified
- ✅ 800-1200 words total output

### L1-L6 Quality Requirements
- ✅ Full L1-L6 depth (not stopping at L2-L3)
- ✅ Specific timelines (weeks and dates)
- ✅ 100+ tasks broken down by phase
- ✅ Dependencies mapped (critical path visible)
- ✅ Risk analysis (5-8 risks minimum)
- ✅ Contingencies for high-severity risks
- ✅ Assumptions validated
- ✅ 2000-3000 words total output
- ✅ RACI coverage ≥70% at L2
- ✅ If-Then coverage ≥2 contingencies

---

## Common Mistakes to Avoid

### ❌ WRONG: Stopping at L2-L3 for Deep Track
```markdown
L1: Technical Advisor
L2: Code Review
L2: Architecture Guidance
[STOPS HERE - Missing L3-L6 depth]
```

### ✅ RIGHT: Full L1-L6 depth
```markdown
L1: Technical Advisor
  L2: Code Review
    L3: Backend Code Review
      L4: Initial Review (Week 1)
        L5: Review authentication module
          L6: Check password hashing
          L6: Verify session management
        L5: Review database queries
      L4: Follow-up Review (Week 2)
```

---

### ❌ WRONG: Vague timelines
```markdown
L4: Soon
L4: Later this month
L4: Eventually
```

### ✅ RIGHT: Specific timelines
```markdown
L4: Week 1 (Jan 15-19)
L4: Week 2-3 (Jan 22-Feb 2)
L4: Month 2 (Feb 5-28)
```

---

### ❌ WRONG: Too few tasks
```markdown
L5: Do the thing
L5: Review stuff
[Only 2 tasks for entire project]
```

### ✅ RIGHT: Sufficient task breakdown
```markdown
L5: Research authentication patterns
L5: Draft security requirements
L5: Design session architecture
L5: Document token lifecycle
L5: Create API contract
[20-30 tasks minimum for L1-L3, 100+ for L1-L6]
```
