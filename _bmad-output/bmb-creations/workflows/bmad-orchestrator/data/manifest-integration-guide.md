# BMAD Manifests Integration Guide

**Reference:** How to use existing BMAD CSV manifests for intelligent workflow routing and selection.

## Manifest Files Location & Purpose

| CSV File | Path | Records | When to Use |
|----------|------|---------|------------|
| **workflow-manifest** | `/_bmad/_config/workflow-manifest.csv` | 52 | Step 2: Workflow selection & matching |
| **advanced-elicitation methods** | `/core/workflows/advanced-elicitation/methods.csv` | 50 | Step 2 [A] menu: Deep analysis methods |
| **problem-solving methods** | `/cis/workflows/problem-solving/solving-methods.csv` | 31 | Step 2 [P] menu: Problem-solving techniques |
| **common-workflow-tools** | `/bmb/workflows/workflow/data/common-workflow-tools.csv` | 19 | Step 4: Tool selection for execution |
| **tool-manifest** | `/_bmad/_config/tool-manifest.csv` | 19 | Step 3-4: Available tools for orchestration |

## CSV Schemas

### workflow-manifest.csv
```
name | description | module | path
```
- **module**: bmm, bmb, cis, tea, core
- **name**: workflow identifier
- **description**: what the workflow does (for user explanation)
- **path**: relative path to workflow file
- **Selection Logic**: Match task keywords to module + description

### methods.csv (advanced-elicitation)
```
num | category | method_name | description | output_pattern
```
- **category**: collaboration, advanced, competitive, technical, creative, research, risk, core, learning, philosophical, retrospective
- **method_name**: specific technique name
- **description**: what it does and when to use
- **output_pattern**: what thinking flow it generates
- **Selection Logic**: Match analysis depth needed to method category

### solving-methods.csv (problem-solving)
```
category | method_name | description | facilitation_prompts
```
- **category**: diagnosis, analysis, synthesis, evaluation, implementation, creative
- **method_name**: technique name
- **facilitation_prompts**: guiding questions separated by `|`
- **Selection Logic**: Match problem stage to category

### common-workflow-tools.csv
```
propose | type | tool_name | description | url | requires_install
```
- **propose**: "always" (core) or "example" (optional)
- **type**: workflow, task, tool-memory, llm-tool-feature, mcp
- **Selection Logic**: Filter by propose=always for core tools

### tool-manifest.csv
```
name | displayName | description | module | path | standalone
```
- **type**: Tool type (workflow, task, mcp, etc.)
- **standalone**: true if can run independently
- **Selection Logic**: Check availability + module location

## Integration Points

### Step 2: Workflow Selection

```
1. Load workflow-manifest.csv
2. Parse task description from Step 1
3. Score each workflow:
   - Exact module match: +10 points
   - Keyword match in description: +5 points per match
   - Module affinity (e.g., "dev" → bmm): +3 points
4. Return top 3-4 options ranked by score
5. For user to select or use auto-select
```

### Step 2 [A]: Advanced Elicitation

```
1. Load methods.csv
2. Determine analysis depth needed from task complexity
3. Select methods by category:
   - Simple clarification: core methods (Socratic, 5 Whys)
   - Complex decision: advanced methods (Tree of Thoughts, Graph of Thoughts)
   - Controversial: competitive methods (Red Team vs Blue Team)
   - Technical: technical methods (Architecture Decision Records)
4. Present method options with facilitation prompts
```

### Step 2 [P]: Party Mode / Problem-Solving

```
1. Load solving-methods.csv
2. Determine problem stage:
   - Clarifying issue: diagnosis methods
   - Understanding causes: analysis methods
   - Finding solutions: synthesis methods
   - Evaluating options: evaluation methods
3. Select 2-3 methods for that stage
4. Guide user through facilitation prompts
```

### Step 3: Orchestration Tools

```
1. Load common-workflow-tools.csv
2. Load tool-manifest.csv
3. For selected workflows, identify required tools
4. Filter by propose="always" for core tools
5. Check requires_install for optional tools
6. Document tool chain in orchestration plan
```

## Usage Patterns

### Pattern 1: Lookup Workflow by Name
```
workflow_name = "create-prd"
match = find_in_csv("workflow-manifest.csv", name == workflow_name)
return match.description, match.path, match.module
```

### Pattern 2: Find Workflows by Task Type
```
task = "I need to design UX"
keywords = ["design", "UX"]
matches = filter_csv("workflow-manifest.csv",
  where description contains any keyword
  order by relevance desc
  limit 5)
```

### Pattern 3: Find Method by Analysis Need
```
analysis_type = "deep_technical_architecture"
method = find_in_csv("methods.csv",
  where category == "technical" or category == "advanced"
  matching method_name contains "architecture" or contains "decision")
return method with facilitation_prompts
```

### Pattern 4: Check Tool Availability
```
tool_name = "party-mode"
tool = find_in_csv("common-workflow-tools.csv", name == tool_name)
if tool.requires_install:
  warn user about installation needed
else:
  tool is available in: tool.url or project path
```

## Data Quality Notes

- **workflow-manifest**: 52 records, actively maintained
- **methods.csv**: 50 unique methods with detailed descriptions
- **solving-methods.csv**: 31 problem-solving techniques with guiding questions
- **common-workflow-tools**: 19 tools, marked as "always" (core) or "example" (optional)
- **tool-manifest**: 19 tool definitions with module locations

## Maintenance

When new workflows/tools are added:
1. Add entry to workflow-manifest.csv with all required fields
2. If new method type, add to appropriate methods CSV
3. Update this guide with category mappings
4. Re-validate CSV schemas match Step files

---

## Advanced: Confidence Scoring for Workflow Selection

### Scoring Formula
```
Total Score = (CSV Match Score × 0.6) + (Relevance Score × 0.4)

CSV Match Score:
  - Exact name match: 100 points
  - Tag match: 75 points per matching tag
  - Module match: 50 points
  - Description keyword match: 25 points per match

Relevance Score:
  - Task complexity alignment: 0-30 points
  - Time constraint fit: 0-20 points
  - User skill level match: 0-20 points
  - Dependencies satisfied: 0-30 points
```

### Ranking Example
```
Task: "Create a PRD for a new feature"

Results:
1. bmm-create-prd
   - Name match: +100
   - Tags match ("prd"): +75
   - Module match (bmm): +50
   - CSV Score: 100 × 0.6 = 60
   - Relevance: 80 points × 0.4 = 32
   - TOTAL: 92 ✓ EXCELLENT

2. bmm-create-product-brief
   - Tag match ("product"): +75
   - Module match (bmm): +50
   - CSV Score: 75 × 0.6 = 45
   - Relevance: 70 points × 0.4 = 28
   - TOTAL: 73 ✓ GOOD

3. cis-design-thinking
   - Description keyword match ("feature"): +25
   - Module match (cis): +50
   - CSV Score: 50 × 0.6 = 30
   - Relevance: 40 points × 0.4 = 16
   - TOTAL: 46 ✓ FAIR
```

### Integration with MCP Tools

If CSV top match has score < 70, supplement with:
1. **Memory search**: `npx claude-flow@v3alpha memory search -q "[task]"`
2. **OctoCode search**: Find similar patterns in GitHub repos
3. **Brave/Tavily search**: Check public solutions and best practices
4. **Context7 search**: Look up framework/library documentation

Final recommendation combines all sources with weighted scores.
