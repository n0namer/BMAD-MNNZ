# Project Stage Discovery - Detailed Examples & Reference

## Real-World Stage Examples

### Example 1: Katana (Game Development)
**Lifecycle Stage:** D - MVP Launched
**Overall Completion:** 65%

**What Exists:**
- Phases 1-4 complete and working
- Epic L in active development (50% done)
- Player base exists, collecting feedback
- Core game mechanics validated

**Timeline Impact:**
- Greenfield estimate: 24 weeks
- Adjusted timeline: 8.4 weeks (35% of greenfield)
- Time saved: 15.6 weeks

**Key Insight:** NOT starting from scratch - significant infrastructure already exists.

---

### Example 2: Beauty Franchise
**Lifecycle Stage:** E - Production (Scaling)
**Overall Completion:** 50%

**What Exists:**
- Pilot studio operational
- 40-50% of business assets ready
- Customer base established
- Marketing materials created
- Operations processes documented

**Timeline Impact:**
- Greenfield estimate: 52 weeks
- Adjusted timeline: 26 weeks (50% of greenfield)
- Time saved: 26 weeks

**Key Insight:** Pilot proven, now focusing on replication and scale.

---

### Example 3: AI Autoresponder (Greenfield)
**Lifecycle Stage:** A - Idea Only
**Overall Completion:** 5%

**What Exists:**
- Concept documentation
- Market research
- Nothing built

**Timeline Impact:**
- Greenfield estimate: 12 weeks
- Adjusted timeline: 11.4 weeks (95% of greenfield)
- Time saved: 0.6 weeks

**Key Insight:** True greenfield - plan accordingly.

---

## Stage Lifecycle Descriptions

### Stage A: Idea Only (0-10% Complete)
**Characteristics:**
- No code, prototypes, or users
- Concept exists in documentation/mind
- Pure planning phase
- No validation yet

**Typical Blockers:**
- Lack of technical skills
- Uncertain market fit
- No resources allocated

**Timeline Multiplier:** 1.0x (full greenfield time)

---

### Stage B: Prototype/POC (10-25% Complete)
**Characteristics:**
- Proof-of-concept exists
- Works locally/in controlled environment
- No users, but functionality validated
- Core hypothesis tested

**Typical Blockers:**
- Scaling challenges unknown
- No production infrastructure
- Limited validation

**Timeline Multiplier:** 0.75-0.90x

---

### Stage C: MVP in Development (25-50% Complete)
**Characteristics:**
- Partial functionality complete
- Some modules working, others in progress
- Architecture defined
- No users yet

**Typical Blockers:**
- Integration challenges
- Resource constraints
- Scope creep

**Timeline Multiplier:** 0.50-0.75x

---

### Stage D: MVP Launched (50-70% Complete)
**Characteristics:**
- Product available to users
- Feedback collection active
- Core features working
- Early metrics available

**Typical Blockers:**
- Feature gaps identified
- Performance issues
- User acquisition challenges

**Timeline Multiplier:** 0.30-0.50x

---

### Stage E: Production/Scaling (70-90% Complete)
**Characteristics:**
- Stable product version
- Paying customers
- Focus on growth
- Established processes

**Typical Blockers:**
- Scaling bottlenecks
- Competition
- Team growth pains

**Timeline Multiplier:** 0.10-0.30x

---

### Stage F: Mature Product (90-100% Complete)
**Characteristics:**
- Established product with history
- Large user base
- Focus on optimization/evolution
- New feature development

**Typical Blockers:**
- Technical debt
- Market saturation
- Innovation challenges

**Timeline Multiplier:** 0.05-0.10x

---

## Completion Percentage Calculation

### Formula
```
Overall % = (Technical% + Product% + Market% + Operations%) / 4
```

### Detailed Breakdown

#### Technical Dimension
- **Code base:** 30% weight
- **Infrastructure:** 25% weight
- **Integrations:** 20% weight
- **DevOps/CI/CD:** 15% weight
- **Database schema:** 10% weight

**Calculation Example:**
```
Code: 60% complete
Infrastructure: 40% complete
Integrations: 20% complete
DevOps: 50% complete
Database: 80% complete

Technical% = (60×0.30 + 40×0.25 + 20×0.20 + 50×0.15 + 80×0.10)
           = 18 + 10 + 4 + 7.5 + 8
           = 47.5%
```

#### Product Dimension
- **Functionality:** 40% weight
- **UI/UX:** 30% weight
- **Documentation:** 20% weight
- **Testing:** 10% weight

#### Market Dimension
- **Users:** 40% weight
- **Metrics/Analytics:** 30% weight
- **Marketing assets:** 20% weight
- **Customer feedback:** 10% weight

#### Operations Dimension
- **Team:** 40% weight
- **Processes:** 30% weight
- **Tools:** 20% weight
- **Documentation:** 10% weight

---

## Walkthrough Example: Beauty Franchise

### User Responses

**Q1: Project Stage?**
Answer: D - MVP Launched (pilot studio operating)

**Q2: What Exists?**
- ✅ Pilot studio (location, equipment, staff)
- ✅ Service menu defined
- ✅ Pricing structure
- ✅ Marketing materials (social media, website)
- ✅ Operations manual (40% complete)
- ✅ Customer base (150 active clients)
- ❌ No franchise package
- ❌ No replication playbook
- ❌ No franchise legal structure

**Q3: Blockers?**
- Primary: How to replicate without losing quality
- Secondary: No standardized training materials
- Tertiary: Unclear franchise pricing model

### Calculation

**Technical (Operations):** 50%
- Processes: 60% (manual exists but incomplete)
- Tools: 40% (booking system works, but not scalable)
- Infrastructure: 50% (pilot location only)

**Product (Service):** 70%
- Service delivery: 90% (validated at pilot)
- Customer experience: 80% (high satisfaction)
- Service menu: 60% (needs standardization)

**Market:** 40%
- Users: 60% (150 clients, good retention)
- Metrics: 30% (basic tracking only)
- Marketing: 40% (local only, not scalable)

**Operations:** 45%
- Team: 50% (pilot team trained, but no franchise training)
- Processes: 60% (operations manual partial)
- Documentation: 25% (not franchise-ready)

**Overall Completion:**
```
(50 + 70 + 40 + 45) / 4 = 51.25% ≈ 50%
```

### Timeline Adjustment

**Greenfield Estimate:** 52 weeks (build entire franchise from scratch)

**Adjusted Timeline:**
```
52 weeks × (100 - 50)% = 52 × 0.50 = 26 weeks
```

**Time Saved:** 26 weeks (because pilot already validates concept and operations)

**Focus Areas (50% remaining):**
- Franchise package creation (legal, contracts)
- Replication playbook
- Franchise training program
- Scalable marketing system
- Multi-location operations tools

---

## Common Mistakes to Avoid

### ❌ Mistake 1: Greenfield Fallacy
**Problem:** Assuming every project starts from 0%

**Example:**
- User: "I have a pilot studio running"
- Wrong approach: Plan 52 weeks for entire franchise
- Right approach: Calculate what's done (50%), plan 26 weeks for remaining 50%

### ❌ Mistake 2: Not Counting "Incomplete" Work
**Problem:** Ignoring partially complete components

**Example:**
- Operations manual 40% complete
- Wrong: Count as 0%
- Right: Count as 40% (saves 40% of time on that component)

### ❌ Mistake 3: Overweighting One Dimension
**Problem:** Focusing only on code completion

**Example:**
- Code 80% done, but no users, no marketing, no team
- Wrong: Project 80% complete
- Right: Project ~20% complete (only 1 of 4 dimensions done)

### ❌ Mistake 4: Not Documenting Blockers
**Problem:** Timeline doesn't account for known obstacles

**Example:**
- "We need to hire 3 developers before starting Phase 2"
- Wrong: Ignore and plan continuous timeline
- Right: Add blocker resolution time to timeline

---

## Quick Stage Assessment Shortcuts

### If User Says...
| Statement | Likely Stage | Completion Range |
|-----------|--------------|------------------|
| "I have an idea" | A | 0-10% |
| "I built a prototype" | B | 10-25% |
| "Some features work" | C | 25-50% |
| "We have X users" | D+ | 50%+ |
| "We have paying customers" | E+ | 70%+ |
| "We're optimizing for scale" | E-F | 80%+ |

### Quick Checklist for Stage D+
If project is Stage D or higher, verify:
- ✅ Users exist (how many?)
- ✅ Metrics tracked (what KPIs?)
- ✅ Feedback loop exists
- ✅ Infrastructure handles load
- ✅ Team can support users

### Quick Blockers Triage
| Blocker Type | Impact on Timeline | Priority |
|--------------|-------------------|----------|
| Technical debt | +20-50% time | High |
| Missing competencies | +30-100% time | Critical |
| Unclear requirements | +50-200% time | Critical |
| Resource constraints | Variable | Medium-High |
| Market uncertainty | Pivot risk | Medium |

---

## Advanced: Multi-Project Scenarios

### Scenario: Platform with Multiple Products

**Challenge:** Each product at different stage

**Solution:** Assess each independently, then aggregate

**Example:**
- Product A: 80% complete (mature)
- Product B: 30% complete (MVP dev)
- Product C: 5% complete (idea)
- Platform infrastructure: 60% complete

**Aggregate Assessment:**
```
Overall = (80 + 30 + 5 + 60) / 4 = 43.75% ≈ 44%
```

**Timeline Strategy:**
- Finish Product A first (20% remaining)
- Leverage A's infrastructure for B and C
- Adjusted timeline: 44% of greenfield for all products

---

## References for Step 08 Integration

### Data Points to Pass Forward

1. **Overall Completion %** → Timeline multiplier
2. **Dimension Breakdown** → Resource allocation
3. **Primary Blocker** → Risk mitigation planning
4. **What Works** → Assets to leverage
5. **Stage** → Phase mapping

### Timeline Adjustment Formula (for Step 08)

```
Adjusted Timeline = Greenfield Estimate × (100 - Completion%) / 100
```

**Constraints:**
- Minimum timeline: 2 weeks (even if 95% complete)
- Maximum adjustment: 90% reduction (10% minimum time needed)

### Example Integration

**From Step 0.5:**
- Overall Completion: 65%
- Timeline Multiplier: 0.35 (35% of greenfield)

**In Step 08:**
- Greenfield estimate: 24 weeks
- Adjusted timeline: 24 × 0.35 = 8.4 weeks
- Resource allocation: Focus 65% of effort on remaining 35% of work
