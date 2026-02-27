# Milestone Dependency Patterns

## Detection Rules

### Explicit Dependencies
Pattern: "Requires X" in phase description
- Parse: Look for keywords: `requires`, `depends on`, `needs`, `after`, `following`
- Extract: Predecessor milestone/phase names
- Validate: Predecessor exists in milestone list

### Implicit Dependencies
Pattern: Sequential phases have predecessor dependency
- **Sequential:** Phase N depends on Phase N-1 by default
- **Blocking:** Cannot start Phase N until Phase N-1 completes
- **Resource:** Phases sharing same resource must serialize

### Parallel Dependencies
Pattern: Phases sharing no resources can run parallel
- **Independent:** No shared resources or data dependencies
- **Convergent:** Multiple parallel phases → single downstream milestone
- **Divergent:** Single phase → multiple parallel downstream phases

## Dependency Types

| Type | Definition | Graph Pattern | Example |
|------|------------|---------------|---------|
| **Sequential** | M2 starts after M1 completes | M1 → M2 | Foundation → Core Features |
| **Parallel** | M2 and M3 both depend on M1, can run simultaneously | M1 → {M2, M3} | Backend + Frontend after Design |
| **Convergent** | M4 requires both M2 and M3 to complete | {M2, M3} → M4 | Testing requires Backend + Frontend |
| **Blocking** | M2 cannot start until M1 100% complete | M1 ⊣ M2 | Legal approval blocks launch |

## Validation Rules

### 1. No Circular Dependencies
```
FORBIDDEN: M1 → M2 → M3 → M1
ALLOWED:   M1 → M2 → M3
```

### 2. Single Start Node
- At least one milestone has no predecessors (entry point)
- Multiple start nodes allowed if truly independent work streams

### 3. Single End Node (Recommended)
- At least one milestone has no successors (project completion)
- Recommended: All paths converge to final integration/launch milestone

### 4. All Reachable
- Every milestone must be reachable from at least one start node
- Orphan milestones (unreachable) indicate planning error

### 5. Dependency Depth
- Maximum depth: 5 levels (deeper = too complex)
- Optimal: 3-4 levels for most projects

## Dependency Commands

### Add Dependency
```
ADD M3 → M2
```
Effect: M3 now depends on M2 (M3 starts after M2 completes)

### Remove Dependency
```
REMOVE M3 → M1
```
Effect: M3 no longer depends on M1 (can start independently)

### Set Parallel
```
PARALLEL M2, M3
```
Effect: Both M2 and M3 depend only on shared predecessors, can run simultaneously

### Set Blocking
```
BLOCK M1 → M2
```
Effect: M2 cannot start until M1 reaches 100% completion (hard dependency)

## Common Patterns

### Pattern: Foundation → Parallel Tracks → Integration
```
     ┌─────────┐
     │   M1    │ Foundation
     └────┬────┘
          │
    ┌─────┴─────┐
    │           │
    v           v
┌───────┐  ┌───────┐
│  M2   │  │  M3   │  Backend || Frontend
└───┬───┘  └───┬───┘
    │          │
    └────┬─────┘
         │
         v
    ┌─────────┐
    │   M4    │ Integration
    └─────────┘
```

### Pattern: Sequential Chain
```
M1 → M2 → M3 → M4
```
Use when: Each phase builds directly on previous (no parallelization possible)

### Pattern: Divergent → Convergent
```
         ┌───────┐
    ┌────│  M2   │────┐
    │    └───────┘    │
┌───v───┐          ┌──v────┐
│  M1   │          │  M4   │
└───┬───┘          └───────┘
    │    ┌───────┐    │
    └────│  M3   │────┘
         └───────┘
```
Use when: Foundation splits into parallel tracks, then converges for launch

## Risk Assessment by Pattern

| Pattern | Risk Level | Reason |
|---------|------------|--------|
| Sequential only | HIGH | No parallelization, delays cascade |
| Parallel tracks | LOW | Can absorb delays in non-critical paths |
| Convergent | MEDIUM | Bottleneck at merge point |
| Deep dependency (5+ levels) | HIGH | Complex coordination, high delay risk |
| Minimal dependencies | LOW | Flexible, easy to reschedule |

## Examples by Domain

### Software Project
```
M1: Architecture Design (no deps)
M2: Backend API (deps: M1)
M3: Frontend UI (deps: M1)
M4: Integration Testing (deps: M2, M3)
M5: Deployment (deps: M4)

Pattern: Foundation → Parallel → Convergent → Sequential
```

### Content Creation
```
M1: Research & Outline (no deps)
M2: Write Chapters 1-5 (deps: M1)
M3: Write Chapters 6-10 (deps: M1)
M4: Editing & Review (deps: M2, M3)
M5: Publishing (deps: M4)

Pattern: Foundation → Parallel → Convergent → Sequential
```

### Product Launch
```
M1: Product Development (no deps)
M2: Marketing Campaign (deps: M1)
M3: Legal Compliance (deps: M1)
M4: Beta Testing (deps: M1)
M5: Launch (deps: M2, M3, M4)

Pattern: Foundation → Parallel convergent
```
