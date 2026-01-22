# EMBER Consilium Confidence Scoring Framework

## Overview
Quantitative confidence assessment for all EMBER consilium recommendations and findings.

## Confidence Scale Definition

### 1.0 - Extremely High Confidence
- **Evidence Quality**: Multiple high-quality sources, peer-reviewed data
- **Consistency**: All evidence sources align perfectly
- **Expertise**: Domain experts unanimously agree
- **Testing**: Extensively validated through multiple methods
- **Context**: Fully understood problem domain and constraints

### 0.8-0.9 - High Confidence
- **Evidence Quality**: Strong evidence from reliable sources
- **Consistency**: Minor variations in evidence sources
- **Expertise**: Strong expert consensus with minor disagreements
- **Testing**: Well-validated through established methods
- **Context**: Well-understood domain with known constraints

### 0.6-0.7 - Moderate Confidence
- **Evidence Quality**: Good evidence with some limitations
- **Consistency**: Some variations requiring reconciliation
- **Expertise**: Mixed expert opinions requiring analysis
- **Testing**: Partially validated with some uncertainty
- **Context**: Partially understood with some unknowns

### 0.4-0.5 - Low Confidence
- **Evidence Quality**: Limited or conflicting evidence
- **Consistency**: Significant variations between sources
- **Expertise**: Divergent expert opinions
- **Testing**: Limited validation with significant uncertainty
- **Context**: Poorly understood with major unknowns

### 0.2-0.3 - Very Low Confidence
- **Evidence Quality**: Weak or anecdotal evidence only
- **Consistency**: Major conflicts between evidence sources
- **Expertise**: No expert consensus, high controversy
- **Testing**: Unvalidated or untested assumptions
- **Context**: Very poorly understood with critical unknowns

### 0.0-0.1 - No Confidence
- **Evidence Quality**: No credible evidence available
- **Consistency**: Complete contradiction between sources
- **Expertise**: No relevant expertise or complete disagreement
- **Testing**: No validation possible
- **Context**: Completely unknown domain

## Overall Confidence Calculation

**DEPRECATED - Simple Weighted Average (Mathematically Incorrect):**
```
OLD_METHOD = (Evidence_Strength × 0.4) + (Analytical_Rigor × 0.3) + (Perspective_Balance × 0.3)
PROBLEM: Assumes independence between factors (usually violated)
```

**RECOMMENDED - Adjusted Confidence with Uncertainty Propagation:**
```
Base_Confidence = (Evidence_Strength × 0.4) + (Analytical_Rigor × 0.3) + (Perspective_Balance × 0.3)

Uncertainty_Propagation = sqrt((σ_Evidence)² + (σ_Rigor)² + (σ_Perspective)²) / sqrt(3)
  Where σ = standard deviation of component scores

Penalty_Factors:
  - Evidence_Gap_Penalty: 0.05 per category with <3 sources
  - MCP_Conflict_Penalty: 0.03 per unresolved MCP conflict
  - Stakeholder_Misalignment: 0.05 if variance >30%
  - Near_Tie_Penalty: 0.20 if top options within 0.3 points

Total_Penalty = sum(Penalty_Factors)

Final_Confidence_Point = Base_Confidence × (1 - Total_Penalty)

Confidence_Range:
  Lower_Bound = Final_Confidence_Point - Uncertainty_Propagation
  Upper_Bound = Final_Confidence_Point + Uncertainty_Propagation

REPORT: [Lower_Bound] - [Upper_Bound] (point: [Final_Confidence_Point])
```

**Example Calculation:**
```
Evidence_Strength = 0.80, Analytical_Rigor = 0.75, Perspective_Balance = 0.85
Base_Confidence = (0.80×0.4) + (0.75×0.3) + (0.85×0.3) = 0.80

Uncertainty = sqrt(0.05² + 0.07² + 0.04²) / sqrt(3) = 0.05

Penalties:
  Evidence_Gap (1 category): 0.05
  MCP_Conflict (0): 0.00
  Stakeholder_Misalignment (0): 0.00
  Near_Tie (0): 0.00
Total_Penalty = 0.05

Final_Confidence_Point = 0.80 × (1 - 0.05) = 0.76

Confidence_Range = 0.71 - 0.81 (point: 0.76)
```

### Confidence Interpretation

#### 0.9+ Exceptional Confidence
- **Recommendation**: Implement immediately
- **Risk Level**: Minimal risk, high certainty
- **Monitoring**: Standard project monitoring
- **Contingency**: Minimal contingency planning needed

#### 0.8-0.9 High Confidence
- **Recommendation**: Implement with standard risk mitigation
- **Risk Level**: Low risk, good certainty
- **Monitoring**: Enhanced monitoring for key milestones
- **Contingency**: Basic contingency planning

#### 0.7-0.8 Good Confidence
- **Recommendation**: Implement with caution and monitoring
- **Risk Level**: Moderate risk, reasonable certainty
- **Monitoring**: Comprehensive milestone monitoring
- **Contingency**: Developed contingency plans

#### 0.6-0.7 Moderate Confidence
- **Recommendation**: Implement as pilot with full evaluation
- **Risk Level**: Elevated risk, some uncertainty
- **Monitoring**: Intensive monitoring and frequent reviews
- **Contingency**: Comprehensive contingency planning

#### 0.5-0.6 Low Confidence
- **Recommendation**: Further analysis required before implementation
- **Risk Level**: High risk, significant uncertainty
- **Monitoring**: Research and validation activities
- **Contingency**: Multiple contingency scenarios

#### <0.5 Very Low Confidence
- **Recommendation**: Do not implement, reassess decision framework
- **Risk Level**: Extreme risk, fundamental uncertainty
- **Monitoring**: Complete decision framework review
- **Contingency**: Fundamental decision reconsideration

### Confidence Adjustment Factors

#### Positive Adjustments (+0.1 to +0.2)
- Strong stakeholder alignment
- Proven similar implementations
- Conservative risk profile
- Abundant resources available
- Flexible implementation timeline

#### Negative Adjustments (-0.1 to -0.2)
- Stakeholder disagreement
- Novel or unproven approach
- Aggressive risk profile
- Resource constraints
- Urgent timeline requirements
