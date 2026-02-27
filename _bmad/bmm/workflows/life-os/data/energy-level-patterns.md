# Energy Level Patterns

## Energy Block Definitions

### Morning (8am-12pm) - HIGH ENERGY
**Best for:** Deep work, complexity, creativity

**Examples:**
- Coding and architecture design
- Writing and strategic planning
- Complex problem-solving
- Creative tasks requiring focus

**Characteristics:**
- Require focus and minimal interruptions
- High cognitive load
- Peak mental clarity

### Afternoon (12pm-5pm) - MEDIUM ENERGY
**Best for:** Collaboration, meetings, reviews

**Examples:**
- Code reviews and testing
- Meetings and collaboration
- Research and documentation
- Moderate complexity tasks

**Characteristics:**
- Moderate focus required
- Interruptions acceptable
- Social interaction welcome

### Evening (5pm-9pm) - LOW ENERGY
**Best for:** Admin, cleanup, light tasks

**Examples:**
- Email and communication
- Filing and organizing
- Small bug fixes
- Reading and planning
- Tomorrow's preparation

**Characteristics:**
- Low cognitive load
- Can be interrupted
- Mechanical or routine tasks

## Balancing Algorithm

```python
morning_tasks = [t for t in daily_tasks if t.energy_level == "high"]
afternoon_tasks = [t for t in daily_tasks if t.energy_level == "medium"]
evening_tasks = [t for t in daily_tasks if t.energy_level == "low"]

# Calculate hours per block
morning_hours = sum(t.estimate_hours for t in morning_tasks)
afternoon_hours = sum(t.estimate_hours for t in afternoon_tasks)
evening_hours = sum(t.estimate_hours for t in evening_tasks)

# Validate balance (30% high / 50% medium / 20% low is ideal)
# Auto-rebalance if needed
if morning_hours > (total_allocated_hours * 0.5):
    # Move some high-energy tasks to afternoon with note
    pass
```

## Ideal Distribution

- **Morning:** 30% of total hours (high-energy tasks)
- **Afternoon:** 50% of total hours (medium-energy tasks)
- **Evening:** 20% of total hours (low-energy tasks)
