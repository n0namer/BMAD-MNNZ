---
name: 'step-03-content-generation-layer-reasoning-frameworks'
description: 'Reasoning Frameworks — XML Frameworks, Pseudo-code, Decision Trees'
layer: 'reasoning-frameworks'
menu:
  next: step-03-content-generation-layer-session-monitoring.md
  back: step-03-content-generation-layer-examples.md
handler: C
---

# Step 3: Content Generation — Reasoning Frameworks

## XML Frameworks

### Framework 1: Content Structure
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

### Framework 2: Decision Tree
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

## Pseudo-code Frameworks

### Framework 3: Content Generation Algorithm
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

### Framework 4: Validation Algorithm
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

## Decision Trees

### Decision Tree 1: Content Strategy
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

### Decision Tree 2: Error Handling
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