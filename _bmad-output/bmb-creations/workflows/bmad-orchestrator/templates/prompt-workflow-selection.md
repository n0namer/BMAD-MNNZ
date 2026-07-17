---
title: "MCP Query Prompts - Workflow Selection"
guide_type: "Prompt Templates"
version: "2.0"
last_updated: "2026-02-26"
usage_context: "Step 02: Workflow Selection via MCP Tools"
---

# MCP Query Prompts for Workflow Selection

**Purpose:** Template prompts for querying MCP tools (Memory, OctoCode, Brave/Tavily, Context7) during Step 02 workflow selection.

**When to Use:** When CSV search doesn't have sufficient matches or confidence score is <70%

---

## 1. Memory Search Prompts (ReasoningBank)

### Template Structure

```python
mcp__claude-flow__memory_search({
  query: "[CONSTRUCTED_QUERY]",
  limit: 10,
  threshold: 0.5
})
```

### Query Templates by Task Type

#### A. Planning Task Template

**User Task:** "I need to create a product roadmap for Q2 2026"

**Memory Search Query:**
```
Product roadmap planning workflow strategy quarterly planning
```

**Alternative Queries:**
1. `product planning workflow template`
2. `quarterly roadmap creation process`
3. `strategic planning workflow bmm`
4. `product strategy planning BMAD workflow`

**Confidence Indicators:**
- Exact match: "product roadmap workflow" → Confidence 85-100%
- Pattern match: Contains "roadmap" + "planning" → Confidence 70-85%
- Partial match: Contains "planning" OR "product" → Confidence 55-70%

---

#### B. Architecture Design Task Template

**User Task:** "Design microservices architecture for our API"

**Memory Search Query:**
```
Microservices architecture design workflow system design pattern
```

**Alternative Queries:**
1. `API architecture design methodology`
2. `system architecture workflow template`
3. `distributed system design patterns`
4. `architecture decision records workflow`

**Confidence Indicators:**
- Exact: "microservices architecture workflow" → 85-100%
- Pattern: "architecture" + ("design" OR "decision") → 70-85%
- Partial: "architecture" OR "design" → 55-70%

---

#### C. Testing & QA Task Template

**User Task:** "Set up automated testing for our CI/CD pipeline"

**Memory Search Query:**
```
Automated testing CI/CD pipeline test automation workflow ATDD
```

**Alternative Queries:**
1. `test automation framework workflow`
2. `CI/CD testing pipeline strategy`
3. `acceptance test driven development process`
4. `continuous integration testing workflow`

**Confidence Indicators:**
- Exact: "test automation workflow" → 85-100%
- Pattern: ("testing" OR "test") + ("CI/CD" OR "automation") → 70-85%
- Partial: "testing" OR "CI" OR "automation" → 55-70%

---

#### D. Implementation/Development Task Template

**User Task:** "Implement user authentication module"

**Memory Search Query:**
```
User authentication implementation development workflow security
```

**Alternative Queries:**
1. `authentication system development pattern`
2. `user login feature implementation workflow`
3. `JWT authentication development guide`
4. `OAuth2 integration workflow`

**Confidence Indicators:**
- Exact: "authentication implementation workflow" → 85-100%
- Pattern: ("authentication" OR "auth") + ("implement" OR "development") → 70-85%
- Partial: "authentication" OR "development" → 55-70%

---

### Query Construction Algorithm

```
Query = [Core_Concept] + [Task_Type] + [Modifiers]

Core_Concept:  [Domain/feature name]
               e.g., "authentication", "roadmap", "architecture"

Task_Type:     [Action verb + workflow]
               Options: "workflow", "process", "pattern", "template",
                       "implementation", "design", "planning"

Modifiers:     [Additional context]
               Options: module names (bmm, bmb, tea, cis),
                       technology (CI/CD, microservices, ATDD),
                       methodology (agile, lean, design-thinking)

Example Construction:
  Core: "product"
  + Task: "roadmap planning workflow"
  + Modifiers: "quarterly strategic BMAD"
  = Final Query: "product roadmap planning workflow quarterly strategic BMAD"
```

---

## 2. OctoCode Search Prompts (GitHub Patterns)

### Template Structure

```python
mcp__octocode__githubSearchCode({
  queries: [{
    mainResearchGoal: "[GOAL]",
    researchGoal: "[SPECIFIC_GOAL]",
    reasoning: "[WHY_THIS_SEARCH]",
    keywordsToSearch: ["[keyword1]", "[keyword2]", "[keyword3]"],
    owner: "[optional: target owner]",
    repo: "[optional: target repo]",
    extension: "[optional: file type]"
  }]
})
```

### Query Templates by Pattern Type

#### A. API Development Pattern

**Goal:** Find workflow implementations for API design

**Search Query:**
```python
{
  mainResearchGoal: "Find workflow patterns for API development",
  researchGoal: "Find GitHub repos with API design workflows and implementations",
  reasoning: "User needs API development workflow - search GitHub for practical examples",
  keywordsToSearch: ["api-workflow", "rest-api-design", "api-architecture", "openapi-spec"],
  extension: "md"
}
```

**Expected Results:**
- Workflow repositories with API design patterns
- API documentation standards
- API architecture decision records

---

#### B. Testing Framework Pattern

**Goal:** Find ATDD/BDD testing workflow implementations

**Search Query:**
```python
{
  mainResearchGoal: "Find testing workflow implementations",
  researchGoal: "Find GitHub repos with test automation and ATDD frameworks",
  reasoning: "User needs testing workflow - search for test framework patterns",
  keywordsToSearch: ["atdd-workflow", "test-automation", "bdd-framework", "e2e-testing"],
  extension: "md"
}
```

**Expected Results:**
- Test automation frameworks
- ATDD/BDD implementation guides
- Testing best practices

---

#### C. Architecture Decision Pattern

**Goal:** Find architecture documentation patterns

**Search Query:**
```python
{
  mainResearchGoal: "Find architecture design workflow patterns",
  researchGoal: "Find repos with architecture decision records and design patterns",
  reasoning: "User designing system - search for ADR and architecture patterns",
  keywordsToSearch: ["architecture-decision-record", "adr-template", "system-design", "microservices-pattern"],
  extension: ["md", "yml", "yaml"]
}
```

**Expected Results:**
- Architecture decision record templates
- System design patterns
- Microservices architecture examples

---

### Confidence Scoring for GitHub Results

| Match Quality | Indicators | Score |
|---------------|-----------|-------|
| **Excellent** | Exact repo match + active maintenance + >100 stars | 85-100% |
| **Good** | Partial match + recent commits + >50 stars | 70-85% |
| **Fair** | Pattern match + some documentation | 55-70% |
| **Low** | Weak match + unclear context | 40-54% |

---

## 3. Brave/Tavily Search Prompts (Public Web Search)

### Template Structure

```python
mcp__tavily__tavily_search({
  query: "[CONSTRUCTED_QUERY]",
  search_depth: "advanced",  # For comprehensive results
  max_results: 10,
  topic: "general"
})
```

### Query Templates by Domain

#### A. Product Management Query

**Task:** "Create product strategy and roadmap"

**Search Query:**
```
Product management workflow template strategic planning best practices 2025
```

**Search Depth:** `advanced` (comprehensive product strategy info)

**Expected Results:**
- Product planning frameworks
- Roadmapping templates
- Strategy development articles
- Case studies

---

#### B. System Architecture Query

**Task:** "Design scalable cloud architecture"

**Search Query:**
```
Cloud architecture design patterns microservices scalability 2025 best practices
```

**Search Depth:** `advanced`

**Expected Results:**
- Architecture patterns and frameworks
- Cloud design best practices
- Case studies and tutorials
- Tools and technologies

---

#### C. Testing & Quality Assurance Query

**Task:** "Establish QA strategy and test automation"

**Search Query:**
```
QA testing strategy test automation framework continuous integration 2025
```

**Search Depth:** `advanced`

**Expected Results:**
- QA methodologies and frameworks
- Test automation tools and patterns
- CI/CD integration guides
- Industry best practices

---

#### D. User Experience Design Query

**Task:** "Design user experience for new product"

**Search Query:**
```
UX design workflow user research prototyping usability testing 2025
```

**Search Depth:** `advanced`

**Expected Results:**
- UX design methodologies
- Research and prototyping guides
- Usability testing frameworks
- Design system templates

---

### Query Optimization Tips

**Keywords to Include:**
- Year (2025, 2026) for recent information
- "best practices" or "guide" for methodology
- "workflow" or "process" for structured approaches
- Industry-specific terms (cloud, microservices, agile, etc.)

**Keywords to Exclude:**
- Year constraint (if historical info needed)
- "forum" or "stack-overflow" (unless specifically needed)
- Brand names (unless technology-specific)

---

## 4. Context7 Search Prompts (Library Documentation)

### Template Structure

```python
mcp__context7__resolve-library-id({
  query: "[USER_TASK_DESCRIPTION]",
  libraryName: "[LIBRARY_OR_FRAMEWORK_NAME]"
})

# Then query documentation:
mcp__context7__query-docs({
  libraryId: "[RETURNED_LIBRARY_ID]",
  query: "[SPECIFIC_DOCUMENTATION_QUESTION]"
})
```

### Query Templates by Framework

#### A. Web Framework Query (Next.js/React)

**User Task:** "Build scalable web application"

**Step 1: Resolve Library**
```python
{
  query: "Create scalable web application with React and Next.js",
  libraryName: "Next.js"
}
```

**Step 2: Query Documentation**
```python
{
  libraryId: "/vercel/next.js",
  query: "How to structure a scalable Next.js application with API routes, middleware, and deployment best practices?"
}
```

**Expected Documentation:**
- Architecture patterns
- Project structure templates
- API design guidelines
- Deployment strategies

---

#### B. Testing Framework Query (Jest/Cypress)

**User Task:** "Set up comprehensive testing"

**Step 1: Resolve Library**
```python
{
  query: "Set up automated testing with Jest and Cypress",
  libraryName: "Jest"
}
```

**Step 2: Query Documentation**
```python
{
  libraryId: "/facebook/jest",
  query: "How to configure Jest for unit, integration, and snapshot testing with code coverage reports?"
}
```

**Expected Documentation:**
- Configuration examples
- Testing patterns
- Coverage requirements
- CI/CD integration

---

#### C. API Framework Query (Express/FastAPI)

**User Task:** "Design RESTful API"

**Step 1: Resolve Library**
```python
{
  query: "Build RESTful API with best practices and validation",
  libraryName: "Express.js"
}
```

**Step 2: Query Documentation**
```python
{
  libraryId: "/expressjs/express",
  query: "How to design a RESTful API with middleware, authentication, error handling, and OpenAPI documentation?"
}
```

**Expected Documentation:**
- API design patterns
- Authentication strategies
- Error handling best practices
- Documentation generation

---

#### D. Database Query (PostgreSQL/MongoDB)

**User Task:** "Design database schema and queries"

**Step 1: Resolve Library**
```python
{
  query: "Design database schema with relationships and optimization",
  libraryName: "PostgreSQL"
}
```

**Step 2: Query Documentation**
```python
{
  libraryId: "/postgres/docs",
  query: "How to design normalized schemas, create indexes, optimize queries, and ensure data consistency?"
}
```

**Expected Documentation:**
- Schema design patterns
- Indexing strategies
- Query optimization
- Consistency guarantees

---

## 5. Composite Search Strategy

### When CSV Search Insufficient (Score < 70%)

**Execute in Sequence:**

```
Step 1: CSV Search (Primary)
  ├─ If Score >= 70%: Use CSV result
  └─ If Score < 70%: Continue to Step 2

Step 2: Memory Search (Fast, Relevant)
  ├─ Query: [Construct from keywords]
  ├─ Wait: ~100-200ms
  └─ If Results Found: Add 40% weight to Memory score

Step 3: OctoCode Search (Practical Examples)
  ├─ Query: [Find repos with pattern]
  ├─ Wait: ~1-2 seconds
  └─ If Results Found: Add 30% weight to GitHub score

Step 4: Brave/Tavily Search (General Knowledge)
  ├─ Query: [Search web for best practices]
  ├─ Wait: ~2-5 seconds
  └─ If Results Found: Add 20% weight to Web score

Step 5: Context7 Search (Framework-Specific)
  ├─ Query: [Find framework documentation]
  ├─ Wait: ~500ms-1s
  └─ If Results Found: Add 10% weight to Doc score

Step 6: Aggregate & Score
  ├─ Calculate: (CSV×0.4) + (Memory×0.4) + (GitHub×0.3) + (Web×0.2) + (Docs×0.1)
  └─ Normalize to 0-100%
```

### Timeouts & Fallbacks

| Source | Timeout | Fallback |
|--------|---------|----------|
| Memory | 500ms | Use CSV result |
| GitHub | 2s | Use Memory or CSV |
| Brave | 5s | Use GitHub or Memory |
| Context7 | 1s | Use CSV or Brave |

**If All Fail:** Use best CSV match (even if < 70%) + Offer manual workflow selection

---

## 6. Confidence Scoring Examples

### Example 1: Product Roadmap Planning

**User Task:** "Create quarterly product roadmap"

**Search Results:**
```
CSV:      bmm-create-prd match score: 75% (tag: "prd|planning")
Memory:   "product-planning-workflow" score: 82% (3 matches)
GitHub:   "roadmap-templates" score: 70% (active repo)
Brave:    "product roadmap best practices" score: 85% (multiple sources)
Context7: No relevant library found

Weighted Score Calculation:
  CSV (75) × 0.4 = 30
  Memory (82) × 0.4 = 32.8
  GitHub (70) × 0.3 = 21
  Brave (85) × 0.2 = 17
  Context7 (0) × 0.1 = 0
  ──────────────────────
  TOTAL = 100.8 → 100% (capped) = EXCELLENT
```

**Recommendation:** Use `bmm-create-prd` with high confidence, supplement with Memory patterns and Brave best practices.

---

### Example 2: API Development

**User Task:** "Build REST API with authentication"

**Search Results:**
```
CSV:      No direct match - score: 0%
Memory:   "api-development-workflow" score: 72%
GitHub:   "rest-api-best-practices" score: 78%
Brave:    "REST API design guide" score: 80%
Context7: Express.js documentation score: 75%

Weighted Score Calculation:
  CSV (0) × 0.4 = 0
  Memory (72) × 0.4 = 28.8
  GitHub (78) × 0.3 = 23.4
  Brave (80) × 0.2 = 16
  Context7 (75) × 0.1 = 7.5
  ──────────────────────
  TOTAL = 75.7% = GOOD
```

**Recommendation:** No perfect CSV match, but strong support from MCP sources. Suggest `bmm-dev-story` + supplement with Memory patterns, GitHub examples, and Express.js documentation.

---

## 7. Integration with Step-02 Workflow

### Pseudo-Code

```python
def step_02_mcp_search(user_task: str, csv_best_match: Dict) -> Dict:
    """
    Execute MCP searches if CSV confidence < 70%
    """

    if csv_best_match['confidence'] >= 70:
        return csv_best_match  # CSV is good enough

    # Extract keywords from user task
    keywords = extract_keywords(user_task)

    # Execute MCP searches in parallel (where possible)
    mcp_results = {
        'memory': memory_search(construct_query(keywords, 'memory')),
        'github': octocode_search(construct_query(keywords, 'github')),
        'brave': brave_search(construct_query(keywords, 'brave')),
        'context7': context7_search(construct_query(keywords, 'context7'))
    }

    # Score and aggregate
    final_score = calculate_aggregate_score(csv_best_match, mcp_results)

    return {
        'primary': csv_best_match or top_mcp_result(mcp_results),
        'confidence': final_score,
        'sources': mcp_results,
        'recommendation': format_recommendation(final_score)
    }
```

---

## 8. Quick Reference Table

| Task Type | CSV Keyword | Memory Query | GitHub Keyword | Brave Search | Context7 |
|-----------|------------|--------------|----------------|--------------|----------|
| **Product Planning** | prd, planning | "product roadmap workflow" | "roadmap-template" | "product strategy 2025" | N/A |
| **Architecture** | architecture, design | "system architecture workflow" | "architecture-pattern" | "cloud design 2025" | AWS/Azure docs |
| **Testing** | testing, qa | "test automation workflow" | "test-framework" | "QA testing 2025" | Jest, Cypress docs |
| **API Dev** | dev, implementation | "api development workflow" | "rest-api-guide" | "REST API design" | Express, FastAPI docs |
| **UX Design** | ux, design | "ux design workflow" | "design-system" | "UX design 2025" | Figma docs |

---

*Prompt Templates Version: 2.0 | Last Updated: 2026-02-26*
