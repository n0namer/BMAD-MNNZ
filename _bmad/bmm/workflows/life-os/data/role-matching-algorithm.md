# Specialist Role Matching Algorithm

## Overview

This algorithm enables intelligent role suggestion based on idea keywords, domain detection, and contextual factors. It provides 2-8 specialist recommendations tailored to project complexity and scope.

---

## Algorithm Components

### 1. Role Database

**Source:** `data/specialist-roles.yaml` (50+ specialist types)

**Categories:**
- Business (10 roles)
- Technical (12 roles)
- Design (8 roles)
- Finance (6 roles)
- Health & Wellness (8 roles)
- Personal Development (6 roles)
- Domain-Specific (10+ roles)

---

### 2. Keyword Extraction

**Input:** Idea title + description from workflow plan

**Process:**
1. Extract nouns, verbs, and domain-specific terms
2. Remove stop words (the, a, and, etc.)
3. Normalize to lowercase
4. Create keyword set (unique terms)

**Example:**
```
Title: "Build mobile app for tracking daily habits"
Description: "Need iOS and Android app with user analytics and gamification"

Keywords extracted: [mobile, app, tracking, habits, ios, android, analytics, gamification, user]
```

---

### 3. Domain Detection

**Domains:** business, tech, design, finance, health, personal, legal, creative, community

**Detection Rules:**

| Domain | Trigger Keywords |
|--------|------------------|
| **business** | revenue, growth, market, customer, product, sales, strategy, business, startup, venture |
| **tech** | app, software, code, system, api, database, server, cloud, mobile, web, platform |
| **design** | ui, ux, interface, design, mockup, wireframe, prototype, visual, brand, layout |
| **finance** | budget, investment, revenue, profit, cost, financial, funding, money, capital, roi |
| **health** | fitness, nutrition, health, wellness, exercise, diet, mental, physical, medical, therapy |
| **personal** | habit, goal, productivity, learning, skill, career, time, focus, motivation, growth |
| **legal** | compliance, regulation, contract, legal, law, policy, rights, terms, agreement |
| **creative** | content, creative, writing, video, audio, music, art, media, storytelling |
| **community** | social, community, network, engagement, events, group, connection, collaboration |

**Algorithm:**
```
1. Count keyword matches per domain
2. Select top 1-3 domains with highest match count
3. If tie, prioritize based on context clues (e.g., "app" → tech > business)
4. Default to "business" + "personal" if no clear domain
```

**Example:**
```
Keywords: [mobile, app, tracking, habits, ios, android, analytics, gamification, user]

Domain scores:
- tech: 6 matches (mobile, app, ios, android, analytics, gamification)
- personal: 2 matches (tracking, habits)
- business: 1 match (user)

Selected domains: [tech, personal]
```

---

### 4. Keyword-to-Role Matching

**Process:**
1. For each role in database, calculate relevance score
2. Score = count(matched_keywords) × role_priority_weight
3. Apply domain filter (only roles matching detected domains)
4. Rank roles by score

**Scoring Formula:**
```
role_score = (matched_keywords_count × 10) + priority_bonus + context_bonus

priority_bonus:
- High priority role: +5
- Medium priority: +2
- Low priority: 0

context_bonus:
- Role in primary domain: +3
- Role in secondary domain: +1
```

**Example:**
```
Role: Product Manager
- Keywords matched: [product, user, app] = 3
- Priority: High (+5)
- Domain: business, tech (primary match +3)

Score: (3 × 10) + 5 + 3 = 38

Role: UX Designer
- Keywords matched: [user, app, interface] = 3 (interface inferred)
- Priority: High (+5)
- Domain: design, tech (secondary match +1)

Score: (3 × 10) + 5 + 1 = 36
```

---

### 5. Domain Default Roles

If keyword matching yields <2 roles, add domain defaults:

| Domain | Default Roles |
|--------|---------------|
| **business** | Product Manager, Business Analyst |
| **tech** | Software Architect, Backend Developer |
| **design** | UX Designer, UI Designer |
| **finance** | Financial Analyst, Budget Planner |
| **health** | Wellness Coach, Nutritionist |
| **personal** | Productivity Coach, Life Coach |
| **legal** | Legal Advisor, Compliance Officer |
| **creative** | Content Strategist, Creative Director |
| **community** | Community Manager, Social Strategist |

**Algorithm:**
```
IF role_count < 2 THEN
  FOR each detected_domain:
    ADD domain_default_roles IF not already in list
  END
END
```

---

### 6. Contextual Refinement

Adjust role suggestions based on project metadata:

#### Budget Impact
```
IF budget_tier = high THEN
  ADD [CFO, Financial Advisor, Investment Strategist]
END

IF budget_tier = low THEN
  FILTER roles requiring significant budget (CFO, etc.)
END
```

#### Timeline Impact
```
IF timeline = urgent (<2 weeks) THEN
  ADD [Project Manager, Scrum Master]
  PRIORITIZE roles with "quick start" capability
END

IF timeline = long (>6 months) THEN
  ADD [Strategic Planner, Change Management Specialist]
END
```

#### Complexity Impact
```
IF complexity_score < 8 (Quick) THEN
  LIMIT to 2-3 roles (core only)
END

IF complexity_score 8-15 (Standard) THEN
  ALLOW 4-6 roles (core + support)
END

IF complexity_score > 15 (Deep) THEN
  ALLOW 6-8 roles (comprehensive team)
END
```

#### Stage Impact
```
IF stage = "ideation" THEN
  PRIORITIZE [Innovation Consultant, Research Analyst]
END

IF stage = "planning" THEN
  PRIORITIZE [Strategic Planner, Project Manager]
END

IF stage = "execution" THEN
  PRIORITIZE [Execution Specialist, Implementation Lead]
END

IF stage = "maintenance" THEN
  PRIORITIZE [Operations Manager, Support Specialist]
END
```

---

### 7. Role Deduplication & Merging

**Rules:**
1. If two roles have >70% keyword overlap → Keep higher priority
2. If roles are hierarchical (e.g., Junior Dev + Senior Dev) → Keep senior
3. If roles conflict (e.g., Waterfall PM + Agile Scrum Master) → Flag for user choice

**Examples:**
```
MERGE: [Business Analyst, Product Analyst] → Keep Business Analyst (higher priority)
MERGE: [Junior Developer, Senior Developer] → Keep Senior Developer
FLAG: [Traditional PM, Agile Coach] → User chooses methodology
```

---

## Complete Algorithm Flow

```
STEP 1: EXTRACT KEYWORDS
  Input: idea title + description
  Output: keyword_set[]

STEP 2: DETECT DOMAINS
  Input: keyword_set[]
  Process: Count matches per domain
  Output: primary_domain, secondary_domains[]

STEP 3: KEYWORD MATCHING
  FOR each role in specialist_roles.yaml:
    Calculate role_score
  END
  Sort roles by score DESC
  Output: ranked_roles[]

STEP 4: APPLY DOMAIN FILTER
  FILTER ranked_roles WHERE role.domains INTERSECT detected_domains
  Output: filtered_roles[]

STEP 5: ADD DOMAIN DEFAULTS (if needed)
  IF filtered_roles.length < 2:
    ADD domain_default_roles
  END

STEP 6: CONTEXTUAL REFINEMENT
  Adjust based on:
    - budget_tier
    - timeline
    - complexity_score
    - project_stage
  Output: refined_roles[]

STEP 7: DEDUPLICATION
  Remove duplicates
  Merge overlapping roles
  Output: final_roles[]

STEP 8: LIMIT BY COMPLEXITY
  IF complexity < 8: RETURN top 2-3
  IF complexity 8-15: RETURN top 4-6
  IF complexity > 15: RETURN top 6-8

STEP 9: PRESENT TO USER
  Show ranked list with rationale
  Allow interactive refinement
```

---

## Presentation Format

When presenting suggested roles to user:

```markdown
📋 **Suggested Specialist Roles**

**Detected Domains:** {primary_domain}, {secondary_domain}
**Project Complexity:** {Quick/Standard/Deep}

**Recommended Roles:**

1. **{Role Name}** — Priority: {High/Medium/Low}
   - **Relevance:** {why this role matches}
   - **Keywords matched:** {list}
   - **Contribution:** {what this role brings}

2. **{Role Name}** — Priority: {High/Medium/Low}
   ...

**Optional Roles (consider if project expands):**
- {Optional Role 1}
- {Optional Role 2}

**Notes:**
- {Any contextual observations or gaps}

---

**Actions:**
[A] Approve these roles
[M] Modify (add/remove/change roles)
[R] Regenerate suggestions with different criteria
[?] Explain role selection logic
```

---

## Interactive Refinement

When user selects [M] Modify:

```
💬 **How would you like to modify the role selection?**

Options:
1. Add a specific role (e.g., "Add Marketing Strategist")
2. Remove a role (e.g., "Remove UX Designer")
3. Replace a role (e.g., "Replace Product Manager with Startup Advisor")
4. Change priority (e.g., "Make Software Architect high priority")
5. Show alternative roles for same domain

Type your request or choose 1-5:
```

**Handling additions:**
```
User: "Add Marketing Strategist"

Response:
✅ Adding "Marketing Strategist" to role list

Updated roles:
1. Product Manager
2. UX Designer
3. Software Architect
4. Marketing Strategist ← NEW

Continue? [Y/N]
```

**Handling removals:**
```
User: "Remove UX Designer"

Response:
⚠️  Warning: Removing "UX Designer" may leave a gap in design expertise.

Alternative options:
- Keep minimal design role (UI Designer only)
- Merge design into Product Manager responsibilities
- Proceed with removal (understand risk)

Confirm removal? [Y/N/Show alternatives]
```

---

## Fallback Logic

**If algorithm fails or produces no results:**

1. **Fallback to manual selection:**
   ```
   ⚠️  Automatic role matching inconclusive.

   Please manually select roles from these categories:
   - Business: [list 5-6 common roles]
   - Technical: [list 5-6 common roles]
   - Design: [list 4-5 common roles]
   - Other: [link to full specialist database]

   Type role names separated by commas:
   ```

2. **Fallback to complexity-based defaults:**
   ```
   IF complexity < 8:
     DEFAULT = [Product Manager, Developer]
   IF complexity 8-15:
     DEFAULT = [Product Manager, Developer, Designer, Tester]
   IF complexity > 15:
     DEFAULT = [Product Manager, System Architect, Developer, Designer, Tester, QA Lead]
   ```

---

## Quality Metrics

**Track algorithm performance:**

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Suggestion Accuracy** | >80% acceptance rate | User approves without modification |
| **Role Coverage** | >90% projects have adequate roles | No gaps in specialist coverage |
| **Refinement Rate** | <30% require modification | Low modification = good suggestions |
| **Domain Detection Accuracy** | >85% correct primary domain | Manual validation by user |

**Store metrics in memory:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "bmad:role-matching:metrics:{date}" \
  --content "{acceptance_rate, coverage_rate, refinement_rate, accuracy}"
```

---

## Integration Points

### With Step-02 (Roles Discovery)
- Algorithm runs AFTER sphere detection
- Uses sphere → domain mapping
- Presents suggestions before role confirmation

### With Step-03 (Specialist Match)
- Confirmed roles feed into specialist matching
- Role specializations guide specialist selection
- Role priorities influence specialist ranking

### With Memory System
- Store successful role combinations for pattern learning
- Retrieve similar project role patterns
- Build confidence scores over time

---

## Future Enhancements

1. **Machine Learning Integration**
   - Train on historical role selections
   - Improve keyword → role mapping
   - Personalize suggestions per user

2. **Role Relationship Graph**
   - Model role dependencies (e.g., Architect requires Developer)
   - Suggest complementary roles automatically
   - Detect missing critical roles

3. **Budget-Aware Suggestions**
   - Estimate role costs
   - Suggest role consolidation for budget constraints
   - Prioritize high-impact roles when limited

4. **Timeline-Aware Phasing**
   - Suggest role hiring sequence
   - Phase roles by project stage
   - Optimize team composition over time

---

## References

- **Specialist Database:** `data/specialist-roles.yaml`
- **Role Descriptions:** `data/roles-descriptions.md`
- **Role Templates:** `data/roles-templates.md`
- **Domain Mapping:** Built-in (see Section 3)

---

**Algorithm Version:** 1.0.0
**Last Updated:** 2026-02-06
**Maintained By:** Life OS Workflow System
