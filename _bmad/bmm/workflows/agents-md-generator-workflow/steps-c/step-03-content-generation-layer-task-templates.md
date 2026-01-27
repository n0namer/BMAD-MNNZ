---
name: 'step-03-content-generation-layer-task-templates'
description: 'Task Templates — Common Tasks и Specialized Templates для типовых операций'
layer: 'task-templates'
menu:
  next: step-03-content-generation-layer-examples.md
  back: step-03-content-generation-layer-phase-workflows.md
handler: C
---

# Step 3: Content Generation — Task Templates

## Common Tasks

### Template 1: File Creation
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

### Template 2: Content Validation
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

## Specialized Templates

### Template 3: BMAD Compliance Check
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

### Template 4: GitHub Copilot Compatibility
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

## Parameterization

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