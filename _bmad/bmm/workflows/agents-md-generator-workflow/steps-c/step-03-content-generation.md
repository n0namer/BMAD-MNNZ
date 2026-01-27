# Step 3: Content Generation

**Purpose:** Generate AGENTS.MD content for all 8 layers, create .github/copilot-instructions.md, develop examples and templates, and build reasoning frameworks

## Overview

This step generates the actual content for both AGENTS.MD and .github/copilot-instructions.md files, implementing all 8 layers of the architecture with comprehensive content.

## Prerequisites

- Step 2: Foundation Setup completed
- All requirements loaded and validated
- 8-layer architecture structure defined
- KR compliance matrix created

## Input Requirements

### Required Inputs

1. **Requirements Metadata** - `output/requirements_metadata.json`
2. **Architecture Structure** - `output/architecture_structure.json`
3. **KR Requirements** - `output/kr_requirements.json`
4. **Validation Results** - `output/architecture_validation.json`

### Optional Inputs

1. **Custom Content** - Additional content specifications
2. **User Preferences** - Content style and format preferences

## Process

### 1. AGENTS.MD Content Generation

```bash
# Generate AGENTS.MD content
AGENTS_MD="output/AGENTS.MD"

# Clear existing content and start fresh
cat > "$AGENTS_MD" << 'EOF'
# AGENTS.MD 2.0

**Version:** 6.0.0-alpha.23
**Created:** 2026-01-24
**Purpose:** Single source of truth для BMAD-совместимой работы через GitHub Copilot Agents Tab

## Table of Contents

1. [UX Layer](#ux-layer)
2. [BMAD Protocol](#bmad-protocol)
3. [Phase Workflows](#phase-workflows)
4. [Task Templates](#task-templates)
5. [Examples](#examples)
6. [Reasoning Frameworks](#reasoning-frameworks)
7. [Session Monitoring](#session-monitoring)
8. [Best Practices](#best-practices)

---

## UX Layer

### Welcome Flow

Добро пожаловать в AGENTS.MD 2.0! Этот документ является главным методологическим и операционным манифестом для LLM в репозитории.

**Quick Start:**
1. Загрузите этот файл в LLM
2. Следуйте BMAD протоколу
3. Используйте task templates для типовых операций
4. Применяйте reasoning frameworks для сложных задач

### Navigation

**Phase-based Navigation:**
- [Phase 1: Discovery](#phase-1-discovery)
- [Phase 2: Planning](#phase-2-planning)
- [Phase 3: Implementation](#phase-3-implementation)
- [Phase 4: Validation](#phase-4-validation)

**Task-based Navigation:**
- [Common Tasks](#common-tasks)
- [Specialized Templates](#specialized-templates)
- [Examples](#examples)

### Feedback System

**Quality Gates:**
- [ ] Content preservation
- [ ] BMAD compliance
- [ ] GitHub Copilot compatibility
- [ ] File size limits

**Validation Points:**
- After each phase
- Before file generation
- During content merge

---

## BMAD Protocol

### Phase Management

**Phase 1: Discovery**
- Purpose: Understand requirements and constraints
- Inputs: User requirements, existing documentation
- Outputs: Requirement analysis, scope definition
- Tools: Advanced Elicitation, Brainstorming

**Phase 2: Planning**
- Purpose: Design solution architecture and plan implementation
- Inputs: Discovery outputs, BMAD requirements
- Outputs: Architecture design, implementation plan
- Tools: Party Mode, Sub-Agents

**Phase 3: Implementation**
- Purpose: Execute implementation according to plan
- Inputs: Planning outputs, task templates
- Outputs: Generated content, intermediate files
- Tools: File I/O, Sub-Processes

**Phase 4: Validation**
- Purpose: Validate outputs and ensure compliance
- Inputs: Implementation outputs, KR requirements
- Outputs: Final files, compliance report
- Tools: Validation frameworks, Quality gates

### Input/Output Specification

**Required Inputs:**
- BMAD requirements directory
- PRD file
- User preferences
- North star description

**Optional Inputs:**
- Custom requirements
- Additional context
- Style preferences

**Output Files:**
- `AGENTS.MD` (~100 слов)
- `.github/copilot-instructions.md` (~80 слов)

**Output Format:**
- Markdown format
- BMAD-compliant structure
- GitHub Copilot compatible

### Compliance Check

**KR Requirements Compliance:**
- [ ] KR-1: Binary identical files
- [ ] KR-2: BMAD phase understanding
- [ ] KR-3: GitHub Copilot compatibility
- [ ] KR-4: Content preservation
- [ ] KR-5: Realistic examples
- [ ] KR-6: Task templates
- [ ] KR-7: Steering guide
- [ ] KR-8: Agent autonomy
- [ ] KR-9: XML + pseudo-code
- [ ] KR-10: Advanced features

---

## Phase Workflows

### Phase 1: Discovery

**Workflow Steps:**
1. Load BMAD requirements
2. Analyze user requirements
3. Identify constraints and dependencies
4. Define scope and objectives

**Decision Points:**
- Requirements completeness
- Scope validation
- Constraint identification

**Output Artifacts:**
- Requirement analysis
- Scope definition
- Constraint documentation

### Phase 2: Planning

**Workflow Steps:**
1. Design 8-layer architecture
2. Map requirements to layers
3. Plan content generation strategy
4. Define validation criteria

**Decision Points:**
- Architecture validation
- Requirement mapping
- Content strategy

**Output Artifacts:**
- Architecture design
- Requirement mapping
- Content plan

### Phase 3: Implementation

**Workflow Steps:**
1. Generate layer content
2. Create task templates
3. Develop examples
4. Build reasoning frameworks

**Decision Points:**
- Content quality
- Template effectiveness
- Example relevance

**Output Artifacts:**
- Layer content
- Task templates
- Examples
- Reasoning frameworks

### Phase 4: Validation

**Workflow Steps:**
1. Validate content compliance
2. Check file size limits
3. Verify GitHub Copilot compatibility
4. Generate final output

**Decision Points:**
- Compliance validation
- Size validation
- Compatibility check

**Output Artifacts:**
- Final AGENTS.MD
- Final copilot instructions
- Compliance report

---

## Task Templates

### Common Tasks

#### Template 1: File Creation
```bash
# Purpose: Create new files with proper structure
# Usage: create_file <filename> <content_type>
create_file() {
    local filename="$1"
    local content_type="$2"
    
    # Validate inputs
    if [ -z "$filename" ] || [ -z "$content_type" ]; then
        echo "Usage: create_file <filename> <content_type>"
        return 1
    fi
    
    # Create directory if needed
    mkdir -p "$(dirname "$filename")"
    
    # Generate content based on type
    case "$content_type" in
        "markdown")
            cat > "$filename" << 'EOF'
# $filename

**Purpose:** [Describe purpose]
**Created:** $(date)
**Type:** [File type]

## Content

[Add content here]
EOF
            ;;
        "json")
            cat > "$filename" << 'EOF'
{
  "filename": "$filename",
  "content_type": "$content_type",
  "created": "$(date)",
  "purpose": "[Describe purpose]"
}
EOF
            ;;
        *)
            echo "Unknown content type: $content_type"
            return 1
            ;;
    esac
    
    echo "✓ Created file: $filename"
}
```

#### Template 2: Content Validation
```bash
# Purpose: Validate content against requirements
# Usage: validate_content <file> <requirements>
validate_content() {
    local file="$1"
    local requirements="$2"
    
    # Check if file exists
    if [ ! -f "$file" ]; then
        echo "✗ File not found: $file"
        return 1
    fi
    
    # Check file size
    local size=$(wc -c < "$file")
    if [ "$size" -gt 102400 ]; then  # 100KB limit
        echo "✗ File size exceeds limit: ${size} bytes"
        return 1
    fi
    
    # Check content structure
    if ! grep -q "^# " "$file"; then
        echo "✗ Missing title in file: $file"
        return 1
    fi
    
    echo "✓ Content validation passed for: $file"
}
```

### Specialized Templates

#### Template 3: BMAD Compliance Check
```bash
# Purpose: Check BMAD compliance
# Usage: check_bmad_compliance <file>
check_bmad_compliance() {
    local file="$1"
    
    # Check for BMAD protocol references
    if ! grep -q "BMAD" "$file"; then
        echo "✗ Missing BMAD protocol references"
        return 1
    fi
    
    # Check for phase references
    local phases=("Discovery" "Planning" "Implementation" "Validation")
    for phase in "${phases[@]}"; do
        if ! grep -q "$phase" "$file"; then
            echo "✗ Missing phase reference: $phase"
            return 1
        fi
    done
    
    echo "✓ BMAD compliance check passed"
}
```

#### Template 4: GitHub Copilot Compatibility
```bash
# Purpose: Check GitHub Copilot compatibility
# Usage: check_copilot_compatibility <file>
check_copilot_compatibility() {
    local file="$1"
    
    # Check file format
    if [[ "$file" != *.md ]]; then
        echo "✗ File must be markdown format"
        return 1
    fi
    
    # Check for required sections
    local required_sections=("## Overview" "## Usage" "## Examples")
    for section in "${required_sections[@]}"; do
        if ! grep -q "$section" "$file"; then
            echo "✗ Missing required section: $section"
            return 1
        fi
    done
    
    echo "✓ GitHub Copilot compatibility check passed"
}
```

### Parameterization

**Template Parameters:**
- `filename` - Target file path
- `content_type` - Type of content to generate
- `requirements` - Compliance requirements
- `validation_rules` - Validation criteria

**Usage Examples:**
```bash
# Create markdown file
create_file "docs/example.md" "markdown"

# Validate content
validate_content "output/AGENTS.MD" "requirements.json"

# Check BMAD compliance
check_bmad_compliance "output/AGENTS.MD"

# Check GitHub Copilot compatibility
check_copilot_compatibility "output/.github/copilot-instructions.md"
```

---

## Examples

### Basic Examples

#### Example 1: Simple File Generation
```bash
# Generate a basic AGENTS.MD file
cat > output/AGENTS.MD << 'EOF'
# AGENTS.MD

**Purpose:** Basic agent instructions
**Created:** 2026-01-24

## Content

This is a basic example of AGENTS.MD content.
EOF

# Validate the generated file
validate_content "output/AGENTS.MD" "requirements.json"
```

#### Example 2: Multi-layer Content
```bash
# Generate content for multiple layers
generate_layer_content() {
    local layer="$1"
    local content="$2"
    
    echo "## $layer" >> output/AGENTS.MD
    echo "" >> output/AGENTS.MD
    echo "$content" >> output/AGENTS.MD
    echo "" >> output/AGENTS.MD
}

# Generate each layer
generate_layer_content "UX Layer" "User experience content..."
generate_layer_content "BMAD Protocol" "BMAD protocol content..."
generate_layer_content "Phase Workflows" "Phase workflow content..."
```

### Advanced Scenarios

#### Example 3: Dynamic Content Generation
```bash
# Generate content based on requirements
generate_dynamic_content() {
    local requirements_file="$1"
    
    # Load requirements
    local requirements=$(cat "$requirements_file")
    
    # Generate content for each requirement
    echo "## Dynamic Content" > output/AGENTS.MD
    
    for req in $requirements; do
        echo "### Requirement: $req" >> output/AGENTS.MD
        echo "Content for requirement $req" >> output/AGENTS.MD
        echo "" >> output/AGENTS.MD
    done
}

# Generate dynamic content
generate_dynamic_content "output/requirements_metadata.json"
```

#### Example 4: Conditional Content
```bash
# Generate content based on conditions
generate_conditional_content() {
    local condition="$1"
    local content="$2"
    
    if [ "$condition" = "true" ]; then
        echo "## Conditional Content" >> output/AGENTS.MD
        echo "$content" >> output/AGENTS.MD
    else
        echo "## Alternative Content" >> output/AGENTS.MD
        echo "Alternative content here" >> output/AGENTS.MD
    fi
}

# Generate conditional content
generate_conditional_content "true" "This is the main content"
```

### Edge Cases

#### Example 5: Error Handling
```bash
# Handle errors gracefully
handle_errors() {
    local file="$1"
    
    if [ ! -f "$file" ]; then
        echo "Error: File not found: $file" >&2
        return 1
    fi
    
    if [ ! -r "$file" ]; then
        echo "Error: Cannot read file: $file" >&2
        return 1
    fi
    
    echo "File is accessible: $file"
}

# Handle errors
handle_errors "output/AGENTS.MD"
```

#### Example 6: Large Content Handling
```bash
# Handle large content efficiently
generate_large_content() {
    local output_file="$1"
    local content_size="$2"
    
    # Check available disk space
    local available_space=$(df . | tail -1 | awk '{print $4}')
    local required_space=$((content_size * 2))  # Double for safety
    
    if [ "$available_space" -lt "$required_space" ]; then
        echo "Error: Insufficient disk space"
        return 1
    fi
    
    # Generate content in chunks
    for i in {1..10}; do
        echo "Chunk $i of large content" >> "$output_file"
    done
    
    echo "Large content generated successfully"
}

# Generate large content
generate_large_content "output/large_content.md" 1000000
```

---

## Reasoning Frameworks

### XML Frameworks

#### Framework 1: Content Structure
```xml
<content_structure>
  <layer id="1" name="UX Layer">
    <components>
      <component id="welcome_flow">Welcome and navigation</component>
      <component id="feedback_system">Quality gates and validation</component>
    </components>
  </layer>
  
  <layer id="2" name="BMAD Protocol">
    <components>
      <component id="phase_management">Phase-based workflow</component>
      <component id="compliance_check">Requirement validation</component>
    </components>
  </layer>
  
  <layer id="3" name="Phase Workflows">
    <components>
      <component id="discovery">Requirement analysis</component>
      <component id="planning">Architecture design</component>
      <component id="implementation">Content generation</component>
      <component id="validation">Compliance verification</component>
    </components>
  </layer>
</content_structure>
```

#### Framework 2: Decision Tree
```xml
<decision_tree>
  <decision id="d1" question="Is this a new AGENTS.MD generation?">
    <option value="yes" next="d2">Proceed to initialization</option>
    <option value="no" next="d3">Load existing content</option>
  </decision>
  
  <decision id="d2" question="Are all requirements loaded?">
    <option value="yes" next="d4">Continue to foundation setup</option>
    <option value="no" next="d5">Load missing requirements</option>
  </decision>
  
  <decision id="d3" question="Is content preservation required?">
    <option value="yes" next="d6">Merge with existing content</option>
    <option value="no" next="d7">Replace with new content</option>
  </decision>
</decision_tree>
```

### Pseudo-code Frameworks

#### Framework 3: Content Generation Algorithm
```
ALGORITHM GenerateAGENTSMD
INPUT: requirements_metadata, architecture_structure
OUTPUT: AGENTS.MD, .github/copilot-instructions.md

BEGIN
    // Initialize
    InitializeOutputFiles()
    LoadRequirements()
    
    // Phase 1: Discovery
    AnalyzeRequirements()
    DefineScope()
    
    // Phase 2: Planning
    DesignArchitecture()
    MapRequirementsToLayers()
    
    // Phase 3: Implementation
    FOR each layer IN architecture_structure DO
        GenerateLayerContent(layer)
        ValidateLayerContent(layer)
    END FOR
    
    // Phase 4: Validation
    ValidateCompliance()
    CheckFileSizeLimits()
    GenerateFinalOutput()
    
    RETURN AGENTS.MD, copilot_instructions.md
END
```

#### Framework 4: Validation Algorithm
```
ALGORITHM ValidateContent
INPUT: file_path, requirements
OUTPUT: validation_result

BEGIN
    // Initialize validation
    validation_result = {}
    validation_result.status = "pending"
    validation_result.errors = []
    
    // Check file existence
    IF NOT FileExists(file_path) THEN
        validation_result.errors.append("File not found")
        validation_result.status = "failed"
        RETURN validation_result
    END IF
    
    // Check file size
    file_size = GetFileSize(file_path)
    IF file_size > 102400 THEN  // 100KB limit
        validation_result.errors.append("File size exceeds limit")
        validation_result.status = "failed"
        RETURN validation_result
    END IF
    
    // Check content structure
    content = ReadFile(file_path)
    IF NOT HasRequiredSections(content) THEN
        validation_result.errors.append("Missing required sections")
        validation_result.status = "failed"
        RETURN validation_result
    END IF
    
    // Check BMAD compliance
    IF NOT CheckBMADCompliance(content, requirements) THEN
        validation_result.errors.append("BMAD compliance failed")
        validation_result.status = "failed"
        RETURN validation_result
    END IF
    
    // Check GitHub Copilot compatibility
    IF NOT CheckCopilotCompatibility(content) THEN
        validation_result.errors.append("GitHub Copilot compatibility failed")
        validation_result.status = "failed"
        RETURN validation_result
    END IF
    
    // All checks passed
    validation_result.status = "passed"
    RETURN validation_result
END
```

### Decision Trees

#### Decision Tree 1: Content Strategy
```
START
├── Is this a new generation?
│   ├── YES → Initialize from scratch
│   └── NO → Load existing content
├── Are all requirements available?
│   ├── YES → Proceed with generation
│   └── NO → Load missing requirements
├── Is content preservation required?
│   ├── YES → Merge strategies
│   └── NO → Replace content
└── Is file size within limits?
    ├── YES → Final validation
    └── NO → Optimize content
```

#### Decision Tree 2: Error Handling
```
ERROR OCCURRED
├── File not found?
│   ├── YES → Check path and permissions
│   └── NO → Continue
├── Permission denied?
│   ├── YES → Request elevated permissions
│   └── NO → Continue
├── Content validation failed?
│   ├── YES → Review and fix content
│   └── NO → Continue
└── Compliance check failed?
    ├── YES → Review requirements
    └── NO → Continue
```

---

## Session Monitoring

### Progress Tracking

#### Progress Monitor
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

#### State Management

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

### Continuation

#### Resume Workflow
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

#### Checkpoint System
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
```

---

## Best Practices

### Coding Standards

#### File Organization
```
output/
├── AGENTS.MD                    # Main AGENTS.MD file
├── .github/
│   └── copilot-instructions.md  # GitHub Copilot specific instructions
├── requirements_metadata.json   # Requirements metadata
├── architecture_structure.json  # Architecture definition
├── kr_requirements.json         # KR requirements
├── compliance_matrix.json       # Compliance matrix
├── architecture_validation.json # Validation results
├── progress.json               # Progress tracking
├── state.json                  # Workflow state
└── checkpoints/                # Step checkpoints
    ├── step-01-initialization.json
    ├── step-02-foundation-setup.json
    └── step-03-content-generation.json
```

#### Naming Conventions
- **Files:** Use kebab-case for file names
- **Variables:** Use snake_case for shell variables
- **Functions:** Use snake_case for function names
- **Constants:** Use UPPER_SNAKE_CASE for constants

#### Code Comments
```bash
# Always comment complex logic
# Example: Map FR requirements to appropriate layers
case "$fr_req" in
    "FR-001"|"FR-002"|"FR-003")
        layer="layer-2" # BMAD Protocol
        ;;
    "FR-004"|"FR-005"|"FR-006")
        layer="layer-3" # Phase Workflows
        ;;
    *)
        layer="layer-1" # UX Layer (default)
        ;;
esac
```

### Performance Guidelines

#### Memory Management
```bash
# Use temporary files for large operations
TEMP_DIR="/tmp/agents-md-generator"
mkdir -p "$TEMP_DIR"

# Clean up temporary files
cleanup() {
    rm -rf "$TEMP_DIR"
    echo "Temporary files cleaned up"
}

# Register cleanup on exit
trap cleanup EXIT
```

#### Processing Optimization
```bash
# Process files in batches for better performance
process_batch() {
    local files=("$@")
    local batch_size=10
    
    for ((i=0; i<${#files[@]}; i+=batch_size)); do
        local batch=("${files[@]:i:batch_size}")
        
        # Process batch
        for file in "${batch[@]}"; do
            process_file "$file"
        done
        
        echo "Processed batch: $i to $((i + batch_size - 1))"
    done
}
```

#### Error Handling
```bash
# Always handle errors gracefully
set -e  # Exit on error
set -u  # Exit on undefined variables
set -o pipefail  # Exit on pipe failures

# Custom error handler
error_handler() {
    local exit_code=$?
    echo "Error occurred with exit code: $exit_code"
    echo "Line number: $1"
    exit $exit_code
}

trap 'error_handler $LINENO' ERR
```

### Security Practices

#### Input Validation
```bash
# Always validate inputs
validate_input() {
    local input="$1"
    local pattern="$2"
    
    if [[ ! "$input" =~ $pattern ]]; then
        echo "Invalid input: $input"
        return 1
    fi
    
    return 0
}

# Usage
if validate_input "$filename" "^[a-zA-Z0-9._/-]+$"; then
    echo "Input is valid"
else
    echo "Input validation failed"
    exit 1
fi
```

#### File Permissions
```bash
# Set appropriate file permissions
set_file_permissions() {
    local file="$1"
    local permissions="$2"
    
    chmod "$permissions" "$file"
    echo "Set permissions $permissions for $file"
}

# Usage
set_file_permissions "output/AGENTS.MD" "644"
set_file_permissions "output/.github/copilot-instructions.md" "644"
```

#### Sensitive Data Handling
```bash
# Never log sensitive information
log_info() {
    local message="$1"
    echo "$(date): $message"
}

log_error() {
    local message="$1"
    echo "$(date): ERROR - $message" >&2
}

# Usage
log_info "Starting content generation"
log_error "Failed to generate content"
```

## Next Steps

Proceed to **Step 4: Assembly & Validation** where we will:
- Merge and optimize generated content
- Validate file size limits and modularization
- Perform final validation and export
- Generate compliance report

## Validation

### Success Criteria

- [ ] All 8 layers content generated
- [ ] AGENTS.MD file created with proper structure
- [ ] .github/copilot-instructions.md created
- [ ] Task templates implemented
- [ ] Examples and reasoning frameworks created
- [ ] Content validation passed

### Quality Gates

- Content follows BMAD protocol
- File size within limits
- GitHub Copilot compatibility
- All task templates functional
- Examples are realistic and useful

## Troubleshooting

### Common Issues

1. **Content generation failed**
   - Check requirements loading
   - Verify architecture structure
   - Review template implementation

2. **File size exceeded**
   - Optimize content structure
   - Remove unnecessary content
   - Use modularization

3. **Validation errors**
   - Review compliance requirements
   - Check content structure
   - Validate file format

### Support

For issues and support:
- Check `docs/KNOWN_ISSUES.md`
- Review `docs/TROUBLESHOOTING.md`
- Contact BMAD support team