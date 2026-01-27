# Examples Reference

## Basic Examples

### Example 1: Simple File Generation
```bash
cat > output/AGENTS.MD << 'EOF'
# AGENTS.MD

**Purpose:** Basic agent instructions
**Created:** 2026-01-24

## Content

This is a basic example of AGENTS.MD content.
EOF

validate_content "output/AGENTS.MD" "requirements.json"
```

### Example 2: Multi-layer Content
```bash
generate_layer_content() {
    local layer="$1"
    local content="$2"
    
    echo "## $layer" >> output/AGENTS.MD
    echo "" >> output/AGENTS.MD
    echo "$content" >> output/AGENTS.MD
    echo "" >> output/AGENTS.MD
}

generate_layer_content "UX Layer" "User experience content..."
generate_layer_content "BMAD Protocol" "BMAD protocol content..."
generate_layer_content "Phase Workflows" "Phase workflow content..."
```

## Advanced Scenarios

### Example 3: Dynamic Content Generation
```bash
generate_dynamic_content() {
    local requirements_file="$1"
    
    local requirements=$(cat "$requirements_file")
    
    echo "## Dynamic Content" > output/AGENTS.MD
    
    for req in $requirements; do
        echo "### Requirement: $req" >> output/AGENTS.MD
        echo "Content for requirement $req" >> output/AGENTS.MD
        echo "" >> output/AGENTS.MD
    done
}

generate_dynamic_content "output/requirements_metadata.json"
```

### Example 4: Conditional Content
```bash
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

generate_conditional_content "true" "This is the main content"
```

## Edge Cases

### Example 5: Error Handling
```bash
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

handle_errors "output/AGENTS.MD"
```

### Example 6: Large Content Handling
```bash
generate_large_content() {
    local output_file="$1"
    local content_size="$2"
    
    local available_space=$(df . | tail -1 | awk '{print $4}')
    local required_space=$((content_size * 2))
    
    if [ "$available_space" -lt "$required_space" ]; then
        echo "Error: Insufficient disk space"
        return 1
    fi
    
    for i in {1..10}; do
        echo "Chunk $i of large content" >> "$output_file"
    done
    
    echo "Large content generated successfully"
}

generate_large_content "output/large_content.md" 1000000