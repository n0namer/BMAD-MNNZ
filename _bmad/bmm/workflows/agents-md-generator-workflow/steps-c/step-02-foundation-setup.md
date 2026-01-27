---
name: 'step-02-foundation-setup'
description: 'Step 2: Foundation Setup — Create architecture structure, load requirements metadata, generate compliance matrix'
layer: 'foundation-setup'
menu:
  next: step-03-content-generation-intro.md
  back: step-01-initialization.md
handler: A
---

# Step 2: Foundation Setup

**Purpose:** Create the architecture structure, load requirements metadata, generate compliance matrix, and prepare for content generation

## Overview

This step establishes the foundation for content generation by creating the 8-layer architecture structure, loading all requirements metadata, and generating the compliance matrix that will guide the entire workflow.

## Prerequisites

- Step 1: Initialization completed
- All requirements loaded and validated
- Environment setup complete
- Workflow state initialized

## Input Requirements

### Required Inputs

1. **Requirements Metadata** - `output/requirements_metadata.json`
2. **BMAD Requirements** - Loaded from step 1
3. **KR Requirements** - Loaded from step 1
4. **User Requirements** - Loaded from step 1
5. **PRD Content** - Loaded from step 1
6. **North Star Description** - Loaded from step 1

### Optional Inputs

1. **Custom Requirements** - Additional requirement specifications
2. **Architecture Preferences** - Custom architecture configurations
3. **Compliance Rules** - Additional compliance requirements

## Process

### 1. Architecture Structure Creation

```bash
# Create 8-layer architecture structure
create_architecture_structure() {
    echo "Creating 8-layer architecture structure..."
    
    local architecture_file="$OUTPUT_DIR/architecture_structure.json"
    
    cat > "$architecture_file" << 'EOF'
{
  "version": "6.0.0-alpha.23",
  "created": "$(date -Iseconds)",
  "architecture": {
    "layers": [
      {
        "id": "layer-1",
        "name": "UX Layer",
        "description": "User experience and navigation layer",
        "components": [
          "welcome_flow",
          "navigation_system",
          "feedback_system"
        ],
        "dependencies": []
      },
      {
        "id": "layer-2", 
        "name": "BMAD Protocol",
        "description": "BMAD protocol and phase management layer",
        "components": [
          "phase_management",
          "input_output_specification",
          "compliance_check"
        ],
        "dependencies": ["layer-1"]
      },
      {
        "id": "layer-3",
        "name": "Phase Workflows",
        "description": "Detailed workflow processes for each phase",
        "components": [
          "discovery_workflow",
          "planning_workflow", 
          "implementation_workflow",
          "validation_workflow"
        ],
        "dependencies": ["layer-2"]
      },
      {
        "id": "layer-4",
        "name": "Task Templates",
        "description": "Reusable task definitions and templates",
        "components": [
          "common_tasks",
          "specialized_templates",
          "parameterization"
        ],
        "dependencies": ["layer-3"]
      },
      {
        "id": "layer-5",
        "name": "Examples",
        "description": "Practical usage examples and scenarios",
        "components": [
          "basic_examples",
          "advanced_scenarios",
          "edge_cases"
        ],
        "dependencies": ["layer-4"]
      },
      {
        "id": "layer-6",
        "name": "Reasoning Frameworks",
        "description": "Decision trees and reasoning algorithms",
        "components": [
          "xml_frameworks",
          "pseudo_code_frameworks",
          "decision_trees"
        ],
        "dependencies": ["layer-5"]
      },
      {
        "id": "layer-7",
        "name": "Session Monitoring",
        "description": "Progress tracking and state management",
        "components": [
          "progress_tracking",
          "state_management",
          "continuation"
        ],
        "dependencies": ["layer-6"]
      },
      {
        "id": "layer-8",
        "name": "Best Practices",
        "description": "Coding standards and best practices",
        "components": [
          "coding_standards",
          "performance_guidelines",
          "security_practices"
        ],
        "dependencies": ["layer-7"]
      }
    ],
    "relationships": {
      "layer-1": ["layer-2"],
      "layer-2": ["layer-3"],
      "layer-3": ["layer-4"],
      "layer-4": ["layer-5"],
      "layer-5": ["layer-6"],
      "layer-6": ["layer-7"],
      "layer-7": ["layer-8"]
    }
  }
}
EOF
    
    echo "✓ Architecture structure created: $architecture_file"
    return 0
}
```

### 2. Requirements Metadata Loading

```bash
# Load and process requirements metadata
load_requirements_metadata() {
    echo "Loading requirements metadata..."
    
    local metadata_file="$OUTPUT_DIR/requirements_metadata.json"
    
    # Extract metadata from loaded requirements
    local bmad_count=$(echo "$BMAD_REQUIREMENTS" | grep -c "^#" || echo "0")
    local kr_count=$(echo "$KR_REQUIREMENTS" | grep -c "^#" || echo "0")
    local user_count=$(echo "$USER_REQUIREMENTS" | grep -c "^#" || echo "0")
    
    cat > "$metadata_file" << EOF
{
  "version": "6.0.0-alpha.23",
  "created": "$(date -Iseconds)",
  "requirements": {
    "bmad": {
      "count": $bmad_count,
      "loaded": ${BMAD_REQUIREMENTS:+true},
      "content_length": ${#BMAD_REQUIREMENTS}
    },
    "kr": {
      "count": $kr_count,
      "loaded": ${KR_REQUIREMENTS:+true},
      "content_length": ${#KR_REQUIREMENTS}
    },
    "user": {
      "count": $user_count,
      "loaded": ${USER_REQUIREMENTS:+true},
      "content_length": ${#USER_REQUIREMENTS}
    },
    "prd": {
      "loaded": ${PRD_CONTENT:+true},
      "content_length": ${#PRD_CONTENT}
    },
    "north_star": {
      "loaded": ${NORTH_STAR:+true},
      "content_length": ${#NORTH_STAR}
    }
  },
  "summary": {
    "total_requirements": $((bmad_count + kr_count + user_count)),
    "all_loaded": ${BMAD_REQUIREMENTS:+${KR_REQUIREMENTS:+${USER_REQUIREMENTS:+true}}},
    "workflow_ready": true
  }
}
EOF
    
    echo "✓ Requirements metadata loaded: $metadata_file"
    return 0
}
```

### 3. Compliance Matrix Generation

```bash
# Generate compliance matrix
generate_compliance_matrix() {
    echo "Generating compliance matrix..."
    
    local matrix_file="$OUTPUT_DIR/compliance_matrix.json"
    
    cat > "$matrix_file" << 'EOF'
{
  "version": "6.0.0-alpha.23",
  "created": "$(date -Iseconds)",
  "compliance_matrix": {
    "kr_requirements": {
      "KR-1": {
        "description": "Binary identical files",
        "status": "pending",
        "layer_mapping": ["layer-2", "layer-8"],
        "validation_rules": [
          "file_content_identical",
          "no_modification_allowed"
        ]
      },
      "KR-2": {
        "description": "BMAD phase understanding",
        "status": "pending", 
        "layer_mapping": ["layer-2", "layer-3"],
        "validation_rules": [
          "phase_references_present",
          "phase_logic_correct"
        ]
      },
      "KR-3": {
        "description": "GitHub Copilot compatibility",
        "status": "pending",
        "layer_mapping": ["layer-1", "layer-4"],
        "validation_rules": [
          "markdown_format",
          "required_sections_present",
          "agent_friendly_structure"
        ]
      },
      "KR-4": {
        "description": "Content preservation",
        "status": "pending",
        "layer_mapping": ["layer-7"],
        "validation_rules": [
          "content_integrity_maintained",
          "no_data_loss"
        ]
      },
      "KR-5": {
        "description": "Realistic examples",
        "status": "pending",
        "layer_mapping": ["layer-5"],
        "validation_rules": [
          "examples_functional",
          "scenarios_realistic",
          "edge_cases_covered"
        ]
      },
      "KR-6": {
        "description": "Task templates",
        "status": "pending",
        "layer_mapping": ["layer-4"],
        "validation_rules": [
          "templates_reusable",
          "parameters_documented",
          "examples_provided"
        ]
      },
      "KR-7": {
        "description": "Steering guide",
        "status": "pending",
        "layer_mapping": ["layer-1", "layer-3"],
        "validation_rules": [
          "navigation_clear",
          "instructions_complete",
          "workflow_documented"
        ]
      },
      "KR-8": {
        "description": "Agent autonomy",
        "status": "pending",
        "layer_mapping": ["layer-6"],
        "validation_rules": [
          "decision_trees_present",
          "autonomous_logic_implemented",
          "fallback_strategies_defined"
        ]
      },
      "KR-9": {
        "description": "XML + pseudo-code",
        "status": "pending",
        "layer_mapping": ["layer-6"],
        "validation_rules": [
          "xml_frameworks_present",
          "pseudo_code_implemented",
          "algorithms_documented"
        ]
      },
      "KR-10": {
        "description": "Advanced features",
        "status": "pending",
        "layer_mapping": ["layer-7", "layer-8"],
        "validation_rules": [
          "monitoring_implemented",
          "best_practices_defined",
          "performance_optimized"
        ]
      }
    },
    "bmad_requirements": {
      "phase_management": {
        "status": "pending",
        "validation_rules": [
          "all_phases_defined",
          "phase_transitions_clear",
          "phase_logic_correct"
        ]
      },
      "input_output_specification": {
        "status": "pending",
        "validation_rules": [
          "inputs_documented",
          "outputs_specified",
          "format_compliant"
        ]
      },
      "compliance_check": {
        "status": "pending",
        "validation_rules": [
          "compliance_framework_defined",
          "validation_rules_implemented",
          "error_handling_present"
        ]
      }
    }
  },
  "summary": {
    "total_kr_requirements": 10,
    "total_bmad_requirements": 3,
    "all_mapped": true,
    "validation_ready": true
  }
}
EOF
    
    echo "✓ Compliance matrix generated: $matrix_file"
    return 0
}
```

### 4. Architecture Validation

```bash
# Validate architecture structure
validate_architecture() {
    echo "Validating architecture structure..."
    
    local architecture_file="$OUTPUT_DIR/architecture_structure.json"
    local validation_errors=0
    
    # Check if architecture file exists
    if [ ! -f "$architecture_file" ]; then
        echo "ERROR: Architecture structure file not found"
        ((validation_errors++))
    fi
    
    # Validate JSON structure
    if ! jq empty "$architecture_file" 2>/dev/null; then
        echo "ERROR: Invalid JSON in architecture structure"
        ((validation_errors++))
    fi
    
    # Check for all 8 layers
    local layer_count=$(jq '.architecture.layers | length' "$architecture_file" 2>/dev/null || echo "0")
    if [ "$layer_count" -ne 8 ]; then
        echo "ERROR: Expected 8 layers, found $layer_count"
        ((validation_errors++))
    fi
    
    # Check layer dependencies
    local dependency_errors=0
    for i in {1..8}; do
        local layer_id="layer-$i"
        local dependencies=$(jq -r ".architecture.layers[$((i-1))].dependencies[]" "$architecture_file" 2>/dev/null || echo "")
        
        for dep in $dependencies; do
            if [ "$dep" = "null" ] || [ -z "$dep" ]; then
                continue
            fi
            
            # Check if dependency layer exists
            local dep_exists=$(jq -r ".architecture.layers[] | select(.id == \"$dep\") | .id" "$architecture_file" 2>/dev/null || echo "")
            if [ -z "$dep_exists" ]; then
                echo "ERROR: Invalid dependency $dep for layer $layer_id"
                ((dependency_errors++))
            fi
        done
    done    
    if [ $validation_errors -eq 0 ] && [ $dependency_errors -eq 0 ]; then
        echo "✓ Architecture validation passed"
        return 0
    else
        echo "✗ Architecture validation failed with $((validation_errors + dependency_errors)) errors"
        return 1
    fi
}
```

## Output Files

### Architecture Structure
- **File:** `output/architecture_structure.json`
- **Content:** 8-layer architecture definition
- **Format:** JSON

### Requirements Metadata
- **File:** `output/requirements_metadata.json`
- **Content:** Requirements loading status and metadata
- **Format:** JSON

### Compliance Matrix
- **File:** `output/compliance_matrix.json`
- **Content:** KR and BMAD compliance mapping
- **Format:** JSON

## Quality Gates

- [ ] Architecture structure created successfully
- [ ] Requirements metadata loaded completely
- [ ] Compliance matrix generated with all mappings
- [ ] Architecture validation passed
- [ ] All dependencies properly defined

## Troubleshooting

### Common Issues

1. **Architecture validation failed**
   - Check JSON syntax in architecture file
   - Verify all 8 layers are defined
   - Validate dependency relationships

2. **Requirements metadata incomplete**
   - Verify all requirements are loaded
   - Check requirement file formats
   - Validate content extraction

3. **Compliance matrix missing mappings**
   - Review KR requirements
   - Check BMAD protocol requirements
   - Validate layer-to-requirement mapping

4. **JSON parsing errors**
   - Check JSON syntax
   - Verify jq tool availability
   - Validate file encoding

### Support

For issues and support:
- Check `docs/KNOWN_ISSUES.md`
- Review `docs/TROUBLESHOOTING.md`
- Contact BMAD support team