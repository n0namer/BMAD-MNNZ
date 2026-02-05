# Roles Auto-Selection Logic

## Sphere Inference Protocol

### 1. Semantic Analysis (Search Orchestrator)

**Priority order:**
1. **CLI Claude Flow memory search** - Check past projects for similar patterns
2. **Local MD search** - Review existing plans/snapshots in project
3. **Web/MCP search** - Only if ambiguous or novel domain

**Sphere Options:**
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

**Selection criteria:**
- Choose 1–3 most relevant spheres
- Prefer primary sphere from idea summary
- Include secondary spheres only if explicitly needed

## 2. Role Matching Rules

### Priority-Based Selection

**From roles-base.csv:**
- Match sphere → role mapping
- Check tags for context alignment
- Map default_template for deep plan integration

**Priority levels:**
| Priority | When to Assign | Examples |
|----------|---------------|----------|
| **high** | Core project delivery | Project Manager, Architect |
| **medium** | Supporting functions | QA Specialist, Documentation |
| **low** | Optional/future | Community Manager, Legal Advisor |

### Overlap Resolution

**If multiple roles overlap:**
1. Identify common responsibilities
2. Keep highest priority role
3. Merge specialized tasks into single role
4. Document rationale in notes

### New Role Suggestion

**Suggest new role if:**
- Idea implies unique responsibility not in roles-base.csv
- Existing roles don't cover critical gap
- Domain requires specialized expertise

**Format:**
```
**New Role Suggested:** {role_name}
**Rationale:** {why needed}
**Sphere:** {primary_sphere}
**Priority:** {high/medium/low}
```

## 3. Presentation Template

```markdown
📋 Suggested Roles for this project:

**Spheres:** {sphere1, sphere2, sphere3}
**Required Roles:**
- {role1} — priority: {high/medium/low} — {brief rationale}
- {role2} — priority: {high/medium/low} — {brief rationale}
- {role3} — priority: {high/medium/low} — {brief rationale}

**Notes:**
- {constraints or gaps}
- {new roles suggested if any}

Please confirm: [A]pprove / [M]odify / [C]ontinue
```

## 4. Confirmation Flow

| User Response | Action |
|---------------|--------|
| **A** or **C** | Proceed to append to workflow plan |
| **M** | Ask for changes, update suggestions, re-present |
| **Other** | Help user respond, redisplay menu |

## 5. Auto-Population Triggers

**When to auto-suggest roles:**
- Idea summary contains domain keywords (finance, health, legal, etc.)
- Tags in roles-base.csv match idea tags
- Previous similar projects used specific roles (from memory search)

**When to ask user:**
- Ambiguous scope (multiple valid interpretations)
- Novel domain not covered in roles-base.csv
- Conflicting role requirements
