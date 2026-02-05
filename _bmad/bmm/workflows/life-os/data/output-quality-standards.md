---
name: 'output-quality-standards'
purpose: 'Define minimum acceptable output quality per track'
version: '1.0'
last_updated: '2026-02-05'
---

# Output Quality Standards Per Track

## Purpose

This document defines **measurable quality standards** for outputs from each Life OS track (Quick, Standard, Deep). These standards ensure consistent quality regardless of which track is chosen, while respecting the time investment differences.

**Key Principle:** Higher tracks = more depth, not necessarily better decisions. Quick can be excellent if criteria are met.

---

## Quick Track Standards

### Minimum Requirements

| Element | Required | Measurement |
|---------|----------|-------------|
| **Scorecard** | Yes | 10-15 lines minimum |
| **Go/NoGo Decision** | Yes | Clear binary recommendation |
| **Risk Assessment** | Yes | 2-3 critical risks identified |
| **Time Estimate** | Yes | Implementation timeline |
| **Resource Check** | Yes | What's needed vs available |
| **Next Step** | Yes | Immediate actionable next step |

### Required Sections

```markdown
## Quick Assessment: [Idea Name]

### Scorecard (10-15 lines)
- Alignment Score: X/10
- Feasibility Score: X/10
- Impact Score: X/10
- Resource Availability: X/10
- Overall: X/40

### Go/NoGo Decision
**Decision:** [GO / NO-GO / DEFER]
**Reasoning:** [2-3 sentence justification]

### Critical Risks (2-3)
1. [Risk name]: [Impact] - [Mitigation]
2. [Risk name]: [Impact] - [Mitigation]
3. [Risk name]: [Impact] - [Mitigation]

### Time Estimate
- Implementation: [X weeks/months]
- First value: [X weeks from start]

### Resources Required
- [Resource 1]: [Have/Need]
- [Resource 2]: [Have/Need]
- [Resource 3]: [Have/Need]

### Next Step
[One clear, actionable step to take next]
```

### Quality Checklist

- [ ] Scorecard has all 4+ dimensions scored
- [ ] Decision is binary and justified
- [ ] Risks are specific (not generic like "might fail")
- [ ] Time estimate includes both implementation and first value
- [ ] Resource check includes availability status
- [ ] Next step is actionable (not "research more")
- [ ] Total length: 100-200 lines
- [ ] Can be completed in 5-10 minutes

### Examples

**✅ GOOD Quick Output:**

```markdown
## Quick Assessment: Mobile App for Task Management

### Scorecard
- Alignment Score: 8/10 (strong fit with productivity goals)
- Feasibility Score: 6/10 (requires React Native skills)
- Impact Score: 7/10 (daily use, high frequency)
- Resource Availability: 5/10 (time limited, no budget)
- Overall: 26/40

### Go/NoGo Decision
**Decision:** DEFER
**Reasoning:** Strong alignment and impact, but feasibility concerns (no React Native experience) and resource constraints (no dev time for 3 months) make this a Q2 2026 candidate, not immediate.

### Critical Risks
1. Skill Gap: No React Native experience - Mitigation: 40-hour online course first
2. Time Availability: Only 5h/week free - Mitigation: Defer to Q2 when project ends
3. Market Saturation: 1000+ competitors - Mitigation: Unique niche (ADHD-friendly design)

### Time Estimate
- Implementation: 12 weeks (assuming 10h/week)
- First value: 4 weeks (MVP with core features)

### Resources Required
- Time: Need 10h/week, have 5h/week
- Skills: Need React Native, have JavaScript
- Budget: $0 needed (free tools)

### Next Step
Enroll in "React Native for Beginners" course (40 hours) and revisit in March 2026.
```

**❌ BAD Quick Output:**

```markdown
## Quick Assessment: Mobile App

### Scorecard
- Good idea: Yes
- Can do: Maybe
- Worth it: Probably

### Decision
Seems interesting, might work.

### Risks
- Might fail
- Could be hard
- Not sure

### Next Step
Think about it more.
```

**Why BAD:**
- No numeric scores
- No clear Go/NoGo decision
- Risks are vague and generic
- No time estimate or resource check
- Next step is not actionable
- Length: ~50 lines (too short)

---

## Standard Track Standards

### Minimum Requirements

| Element | Required | Measurement |
|---------|----------|-------------|
| **Workflow Plan** | Yes | 50-100 lines minimum |
| **Scorecard** | Yes | 6+ dimensions scored |
| **Integration Plan** | Yes | How fits with existing work |
| **Calendar Mapping** | Yes | When will work happen |
| **Success Metrics** | Yes | How to measure progress |
| **Risk Analysis** | Yes | 5+ risks with mitigations |
| **Decision Documentation** | Yes | Clear recommendation with rationale |

### Required Sections

```markdown
## Standard Analysis: [Idea Name]

### Scorecard (6+ dimensions)
- Alignment: X/10
- Feasibility: X/10
- Impact: X/10
- Resource Availability: X/10
- Strategic Fit: X/10
- Risk Level: X/10
- Overall: X/60

### Workflow Plan (50-100 lines)
#### Phase 1: [Name] (~X weeks)
- [ ] Task 1
- [ ] Task 2
- [ ] Task 3

#### Phase 2: [Name] (~X weeks)
- [ ] Task 1
- [ ] Task 2

[etc.]

### Integration Plan
- **Existing Work:** [How this fits with current projects]
- **Calendar Impact:** [When/where this work happens]
- **Resource Sharing:** [Shared resources with other work]
- **Synergies:** [How this enhances other projects]
- **Conflicts:** [Potential clashes to manage]

### Success Metrics
- **Leading Indicators:** [Early signals of progress]
- **Lagging Indicators:** [Final outcome measures]
- **Milestones:** [Key checkpoints]
- **Review Cadence:** [How often to check progress]

### Risk Analysis (5+ risks)
| Risk | Probability | Impact | Mitigation | Owner |
|------|-------------|--------|------------|-------|
| [Risk 1] | High/Med/Low | High/Med/Low | [Strategy] | [Who] |
| [Risk 2] | High/Med/Low | High/Med/Low | [Strategy] | [Who] |
[5+ rows]

### Decision & Recommendation
**Decision:** [GO / NO-GO / DEFER / PILOT]
**Confidence:** X/10
**Reasoning:** [3-5 sentence justification]
**Conditions:** [Any conditions for GO decision]

### Next Steps (Immediate)
1. [Step 1] - by [date]
2. [Step 2] - by [date]
3. [Step 3] - by [date]
```

### Quality Checklist

- [ ] Scorecard has 6+ dimensions scored numerically
- [ ] Workflow plan has 3+ phases with tasks
- [ ] Integration plan addresses calendar conflicts
- [ ] Success metrics include leading AND lagging indicators
- [ ] Risk analysis has 5+ specific risks with probability/impact
- [ ] Decision is clear with confidence score
- [ ] Next steps have specific dates/owners
- [ ] Total length: 300-500 lines
- [ ] Can be completed in 30-60 minutes

### Examples

**✅ GOOD Standard Output:**

```markdown
## Standard Analysis: Automated Content Pipeline

### Scorecard
- Alignment: 9/10 (core strategic goal)
- Feasibility: 7/10 (technical challenges but solvable)
- Impact: 8/10 (saves 15h/week)
- Resource Availability: 6/10 (time limited, budget OK)
- Strategic Fit: 9/10 (enables other projects)
- Risk Level: 5/10 (moderate technical risk)
- Overall: 44/60

### Workflow Plan (~8 weeks)

#### Phase 1: Research & Design (2 weeks)
- [ ] Audit current content creation process (3h)
- [ ] Identify automation opportunities (2h)
- [ ] Select tools (Claude API, Make.com, Airtable) (4h)
- [ ] Design architecture diagram (3h)
- [ ] Prototype first workflow (8h)
- **Deliverable:** Architecture doc + working prototype

#### Phase 2: Core Pipeline (3 weeks)
- [ ] Set up Airtable content database (4h)
- [ ] Build Make.com automation flows (12h)
- [ ] Integrate Claude API for generation (8h)
- [ ] Add error handling and logging (6h)
- [ ] Create content templates (4h)
- **Deliverable:** Working pipeline for 1 content type

#### Phase 3: Testing & Refinement (2 weeks)
- [ ] Run 10 test articles through pipeline (10h)
- [ ] Measure quality vs manual (4h)
- [ ] Optimize prompts based on results (6h)
- [ ] Add quality checks (6h)
- [ ] Document usage guide (4h)
- **Deliverable:** Production-ready pipeline + docs

#### Phase 4: Scale & Monitor (1 week)
- [ ] Add 3 more content types (6h)
- [ ] Set up monitoring dashboard (4h)
- [ ] Train team on usage (3h)
- [ ] Establish review process (2h)
- **Deliverable:** Full pipeline + training

### Integration Plan

**Existing Work:**
- Replaces manual content creation (currently 15h/week)
- Enables new SEO project (dependent on content volume)
- Supports social media strategy (cross-posts content)

**Calendar Impact:**
- Build time: Tuesdays/Thursdays 6-9pm (6h/week)
- Frees up: Mondays 9am-12pm, Wednesdays 2-5pm (6h/week)
- Net gain after 8 weeks: +9h/week

**Resource Sharing:**
- Uses same Airtable base as CRM project (synergy)
- Claude API budget shared with other automation (watch quota)
- Make.com plan has capacity for 10K ops/month

**Synergies:**
- Content pipeline feeds SEO project
- Learnings apply to email automation project
- Airtable skills transfer to other projects

**Conflicts:**
- Tuesday nights overlap with family time (need to negotiate)
- Claude API quota shared - may need upgrade if both projects scale

### Success Metrics

**Leading Indicators:**
- Pipeline runs successfully: 95%+ success rate
- Time per article: <30 minutes (vs 2h manual)
- Quality score: 7+/10 (team review)

**Lagging Indicators:**
- Content output: 20 articles/month (vs 8 currently)
- Time saved: 12h/week measured after 1 month
- ROI: Break even on tool costs within 3 months

**Milestones:**
- Week 2: Prototype working
- Week 5: First article published via pipeline
- Week 8: Full pipeline live
- Week 12: 150% increase in content output

**Review Cadence:**
- Daily: Check pipeline runs (2 min)
- Weekly: Review quality metrics (15 min)
- Monthly: ROI and optimization review (1h)

### Risk Analysis

| Risk | Probability | Impact | Mitigation | Owner |
|------|-------------|--------|------------|-------|
| Claude API quality varies | High | Medium | Build quality checks, maintain human review | Me |
| Tool costs exceed budget | Medium | Low | Start with free tiers, scale gradually | Me |
| Team rejects automated content | Medium | High | Involve team early, maintain quality bar | Team Lead |
| Integration breaks with updates | Medium | Medium | Version lock APIs, monitor changelogs | Me |
| Time investment exceeds estimate | High | Medium | Time-box phases, cut scope if needed | Me |
| Content quality below standards | Medium | High | A/B test vs manual, iterate prompts | Content Lead |

### Decision & Recommendation

**Decision:** GO (with pilot)
**Confidence:** 8/10
**Reasoning:** High strategic value (enables SEO project), strong ROI (saves 12h/week), feasible with current resources. Risks are manageable through incremental approach. Starting with pilot (1 content type) reduces risk while proving value.

**Conditions:**
1. Start with ONE content type only (blog posts)
2. Maintain human review for first 3 months
3. Pause if quality drops below 7/10 for 2 weeks
4. Re-evaluate after pilot (Week 5)

### Next Steps

1. **This Week:** Set up Airtable base and test Make.com account - by Friday
2. **Next Week:** Build first automation prototype - by Feb 14
3. **Week 3:** Present pilot results to team - by Feb 21
```

**❌ BAD Standard Output:**

```markdown
## Standard Analysis: Content Pipeline

### Scorecard
- Good: 8/10
- Doable: 7/10
- Overall: 15/20

### Plan
1. Research tools
2. Build automation
3. Test it
4. Launch

### Risks
- Might not work
- Could be expensive
- Team might not like it
- Technical issues
- Time issues

### Decision
GO - seems like a good idea.

### Next Steps
Start researching tools and building.
```

**Why BAD:**
- Scorecard missing key dimensions (Resource Availability, Strategic Fit)
- Workflow plan has no phases, tasks, or time estimates
- No integration plan (calendar, resource sharing, conflicts)
- No success metrics or review cadence
- Risks are generic with no mitigation or owner
- Decision lacks confidence score and conditions
- Next steps have no dates or specifics
- Length: ~150 lines (too short for Standard)

---

## Deep Track Standards

### Minimum Requirements

| Element | Required | Measurement |
|---------|----------|-------------|
| **Comprehensive Plan** | Yes | 200+ lines minimum |
| **L1-L6 Breakdown** | Yes | All 6 levels documented |
| **TRIZ Analysis** | Conditional | If contradictions detected |
| **Templates Created** | Yes | Reusable artifacts (3+ templates) |
| **Integration Analysis** | Yes | Calendar, resources, dependencies |
| **Risk Management** | Yes | 10+ risks with detailed mitigations |
| **Success Framework** | Yes | Metrics, KPIs, review process |
| **Implementation Guide** | Yes | Step-by-step execution plan |

### Required Sections

```markdown
## Deep Plan: [Idea Name]

### Executive Summary
- **Decision:** [GO/NO-GO/DEFER/PILOT]
- **Confidence:** X/10
- **Investment:** [Time/Money/Resources]
- **Expected Return:** [Quantified value]
- **Timeline:** [Start - End]
- **Critical Success Factors:** [3-5 factors]

### Scorecard (8+ dimensions)
- Alignment: X/10
- Feasibility: X/10
- Impact: X/10
- Resource Availability: X/10
- Strategic Fit: X/10
- Risk Level: X/10
- Innovation Potential: X/10
- Scalability: X/10
- Overall: X/80

### L1-L6 Breakdown (200+ lines)

#### L1: Vision & Strategy
- **Vision:** [What does success look like in 1 year?]
- **Strategic Context:** [Why now? Why this?]
- **Alignment:** [How fits with life/career goals]
- **Success Definition:** [Measurable outcomes]

#### L2: Epics (3-6 major themes)
1. **Epic:** [Name]
   - Scope: [What's included]
   - Value: [Why this epic matters]
   - Dependencies: [What's needed first]
   - Timeline: [Weeks X-Y]

[Repeat for each epic]

#### L3: Features (12-20 capabilities)
[Each feature from each epic, with description and acceptance criteria]

#### L4: User Stories (40-80 stories)
[Grouped by epic/feature, in user story format]

#### L5: Tasks (150-300 tasks)
[Actionable tasks with owners and estimates]

#### L6: Sub-tasks (300-600 items)
[Detailed implementation steps]

### TRIZ Analysis (if contradictions exist)
- **Contradiction Identified:** [Description]
- **Conflicting Parameters:** [X vs Y]
- **Inventive Principles Applied:** [Principle names]
- **Resolution Strategy:** [How contradiction resolved]
- **Novel Approach:** [What makes this innovative]

### Templates Created (3+ artifacts)

#### Template 1: [Name]
[Full template with instructions]

#### Template 2: [Name]
[Full template with instructions]

#### Template 3: [Name]
[Full template with instructions]

### Comprehensive Integration Analysis

#### Calendar Mapping
- **Weekly Time Required:** [Hours by day]
- **Peak Periods:** [When intensity is highest]
- **Conflicts:** [Overlaps with existing commitments]
- **Adjustments:** [What needs to move]

#### Resource Planning
- **Budget:** [Detailed cost breakdown]
- **Tools:** [Software/services needed]
- **Skills:** [Competencies required vs available]
- **Support:** [People/expertise needed]

#### Dependency Analysis
- **Prerequisites:** [What must be done first]
- **Parallel Tracks:** [What can run concurrently]
- **Blockers:** [Known obstacles]
- **Critical Path:** [Longest dependent chain]

### Risk Management (10+ risks)

| Risk | Prob | Impact | Trigger | Mitigation | Contingency | Owner |
|------|------|--------|---------|------------|-------------|-------|
| [Risk 1] | H/M/L | H/M/L | [Early warning] | [Prevention] | [Response] | [Who] |
[10+ rows with detailed strategies]

### Success Framework

#### KPIs & Metrics
- **Input Metrics:** [What we control]
- **Output Metrics:** [What we produce]
- **Outcome Metrics:** [What changes]
- **Leading Indicators:** [Early signals]
- **Lagging Indicators:** [Final results]

#### Review Process
- **Daily:** [Quick checks, 5 min]
- **Weekly:** [Progress review, 30 min]
- **Monthly:** [Deep dive, 2h]
- **Quarterly:** [Strategic review, 4h]

#### Decision Gates
- **Gate 1:** [Criteria and timing]
- **Gate 2:** [Criteria and timing]
- **Gate 3:** [Criteria and timing]

### Implementation Guide

#### Phase-by-Phase Breakdown
[Detailed phases with tasks, owners, dates, deliverables]

#### Rollout Strategy
- **Pilot Approach:** [How to test first]
- **Scale Plan:** [How to expand]
- **Communication:** [How to inform stakeholders]

#### Monitoring & Adaptation
- **Dashboard:** [What to track visually]
- **Alerts:** [When to intervene]
- **Adjustment Triggers:** [When to pivot]

### Appendices
- Detailed calculations
- Research findings
- Stakeholder analysis
- Market/competitive analysis
- Technical specifications
```

### Quality Checklist

- [ ] Executive summary provides complete overview
- [ ] Scorecard has 8+ dimensions scored
- [ ] L1-L6 breakdown totals 200+ lines
- [ ] L6 has 300+ sub-tasks (detailed enough to execute)
- [ ] TRIZ applied if contradictions exist
- [ ] 3+ reusable templates created
- [ ] Calendar mapping includes weekly breakdown
- [ ] Resource planning has detailed budget
- [ ] 10+ risks with full mitigation/contingency plans
- [ ] Success framework includes all review levels
- [ ] Implementation guide is actionable step-by-step
- [ ] Total length: 800-1500+ lines
- [ ] Can be completed in 2-4 hours

### Examples

**✅ GOOD Deep Output:**

```markdown
## Deep Plan: Build AI-Powered Personal CRM

### Executive Summary

**Decision:** GO (with phased rollout)
**Confidence:** 9/10
**Investment:** 240 hours over 16 weeks, $500 tools budget
**Expected Return:** Save 8h/week on relationship management, 3x follow-up rate
**Timeline:** Feb 5 - May 28, 2026
**Critical Success Factors:**
1. Integration with existing tools (email, calendar, notes)
2. Adoption by user (overcome habit of manual tracking)
3. Data privacy maintained (no cloud exposure of sensitive contacts)
4. Quality of AI recommendations (must be >80% relevant)
5. Sustain after initial build (ongoing maintenance <2h/month)

### Scorecard

- Alignment: 9/10 (core to relationship-building life goal)
- Feasibility: 7/10 (technical challenges but clear path)
- Impact: 9/10 (daily use, high value)
- Resource Availability: 6/10 (time tight, budget OK)
- Strategic Fit: 10/10 (enables consulting business growth)
- Risk Level: 6/10 (moderate technical + adoption risk)
- Innovation Potential: 8/10 (novel approach to CRM)
- Scalability: 7/10 (can grow with contact base)
- Overall: 62/80

### L1-L6 Breakdown

#### L1: Vision & Strategy

**Vision:** By June 2026, I never miss a follow-up, remember context about every contact, and nurture relationships proactively without manual effort. The system becomes my "second brain" for relationships.

**Strategic Context:**
- **Why Now:** Consulting business growing, contacts increasing 30%/quarter, manual system failing
- **Why This:** Existing CRMs too sales-focused, not relationship-focused. Need ADHD-friendly, low-friction system.
- **Market Gap:** No tool combines contact management + AI context + privacy + ADHD design

**Alignment:**
- Life Goal: Build meaningful professional relationships
- Career Goal: Grow consulting to $200K/year (needs strong network)
- Skills Goal: Master AI integration (transferable skill)

**Success Definition:**
- **Quantified:** Follow-up rate increases from 25% to 75%
- **Behavioral:** Check system daily (habit formed)
- **Business:** 3 new client opportunities from better follow-up
- **Personal:** Feel less anxious about "forgetting people"

#### L2: Epics (5 major themes)

**Epic 1: Core CRM Foundation**
- **Scope:** Contact database, basic CRUD, search, tags
- **Value:** Foundation for all other features
- **Dependencies:** None (can start immediately)
- **Timeline:** Weeks 1-4
- **Deliverable:** Working contact database with 100 contacts imported

**Epic 2: AI Context Engine**
- **Scope:** Integration with email/calendar/notes to extract context
- **Value:** Automatically remembers what I discussed with each person
- **Dependencies:** Epic 1 complete (needs contact DB)
- **Timeline:** Weeks 5-8
- **Deliverable:** Auto-populated contact timelines from email history

**Epic 3: Intelligent Reminders**
- **Scope:** AI-driven follow-up suggestions based on relationship strength + context
- **Value:** Proactive nudges prevent relationship decay
- **Dependencies:** Epic 1 + 2 (needs contacts + context)
- **Timeline:** Weeks 9-12
- **Deliverable:** Daily digest of suggested follow-ups

**Epic 4: Privacy & Security**
- **Scope:** Local-first architecture, encryption, no cloud leaks
- **Value:** Trust system with sensitive relationship data
- **Dependencies:** None (parallel to others)
- **Timeline:** Weeks 1-16 (ongoing)
- **Deliverable:** Security audit report + encryption implementation

**Epic 5: Habit Formation**
- **Scope:** Onboarding, UI/UX optimization, integration with daily routine
- **Value:** Ensure tool is actually used (not abandoned)
- **Dependencies:** Epic 1-3 working
- **Timeline:** Weeks 13-16
- **Deliverable:** 30-day usage streak + habit anchor established

#### L3: Features (18 capabilities)

**From Epic 1: Core CRM Foundation**
1. Contact CRUD (Create, Read, Update, Delete)
2. Contact search (full-text, fuzzy)
3. Tagging system (categories, relationship types)
4. Import from existing sources (Google Contacts, LinkedIn)
5. Export/backup functionality

**From Epic 2: AI Context Engine**
6. Email integration (read-only access to Gmail)
7. Calendar integration (past meetings extraction)
8. Notes integration (scan for mentions)
9. Context timeline (auto-generated relationship history)
10. Conversation topic extraction (AI identifies themes)

**From Epic 3: Intelligent Reminders**
11. Relationship strength scoring (recency, frequency, depth)
12. Follow-up suggestions (who, when, why)
13. Daily digest email (morning summary)
14. Smart scheduling (suggest meeting times)
15. Context-aware templates (personalized outreach drafts)

**From Epic 4: Privacy & Security**
16. Local SQLite database (no cloud)
17. End-to-end encryption for sensitive notes
18. Audit log (track all data access)

**From Epic 5: Habit Formation**
19. Onboarding wizard (import contacts, set preferences)
20. Daily habit anchor (integrate with morning routine)
21. Gamification (streaks, progress tracking)

[Full L4-L6 breakdown would continue here with 40-80 user stories, 150-300 tasks, 300-600 sub-tasks...]

#### L4: User Stories (Sample - would have 40-80 total)

**Epic 1 Stories:**
- As a user, I want to add a new contact with name/email/phone, so I can start tracking relationships
- As a user, I want to search contacts by name/company/tag, so I can quickly find people
- As a user, I want to tag contacts with categories, so I can organize my network
- As a user, I want to import my Google Contacts, so I don't manually re-enter 200 people
- As a user, I want to export my data, so I can back up or migrate

**Epic 2 Stories:**
- As a user, I want the system to read my email history, so it auto-populates contact context
- As a user, I want to see a timeline of interactions per contact, so I remember past conversations
- As a user, I want the AI to identify conversation topics, so I remember what we discussed
- [etc. - 10 more stories for Epic 2]

[Full list continues for all 5 epics...]

#### L5: Tasks (Sample - would have 150-300 total)

**Epic 1, Feature 1 (Contact CRUD):**
- [ ] Design database schema for contacts table (2h)
- [ ] Set up SQLite database (1h)
- [ ] Create contact model class (2h)
- [ ] Implement CREATE endpoint (3h)
- [ ] Implement READ endpoint (2h)
- [ ] Implement UPDATE endpoint (3h)
- [ ] Implement DELETE endpoint (2h)
- [ ] Write unit tests for CRUD (4h)
- [ ] Build simple UI form for adding contacts (6h)
- [ ] Test end-to-end contact creation (2h)

[Full task list continues across all features...]

#### L6: Sub-tasks (Sample - would have 300-600 total)

**Task: Design database schema (2h)**
- [ ] Research SQLite best practices for contact data (30 min)
- [ ] List all contact fields (name, email, phone, company, etc.) (15 min)
- [ ] Define data types for each field (15 min)
- [ ] Design indexes for search performance (20 min)
- [ ] Add created_at/updated_at timestamps (10 min)
- [ ] Design foreign key relationships for tags (20 min)
- [ ] Write SQL CREATE TABLE statement (10 min)

**Task: Set up SQLite database (1h)**
- [ ] Install better-sqlite3 npm package (5 min)
- [ ] Create database file at ./data/crm.db (5 min)
- [ ] Write initialization script (20 min)
- [ ] Run schema creation (5 min)
- [ ] Test connection (10 min)
- [ ] Set up migrations folder (15 min)

[Full sub-task list continues for all 150-300 tasks...]

### TRIZ Analysis

**Contradiction Identified:**
**Need privacy (local-first, no cloud)** vs **Need AI features (require cloud LLM APIs)**

**Conflicting Parameters:**
- Parameter 1: Data privacy (local storage, no external access)
- Parameter 2: AI capability (requires cloud models like Claude API)

**Inventive Principles Applied:**
- **Principle 1: Segmentation** - Separate sensitive data (local) from anonymized context (sent to API)
- **Principle 24: Intermediary** - Use local embedding model for search, only send anonymized summaries to cloud for generation
- **Principle 27: Cheap short-living objects** - Generate temporary, anonymized prompts that don't expose PII

**Resolution Strategy:**
1. **Contact data stays local:** Names, emails, phone numbers NEVER sent to cloud
2. **Anonymized context sent to AI:** "Person A discussed topic X on date Y" instead of "John Smith from Acme Corp..."
3. **Local embeddings for search:** Use sentence-transformers (local model) for semantic search
4. **Cloud AI for generation only:** Claude API generates follow-up templates from anonymized context

**Novel Approach:**
This "anonymized intermediary" pattern allows AI-powered features while maintaining privacy. Contact details never leave device, but still get AI-powered insights.

### Templates Created

#### Template 1: Follow-Up Email Generator

```markdown
# Follow-Up Email Template

## Inputs (Auto-populated from CRM)
- Last interaction date: {{last_contact_date}}
- Last topic discussed: {{last_topic}}
- Relationship strength: {{strength_score}}/10
- Contact's current focus: {{current_context}}

## Generated Email

Subject: {{ai_generated_subject}}

Hi {{first_name}},

{{ai_generated_opening_based_on_last_topic}}

{{ai_generated_value_add_or_question}}

{{ai_generated_closing}}

Best,
{{my_name}}

## Usage Instructions
1. System auto-selects contacts due for follow-up (30+ days, strength >6/10)
2. AI generates personalized draft based on last interaction
3. User reviews/edits before sending
4. Sent emails auto-logged back to CRM timeline
```

#### Template 2: Relationship Strength Scorecard

```markdown
# Relationship Strength Calculation

## Inputs
- Recency: Days since last interaction
- Frequency: Interactions per month (last 6 months)
- Depth: Avg conversation length (email word count, meeting minutes)
- Reciprocity: Ratio of outbound vs inbound contacts
- Shared context: Number of common topics/interests

## Formula
Strength Score = (Recency * 0.3) + (Frequency * 0.25) + (Depth * 0.2) + (Reciprocity * 0.15) + (Context * 0.1)

## Score Bands
- 9-10: Inner circle (VIP relationships)
- 7-8: Strong connections (active network)
- 5-6: Casual contacts (occasional touch-base)
- 3-4: Weak ties (at risk of decay)
- 0-2: Dormant (needs revival or archive)

## Usage
Auto-calculated daily, displayed on contact card, triggers follow-up suggestions when score drops below 6.
```

#### Template 3: Weekly Relationship Review

```markdown
# Weekly CRM Review (Sundays 9am, 15 min)

## Section 1: Wins This Week (2 min)
- [ ] Who did I have great conversations with?
- [ ] Any new connections made?
- [ ] Follow-ups that led to opportunities?

## Section 2: Strength Changes (3 min)
- [ ] Review contacts with score drop >2 points
- [ ] Review contacts with score increase >2 points
- [ ] Any patterns? (e.g., neglecting certain categories)

## Section 3: Upcoming Follow-Ups (5 min)
- [ ] Review AI-suggested follow-ups for next week
- [ ] Add manual follow-ups (birthdays, anniversaries, milestones)
- [ ] Schedule meeting invites where appropriate

## Section 4: System Health (5 min)
- [ ] Check email integration working (last sync time)
- [ ] Review AI suggestion quality (any bad recommendations?)
- [ ] Export backup (monthly on first Sunday)

## Output
- Todo list for next week's relationship actions
- Adjustments to follow-up cadence if needed
```

### Comprehensive Integration Analysis

#### Calendar Mapping

**Weekly Time Required:**
- **Weeks 1-4 (Epic 1):** 15h/week
  - Mon/Wed: 6-9pm (6h) - Core development
  - Sat: 9am-12pm, 2-5pm (6h) - Extended sessions
  - Sun: 10-1pm (3h) - Review & planning
- **Weeks 5-8 (Epic 2):** 12h/week
  - Tue/Thu: 6-9pm (6h) - AI integration
  - Sat: 9am-3pm (6h) - Testing & refinement
- **Weeks 9-12 (Epic 3):** 10h/week
  - Wed/Thu: 7-9pm (4h) - Reminder logic
  - Sat: 9am-3pm (6h) - UI polish
- **Weeks 13-16 (Epic 5):** 8h/week
  - Daily: 30 min dogfooding (using the tool)
  - Sat: 9am-2pm (5h) - Refinement based on usage

**Peak Periods:**
- Weeks 2-3: Most intense (database + import logic)
- Week 6: AI integration complexity spike
- Week 14: Habit formation (requires daily discipline)

**Conflicts:**
- Saturday mornings overlap with family breakfast (move to 10am start)
- Wednesday nights have gym commitment (shift to Thursday)
- Memorial Day weekend (Week 12): Skip, extend timeline by 1 week

**Adjustments:**
- Negotiate with partner: Saturdays 10am-3pm for 16 weeks
- Move gym to Tuesday/Friday to free Wednesday
- Plan buffer week (Week 17) for slippage

#### Resource Planning

**Budget: $500**
- Claude API: $100/month * 4 months = $400 (estimated 1M tokens/month)
- Domain + hosting (if web version): $50
- Tools/services: $50 buffer

**Tools:**
- Development: VS Code (free), Node.js (free), SQLite (free)
- AI: Claude API (paid), sentence-transformers (free, local)
- Deployment: Local-first (free), optional Electron for desktop app
- Testing: Jest (free), Playwright (free)

**Skills:**
- Have: JavaScript, Node.js, SQL, API integration
- Need: sentence-transformers (Python) - 8h learning curve
- Need: Encryption best practices - 4h research
- Nice-to-have: Electron (if desktop app) - 12h learning

**Support:**
- Technical mentor: John (security review) - 2h of his time
- Beta testers: 5 trusted friends - 1h each for feedback
- Accountability partner: Sarah (weekly check-ins) - 30 min/week

#### Dependency Analysis

**Prerequisites:**
- None (can start immediately)
- Email API access (Gmail OAuth setup) - prerequisite for Epic 2

**Parallel Tracks:**
- Epic 1 (Core CRM) and Epic 4 (Security) can run in parallel
- Epic 2, 3 must be sequential (context engine before reminders)
- Epic 5 (Habit) depends on Epic 1-3 being functional

**Blockers:**
- Gmail OAuth approval (may take 1-2 weeks) - start early in Week 1
- Claude API quota (if exceeded, pause and upgrade) - monitor weekly
- Local embedding model performance (may need GPU) - test in Week 5

**Critical Path:**
- Epic 1 (4 weeks) → Epic 2 (4 weeks) → Epic 3 (4 weeks) → Epic 5 (4 weeks) = 16 weeks minimum
- Epic 4 runs parallel, doesn't extend timeline

### Risk Management

| Risk | Prob | Impact | Trigger | Mitigation | Contingency | Owner |
|------|------|--------|---------|------------|-------------|-------|
| Gmail API access denied | Low | High | OAuth rejection email | Apply early, follow guidelines exactly | Use IMAP fallback (less integrated) | Me |
| Claude API costs exceed budget | Med | Med | Monthly bill >$100 | Monitor usage weekly, optimize prompts | Switch to local model (lower quality) | Me |
| Time estimate too optimistic | High | Med | Behind by Week 4 | Time-box features, cut scope | Drop Epic 3 (reminders), keep core | Me |
| Adoption failure (tool not used) | Med | High | <3 uses/week by Week 14 | Design for habits from Day 1, daily anchor | Simplify to basic CRM only | Me |
| Email integration breaks | Med | Med | Sync fails >2 days | Build retry logic, error alerts | Manual entry fallback | Me |
| Data loss (no backup) | Low | Crit | Database corruption | Daily auto-backup to cloud (encrypted) | Restore from last backup | Me |
| Privacy leak (data exposed) | Low | Crit | Suspicious API calls detected | Code review, security audit | Immediate shutdown, investigate | John (mentor) |
| Scope creep (feature bloat) | High | Med | Feature list grows >25% | Strict MVP mindset, defer to v2 | Freeze features at Week 8 | Me |
| Competitor launches similar tool | Low | Low | New product announcement | Monitor market quarterly | Differentiate on privacy/ADHD focus | Me |
| Burnout (lose motivation) | Med | High | Skip 2+ consecutive weeks | Weekly accountability with Sarah | Take 1-week break, resume | Sarah (partner) |
| Technical debt accumulates | Med | Med | Code quality score <7/10 | Weekly refactoring session (1h) | Dedicate Week 17 to cleanup | Me |
| AI suggestions low quality | Med | High | Relevance <80% in testing | A/B test prompts, collect feedback | Manual mode with AI-assist | Me |

### Success Framework

#### KPIs & Metrics

**Input Metrics (What I Control):**
- Development hours per week (target: 12h avg)
- Code commits per week (target: 10+)
- Tests written (target: 80% coverage)
- Daily usage of tool (target: 7 days/week)

**Output Metrics (What I Produce):**
- Features completed (target: 18/18)
- Contacts imported (target: 200+)
- AI suggestions generated (target: 10/day)
- Follow-ups sent via tool (target: 5/week)

**Outcome Metrics (What Changes):**
- Follow-up rate: 25% → 75% (3x improvement)
- Relationship strength avg: 5.2 → 7.0 (boost network quality)
- Consulting leads from network: +3 in 6 months
- Anxiety about "forgetting people": 8/10 → 3/10 (self-reported)

**Leading Indicators (Early Signals):**
- Week 4: Core CRM functional (can add/search contacts)
- Week 8: AI context populating correctly (80% accuracy)
- Week 12: Daily habit forming (6+ days/week usage)

**Lagging Indicators (Final Results):**
- Month 6: Follow-up rate sustained at 75%
- Month 6: 3 client opportunities from better follow-up
- Month 12: Tool becomes "can't live without it"

#### Review Process

**Daily (5 min):**
- Morning: Check daily digest of suggested follow-ups
- Evening: Log any manual relationship interactions
- Monitor: AI suggestion quality (thumbs up/down)

**Weekly (30 min, Sundays 9am):**
- Review relationship strength changes
- Plan next week's follow-ups
- Check development progress (if still building)
- Accountability call with Sarah

**Monthly (2h, First Sunday):**
- Deep metrics review (follow-up rate, relationship strength trends)
- Export backup
- Optimize AI prompts based on quality feedback
- Adjust follow-up cadence if needed

**Quarterly (4h):**
- Strategic review: Is tool delivering expected ROI?
- Feature prioritization for next quarter
- Cost analysis (API usage vs value)
- Security audit

#### Decision Gates

**Gate 1: End of Week 4 (Epic 1 Complete)**
- **Criteria:** Core CRM functional, 100 contacts imported, search working
- **Decision:** If YES → Continue to Epic 2. If NO → Extend Epic 1 by 1 week max, then reassess.
- **Kill Switch:** If core functionality not working after 6 weeks total, abort project.

**Gate 2: End of Week 8 (Epic 2 Complete)**
- **Criteria:** Email integration working, context auto-populating with 80% accuracy
- **Decision:** If YES → Continue to Epic 3. If NO → Simplify context (manual entry), move to Epic 3.
- **Kill Switch:** If AI context completely non-functional, pivot to manual CRM (skip Epic 3).

**Gate 3: End of Week 12 (Epic 3 Complete)**
- **Criteria:** Reminders generating, at least 5 follow-ups sent via tool
- **Decision:** If YES → Continue to Epic 5. If NO → Use tool as-is, defer Epic 5.
- **Kill Switch:** If follow-up rate not improving by Week 14, investigate adoption issues.

**Gate 4: End of Week 16 (Full Launch)**
- **Criteria:** Using tool daily, follow-up rate >60%, relationship strength trending up
- **Decision:** If YES → Declare v1.0 complete, shift to maintenance mode. If NO → Diagnose adoption issues, iterate.
- **Kill Switch:** If not using tool by Week 18, archive project as failed.

### Implementation Guide

#### Phase-by-Phase Breakdown

**Phase 1: Foundation (Weeks 1-4)**

**Week 1:**
- [ ] Set up development environment (Node.js, SQLite, VS Code) - 2h
- [ ] Design database schema - 2h
- [ ] Create contact model - 2h
- [ ] Implement CRUD operations - 6h
- [ ] Write unit tests for CRUD - 3h
- **Deliverable:** Working contact CRUD API

**Week 2:**
- [ ] Build search functionality (full-text + fuzzy) - 4h
- [ ] Implement tagging system - 4h
- [ ] Create simple UI for adding contacts - 6h
- [ ] Import Google Contacts (OAuth + API) - 3h
- **Deliverable:** Can add, search, tag contacts via UI

**Week 3:**
- [ ] Import contacts from Google Contacts - 2h
- [ ] Build export/backup functionality - 3h
- [ ] Polish UI (responsive design, keyboard shortcuts) - 6h
- [ ] End-to-end testing with 100 contacts - 2h
- [ ] Set up daily auto-backup - 2h
- **Deliverable:** 100 contacts imported, backups working

**Week 4:**
- [ ] Performance optimization (index tuning) - 3h
- [ ] Security hardening (SQL injection prevention) - 3h
- [ ] Documentation (API docs, usage guide) - 4h
- [ ] User acceptance testing (dogfood for 1 week) - 5h
- **Deliverable:** Gate 1 decision - ready for Epic 2?

**Phase 2: AI Context (Weeks 5-8)**

**Week 5:**
- [ ] Set up Gmail OAuth - 3h
- [ ] Implement email read access - 4h
- [ ] Extract email history for each contact - 4h
- [ ] Test sentence-transformers (local embedding) - 4h
- **Deliverable:** Can read email history per contact

**Week 6:**
- [ ] Build context timeline (chronological interaction view) - 6h
- [ ] Integrate Claude API for topic extraction - 4h
- [ ] Test AI topic extraction accuracy - 2h
- [ ] Optimize prompts for better accuracy - 3h
- **Deliverable:** Auto-generated context timelines with 80% accuracy

**Week 7:**
- [ ] Add calendar integration (past meetings) - 4h
- [ ] Add notes integration (scan for mentions) - 4h
- [ ] Build unified context view - 3h
- [ ] Performance testing (handle 200 contacts) - 2h
- **Deliverable:** Comprehensive context from email + calendar + notes

**Week 8:**
- [ ] Polish context UI (timeline visualization) - 4h
- [ ] Error handling for API failures - 3h
- [ ] User testing (beta with 3 friends) - 3h
- [ ] Refinement based on feedback - 5h
- **Deliverable:** Gate 2 decision - context engine working?

**Phase 3: Intelligent Reminders (Weeks 9-12)**

**Week 9:**
- [ ] Design relationship strength algorithm - 3h
- [ ] Implement scoring calculation - 4h
- [ ] Backfill scores for existing contacts - 2h
- [ ] Test score accuracy (does it match intuition?) - 3h
- **Deliverable:** Every contact has a strength score

**Week 10:**
- [ ] Build follow-up suggestion logic - 5h
- [ ] Integrate Claude API for suggestion generation - 4h
- [ ] Create daily digest email template - 3h
- [ ] Test suggestions (are they relevant?) - 3h
- **Deliverable:** Daily digest with 5+ follow-up suggestions

**Week 11:**
- [ ] Build follow-up template generator - 4h
- [ ] Add smart scheduling (suggest meeting times) - 4h
- [ ] Implement feedback loop (thumbs up/down on suggestions) - 3h
- [ ] User testing (beta with 5 friends) - 4h
- **Deliverable:** Can generate personalized follow-up drafts

**Week 12:**
- [ ] Refinement based on beta feedback - 6h
- [ ] Performance optimization (digest generation <5s) - 3h
- [ ] Documentation (how to use reminders) - 2h
- [ ] Send first 5 follow-ups via tool - 4h
- **Deliverable:** Gate 3 decision - reminders useful?

**Phase 4: Habit Formation (Weeks 13-16)**

**Week 13:**
- [ ] Design onboarding wizard - 3h
- [ ] Build wizard UI (step-by-step setup) - 6h
- [ ] Integrate wizard with tool - 3h
- [ ] Test with new user (friend) - 3h
- **Deliverable:** Smooth onboarding experience

**Week 14:**
- [ ] Establish daily habit anchor (integrate with morning routine) - 2h
- [ ] Add gamification (streaks, progress tracking) - 4h
- [ ] Daily usage for 7 consecutive days - 3h (30 min/day)
- [ ] Collect personal usage data - 1h
- **Deliverable:** 7-day usage streak achieved

**Week 15:**
- [ ] Analyze usage patterns (when, how often, what features) - 3h
- [ ] Optimize UI based on personal usage - 4h
- [ ] Add keyboard shortcuts for frequent actions - 3h
- [ ] Daily usage continues (14-day streak) - 3h (30 min/day)
- **Deliverable:** 14-day usage streak, tool feels natural

**Week 16:**
- [ ] Final polish (UI tweaks, performance) - 4h
- [ ] Documentation (complete user guide) - 4h
- [ ] Security audit with John (mentor) - 2h
- [ ] Celebrate v1.0 launch - 1h
- [ ] Daily usage continues (21-day streak) - 3h (30 min/day)
- **Deliverable:** Gate 4 decision - v1.0 complete!

#### Rollout Strategy

**Pilot Approach:**
- Weeks 1-12: Solo usage (dogfooding)
- Week 8: Invite 3 beta testers (close friends)
- Week 11: Invite 5 more beta testers (broader network)
- Week 16: Soft launch (share with inner circle)
- Month 6: Public launch (if results are strong)

**Scale Plan:**
- Month 1-3: Personal use only, refine based on own needs
- Month 4-6: Inner circle (10-15 users), collect feedback
- Month 7-12: Broader network (50 users), iterate on feedback
- Year 2: Consider productization (if demand exists)

**Communication:**
- Week 8: Email beta testers: "I'm building a personal CRM, want to test?"
- Week 16: Post on LinkedIn: "I built an AI-powered CRM for ADHD professionals"
- Month 6: Write blog post: "How I 3x'd my follow-up rate with a custom CRM"

#### Monitoring & Adaptation

**Dashboard (Daily View):**
- Today's suggested follow-ups: 5 cards with context
- Relationship strength changes: Graph showing trends
- Recent interactions: Timeline of last 7 days
- Habit streak: Days in a row using tool
- System health: Last sync time, errors, API quota

**Alerts:**
- Email sync failed >24h → Notification + retry button
- Claude API quota at 80% → Email warning
- Relationship strength drops >3 points → Nudge to follow up
- No usage for 2 days → Reminder notification

**Adjustment Triggers:**
- Follow-up rate not improving by Week 10 → Simplify suggestions
- AI accuracy <70% by Week 8 → Revisit prompts or switch models
- Daily usage <5 days/week by Week 14 → Investigate friction points
- API costs >$120/month → Optimize prompts or switch to local models

### Appendices

#### Appendix A: Detailed Cost Breakdown

| Item | Monthly | Total (4 months) | Notes |
|------|---------|------------------|-------|
| Claude API | $100 | $400 | Estimate 1M tokens/month |
| Domain | $1 | $12 (annual) | Optional for web version |
| Hosting | $0 | $0 | Local-first, no hosting |
| Tools | $0 | $0 | All free (VS Code, SQLite, Node.js) |
| Buffer | - | $50 | Misc expenses |
| **Total** | - | **$500** | |

#### Appendix B: Technical Architecture Diagram

```
┌─────────────────────────────────────────┐
│           User Interface (Web/Desktop)  │
│  - Contact List                          │
│  - Timeline View                         │
│  - Daily Digest                          │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│         Application Layer (Node.js)     │
│  - API Routes (Express)                  │
│  - Business Logic                        │
│  - Authentication                        │
└──────────────┬──────────────────────────┘
               │
      ┌────────┴────────┐
      │                 │
┌─────▼─────┐  ┌────────▼────────┐
│  SQLite   │  │  AI Services    │
│  Database │  │  - Claude API   │
│  (Local)  │  │  - Embeddings   │
└───────────┘  └────────┬────────┘
                        │
              ┌─────────▼─────────┐
              │  External APIs    │
              │  - Gmail (OAuth)  │
              │  - Google Calendar│
              └───────────────────┘
```

#### Appendix C: Sample Relationship Strength Calculation

**Contact: Jane Doe**

**Inputs:**
- Recency: Last interaction 10 days ago → Score: 9/10 (recent)
- Frequency: 8 interactions in last 6 months → Score: 7/10 (moderate)
- Depth: Avg 300 words per email, 30 min meetings → Score: 8/10 (substantial)
- Reciprocity: 12 outbound, 10 inbound → Score: 8/10 (balanced)
- Shared Context: 5 common topics (AI, consulting, productivity, parenting, hiking) → Score: 9/10 (strong)

**Calculation:**
Strength = (9 * 0.3) + (7 * 0.25) + (8 * 0.2) + (8 * 0.15) + (9 * 0.1)
         = 2.7 + 1.75 + 1.6 + 1.2 + 0.9
         = **8.15/10** → **Strong Connection** (active network)

**Interpretation:** Jane is a strong, active relationship. No follow-up urgency, but maintain regular contact (every 2-3 weeks).

#### Appendix D: Security Threat Model

**Threat 1: Data Breach (Unauthorized Access to Local Database)**
- **Likelihood:** Low (local-only access)
- **Impact:** Critical (exposes all contact data)
- **Mitigation:** Encrypt database at rest, require OS-level authentication
- **Detection:** File integrity monitoring, audit logs

**Threat 2: API Key Exposure (Claude API key leaked)**
- **Likelihood:** Medium (accidental commit to git)
- **Impact:** High (financial + quota abuse)
- **Mitigation:** Store in environment variables, add to .gitignore, rotate quarterly
- **Detection:** Monitor API usage for anomalies

**Threat 3: Privacy Leak (PII sent to Claude API)**
- **Likelihood:** Medium (coding error in anonymization)
- **Impact:** Critical (violates privacy promise)
- **Mitigation:** Code review, unit tests for anonymization, manual audit of API calls
- **Detection:** Log all API requests (review for PII)

**Threat 4: Email Integration Compromise (OAuth token stolen)**
- **Likelihood:** Low (requires OS-level breach)
- **Impact:** High (attacker reads all emails)
- **Mitigation:** Store OAuth tokens encrypted, revoke and rotate monthly
- **Detection:** Monitor OAuth scopes, check for unusual API calls

[Additional threats documented...]
```

**❌ BAD Deep Output:**

```markdown
## Deep Plan: AI-Powered CRM

### Summary
Build a CRM with AI features. Should be good.

### Scorecard
- Alignment: 9/10
- Feasibility: 7/10
- Impact: 9/10
- Overall: 25/30

### Plan
1. Set up database
2. Add contacts
3. Build AI features
4. Make it work
5. Use it daily

### Risks
- Might take longer than expected
- AI might not work well
- Could be hard to use
- Privacy concerns
- Cost might be high
- Might not adopt it

### Decision
GO - seems like a great idea.

### Next Steps
Start building the database and see how it goes.
```

**Why BAD:**
- No executive summary (missing investment, timeline, critical success factors)
- Scorecard missing 5+ dimensions (Resource Availability, Strategic Fit, Risk, Innovation, Scalability)
- No L1-L6 breakdown (plan is 5 vague steps, not 200+ lines)
- No TRIZ analysis (contradiction exists but not addressed)
- No templates created
- No integration analysis (calendar, resources, dependencies)
- Risks are generic with no probability/impact/mitigation
- No success framework (KPIs, review process, decision gates)
- No implementation guide (phases, rollout, monitoring)
- Total length: ~200 lines (too short for Deep track)

---

## Quality Measurement

### How to Verify Output Meets Standards

#### Quick Track Verification

```bash
# Automated checks (could be scripted)
line_count=$(wc -l < output.md)
[[ $line_count -ge 100 ]] && echo "✅ Length OK" || echo "❌ Too short"

grep -q "Go/NoGo Decision" output.md && echo "✅ Decision present" || echo "❌ Missing decision"
grep -q "Critical Risks" output.md && echo "✅ Risks present" || echo "❌ Missing risks"

# Manual checks
# - [ ] Scorecard has numeric scores (not "good", "bad")
# - [ ] Decision is binary (GO/NO-GO/DEFER, not "maybe")
# - [ ] Risks are specific (not "might fail")
# - [ ] Next step is actionable (not "research more")
```

#### Standard Track Verification

```bash
# Automated checks
line_count=$(wc -l < output.md)
[[ $line_count -ge 300 ]] && echo "✅ Length OK" || echo "❌ Too short"

grep -q "Workflow Plan" output.md && echo "✅ Workflow present" || echo "❌ Missing workflow"
grep -q "Integration Plan" output.md && echo "✅ Integration present" || echo "❌ Missing integration"
grep -q "Success Metrics" output.md && echo "✅ Metrics present" || echo "❌ Missing metrics"

# Count risks (should be 5+)
risk_count=$(grep -c "^|" output.md | grep -A 5 "Risk Analysis")
[[ $risk_count -ge 5 ]] && echo "✅ Enough risks" || echo "❌ Need more risks"

# Manual checks
# - [ ] Scorecard has 6+ dimensions
# - [ ] Workflow has 3+ phases
# - [ ] Integration addresses calendar conflicts
# - [ ] Success metrics include leading AND lagging
# - [ ] Decision has confidence score
```

#### Deep Track Verification

```bash
# Automated checks
line_count=$(wc -l < output.md)
[[ $line_count -ge 800 ]] && echo "✅ Length OK" || echo "❌ Too short"

grep -q "L1: Vision" output.md && echo "✅ L1 present" || echo "❌ Missing L1"
grep -q "L2: Epics" output.md && echo "✅ L2 present" || echo "❌ Missing L2"
grep -q "L6: Sub-tasks" output.md && echo "✅ L6 present" || echo "❌ Missing L6"
grep -q "TRIZ Analysis" output.md && echo "✅ TRIZ present" || echo "❌ Missing TRIZ"

# Count templates (should be 3+)
template_count=$(grep -c "^#### Template" output.md)
[[ $template_count -ge 3 ]] && echo "✅ Enough templates" || echo "❌ Need more templates"

# Count risks (should be 10+)
risk_count=$(grep -c "^|" output.md | grep -A 10 "Risk Management")
[[ $risk_count -ge 10 ]] && echo "✅ Enough risks" || echo "❌ Need more risks"

# Manual checks
# - [ ] L6 has 300+ sub-tasks
# - [ ] Calendar mapping includes weekly breakdown
# - [ ] Resource planning has detailed budget
# - [ ] 3+ reusable templates created
# - [ ] Implementation guide is step-by-step
```

### Scoring Rubric (For Human Review)

| Criterion | Quick (Max 10) | Standard (Max 10) | Deep (Max 10) |
|-----------|----------------|-------------------|---------------|
| **Length** | 100-200 lines | 300-500 lines | 800-1500+ lines |
| **Completeness** | All 6 required sections | All 7 required sections | All 10+ required sections |
| **Specificity** | Risks are specific, not generic | Workflow has tasks, not vague steps | L6 has actionable sub-tasks |
| **Actionability** | Next step is clear | Next 3 steps have dates | Implementation guide is executable |
| **Measurability** | Scorecard has numbers | Metrics are quantified | KPIs cover input/output/outcome |
| **Justification** | Decision has 2-3 sentence rationale | Decision has confidence score + conditions | Decision has 3-5 sentence rationale + gates |

**Passing Score:** 7/10 or higher (meets standards)

---

## Validation Workflow

**After completing any track output:**

1. **Run automated checks** (bash scripts above)
2. **Complete quality checklist** (per track)
3. **Score against rubric** (aim for 7+/10)
4. **If score <7:** Revise output before saving
5. **If score ≥7:** Save to `output/` directory

**Example:**

```bash
# After completing Quick Track output
./scripts/validate-output.sh quick output/idea-001-quick.md

# Output:
# ✅ Length OK (142 lines)
# ✅ Decision present
# ✅ Risks present
# ✅ Scorecard has numeric scores
# ❌ Next step not actionable ("research more" is vague)
# Score: 6/10 - NEEDS REVISION
```

---

## Summary

| Track | Min Lines | Required Elements | Time | Purpose |
|-------|-----------|------------------|------|---------|
| **Quick** | 100-200 | Scorecard, Go/NoGo, 2-3 risks, time estimate, next step | 5-10 min | Rapid triage |
| **Standard** | 300-500 | Workflow, scorecard, integration, metrics, 5+ risks, decision | 30-60 min | Actionable plan |
| **Deep** | 800-1500+ | L1-L6, TRIZ, 3+ templates, integration, 10+ risks, implementation guide | 2-4 hours | Complete blueprint |

**Key Principle:** Quality is measured by completeness, specificity, and actionability—not just length. A 150-line Quick output that meets all criteria is excellent. A 500-line Standard output that's vague and generic is poor.

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-05 | Initial standards document created |
