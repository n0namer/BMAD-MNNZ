---
document: auto-suggest-engine
version: 1.0
phase: 3
status: implementation_ready
purpose: Intelligent framework suggestion engine with trigger detection
integration: Steps 1, 4, 5, 8
depends_on:
  - method-rankings.yaml
  - framework-synergy-matrix.csv
  - domain-framework-integration.md
  - domain-template-architecture.md
---

# Life OS Auto-Suggest Engine

**Phase:** 3 (Auto-Suggest)
**Status:** Implementation Ready
**Integration:** Claude Code workflow steps

---

## 1. Engine Overview

**What it does:**
- Detects triggers (keywords, consilium patterns, scoring conflicts)
- Matches triggers to framework recommendations from method-rankings.yaml
- Calculates confidence scores with multi-signal aggregation
- Presents suggestions to user with rationale and synergy notes
- Learns from user feedback to improve future suggestions

**When it runs:**
- After Step 1 (Collect Ideas) - detect domain from user input
- After Step 4 (Consilium) - detect contradictions and divergence across hats
- After Step 5 (Scoring) - detect MCDA scoring conflicts and missing criteria
- During Step 8 (Deep Plan) - detect planning contradictions at L2+

**Confidence threshold:** >=70% to show suggestion
**Max suggestions per trigger point:** 3
**Cooldown:** Same framework not re-suggested within same session unless new trigger

---

## 2. Trigger Detection System

### 2.1 Keyword Triggers

Keyword triggers are the primary detection mechanism at Step 1 (Collect Ideas).
Each keyword carries a confidence weight. Multiple keyword matches compound.

**Business Domain Keywords:**

```yaml
business_keywords:
  high_confidence: # 90%+ base confidence
    - startup
    - product launch
    - business model
    - revenue
    - customers
    - market share
    - b2b
    - b2c
    - saas
    - marketplace
    - scaling
    - acquisition
    - retention
    - conversion
    - go-to-market

  medium_confidence: # 70-89% base confidence
    - competition
    - value proposition
    - pricing
    - channels
    - partnerships
    - mvp
    - product-market fit
    - business plan
    - target audience
    - user growth
    - churn
    - engagement
    - metrics
    - pivot
    - monetization

  low_confidence: # 50-69% - only contributes if combined with other signals
    - idea
    - project
    - work
    - team
    - client
    - website
    - app
    - service
```

**Finance Domain Keywords:**

```yaml
finance_keywords:
  high_confidence:
    - investment
    - roi
    - npv
    - cash flow
    - valuation
    - portfolio
    - property
    - rental
    - stock
    - crypto
    - dividend
    - compound interest
    - asset allocation
    - real estate
    - equity

  medium_confidence:
    - budget
    - financial
    - returns
    - risk-reward
    - payback period
    - interest rate
    - mortgage
    - savings
    - retirement
    - passive income
    - capital
    - debt
    - yield
    - diversification
    - inflation

  low_confidence:
    - money
    - cost
    - price
    - expensive
    - cheap
    - afford
    - pay
    - earn
```

**Health Domain Keywords:**

```yaml
health_keywords:
  high_confidence:
    - weight loss
    - fitness
    - gym
    - workout
    - diet
    - nutrition
    - muscle
    - cardio
    - marathon
    - body composition
    - bulking
    - cutting
    - strength training
    - flexibility
    - body fat

  medium_confidence:
    - health
    - exercise
    - training
    - recovery
    - sleep
    - energy
    - calories
    - protein
    - supplements
    - running
    - swimming
    - yoga
    - posture
    - mobility
    - endurance

  low_confidence:
    - tired
    - weight
    - body
    - pain
    - stress
    - food
    - walk
    - active
```

**Personal Development Keywords:**

```yaml
personal_keywords:
  high_confidence:
    - learn
    - skill
    - master
    - practice
    - study
    - course
    - certification
    - competency
    - deliberate practice
    - skill acquisition
    - expertise
    - mastery
    - habit building
    - behavior change
    - self-improvement

  medium_confidence:
    - productivity
    - focus
    - time management
    - habit
    - goal
    - growth
    - development
    - discipline
    - routine
    - mindset
    - motivation
    - procrastination
    - organization
    - planning
    - reading

  low_confidence:
    - better
    - improve
    - change
    - start
    - new
    - want
    - try
    - effort
```

**Detection Algorithm:**

```python
def detect_domain_from_keywords(user_input):
    """
    Scans user input for domain keywords.
    Returns primary domain, secondary domain (if any), and confidence.
    Uses weighted scoring with diminishing returns for multiple matches.
    """
    scores = {
        'business': 0.0,
        'finance': 0.0,
        'health': 0.0,
        'personal': 0.0
    }

    # Normalize input: lowercase, split into words and 2-grams
    text = user_input.lower()
    words = text.split()
    bigrams = [f"{words[i]} {words[i+1]}" for i in range(len(words)-1)]
    tokens = words + bigrams

    # Weight map
    weights = {
        'high_confidence': 0.90,
        'medium_confidence': 0.70,
        'low_confidence': 0.50
    }

    for token in tokens:
        for domain in ['business', 'finance', 'health', 'personal']:
            keyword_set = globals()[f'{domain}_keywords']
            for tier, weight in weights.items():
                if token in keyword_set[tier]:
                    # Diminishing returns: each subsequent match adds less
                    current = scores[domain]
                    increment = weight * (1.0 / (1.0 + current))
                    scores[domain] += increment

    # Normalize to 0-1 range
    max_possible = 3.0  # practical ceiling
    for domain in scores:
        scores[domain] = min(scores[domain] / max_possible, 1.0)

    # Determine primary and secondary domains
    sorted_domains = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    primary_domain = sorted_domains[0][0]
    primary_confidence = sorted_domains[0][1]
    secondary_domain = sorted_domains[1][0] if sorted_domains[1][1] >= 0.40 else None
    secondary_confidence = sorted_domains[1][1] if secondary_domain else 0.0

    # Apply threshold
    if primary_confidence >= 0.70:
        return {
            'primary_domain': primary_domain,
            'primary_confidence': round(primary_confidence, 2),
            'secondary_domain': secondary_domain,
            'secondary_confidence': round(secondary_confidence, 2),
            'all_scores': {k: round(v, 2) for k, v in scores.items()},
            'trigger_type': 'keyword'
        }
    elif primary_confidence >= 0.50:
        return {
            'primary_domain': primary_domain,
            'primary_confidence': round(primary_confidence, 2),
            'secondary_domain': None,
            'secondary_confidence': 0.0,
            'all_scores': {k: round(v, 2) for k, v in scores.items()},
            'trigger_type': 'keyword_weak',
            'note': 'Below 70% threshold - suggest but mark as tentative'
        }
    else:
        return {
            'primary_domain': None,
            'primary_confidence': 0.0,
            'secondary_domain': None,
            'secondary_confidence': 0.0,
            'all_scores': {k: round(v, 2) for k, v in scores.items()},
            'trigger_type': 'none'
        }
```

---

### 2.2 Consilium Divergence Triggers

Consilium (Step 4) uses Six Thinking Hats. When specialists diverge significantly,
this indicates a contradiction that TRIZ or other frameworks can resolve.

**Divergence Measurement:**

```yaml
divergence_detection:
  measurement: variance_across_hat_recommendations
  threshold_moderate: 30%   # Mention TRIZ as optional
  threshold_high: 40%       # Actively suggest TRIZ
  threshold_extreme: 60%    # Strongly recommend TRIZ + structured analysis

  hat_opposition_pairs:
    - pair: [black_hat, yellow_hat]
      opposition: risk_vs_benefit
      triz_relevance: high
      description: "Black Hat warns of risks, Yellow Hat sees strong benefits"

    - pair: [black_hat, green_hat]
      opposition: feasibility_vs_innovation
      triz_relevance: high
      description: "Black Hat questions feasibility, Green Hat proposes creative solution"

    - pair: [white_hat, red_hat]
      opposition: data_vs_intuition
      triz_relevance: medium
      description: "White Hat says data insufficient, Red Hat feels strongly positive"

    - pair: [yellow_hat, red_hat]
      opposition: logic_vs_emotion
      triz_relevance: low
      description: "Both positive but for different reasons - may not need resolution"
```

**Detection Algorithm:**

```python
def detect_contradiction_from_consilium(consilium_output):
    """
    Analyzes Six Hats consilium output for contradictions.
    Returns list of detected contradictions with framework recommendations.
    """
    hats = parse_six_hats(consilium_output)
    contradictions = []

    # 1. Risk-Benefit contradiction (Black vs Yellow)
    if hats['black_hat'].risk_level in ['high', 'very_high'] and \
       hats['yellow_hat'].benefit_level in ['high', 'very_high']:
        contradictions.append({
            'type': 'risk_benefit',
            'severity': 'high',
            'description': f"High benefit potential ({hats['yellow_hat'].summary}) "
                          f"but significant risks ({hats['black_hat'].summary})",
            'framework': 'TRIZ',
            'confidence': 0.85,
            'triz_principle_hint': 'Segmentation, Extraction, or Parameter Change',
            'rationale': 'TRIZ specializes in resolving "we want A but it causes B" contradictions'
        })

    # 2. Innovation-Feasibility contradiction (Green vs Black)
    if hats['green_hat'].innovation_level in ['high', 'very_high'] and \
       hats['black_hat'].feasibility_concern in ['high', 'very_high']:
        contradictions.append({
            'type': 'innovation_feasibility',
            'severity': 'high',
            'description': f"Innovative approach ({hats['green_hat'].summary}) "
                          f"faces feasibility barriers ({hats['black_hat'].summary})",
            'framework': 'TRIZ',
            'confidence': 0.80,
            'triz_principle_hint': 'Prior Action, Equipotentiality, or Dynamics',
            'rationale': 'TRIZ resolves innovation-vs-feasibility through systematic inventive principles'
        })

    # 3. Data-Intuition split (White vs Red)
    if hats['white_hat'].data_sufficiency == 'insufficient' and \
       hats['red_hat'].gut_feeling in ['positive', 'strongly_positive']:
        contradictions.append({
            'type': 'data_intuition',
            'severity': 'medium',
            'description': f"Data is insufficient ({hats['white_hat'].summary}) "
                          f"but intuition says proceed ({hats['red_hat'].summary})",
            'framework': 'Monte Carlo',
            'confidence': 0.70,
            'rationale': 'Monte Carlo simulation models uncertainty ranges when hard data is limited'
        })

    # 4. Cross-specialist disagreement on priority
    specialist_priorities = extract_specialist_priorities(consilium_output)
    if specialist_priorities:
        priority_variance = calculate_variance(specialist_priorities)
        if priority_variance >= 0.40:
            contradictions.append({
                'type': 'specialist_divergence',
                'severity': 'high',
                'description': f"Specialists diverge on priorities "
                              f"(variance: {priority_variance*100:.0f}%)",
                'framework': 'TRIZ',
                'confidence': 0.75 + (priority_variance * 0.15),
                'rationale': 'High specialist divergence indicates underlying contradiction in goals'
            })

    # 5. Blue Hat process concern - complexity flag
    if hats['blue_hat'].complexity_flag == 'high':
        contradictions.append({
            'type': 'complexity_overload',
            'severity': 'medium',
            'description': 'Blue Hat flags excessive complexity in approach',
            'framework': 'Design Thinking',
            'confidence': 0.70,
            'rationale': 'Design Thinking helps simplify through empathy-first decomposition'
        })

    return contradictions


def calculate_divergence(consilium_output):
    """
    Calculates overall divergence score (0.0 to 1.0) across all hat outputs.
    Used for threshold checking.
    """
    hats = parse_six_hats(consilium_output)

    # Convert each hat's stance to a numeric score (-1 to +1)
    stances = {
        'white': score_data_stance(hats['white_hat']),
        'red': score_emotional_stance(hats['red_hat']),
        'black': score_risk_stance(hats['black_hat']),
        'yellow': score_benefit_stance(hats['yellow_hat']),
        'green': score_innovation_stance(hats['green_hat']),
        'blue': score_process_stance(hats['blue_hat'])
    }

    # Calculate variance across stances
    values = list(stances.values())
    mean = sum(values) / len(values)
    variance = sum((v - mean) ** 2 for v in values) / len(values)

    # Normalize to 0-1 range (max theoretical variance is 1.0)
    return min(variance, 1.0)
```

---

### 2.3 Scoring Conflict Triggers

After MCDA scoring in Step 5, certain criterion combinations indicate
framework opportunities. These triggers detect when scores create
contradictions or reveal missing analysis.

**MCDA Criteria Conflicts:**

```yaml
scoring_conflicts:
  # === UNIVERSAL CONFLICTS (Any Domain) ===

  high_impact_high_effort:
    trigger: Impact >= 8 AND Effort >= 8
    framework: TRIZ
    confidence: 0.75
    severity: high
    message: "High impact requires high effort - TRIZ can find breakthrough to reduce effort"
    triz_contradiction: "We want maximum impact (parameter to improve) without excessive effort (parameter that worsens)"

  high_confidence_low_alignment:
    trigger: Confidence >= 8 AND Strategic_Alignment <= 4
    framework: OKRs
    confidence: 0.70
    severity: medium
    message: "You're confident in execution but unclear on strategy - OKRs can align this project with goals"

  high_passion_low_feasibility:
    trigger: Passion >= 8 AND Feasibility <= 4
    framework: Lean Canvas
    confidence: 0.72
    severity: medium
    message: "Strong passion but feasibility concerns - Lean Canvas validates if a viable path exists"

  high_urgency_low_resources:
    trigger: Urgency >= 7 AND Resources <= 4
    framework: Eisenhower
    confidence: 0.70
    severity: medium
    message: "Urgent but under-resourced - Eisenhower matrix helps prioritize what actually matters"

  # === FINANCE-SPECIFIC CONFLICTS ===

  high_risk_high_return:
    trigger: Risk >= 7 AND Expected_Value >= 8
    domain_required: finance
    framework: Real Options
    confidence: 0.80
    severity: high
    message: "High uncertainty with high potential return - Real Options quantifies the value of deferring decisions"

  uncertain_valuation:
    trigger: Confidence <= 5 AND Financial_Impact >= 7
    domain_required: finance
    framework: Monte Carlo
    confidence: 0.78
    severity: high
    message: "Low confidence in a high-stakes financial decision - Monte Carlo simulation models the range of outcomes"

  long_payback_high_npv:
    trigger: Time_Horizon >= 7 AND Financial_Impact >= 7
    domain_required: finance
    framework: DCF
    confidence: 0.82
    severity: medium
    message: "Long-term financial commitment - DCF analysis properly discounts future cash flows"

  # === HEALTH-SPECIFIC CONFLICTS ===

  high_motivation_low_consistency:
    trigger: Passion >= 8 AND Consistency <= 4
    domain_required: health
    framework: Atomic Habits
    confidence: 0.80
    severity: high
    message: "High motivation but consistency issues - Atomic Habits builds reliable systems"

  ambitious_goal_no_baseline:
    trigger: Impact >= 8 AND Baseline_Data <= 3
    domain_required: health
    framework: Progressive Overload
    confidence: 0.75
    severity: medium
    message: "Ambitious fitness goal without baseline - Progressive Overload provides structured path from current to target"

  # === PERSONAL-SPECIFIC CONFLICTS ===

  learning_goal_time_pressure:
    trigger: Learning_Curve >= 7 AND Time_Pressure >= 7
    domain_required: personal
    framework: Deliberate Practice
    confidence: 0.78
    severity: high
    message: "Need to learn fast - Deliberate Practice is the most efficient skill acquisition method"

  many_goals_low_focus:
    trigger: Goal_Count >= 3 AND Focus_Score <= 4
    domain_required: personal
    framework: GTD
    confidence: 0.75
    severity: medium
    message: "Multiple goals competing for attention - GTD organizes and captures everything so nothing slips"
```

**Detection Algorithm:**

```python
def detect_scoring_conflicts(mcda_scores, domain):
    """
    Analyzes MCDA scores for conflict patterns.
    Returns list of conflicts with framework recommendations.

    Args:
        mcda_scores: dict of criterion_name -> score (1-10)
        domain: str - primary domain from keyword detection
    """
    conflicts = []

    # === Universal Conflicts ===

    impact = mcda_scores.get('impact', mcda_scores.get('potential_impact', 0))
    effort = mcda_scores.get('effort', mcda_scores.get('resource_requirement', 0))
    confidence = mcda_scores.get('confidence', 0)
    alignment = mcda_scores.get('strategic_alignment', 0)
    passion = mcda_scores.get('passion', mcda_scores.get('motivation', 0))
    feasibility = mcda_scores.get('feasibility', 0)
    urgency = mcda_scores.get('urgency', 0)
    resources = mcda_scores.get('resources', mcda_scores.get('resource_availability', 0))

    if impact >= 8 and effort >= 8:
        conflicts.append({
            'type': 'high_impact_high_effort',
            'framework': 'TRIZ',
            'confidence': 0.75,
            'severity': 'high',
            'rationale': f'Impact={impact}/10 but Effort={effort}/10 - '
                        f'TRIZ can resolve this contradiction systematically',
            'scores_involved': {'impact': impact, 'effort': effort},
            'trigger': 'scoring_conflict'
        })

    if confidence >= 8 and alignment <= 4:
        conflicts.append({
            'type': 'high_confidence_low_alignment',
            'framework': 'OKRs',
            'confidence': 0.70,
            'severity': 'medium',
            'rationale': f'Confidence={confidence}/10 but Alignment={alignment}/10 - '
                        f'OKRs connect this project to strategic goals',
            'scores_involved': {'confidence': confidence, 'strategic_alignment': alignment},
            'trigger': 'scoring_conflict'
        })

    if passion >= 8 and feasibility <= 4:
        conflicts.append({
            'type': 'high_passion_low_feasibility',
            'framework': 'Lean Canvas',
            'confidence': 0.72,
            'severity': 'medium',
            'rationale': f'Passion={passion}/10 but Feasibility={feasibility}/10 - '
                        f'Lean Canvas validates whether a viable path exists',
            'scores_involved': {'passion': passion, 'feasibility': feasibility},
            'trigger': 'scoring_conflict'
        })

    if urgency >= 7 and resources <= 4:
        conflicts.append({
            'type': 'high_urgency_low_resources',
            'framework': 'Eisenhower',
            'confidence': 0.70,
            'severity': 'medium',
            'rationale': f'Urgency={urgency}/10 but Resources={resources}/10 - '
                        f'Eisenhower helps ruthlessly prioritize',
            'scores_involved': {'urgency': urgency, 'resources': resources},
            'trigger': 'scoring_conflict'
        })

    # === Domain-Specific Conflicts ===

    if domain == 'finance':
        risk = mcda_scores.get('risk', 0)
        expected_value = mcda_scores.get('expected_value', mcda_scores.get('npv', 0))
        financial_impact = mcda_scores.get('financial_impact', impact)
        time_horizon = mcda_scores.get('time_horizon', 0)

        if risk >= 7 and expected_value >= 8:
            conflicts.append({
                'type': 'high_risk_high_return',
                'framework': 'Real Options',
                'confidence': 0.80,
                'severity': 'high',
                'rationale': f'Risk={risk}/10 with Expected Value={expected_value}/10 - '
                            f'Real Options quantifies flexibility value',
                'scores_involved': {'risk': risk, 'expected_value': expected_value},
                'trigger': 'scoring_conflict'
            })

        if confidence <= 5 and financial_impact >= 7:
            conflicts.append({
                'type': 'uncertain_valuation',
                'framework': 'Monte Carlo',
                'confidence': 0.78,
                'severity': 'high',
                'rationale': f'Confidence={confidence}/10 on Financial Impact={financial_impact}/10 - '
                            f'Monte Carlo models uncertainty ranges',
                'scores_involved': {'confidence': confidence, 'financial_impact': financial_impact},
                'trigger': 'scoring_conflict'
            })

        if time_horizon >= 7 and financial_impact >= 7:
            conflicts.append({
                'type': 'long_payback_high_npv',
                'framework': 'DCF',
                'confidence': 0.82,
                'severity': 'medium',
                'rationale': f'Time Horizon={time_horizon}/10 with Impact={financial_impact}/10 - '
                            f'DCF properly discounts future cash flows',
                'scores_involved': {'time_horizon': time_horizon, 'financial_impact': financial_impact},
                'trigger': 'scoring_conflict'
            })

    if domain == 'health':
        consistency = mcda_scores.get('consistency', 0)
        baseline = mcda_scores.get('baseline_data', mcda_scores.get('current_level', 0))

        if passion >= 8 and consistency <= 4:
            conflicts.append({
                'type': 'high_motivation_low_consistency',
                'framework': 'Atomic Habits',
                'confidence': 0.80,
                'severity': 'high',
                'rationale': f'Passion={passion}/10 but Consistency={consistency}/10 - '
                            f'Atomic Habits builds reliable daily systems',
                'scores_involved': {'passion': passion, 'consistency': consistency},
                'trigger': 'scoring_conflict'
            })

        if impact >= 8 and baseline <= 3:
            conflicts.append({
                'type': 'ambitious_goal_no_baseline',
                'framework': 'Progressive Overload',
                'confidence': 0.75,
                'severity': 'medium',
                'rationale': f'Impact={impact}/10 but Baseline={baseline}/10 - '
                            f'Progressive Overload creates structured path from current to target',
                'scores_involved': {'impact': impact, 'baseline_data': baseline},
                'trigger': 'scoring_conflict'
            })

    if domain == 'personal':
        learning_curve = mcda_scores.get('learning_curve', 0)
        time_pressure = mcda_scores.get('time_pressure', urgency)
        goal_count = mcda_scores.get('goal_count', 0)
        focus_score = mcda_scores.get('focus', 0)

        if learning_curve >= 7 and time_pressure >= 7:
            conflicts.append({
                'type': 'learning_goal_time_pressure',
                'framework': 'Deliberate Practice',
                'confidence': 0.78,
                'severity': 'high',
                'rationale': f'Learning Curve={learning_curve}/10 with Time Pressure={time_pressure}/10 - '
                            f'Deliberate Practice is most efficient skill acquisition method',
                'scores_involved': {'learning_curve': learning_curve, 'time_pressure': time_pressure},
                'trigger': 'scoring_conflict'
            })

        if goal_count >= 3 and focus_score <= 4:
            conflicts.append({
                'type': 'many_goals_low_focus',
                'framework': 'GTD',
                'confidence': 0.75,
                'severity': 'medium',
                'rationale': f'Goal Count={goal_count} with Focus={focus_score}/10 - '
                            f'GTD organizes and captures everything so nothing slips',
                'scores_involved': {'goal_count': goal_count, 'focus': focus_score},
                'trigger': 'scoring_conflict'
            })

    # === Missing Domain Criteria Detection ===
    missing = detect_missing_domain_criteria(mcda_scores, domain)
    if missing:
        conflicts.extend(missing)

    # Sort by confidence descending
    conflicts.sort(key=lambda x: x['confidence'], reverse=True)

    return conflicts[:3]  # Max 3 suggestions


def detect_missing_domain_criteria(mcda_scores, domain):
    """
    Detects when domain-critical criteria are missing from MCDA scoring.
    This often indicates a framework gap.
    """
    missing = []
    criteria_names = set(mcda_scores.keys())

    if domain == 'finance':
        finance_criteria = {'npv', 'roi', 'risk', 'payback_period', 'cash_flow'}
        present = criteria_names.intersection(finance_criteria)
        if len(present) == 0:
            missing.append({
                'type': 'missing_domain_criterion',
                'framework': 'NPV',
                'confidence': 0.90,
                'severity': 'high',
                'rationale': 'Finance project without any financial analysis criteria - '
                            'add NPV or ROI criterion for proper evaluation',
                'trigger': 'missing_criterion'
            })

    if domain == 'health':
        health_criteria = {'baseline_data', 'current_level', 'body_composition', 'fitness_level'}
        present = criteria_names.intersection(health_criteria)
        if len(present) == 0:
            missing.append({
                'type': 'missing_domain_criterion',
                'framework': 'Progressive Overload',
                'confidence': 0.75,
                'severity': 'medium',
                'rationale': 'Health project without baseline measurement - '
                            'Progressive Overload requires knowing where you start',
                'trigger': 'missing_criterion'
            })

    if domain == 'business':
        business_criteria = {'market_size', 'customer_segment', 'competitive_advantage'}
        present = criteria_names.intersection(business_criteria)
        if len(present) == 0 and mcda_scores.get('financial_impact', 0) >= 7:
            missing.append({
                'type': 'missing_domain_criterion',
                'framework': 'Lean Canvas',
                'confidence': 0.72,
                'severity': 'medium',
                'rationale': 'High-impact business project without market analysis - '
                            'Lean Canvas validates problem-solution fit',
                'trigger': 'missing_criterion'
            })

    return missing
```

---

### 2.4 Planning Contradiction Triggers

During Step 8 (Deep Plan), L2+ task breakdowns may reveal contradictions
between goals, constraints, and methods. These are detected via keyword
co-occurrence and semantic opposition.

**Planning Contradiction Definitions:**

```yaml
planning_contradictions:
  speed_quality:
    positive_keywords: ["fast", "quick", "speed", "launch", "rapid", "asap", "immediately"]
    negative_keywords: ["quality", "thorough", "testing", "reliable", "robust", "stable"]
    framework: TRIZ
    confidence: 0.85
    triz_hint: "Principle #15 Dynamics, #28 Mechanics Substitution, #35 Parameter Change"
    message: "Speed vs quality contradiction detected - TRIZ has 40 principles for exactly this"

  budget_scope:
    positive_keywords: ["limited budget", "tight budget", "low cost", "minimal spend", "bootstrap"]
    negative_keywords: ["comprehensive", "full featured", "enterprise", "scalable", "production-ready"]
    framework: TRIZ
    alt_framework: Lean Canvas
    confidence: 0.75
    triz_hint: "Principle #1 Segmentation, #2 Extraction, #25 Self-Service"
    message: "Budget vs scope contradiction - TRIZ or Lean Canvas can find the viable subset"

  time_learning:
    positive_keywords: ["deadline", "urgent", "time limit", "due date", "by next week"]
    negative_keywords: ["learn", "new skill", "never done", "first time", "unfamiliar", "no experience"]
    framework: Deliberate Practice
    alt_framework: Pomodoro
    confidence: 0.80
    message: "Time pressure with learning curve - Deliberate Practice + Pomodoro optimize skill acquisition speed"

  scale_simplicity:
    positive_keywords: ["scale", "grow", "expand", "millions", "enterprise"]
    negative_keywords: ["simple", "lightweight", "minimal", "clean", "small team"]
    framework: TRIZ
    confidence: 0.72
    triz_hint: "Principle #5 Merging, #17 Another Dimension, #40 Composite Materials"
    message: "Scale vs simplicity tension - TRIZ resolves 'grow without complexity' contradictions"

  automation_customization:
    positive_keywords: ["automate", "template", "standardize", "consistent", "repeatable"]
    negative_keywords: ["custom", "personalize", "unique", "tailored", "case-by-case"]
    framework: TRIZ
    confidence: 0.78
    triz_hint: "Principle #3 Local Quality, #15 Dynamics, #35 Parameter Change"
    message: "Automation vs customization - TRIZ finds solutions that are both standardized AND flexible"

  consistency_flexibility:
    positive_keywords: ["routine", "habit", "daily", "consistent", "systematic"]
    negative_keywords: ["flexible", "adapt", "change", "variety", "spontaneous"]
    framework: Atomic Habits
    alt_framework: GTD
    confidence: 0.73
    message: "Consistency vs flexibility - Atomic Habits framework handles habit stacking with flexibility"
```

**Detection Algorithm:**

```python
def detect_planning_contradictions(deep_plan_text):
    """
    Scans L2+ deep plan text for co-occurring contradictory keywords.
    Returns list of detected contradictions with framework recommendations.
    """
    text = deep_plan_text.lower()
    contradictions = []

    for name, pattern in PLANNING_CONTRADICTIONS.items():
        positive_found = any(kw in text for kw in pattern['positive_keywords'])
        negative_found = any(kw in text for kw in pattern['negative_keywords'])

        if positive_found and negative_found:
            # Count how many keywords from each side
            pos_count = sum(1 for kw in pattern['positive_keywords'] if kw in text)
            neg_count = sum(1 for kw in pattern['negative_keywords'] if kw in text)

            # Confidence scales with number of keyword matches
            base_confidence = pattern['confidence']
            match_boost = min((pos_count + neg_count - 2) * 0.03, 0.10)
            final_confidence = min(base_confidence + match_boost, 0.95)

            result = {
                'type': name,
                'framework': pattern['framework'],
                'confidence': round(final_confidence, 2),
                'rationale': pattern['message'],
                'positive_matches': pos_count,
                'negative_matches': neg_count,
                'trigger': 'planning_contradiction'
            }

            if 'triz_hint' in pattern:
                result['triz_hint'] = pattern['triz_hint']
            if 'alt_framework' in pattern:
                result['alt_framework'] = pattern['alt_framework']

            contradictions.append(result)

    # Sort by confidence
    contradictions.sort(key=lambda x: x['confidence'], reverse=True)

    return contradictions[:3]  # Max 3 per scan
```

---

## 3. Framework Recommendation Engine

### 3.1 Recommendation Matrix

Aligned with method-rankings.yaml tier structure.
All applicability scores reference domain-framework-integration.md research data.

**Primary Recommendations by Domain:**

```yaml
business_recommendations:
  tier_1:  # Always suggest if domain = business
    - framework: OKRs
      slug: okrs
      score: 23/25
      applicability: 92%
      when: Strategic project, growth focus, goal alignment
      confidence_base: 0.85
      time_investment: 45-90 min
      boost_keywords: ["goal", "strategy", "growth", "alignment", "quarterly"]
      synergies: [Six_Hats, SWOT, PDCA]

    - framework: Lean Canvas
      slug: lean-canvas
      score: 22/25
      applicability: 88%
      when: Startup, new product, MVP validation
      confidence_base: 0.80
      time_investment: 20-90 min
      boost_keywords: ["startup", "mvp", "launch", "product", "validate"]
      synergies: [TRIZ, Design_Thinking, Jobs_to_be_Done]

  tier_2:  # Suggest if specific triggers match
    - framework: SWOT
      slug: swot
      score: 21/25
      applicability: 84%
      when: Mature business, competitive analysis, strategic decisions
      confidence_base: 0.70
      time_investment: 10-120 min
      trigger_keywords: ["competition", "market", "strengths", "weaknesses", "opportunity", "threat"]
      synergies: [Six_Hats, BMC, OKRs]

    - framework: Business Model Canvas
      slug: bmc
      score: 21/25
      applicability: 84%
      when: Business model design, revenue model, partnerships
      confidence_base: 0.75
      time_investment: 15-180 min
      trigger_keywords: ["business model", "revenue", "partners", "channels", "value proposition"]
      synergies: [TRIZ, Jobs_to_be_Done, SWOT]

    - framework: Porter's Five Forces
      slug: five-forces
      score: 20/25
      applicability: 80%
      when: Market entry, competitive landscape analysis
      confidence_base: 0.68
      time_investment: 15-240 min
      trigger_keywords: ["industry", "market entry", "competition", "suppliers", "barriers"]
      synergies: [SWOT, BMC]

  tier_3:  # Only if very specific context
    - framework: Balanced Scorecard
      slug: balanced-scorecard
      applicability: 76%
      when: Large organization, strategy execution, multi-perspective measurement
      confidence_base: 0.60
      time_investment: 60-180 min
      trigger_keywords: ["kpi", "dashboard", "balanced", "scorecard", "perspectives"]

finance_recommendations:
  tier_1:
    - framework: NPV / DCF
      slug: npv-dcf
      score: 24/25
      applicability: 96%
      when: Any investment decision with cash flows
      confidence_base: 0.90
      time_investment: 30-120 min
      boost_keywords: ["investment", "cash flow", "valuation", "discount rate", "future value"]
      synergies: [Monte_Carlo, Real_Options]

    - framework: Monte Carlo Simulation
      slug: monte-carlo
      score: 19/25
      applicability: 76%
      when: High uncertainty, range of outcomes needed
      confidence_base: 0.75
      time_investment: 45-180 min
      trigger_keywords: ["uncertain", "risk", "volatile", "unpredictable", "probability", "scenario"]
      synergies: [NPV, Real_Options, CAPM]

  tier_2:
    - framework: Real Options
      slug: real-options
      score: 18/25
      applicability: 72%
      when: Decision can be staged or deferred, flexibility has value
      confidence_base: 0.70
      time_investment: 60-180 min
      trigger_keywords: ["wait", "defer", "flexibility", "staged", "option", "reversible"]
      synergies: [NPV, Monte_Carlo]

    - framework: CAPM
      slug: capm
      applicability: 68%
      when: Risk-adjusted returns, portfolio decisions
      confidence_base: 0.65
      time_investment: 30-90 min
      trigger_keywords: ["beta", "market return", "risk premium", "systematic risk"]

  tier_3:
    - framework: Kelly Criterion
      slug: kelly-criterion
      applicability: 60%
      when: Bet sizing, position sizing, optimal allocation
      confidence_base: 0.55
      trigger_keywords: ["bet size", "position size", "optimal allocation", "bankroll"]

    - framework: Sharpe Ratio
      slug: sharpe-ratio
      applicability: 60%
      when: Comparing risk-adjusted returns across investments
      confidence_base: 0.55
      trigger_keywords: ["risk-adjusted", "sharpe", "portfolio comparison"]

health_recommendations:
  tier_1:
    - framework: Progressive Overload
      slug: progressive-overload
      score: high
      applicability: 88%
      when: Strength training, fitness goal, measurable physical improvement
      confidence_base: 0.85
      time_investment: 15-60 min
      boost_keywords: ["gym", "muscle", "strength", "workout", "reps", "sets", "weight"]
      synergies: [SMART, Deliberate_Practice, Pomodoro]

    - framework: Health Belief Model (HBM)
      slug: hbm
      score: 7.8/10
      applicability: 84%
      when: Behavior change, motivation analysis, health decision
      confidence_base: 0.75
      time_investment: 20-60 min
      boost_keywords: ["habit", "change", "motivation", "readiness", "barrier", "belief"]
      synergies: [Atomic_Habits, Growth_Mindset]

  tier_2:
    - framework: Habit Loop
      slug: habit-loop
      applicability: 80%
      when: Building or breaking habits, understanding triggers
      confidence_base: 0.72
      time_investment: 15-45 min
      trigger_keywords: ["cue", "routine", "reward", "trigger", "craving", "loop"]
      synergies: [Atomic_Habits, HBM]

    - framework: Recovery Protocols
      slug: recovery-protocols
      applicability: 72%
      when: Overtraining, injury prevention, rest optimization
      confidence_base: 0.65
      trigger_keywords: ["recovery", "rest", "overtraining", "injury", "sleep", "deload"]

  tier_3:
    - framework: Macro Tracking
      slug: macro-tracking
      applicability: 68%
      when: Nutrition optimization, body composition goals
      confidence_base: 0.60
      trigger_keywords: ["calories", "macros", "protein", "carbs", "fat", "nutrition plan"]

personal_recommendations:
  tier_1:
    - framework: Pomodoro Technique
      slug: pomodoro
      score: 23/25
      applicability: 92%
      when: Time management, focus improvement, deep work
      confidence_base: 0.85
      time_investment: 5-30 min
      boost_keywords: ["time", "focus", "distraction", "productivity", "deep work", "concentration"]
      synergies: [GTD, Deliberate_Practice, Eisenhower]

    - framework: Atomic Habits
      slug: atomic-habits
      score: 23/25
      applicability: 92%
      when: Habit building, behavior change, system design
      confidence_base: 0.85
      time_investment: 15-60 min
      boost_keywords: ["habit", "daily", "routine", "consistency", "system", "compound"]
      synergies: [HBM, Pomodoro, Growth_Mindset]

  tier_2:
    - framework: Eisenhower Matrix
      slug: eisenhower
      applicability: 84%
      when: Prioritization, too many tasks, urgency management
      confidence_base: 0.75
      time_investment: 10-30 min
      trigger_keywords: ["priority", "urgent", "important", "overwhelmed", "too much", "decide"]
      synergies: [GTD, Pareto, Pomodoro]

    - framework: GTD (Getting Things Done)
      slug: gtd
      applicability: 84%
      when: Organizing complex workload, reducing mental overhead
      confidence_base: 0.75
      time_investment: 30-120 min
      trigger_keywords: ["organize", "todo", "inbox", "capture", "next action", "project list"]
      synergies: [Eisenhower, Time_Blocking, Pomodoro]

  tier_3:
    - framework: Growth Mindset
      slug: growth-mindset
      applicability: 80%
      when: Facing difficulty, fear of failure, perfectionism
      confidence_base: 0.65
      trigger_keywords: ["afraid", "fail", "can't", "stuck", "impossible", "talent"]
      synergies: [Deliberate_Practice, PDCA]

    - framework: Deliberate Practice
      slug: deliberate-practice
      applicability: 80%
      when: Skill mastery, plateau-breaking, expert-level performance
      confidence_base: 0.70
      trigger_keywords: ["plateau", "expert", "mastery", "10000 hours", "weakness", "feedback"]
      synergies: [Pomodoro, Growth_Mindset, Progressive_Overload]
```

---

### 3.2 Confidence Calculation

Multi-signal confidence scoring with diminishing returns and hard cap at 0.95.

**Confidence Score Formula:**

```python
def calculate_confidence(framework_entry, context):
    """
    Calculates final confidence score for a framework suggestion.

    Args:
        framework_entry: dict from recommendation matrix
        context: dict with trigger information
            - keyword_matches_high: int
            - keyword_matches_medium: int
            - keyword_matches_low: int
            - specialist_present: bool
            - trigger_count: int (how many different trigger types fired)
            - past_effectiveness: float (1-5 star average, 0 if no history)
            - user_declined_before: bool
            - synergy_partner_active: bool (another active framework has 4-5 star synergy)
    """
    confidence = framework_entry['confidence_base']

    # === Keyword Match Boost ===
    # High-confidence keywords: +5% each (max +15%)
    kw_high_boost = min(context.get('keyword_matches_high', 0) * 0.05, 0.15)
    # Medium-confidence keywords: +3% each (max +9%)
    kw_med_boost = min(context.get('keyword_matches_medium', 0) * 0.03, 0.09)
    # Low-confidence keywords: +1% each (max +3%)
    kw_low_boost = min(context.get('keyword_matches_low', 0) * 0.01, 0.03)
    confidence += kw_high_boost + kw_med_boost + kw_low_boost

    # === Consilium Signal Boost ===
    # If matched specialist is present in consilium (+10%)
    if context.get('specialist_present', False):
        confidence += 0.10

    # === Multiple Trigger Types Boost ===
    # If >1 trigger type detected (keyword + scoring conflict, etc.) (+15%)
    trigger_count = context.get('trigger_count', 1)
    if trigger_count > 1:
        confidence += 0.15
    if trigger_count > 2:
        confidence += 0.05  # Additional +5% for 3+ triggers

    # === User History Adjustments ===
    past_effectiveness = context.get('past_effectiveness', 0)
    if past_effectiveness >= 4.0:
        confidence += 0.05   # Worked well before
    elif past_effectiveness > 0 and past_effectiveness <= 2.0:
        confidence -= 0.10   # Worked poorly before

    if context.get('user_declined_before', False):
        confidence -= 0.15   # User has declined this framework before

    # === Synergy Boost ===
    # If another framework with 4-5 star synergy is already active (+8%)
    if context.get('synergy_partner_active', False):
        confidence += 0.08

    # === Hard Cap ===
    confidence = max(0.0, min(confidence, 0.95))

    return round(confidence, 2)
```

**Example Calculations:**

```
Example 1: Lean Canvas for "I want to launch a startup MVP"
  Base: 0.80
  + Keywords: "startup" (high) + "mvp" (high) + "launch" (high) = +0.15 (capped)
  + Specialist: Product Manager in consilium = +0.10
  + Multiple triggers: Keywords + Domain match = +0.15
  = 1.20 -> Capped at 0.95 (95% confidence)

Example 2: TRIZ for scoring conflict (Impact=9, Effort=9)
  Base: 0.75
  + Scoring conflict detected = already in base
  + No keyword boost (trigger was scoring, not keyword)
  + Consilium divergence also detected = +0.15 (2 triggers)
  = 0.90 (90% confidence)

Example 3: GTD for "I want to organize my projects"
  Base: 0.75
  + Keywords: "organize" (medium) + "projects" (low) = +0.03 + 0.01 = +0.04
  + No specialist = +0.00
  + Single trigger = +0.00
  + User declined GTD last session = -0.15
  = 0.64 -> Below 70% threshold -> Do NOT show suggestion

Example 4: NPV for finance project with no financial criteria
  Base: 0.90
  + Missing criterion trigger = already in base
  + Domain = finance = +0.00 (already reflected)
  + Keywords: "investment" (high) = +0.05
  = 0.95 (95% confidence - strong recommendation)
```

---

### 3.3 Multi-Framework Suggestions

When multiple frameworks are relevant, present them together with synergy notes.
Never show more than 3 suggestions. Leverage framework-synergy-matrix.csv data.

**Multi-Framework Rules:**

```yaml
multi_framework_rules:
  max_suggestions: 3
  min_confidence_for_inclusion: 0.65  # Below 0.70 threshold but shown as "also consider"
  confidence_gap_max: 0.20  # Don't show if >20% gap from top suggestion

  synergy_boost_rules:
    # If two suggested frameworks have 5-star synergy, boost both +10%
    synergy_5_star_boost: 0.10
    # If 4-star synergy, boost both +5%
    synergy_4_star_boost: 0.05
    # If 3-star synergy, no boost
    synergy_3_star_boost: 0.00

  presentation_order:
    # Primary: highest confidence
    # Secondary: highest synergy with primary
    # Tertiary: next highest confidence (if within gap_max)
    sort: confidence_desc_then_synergy

  domain_combination_rules:
    # Multi-domain projects: suggest 1 framework per detected domain
    multi_domain_detected: true
    max_per_domain: 1
    confidence_multiplier: 0.95  # Slightly lower per-framework confidence in multi-domain
```

**Selection Algorithm:**

```python
def select_multi_framework_suggestions(all_candidates, synergy_matrix):
    """
    Selects optimal set of framework suggestions (max 3).
    Accounts for synergy and avoids redundancy.

    Args:
        all_candidates: list of {framework, confidence, domain, trigger} dicts
        synergy_matrix: dict of (framework_a, framework_b) -> synergy_score
    """
    # Sort by confidence
    candidates = sorted(all_candidates, key=lambda x: x['confidence'], reverse=True)

    if not candidates:
        return []

    selected = [candidates[0]]  # Always include top candidate
    top_confidence = candidates[0]['confidence']

    for candidate in candidates[1:]:
        if len(selected) >= 3:
            break

        # Check confidence gap
        if top_confidence - candidate['confidence'] > 0.20:
            break

        # Check for redundancy (same domain and similar framework type)
        is_redundant = any(
            s['domain'] == candidate['domain'] and
            s['framework'] == candidate['framework']
            for s in selected
        )
        if is_redundant:
            continue

        # Check synergy with already selected
        best_synergy = 0
        for s in selected:
            pair_key = tuple(sorted([s['framework'], candidate['framework']]))
            synergy = synergy_matrix.get(pair_key, 0)
            best_synergy = max(best_synergy, synergy)

        # Apply synergy boost
        if best_synergy >= 5:
            candidate['confidence'] = min(candidate['confidence'] + 0.10, 0.95)
            candidate['synergy_note'] = f"5-star synergy with {selected[0]['framework']}"
        elif best_synergy >= 4:
            candidate['confidence'] = min(candidate['confidence'] + 0.05, 0.95)
            candidate['synergy_note'] = f"4-star synergy with {selected[0]['framework']}"

        selected.append(candidate)

    return selected
```

---

## 4. Suggestion Presentation

### 4.1 UI/UX Templates

**Single Framework Suggestion:**

```markdown
---

**Framework Suggestion**

Based on your project description, I recommend **{Framework Name}** ({Domain} domain).

**Why this framework:**
- {Rationale point 1 - primary trigger reason}
- {Rationale point 2 - supporting evidence}
- {Trigger explanation - what specifically triggered this}

**Time investment:** {quick|moderate|intensive} ({X-Y min})
- Quick analysis: {quick_time}
- Full analysis: {full_time}

**What you'll get:**
- {Output 1 - specific deliverable}
- {Output 2 - specific deliverable}
- {Scoring impact - how it changes MCDA}

**Confidence:** {X}% match for this project

**Options:** [Use {Framework}] [Tell me more] [Skip]

---
```

**Multiple Framework Suggestion:**

```markdown
---

**Framework Suggestions** (Top {N} for your project)

**1. {Framework 1}** - {Confidence}% match
   Domain: {domain} | Time: {X min} | Best for: {use case}
   Why: {one-line rationale}

**2. {Framework 2}** - {Confidence}% match
   Domain: {domain} | Time: {Y min} | Best for: {use case}
   Why: {one-line rationale}

**3. {Framework 3}** - {Confidence}% match
   Domain: {domain} | Time: {Z min} | Best for: {use case}
   Why: {one-line rationale}

**Synergy Note:** {Framework 1} + {Framework 2} work great together
({synergy_score}-star synergy from matrix)

**Options:** [Use #1 + #2 combo] [Just #1] [Just #2] [Skip all]

---
```

**TRIZ-Specific Suggestion (Contradiction Detected):**

```markdown
---

**Contradiction Detected - TRIZ Recommended**

I detected a contradiction in your project:
> "{Contradiction description}"

This is exactly what TRIZ was designed for.

**The contradiction:**
- You want: {desired parameter to improve}
- But it causes: {parameter that worsens}

**Relevant TRIZ principles:**
- Principle #{N1}: {Name} - {one-line description}
- Principle #{N2}: {Name} - {one-line description}
- Principle #{N3}: {Name} - {one-line description}

**Time:** {10-30 min} for Quick TRIZ, {2-4 hr} for full ARIZ

**Confidence:** {X}% - {trigger type explanation}

**Options:** [Run Quick TRIZ] [Run Full ARIZ] [Tell me more] [Skip]

---
```

**Below-Threshold Tentative Suggestion (50-69%):**

```markdown
---

**Possible Framework Match** (tentative)

This might be relevant, though I'm not highly confident:

**{Framework Name}** ({Confidence}% match)
- {Brief rationale}
- {Why confidence is lower}

This could help if: {condition that would make it more relevant}

**Options:** [Use anyway] [Not relevant] [Skip]

---
```

---

### 4.2 Integration Points

**Step 1 (Collect Ideas) - After empathy questions:**

```python
def auto_suggest_after_step_1(user_input, empathy_responses):
    """
    Runs after user describes their idea and answers empathy questions.
    Detects domain and suggests tier-1 frameworks.
    """
    # Combine all user text
    full_text = f"{user_input} {' '.join(empathy_responses.values())}"

    # Detect domain
    detection = detect_domain_from_keywords(full_text)

    if detection['trigger_type'] == 'none':
        return None  # No suggestion - domain unclear

    domain = detection['primary_domain']
    confidence = detection['primary_confidence']

    # Get tier 1 frameworks for detected domain
    recommendations = get_recommendations(domain)
    tier_1 = [r for r in recommendations if r.get('tier', 99) == 1]

    # Calculate confidence for each
    suggestions = []
    for fw in tier_1:
        context = build_context_from_keywords(full_text, fw)
        fw_confidence = calculate_confidence(fw, context)

        if fw_confidence >= 0.70:
            suggestions.append({
                'framework': fw['framework'],
                'confidence': fw_confidence,
                'domain': domain,
                'rationale': f"Your project is in the {domain} domain. "
                           f"{fw['framework']} is tier-1 for {fw['when']}.",
                'time_investment': fw['time_investment'],
                'trigger': 'step_1_domain_detection'
            })

    # Check for secondary domain
    if detection['secondary_domain']:
        sec_domain = detection['secondary_domain']
        sec_recommendations = get_recommendations(sec_domain)
        sec_tier_1 = [r for r in sec_recommendations if r.get('tier', 99) == 1]
        if sec_tier_1:
            fw = sec_tier_1[0]
            context = build_context_from_keywords(full_text, fw)
            fw_confidence = calculate_confidence(fw, context)
            fw_confidence *= 0.95  # Secondary domain penalty
            if fw_confidence >= 0.65:
                suggestions.append({
                    'framework': fw['framework'],
                    'confidence': round(fw_confidence, 2),
                    'domain': sec_domain,
                    'rationale': f"Secondary domain detected: {sec_domain}. "
                               f"Consider {fw['framework']} for {fw['when']}.",
                    'time_investment': fw['time_investment'],
                    'trigger': 'step_1_secondary_domain'
                })

    # Select and present
    if suggestions:
        final = select_multi_framework_suggestions(suggestions, SYNERGY_MATRIX)
        present_suggestions(final)
        return final

    return None
```

**Step 4 (Consilium) - After gathering all hat views:**

```python
def auto_suggest_after_step_4(consilium_output):
    """
    Runs after consilium completes all six hat perspectives.
    Checks for divergence and contradictions.
    """
    # Check overall divergence
    divergence = calculate_divergence(consilium_output)

    suggestions = []

    if divergence >= 0.40:
        suggestions.append({
            'framework': 'TRIZ',
            'confidence': 0.75 + (divergence * 0.20),  # Higher divergence = higher confidence
            'domain': 'universal',
            'rationale': f"Consilium shows {divergence*100:.0f}% divergence across perspectives. "
                        f"This indicates an underlying contradiction that TRIZ can resolve.",
            'trigger': 'consilium_divergence',
            'divergence_score': divergence
        })

    # Check for specific contradictions
    contradictions = detect_contradiction_from_consilium(consilium_output)
    for c in contradictions:
        # Avoid duplicate TRIZ suggestions
        if c['framework'] == 'TRIZ' and any(s['framework'] == 'TRIZ' for s in suggestions):
            # Merge - take higher confidence
            existing = next(s for s in suggestions if s['framework'] == 'TRIZ')
            if c['confidence'] > existing['confidence']:
                existing['confidence'] = c['confidence']
                existing['rationale'] += f"\nAdditional: {c['description']}"
            continue

        suggestions.append({
            'framework': c['framework'],
            'confidence': c['confidence'],
            'domain': 'universal',
            'rationale': c['description'] + ' - ' + c['rationale'],
            'trigger': 'consilium_contradiction',
            'contradiction_type': c['type']
        })

    # Present if any
    if suggestions:
        final = select_multi_framework_suggestions(suggestions, SYNERGY_MATRIX)
        present_suggestions(final)
        return final

    return None
```

**Step 5 (Scoring) - After MCDA complete:**

```python
def auto_suggest_after_step_5(mcda_scores, domain):
    """
    Runs after MCDA scoring is complete.
    Detects scoring conflicts, missing criteria, and domain opportunities.
    """
    # Get scoring conflicts
    conflicts = detect_scoring_conflicts(mcda_scores, domain)

    suggestions = []
    for conflict in conflicts:
        suggestions.append({
            'framework': conflict['framework'],
            'confidence': conflict['confidence'],
            'domain': domain,
            'rationale': conflict['rationale'],
            'trigger': conflict['trigger'],
            'conflict_type': conflict['type'],
            'scores_involved': conflict.get('scores_involved', {})
        })

    # Present if any
    if suggestions:
        final = select_multi_framework_suggestions(suggestions, SYNERGY_MATRIX)
        present_suggestions(final)
        return final

    return None
```

**Step 8 (Deep Plan) - During L2+ planning:**

```python
def auto_suggest_during_step_8(deep_plan_text, domain):
    """
    Runs during deep plan generation, scanning L2+ headings and content.
    Detects planning contradictions.
    """
    # Detect planning contradictions
    contradictions = detect_planning_contradictions(deep_plan_text)

    suggestions = []
    for c in contradictions:
        primary = {
            'framework': c['framework'],
            'confidence': c['confidence'],
            'domain': domain if domain else 'universal',
            'rationale': c['rationale'],
            'trigger': 'planning_contradiction',
            'contradiction_type': c['type']
        }
        if 'triz_hint' in c:
            primary['triz_hint'] = c['triz_hint']
        suggestions.append(primary)

        # Also suggest alternative framework if available
        if 'alt_framework' in c:
            alt_confidence = c['confidence'] * 0.85  # Alternative is less confident
            if alt_confidence >= 0.65:
                suggestions.append({
                    'framework': c['alt_framework'],
                    'confidence': round(alt_confidence, 2),
                    'domain': domain if domain else 'universal',
                    'rationale': f"Alternative to {c['framework']}: {c['rationale']}",
                    'trigger': 'planning_contradiction_alt'
                })

    # Present if any
    if suggestions:
        final = select_multi_framework_suggestions(suggestions, SYNERGY_MATRIX)
        present_suggestions(final)
        return final

    return None
```

---

## 5. Learning Loop and Feedback

### 5.1 Post-Use Feedback Collection

After a framework is applied, collect effectiveness feedback.

**Feedback Prompt:**

```markdown
---

**Framework Feedback**

You just completed **{Framework Name}** analysis.

How helpful was it for this project?

  [5] Extremely helpful - breakthrough insight or major clarity
  [4] Very helpful - clarified approach significantly
  [3] Moderately helpful - some useful insights
  [2] Slightly helpful - minimal value
  [1] Not helpful - wasted time

Optional: What was most/least useful? ___

[Submit] [Skip feedback]

---
```

**Feedback Storage:**

```yaml
feedback_record:
  framework: "{name}"
  framework_slug: "{slug}"
  domain: "{domain}"
  project_id: "{from workflow-plan.md}"
  project_type: "{from step 1 classification}"
  effectiveness_rating: {1-5}
  confidence_when_suggested: {0.0-0.95}
  triggers_that_fired: ["{trigger_type_1}", "{trigger_type_2}"]
  user_accepted_suggestion: {true|false}
  time_spent_minutes: {actual}
  time_estimated_minutes: {from recommendation}
  user_comment: "{optional free text}"
  timestamp: "{ISO 8601}"
  session_id: "{session identifier}"
```

**Storage Command:**

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:auto-suggest:feedback:{framework_slug}:{project_id}" \
  --content "{JSON feedback_record}"
```

---

### 5.2 Algorithm Refinement

Use accumulated feedback to adjust confidence baselines and trigger weights.

**Refinement Algorithm:**

```python
def refine_confidence_algorithm():
    """
    Runs periodically (monthly or after every 20 feedback entries).
    Adjusts base confidence and trigger weights based on actual effectiveness.
    """
    # Query all feedback from memory
    feedback = memory_search("life-os:auto-suggest:feedback")

    if len(feedback) < 10:
        return  # Not enough data to refine

    # === Framework Base Confidence Adjustment ===
    for framework in ALL_FRAMEWORKS:
        fw_feedback = [f for f in feedback if f['framework'] == framework['name']]
        if len(fw_feedback) < 3:
            continue  # Need at least 3 data points

        # Calculate average effectiveness
        ratings = [f['effectiveness_rating'] for f in fw_feedback]
        avg_rating = sum(ratings) / len(ratings)

        # Adjust base confidence
        if avg_rating >= 4.0:
            adjustment = +0.05  # Boost - consistently effective
        elif avg_rating >= 3.0:
            adjustment = 0.00   # Keep - acceptable
        elif avg_rating >= 2.0:
            adjustment = -0.03  # Slight decrease
        else:
            adjustment = -0.08  # Significant decrease

        framework['confidence_base'] = max(0.40, min(0.95,
            framework['confidence_base'] + adjustment))

    # === Trigger Accuracy Adjustment ===
    for trigger_type in ALL_TRIGGER_TYPES:
        trigger_feedback = [f for f in feedback
                          if trigger_type in f.get('triggers_that_fired', [])]
        if len(trigger_feedback) < 5:
            continue

        # Acceptance rate
        accepted = [f for f in trigger_feedback if f['user_accepted_suggestion']]
        acceptance_rate = len(accepted) / len(trigger_feedback)

        # Effectiveness of accepted suggestions
        accepted_ratings = [f['effectiveness_rating'] for f in accepted]
        avg_accepted_rating = sum(accepted_ratings) / len(accepted_ratings) if accepted_ratings else 0

        # Adjust trigger confidence multiplier
        if acceptance_rate >= 0.70 and avg_accepted_rating >= 3.5:
            trigger_type['confidence_multiplier'] = 1.05  # Slightly boost
        elif acceptance_rate < 0.40:
            trigger_type['confidence_multiplier'] = 0.85  # Reduce
        elif avg_accepted_rating < 2.5:
            trigger_type['confidence_multiplier'] = 0.90  # Reduce

    # === Time Estimate Refinement ===
    for framework in ALL_FRAMEWORKS:
        fw_feedback = [f for f in feedback
                      if f['framework'] == framework['name']
                      and f.get('time_spent_minutes')]
        if len(fw_feedback) < 3:
            continue

        actual_times = [f['time_spent_minutes'] for f in fw_feedback]
        avg_actual = sum(actual_times) / len(actual_times)

        # Update time estimate if consistently off by >30%
        estimated = framework.get('time_investment_avg', 0)
        if estimated > 0:
            ratio = avg_actual / estimated
            if ratio > 1.30:
                framework['time_investment_note'] = f"Usually takes {avg_actual:.0f} min (longer than estimated)"
            elif ratio < 0.70:
                framework['time_investment_note'] = f"Usually takes {avg_actual:.0f} min (faster than estimated)"

    # === Log Refinement Results ===
    log_refinement({
        'timestamp': datetime.now().isoformat(),
        'feedback_count': len(feedback),
        'frameworks_adjusted': [fw['name'] for fw in ALL_FRAMEWORKS if fw.get('_adjusted')],
        'triggers_adjusted': [t['name'] for t in ALL_TRIGGER_TYPES if t.get('_adjusted')]
    })
```

---

### 5.3 Personalization

Learn individual user preferences to improve suggestion relevance over time.

**User Preference Model:**

```python
def build_user_preference_model():
    """
    Builds a preference model from accumulated usage data.
    """
    # Query user's framework usage history
    usage_history = memory_search("life-os:auto-suggest:feedback")
    template_usage = memory_search("life-os:templates:completed")

    preferences = {
        'favorite_frameworks': [],      # Most used AND highest rated (>=4 stars)
        'avoided_frameworks': [],       # Suggested but declined 2+ times
        'effective_frameworks': [],     # Used AND rated 4+ stars
        'ineffective_frameworks': [],   # Used AND rated <=2 stars
        'preferred_complexity': None,   # quick / moderate / intensive
        'preferred_domains': [],        # Domains with most projects
        'suggestion_receptiveness': 0.0 # 0-1: how often user accepts suggestions
    }

    # === Identify Favorites ===
    framework_stats = {}
    for entry in usage_history:
        fw = entry['framework']
        if fw not in framework_stats:
            framework_stats[fw] = {'uses': 0, 'total_rating': 0, 'declined': 0}
        if entry['user_accepted_suggestion']:
            framework_stats[fw]['uses'] += 1
            framework_stats[fw]['total_rating'] += entry['effectiveness_rating']
        else:
            framework_stats[fw]['declined'] += 1

    for fw, stats in framework_stats.items():
        if stats['uses'] >= 2:
            avg = stats['total_rating'] / stats['uses']
            if avg >= 4.0:
                preferences['favorite_frameworks'].append(fw)
                preferences['effective_frameworks'].append(fw)
            elif avg <= 2.0:
                preferences['ineffective_frameworks'].append(fw)

        if stats['declined'] >= 2 and stats['uses'] == 0:
            preferences['avoided_frameworks'].append(fw)

    # === Suggestion Receptiveness ===
    total_suggestions = len(usage_history)
    accepted = sum(1 for f in usage_history if f['user_accepted_suggestion'])
    if total_suggestions > 0:
        preferences['suggestion_receptiveness'] = accepted / total_suggestions

    # === Preferred Complexity ===
    if usage_history:
        times = [f.get('time_spent_minutes', 0) for f in usage_history if f.get('time_spent_minutes')]
        if times:
            avg_time = sum(times) / len(times)
            if avg_time <= 20:
                preferences['preferred_complexity'] = 'quick'
            elif avg_time <= 60:
                preferences['preferred_complexity'] = 'moderate'
            else:
                preferences['preferred_complexity'] = 'intensive'

    # === Preferred Domains ===
    domain_counts = {}
    for entry in usage_history:
        d = entry.get('domain', 'unknown')
        domain_counts[d] = domain_counts.get(d, 0) + 1
    preferences['preferred_domains'] = sorted(
        domain_counts, key=domain_counts.get, reverse=True)[:2]

    return preferences


def apply_personalization(suggestions, preferences):
    """
    Adjusts suggestion confidence based on user preferences.
    """
    for suggestion in suggestions:
        fw = suggestion['framework']

        # Boost favorites
        if fw in preferences['favorite_frameworks']:
            suggestion['confidence'] = min(suggestion['confidence'] * 1.10, 0.95)
            suggestion['personalization_note'] = "You've used this effectively before"

        # Penalize avoided
        if fw in preferences['avoided_frameworks']:
            suggestion['confidence'] *= 0.50
            suggestion['personalization_note'] = "You've declined this before - showing at lower priority"

        # Penalize ineffective
        if fw in preferences['ineffective_frameworks']:
            suggestion['confidence'] *= 0.70
            suggestion['personalization_note'] = "Previously rated low effectiveness"

        # Adjust for receptiveness
        if preferences['suggestion_receptiveness'] < 0.30:
            # User rarely accepts suggestions - only show high confidence
            if suggestion['confidence'] < 0.80:
                suggestion['suppress'] = True

    # Remove suppressed
    return [s for s in suggestions if not s.get('suppress', False)]
```

---

## 6. Edge Cases and Failure Modes

### 6.1 Ambiguous Domain Detection

```yaml
edge_case: multi_domain_equal_scores
description: Two domains score within 5% of each other
handling:
  - Present both domain suggestions
  - Ask user to confirm primary domain
  - Example: "I detected both Business (72%) and Finance (70%) signals.
    Which is the primary focus?"

edge_case: no_domain_detected
description: All domain scores below 50%
handling:
  - Do not suggest any framework
  - Proceed with universal tools only (TRIZ, Six Hats, SCAMPER)
  - Log for potential new keyword additions

edge_case: all_domains_high
description: 3+ domains score above 70%
handling:
  - Likely a complex life project (e.g., "start a fitness coaching business")
  - Suggest 1 framework per top-2 domains
  - Note multi-domain nature to user
```

### 6.2 Conflicting Suggestions

```yaml
edge_case: contradictory_framework_suggestions
description: Two triggers suggest frameworks that conflict or overlap
handling:
  - Check synergy matrix for pair score
  - If synergy >= 3: present both with synergy note
  - If synergy <= 2: present only higher-confidence one
  - If equal confidence: present both and let user choose

edge_case: too_many_suggestions
description: More than 5 frameworks triggered simultaneously
handling:
  - Hard cap at 3 suggestions
  - Sort by confidence
  - Group by domain (max 1 per domain in multi-domain)
  - Log excess triggers for analysis
```

### 6.3 Feedback Data Quality

```yaml
edge_case: insufficient_feedback_data
description: Fewer than 10 feedback entries for refinement
handling:
  - Use default confidence values from method-rankings.yaml
  - Do not run refinement algorithm
  - Continue collecting data

edge_case: biased_feedback
description: User always rates 5 stars or always skips
handling:
  - Detect bias pattern (>90% same rating)
  - Weight biased feedback at 0.5x
  - Rely more on acceptance rate than star rating

edge_case: framework_never_used
description: Framework frequently suggested but never accepted
handling:
  - After 5 consecutive declines: suppress for this user
  - After 3 consecutive declines: reduce confidence by 30%
  - Log pattern for potential keyword/trigger adjustment
```

### 6.4 Session-Level Constraints

```yaml
constraint: suggestion_cooldown
description: Same framework not re-suggested in same session
handling:
  - Track suggested frameworks per session
  - If already suggested this session: skip unless new trigger type
  - New trigger type (e.g., scoring conflict after keyword) = re-suggest allowed

constraint: suggestion_fatigue
description: User has received 5+ suggestions in one session
handling:
  - Raise threshold to 85% for remaining session
  - Only show "high severity" suggestions
  - Note in presentation: "Showing only high-confidence suggestions"

constraint: user_opted_out
description: User explicitly says "no more framework suggestions"
handling:
  - Disable auto-suggest for remainder of session
  - Record preference
  - Resume next session with normal behavior
```

---

## 7. Implementation Checklist

**Phase 3 tasks:**

- [ ] Implement keyword detection for all 4 domains (Business/Finance/Health/Personal)
- [ ] Implement bigram matching for multi-word keywords
- [ ] Implement consilium divergence calculation with hat opposition pairs
- [ ] Implement contradiction detection from Six Hats output
- [ ] Implement MCDA scoring conflict detection (universal + domain-specific)
- [ ] Implement missing domain criteria detection
- [ ] Implement planning contradiction detection with keyword co-occurrence
- [ ] Build recommendation engine with tier-based selection
- [ ] Implement confidence calculation with multi-signal aggregation
- [ ] Implement multi-framework selection with synergy boost
- [ ] Create all presentation templates (single, multi, TRIZ-specific, tentative)
- [ ] Integrate with Step 1 (after empathy questions complete)
- [ ] Integrate with Step 4 (after consilium all hats complete)
- [ ] Integrate with Step 5 (after MCDA scoring complete)
- [ ] Integrate with Step 8 (during deep plan L2+ generation)
- [ ] Implement feedback collection mechanism
- [ ] Implement feedback storage to shared-knowledge memory
- [ ] Implement learning loop with base confidence adjustment
- [ ] Implement trigger accuracy tracking and adjustment
- [ ] Implement time estimate refinement from actuals
- [ ] Implement user preference model and personalization
- [ ] Handle all edge cases (ambiguous domain, conflicting suggestions, etc.)
- [ ] Implement session-level constraints (cooldown, fatigue, opt-out)
- [ ] Test with 10 sample projects:
  - 2 Business projects (startup + mature)
  - 2 Finance projects (investment + budgeting)
  - 2 Health projects (fitness + habit change)
  - 2 Personal projects (skill learning + productivity)
  - 2 Multi-domain projects (business+finance, health+personal)
- [ ] Validate confidence scores correlate with actual effectiveness
- [ ] Document API contract for each integration point

---

## 8. Success Metrics

**Engine effectiveness targets:**

| Metric | Target | Measurement |
|--------|--------|-------------|
| Acceptance Rate | >=60% | suggestions accepted / suggestions shown |
| Effectiveness | >=70% of accepted rated 4+ stars | 4-5 star ratings / total accepted ratings |
| Confidence Accuracy | R-squared >= 0.70 | correlation(predicted confidence, actual effectiveness) |
| False Positive Rate | <20% | suggestions rated <=2 stars / total accepted |
| Coverage | >=80% | projects with at least 1 suggestion / total projects |
| Domain Detection Accuracy | >=85% | correct domain / total domain detections |
| Suggestion Latency | <500ms | time from trigger to suggestion display |

**Measurement queries:**

```bash
# Acceptance rate
npx claude-flow@v3alpha memory search -q "auto-suggest:feedback user_accepted_suggestion"

# Effectiveness distribution
npx claude-flow@v3alpha memory search -q "auto-suggest:feedback effectiveness_rating"

# Coverage check
npx claude-flow@v3alpha memory search -q "auto-suggest:feedback" --count
npx claude-flow@v3alpha memory search -q "life-os:workflow-plan" --count

# Domain accuracy (requires manual review of first 20 detections)
npx claude-flow@v3alpha memory search -q "auto-suggest:feedback domain"
```

**Monthly review checklist:**
1. Pull all feedback entries from memory
2. Calculate each metric against targets
3. Run refinement algorithm if >=20 new entries
4. Identify worst-performing trigger types
5. Identify best/worst framework suggestions per domain
6. Adjust keyword lists if domain detection accuracy <85%
7. Update this document with findings

---

## 9. Architecture Summary

```
User Input (Step 1, 4, 5, or 8)
        |
        v
+------------------+
| Trigger Detection |
| - Keywords (2.1)  |
| - Consilium (2.2) |
| - Scoring (2.3)   |
| - Planning (2.4)  |
+------------------+
        |
        v
+---------------------------+
| Recommendation Engine (3) |
| - Matrix lookup (3.1)     |
| - Confidence calc (3.2)   |
| - Multi-select (3.3)      |
+---------------------------+
        |
        v
+---------------------------+
| Personalization (5.3)     |
| - User preferences        |
| - Session constraints      |
| - History adjustments      |
+---------------------------+
        |
        v
+---------------------------+
| Presentation (4)          |
| - Template selection       |
| - Confidence threshold     |
| - User action buttons      |
+---------------------------+
        |
        v
   User Decision
   [Accept] / [Skip]
        |
        v
+---------------------------+
| Feedback Loop (5)         |
| - Collect rating           |
| - Store in memory          |
| - Refine algorithm         |
+---------------------------+
```

**Data dependencies:**
- `method-rankings.yaml` - Tier structure and framework scores
- `framework-synergy-matrix.csv` - Synergy scores between framework pairs
- `domain-framework-integration.md` - Applicability data and integration patterns
- `domain-template-architecture.md` - Template structure for framework outputs

---

**Engine Version:** 1.0 (Phase 3)
**Status:** Implementation Ready
**Next:** Phase 4 (Full Ecosystem) - Template composition, cross-linking, metrics dashboard
