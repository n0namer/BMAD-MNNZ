# Task Templates Reference

## Common Tasks

### Template 1: File Creation
```bash
create_file() {
    local filename="$1"
    local content_type="$2"
    
    if [ -z "$filename" ] || [ -z "$content_type" ]; then
        echo "Usage: create_file <filename> <content_type>"
        return 1
    fi
    
    mkdir -p "$(dirname "$filename")"
    
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
validate_content() {
    local file="$1"
    local requirements="$2"
    
    if [ ! -f "$file" ]; then
        echo "✗ File not found: $file"
        return 1
    fi
    
    local size=$(wc -c < "$file")
    if [ "$size" -gt 102400 ]; then
        echo "✗ File size exceeds limit: ${size} bytes"
        return 1
    fi
    
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
check_bmad_compliance() {
    local file="$1"
    
    if ! grep -q "BMAD" "$file"; then
        echo "✗ Missing BMAD protocol references"
        return 1
    fi
    
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
check_copilot_compatibility() {
    local file="$1"
    
    if [[ "$file" != *.md ]]; then
        echo "✗ File must be markdown format"
        return 1
    fi
    
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
create_file "docs/example.md" "markdown"
validate_content "output/AGENTS.MD" "requirements.json"
check_bmad_compliance "output/AGENTS.MD"
check_copilot_compatibility "output/.github/copilot-instructions.md"