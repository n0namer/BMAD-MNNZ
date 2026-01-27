---
name: 'step-01-initialization'
description: 'Step 1: Initialization — Setup environment, load requirements, validate prerequisites'
layer: 'initialization'
menu:
  next: step-02-foundation-setup.md
  back: AGENTS-MD-GENERATOR-WORKFLOW.md
handler: A
---

# Step 1: Initialization

**Purpose:** Initialize the AGENTS.MD generation workflow, setup environment, load requirements, and validate prerequisites

## Overview

This step sets up the foundation for the AGENTS.MD generation workflow by initializing the environment, loading all necessary requirements, and validating that all prerequisites are met.

## Prerequisites

### System Requirements

- **Operating System:** Linux, macOS, or Windows with WSL
- **Shell:** Bash 4.0+ or compatible shell
- **Tools:** jq, git, curl, wget
- **Permissions:** Write access to workflow directory

### Environment Setup

```bash
# Set up environment variables
export WORKFLOW_DIR="$(pwd)"
export OUTPUT_DIR="$WORKFLOW_DIR/output"
export REQUIREMENTS_DIR="$WORKFLOW_DIR/requirements"
export LOGS_DIR="$WORKFLOW_DIR/logs"

# Create necessary directories
mkdir -p "$OUTPUT_DIR" "$REQUIREMENTS_DIR" "$LOGS_DIR"

# Set up logging
LOG_FILE="$LOGS_DIR/initialization.log"
exec > >(tee -a "$LOG_FILE")
exec 2>&1

echo "=== AGENTS.MD Generation Workflow - Initialization ==="
echo "Workflow directory: $WORKFLOW_DIR"
echo "Output directory: $OUTPUT_DIR"
echo "Requirements directory: $REQUIREMENTS_DIR"
echo "Log file: $LOG_FILE"
```

## Input Requirements

### Required Inputs

1. **BMAD Requirements Directory** - `requirements/` directory containing:
   - `bmad-requirements.md` - Core BMAD protocol requirements
   - `kr-requirements.md` - Key Result requirements
   - `user-requirements.md` - User-specific requirements

2. **PRD File** - `prd.md` containing:
   - Product requirements
   - User stories
   - Acceptance criteria

3. **North Star Description** - `north-star.md` containing:
   - Project vision
   - Success metrics
   - Long-term goals

### Optional Inputs

1. **Custom Requirements** - Additional requirement files
2. **Configuration Files** - Custom workflow configurations
3. **User Preferences** - Style and format preferences

## Process

### 1. Environment Validation

```bash
# Validate environment setup
validate_environment() {
    local errors=0
    
    # Check required tools
    local required_tools=("jq" "git" "curl" "wget")
    for tool in "${required_tools[@]}"; do
        if ! command -v "$tool" &> /dev/null; then
            echo "ERROR: Required tool not found: $tool"
            ((errors++))
        else
            echo "✓ Tool available: $tool"
        fi
    done
    
    # Check directory permissions
    if [ ! -w "$WORKFLOW_DIR" ]; then
        echo "ERROR: No write permission to workflow directory: $WORKFLOW_DIR"
        ((errors++))
    else
        echo "✓ Directory permissions OK: $WORKFLOW_DIR"
    fi
    
    # Check disk space
    local available_space=$(df "$WORKFLOW_DIR" | tail -1 | awk '{print $4}')
    local required_space=100000  # 100MB in KB
    
    if [ "$available_space" -lt "$required_space" ]; then
        echo "ERROR: Insufficient disk space. Available: ${available_space}KB, Required: ${required_space}KB"
        ((errors++))
    else
        echo "✓ Disk space sufficient: ${available_space}KB available"
    fi
    
    if [ $errors -eq 0 ]; then
        echo "✓ Environment validation passed"
        return 0
    else
        echo "✗ Environment validation failed with $errors errors"
        return 1
    fi
}
```

### 2. Requirements Loading

```bash
# Load and validate requirements
load_requirements() {
    echo "Loading requirements..."
    
    # Check for required requirement files
    local required_files=(
        "$REQUIREMENTS_DIR/bmad-requirements.md"
        "$REQUIREMENTS_DIR/kr-requirements.md"
        "$REQUIREMENTS_DIR/user-requirements.md"
        "$WORKFLOW_DIR/prd.md"
        "$WORKFLOW_DIR/north-star.md"
    )
    
    local missing_files=()
    for file in "${required_files[@]}"; do
        if [ ! -f "$file" ]; then
            missing_files+=("$file")
        fi
    done
    
    if [ ${#missing_files[@]} -gt 0 ]; then
        echo "ERROR: Missing required files:"
        for file in "${missing_files[@]}"; do
            echo "  - $file"
        done
        return 1
    fi
    
    echo "✓ All required files found"
    
    # Load BMAD requirements
    if [ -f "$REQUIREMENTS_DIR/bmad-requirements.md" ]; then
        echo "Loading BMAD requirements..."
        export BMAD_REQUIREMENTS=$(cat "$REQUIREMENTS_DIR/bmad-requirements.md")
    fi
    
    # Load KR requirements
    if [ -f "$REQUIREMENTS_DIR/kr-requirements.md" ]; then
        echo "Loading KR requirements..."
        export KR_REQUIREMENTS=$(cat "$REQUIREMENTS_DIR/kr-requirements.md")
    fi
    
    # Load user requirements
    if [ -f "$REQUIREMENTS_DIR/user-requirements.md" ]; then
        echo "Loading user requirements..."
        export USER_REQUIREMENTS=$(cat "$REQUIREMENTS_DIR/user-requirements.md")
    fi
    
    # Load PRD
    if [ -f "$WORKFLOW_DIR/prd.md" ]; then
        echo "Loading PRD..."
        export PRD_CONTENT=$(cat "$WORKFLOW_DIR/prd.md")
    fi
    
    # Load North Star
    if [ -f "$WORKFLOW_DIR/north-star.md" ]; then
        echo "Loading North Star description..."
        export NORTH_STAR=$(cat "$WORKFLOW_DIR/north-star.md")
    fi
    
    echo "✓ Requirements loaded successfully"
    return 0
}
```

### 3. Prerequisites Validation

```bash
# Validate all prerequisites
validate_prerequisites() {
    echo "Validating prerequisites..."
    
    local validation_errors=0
    
    # Validate BMAD requirements format
    if [ -n "$BMAD_REQUIREMENTS" ]; then
        if ! echo "$BMAD_REQUIREMENTS" | grep -q "BMAD"; then
            echo "ERROR: BMAD requirements missing BMAD protocol references"
            ((validation_errors++))
        fi
    fi
    
    # Validate KR requirements format
    if [ -n "$KR_REQUIREMENTS" ]; then
        if ! echo "$KR_REQUIREMENTS" | grep -q "KR"; then
            echo "ERROR: KR requirements missing Key Result references"
            ((validation_errors++))
        fi
    fi
    
    # Validate PRD format
    if [ -n "$PRD_CONTENT" ]; then
        if ! echo "$PRD_CONTENT" | grep -q "requirements"; then
            echo "ERROR: PRD missing requirements section"
            ((validation_errors++))
        fi
    fi
    
    # Validate North Star format
    if [ -n "$NORTH_STAR" ]; then
        if ! echo "$NORTH_STAR" | grep -q "vision"; then
            echo "ERROR: North Star missing vision section"
            ((validation_errors++))
        fi
    fi
    
    if [ $validation_errors -eq 0 ]; then
        echo "✓ All prerequisites validated successfully"
        return 0
    else
        echo "✗ Prerequisites validation failed with $validation_errors errors"
        return 1
    fi
}
```

### 4. State Initialization

```bash
# Initialize workflow state
initialize_state() {
    echo "Initializing workflow state..."
    
    # Create state file
    local state_file="$OUTPUT_DIR/state.json"
    cat > "$state_file" << EOF
{
  "workflow_started": "$(date -Iseconds)",
  "workflow_version": "6.0.0-alpha.23",
  "environment": {
    "workflow_dir": "$WORKFLOW_DIR",
    "output_dir": "$OUTPUT_DIR",
    "requirements_dir": "$REQUIREMENTS_DIR",
    "logs_dir": "$LOGS_DIR"
  },
  "requirements_loaded": {
    "bmad": ${BMAD_REQUIREMENTS:+true},
    "kr": ${KR_REQUIREMENTS:+true},
    "user": ${USER_REQUIREMENTS:+true},
    "prd": ${PRD_CONTENT:+true},
    "north_star": ${NORTH_STAR:+true}
  },
  "validation": {
    "environment": "pending",
    "prerequisites": "pending"
  },
  "current_step": "step-01-initialization",
  "status": "running"
}
EOF
    
    echo "✓ Workflow state initialized"
    return 0
}
```

## Output Files

### State File
- **File:** `output/state.json`
- **Content:** Workflow state and configuration
- **Format:** JSON

### Log File
- **File:** `logs/initialization.log`
- **Content:** Initialization process log
- **Format:** Text

## Quality Gates

- [ ] Environment validation passed
- [ ] All required files loaded
- [ ] Prerequisites validation successful
- [ ] Workflow state initialized
- [ ] No critical errors detected

## Troubleshooting

### Common Issues

1. **Missing required tools**
   - Install missing tools using package manager
   - Verify PATH configuration
   - Check tool versions

2. **Missing requirement files**
   - Create missing files with proper structure
   - Verify file paths and permissions
   - Check file content format

3. **Permission errors**
   - Check directory write permissions
   - Verify user ownership
   - Adjust file system permissions

4. **Disk space issues**
   - Free up disk space
   - Change output directory location
   - Clean up temporary files

### Support

For issues and support:
- Check `docs/KNOWN_ISSUES.md`
- Review `docs/TROUBLESHOOTING.md`
- Contact BMAD support team