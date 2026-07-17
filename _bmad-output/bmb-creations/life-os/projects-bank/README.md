# Projects Bank

The Projects Bank contains all active, completed, and terminated projects with full context, tracking, and artifacts.

## Purpose

- Maintain single source of truth for all project work
- Track progress across multiple concurrent projects
- Archive completed work with learnings and artifacts
- Learn from killed projects to improve future decisions

## Folder Structure

### active/
**Purpose**: Currently running projects

Each project is a FOLDER with structure:
```
{project-id}/
├── project.md         # Main file with metadata and overview
├── plan.md           # Detailed implementation plan
├── tasks/            # Task breakdown and tracking
├── artifacts/        # Deliverables and outputs
└── logs/             # Progress logs and decisions
```

**Characteristics**:
- Started date in the past
- Progress < 100%
- Regular updates in logs/
- Active task tracking

### completed/
**Purpose**: Successfully finished projects

- Same folder structure as active/
- Progress = 100%
- Contains final artifacts and retrospective
- Learnings documented in logs/
- Reference for similar future projects

### killed/
**Purpose**: Terminated projects with rationale

- Same folder structure as active/
- Contains kill decision rationale in project.md
- Documents what was learned (even from failure)
- Prevents repeating mistakes

## Project Lifecycle

```
1. ACTIVATE  → active/        (from ideas-bank/planned/)
2. EXECUTE   → active/        (iterative progress tracking)
3. COMPLETE  → completed/     (100% done, retro documented)
   OR
   KILL      → killed/        (explicit decision with reasons)
```

## Template

Use `templates/project.template.md` to create new project folders with proper structure.

## Project Tracking

Each project folder must maintain:

1. **project.md**: Current status, metadata, origin story
2. **plan.md**: Implementation approach (can evolve)
3. **tasks/**: Active task list with dependencies
4. **artifacts/**: Concrete deliverables
5. **logs/**: Decision log and progress notes

## Best Practices

1. Limit active projects (3-5 max across all spheres)
2. Update project.md progress weekly minimum
3. Log key decisions immediately in logs/
4. Move to completed/ only when truly done (don't leave orphans)
5. Write kill rationale immediately when terminating
6. Review completed/ quarterly for patterns and learnings

## Status Codes

- **active**: Work in progress, resources allocated
- **completed**: 100% done, artifacts delivered, retro complete
- **killed**: Explicitly terminated with documented reasoning

## Integration with Ideas Bank

- New projects MUST link to origin idea in frontmatter
- When activating idea → copy idea file to `ideas-bank/archive/activated/`
- Maintain traceability: idea ID → project ID

## Metrics to Track

- Active projects count (prevent overcommitment)
- Time from activation to completion (velocity)
- Kill rate and reasons (decision quality)
- Artifact count per project (output productivity)
