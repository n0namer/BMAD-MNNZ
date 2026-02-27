# Roles CSV Filtering Algorithm

## Overview

This algorithm filters the base roles CSV file by detected spheres, returning only relevant roles (~10-20 rows instead of 150+ full CSV).

---

## Algorithm Flow

### Input
- Detected spheres: 1-3 spheres from step-02 (business, finance, career, health, relationships, learning, home, legal, creative, community)
- Base roles CSV: `data/roles-base.csv`

### Output
- Filtered roles list containing:
  - role name
  - sphere
  - priority (high/medium/low)
  - default_template

---

## Filtering Process

### Step 1: Load CSV
```
LOAD roles_base.csv
PARSE into rows[]
```

### Step 2: Filter by Sphere Match
```
FOR each row in rows[]:
  IF row.sphere IN detected_spheres:
    ADD to filtered_results[]
  END
END
```

### Step 3: Extract Relevant Fields
```
FOR each row in filtered_results[]:
  EXTRACT:
    - role
    - sphere
    - priority
    - default_template
  STORE in output[]
END
```

### Step 4: Return Results
```
RETURN output[] (typically 10-20 rows)
```

---

## Subprocess Pattern

### Pattern 1: CSV Filtering Subprocess

**When to use:** Filtering large CSV files by criteria (saves ~450 lines of context)

**Launch subprocess that:**
1. Loads `roles-base.csv`
2. Filters rows matching detected spheres
3. Extracts only: role, sphere, priority, default_template
4. Returns ONLY relevant rows (~10-20 lines)

**Subprocess returns:** Filtered roles matching current spheres + priority + template mapping

**Context Savings:** ~450 lines (150 CSV rows → 10-20 filtered rows)

### Pattern 3: Graceful Fallback

**If subprocess unavailable:**
```bash
# Grep CSV for sphere matches
grep -E "(sphere1|sphere2|sphere3)" data/roles-base.csv

# Then load full CSV if needed
```

---

## Integration with Role Matching Algorithm

### Execution Order
1. **Primary:** AI specialist matching from `data/role-matching-algorithm.md`
2. **Fallback:** CSV filtering (if specialist database insufficient)

### When to Use CSV Fallback
- Specialist matching returns <2 roles
- User requests base roles explicitly
- Specialist database unavailable

### Merge Strategy
```
IF specialist_roles.length < 2:
  filtered_base_roles = run_csv_filtering(detected_spheres)
  MERGE specialist_roles + filtered_base_roles
  DEDUPLICATE by role name
END
```

---

## Example Execution

### Input
```
Detected spheres: [business, tech, personal]
```

### CSV Filtering
```
Original CSV: 150 rows
Filtered rows: 18 rows matching [business, tech, personal] spheres

Results:
- Product Manager (business, high, product-manager-template)
- Business Analyst (business, medium, business-analyst-template)
- Software Architect (tech, high, architect-template)
- Backend Developer (tech, medium, backend-dev-template)
- UX Designer (tech, medium, ux-designer-template)
- Life Coach (personal, medium, life-coach-template)
- Productivity Coach (personal, low, productivity-coach-template)
... (11 more rows)
```

### Output Format
```markdown
**Filtered Base Roles (from CSV):**

Business Sphere:
- Product Manager (high priority)
- Business Analyst (medium priority)
- Financial Analyst (medium priority)

Tech Sphere:
- Software Architect (high priority)
- Backend Developer (medium priority)
- Frontend Developer (medium priority)
- UX Designer (medium priority)

Personal Sphere:
- Life Coach (medium priority)
- Productivity Coach (low priority)
- Career Advisor (low priority)
```

---

## Performance Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Context Reduction** | 90%+ | 150 rows → 10-20 rows |
| **Filtering Accuracy** | 100% | All returned roles match spheres |
| **Response Time** | <500ms | CSV load + filter + return |
| **Fallback Success Rate** | >95% | Graceful degradation when subprocess fails |

---

## Error Handling

### CSV Not Found
```
IF roles-base.csv NOT EXISTS:
  FALLBACK to specialist_roles.yaml only
  NOTIFY user: "Base roles unavailable, using specialist database"
END
```

### Empty Filter Results
```
IF filtered_results.length = 0:
  EXPAND sphere detection (add default: business + personal)
  RETRY filtering
  IF still empty:
    USE complexity-based defaults
  END
END
```

### Subprocess Timeout
```
IF subprocess timeout > 5s:
  CANCEL subprocess
  FALLBACK to grep-based filtering
  LOG warning
END
```

---

## References

- **Base Roles CSV:** `data/roles-base.csv`
- **Specialist Roles:** `data/specialist-roles.yaml`
- **Role Matching Algorithm:** `data/role-matching-algorithm.md`
- **Sphere Detection Rules:** `data/sphere-detection-rules.md`

---

**Version:** 1.0.0
**Last Updated:** 2026-02-06
**Maintained By:** Life OS Workflow System
