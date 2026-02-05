# Goals YAML Structure Reference

## File Location
`{bmb_creations_output_folder}/life-os/goals.yaml`

---

## YAML Template

```yaml
---
created: {today's date YYYY-MM-DD}
lastUpdated: {today's date}
version: 1.0
status: ACTIVE
---

finance:
  1_year:
    goal: "{user's 1-year finance goal}"
    measurable: true/false
  3_years:
    goal: "{user's 3-year finance goal}"
    measurable: true/false
  5_10_years:
    goal: "{user's 5-10 year finance goal}"
    measurable: true/false

business:
  1_year:
    goal: "{user's 1-year business goal}"
    measurable: true/false
  3_years:
    goal: "{user's 3-year business goal}"
    measurable: true/false
  5_10_years:
    goal: "{user's 5-10 year business goal}"
    measurable: true/false

health:
  1_year:
    goal: "{user's 1-year health goal}"
    measurable: true/false
  3_years:
    goal: "{user's 3-year health goal}"
    measurable: true/false
  5_10_years:
    goal: "{user's 5-10 year health goal}"
    measurable: true/false

personal:
  1_year:
    goal: "{user's 1-year personal goal}"
    measurable: true/false
  3_years:
    goal: "{user's 3-year personal goal}"
    measurable: true/false
  5_10_years:
    goal: "{user's 5-10 year personal goal}"
    measurable: true/false

alignmentWeights:
  1_year: 0.5
  3_years: 0.3
  5_10_years: 0.2
```

---

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `created` | date | YYYY-MM-DD when goals were first documented |
| `lastUpdated` | date | YYYY-MM-DD when goals were last revised |
| `version` | string | Semantic versioning (1.0, 1.1, 2.0) |
| `status` | enum | ACTIVE, ARCHIVED, PAUSED |
| `{domain}.{timeframe}.goal` | string | User's goal statement (SMART preferred) |
| `{domain}.{timeframe}.measurable` | boolean | Is goal SMART-compliant? |
| `alignmentWeights` | object | Weights for Strategic Alignment scoring |

---

## Alignment Weights Explained

Used in Step 05 (Strategic Alignment) to calculate:

```
Strategic Alignment Score =
  (impact on 1-year goals × 0.5) +
  (impact on 3-year goals × 0.3) +
  (impact on 5-10-year goals × 0.2)
```

**Rationale:**
- **1-year (0.5):** Near-term impact matters most for project prioritization
- **3-years (0.3):** Mid-term strategic fit prevents short-sightedness
- **5-10-years (0.2):** Long-term vision ensures alignment with ultimate purpose

---

## Claude Flow Memory Backup

**Parallel save (required):**

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:goals:user" \
  --content "{yaml_content}"

npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:scoring:alignment-weights" \
  --content "1_year:0.5,3_years:0.3,5_10_years:0.2"
```

---

**Reference:** Load this file when implementing YAML save or memory storage.
