---
name: 'step-03-generate'
description: 'Generate final documentation package from scan results'

nextStepFile: './step-04-finalize.md'
---

# Step 3: YOLO Documentation Generation

## STEP GOAL:

Generate final BMAD documentation package from scan results in YOLO autonomous mode.

## YOLO MODE: Auto-Generate Documentation

**CRITICAL:** Auto-generate complete documentation package without user interaction.

## EXECUTION SEQUENCE

### 1. Process Scan Results

Read all generated files from document-project workflow:
- index.md (if exists)
- architecture.md
- api-contracts.md
- data-models.md
- development-guide.md
- And other generated files

### 2. Validate Documentation Completeness

Check that all required sections are present:
- Project overview
- Architecture documentation
- API contracts (if applicable)
- Data models (if applicable)
- Development setup
- Source tree analysis

### 3. Generate Missing Sections (Auto)

If any sections missing, auto-generate using scan data:
- Use templates from document-project
- Fill with collected project information
- Auto-resolve any missing data points

### 4. EMBER Fallback Check

If generation encounters complex decisions:
- Auto-activate EMBER workflow
- Provide context from current generation state
- Use EMBER output to resolve complexity
- Continue generation with EMBER insights

### 5. Compile Final Package

Create complete documentation package:
- index.md as master entry point
- All supporting documentation files
- Cross-references between documents
- Consistent formatting and structure

### 6. Auto-Proceed to Finalization

**YOLO MODE:** Immediately proceed to finalization without user confirmation.

---

## SUCCESS METRICS

- Complete documentation package generated
- EMBER fallback activated when needed
- All required sections present
- Auto-proceeded to finalization
