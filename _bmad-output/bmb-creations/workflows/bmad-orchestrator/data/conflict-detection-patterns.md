# Conflict Detection Patterns

## Conflict Types

### 1. Read-After-Write (RAW)

**Description:** Workflow B reads a file that Workflow A writes to.

**Pattern:**
```
Workflow A: WRITE file.md
Workflow B: READ file.md  [DEPENDS ON A]
```

**Detection:**
- Check if any workflow's inputs overlap with another's outputs
- Order: A must complete before B starts

**Example:**
```yaml
raw_conflict_example:
  workflow_a:
    outputs: ["prd.md"]
  workflow_b:
    inputs: ["prd.md"]
  resolution: "Sequential execution: A → B"
```

### 2. Write-After-Read (WAR)

**Description:** Workflow B writes to a file that Workflow A reads.

**Pattern:**
```
Workflow A: READ file.md
Workflow B: WRITE file.md  [CAN RUN IN PARALLEL]
```

**Detection:**
- Generally safe for parallel execution
- Exception: If A depends on file state that B changes

**Example:**
```yaml
war_safe_example:
  workflow_a:
    inputs: ["brief.md"]
    outputs: ["prd.md"]
  workflow_b:
    inputs: ["brief.md"]
    outputs: ["architecture.md"]
  resolution: "Parallel execution safe - different outputs"
```

### 3. Write-After-Write (WAW)

**Description:** Both workflows write to the same file.

**Pattern:**
```
Workflow A: WRITE file.md
Workflow B: WRITE file.md  [CONFLICT!]
```

**Detection:**
- Same output file from multiple workflows
- Must resolve: sequential or merge strategy

**Example:**
```yaml
waw_conflict_example:
  workflow_a:
    outputs: ["config.json"]
  workflow_b:
    outputs: ["config.json"]
  resolution: "CONFLICT - Must sequentialize or use append strategy"
```

## Conflict Detection Algorithm

```
1. Collect all workflows with their inputs and outputs
2. Build adjacency matrix of file access
3. For each file:
   a. Count readers and writers
   b. If multiple writers → WAW conflict
   c. If writer followed by reader → RAW dependency
   d. If reader and writer concurrent → Check for WAR issues
4. Build dependency graph
5. Identify parallel-safe zones
```

## Parallel Zone Examples

### Safe Parallel Zone

```
Zone 1 (Parallel):
  - create-prd: reads brief.md, writes prd.md
  - create-ux: reads brief.md, writes ux-design.md
  
Result: ✅ SAFE - No shared outputs
```

### Unsafe Parallel Zone

```
Zone 1 (Parallel):
  - edit-prd: reads/writes prd.md
  - validate-prd: reads prd.md
  
Result: ❌ UNSAFE - RAW dependency
Resolution: Sequential - edit first, then validate
```

## Visual Dependency Representation

```
┌─────────────────────────────────────────────────────────┐
│                    DEPENDENCY GRAPH                      │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  brief.md                                                │
│     │                                                    │
│     ├──► [create-prd] ──► prd.md ──► [validate-prd]     │
│     │                                                    │
│     └──► [create-ux] ──► ux-design.md                    │
│            │                                             │
│            └──► [create-arch] ──► architecture.md        │
│                      │                                   │
│                      └──► [create-epics] ──► epics.md    │
│                                                          │
│  PARALLEL ZONES:                                         │
│  • Zone 1: [create-prd] + [create-ux]                    │
│  • Zone 2: [validate-prd]                                │
│  • Zone 3: [create-arch]                                 │
│  • Zone 4: [create-epics]                                │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

## Large File Handling Strategies

### Strategy 1: Range Read

```yaml
large_file_strategy:
  file: "large-document.md"
  lines: 5000
  approach:
    - Read only sections that need modification
    - Use line numbers: read_file(startLine, endLine)
    - Keep context within 200-line window
```

### Strategy 2: Append-Only Building

```yaml
append_strategy:
  target: "new-document.md"
  approach:
    - Build document section by section
    - Append new content instead of rewriting
    - Minimize context usage
```

### Strategy 3: Chunked Processing

```yaml
chunk_strategy:
  file: "huge-spec.md"
  lines: 10000
  approach:
    - Split into 1000-line chunks
    - Process chunks independently
    - Merge results at the end
```

## Safety Measures

### Context Overflow Prevention

```yaml
context_management:
  thresholds:
    warning: 150000  # tokens
    critical: 200000 # tokens
  actions:
    warning: "Prompt user about large file"
    critical: "Force range read mode"
```

### Backup Before Write

```yaml
backup_strategy:
  before_write:
    - Copy original to .backup/filename.ts.bak
    - Log backup location
    - Enable rollback capability
```

### Checkpoint System

```yaml
checkpoint_strategy:
  frequency: "every phase"
  storage: "intermediate/checkpoint-phase-{N}.md"
  includes:
    - Completed workflows
    - Modified files
    - Context usage stats
```

## Common Conflict Resolution Patterns

### Pattern 1: Sequential Chaining

```
A → B → C (all dependent)
```

### Pattern 2: Fan-Out (Parallel)

```
    ┌─► B
A ──┼─► C  (B, C, D parallel)
    └─► D
```

### Pattern 3: Fan-In (Merge Point)

```
A ──┐
B ──┼─► E (E waits for A, B, C)
C ──┘
```

### Pattern 4: Diamond Pattern

```
    ┌─► B ──┐
A ──┤       ├─► D
    └─► C ──┘
```

## Example: Full Orchestration Plan

```
ORCHESTRATION PLAN: BMAD Cascade

Phase 1 (Parallel Zone 1):
  - bmad-bmm-create-product-brief

Phase 2 (Parallel Zone 2):
  - bmad-bmm-create-prd (reads brief)
  - bmad-bmm-create-ux-design (reads brief)

Phase 3 (Sequential):
  - bmad-bmm-create-architecture (reads prd, ux)

Phase 4 (Parallel Zone 3):
  - bmad-bmm-create-epics-and-stories (reads arch)
  - bmad-bmm-create-story (reads arch)

Phase 5 (Sequential):
  - bmad-bmm-sprint-planning (reads epics, stories)

Conflicts Detected: 0
Parallel Zones: 3
Sequential Dependencies: 2
```
