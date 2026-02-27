# Sphere Detection Rules

## Overview

This algorithm infers 1-3 spheres from idea title and description using keyword matching and domain inference.

---

## Available Spheres

**10 Life Spheres:**
- business
- finance
- career
- health
- relationships
- learning
- home
- legal
- creative
- community

---

## Detection Algorithm

### Step 1: Extract Keywords
```
INPUT: idea title + description
PROCESS: Extract nouns, verbs, domain terms
REMOVE: Stop words (the, a, and, etc.)
OUTPUT: keyword_set[]
```

### Step 2: Match Keywords to Spheres
```
FOR each sphere in available_spheres:
  sphere_score = count(keywords matching sphere_triggers)
END

SORT spheres by score DESC
SELECT top 1-3 spheres (score > 0)
```

### Step 3: Apply Default Rules
```
IF no spheres detected:
  DEFAULT = [business, personal]
END

IF only 1 sphere detected:
  IF complexity > 10:
    ADD secondary sphere based on context
  END
END
```

---

## Sphere Trigger Keywords

### Business
**Triggers:** revenue, growth, market, customer, product, sales, strategy, business, startup, venture, company, client, profit, roi, brand, marketing, competition

**Context clues:**
- Mentions of "launch", "scale", "market share"
- Business model references
- Customer/client language

### Finance
**Triggers:** budget, investment, revenue, profit, cost, financial, funding, money, capital, roi, cash, expense, accounting, tax, savings, loan, debt

**Context clues:**
- Numbers with currency symbols
- Financial planning language
- Investment/funding mentions

### Career
**Triggers:** career, job, resume, interview, promotion, skill, professional, work, employer, salary, networking, leadership, advancement, transition

**Context clues:**
- Job titles mentioned
- Career progression language
- Professional development focus

### Health
**Triggers:** fitness, nutrition, health, wellness, exercise, diet, mental, physical, medical, therapy, doctor, treatment, stress, sleep, recovery, energy

**Context clues:**
- Medical/health conditions
- Fitness goals
- Wellness objectives

### Relationships
**Triggers:** relationship, partner, family, friend, social, connection, communication, dating, marriage, children, parents, conflict, trust, intimacy

**Context clues:**
- People-focused language
- Social dynamics
- Interpersonal goals

### Learning
**Triggers:** learning, education, course, study, skill, knowledge, training, certification, language, research, book, tutorial, mastery, understanding

**Context clues:**
- Educational goals
- Skill acquisition language
- Knowledge building focus

### Home
**Triggers:** home, house, apartment, renovation, furniture, decor, organization, cleaning, maintenance, garden, property, moving, space, room

**Context clues:**
- Physical space references
- Home improvement language
- Living situation mentions

### Legal
**Triggers:** legal, law, contract, agreement, compliance, regulation, policy, rights, lawsuit, attorney, patent, trademark, terms, liability

**Context clues:**
- Legal terminology
- Regulatory mentions
- Rights/obligations language

### Creative
**Triggers:** creative, art, design, content, writing, video, music, photography, painting, craft, storytelling, project, expression, portfolio

**Context clues:**
- Artistic mediums
- Creative output goals
- Portfolio/showcase language

### Community
**Triggers:** community, social, network, group, event, volunteer, nonprofit, activism, engagement, outreach, membership, collaboration, organization

**Context clues:**
- Collective action language
- Group/community focus
- Social impact goals

---

## Multi-Sphere Detection Logic

### Primary + Secondary Pattern
```
IF top_sphere_score > 2 × second_sphere_score:
  RETURN [primary_sphere]
ELSE:
  RETURN [primary_sphere, secondary_sphere]
END
```

### Three Sphere Pattern
```
IF top_3_spheres all have score ≥ 3:
  RETURN [sphere_1, sphere_2, sphere_3]
ELSE:
  RETURN top 2 spheres
END
```

### Context-Based Expansion
```
IF complexity > 10:
  IF business sphere detected:
    ADD finance sphere (business often needs financial planning)
  END

  IF tech + creative detected:
    ADD business sphere (likely product/startup)
  END
END
```

---

## Examples

### Example 1: Single Sphere
```
Title: "Start morning meditation habit"
Description: "Want to meditate 10 minutes daily to reduce stress"

Keywords: [meditation, habit, daily, stress, reduce]
Sphere matches:
- health: 4 (meditation, stress, daily routine, wellness)
- personal: 2 (habit, daily)

Result: [health]
```

### Example 2: Two Spheres
```
Title: "Launch freelance design business"
Description: "Offer branding and web design services to small businesses"

Keywords: [launch, freelance, design, business, branding, web, services, small businesses]
Sphere matches:
- business: 6 (launch, business, services, small businesses, freelance)
- creative: 4 (design, branding, web)

Result: [business, creative]
```

### Example 3: Three Spheres
```
Title: "Build health tech startup"
Description: "Mobile app for tracking fitness and nutrition with community features"

Keywords: [build, health, tech, startup, mobile, app, tracking, fitness, nutrition, community]
Sphere matches:
- tech: 5 (tech, mobile, app, tracking, build)
- health: 4 (health, fitness, nutrition)
- business: 3 (startup, build, app)
- community: 2 (community, tracking)

Result: [tech, health, business] (top 3, all ≥ 3)
```

### Example 4: Default Fallback
```
Title: "Organize my life better"
Description: "Need a system to manage everything"

Keywords: [organize, life, system, manage]
Sphere matches:
- personal: 2 (life, organize)
- (no other strong matches)

Result: [business, personal] (default applied due to low confidence)
```

---

## Search Orchestrator Integration

**Priority sequence for sphere detection:**
1. **CLI Claude Flow memory search** — Check for similar ideas with known spheres
2. **Local MD search** — Check plans/snapshots for sphere patterns
3. **Web/MCP** — If ambiguous, research domain context

**Example:**
```bash
# Step 1: Search memory for similar ideas
npx claude-flow@v3alpha memory search -q "similar to: ${idea_title}"

# Step 2: If found, extract spheres from historical data
IF history_found:
  USE historical_spheres as starting point
  VALIDATE with keyword matching
END

# Step 3: If ambiguous, search web for domain clarification
IF confidence < 70%:
  SEARCH web for "${idea_title} domain category"
  REFINE sphere selection
END
```

---

## Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Detection Accuracy** | >85% | Manual validation by user |
| **Multi-Sphere Precision** | >80% | All detected spheres are relevant |
| **Default Fallback Rate** | <15% | Rare use of default [business, personal] |
| **User Override Rate** | <20% | Low rate of manual corrections |

**Store metrics:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "bmad:sphere-detection:metrics:{date}" \
  --content "{accuracy, precision, fallback_rate, override_rate}"
```

---

## Error Handling

### No Keywords Extracted
```
IF keyword_set.length = 0:
  USE title words as keywords
  RETRY detection
  IF still empty:
    USE default [business, personal]
  END
END
```

### Conflicting Spheres
```
IF spheres contain [legal, creative, health] simultaneously:
  FLAG as unusual combination
  ASK user to confirm or adjust
END
```

### Overload (>3 spheres)
```
IF sphere_matches > 3 with similar scores:
  SELECT top 3 by score
  NOTE to user: "Additional relevant spheres: [list]"
  ALLOW user to swap if needed
END
```

---

## References

- **Role Filtering Algorithm:** `data/roles-filtering-algorithm.md`
- **Role Matching Algorithm:** `data/role-matching-algorithm.md`
- **Roles Auto-Selection:** `data/roles-auto-selection.md`

---

**Version:** 1.0.0
**Last Updated:** 2026-02-06
**Maintained By:** Life OS Workflow System
