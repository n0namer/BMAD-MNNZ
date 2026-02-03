Project C  0.320   0.093   0.078  0.021
```

#### Step 3: Identify Ideal Solutions

**Ideal Best (A+)**:
- For benefit criteria: maximum value
- For cost criteria: minimum value

**Ideal Worst (A-)**:
- For benefit criteria: minimum value
- For cost criteria: maximum value

```
A+ = [0.360, 0.040, 0.078, 0.021]
     (max Impact, min Effort, min Risk, min Timeline)

A- = [0.281, 0.093, 0.196, 0.047]
     (min Impact, max Effort, max Risk, max Timeline)
```

#### Step 4: Calculate Euclidean Distances

**Distance to Ideal Best (d+)**:

```
d+(A) = √[(0.360-0.360)² + (0.067-0.040)² + (0.117-0.078)² + (0.031-0.021)²]
      = √[0 + 0.00073 + 0.00152 + 0.00010]
      = 0.049

d+(B) = √[(0.281-0.360)² + (0.040-0.040)² + (0.196-0.078)² + (0.047-0.021)²]
      = √[0.00624 + 0 + 0.01392 + 0.00068]
      = 0.144

d+(C) = √[(0.320-0.360)² + (0.093-0.040)² + (0.078-0.078)² + (0.021-0.021)²]
      = √[0.00160 + 0.00281 + 0 + 0]
      = 0.066
```

**Distance to Ideal Worst (d-)**:

```
d-(A) = √[(0.360-0.281)² + (0.067-0.093)² + (0.117-0.196)² + (0.031-0.047)²]
      = √[0.00624 + 0.00068 + 0.00624 + 0.00026]
      = 0.119

d-(B) = √[(0.281-0.281)² + (0.040-0.093)² + (0.196-0.196)² + (0.047-0.047)²]
      = √[0 + 0.00281 + 0 + 0]
      = 0.053

d-(C) = √[(0.320-0.281)² + (0.093-0.093)² + (0.078-0.196)² + (0.021-0.047)²]
      = √[0.00152 + 0 + 0.01392 + 0.00068]
      = 0.127
```

#### Step 5: Calculate Relative Closeness (Ci)

```
Ci = d- / (d+ + d-)

Ci(A) = 0.119 / (0.049 + 0.119) = 0.708
Ci(B) = 0.053 / (0.144 + 0.053) = 0.269
Ci(C) = 0.127 / (0.066 + 0.127) = 0.658

Range: 0 ≤ Ci ≤ 1
Higher Ci = better alternative
```

#### Step 6: Rank Alternatives

```
Final Ranking:
1. Project A (Ci = 0.708) ← Best
2. Project C (Ci = 0.658)
3. Project B (Ci = 0.269) ← Worst
```

---

## Part 3: Implementation Guide

### 3.1 When to Use AHP vs Simpler Methods

```
Decision Tree:

Start
 │
 ├─ Number of criteria?
 │   ├─ 1-2 criteria → Use weighted scoring (skip AHP)
 │   ├─ 3-5 criteria → AHP recommended
 │   └─ 6+ criteria → AHP essential (complexity management)
 │
 ├─ Criteria independence?
 │   ├─ Highly correlated → Consider ANP (network process)
 │   └─ Independent → AHP appropriate
 │
 ├─ Stakeholder alignment?
 │   ├─ Consensus needed → Group AHP (aggregate judgments)
 │   └─ Single decision-maker → Standard AHP
 │
 └─ Uncertainty level?
     ├─ High uncertainty → Fuzzy AHP/TOPSIS
     └─ Low uncertainty → Standard AHP/TOPSIS
```

### 3.2 Integration with D/F/V/C Criteria Blocks

**Mapping Life-OS Criteria to AHP/TOPSIS**:

```yaml
Design/Plan/Create Sphere:
  AHP_Criteria:
    - Impact_on_goals: "How much does this advance sphere objectives?"
    - Effort_required: "Time/resources needed (cost criterion)"
    - Risk_of_failure: "Probability × consequence (cost criterion)"
    - Timeline_urgency: "Deadline pressure (cost criterion)"
    - Alignment_with_values: "Fit with personal values (benefit)"

Focus/Priorities Sphere:
  AHP_Criteria:
    - Strategic_importance: "Long-term impact"
    - Resource_efficiency: "ROI (benefit)"
    - Skill_development: "Learning opportunity (benefit)"
    - Energy_drain: "Mental/physical cost (cost)"

Validate/Improve Sphere:
  AHP_Criteria:
    - Validation_confidence: "Evidence strength (benefit)"
    - Improvement_potential: "Upside if fixed (benefit)"
    - Technical_debt: "Cost of postponing (cost)"
    - Stakeholder_impact: "Who benefits (benefit)"

Connect/Integrate Sphere:
  AHP_Criteria:
    - Network_effect: "Multiplier benefit (benefit)"
    - Integration_complexity: "Coordination cost (cost)"
    - Dependency_risk: "Coupling risk (cost)"
    - Synergy_potential: "Combined value (benefit)"
```

### 3.3 Sphere-Specific Weight Adjustments

**Recommended AHP Weight Distributions by Sphere**:

```
Design/Plan/Create:
  Impact_on_goals:      45-50%  (primary driver)
  Effort_required:      20-25%
  Risk_of_failure:      15-20%
  Timeline_urgency:     10-15%

Focus/Priorities:
  Strategic_importance: 40-45%
  Resource_efficiency:  25-30%
  Skill_development:    15-20%
  Energy_drain:         10-15%

Validate/Improve:
  Validation_confidence: 35-40%
  Improvement_potential: 30-35%
  Technical_debt:        20-25%
  Stakeholder_impact:    5-10%

Connect/Integrate:
  Network_effect:        40-45%
  Integration_complexity: 25-30%
  Synergy_potential:     20-25%
  Dependency_risk:       5-10%
```

### 3.4 Recalculation Triggers

**When to re-run AHP/TOPSIS**:

1. **Criteria Weight Changes** (AHP):
   - New strategic priorities emerge
   - Stakeholder feedback changes importance
   - Major external events shift context
   - **Frequency**: Quarterly or on major changes
