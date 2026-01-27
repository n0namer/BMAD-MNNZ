---
name: 'step-03-content-generation-layer-best-practices'
description: 'Best Practices — Coding Standards, Performance Guidelines, Security Practices'
layer: 'best-practices'
menu:
  next: step-03-content-generation-layer-validation.md
  back: step-03-content-generation-layer-session-monitoring.md
handler: C
---

# Step 3: Content Generation — Best Practices

## Coding Standards

### File Organization
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

### Naming Conventions
- **Files:** Use kebab-case for file names
- **Variables:** Use snake_case for shell variables
- **Functions:** Use snake_case for function names
- **Constants:** Use UPPER_SNAKE_CASE for constants

### Code Comments
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

## Performance Guidelines

### Memory Management
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

### Processing Optimization
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

### Error Handling
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

## Security Practices

### Input Validation
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

### File Permissions
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

### Sensitive Data Handling
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