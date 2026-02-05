# Deep Plan Quality Gates & Checkpoints

## Overview

Quality gates ensure deep plans meet minimum standards before proceeding. This document defines validation criteria, checkpoint protocols, and common quality issues.

---

## L1-L3 Quality Standards (Standard Track)

### Minimum Requirements

| Criterion | Standard | Validation |
|-----------|----------|------------|
| **Depth Coverage** | L1-L3 present | All 3 levels exist with content |
| **Phase Definition** | 3-5 major phases | Count phase headers |
| **Milestone Count** | 5-8 key milestones | Count milestone entries |
| **Timeline Specificity** | Weeks or dates, not "soon" | No vague time references |
| **Task Breakdown** | 20-30 tasks outlined | Count task items across milestones |
| **Risk Identification** | Top 3 risks identified | Minimum 3 risk entries |
| **Word Count** | 800-1200 words | Total output length |

### Validation Checklist

```markdown
L1-L3 Quality Validation:

☐ L1 High-Level Overview exists (2-3 paragraphs: what, why, how)
☐ L2 Major Phases defined (3-5 phases with durations)
☐ L3 Key Milestones listed (5-8 milestones with dates)
☐ Timelines are specific (e.g., "Week 2-3" not "soon")
☐ Tasks outlined (20-30 total across all milestones)
☐ Top 3 risks identified with severity ratings
☐ Output length 800-1200 words

Score: __/7 criteria met

PASS: 7/7 criteria ✅
CONDITIONAL PASS: 5-6/7 criteria ⚠️
FAIL: <5/7 criteria ❌
```

---

## L1-L6 Quality Standards (Deep Track)

### Minimum Requirements

| Criterion | Standard | Validation |
|-----------|----------|------------|
| **Depth Coverage** | L1-L6 all present | All 6 levels exist, not stopping at L2-L3 |
| **Timeline Specificity** | Weeks AND dates | Specific dates for L4+ stages |
| **Task Breakdown** | 100+ tasks minimum | Count all L5 task items |
| **Dependency Mapping** | Critical path visible | Dependencies between stages marked |
| **Risk Analysis** | 5-8 risks minimum | Identified with severity and impact |
| **Contingency Planning** | High-severity risks have contingencies | If-Then actions defined |
| **Assumptions Validation** | Key assumptions documented | List of validated assumptions |
| **Word Count** | 2000-3000 words | Total output length |
| **RACI Coverage** | ≥70% at L2 | L2 nodes with R and A assigned |
| **If-Then Actions** | ≥2 contingencies | Count If-Then entries |

### Validation Checklist

```markdown
L1-L6 Quality Validation:

☐ L1 Role/Mission clearly defined
☐ L2 Contribution Areas (2-5 areas, not just 1)
☐ L3 Work Streams (2-4 per L2 area)
☐ L4 Stages (2-5 per work stream)
☐ L5 Tasks (3-10 per stage, 100+ total)
☐ L6 Atomic Actions (2-5 per critical tasks)
☐ Timelines: weeks for L2-L3, dates for L4+
☐ Dependencies mapped (critical path identified)
☐ Risk analysis: 5-8 risks with severity
☐ Contingencies for high-severity risks (If-Then)
☐ Assumptions validated (key assumptions listed)
☐ Output length 2000-3000 words
☐ RACI Coverage ≥70% at L2 (R and A assigned)
☐ If-Then Coverage ≥2 actions

Score: __/14 criteria met

PASS: 12-14/14 criteria ✅
CONDITIONAL PASS: 9-11/14 criteria ⚠️
FAIL: <9/14 criteria ❌
```

---

## Self-Validation Protocol

### Step 1: Automated Metrics Check

**Compute these metrics before showing user:**

```javascript
// Depth Coverage
const depthCovered = countLevelsPresent(plan) / 6  // For L1-L6
// Example: L1-L4 present = 4/6 = 0.67

// Node Count
const totalNodes = countAllLevelNodes(plan)
// Example: 15 L2 + 45 L3 + 120 L4 + 300 L5 + 180 L6 = 660 nodes

// RACI Coverage
const l2NodesWithRaci = countL2WithRandA(plan)
const totalL2Nodes = countL2Nodes(plan)
const raciCoverage = l2NodesWithRaci / totalL2Nodes
// Example: 12 L2 with RACI / 15 total L2 = 0.80 = 80%

// If-Then Coverage
const ifThenCount = countIfThenActions(plan)
// Example: 5 If-Then contingencies

// Timeline Specificity
const vagueDates = countVagueDateReferences(plan)  // "soon", "later", "eventually"
const specificDates = countSpecificDateReferences(plan)  // "Week 2", "Jan 15"
const timelineQuality = vagueDates === 0 && specificDates > 0
```

### Step 2: Quality Score Calculation

```javascript
// L1-L6 Quality Score (0.0 to 1.0)
const qualityScore = (
  (depthCovered >= 1.0 ? 0.2 : depthCovered * 0.2) +         // 20% - Depth
  (raciCoverage >= 0.7 ? 0.2 : raciCoverage * 0.2) +        // 20% - RACI
  (ifThenCount >= 2 ? 0.15 : ifThenCount * 0.075) +         // 15% - If-Then
  (totalNodes >= 100 ? 0.15 : totalNodes * 0.0015) +        // 15% - Task count
  (riskCount >= 5 ? 0.15 : riskCount * 0.03) +              // 15% - Risks
  (timelineQuality ? 0.15 : 0)                               // 15% - Timeline specificity
)

// Quality rating
if (qualityScore >= 0.85) return "PASS ✅"
if (qualityScore >= 0.70) return "CONDITIONAL PASS ⚠️"
return "FAIL ❌"
```

### Step 3: Present Quality Report

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 DEEP PLAN QUALITY REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Overall Quality Score: 0.82 / 1.0 (CONDITIONAL PASS ⚠️)

Metrics Breakdown:
✅ Depth Coverage: 4/6 levels (67%) - L1-L4 present
✅ RACI Coverage: 12/15 L2 nodes (80%) - Meets standard
⚠️  If-Then Coverage: 1 action - BELOW target (need 2+)
✅ Task Count: 120 tasks - Meets L1-L6 standard (100+)
⚠️  Risk Analysis: 4 risks - BELOW target (need 5-8)
✅ Timeline Specificity: All dates specific

Issues Found:
❌ Missing L5 and L6 levels (stopped at L4)
❌ Only 1 If-Then contingency (need 2+)
❌ Only 4 risks identified (need 5-8)

Recommendations:
1. Extend plan to include L5 (tasks) and L6 (atomic actions)
2. Add 1+ If-Then contingency for high-severity risks
3. Identify 1-4 additional risks or consolidate existing

Quality Check Action:
[I]mprove Output - Fix issues before proceeding
[A]ccept as-is - Continue with quality risk acknowledged
[R]efer to examples - Show WRONG vs RIGHT examples
[C]ontinue - Quality standards met (PASS only)

➡️ Your choice: [I/A/R/C]
```

---

## Common Quality Issues & Fixes

### Issue 1: Stopping at L2-L3 (Insufficient Depth)

**SYMPTOM:**
```markdown
L1: Technical Advisor
  L2: Code Review
  L2: Architecture Guidance
[Plan ends here - only 2 levels]
```

**FIX:**
```markdown
Extend to L3-L6:

L1: Technical Advisor
  L2: Code Review
    L3: Backend Code Review
      L4: Initial Review (Week 1)
        L5: Review authentication module
          L6: Check password hashing implementation
          L6: Verify session management logic
        L5: Review database queries
          L6: Analyze query performance
          L6: Check for SQL injection risks
      L4: Follow-up Review (Week 2)
        [... continue with L5-L6 ...]
```

---

### Issue 2: Vague Timelines

**SYMPTOM:**
```markdown
L4: Soon
L4: Later this month
L4: Eventually
L4: When ready
```

**FIX:**
```markdown
L4: Week 1 (Jan 15-19, 2025)
L4: Week 2-3 (Jan 22 - Feb 2, 2025)
L4: Month 2 (Feb 5-28, 2025)
L4: Q2 2025 (Apr-Jun)
```

---

### Issue 3: Insufficient Task Breakdown

**SYMPTOM:**
```markdown
L5: Do the work
L5: Review everything
L5: Complete project
[Only 3 tasks for entire project]
```

**FIX:**
```markdown
Expand into specific, actionable tasks:

L5: Research authentication patterns (2 hours)
L5: Draft security requirements document (3 hours)
L5: Design session architecture diagram (2 hours)
L5: Document token lifecycle flow (1 hour)
L5: Create API contract specifications (3 hours)
L5: Review OAuth 2.0 integration options (2 hours)
L5: Implement JWT token generation (4 hours)
L5: Write unit tests for auth module (3 hours)
[... 92+ more tasks to reach 100+ minimum ...]
```

---

### Issue 4: Missing Dependency Mapping

**SYMPTOM:**
```markdown
L4: Design database schema
L4: Implement API endpoints
L4: Write tests
[No indication which must happen first]
```

**FIX:**
```markdown
L4: Design database schema (Week 1) [CRITICAL PATH]
  Dependencies: None (can start immediately)

L4: Implement API endpoints (Week 2-3) [CRITICAL PATH]
  Dependencies: Database schema must be complete

L4: Write tests (Week 3-4)
  Dependencies: API endpoints partially implemented
  Can run in parallel with API completion
```

---

### Issue 5: Weak Risk Analysis

**SYMPTOM:**
```markdown
Risks:
- Something might go wrong
- Project could be delayed
```

**FIX:**
```markdown
Risk Analysis (5-8 risks minimum):

1. **Authentication Security Vulnerability**
   - Severity: HIGH
   - Impact: Data breach, user accounts compromised
   - Probability: MEDIUM (if best practices not followed)
   - Contingency: Security audit in Week 2, penetration testing before launch

2. **Database Performance Bottleneck**
   - Severity: MEDIUM
   - Impact: Slow API responses, poor UX
   - Probability: LOW (with proper indexing)
   - Contingency: Load testing in Week 3, caching layer if needed

3. **Third-Party OAuth Provider Downtime**
   - Severity: MEDIUM
   - Impact: Users can't log in during outage
   - Probability: LOW (99.9% SLA)
   - Contingency: Fallback to local auth, status page monitoring

[... 2-5 more detailed risks ...]
```

---

### Issue 6: Missing RACI Assignments

**SYMPTOM:**
```markdown
L2: Code Review
L2: Architecture Guidance
L2: Performance Optimization
[No RACI roles assigned]
```

**FIX:**
```markdown
L2: Code Review
  - Responsible: Senior Engineer (me)
  - Accountable: Tech Lead
  - Consulted: Backend team
  - Informed: Product Manager

L2: Architecture Guidance
  - Responsible: Tech Lead (me)
  - Accountable: CTO
  - Consulted: Senior Engineers
  - Informed: Engineering team

L2: Performance Optimization
  - Responsible: Performance Engineer (me)
  - Accountable: Tech Lead
  - Consulted: DevOps team
  - Informed: Product team

RACI Coverage: 3/3 L2 nodes (100%) ✅
```

---

## Detailed Review Checkpoint

**After quality validation passes, run detailed review:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔍 DETAILED PLAN REVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Deep Plan Generated:
- Depth: L1 through L6 ✅
- Total nodes: 660 nodes ✅
- Scenario: Tech Expert template
- Auto-linked: NPV milestones → L2 phases

Plan Preview:
L1: Technical Advisor
  L2: Code Review & Quality (12 RACI, 3 If-Then)
    L3: Backend Code Review
      L4: Initial Review (Week 1)
        L5: Review auth module (8 tasks)
        L5: Review DB queries (6 tasks)
      L4: Follow-up Review (Week 2)
    L3: Frontend Code Review
    L3: Security Review
  L2: Architecture Guidance (15 RACI, 2 If-Then)
  L2: Performance Optimization (8 RACI, 1 If-Then)

Quality Check:
☑ Plan structure reflects contribution approach?
☑ All contribution areas (L2) clearly defined?
☑ Depth appropriate (L1-L6 for Deep Track)?
☑ RACI assignments clear for key nodes?
☑ If-Then contingencies make sense?
☑ Anything missing or unclear?

Does this deep plan meet expectations?

[Y]es - Plan is good, proceed
[N]o - Needs improvement, let me revise
[E]xplain - Show me what each level means

➡️ Your choice: [Y/N/E]
```

---

## Quality Gate Pass/Fail Actions

### IF PASS (Quality Score ≥0.85):

```
✅ QUALITY GATE PASSED

Your deep plan meets all minimum standards:
- Full depth coverage (L1-L6)
- Sufficient task breakdown (100+ tasks)
- RACI coverage (≥70%)
- Risk analysis (5-8 risks)
- Contingencies defined (2+ If-Then)

Proceeding to menu options...
```

### IF CONDITIONAL PASS (Quality Score 0.70-0.84):

```
⚠️ QUALITY GATE: CONDITIONAL PASS

Your deep plan meets most standards but has minor gaps:
- Missing: 1-2 If-Then contingencies
- Timeline: Some dates could be more specific

You can proceed, but plan may lack detail for execution.

[I]mprove now (recommended)
[P]roceed anyway (quality risk acknowledged)

➡️ Your choice: [I/P]
```

### IF FAIL (Quality Score <0.70):

```
❌ QUALITY GATE FAILED

Your deep plan does not meet minimum standards:
- Missing levels: L5, L6 not present
- Task count: 45 tasks (need 100+)
- Risk analysis: 2 risks (need 5-8)

CANNOT proceed until quality standards met.

[I]mprove plan now (required)
[S]how examples (WRONG vs RIGHT)

➡️ Your choice: [I/S]
```

---

## Integration with Validation Examples

**Reference:** `validation-examples.md` contains WRONG vs RIGHT examples

**When to show examples:**

1. User selects [R]efer to examples in quality check
2. Quality gate fails and user needs guidance
3. User asks "What does good look like?"

**Example display:**

```
📖 REFERENCE: validation-examples.md

Example: L1-L6 Depth (WRONG vs RIGHT)

❌ WRONG: Stopping at L2-L3
```markdown
L1: Technical Advisor
L2: Code Review
L2: Architecture Guidance
[Plan ends - only 2 levels]
```

✅ RIGHT: Full L1-L6 depth
```markdown
L1: Technical Advisor
  L2: Code Review
    L3: Backend Review
      L4: Week 1 Review
        L5: Review auth module
          L6: Check password hashing
          L6: Verify sessions
[... continues through all 6 levels ...]
```

[Show more examples] [Return to quality check]
```

---

## Storage & Learning

**Save quality scores to memory for improvement:**

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "quality-gates:deep-plan:{project_id}:{timestamp}" \
  --content "{
    \"project_id\": \"proj-123\",
    \"track\": \"deep\",
    \"depth_selected\": \"L1-L6\",
    \"quality_score\": 0.82,
    \"pass_status\": \"conditional_pass\",
    \"issues\": [\"missing_l5_l6\", \"low_if_then_coverage\"],
    \"improvements_made\": true,
    \"final_quality_score\": 0.91,
    \"timestamp\": \"2025-01-15T10:45:00Z\"
  }"
```

**Retrieve for future learning:**

```bash
# Check quality trends across projects
npx claude-flow@v3alpha memory search -q "quality-gates deep-plan pass"

# Learn from high-quality plans
# e.g., "Last 3 deep plans scored 0.9+, reuse structure"
```
