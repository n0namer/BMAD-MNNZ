---
name: 'step-03-content-generation-layer-session-monitoring'
description: 'Session Monitoring — Progress Tracking, State Management, Continuation'
layer: 'session-monitoring'
menu:
  next: step-03-content-generation-layer-best-practices.md
  back: step-03-content-generation-layer-reasoning-frameworks.md
handler: C
---

# Step 3: Content Generation — Session Monitoring

## Progress Tracking

### Progress Monitor
```bash
# Track workflow progress
PROGRESS_FILE="output/progress.json"

initialize_progress() {
    echo '{"steps": [], "current_step": 0, "total_steps": 0, "status": "running"}' > "$PROGRESS_FILE"
}

update_progress() {
    local step="$1"
    local status="$2"
    
    jq --arg step "$step" --arg status "$status" \
       '.steps += [{"step": $step, "status": $status, "timestamp": now}]' \
       "$PROGRESS_FILE" > temp.json && mv temp.json "$PROGRESS_FILE"
    
    local current=$(jq '.steps | length' "$PROGRESS_FILE")
    jq --argjson current "$current" '.current_step = $current' \
       "$PROGRESS_FILE" > temp.json && mv temp.json "$PROGRESS_FILE"
}

# Usage
initialize_progress
update_progress "step-01-initialization" "completed"
update_progress "step-02-foundation-setup" "completed"
update_progress "step-03-content-generation" "in_progress"
```

### State Management
```bash
# Manage workflow state
STATE_FILE="output/state.json"

save_state() {
    local state="$1"
    echo "$state" > "$STATE_FILE"
}

load_state() {
    if [ -f "$STATE_FILE" ]; then
        cat "$STATE_FILE"
    else
        echo '{"status": "new", "step": "none"}'
    fi
}

# Usage
save_state '{"status": "running", "step": "step-03-content-generation"}'
current_state=$(load_state)
echo "Current state: $current_state"
```

## Continuation

### Resume Workflow
```bash
# Resume from last completed step
resume_workflow() {
    local progress_file="$1"
    
    if [ ! -f "$progress_file" ]; then
        echo "No progress file found, starting from beginning"
        return 0
    fi
    
    local last_step=$(jq -r '.steps[-1].step' "$progress_file")
    local last_status=$(jq -r '.steps[-1].status' "$progress_file")
    
    echo "Resuming from step: $last_step (status: $last_status)"
    
    case "$last_step" in
        "step-01-initialization")
            if [ "$last_status" = "completed" ]; then
                run_step_02
            else
                run_step_01
            fi
            ;;
        "step-02-foundation-setup")
            if [ "$last_status" = "completed" ]; then
                run_step_03
            else
                run_step_02
            fi
            ;;
        "step-03-content-generation")
            if [ "$last_status" = "completed" ]; then
                run_step_04
            else
                run_step_03
            fi
            ;;
        *)
            echo "Unknown step: $last_step"
            return 1
            ;;
    esac
}

# Usage
resume_workflow "output/progress.json"
```

### Checkpoint System
```bash
# Create checkpoints
create_checkpoint() {
    local step="$1"
    local data="$2"
    
    local checkpoint_file="output/checkpoints/${step}.json"
    mkdir -p "output/checkpoints"
    
    echo "$data" > "$checkpoint_file"
    echo "Checkpoint created: $checkpoint_file"
}

# Load checkpoint
load_checkpoint() {
    local step="$1"
    
    local checkpoint_file="output/checkpoints/${step}.json"
    if [ -f "$checkpoint_file" ]; then
        cat "$checkpoint_file"
    else
        echo "Checkpoint not found: $checkpoint_file"
        return 1
    fi
}

# Usage
create_checkpoint "step-02-foundation-setup" '{"requirements_loaded": true, "architecture_defined": true}'
checkpoint_data=$(load_checkpoint "step-02-foundation-setup")