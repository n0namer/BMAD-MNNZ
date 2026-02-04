# Template Composition Patterns

**Purpose:** Combine multiple framework templates for complex projects that span multiple life domains.

**Last Updated:** 2026-02-04

---

## Overview

Complex projects often require combining frameworks from multiple domains (business, finance, health, personal). This guide provides 10 proven composition patterns that integrate 2-5 frameworks with clear auto-linking rules and output artifacts.

**Key Concepts:**
- **Composition Pattern:** Predefined combination of frameworks for specific use case
- **Auto-Linking:** Automatic connection of outputs between framework templates
- **Integration Flow:** Ordered sequence of framework execution
- **Output Artifacts:** Combined documents produced from multiple templates

---

## Pattern 1: Startup Launch

**Frameworks:** Lean Canvas + NPV + OKRs + Pomodoro
**Domains:** Business + Finance + Personal
**Use Case:** Launching new product, service, or side business
**Total Time:** 8-12 hours
**Complexity:** High

### Integration Flow

```
Step 1: Lean Canvas (Business Model) → 2-3 hours
  ↓ (auto-link: Revenue Streams → NPV Cash Inflows)
Step 5: NPV Analysis (Financial Viability) → 2-3 hours
  ↓ (auto-link: Cost Structure → NPV Cash Outflows)
Step 6: OKRs (Strategic Alignment) → 2-3 hours
  ↓ (auto-link: Objectives → Deep Plan L1)
Step 8: Pomodoro (Execution Planning) → 1-2 hours
  ↓ (auto-link: Time Blocks → Deep Plan L5)
```

### Auto-Linking Rules

| Source Framework | Source Field | Target Framework | Target Field |
|------------------|--------------|------------------|--------------|
| Lean Canvas | Revenue Streams | NPV | Cash Inflows (positive) |
| Lean Canvas | Cost Structure | NPV | Cash Outflows (negative) |
| Lean Canvas | Key Metrics | OKRs | Key Results |
| NPV | Break-Even Month | OKRs | Timebound objective |
| OKRs | Objectives | Deep Plan | L1 Strategic Goals |
| OKRs | Key Results | Deep Plan | L2 Milestones |
| Pomodoro | Daily Blocks | Deep Plan | L5 Daily Tasks |

### Output Artifacts

1. **lean-canvas-analysis.md** - Business model breakdown
2. **npv-financial-model.md** - 12-24 month financial projection
3. **okrs-strategic-plan.md** - Quarterly objectives and key results
4. **workflow-plan.md** - Combined execution plan with all 5 levels
5. **startup-dashboard.md** - Single-page summary

### Example Workflow

**Context:** Launching a SaaS product for freelancers

#### Phase 1: Business Model (Lean Canvas - 2.5 hours)

```markdown
## Lean Canvas Output

**Problem:**
1. Freelancers struggle with client invoicing
2. Manual time tracking is error-prone
3. No integrated tax calculation

**Customer Segments:**
- Solo freelancers ($50k-$150k/year)
- Small agencies (2-10 people)

**Unique Value Proposition:**
"Invoice, track, and file taxes in one place - 10 minutes per week"

**Solution:**
1. Automated time tracking
2. One-click invoicing
3. Real-time tax estimation

**Revenue Streams:**
- Monthly subscription: $29/month
- Annual plan: $290/year (save $58)
- Target: 100 users by Month 6, 500 by Month 12

**Cost Structure:**
- Development: $15k (one-time)
- Hosting: $200/month
- Marketing: $1,000/month
- Support: $500/month (part-time)

**Key Metrics:**
- MRR (Monthly Recurring Revenue)
- Churn rate <5%
- CAC (Customer Acquisition Cost) <$100
- LTV/CAC ratio >3
```

#### Phase 2: Financial Viability (NPV - 2.5 hours)

**AUTO-LINKED from Lean Canvas:**
- Revenue: $29/user/month → NPV Cash Inflows
- Costs: Development + hosting + marketing + support → NPV Cash Outflows

```markdown
## NPV Financial Model

**Assumptions:**
- Discount rate: 10% (opportunity cost)
- Time horizon: 24 months
- Growth rate: 20 users/month (months 1-6), 40 users/month (months 7-12)

**Cash Flow Projection (Monthly):**

| Month | Users | MRR | Costs | Net Cash Flow | Cumulative |
|-------|-------|-----|-------|---------------|------------|
| 0 | 0 | $0 | $15,000 | -$15,000 | -$15,000 |
| 1 | 20 | $580 | $1,700 | -$1,120 | -$16,120 |
| 2 | 40 | $1,160 | $1,700 | -$540 | -$16,660 |
| 3 | 60 | $1,740 | $1,700 | $40 | -$16,620 |
| 6 | 120 | $3,480 | $1,700 | $1,780 | -$8,220 |
| 12 | 360 | $10,440 | $1,700 | $8,740 | +$12,560 |
| 24 | 840 | $24,360 | $1,700 | $22,660 | +$180,340 |

**NPV Calculation:**
NPV = -$15,000 + Σ(Cash Flow_t / (1+0.10)^t)
NPV (24 months) = $142,680

**Decision:** PROCEED - Positive NPV, break-even at Month 11
```

#### Phase 3: Strategic Alignment (OKRs - 2 hours)

**AUTO-LINKED from NPV:**
- Break-even Month 11 → Objective timeframe
- MRR targets → Key Results

```markdown
## OKRs - Q1 2026

**Objective 1:** Achieve product-market fit
- KR1: 100 paying users by end Q1 (currently 0)
- KR2: NPS score >40
- KR3: <5% monthly churn rate

**Objective 2:** Validate financial model
- KR1: MRR of $3,500 by Month 6
- KR2: CAC <$100
- KR3: LTV/CAC >3

**Objective 3:** Build repeatable growth engine
- KR1: 3 acquisition channels tested (content, referral, ads)
- KR2: 20% month-over-month user growth
- KR3: 2 case studies published

## OKRs - Q2 2026

**Objective 1:** Scale to profitability
- KR1: 360 paying users (break-even)
- KR2: MRR of $10,440
- KR3: Positive cash flow for 3 consecutive months
```

#### Phase 4: Execution Planning (Pomodoro - 1.5 hours)

**AUTO-LINKED from OKRs:**
- Q1 objectives → Weekly themes
- KR milestones → Daily tasks

```markdown
## Week 1-2: MVP Development (40 Pomodoros)

**Daily Allocation:**
- 4 Pomodoros: Core features (time tracking)
- 3 Pomodoros: Invoicing logic
- 2 Pomodoros: Testing

**Week 3-4: Beta Launch (30 Pomodoros)**

**Daily Allocation:**
- 3 Pomodoros: Bug fixes
- 3 Pomodoros: User onboarding
- 2 Pomodoros: Marketing content
- 1 Pomodoro: Support

**Months 2-6: Growth Phase (20 Pomodoros/week)**

**Weekly Allocation:**
- 8 Pomodoros: Feature development
- 6 Pomodoros: Marketing/sales
- 4 Pomodoros: Customer support
- 2 Pomodoros: Analytics review
```

#### Phase 5: Deep Plan Integration

**AUTO-GENERATED from all frameworks:**

```markdown
## Deep Plan - Startup Launch

**L1 - Strategic Goals (from OKRs):**
1. Achieve product-market fit (Q1)
2. Validate financial model (Q1-Q2)
3. Scale to profitability (Q2)

**L2 - Milestones (from Lean Canvas + NPV):**
1.1 MVP shipped (Month 1)
1.2 100 users acquired (Month 6)
2.1 Break-even achieved (Month 11)
3.1 $10k MRR (Month 12)

**L3 - Epics (from OKRs Key Results):**
1.1.1 Build time tracking (2 weeks)
1.1.2 Build invoicing (2 weeks)
1.2.1 Content marketing (ongoing)
1.2.2 Referral program (Week 8)

**L4 - User Stories (from Pomodoro themes):**
1.1.1.1 As a freelancer, I want automatic time tracking
1.1.1.2 As a freelancer, I want manual time entry backup
1.1.2.1 As a freelancer, I want one-click invoice generation

**L5 - Tasks (from Pomodoro daily blocks):**
- [ ] Week 1 Day 1: Design time tracking UI (4 Pomodoros)
- [ ] Week 1 Day 2: Implement timer logic (4 Pomodoros)
- [ ] Week 1 Day 3: Add start/stop controls (3 Pomodoros)
```

### Success Metrics

After completing this composition:
- ✅ Business model validated (Lean Canvas)
- ✅ Financial viability confirmed (NPV >0)
- ✅ Clear quarterly goals (OKRs)
- ✅ Executable daily plan (Pomodoro → Deep Plan L5)
- ✅ Single unified workflow-plan.md

### Memory Storage

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "template-compositions:startup-launch:success" \
  --content "4-framework composition: Lean Canvas → NPV → OKRs → Pomodoro. NPV=$142k, break-even Month 11. 100% of links auto-populated successfully."
```

---

## Pattern 2: Skill Acquisition

**Frameworks:** Deliberate Practice + Pomodoro + Habit Loop + Recovery Protocols
**Domains:** Personal + Health
**Use Case:** Learning new skill (coding, language, instrument, sport)
**Total Time:** 4-6 hours planning
**Complexity:** Medium

### Integration Flow

```
Step 1: Deliberate Practice (Skill Breakdown) → 2 hours
  ↓ (auto-link: Skill Components → Pomodoro Focus Areas)
Step 2: Pomodoro (Time Blocking) → 1 hour
  ↓ (auto-link: Daily Practice → Habit Loop Cue)
Step 3: Habit Loop (Consistency) → 1 hour
  ↓ (auto-link: Cue-Routine-Reward → Deep Plan L5)
Step 4: Recovery Protocols (Avoid Burnout) → 1 hour
  ↓ (auto-link: Rest Days → Pomodoro Schedule)
```

### Auto-Linking Rules

| Source Framework | Source Field | Target Framework | Target Field |
|------------------|--------------|------------------|--------------|
| Deliberate Practice | Skill Components | Pomodoro | Focus Areas (25-min blocks) |
| Deliberate Practice | Feedback Loops | Habit Loop | Reward |
| Pomodoro | Daily Practice Time | Habit Loop | Routine |
| Habit Loop | Cue | Deep Plan | L5 Daily Trigger |
| Recovery Protocols | Rest Days | Pomodoro | Off Days |
| Recovery Protocols | Intensity Limits | Deliberate Practice | Max Practice Time |

### Output Artifacts

1. **deliberate-practice-plan.md** - Skill breakdown and progression
2. **pomodoro-practice-schedule.md** - Daily time blocks
3. **habit-loop-design.md** - Cue-Routine-Reward system
4. **recovery-protocol.md** - Rest and intensity management
5. **workflow-plan.md** - Combined learning plan

### Example Workflow

**Context:** Learning to code in Python (beginner to job-ready in 6 months)

#### Phase 1: Deliberate Practice (2 hours)

```markdown
## Skill Breakdown

**Current Level:** Absolute beginner
**Target Level:** Junior developer (job-ready)
**Timeline:** 6 months (26 weeks)

**Skill Components:**
1. **Syntax & Fundamentals** (Weeks 1-4)
   - Variables, data types, operators
   - Control flow (if/else, loops)
   - Functions and scope
   - Feedback: Run code daily, check output

2. **Data Structures** (Weeks 5-8)
   - Lists, tuples, dictionaries
   - Sets and comprehensions
   - Feedback: Solve 5 problems/week on LeetCode Easy

3. **Object-Oriented Programming** (Weeks 9-12)
   - Classes and objects
   - Inheritance, polymorphism
   - Feedback: Build 2 small projects

4. **Libraries & Frameworks** (Weeks 13-18)
   - NumPy, Pandas (data manipulation)
   - Flask/Django (web dev)
   - Feedback: Contribute to 1 open-source project

5. **Portfolio Projects** (Weeks 19-26)
   - 3 substantial projects
   - GitHub presence
   - Feedback: Code reviews from mentors

**Practice Structure:**
- Daily: 2 hours (4 Pomodoros)
- Weekly: 10 hours
- Total: 260 hours over 26 weeks
```

#### Phase 2: Pomodoro Schedule (1 hour)

**AUTO-LINKED from Deliberate Practice:**
- Skill Components → Focus Areas
- 2 hours/day → 4 Pomodoros

```markdown
## Daily Practice Schedule

**Weekdays (Mon-Fri):**
- 6:00-6:25am: Pomodoro 1 - New concept study
- 6:30-6:55am: Pomodoro 2 - Code examples
- 7:00-7:25am: Pomodoro 3 - Problem solving
- 7:30-7:55am: Pomodoro 4 - Review & notes

**Weekends (Sat-Sun):**
- 9:00-9:25am: Pomodoro 1 - Review week's concepts
- 9:30-9:55am: Pomodoro 2 - Project work
- 10:00-10:25am: Pomodoro 3 - Project work
- 10:30-10:55am: Pomodoro 4 - Plan next week

**Weekly Theme (changes every 4 weeks):**
- Weeks 1-4: Syntax & Fundamentals
- Weeks 5-8: Data Structures
- Weeks 9-12: OOP
- Weeks 13-18: Libraries
- Weeks 19-26: Portfolio
```

#### Phase 3: Habit Loop Design (1 hour)

**AUTO-LINKED from Pomodoro:**
- 6:00am daily practice → Cue

```markdown
## Habit Loop - Daily Python Practice

**Cue (Trigger):**
- Time: 6:00am (after morning coffee)
- Location: Home office desk
- Pre-cue ritual: Open VS Code, water bottle ready

**Routine (Behavior):**
- 4 Pomodoros of focused Python practice
- No phone, no distractions
- Follow weekly theme from Deliberate Practice plan

**Reward (Positive Reinforcement):**
- Immediate: Check off daily practice in tracker
- Daily: 10-minute favorite podcast episode
- Weekly: Share progress on Twitter/LinkedIn
- Monthly: Buy new tech book or course

**Tracking:**
- Digital: Notion habit tracker
- Physical: Wall calendar with X's (don't break the chain)
- Metric: Consecutive days practiced (target: 180/182 days)
```

#### Phase 4: Recovery Protocol (1 hour)

**AUTO-LINKED from Deliberate Practice:**
- Max 2 hours/day → Intensity Limits

```markdown
## Recovery & Burnout Prevention

**Rest Days:**
- 2 days off per month (1st and 15th)
- Use for: Review progress, plan adjustments, passive learning (videos)

**Intensity Management:**
- Max 2 hours focused practice/day (4 Pomodoros)
- If mental fatigue: Switch to passive learning (tutorials)
- If frustration >30 min: Take 24-hour break

**Weekly Review (Sunday):**
- What worked this week?
- What was too hard?
- Adjust next week's difficulty

**Signs of Burnout (STOP if detected):**
- Dread opening VS Code
- Consistent frustration (>3 days)
- Skipping 3+ days in a row
- Action: Take 3-day break, revisit goals

**Deload Weeks:**
- Week 13 (after data structures)
- Week 26 (after portfolio)
- Reduce to 1 hour/day, focus on review
```

#### Phase 5: Deep Plan Integration

```markdown
## Deep Plan - Python Skill Acquisition

**L1 - Strategic Goal:**
1. Become job-ready Python developer (6 months)

**L2 - Milestones:**
1.1 Complete fundamentals (Month 1)
1.2 Master data structures (Month 2)
1.3 Understand OOP (Month 3)
1.4 Learn key libraries (Months 4-5)
1.5 Build portfolio (Month 6)

**L3 - Epics:**
1.1.1 Study syntax (Week 1-2)
1.1.2 Build 5 mini-projects (Week 3-4)
1.2.1 Solve 40 LeetCode Easy (Week 5-8)

**L4 - User Stories:**
1.1.1.1 Complete Python Crash Course Ch 1-5
1.1.1.2 Build calculator program
1.2.1.1 Solve 10 list problems

**L5 - Daily Tasks (from Habit Loop):**
- [x] 6:00am: Cue - Coffee + open VS Code
- [x] 6:00-7:55am: 4 Pomodoros (Routine)
- [x] 8:00am: Reward - Mark tracker, podcast
```

### Success Metrics

- ✅ Skill breakdown with 5 components
- ✅ Daily 2-hour practice routine established
- ✅ Habit loop with cue/reward system
- ✅ Recovery protocol prevents burnout
- ✅ 180+ consecutive practice days (target)

---

## Pattern 3: Health Transformation

**Frameworks:** HBM + Progressive Overload + Macros + NPV + Atomic Habits
**Domains:** Health + Finance + Personal
**Use Case:** Major fitness/health goal (lose 30 lbs, run marathon, build muscle)
**Total Time:** 5-7 hours
**Complexity:** High

### Integration Flow

```
Step 1: HBM (Health Belief Model) → 1.5 hours
  ↓ (auto-link: Perceived Barriers → NPV Costs)
Step 2: Progressive Overload (Training Plan) → 2 hours
  ↓ (auto-link: Weekly Progression → Deep Plan L4)
Step 3: Macros Calculation → 1 hour
  ↓ (auto-link: Daily Targets → Atomic Habits Routine)
Step 4: NPV (Financial Investment) → 1 hour
  ↓ (auto-link: Gym/Food Costs → HBM Barriers)
Step 5: Atomic Habits (Behavior Change) → 1.5 hours
  ↓ (auto-link: Tiny Habits → Deep Plan L5)
```

### Auto-Linking Rules

| Source Framework | Source Field | Target Framework | Target Field |
|------------------|--------------|------------------|--------------|
| HBM | Perceived Barriers | NPV | Costs (financial/time) |
| HBM | Cues to Action | Atomic Habits | Implementation Intention |
| Progressive Overload | Weekly Sets/Reps | Deep Plan | L4 User Stories |
| Macros | Daily Protein/Carbs/Fats | Atomic Habits | Routine |
| NPV | Total Investment | HBM | Perceived Costs |
| Atomic Habits | Habit Stack | Deep Plan | L5 Daily Tasks |

### Output Artifacts

1. **hbm-health-analysis.md** - Motivation and barriers
2. **progressive-overload-plan.md** - 12-week training program
3. **macros-nutrition-plan.md** - Daily nutrition targets
4. **npv-health-investment.md** - Financial analysis
5. **atomic-habits-system.md** - Behavior change plan
6. **workflow-plan.md** - Combined health transformation plan

### Example Workflow

**Context:** Lose 30 lbs and build muscle (male, 35, 210 lbs → 180 lbs, 6 months)

#### Phase 1: Health Belief Model (1.5 hours)

```markdown
## HBM Analysis

**Perceived Susceptibility:**
- Current: BMI 30 (obese), family history of diabetes
- Risk: High chance of Type 2 diabetes by age 45

**Perceived Severity:**
- Health: Reduced lifespan, medication dependence
- Life quality: Low energy, poor sleep, joint pain

**Perceived Benefits:**
- Health: Reduce diabetes risk by 50%
- Life: More energy, better sleep, confidence
- Long-term: Save $200k in medical costs (lifetime)

**Perceived Barriers:**
- Time: 6 hours/week for gym + meal prep
- Money: $100/month gym, $150/month extra for protein/food
- Social: Less time with friends who eat out
- Knowledge: Don't know how to lift weights properly

**Cues to Action:**
- Internal: Seeing old photos, feeling winded climbing stairs
- External: Doctor's warning at checkup
- Trigger: Set phone reminder 5:30am daily "Gym time"

**Self-Efficacy:**
- Past success: Ran 5K last year
- Support: Wife supports, will meal prep together
- Plan: Hire trainer for Month 1 (technique)
```

#### Phase 2: Progressive Overload Plan (2 hours)

**AUTO-LINKED from HBM:**
- Barrier (knowledge) → Solution: Hire trainer Month 1

```markdown
## 12-Week Progressive Overload

**Starting Stats:** 210 lbs, 28% body fat, novice lifter
**Target:** 185 lbs, 18% body fat, intermediate lifter
**Frequency:** 4 days/week (Mon/Tue/Thu/Fri)

### Weeks 1-4: Foundation Phase

**Monday/Thursday - Upper Body:**
| Exercise | Week 1 | Week 2 | Week 3 | Week 4 |
|----------|--------|--------|--------|--------|
| Bench Press | 3x8 @95lbs | 3x8 @100lbs | 3x8 @105lbs | 3x8 @110lbs |
| Rows | 3x10 @80lbs | 3x10 @85lbs | 3x10 @90lbs | 3x10 @95lbs |
| Shoulder Press | 3x10 @40lbs | 3x10 @45lbs | 3x10 @50lbs | 3x10 @55lbs |
| Bicep Curls | 3x12 @25lbs | 3x12 @30lbs | 3x12 @30lbs | 3x12 @35lbs |

**Tuesday/Friday - Lower Body:**
| Exercise | Week 1 | Week 2 | Week 3 | Week 4 |
|----------|--------|--------|--------|--------|
| Squats | 3x10 @95lbs | 3x10 @105lbs | 3x10 @115lbs | 3x10 @125lbs |
| Deadlifts | 3x8 @135lbs | 3x8 @145lbs | 3x8 @155lbs | 3x8 @165lbs |
| Lunges | 3x10/leg @25lbs | 3x10 @30lbs | 3x10 @35lbs | 3x10 @40lbs |
| Calf Raises | 3x15 BW | 3x15 BW | 3x15 @25lbs | 3x15 @25lbs |

**Progression Rule:** +5 lbs/week if all sets completed

### Weeks 5-8: Hypertrophy Phase
(Increase volume: 4 sets instead of 3, add isolation exercises)

### Weeks 9-12: Strength Phase
(Lower reps: 5x5, heavier weight, longer rest)
```

#### Phase 3: Macros Calculation (1 hour)

```markdown
## Nutrition Plan

**Current TDEE:** 2,400 calories/day (sedentary baseline)
**Activity Addition:** +400 cal/day (4 workouts/week average)
**Total Maintenance:** 2,800 cal/day

**Target for Fat Loss:**
- Deficit: 500 cal/day = 3,500 cal/week = 1 lb/week
- Daily Target: 2,300 calories
- Weekly Loss: 1 lb (conservative, sustainable)
- 6-month loss: 26 lbs (close to 30 lb goal)

**Macro Breakdown (40/30/30):**
- Protein: 40% = 920 cal = 230g (1.1g/lb for muscle retention)
- Carbs: 30% = 690 cal = 173g (fuel for workouts)
- Fats: 30% = 690 cal = 77g (hormone health)

**Daily Meal Plan:**
- Breakfast: 600 cal (4 eggs, oatmeal, berries)
- Lunch: 700 cal (chicken, rice, veggies)
- Dinner: 700 cal (salmon, sweet potato, salad)
- Snacks: 300 cal (protein shake, almonds)

**Weekly Prep:**
- Sunday: Cook 4 lbs chicken, 3 lbs rice, chop veggies
- Wednesday: Cook 2 lbs salmon, 5 sweet potatoes
```

#### Phase 4: NPV Analysis (1 hour)

**AUTO-LINKED from HBM:**
- Barriers (time/money) → NPV Costs

```markdown
## Financial Investment

**One-Time Costs:**
- Gym membership signup: $50
- Personal trainer (4 sessions): $200
- Home equipment (resistance bands, mat): $100
- **Total:** $350

**Monthly Recurring Costs:**
- Gym membership: $60/month
- Extra food (protein, veggies): $120/month
- Supplements (protein powder, creatine): $40/month
- **Total:** $220/month x 6 months = $1,320

**Total 6-Month Investment:** $1,670

**Benefits (NPV Calculation):**
- Avoided medical costs (diabetes prevention): $5,000/year x 20 years = $100,000 (discounted)
- Increased productivity (more energy): +2 hours/week x $50/hour = $5,200/year
- Reduced sick days: 3 fewer days/year x $400/day = $1,200/year

**NPV (10-year horizon, 5% discount):**
NPV = -$1,670 + Σ($6,400/year / 1.05^t) = +$47,800

**Decision:** INVEST - Positive NPV, payback in <4 months
```

#### Phase 5: Atomic Habits System (1.5 hours)

**AUTO-LINKED from Macros + Progressive Overload:**
- Daily nutrition targets → Habit Stack
- 4 workouts/week → Implementation Intentions

```markdown
## Atomic Habits - Health Transformation

### Habit Stack 1: Morning Workout

**Anchor Habit:** Wake up at 5:30am (already doing)

**Tiny Habits (1% improvements):**
1. After I wake up, I will drink 16oz water (hydration)
2. After I drink water, I will put on gym clothes
3. After I put on gym clothes, I will drive to gym (remove friction)
4. After I arrive at gym, I will start with 5-min warmup

**Implementation Intention:**
"On Monday/Tuesday/Thursday/Friday, when my alarm rings at 5:30am, I will immediately drink water and put on gym clothes that I laid out the night before."

### Habit Stack 2: Evening Meal Prep

**Anchor Habit:** Dinner at 6:30pm (already doing)

**Tiny Habits:**
1. After I finish dinner, I will pack tomorrow's lunch (5 min)
2. After I pack lunch, I will prep breakfast (2 eggs in bowl)
3. After I prep breakfast, I will set out gym clothes

### Environment Design

**Make Good Habits Obvious:**
- Gym bag by front door (night before)
- Protein powder on kitchen counter
- Meal prep containers visible in fridge

**Make Bad Habits Invisible:**
- No junk food in house
- Unfollow food Instagram accounts
- Delete food delivery apps

### Habit Tracking

**Daily Checklist:**
- [ ] 5:30am wake-up
- [ ] Gym workout completed
- [ ] Hit macro targets (230P/173C/77F)
- [ ] 8 hours sleep

**Weekly Review (Sunday):**
- Workouts completed: ___ / 4
- Days hit macros: ___ / 7
- Weight change: -___ lbs
- Progress photos: Yes/No
```

#### Phase 6: Deep Plan Integration

```markdown
## Deep Plan - Health Transformation

**L1 - Strategic Goal:**
1. Transform health: 210 → 180 lbs, 28% → 18% body fat (6 months)

**L2 - Milestones:**
1.1 Lose 10 lbs + master form (Month 1-2)
1.2 Lose 10 lbs + build strength (Month 3-4)
1.3 Lose 10 lbs + optimize body comp (Month 5-6)

**L3 - Epics (from Progressive Overload phases):**
1.1.1 Complete Foundation Phase (Weeks 1-4)
1.2.1 Complete Hypertrophy Phase (Weeks 5-8)
1.3.1 Complete Strength Phase (Weeks 9-12)

**L4 - User Stories (from Weekly Workouts):**
1.1.1.1 Week 1 Monday - Upper body (3x8 bench @95lbs)
1.1.1.2 Week 1 Tuesday - Lower body (3x10 squats @95lbs)
1.1.1.3 Week 1 Thursday - Upper body
1.1.1.4 Week 1 Friday - Lower body

**L5 - Daily Tasks (from Atomic Habits):**
- [ ] 5:30am: Wake up, drink water
- [ ] 5:35am: Put on gym clothes
- [ ] 5:45am: Drive to gym
- [ ] 6:00-7:00am: Workout (Progressive Overload plan)
- [ ] 7:30am: Log workout + macros in app
- [ ] 6:30pm: Meal prep for tomorrow
```

### Success Metrics

- ✅ HBM addresses motivation and barriers
- ✅ Progressive Overload provides structured training
- ✅ Macros ensure proper nutrition
- ✅ NPV confirms financial viability (+$47k)
- ✅ Atomic Habits makes behaviors sustainable
- ✅ All frameworks auto-linked into unified plan

---

## Pattern 4: Investment Decision

**Frameworks:** NPV + DCF + Monte Carlo + Real Options + SWOT
**Domains:** Finance + Business
**Use Case:** Major investment (rental property, business acquisition, equity)
**Total Time:** 6-10 hours
**Complexity:** Very High

### Integration Flow

```
Step 1: SWOT (Qualitative Analysis) → 1.5 hours
  ↓ (auto-link: Opportunities/Threats → Monte Carlo Scenarios)
Step 2: DCF (Valuation) → 2 hours
  ↓ (auto-link: Free Cash Flows → NPV Calculation)
Step 3: NPV (Decision Criteria) → 1 hour
  ↓ (auto-link: NPV Result → Real Options Decision Tree)
Step 4: Monte Carlo (Risk Analysis) → 2 hours
  ↓ (auto-link: Probability Distributions → Real Options)
Step 5: Real Options (Flexibility Value) → 1.5 hours
```

### Auto-Linking Rules

| Source Framework | Source Field | Target Framework | Target Field |
|------------------|--------------|------------------|--------------|
| SWOT | Opportunities | Monte Carlo | Best-Case Scenario |
| SWOT | Threats | Monte Carlo | Worst-Case Scenario |
| DCF | Free Cash Flows | NPV | Cash Flow Inputs |
| DCF | WACC | NPV | Discount Rate |
| NPV | Net Present Value | Real Options | Exercise Decision |
| Monte Carlo | Probability Dist | Real Options | Volatility Input |
| Real Options | Option Value | NPV | Total Value (NPV + option) |

### Output Artifacts

1. **swot-qualitative-analysis.md**
2. **dcf-valuation-model.md**
3. **npv-investment-decision.md**
4. **monte-carlo-risk-analysis.md**
5. **real-options-flexibility-value.md**
6. **workflow-plan.md** - Combined investment analysis

### Example Workflow

**Context:** Buying rental property ($300k purchase, evaluating over 10 years)

#### Phase 1: SWOT Analysis (1.5 hours)

```markdown
## SWOT - Rental Property Investment

**Strengths:**
- Location: Near university (stable tenant demand)
- Property: 3-bed/2-bath, good condition (minimal repairs)
- Market: Property values up 5%/year last 5 years
- Cashflow: Positive from Day 1 ($400/month after expenses)

**Weaknesses:**
- High leverage: 20% down ($60k), 80% mortgage
- Illiquidity: Takes 3-6 months to sell
- Management: Need property manager (10% of rent)
- Concentration: Single property (no diversification)

**Opportunities:**
- Appreciation: Market projected 4%/year next 10 years
- Rent growth: 3%/year (historically consistent)
- Tax benefits: Depreciation, mortgage interest deduction
- Future: Could refinance to buy 2nd property (Year 5)

**Threats:**
- Interest rate risk: If rates rise, property values fall
- Vacancy risk: 1-2 month vacancy/year possible
- Maintenance: Roof ($10k), HVAC ($5k) may need replacement
- Market downturn: 2008-style crash could reduce value 30%
- Regulatory: Rent control laws could limit increases
```

#### Phase 2: DCF Valuation (2 hours)

**AUTO-LINKED from SWOT:**
- Opportunities (appreciation, rent growth) → DCF projections

```markdown
## DCF Model - 10-Year Rental Property

**Assumptions:**
- Purchase Price: $300,000
- Down Payment: $60,000 (20%)
- Mortgage: $240,000 @ 6.5% (30-year fixed)
- Monthly Mortgage: $1,517
- Initial Rent: $2,500/month
- Rent Growth: 3%/year
- Property Appreciation: 4%/year
- Operating Expenses: 40% of rent (incl. property mgmt, taxes, insurance, maintenance)
- WACC (Discount Rate): 10% (opportunity cost)

**Annual Cash Flow Projection:**

| Year | Rent | Expenses | Mortgage | Net Cash Flow | Property Value |
|------|------|----------|----------|---------------|----------------|
| 1 | $30,000 | $12,000 | $18,204 | -$204 | $312,000 |
| 2 | $30,900 | $12,360 | $18,204 | $336 | $324,480 |
| 3 | $31,827 | $12,731 | $18,204 | $892 | $337,459 |
| 5 | $33,782 | $13,513 | $18,204 | $2,065 | $365,349 |
| 10 | $39,316 | $15,726 | $18,204 | $5,386 | $444,074 |

**Terminal Value (Year 10):**
- Property Sale: $444,074
- Mortgage Balance: $198,623
- Net Proceeds: $245,451

**DCF Calculation:**
PV(Cash Flows) = Σ(CF_t / (1+0.10)^t)
PV(Terminal Value) = $245,451 / (1.10)^10 = $94,684
Total PV = $94,684 + $15,234 (sum of annual CFs) = $109,918

**Fair Value:** $109,918 (present value of future cash flows)
```

#### Phase 3: NPV Decision (1 hour)

**AUTO-LINKED from DCF:**
- Free Cash Flows → NPV inputs

```markdown
## NPV Analysis

**Initial Investment:** -$60,000 (down payment)

**Cash Flows (from DCF):**
- Years 1-10: Annual net cash flows
- Year 10: + Terminal value ($245,451)

**NPV Calculation:**
NPV = -$60,000 + Σ(CF_t / (1+0.10)^t)
NPV = -$60,000 + $109,918
NPV = $49,918

**Decision Criteria:**
- NPV > 0? ✅ YES ($49,918 positive)
- IRR: 15.2% (higher than 10% WACC) ✅
- Payback Period: 8.3 years (acceptable for real estate) ✅

**Preliminary Decision:** INVEST (positive NPV)

**But wait - need to assess RISK with Monte Carlo...**
```

#### Phase 4: Monte Carlo Risk Analysis (2 hours)

**AUTO-LINKED from SWOT:**
- Threats → Monte Carlo worst-case
- Opportunities → Monte Carlo best-case

```markdown
## Monte Carlo Simulation (10,000 iterations)

**Variable Inputs (with uncertainty):**
1. **Rent Growth:** Normal(μ=3%, σ=2%)
   - Best case: 7%/year
   - Worst case: -1%/year
2. **Property Appreciation:** Normal(μ=4%, σ=3%)
   - Best case: 10%/year
   - Worst case: -2%/year
3. **Vacancy Rate:** Uniform(0%, 10%)
4. **Major Repairs:** Poisson(λ=1 event/5 years, $10k each)
5. **Interest Rate (refi opportunity):** Normal(μ=6.5%, σ=1.5%)

**Output Distribution (NPV):**
- Mean NPV: $48,200 (close to base case $49,918)
- Median NPV: $51,300
- Std Dev: $35,000 (high volatility)
- 5th Percentile (worst 5%): -$12,000 (LOSS)
- 95th Percentile (best 5%): $125,000

**Risk Metrics:**
- Probability NPV > 0: 82% ✅ (good)
- Probability NPV > $50k: 48%
- Probability Loss > $20k: 8% ⚠️ (moderate risk)

**Key Insights:**
- 18% chance of losing money (negative NPV)
- If things go well (top 25%): NPV >$80k
- If things go badly (bottom 25%): NPV <$15k or negative
- Biggest risk: Market downturn (appreciation <0%)
```

#### Phase 5: Real Options Analysis (1.5 hours)

**AUTO-LINKED from NPV + Monte Carlo:**
- NPV result → Exercise decision
- Monte Carlo volatility → Option value

```markdown
## Real Options - Flexibility Value

**Option 1: Refinance Option (Year 5)**
- If interest rates drop to <5%, refinance mortgage
- Savings: ~$300/month (lower payment)
- PV of savings: $15,000
- Probability: 35% (from Monte Carlo)
- Option Value: $5,250

**Option 2: Expand Option (Year 5)**
- If property value > $380k, cash-out refinance
- Extract $50k equity to buy 2nd property
- Creates growth option (compound returns)
- Probability: 45%
- Option Value: $12,000 (estimated from 2nd property NPV)

**Option 3: Abandon Option (Any Year)**
- If market crashes, can sell property
- Loss limited to equity invested ($60k max)
- Put option value: $8,000 (insurance against catastrophic loss)

**Total Real Options Value:** $25,250

**Adjusted NPV:**
Base NPV: $49,918
+ Real Options: $25,250
**Total Strategic Value: $75,168** ✅

**Final Decision:** INVEST - Even with risk, total value is strong
```

#### Phase 6: Deep Plan Integration

```markdown
## Deep Plan - Real Estate Investment

**L1 - Strategic Goal:**
1. Acquire rental property for long-term wealth building (10-year hold)

**L2 - Milestones:**
1.1 Complete due diligence (Month 1)
1.2 Close on property (Month 2)
1.3 Stabilize operations (Months 3-6)
1.4 Optimize cashflow (Years 2-4)
1.5 Execute refinance/expand (Year 5)
1.6 Exit or scale (Year 10)

**L3 - Epics:**
1.1.1 Financial analysis (this doc)
1.1.2 Property inspection
1.1.3 Legal review (title, zoning)
1.2.1 Secure financing
1.2.2 Close transaction

**L4 - User Stories:**
1.1.1.1 Complete SWOT analysis
1.1.1.2 Build DCF model
1.1.1.3 Run Monte Carlo simulation
1.1.1.4 Calculate real options value

**L5 - Tasks:**
- [x] Phase 1: SWOT (1.5 hours)
- [x] Phase 2: DCF (2 hours)
- [x] Phase 3: NPV (1 hour)
- [x] Phase 4: Monte Carlo (2 hours)
- [x] Phase 5: Real Options (1.5 hours)
- [ ] Next: Schedule property inspection
```

### Success Metrics

- ✅ SWOT identifies key qualitative factors
- ✅ DCF provides rigorous valuation
- ✅ NPV shows positive return ($49k)
- ✅ Monte Carlo quantifies risk (82% success probability)
- ✅ Real Options adds $25k value (flexibility)
- ✅ Total strategic value: $75k (strong investment)

---

## Pattern 5: Career Change

**Frameworks:** SWOT + Growth Mindset + Deliberate Practice + NPV
**Domains:** Business + Personal + Finance
**Use Case:** Career transition, upskilling, job change
**Total Time:** 8-12 hours
**Complexity:** High

### Integration Flow

```
Step 1: SWOT (Career Assessment) → 2 hours
  ↓ (auto-link: Weaknesses → Growth Mindset Learning Goals)
Step 2: Growth Mindset (Mindset Shift) → 2 hours
  ↓ (auto-link: Fixed→Growth beliefs → Deliberate Practice)
Step 3: Deliberate Practice (Skill Building) → 3 hours
  ↓ (auto-link: Practice Plan → NPV Time Investment)
Step 4: NPV (Financial Analysis) → 2 hours
  ↓ (auto-link: Salary Increase → NPV Benefits)
Step 5: Deep Plan Integration → 1 hour
```

### Auto-Linking Rules

| Source Framework | Source Field | Target Framework | Target Field |
|------------------|--------------|------------------|--------------|
| SWOT | Weaknesses (skill gaps) | Growth Mindset | Learning challenges |
| SWOT | Opportunities | NPV | Future salary (benefits) |
| Growth Mindset | Fixed→Growth statements | Deliberate Practice | Motivation |
| Deliberate Practice | Time required | NPV | Time cost (opportunity cost) |
| NPV | Education costs | SWOT | Threats (financial risk) |
| NPV | Salary increase | Deep Plan | L1 Goal (financial outcome) |

### Output Artifacts

1. **swot-career-assessment.md**
2. **growth-mindset-transformation.md**
3. **deliberate-practice-skill-plan.md**
4. **npv-career-change-analysis.md**
5. **workflow-plan.md** - Combined career transition plan

### Example Workflow

**Context:** Transitioning from marketing manager → data analyst (9-month plan)

#### Phase 1: SWOT Career Assessment (2 hours)

```markdown
## SWOT - Career Change Analysis

**Strengths:**
- Domain knowledge: 8 years marketing (customer behavior, campaigns)
- Communication: Strong presentation and stakeholder management
- Business acumen: Understand metrics, ROI, strategy
- Learning ability: Self-taught Excel, Google Analytics

**Weaknesses (Skill Gaps):**
- Technical: No Python, SQL, or R experience
- Statistics: Limited understanding of regression, hypothesis testing
- Tools: Never used Tableau, PowerBI, Jupyter
- Experience: No portfolio of data projects

**Opportunities:**
- Demand: Data analyst roles up 30% YoY in my city
- Salary: $85k → $105k potential (24% increase)
- Remote work: 60% of data roles are remote (flexibility)
- Transferable skills: Marketing domain knowledge is valuable for analytics roles
- Internal: My company has open data analyst position

**Threats:**
- Competition: New grads with CS degrees
- Time: 15-20 hours/week for 9 months while working full-time
- Financial: $3k bootcamp cost + opportunity cost
- Impostor syndrome: Feeling behind compared to technical peers
- Failure: What if I spend 9 months and don't get hired?
```

#### Phase 2: Growth Mindset Transformation (2 hours)

**AUTO-LINKED from SWOT:**
- Weaknesses (skill gaps) → Growth mindset learning challenges
- Threats (impostor syndrome) → Fixed→Growth reframe

```markdown
## Growth Mindset - Career Transition

**Fixed Mindset Beliefs (OLD):**
1. "I'm not a math person" → I struggled with stats in college
2. "I'm too old to learn coding" → I'm 32, should've started younger
3. "Real programmers have CS degrees" → I'll never be technical enough
4. "If I fail, it proves I wasn't meant for this" → Failure is permanent

**Growth Mindset Reframes (NEW):**
1. "I can learn math with practice" → Stats is a skill, not innate talent
   - Evidence: I learned Excel formulas, Google Analytics (both technical)
   - Action: 30 min/day on Khan Academy Statistics
2. "Age is irrelevant; effort matters" → Many career changers start at 30+
   - Evidence: Reddit r/datascience has hundreds of success stories 30+
   - Action: Join "Data Career Changers" community for support
3. "I bring unique value" → Marketing domain knowledge is rare in data roles
   - Evidence: Job posts explicitly want "business acumen + technical skills"
   - Action: Frame my marketing experience as strength in interviews
4. "Failure is feedback" → If I don't get hired in 9 months, I'll adjust strategy
   - Evidence: First job search might take 50-100 applications
   - Action: Treat rejections as data points, iterate on resume/projects

**Mantras (Daily Affirmations):**
- "Every expert was once a beginner"
- "Struggle means I'm learning, not failing"
- "My marketing background is an asset, not a liability"

**Tracking Progress (Weekly):**
- What did I learn this week that I couldn't do before?
- What mistake did I make that taught me something?
- How did I handle frustration? (Rate 1-10, track improvement)
```

#### Phase 3: Deliberate Practice Plan (3 hours)

**AUTO-LINKED from Growth Mindset:**
- Growth beliefs → Motivation for practice

```markdown
## Deliberate Practice - Data Analyst Skills (9 months)

**Current Level:** Marketing professional, novice in data analysis
**Target Level:** Job-ready junior data analyst
**Timeline:** 9 months (39 weeks)
**Weekly Commitment:** 15 hours (10 hours learning + 5 hours projects)

### Phase 1: Foundations (Months 1-3, 12 weeks)

**Skills:**
1. **SQL** (Weeks 1-4, 40 hours)
   - SELECT, WHERE, JOIN, GROUP BY, subqueries
   - Practice: 100 problems on SQLZoo, HackerRank
   - Feedback: Solutions must pass automated tests
2. **Python Basics** (Weeks 5-8, 40 hours)
   - Variables, loops, functions, pandas, numpy
   - Practice: Python for Data Analysis book + exercises
   - Feedback: Code review from mentor (find on Reddit)
3. **Statistics** (Weeks 9-12, 40 hours)
   - Descriptive stats, probability, distributions, hypothesis testing
   - Practice: Khan Academy + "Statistics for Business" course
   - Feedback: Weekly quizzes (target >80%)

### Phase 2: Intermediate (Months 4-6, 12 weeks)

**Skills:**
1. **Data Visualization** (Weeks 13-16, 40 hours)
   - Tableau, matplotlib, seaborn
   - Practice: Recreate 20 visualizations from FiveThirtyEight
   - Feedback: Post on r/dataisbeautiful for critique
2. **Advanced SQL** (Weeks 17-20, 40 hours)
   - Window functions, CTEs, performance optimization
   - Practice: LeetCode SQL (50 medium problems)
   - Feedback: Compare my solution to "best solution" (learn efficiency)
3. **Regression & ML Basics** (Weeks 21-24, 40 hours)
   - Linear/logistic regression, decision trees
   - Practice: scikit-learn tutorials + 3 kaggle competitions (beginner)
   - Feedback: Compare my score to benchmark (aim for top 50%)

### Phase 3: Portfolio (Months 7-9, 15 weeks)

**Projects (to showcase on resume):**
1. **Marketing Campaign Analysis** (Weeks 25-29, 50 hours)
   - Use SQL to extract campaign data from sample DB
   - Python to analyze conversion rates, segment customers
   - Tableau dashboard to present findings
   - Feedback: Mock presentation to mentor
2. **Customer Churn Prediction** (Weeks 30-34, 50 hours)
   - Build logistic regression model to predict churn
   - Feature engineering, model evaluation (AUC, precision/recall)
   - Document in Jupyter notebook + GitHub
   - Feedback: Share on LinkedIn, tag data professionals for input
3. **A/B Test Analysis** (Weeks 35-39, 50 hours)
   - Design mock A/B test, collect sample data
   - Hypothesis testing (t-test, chi-square)
   - Present business recommendation
   - Feedback: Practice with marketing team (internal)

**Total Practice Time:** ~550 hours over 9 months
```

#### Phase 4: NPV Financial Analysis (2 hours)

**AUTO-LINKED from Deliberate Practice:**
- 550 hours → NPV time cost
- Skills acquired → SWOT opportunities (salary)

```markdown
## NPV - Career Change Investment

**Costs:**

**1. Education Costs (Financial):**
- Bootcamp (optional): $3,000
- Books/courses: $500
- Computer upgrade: $1,000
- Total: $4,500

**2. Time Costs (Opportunity Cost):**
- Hours invested: 550 hours (15 hours/week x 39 weeks)
- Hourly value: $45/hour (current salary $75k/year ÷ 2000 hours)
- Opportunity cost: 550 x $45 = $24,750
- Total: $24,750

**Total Investment:** $29,250 (financial + time)

**Benefits:**

**1. Salary Increase:**
- Current: $75,000/year (marketing manager)
- Target: $95,000/year (junior data analyst)
- Increase: $20,000/year

**2. Future Growth:**
- Year 1: $95k (junior)
- Year 3: $115k (mid-level, +$20k)
- Year 5: $140k (senior, +$25k)
- Year 10: $180k (lead/manager, +$40k)

**3. Other Benefits:**
- Remote work: Save $3k/year commute costs
- Job security: Data roles less affected by automation
- Satisfaction: Better alignment with interests (quantitative work)

**NPV Calculation (10-year horizon, 5% discount rate):**

| Year | Salary Increase | Commute Savings | Total Benefit | PV (5%) |
|------|------------------|-----------------|---------------|---------|
| 0 | $0 | $0 | -$29,250 | -$29,250 |
| 1 | $20,000 | $3,000 | $23,000 | $21,905 |
| 2 | $20,000 | $3,000 | $23,000 | $20,862 |
| 3 | $40,000 | $3,000 | $43,000 | $37,144 |
| 5 | $65,000 | $3,000 | $68,000 | $53,263 |
| 10 | $105,000 | $3,000 | $108,000 | $66,311 |

**NPV (10 years) = $312,450**

**IRR = 68%** (extremely high return on investment)

**Payback Period:** 1.3 years (break even after 15 months in new role)

**Decision:** INVEST - Massive positive NPV, life-changing return
```

#### Phase 5: Deep Plan Integration (1 hour)

```markdown
## Deep Plan - Career Change to Data Analyst

**L1 - Strategic Goal:**
1. Transition from marketing manager → data analyst (9 months)

**L2 - Milestones:**
1.1 Complete foundations (Month 1-3): SQL, Python, Statistics
1.2 Build intermediate skills (Month 4-6): Visualization, ML
1.3 Create portfolio (Month 7-9): 3 projects
1.4 Land job offer (Month 9-10)

**L3 - Epics (from Deliberate Practice phases):**
1.1.1 Master SQL (Weeks 1-4)
1.1.2 Learn Python basics (Weeks 5-8)
1.1.3 Study statistics (Weeks 9-12)
1.2.1 Build visualizations (Weeks 13-16)
1.2.2 Advanced SQL (Weeks 17-20)
1.2.3 ML fundamentals (Weeks 21-24)
1.3.1 Project 1: Marketing analysis (Weeks 25-29)
1.3.2 Project 2: Churn prediction (Weeks 30-34)
1.3.3 Project 3: A/B testing (Weeks 35-39)

**L4 - User Stories (Weekly):**
1.1.1.1 Week 1: Complete SQLZoo tutorials 1-5
1.1.1.2 Week 2: Solve 25 SQL problems on HackerRank
1.1.1.3 Week 3: Build sample database + 10 queries
1.1.1.4 Week 4: Mock interview (SQL questions)

**L5 - Daily Tasks (from Growth Mindset + Practice Plan):**
- [ ] 6:00-6:30am: Morning mantra + review yesterday's learning
- [ ] 6:30-8:00am: Study session (1.5 hours)
- [ ] 12:00-12:30pm: Lunch learning (30 min video/reading)
- [ ] 8:00-9:00pm: Practice problems (1 hour)
- [ ] 9:00-9:30pm: Reflect + plan tomorrow (journal)
```

### Success Metrics

- ✅ SWOT identifies skill gaps and opportunities
- ✅ Growth Mindset addresses impostor syndrome
- ✅ Deliberate Practice provides 550-hour roadmap
- ✅ NPV shows $312k return (68% IRR)
- ✅ Deep Plan translates into executable weekly/daily tasks

---

## Pattern 6: Product Development

**Frameworks:** Lean Canvas + OKRs + TRIZ + Deliberate Practice
**Domains:** Business + Personal
**Use Case:** Building new product, feature, or solving complex problem
**Total Time:** 10-15 hours
**Complexity:** Very High

### Integration Flow

```
Step 1: Lean Canvas (Product-Market Fit) → 3 hours
  ↓ (auto-link: Problem → TRIZ Contradiction)
Step 2: TRIZ (Innovation) → 3 hours
  ↓ (auto-link: Solution Patterns → OKRs)
Step 3: OKRs (Goals & Metrics) → 2 hours
  ↓ (auto-link: Key Results → Deliberate Practice)
Step 4: Deliberate Practice (Skill Building) → 2 hours
  ↓ (auto-link: Practice Plan → Deep Plan L4/L5)
```

### Auto-Linking Rules

| Source Framework | Source Field | Target Framework | Target Field |
|------------------|--------------|------------------|--------------|
| Lean Canvas | Problem | TRIZ | Contradiction |
| TRIZ | 40 Principles | Lean Canvas | Solution |
| Lean Canvas | Key Metrics | OKRs | Key Results |
| OKRs | Objectives | Deep Plan | L1 Strategic Goals |
| OKRs | Key Results | Deliberate Practice | Skill Requirements |
| Deliberate Practice | Components | Deep Plan | L4 User Stories |

### Output Artifacts

1. **lean-canvas-product.md**
2. **triz-innovation-analysis.md**
3. **okrs-product-goals.md**
4. **deliberate-practice-skills.md**
5. **workflow-plan.md** - Product development roadmap

---

## Pattern 7: Habit Stack

**Frameworks:** Habit Loop + Atomic Habits + Pomodoro + Recovery
**Domains:** Health + Personal
**Use Case:** Building multiple habits simultaneously
**Total Time:** 3-4 hours
**Complexity:** Medium

### Integration Flow

```
Step 1: Habit Loop (Core Habit Design) → 1 hour
Step 2: Atomic Habits (Tiny Habits + Environment) → 1 hour
Step 3: Pomodoro (Time Blocking) → 30 min
Step 4: Recovery (Prevent Burnout) → 30 min
```

---

## Pattern 8: Business Optimization

**Frameworks:** SWOT + Porter's 5 Forces + OKRs + NPV + TRIZ
**Domains:** Business + Finance
**Use Case:** Improving existing business performance
**Total Time:** 8-12 hours
**Complexity:** Very High

---

## Pattern 9: Financial Independence Plan

**Frameworks:** NPV + Monte Carlo + Kelly Criterion + GTD + Atomic Habits
**Domains:** Finance + Personal
**Use Case:** Long-term financial goals (FIRE, retirement, wealth building)
**Total Time:** 10-15 hours
**Complexity:** Very High

---

## Pattern 10: Learning Productivity System

**Frameworks:** GTD + Pomodoro + Deliberate Practice + Eisenhower Matrix + Growth Mindset
**Domains:** Personal
**Use Case:** Personal productivity overhaul, time management mastery
**Total Time:** 6-8 hours
**Complexity:** High

---

## Auto-Composition Logic

**When Life OS detects multiple frameworks, it will auto-compose if:**

1. **Frameworks from different domains**
   - Example: Business (Lean Canvas) + Finance (NPV) + Personal (Pomodoro)

2. **Clear synergy exists**
   - Check `framework-synergy-matrix.csv` for synergy score >7/10
   - Example: Deliberate Practice + Habit Loop (score: 9/10)

3. **User confirms composition**
   - "I want to launch a startup" → Suggests Pattern 1 (4 frameworks)
   - User accepts → Auto-loads all 4 templates with linking rules

### Auto-Linking Implementation

**Format:**
```yaml
auto_links:
  - source_framework: "Lean Canvas"
    source_field: "Revenue Streams"
    target_framework: "NPV"
    target_field: "Cash Inflows"
    transform: "currency"  # Data type conversion if needed

  - source_framework: "OKRs"
    source_field: "Objectives"
    target_framework: "Deep Plan"
    target_field: "L1 Strategic Goals"
    transform: "text"
```

**Execution:**
When Step 5 (NPV) is reached:
1. Life OS checks if Step 1 (Lean Canvas) was completed
2. Extracts "Revenue Streams" value: "$2,900/month"
3. Auto-populates NPV template field "Cash Inflows" with "$2,900"
4. Flags field as [AUTO-LINKED] for user review

### Memory Integration

**Store successful compositions for reuse:**

```bash
# After completing Pattern 1 (Startup Launch)
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "template-compositions:startup-launch:success" \
  --content "{
    pattern: 'Startup Launch',
    frameworks: ['Lean Canvas', 'NPV', 'OKRs', 'Pomodoro'],
    duration: '9.5 hours',
    auto_link_success_rate: '100%',
    user_satisfaction: 9/10,
    outcome: 'NPV=$142k, clear execution plan',
    lessons: 'NPV calculation motivated by Lean Canvas revenue projection'
  }"
```

**Retrieve for future use:**

```bash
# When user says "I'm launching a startup"
npx claude-flow@v3alpha memory search -q "startup launch composition"

# Returns: Pattern 1 with historical success data
# Life OS suggests: "I found a 4-framework composition used successfully before. Use it?"
```

---

## Usage Guidelines

### When to Use Composition Patterns

**Use when:**
- Project spans multiple life domains (business + health + finance)
- Complexity requires multiple frameworks (>2)
- Clear synergy between frameworks (check synergy matrix)
- Time available: 3+ hours for planning

**Don't use when:**
- Simple single-domain task (just use one framework)
- Time constrained (<2 hours)
- Frameworks have low synergy (<5/10)

### How to Choose Pattern

**Decision Tree:**

```
1. What's the primary goal?
   - Launch business → Pattern 1 (Startup Launch)
   - Learn skill → Pattern 2 (Skill Acquisition)
   - Improve health → Pattern 3 (Health Transformation)
   - Make investment → Pattern 4 (Investment Decision)
   - Change career → Pattern 5 (Career Change)
   - Build product → Pattern 6 (Product Development)
   - Build habits → Pattern 7 (Habit Stack)
   - Optimize business → Pattern 8 (Business Optimization)
   - Plan retirement → Pattern 9 (Financial Independence)
   - Fix productivity → Pattern 10 (Learning Productivity)

2. How many domains involved?
   - 1 domain → Single framework (not composition)
   - 2 domains → Patterns 2, 7
   - 3+ domains → Patterns 1, 3, 4, 5, 6, 8, 9, 10

3. What's time available?
   - 3-4 hours → Patterns 2, 7
   - 5-8 hours → Patterns 3, 5, 10
   - 8-12 hours → Patterns 1, 4, 8
   - 10-15 hours → Patterns 4, 6, 9
```

### Customizing Patterns

**Users can:**
1. Remove optional frameworks
   - Example: Pattern 1 without Pomodoro (reduce to 6-9 hours)
2. Add frameworks
   - Example: Pattern 2 + NPV (evaluate bootcamp cost)
3. Modify auto-linking rules
   - Example: Change NPV discount rate based on personal risk tolerance

---

## Integration with Life OS

**Step-by-Step Usage:**

1. **User starts idea collection (Step 1)**
   - Mentions keywords: "startup", "investment", "learn Python"

2. **Step 2 (Roles Discovery) suggests composition**
   - "Detected: Startup launch. Recommend Pattern 1 (4 frameworks, 8-12 hours). Proceed?"

3. **User accepts → Auto-loads frameworks**
   - Lean Canvas → NPV → OKRs → Pomodoro
   - Auto-linking rules configured

4. **User completes each framework step-by-step**
   - As each completes, auto-linked fields populate next framework

5. **Step 8 (Deep Plan) generates unified plan**
   - All frameworks merged into single workflow-plan.md
   - L1-L5 hierarchy with cross-framework integration

6. **Memory stores composition success**
   - For future reuse across all projects (global memory)

---

## Conclusion

These 10 composition patterns provide proven combinations for complex multi-domain projects. Auto-linking rules ensure seamless data flow between frameworks, and memory integration enables continuous improvement across all projects.

**Next Steps:**
1. Implement auto-linking logic in Life OS Step 8 (Deep Plan)
2. Build synergy detection from framework-synergy-matrix.csv
3. Add pattern suggestion to Step 2 (Roles Discovery)
4. Test each pattern with real user scenarios

---

**Related Documents:**
- domain-template-architecture.md (defines 10 patterns)
- framework-synergy-matrix.csv (synergy scores)
- deep-plan-templates.md (L1-L5 structure)
- template-integration-guide.md (how to build templates)
