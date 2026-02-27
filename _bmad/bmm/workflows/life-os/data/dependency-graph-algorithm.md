# Dependency Graph & Timeline Calculation Algorithm

## Timeline Grid Calculation

### Algorithm Specification

```
INPUT:
  - milestones[] with start_date, end_date, duration_weeks
  - project_start_date
  - project_end_date

OUTPUT:
  - timeline_grid
  - week_markers[]
  - month_markers[]
  - milestone_positions[]

STEPS:

1. Calculate total_weeks = (end_date - start_date) / 7

2. Determine grid resolution:
   IF total_weeks <= 8:
     resolution = "daily"
     unit_size = 1 day
   ELSE IF total_weeks <= 16:
     resolution = "weekly"
     unit_size = 1 week
   ELSE:
     resolution = "monthly"
     unit_size = 1 week with month grouping

3. Generate week_markers[]:
   FOR each week from start_date to end_date:
     IF resolution == "daily":
       marker = day_name (e.g., "Mon", "Tue")
     ELSE IF resolution == "weekly":
       marker = week_number (e.g., "W01", "W02")
     ELSE:
       marker = week_of_month (e.g., "Feb W1", "Feb W2")
     APPEND marker to week_markers[]

4. Generate month_markers[]:
   FOR each month boundary in range:
     marker = month_name (e.g., "Feb", "Mar", "Apr")
     APPEND marker to month_markers[]

5. Calculate milestone positions:
   FOR each milestone:
     start_column = (milestone.start_date - project_start) / unit_size
     width = milestone.duration_weeks * (7 / unit_size)
     position = {
       row: milestone_index,
       start_column: start_column,
       width: width
     }
```

## Dependency Graph Construction

### Data Structure

```
milestone = {
  id: string,
  name: string,
  start_date: Date,
  end_date: Date,
  duration_weeks: float,
  dependencies: string[],  // IDs of prerequisite milestones
  earliest_start: Date,
  latest_start: Date,
  earliest_finish: Date,
  latest_finish: Date,
  slack: float
}

dependency_edge = {
  from_milestone: string,
  to_milestone: string,
  type: "finish-to-start" | "start-to-start" | "finish-to-finish"
}
```

### Forward Pass Algorithm

Calculate earliest start/finish dates:

```
ALGORITHM forward_pass(milestones[]):

  1. Initialize:
     FOR each milestone:
       milestone.earliest_start = null
       milestone.earliest_finish = null

  2. Find start milestones (no dependencies):
     start_milestones = milestones WHERE dependencies.length == 0

     FOR each start_milestone:
       start_milestone.earliest_start = project_start_date
       start_milestone.earliest_finish =
         start_milestone.earliest_start + milestone.duration_weeks

  3. Topologically sort milestones by dependencies

  4. Calculate earliest dates:
     FOR each milestone in sorted_order:
       IF milestone has dependencies:
         earliest_start_candidates = []

         FOR each dependency_id in milestone.dependencies:
           dependent_milestone = find_milestone(dependency_id)
           earliest_start_candidates.push(
             dependent_milestone.earliest_finish
           )

         milestone.earliest_start = MAX(earliest_start_candidates)

       milestone.earliest_finish =
         milestone.earliest_start + milestone.duration_weeks

  RETURN milestones with earliest_start/finish calculated
```

### Backward Pass Algorithm

Calculate latest start/finish dates:

```
ALGORITHM backward_pass(milestones[], project_end_date):

  1. Initialize:
     FOR each milestone:
       milestone.latest_start = null
       milestone.latest_finish = null

  2. Find end milestones (no successors):
     end_milestones = milestones WHERE not referenced in any dependencies

     FOR each end_milestone:
       end_milestone.latest_finish = project_end_date
       end_milestone.latest_start =
         end_milestone.latest_finish - milestone.duration_weeks

  3. Reverse topologically sort milestones

  4. Calculate latest dates:
     FOR each milestone in reverse_sorted_order:
       IF milestone has successors:
         latest_finish_candidates = []

         FOR each successor in milestones:
           IF successor.dependencies contains milestone.id:
             latest_finish_candidates.push(
               successor.latest_start
             )

         milestone.latest_finish = MIN(latest_finish_candidates)

       milestone.latest_start =
         milestone.latest_finish - milestone.duration_weeks

  RETURN milestones with latest_start/finish calculated
```

### Slack Calculation

```
ALGORITHM calculate_slack(milestones[]):

  FOR each milestone:
    milestone.slack =
      milestone.latest_start - milestone.earliest_start

    # Alternative calculation (should be same):
    # milestone.slack = milestone.latest_finish - milestone.earliest_finish

  RETURN milestones with slack calculated
```

## Dependency Validation

### Circular Dependency Detection

```
ALGORITHM detect_circular_dependencies(milestones[]):

  visited = {}
  recursion_stack = {}

  FUNCTION has_cycle(milestone_id):
    visited[milestone_id] = true
    recursion_stack[milestone_id] = true

    milestone = find_milestone(milestone_id)

    FOR each dependency_id in milestone.dependencies:
      IF not visited[dependency_id]:
        IF has_cycle(dependency_id):
          RETURN true
      ELSE IF recursion_stack[dependency_id]:
        RETURN true  # Cycle detected

    recursion_stack[milestone_id] = false
    RETURN false

  FOR each milestone:
    IF not visited[milestone.id]:
      IF has_cycle(milestone.id):
        RETURN {
          has_cycle: true,
          cycle_path: reconstruct_cycle(recursion_stack)
        }

  RETURN {has_cycle: false}
```

### Invalid Dependency Detection

```
ALGORITHM validate_dependencies(milestones[]):

  errors = []

  FOR each milestone:
    FOR each dependency_id in milestone.dependencies:

      # Check if dependency exists
      IF not find_milestone(dependency_id):
        errors.push({
          type: "missing_dependency",
          milestone: milestone.id,
          dependency: dependency_id
        })

      # Check for self-dependency
      IF dependency_id == milestone.id:
        errors.push({
          type: "self_dependency",
          milestone: milestone.id
        })

      # Check chronological validity
      dependent = find_milestone(dependency_id)
      IF dependent.end_date > milestone.start_date:
        errors.push({
          type: "invalid_dates",
          milestone: milestone.id,
          dependency: dependency_id,
          message: "Dependency finishes after milestone starts"
        })

  RETURN errors
```

## Topological Sort

```
ALGORITHM topological_sort(milestones[]):

  visited = {}
  stack = []

  FUNCTION visit(milestone_id):
    IF visited[milestone_id]:
      RETURN

    visited[milestone_id] = true
    milestone = find_milestone(milestone_id)

    FOR each dependency_id in milestone.dependencies:
      visit(dependency_id)

    stack.push(milestone_id)

  FOR each milestone:
    visit(milestone.id)

  RETURN reverse(stack)  # Reverse to get correct order
```

## Dependency Arrow Positioning

### ASCII Arrow Calculation

```
ALGORITHM calculate_dependency_arrows(milestones[], timeline_grid):

  arrows = []

  FOR each milestone:
    FOR each dependency_id in milestone.dependencies:
      dependent = find_milestone(dependency_id)

      arrow = {
        from_row: dependent.position.row,
        to_row: milestone.position.row,
        from_column: dependent.position.start_column + dependent.position.width,
        to_column: milestone.position.start_column,
        style: milestone.on_critical_path ? "bold" : "normal"
      }

      arrows.push(arrow)

  RETURN arrows
```

## Example Calculation

Given milestones:
- M1: No dependencies, 2 weeks
- M2: Depends on M1, 3 weeks
- M3: Depends on M1, 2.5 weeks
- M4: Depends on M2 and M3, 2 weeks

### Forward Pass Result

```
M1: ES=Week0, EF=Week2
M2: ES=Week2, EF=Week5
M3: ES=Week2, EF=Week4.5
M4: ES=Week5, EF=Week7  # Must wait for M2 (Week5), not M3 (Week4.5)
```

### Backward Pass Result

```
Project end: Week7
M4: LS=Week5, LF=Week7
M2: LS=Week2, LF=Week5
M3: LS=Week2.5, LF=Week5  # Can start later than M2
M1: LS=Week0, LF=Week2
```

### Slack Calculation

```
M1: slack = 0 weeks (critical)
M2: slack = 0 weeks (critical)
M3: slack = 0.5 weeks (can delay up to 0.5 weeks)
M4: slack = 0 weeks (critical)
```
