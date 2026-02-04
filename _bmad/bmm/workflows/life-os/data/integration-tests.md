# Life OS Integration Tests

**Purpose:** Verify all components work together correctly across the entire Life OS workflow system.

**Version:** 1.0
**Last Updated:** 2026-02-04
**Total Tests:** 47
**Estimated Run Time:** 45-60 minutes (full suite)

---

## Test Suite 1: End-to-End Workflow

### Test 1.1: Simple Project (Health Domain)

**Scenario:** Build daily exercise habit

**Expected Total Time:** 25-35 minutes

**Steps:**

#### 1. Step 1: Collect Idea
- **Input:** "I want to exercise daily"
- **Expected:** Design Thinking questions appear
- **Verify:** Workflow plan initialized at `.bmad/current-workflow.md`
- **Assertions:**
  - ✅ Workflow plan file exists
  - ✅ Project name extracted: "Daily Exercise Habit"
  - ✅ Domain detected: "health"
  - ✅ Design Thinking questions (5W1H) rendered

#### 2. Step 2: Roles Discovery
- **Expected:** Health specialists auto-detected from `roles-base-enhanced.csv`
- **Verify:** Fitness Coach, Habit Specialist, Nutritionist in list
- **Assertions:**
  - ✅ At least 3 health-domain specialists returned
  - ✅ Each specialist has: name, domain, expertise, matching_score >70%
  - ✅ Results saved to memory: `shared-knowledge:roles:health:specialists`

#### 3. Step 3: Specialist Match
- **Expected:** 2-3 specialists selected based on project needs
- **Verify:** Roles saved to workflow plan
- **Assertions:**
  - ✅ Specialists list in workflow plan (YAML frontmatter)
  - ✅ Each specialist has clear role description
  - ✅ Total specialists: 2-4 (optimal consilium size)

#### 4. Step 4: Consilium
- **Expected:** Six Hats auto-assigned
- **Verify:** Each specialist has hat color
- **Assertions:**
  - ✅ White Hat (data): Fitness Coach
  - ✅ Red Hat (emotion): Habit Specialist
  - ✅ Yellow Hat (optimism): Nutritionist
  - ✅ Auto-suggest framework: "Habit Loop" (confidence >80%)
  - ✅ Consilium recommendations section complete

#### 5. Step 5: Scoring
- **Expected:** Health-specific criteria added
- **Verify:** Readiness (HBM) and Sustainability criteria present
- **Assertions:**
  - ✅ 7 criteria total (Impact, Confidence, Effort, Strategic Alignment, Risk, Readiness, Sustainability)
  - ✅ Weights sum to 1.0
  - ✅ MCDA score calculated: ≥6.5 (PASS gate)
  - ✅ Decision: PROCEED

#### 6. Step 6: Integration
- **Expected:** Strategic bucket assigned
- **Verify:** "Health & Wellness" bucket, WIP check
- **Assertions:**
  - ✅ Bucket: "Health & Wellness"
  - ✅ WIP capacity: 2/3 available (PASS)
  - ✅ Timeline allocated: 30 days (habit formation)
  - ✅ Project added to portfolio tracking

#### 7. Step 7: Calendar Sync
- **Expected:** Time blocks created
- **Verify:** Daily 7:00 AM slot
- **Assertions:**
  - ✅ Calendar event created: "Daily Exercise" @ 7:00 AM
  - ✅ Recurring: Daily for 30 days
  - ✅ Reminder: 15 minutes before
  - ✅ Linked to project in workflow plan

#### 8. Step 8: Deep Plan
- **Expected:** L1-L6 structure
- **Verify:** L1 mission, L2 phases (Foundation/Solidification/Automation)
- **Assertions:**
  - ✅ L1 Mission: Clear purpose statement
  - ✅ L2 Phases: 3 phases (Foundation, Solidification, Automation)
  - ✅ L3 Milestones: At least 2 per phase
  - ✅ L4 Tasks: At least 5 tasks per milestone
  - ✅ L5 RACI: ≥70% coverage
  - ✅ L6 Metrics: KPIs defined
  - ✅ Quality Gate check: PASS

#### 9. Step 9: Templates
- **Expected:** Habit Loop template filled
- **Verify:** All 4 components (Cue/Craving/Response/Reward)
- **Assertions:**
  - ✅ Template file created: `templates/personal/habit-loop-daily-exercise.md`
  - ✅ Cue: "Wake up at 6:45 AM"
  - ✅ Craving: "Feel energized"
  - ✅ Response: "20-minute workout"
  - ✅ Reward: "Post-workout smoothie"
  - ✅ Auto-linked from workflow plan (project_name, stakeholders populated)

**Success Criteria:**
- ✅ All 9 steps complete without errors
- ✅ Framework auto-suggested correctly (Habit Loop, confidence >80%)
- ✅ Auto-linking works (workflow plan → template)
- ✅ Quality gates PASS (scoring ≥6.5, deep plan quality)
- ✅ Template fully populated

---

### Test 1.2: Moderate Project (Business Domain)

**Scenario:** Launch side business (online course platform)

**Expected Total Time:** 2.5-3.5 hours

**Frameworks Used:** Lean Canvas + OKRs + SWOT (3 frameworks)

**Steps:**

#### 1. Step 1: Collect Idea
- **Input:** "Launch online course platform for freelancers"
- **Expected:** Design Thinking questions + business-specific prompts
- **Verify:** Domain detected: "business"
- **Assertions:**
  - ✅ Workflow plan initialized
  - ✅ Business-specific questions (market, revenue model, competition)

#### 2. Step 2: Roles Discovery
- **Expected:** Business specialists auto-detected
- **Verify:** Market Analyst, Business Strategist, Financial Advisor in list
- **Assertions:**
  - ✅ At least 4 business-domain specialists
  - ✅ Matching scores >75%

#### 3. Step 3: Specialist Match
- **Expected:** 3-4 specialists selected
- **Verify:** Roles include market research, strategy, finance
- **Assertions:**
  - ✅ 3-4 specialists assigned
  - ✅ Diverse perspectives (market, strategy, finance, operations)

#### 4. Step 4: Consilium
- **Expected:** Six Hats auto-assigned
- **Verify:** Divergence detection triggers TRIZ suggestion
- **Assertions:**
  - ✅ White Hat (data): Market Analyst
  - ✅ Black Hat (risks): Risk Advisor
  - ✅ Yellow Hat (opportunities): Growth Lead
  - ✅ Auto-suggest frameworks: Lean Canvas (85%), OKRs (80%), SWOT (75%)
  - ✅ Divergence: 38% → TRIZ suggested (confidence >85%)

#### 5. Step 5: Scoring
- **Expected:** Business-specific criteria
- **Verify:** Market Opportunity criterion added
- **Assertions:**
  - ✅ 6 criteria (Impact, Confidence, Effort, Strategic Alignment, Risk, Market Opportunity)
  - ✅ MCDA score: 7.8/10 (PASS)
  - ✅ Decision: PROCEED

#### 6. Step 6: Integration
- **Expected:** Strategic bucket: "Business Growth"
- **Verify:** WIP check passes
- **Assertions:**
  - ✅ Bucket: "Business Growth"
  - ✅ WIP: 1/2 capacity (PASS)
  - ✅ Timeline: 120 days (4 months)

#### 7. Step 7: Calendar Sync
- **Expected:** Weekly sprint planning + daily execution blocks
- **Verify:** Recurring events created
- **Assertions:**
  - ✅ Sprint planning: Every Monday 9:00 AM
  - ✅ Execution blocks: Tue-Fri 2:00-4:00 PM
  - ✅ Review: Every Friday 5:00 PM

#### 8. Step 8: Deep Plan
- **Expected:** L1-L6 structure with 4 phases
- **Verify:** Phases: Research, MVP, Launch, Growth
- **Assertions:**
  - ✅ L1 Mission: "Empower freelancers with structured learning"
  - ✅ L2 Phases: 4 phases (Research, MVP, Launch, Growth)
  - ✅ L3 Milestones: 8 total (2 per phase)
  - ✅ L4 Tasks: 32 total (~4 per milestone)
  - ✅ L5 RACI: 85% coverage
  - ✅ L6 Metrics: Revenue, CAC, LTV, NPS defined
  - ✅ Quality Gate: PASS

#### 9. Step 9: Templates
- **Expected:** 3 framework templates filled + auto-linked
- **Verify:** Lean Canvas, OKRs, SWOT
- **Assertions:**
  - ✅ `templates/business/lean-canvas-course-platform.md` (9 blocks complete)
  - ✅ `templates/business/okrs-course-platform.md` (3 objectives, 9 KRs)
  - ✅ `templates/business/swot-course-platform.md` (4 quadrants complete)
  - ✅ Auto-linked data:
    - Lean Canvas revenue → NPV template (if used)
    - OKRs key results → Deep Plan L3 milestones
    - SWOT opportunities → Market Opportunity scoring criterion

**Success Criteria:**
- ✅ All 9 steps complete
- ✅ 3 frameworks auto-suggested and correctly prioritized
- ✅ Auto-linking between frameworks (8+ links verified)
- ✅ TRIZ suggested due to divergence
- ✅ All templates fully populated

---

### Test 1.3: Complex Multi-Domain Project

**Scenario:** Career transition (Software Engineer → Product Manager)

**Domains:** Business + Personal Development

**Expected Total Time:** 5-7 hours

**Frameworks Used:** 5 frameworks + TRIZ for contradiction resolution

**Steps:**

#### 1. Step 1: Collect Idea
- **Input:** "Transition from software engineer to product manager within 12 months"
- **Expected:** Multi-domain detection
- **Verify:** Domains: "business", "personal-development"
- **Assertions:**
  - ✅ Workflow plan initialized
  - ✅ Multi-domain flag: true
  - ✅ Complexity score: HIGH

#### 2. Step 2: Roles Discovery
- **Expected:** Specialists from both domains
- **Verify:** Career Coach, Product Manager, Hiring Manager, Skill Development Specialist
- **Assertions:**
  - ✅ 6+ specialists (3+ per domain)
  - ✅ Cross-domain expertise (career coach with product management knowledge)

#### 3. Step 3: Specialist Match
- **Expected:** 4-5 specialists selected
- **Verify:** Balance across domains
- **Assertions:**
  - ✅ 4-5 specialists
  - ✅ Business domain: 2-3 specialists
  - ✅ Personal dev domain: 2-3 specialists

#### 4. Step 4: Consilium
- **Expected:** Six Hats + high divergence → TRIZ triggered
- **Verify:** Contradiction identified (technical skills vs. product skills)
- **Assertions:**
  - ✅ All 6 hats assigned
  - ✅ Divergence: 52% (HIGH)
  - ✅ TRIZ auto-suggested: "Resolve technical vs. product skills contradiction"
  - ✅ Auto-suggest frameworks:
    - Personal Development Plan (90%)
    - Learning Roadmap (85%)
    - OKRs (80%)
    - Portfolio Projects (75%)
    - Skill Gap Analysis (70%)

#### 5. Step 5: Scoring
- **Expected:** Combined criteria from both domains
- **Verify:** 8 criteria (business + personal dev)
- **Assertions:**
  - ✅ 8 criteria total
  - ✅ Career Impact (0.20)
  - ✅ Skill Transferability (0.15)
  - ✅ Market Demand (0.15)
  - ✅ Learning Curve (0.15)
  - ✅ Risk (0.10)
  - ✅ Readiness (0.10)
  - ✅ Strategic Alignment (0.10)
  - ✅ Time Investment (0.05)
  - ✅ MCDA score: 8.2/10 (PASS)

#### 6. Step 6: Integration
- **Expected:** Multiple strategic buckets
- **Verify:** "Career Development" + "Skill Building"
- **Assertions:**
  - ✅ Primary bucket: "Career Development"
  - ✅ Secondary bucket: "Skill Building"
  - ✅ WIP check: PASS (1/2 capacity)
  - ✅ Timeline: 365 days (12 months)

#### 7. Step 7: Calendar Sync
- **Expected:** Comprehensive schedule (learning + networking + projects)
- **Verify:** Multiple recurring events
- **Assertions:**
  - ✅ Learning blocks: Mon/Wed/Fri 7:00-9:00 PM
  - ✅ Portfolio projects: Tue/Thu 7:00-10:00 PM
  - ✅ Networking: Every other Saturday 10:00 AM
  - ✅ Skill assessments: Monthly (first Sunday)
  - ✅ Career coach check-ins: Bi-weekly

#### 8. Step 8: Deep Plan
- **Expected:** L1-L6 with 6 phases (12-month roadmap)
- **Verify:** Phases align with career transition stages
- **Assertions:**
  - ✅ L1 Mission: "Transition to product management role in top tech company"
  - ✅ L2 Phases: 6 phases
    - Foundation (Months 1-2)
    - Skill Building (Months 3-5)
    - Portfolio Development (Months 6-8)
    - Networking & Visibility (Months 9-10)
    - Job Search (Months 11-12)
    - Transition (Month 12+)
  - ✅ L3 Milestones: 18 total (3 per phase)
  - ✅ L4 Tasks: 72 total (~4 per milestone)
  - ✅ L5 RACI: 90% coverage
  - ✅ L6 Metrics: Skills acquired, portfolio projects, network connections, interviews, offers
  - ✅ Quality Gate: PASS

#### 9. Step 9: Templates + TRIZ
- **Expected:** 5 framework templates + TRIZ analysis
- **Verify:** All frameworks filled + TRIZ contradiction resolved
- **Assertions:**
  - ✅ Personal Development Plan: 6 sections complete
  - ✅ Learning Roadmap: Skills categorized (technical, product, soft)
  - ✅ OKRs: 3 objectives, 12 key results
  - ✅ Portfolio Projects: 3 projects with product focus
  - ✅ Skill Gap Analysis: Current vs. target skills mapped
  - ✅ TRIZ analysis:
    - Contradiction: "Need technical skills but also product skills"
    - Principle applied: #1 Segmentation (separate learning into parallel tracks)
    - Resolution: Technical skills → portfolio projects; Product skills → case studies
  - ✅ Auto-linking verified (15+ cross-references)

**Success Criteria:**
- ✅ All 9 steps complete
- ✅ 5 frameworks auto-suggested and filled
- ✅ TRIZ triggered and contradiction resolved
- ✅ Multi-domain integration works
- ✅ 15+ auto-links between frameworks
- ✅ Quality gates PASS

---

## Test Suite 2: Framework Integration

### Test 2.1: Auto-Suggest Triggering

```yaml
test: framework_auto_suggest
scenarios:
  - keyword_match:
      input: "I want to start a business"
      expected_frameworks:
        - Lean Canvas (confidence: 88%)
        - Business Model Canvas (confidence: 85%)
        - Market Analysis (confidence: 78%)
      verify:
        - suggestions_appear_in_step_04
        - confidence_scores_above_70_percent
        - frameworks_ranked_by_confidence

  - consilium_divergence:
      divergence: 45%
      expected_trigger: TRIZ
      expected_confidence: >85%
      verify:
        - triz_menu_option_appears
        - contradiction_detected
        - principles_suggested

  - domain_detection:
      input: "lose 20kg in 6 months"
      detected_domain: health
      expected_frameworks:
        - HBM (Health Belief Model) (confidence: 90%)
        - Progressive Overload (confidence: 82%)
        - Macro Calculation (confidence: 75%)
      verify:
        - health_domain_specialists_loaded
        - health_specific_criteria_in_scoring
        - readiness_and_sustainability_criteria_added

  - multi_framework_composition:
      input: "launch SaaS product"
      expected_frameworks:
        - Lean Canvas (confidence: 90%)
        - OKRs (confidence: 85%)
        - NPV/Financial Model (confidence: 80%)
        - Agile Sprint Planning (confidence: 75%)
      expected_synergies:
        - lean_canvas_to_npv: 0.92
        - okrs_to_sprint_planning: 0.88
      verify:
        - all_4_frameworks_suggested
        - synergy_matrix_calculated
        - frameworks_ordered_by_priority
```

### Test 2.2: Auto-Linking

```yaml
test: auto_linking
scenarios:
  - lean_canvas_to_npv:
      source:
        framework: lean_canvas
        field: revenue_streams
        value: "$50/mo subscription × 1000 users"
      target:
        framework: npv
        field: cash_inflows.year_1
        expected_value: 600000
        confidence: >0.9
        formula: "50 * 1000 * 12"
      verify:
        - npv_template_created
        - revenue_auto_populated
        - cash_flow_years_1_to_5_initialized

  - okrs_to_deep_plan:
      source:
        framework: okrs
        field: key_results
        value:
          - "Sign 100 users by Q2"
          - "Achieve 4.5 NPS by Q3"
          - "Launch 3 features by Q4"
      target:
        framework: deep_plan
        field: l2_phases
        expected_phases:
          - "Phase 1: User Acquisition (Q1-Q2)"
          - "Phase 2: Product Quality (Q2-Q3)"
          - "Phase 3: Feature Development (Q3-Q4)"
        confidence: >0.85
      verify:
        - phases_match_key_results
        - milestones_align_with_kr_targets
        - metrics_track_kr_progress

  - habit_loop_to_deep_plan:
      source:
        framework: habit_loop
        field: [cue, craving, response, reward]
        value:
          cue: "Wake up at 6:45 AM"
          craving: "Feel energized"
          response: "20-minute workout"
          reward: "Post-workout smoothie"
      target:
        framework: deep_plan
        field: l4_tasks
        expected_tasks:
          - "Set alarm for 6:45 AM"
          - "Prepare workout clothes night before"
          - "Buy smoothie ingredients weekly"
          - "Track energy levels in journal"
        confidence: >0.80
      verify:
        - tasks_support_habit_formation
        - environmental_design_included
        - tracking_mechanism_present

  - swot_to_scoring:
      source:
        framework: swot
        field: [strengths, weaknesses, opportunities, threats]
        value:
          strengths: ["Experienced team", "Strong network"]
          weaknesses: ["Limited capital", "No marketing"]
          opportunities: ["Growing market", "Low competition"]
          threats: ["Economic downturn", "Regulatory changes"]
      target:
        framework: scoring
        field: criteria_adjustments
        expected_adjustments:
          - criterion: "Risk"
            adjustment: +15%  # Increase weight due to threats
          - criterion: "Market Opportunity"
            adjustment: +10%  # Increase due to opportunities
          - criterion: "Confidence"
            adjustment: -5%   # Decrease due to weaknesses
        confidence: >0.75
      verify:
        - weights_adjusted_based_on_swot
        - total_weights_still_sum_to_1.0
        - scoring_reflects_swot_analysis
```

### Test 2.3: Template Composition

```yaml
test: template_composition
patterns:
  - startup_launch:
      frameworks:
        - Lean Canvas
        - NPV Financial Model
        - OKRs
        - Pomodoro Technique
      expected_auto_links: 8
      auto_link_map:
        1: lean_canvas.revenue_streams → npv.cash_inflows
        2: lean_canvas.cost_structure → npv.cash_outflows
        3: lean_canvas.key_metrics → okrs.key_results
        4: okrs.objectives → deep_plan.l2_phases
        5: okrs.key_results → deep_plan.l3_milestones
        6: pomodoro.daily_schedule → calendar_sync.time_blocks
        7: npv.roi_percentage → scoring.expected_value_criterion
        8: lean_canvas.unfair_advantage → scoring.strategic_alignment
      expected_time: "8-12 hours"
      verify_synergies: true
      expected_synergy_score: >0.85

  - habit_formation:
      frameworks:
        - Habit Loop
        - Progressive Overload
        - SMART Goals
      expected_auto_links: 5
      auto_link_map:
        1: habit_loop.cue → calendar_sync.trigger_events
        2: habit_loop.response → deep_plan.l4_tasks
        3: progressive_overload.weekly_progression → deep_plan.l3_milestones
        4: smart_goals.specific_target → scoring.impact_criterion
        5: smart_goals.timeline → timeline_allocation.duration
      expected_time: "2-3 hours"
      verify_synergies: true
      expected_synergy_score: >0.90

  - career_transition:
      frameworks:
        - Personal Development Plan
        - Learning Roadmap
        - OKRs
        - Portfolio Projects
        - Skill Gap Analysis
      expected_auto_links: 15
      expected_time: "5-7 hours"
      verify:
        - all_5_frameworks_generated
        - cross_references_consistent
        - no_contradictions_between_frameworks
        - synergy_matrix_all_pairs_calculated
```

---

## Test Suite 3: Six Thinking Hats

### Test 3.1: Auto-Assignment

```yaml
test: six_hats_auto_assignment
specialists:
  - name: Market Analyst
    domain: business
    expertise: data_analysis
    expected_hat: "⚪ White Hat"
    reason: data_driven_factual_analysis
    confidence: >0.95

  - name: Risk Advisor
    domain: business
    expertise: risk_management
    expected_hat: "⚫ Black Hat"
    reason: risk_focused_critical_thinking
    confidence: >0.98

  - name: Growth Lead
    domain: business
    expertise: opportunity_identification
    expected_hat: "🟡 Yellow Hat"
    reason: optimistic_opportunities_benefits
    confidence: >0.92

  - name: Creative Director
    domain: business
    expertise: innovation
    expected_hat: "🟢 Green Hat"
    reason: creative_alternatives_brainstorming
    confidence: >0.90

  - name: Customer Success Manager
    domain: business
    expertise: customer_empathy
    expected_hat: "🔴 Red Hat"
    reason: emotional_intuitive_customer_feelings
    confidence: >0.88

  - name: Project Manager
    domain: business
    expertise: process_management
    expected_hat: "🔵 Blue Hat"
    reason: process_control_coordination
    confidence: >0.85

verify:
  - all_6_hats_assigned_when_6_specialists
  - no_duplicate_hats_unless_7plus_specialists
  - hat_assignment_confidence_above_80_percent
  - fallback_to_balanced_assignment_if_ambiguous
```

### Test 3.2: Consilium Output Format

```yaml
test: consilium_output
scenarios:
  - lite_mode:
      specialists: 3
      expected_format:
        section_header: "Consilium Recommendations (Six Hats - Lite Mode)"
        per_specialist:
          format: "{Name} ({Hat Color} Hat - {Perspective}): {recommendation}"
          example: "Market Analyst (⚪ White Hat - Data): Market size is $50M annually"
        consensus_section:
          present: true
          format: "Consensus: {summary_of_all_recommendations}"
          balanced: all_hats_considered
      expected_time: "5-10 min"

  - deep_mode:
      specialists: 5
      expected_format:
        section_header: "Consilium Recommendations (Six Hats - Deep Mode)"
        per_specialist:
          format: |
            ### {Name} ({Hat Color} Hat - {Perspective})
            **Analysis:**
            {detailed_analysis}

            **Recommendation:**
            {recommendation}

            **Confidence:** {score}/10
        divergence_analysis:
          present: true
          format: "Divergence Score: {percentage}%"
          threshold_check: if >40% then suggest TRIZ
        consensus_section:
          present: true
          format: |
            ## Consilium Consensus
            {synthesized_recommendation}

            **Areas of Agreement:** {list}
            **Areas of Disagreement:** {list}
            **Recommended Next Steps:** {action_items}
      expected_time: "20-40 min"

verify:
  - output_matches_mode_format
  - all_specialists_included
  - hat_colors_and_perspectives_correct
  - consensus_balances_all_viewpoints
  - divergence_score_calculated_in_deep_mode
  - triz_suggested_if_divergence_high
```

### Test 3.3: Divergence Detection

```yaml
test: divergence_detection
scenarios:
  - low_divergence:
      specialists:
        - Market Analyst: "Market is ready"
        - Growth Lead: "Great opportunity"
        - Financial Advisor: "Strong ROI expected"
      divergence_score: 12%
      expected_outcome: consensus_clear
      triz_suggested: false

  - moderate_divergence:
      specialists:
        - Market Analyst: "Market size unclear"
        - Risk Advisor: "High regulatory risk"
        - Growth Lead: "First-mover advantage"
      divergence_score: 38%
      expected_outcome: consensus_with_caveats
      triz_suggested: false

  - high_divergence:
      specialists:
        - Market Analyst: "Market not proven"
        - Risk Advisor: "Too many unknowns"
        - Growth Lead: "Massive opportunity"
        - Creative Director: "Disruptive innovation possible"
      divergence_score: 52%
      expected_outcome: significant_disagreement
      triz_suggested: true
      triz_confidence: >85%
      contradiction_identified: "Need to move fast vs. reduce risk"

verify:
  - divergence_score_calculated_correctly
  - triz_triggered_at_40_percent_threshold
  - contradiction_clearly_stated
  - user_prompted_to_resolve_or_continue
```

---

## Test Suite 4: TRIZ Integration

### Test 4.1: TRIZ Menu Appearance

```yaml
test: triz_menu_availability
steps:
  - step_04_consilium:
      menu_before: "[A][P][C]"
      menu_after: "[T][A][P][C]"
      triz_option: "[T] TRIZ - Resolve contradictions between specialist recommendations"
      appears_when: divergence >40%

  - step_05_scoring:
      menu: "[T][A][P][C]"
      triz_option: "[T] TRIZ - Resolve scoring conflicts (e.g., high impact but high risk)"
      appears_when: always_available

  - step_08_deep_plan:
      menu: "[T][A][P][C]"
      triz_option: "[T] TRIZ - Resolve planning contradictions (e.g., speed vs. quality)"
      appears_when: always_available

verify:
  - triz_menu_option_present_in_all_3_steps
  - menu_format_consistent
  - option_descriptions_clear_and_specific
  - triz_not_in_other_steps
```

### Test 4.2: TRIZ Mode Selection

```yaml
test: triz_modes
modes:
  - quick:
      time: "5-10 min"
      template: triz-quick.template.md
      inputs:
        - contradiction_statement
        - desired_outcome
      outputs:
        - top_3_principles_from_40
        - quick_brainstorm_ideas
        - recommended_principle_with_rationale
      verify:
        - template_generated_correctly
        - principles_relevant_to_contradiction
        - ideas_actionable

  - structured:
      time: "30-60 min"
      template: triz-structured.template.md
      inputs:
        - contradiction_statement
        - system_components
        - constraints
      outputs:
        - contradiction_matrix_lookup
        - systematic_analysis_of_principles
        - 5_to_10_solution_concepts
        - feasibility_assessment
      verify:
        - matrix_lookup_correct
        - all_relevant_principles_analyzed
        - solution_concepts_detailed
        - feasibility_ratings_included

  - full_ariz:
      time: "2-4 hours"
      template: ariz-full.template.md
      inputs:
        - detailed_problem_description
        - system_analysis
        - resource_inventory
      outputs:
        - complete_ariz_85c_analysis
        - ideal_final_result_defined
        - physical_contradictions_identified
        - patent_research_summary
        - implementation_roadmap
      verify:
        - all_ariz_sections_complete
        - ifr_clearly_defined
        - contradictions_at_multiple_levels
        - patent_search_conducted
        - roadmap_actionable

verify:
  - user_can_select_mode_in_menu
  - correct_template_loaded_per_mode
  - estimated_time_displayed
  - mode_selection_saved_in_workflow_plan
```

### Test 4.3: Contradiction Resolution

```yaml
test: contradiction_resolution
scenarios:
  - speed_vs_quality:
      contradiction: "Need to launch fast but also need high quality"
      triz_mode: quick
      expected_principles:
        - Principle 1: Segmentation (MVP approach)
        - Principle 10: Preliminary Action (prepare quality checks in advance)
        - Principle 15: Dynamics (iterative quality improvement)
      expected_resolution: "Launch MVP quickly, then iterate quality in phases"
      verify:
        - principles_applied_correctly
        - resolution_addresses_both_sides
        - actionable_next_steps_provided

  - cost_vs_features:
      contradiction: "Need many features but have limited budget"
      triz_mode: structured
      expected_principles:
        - Principle 1: Segmentation (prioritize core features)
        - Principle 35: Parameter Changes (adjust scope to fit budget)
        - Principle 5: Merging (combine features for efficiency)
      expected_resolution: "Focus on 3 core features, combine related functionality"
      verify:
        - matrix_lookup_used
        - multiple_principles_evaluated
        - best_principle_selected_with_rationale

  - scale_vs_personalization:
      contradiction: "Need to scale to 10k users but provide personalized experience"
      triz_mode: full_ariz
      expected_principles:
        - Principle 1: Segmentation (user cohorts)
        - Principle 23: Feedback (ML-driven personalization)
        - Principle 25: Self-Service (automated personalization)
      expected_resolution: "Segment users into cohorts, use ML for automated personalization at scale"
      verify:
        - ariz_process_followed
        - ifr_defined
        - technical_and_physical_contradictions_analyzed
        - implementation_roadmap_created

verify:
  - contradiction_clearly_restated
  - principles_from_40_inventive_principles
  - resolution_creative_and_actionable
  - integrated_into_workflow_plan
```

---

## Test Suite 5: Memory Integration

### Test 5.1: Knowledge Storage

```yaml
test: memory_storage
hooks:
  - post_edit:
      trigger: after_step_file_edit
      action: extract_patterns
      expected_behavior:
        - detects_patterns_in_edited_file
        - stores_pattern_in_shared_knowledge_namespace
        - tags_with_domain_and_framework
      verify:
        - pattern_stored_in_memory
        - namespace: "shared-knowledge:patterns:{domain}:{pattern_name}"
        - searchable: true
        - retrieval_time: <100ms

  - post_task:
      trigger: after_step_completion
      action: save_learnings
      expected_behavior:
        - extracts_learnings_from_step_output
        - categorizes_by_kb_category
        - stores_with_metadata
      verify:
        - learning_in_shared_knowledge_namespace
        - namespace: "shared-knowledge:learnings:{step}:{topic}"
        - metadata_includes: [timestamp, project_name, domain, success_status]
        - searchable: true

  - consolidate:
      trigger: every_30_min
      action: deduplicate_optimize
      expected_behavior:
        - identifies_duplicate_entries
        - merges_similar_patterns
        - rebuilds_hnsw_index
      verify:
        - duplicate_count_reduced
        - hnsw_index_updated
        - search_performance_maintained: <100ms
        - storage_size_optimized

verify:
  - all_3_hooks_active
  - hooks_triggered_correctly
  - memory_backend_connected: hybrid
  - global_memory_accessible: ~/.claude-flow/agentdb-global/
```

### Test 5.2: Pattern Retrieval

```yaml
test: memory_retrieval
scenarios:
  - before_coding:
      query: "launch business pattern"
      expected_results:
        - patterns_from_previous_business_projects
        - frameworks_used: [Lean Canvas, OKRs, SWOT]
        - confidence_scores: >0.80
      verify:
        - results_returned_in_under_100ms
        - patterns_relevant_to_query
        - reuse_saves_tokens: true
        - token_savings_estimated: 32%

  - cross_project:
      scenario:
        - project_a: "E-commerce startup"
        - action: stores_lean_canvas_pattern
        - project_b: "SaaS launch"
        - action: searches_for_business_patterns
      expected:
        - project_b_retrieves_project_a_pattern
        - pattern_content_identical
        - metadata_shows_origin: project_a
      verify:
        - global_memory_works
        - cross_project_access_confirmed
        - pattern_reusable_across_domains

  - domain_specific_search:
      query: "health habit formation"
      domain_filter: "health"
      expected_results:
        - patterns_from_health_domain_only
        - frameworks: [Habit Loop, HBM, Progressive Overload]
        - specialists: [Fitness Coach, Nutritionist, Habit Specialist]
      verify:
        - domain_filter_applied
        - no_irrelevant_domains_in_results
        - confidence_scores: >0.85

verify:
  - search_api_functional
  - hnsw_indexing_provides_speed_boost: 150x-12500x
  - pattern_confidence_scores_calculated
  - token_savings_tracked
```

### Test 5.3: Knowledge Base Auto-Population

```yaml
test: kb_auto_population
categories:
  - code_patterns:
      source: post-edit hook
      expected_entries: patterns_extracted_from_code_changes
      verify:
        - namespace: "kb:code-patterns:{language}:{pattern}"
        - auto_tagged: true
        - searchable: true

  - architecture:
      source: post-task hook (step 8 deep plan)
      expected_entries: system_design_decisions
      verify:
        - namespace: "kb:architecture:{project}:{decision}"
        - decision_rationale_included: true

  - workflows:
      source: post-task hook (step 9 complete)
      expected_entries: workflow_completion_summary
      verify:
        - namespace: "kb:workflows:{workflow_name}:{timestamp}"
        - includes: [steps_completed, frameworks_used, time_taken]

  - learnings:
      source: post-task hook (all steps)
      expected_entries: step_specific_learnings
      verify:
        - namespace: "kb:learnings:{step}:{topic}"
        - categorized_by_success_failure: true

verify:
  - 80_percent_auto_population_rate
  - manual_entry_only_for_20_percent
  - all_12_kb_categories_populated
  - consolidate_worker_deduplicates_daily
```

---

## Test Suite 6: Scoring Integration

### Test 6.1: Domain-Specific Criteria

```yaml
test: domain_criteria
domains:
  - business:
      criteria:
        - Impact (0.25)
        - Confidence (0.15)
        - Effort (0.15)
        - Strategic Alignment (0.20)
        - Risk (0.15)
        - Market Opportunity (0.10)
      verify:
        - total_weight: 1.0
        - market_opportunity_unique_to_business: true
        - criteria_appropriate_for_business_projects: true

  - finance:
      criteria:
        - Impact (0.20)
        - Confidence (0.15)
        - Effort (0.10)
        - Strategic Alignment (0.15)
        - Risk (0.15)
        - Expected Value (0.15)
        - Option Value (0.10)
      verify:
        - total_weight: 1.0
        - expected_value_and_option_value_unique_to_finance: true
        - npv_and_real_options_considered: true

  - health:
      criteria:
        - Impact (0.20)
        - Confidence (0.15)
        - Effort (0.15)
        - Strategic Alignment (0.15)
        - Risk (0.15)
        - Readiness (0.10)
        - Sustainability (0.10)
      verify:
        - total_weight: 1.0
        - readiness_uses_hbm_framework: true
        - sustainability_long_term_habit_focus: true

  - personal_development:
      criteria:
        - Impact (0.25)
        - Confidence (0.15)
        - Effort (0.15)
        - Strategic Alignment (0.20)
        - Risk (0.10)
        - Learning Potential (0.10)
        - Career Relevance (0.05)
      verify:
        - total_weight: 1.0
        - learning_potential_unique_to_personal_dev: true

verify:
  - domain_auto_detected_correctly
  - correct_criteria_loaded_per_domain
  - weights_customizable_by_user
  - default_weights_sensible
```

### Test 6.2: Stage Gate Logic

```yaml
test: stage_gates
gates:
  - idea_gate:
      location: after_step_04_consilium
      criteria:
        - consilium_consensus_score: ≥80%
      decision_rules:
        - if_pass: proceed_to_step_05
        - if_fail: options = [rescore, kill_project, return_to_consilium]
      verify:
        - gate_evaluated_automatically
        - decision_clear: PASS | FAIL
        - user_prompted_if_fail

  - scoring_gate:
      location: after_step_05_scoring
      criteria:
        - mcda_score: ≥6.5/10
      decision_rules:
        - if_pass: proceed_to_step_06
        - if_fail: options = [adjust_criteria, rescore, kill_project]
      verify:
        - gate_evaluated_automatically
        - score_threshold_configurable
        - failure_prompts_user_action

  - planning_gate:
      location: after_step_08_deep_plan
      criteria:
        - l1_mission_present: true
        - l2_phases_count: ≥2
        - l3_milestones_count: ≥4
        - l4_tasks_count: ≥10
        - l5_raci_coverage: ≥70%
        - l6_metrics_defined: true
      decision_rules:
        - if_pass: proceed_to_step_09
        - if_fail: options = [improve_plan, skip_gate, return_to_planning]
      verify:
        - all_quality_checks_evaluated
        - gate_pass_fail_clear
        - failure_shows_missing_components

verify:
  - all_3_gates_enforced
  - gates_prevent_progression_on_fail
  - user_always_has_override_option
  - gate_decisions_logged_in_workflow_plan
```

### Test 6.3: MCDA Calculation

```yaml
test: mcda_calculation
scenarios:
  - business_project:
      scores:
        impact: 9
        confidence: 7
        effort: 3  # Low effort = higher score
        strategic_alignment: 8
        risk: 4    # Low risk = higher score
        market_opportunity: 8
      weights:
        impact: 0.25
        confidence: 0.15
        effort: 0.15
        strategic_alignment: 0.20
        risk: 0.15
        market_opportunity: 0.10
      expected_mcda_score: 7.35
      decision: PASS (≥6.5)
      verify:
        - calculation_correct
        - effort_and_risk_inverted_properly
        - weighted_sum_accurate

  - health_project:
      scores:
        impact: 8
        confidence: 6
        effort: 5
        strategic_alignment: 7
        risk: 6
        readiness: 7  # HBM score
        sustainability: 8
      weights:
        impact: 0.20
        confidence: 0.15
        effort: 0.15
        strategic_alignment: 0.15
        risk: 0.15
        readiness: 0.10
        sustainability: 0.10
      expected_mcda_score: 6.75
      decision: PASS (≥6.5)
      verify:
        - health_specific_criteria_included
        - hbm_readiness_calculated
        - sustainability_assessed

verify:
  - mcda_formula_correct: Σ(weight_i × score_i)
  - scores_normalized_1_to_10
  - effort_and_risk_inverted: (11 - raw_score)
  - threshold_6.5_applied_consistently
```

---

## Test Suite 7: Performance Tests

### Test 7.1: Load Testing

```yaml
test: concurrent_projects
scenarios:
  - batch_10_projects:
      count: 10
      mode: parallel
      operations:
        - create_workflow_plans: 10
        - assign_specialists: 10
        - run_consilium: 10
        - calculate_scores: 10
      expected_time: <5min total
      verify:
        - no_data_conflicts
        - all_10_projects_complete
        - memory_usage: <2GB

  - portfolio_50_projects:
      count: 50
      mode: active_tracking
      operations:
        - wip_limits_enforced: true
        - portfolio_health_calculated: true
        - strategic_bucket_allocation: balanced
      expected_time: <10min for full portfolio analysis
      verify:
        - wip_limits_respected
        - no_more_than_5_projects_in_execution
        - capacity_management_working
        - portfolio_dashboard_accurate

verify:
  - no_race_conditions
  - memory_backend_handles_concurrent_writes
  - hnsw_index_updates_without_corruption
  - system_remains_responsive
```

### Test 7.2: Memory Performance

```yaml
test: memory_speed
scenarios:
  - search_100k_entries:
      entries: 100000
      query: "business launch pattern"
      expected_latency: <100ms
      index_type: hnsw
      verify:
        - hnsw_indexing_working
        - search_results_accurate
        - 150x_to_12500x_speedup_vs_linear_search

  - cross_project_search:
      projects: 20
      patterns_per_project: 50
      total_entries: 1000
      query: "habit formation techniques"
      expected_latency: <200ms
      verify:
        - global_memory_searched
        - results_from_multiple_projects
        - relevance_scores_accurate

  - write_performance:
      operations: 1000
      operation_type: memory_store
      batch_size: 100
      expected_time: <5s for 1000 writes
      verify:
        - batch_writes_faster_than_individual
        - no_data_loss
        - hnsw_index_updates_queued

  - consolidation_performance:
      entries_before: 10000
      duplicates: 1500
      consolidation_time: <30s
      expected_entries_after: 8500
      verify:
        - duplicates_removed
        - hnsw_index_rebuilt
        - search_performance_maintained_or_improved

verify:
  - hnsw_enabled_globally
  - search_latency_targets_met
  - write_throughput_acceptable
  - consolidation_worker_efficient
```

---

## Test Suite 8: Error Handling

### Test 8.1: Invalid Inputs

```yaml
test: input_validation
scenarios:
  - empty_idea:
      input: ""
      expected_behavior:
        - error_message: "Project description cannot be empty"
        - prompt_user: "Please describe your project or goal:"
        - no_workflow_plan_created

  - invalid_score:
      score: 15  # out of 1-10 range
      expected_behavior:
        - error_message: "Score must be between 1 and 10"
        - prompt_user: "Please enter a valid score (1-10):"
        - previous_scores_preserved

  - missing_specialist:
      role: "NonExistentRole"
      expected_behavior:
        - error_message: "Specialist 'NonExistentRole' not found"
        - suggestion: "Did you mean: [similar_role_1, similar_role_2]?"
        - fuzzy_matching_used: true

  - invalid_framework:
      framework: "Invalid Framework Name"
      expected_behavior:
        - error_message: "Framework 'Invalid Framework Name' not found"
        - suggestion: "Available frameworks in {domain}: [list]"
        - no_template_created

  - malformed_yaml:
      file: workflow_plan_with_syntax_error
      expected_behavior:
        - error_message: "YAML syntax error in workflow plan"
        - show_error_location: "Line 45, column 12"
        - offer_auto_fix: true

verify:
  - all_inputs_validated
  - error_messages_clear_and_actionable
  - system_never_crashes_on_invalid_input
  - user_always_has_path_forward
```

### Test 8.2: Graceful Degradation

```yaml
test: graceful_degradation
scenarios:
  - memory_unavailable:
      condition: memory_backend_down
      expected_behavior:
        - fallback: continue_without_pattern_reuse
        - warning: "Memory system unavailable - no pattern suggestions"
        - functionality_preserved: true
        - retry_memory_connection: every_5min
      verify:
        - workflow_continues
        - no_data_loss
        - user_informed_of_limitation

  - framework_template_missing:
      condition: template_file_not_found
      expected_behavior:
        - fallback: use_generic_template
        - warning: "Template for {framework} not found - using generic"
        - generic_template_structure: sections_based_on_framework_type
      verify:
        - template_still_created
        - user_can_fill_manually
        - warning_logged

  - specialist_database_unavailable:
      condition: roles_csv_file_missing
      expected_behavior:
        - fallback: use_cached_specialists_from_memory
        - warning: "Specialist database unavailable - using cached list"
        - allow_manual_entry: true
      verify:
        - workflow_continues
        - cached_list_has_core_specialists: ≥20
        - user_can_add_custom_specialists

  - hnsw_index_corrupted:
      condition: hnsw_index_rebuild_required
      expected_behavior:
        - fallback: linear_search_temporarily
        - background_task: rebuild_hnsw_index
        - warning: "Search may be slower - rebuilding index"
      verify:
        - search_still_works
        - results_accurate
        - index_rebuilt_automatically: <5min

verify:
  - system_never_fully_fails
  - degraded_mode_always_available
  - recovery_automatic_when_possible
  - user_always_informed_of_status
```

### Test 8.3: Data Consistency

```yaml
test: data_consistency
scenarios:
  - concurrent_workflow_edits:
      condition: two_users_edit_same_workflow_plan
      expected_behavior:
        - conflict_detection: true
        - merge_strategy: last_write_wins_with_warning
        - backup_created: true
      verify:
        - no_data_corruption
        - both_edits_logged
        - user_notified_of_conflict

  - partial_step_completion:
      condition: user_stops_mid_step
      expected_behavior:
        - workflow_plan_updated: partial_progress_saved
        - next_session: prompt_to_resume_or_restart
        - no_orphaned_files: true
      verify:
        - partial_state_preserved
        - resume_works_correctly
        - no_data_loss

  - framework_template_auto_link_failure:
      condition: auto_linking_cannot_resolve_field
      expected_behavior:
        - placeholder_inserted: "{AUTO_LINK_FAILED: source.field}"
        - warning_in_template: "Manual input required"
        - log_failure_reason: true
      verify:
        - template_still_created
        - user_knows_what_to_fill
        - failure_logged_for_debugging

verify:
  - data_integrity_maintained
  - no_silent_failures
  - all_failures_logged
  - recovery_paths_clear
```

---

## Test Suite 9: User Experience

### Test 9.1: Step Navigation

```yaml
test: step_navigation
scenarios:
  - forward_navigation:
      action: complete_step_N
      expected: auto_advance_to_step_N_plus_1
      verify:
        - menu_updated
        - next_step_instructions_shown
        - progress_tracker_updated

  - backward_navigation:
      action: user_selects_previous_step
      expected: allow_return_to_previous_step
      verify:
        - previous_data_preserved
        - warning_if_changes_affect_later_steps
        - re_validation_option_offered

  - jump_navigation:
      action: user_selects_step_from_menu
      expected: allow_jump_if_no_blockers
      verify:
        - blocker_check: required_previous_steps_complete
        - if_blocked: show_required_steps
        - if_unblocked: allow_jump

verify:
  - navigation_intuitive
  - progress_always_saved
  - user_never_loses_work
```

### Test 9.2: Menu Responsiveness

```yaml
test: menu_responsiveness
scenarios:
  - dynamic_menu_updates:
      trigger: step_completion
      expected: menu_options_update_immediately
      verify:
        - completed_steps: show_checkmark
        - current_step: highlighted
        - next_steps: enabled

  - contextual_options:
      step: step_04_consilium
      divergence: 45%
      expected: triz_option_appears_in_menu
      verify:
        - menu_before: "[A][P][C]"
        - menu_after: "[T][A][P][C]"
        - option_description_clear

  - shortcut_keys:
      shortcuts:
        - "[A]": auto_suggest
        - "[P]": proceed
        - "[C]": cancel
        - "[T]": triz
      verify:
        - shortcuts_work_consistently
        - shortcuts_documented_in_menu
        - no_conflicts_with_input_fields

verify:
  - menu_always_reflects_current_state
  - options_enabled_disabled_appropriately
  - shortcuts_reduce_clicks
```

---

## Test Execution Framework

### Running Tests

```bash
# Full test suite (all 47 tests)
life-os test --suite all --report html

# Specific suite
life-os test --suite end-to-end
life-os test --suite framework-integration
life-os test --suite six-thinking-hats
life-os test --suite triz
life-os test --suite memory
life-os test --suite scoring
life-os test --suite performance
life-os test --suite error-handling
life-os test --suite user-experience

# Specific test
life-os test Test-1.1-Simple-Project
life-os test Test-2.2-Auto-Linking

# Parallel execution (faster)
life-os test --suite all --parallel --workers 8

# Verbose output
life-os test --suite all --verbose

# Report formats
life-os test --suite all --report junit.xml  # For CI/CD
life-os test --suite all --report html        # For browser viewing
life-os test --suite all --report json        # For programmatic analysis
```

### CI/CD Integration

```yaml
# .github/workflows/integration-tests.yml
name: Life OS Integration Tests
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM

jobs:
  integration-tests:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name: Setup Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '20'

      - name: Install dependencies
        run: |
          npm install
          npx claude-flow@v3alpha daemon start

      - name: Run integration tests
        run: |
          life-os test --suite all --report junit.xml --parallel

      - name: Publish test results
        uses: EnricoMi/publish-unit-test-result-action@v1
        if: always()
        with:
          files: junit.xml

      - name: Upload HTML report
        uses: actions/upload-artifact@v2
        if: always()
        with:
          name: integration-test-report
          path: test-report.html
```

---

## Success Criteria Summary

**All Tests PASS Requirements:**

| Category | Requirement | Target |
|----------|-------------|--------|
| **End-to-End** | All workflows complete without errors | 100% |
| **Framework Auto-Suggest** | Accuracy of suggestions | >85% |
| **Auto-Linking** | Confidence of cross-references | >90% |
| **Six Hats** | Hat assignment accuracy | 100% |
| **TRIZ** | Menu appears in all 3 steps | 100% |
| **Memory Storage** | Pattern storage latency | <100ms |
| **Memory Retrieval** | Search latency (100K entries) | <100ms |
| **Scoring Gates** | Enforcement accuracy | 100% |
| **MCDA Calculation** | Calculation correctness | 100% |
| **Data Consistency** | No data loss or corruption | 100% |
| **Error Handling** | Graceful degradation | 100% |
| **User Experience** | Navigation intuitive, no dead ends | 100% |

**Performance Targets:**

- Simple project (Test 1.1): 25-35 minutes
- Moderate project (Test 1.2): 2.5-3.5 hours
- Complex project (Test 1.3): 5-7 hours
- Memory search (100K entries): <100ms
- Concurrent 10 projects: <5 minutes
- Full test suite execution: 45-60 minutes

**Quality Metrics:**

- Code coverage: >90%
- Test pass rate: 100%
- No flaky tests
- All edge cases covered
- Error messages clear and actionable

---

## Continuous Improvement

### Test Maintenance

```bash
# Add new test
life-os test --create Test-10.1-New-Feature

# Update existing test
life-os test --update Test-1.1-Simple-Project

# Archive deprecated test
life-os test --archive Test-Obsolete-Feature

# Validate all tests still run
life-os test --validate-suite
```

### Metrics Tracking

```yaml
metrics:
  test_execution:
    - total_tests: 47
    - pass_rate: 100%
    - average_duration: 52min
    - flaky_tests: 0

  coverage:
    - code_coverage: 94%
    - feature_coverage: 100%
    - edge_case_coverage: 87%

  performance:
    - memory_search_p50: 45ms
    - memory_search_p95: 85ms
    - memory_search_p99: 120ms
    - workflow_completion_p50: 28min
    - workflow_completion_p95: 6.5h
```

---

**Integration Tests Version:** 1.0
**Last Updated:** 2026-02-04
**Total Tests:** 47
**Estimated Run Time:** 45-60 minutes (full suite)
**Maintainer:** Life OS Development Team

**Next Review:** 2026-03-04 (monthly review cycle)
