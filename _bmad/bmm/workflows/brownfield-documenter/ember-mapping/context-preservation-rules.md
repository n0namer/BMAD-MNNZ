# Context Preservation Rules
# Rules for maintaining context across BMM workflow steps in EMBER Orchestration

## Overview

Context preservation ensures that EMBER responses maintain consistency and relevance across multiple workflow steps by tracking and reusing context variables, decisions, and constraints.

## Context Types

### 1. Project Context
**Variables to preserve:**
- `project_domain` - Core business domain
- `target_market` - Primary market segment
- `geography` - Target geography/regions
- `industry` - Industry classification
- `scale_requirements` - Expected scale (users, data, transactions)
- `time_constraints` - Timeline and deadline constraints

**Propagation Rules:**
- Set in analysis stage, reused in planning/solutioning
- Updated when new information becomes available
- Validated for consistency across stages

### 2. User Context
**Variables to preserve:**
- `user_personas` - Defined user personas and characteristics
- `user_journeys` - Primary user journey maps
- `pain_points` - Identified user problems and needs
- `success_scenarios` - Key success scenarios
- `usability_goals` - UX and usability requirements

**Propagation Rules:**
- Defined in analysis stage, referenced in design stages
- Updated based on validation feedback
- Maintained across UX design and validation steps

### 3. Technical Context
**Variables to preserve:**
- `tech_stack` - Selected technology choices
- `architecture_decisions` - Key architectural decisions
- `integration_points` - External system integrations
- `security_requirements` - Security and compliance needs
- `performance_requirements` - Performance and scalability needs

**Propagation Rules:**
- Evolve from requirements to implementation
- Updated during architecture design
- Referenced in implementation planning

### 4. Business Context
**Variables to preserve:**
- `business_goals` - Primary business objectives
- `success_metrics` - Defined KPIs and success measures
- `market_positioning` - Competitive positioning strategy
- `revenue_model` - Business model and monetization
- `risk_assessment` - Identified business risks

**Propagation Rules:**
- Set early, influence all downstream decisions
- Updated based on market analysis
- Referenced in prioritization and planning

## Context Propagation Rules

### Stage-to-Stage Propagation

#### Analysis → Planning
```
Analysis Outputs → Planning Inputs
├── User research → UX design requirements
├── Market analysis → Feature prioritization
├── Technical constraints → Technical architecture
└── Business goals → Product strategy
```

#### Planning → Solutioning
```
Planning Outputs → Solutioning Inputs
├── UX requirements → Architecture design
├── Feature lists → Epic breakdown
├── Technical specs → Implementation planning
└── Acceptance criteria → Validation planning
```

### Within-Stage Propagation

#### Research Workflow Context Flow
```
Domain Analysis → Market Analysis → Technical Analysis
     ↓              ↓              ↓
Competitors ──── Positioning ─── Tech Requirements
     ↓              ↓              ↓
Regulatory ─── Segmentation ─── Constraints
```

#### Product Brief Context Flow
```
Vision → Users → Metrics → Scope
   ↓       ↓       ↓       ↓
Mission ─ Personas ─ KPIs ─ MVP Features
   ↓       ↓       ↓       ↓
Goals ── Journeys ─ North Star ─ Exclusions
```

## Context Validation Rules

### Consistency Checks
1. **Domain Consistency** - All responses reference same project domain
2. **User Alignment** - Technical decisions align with user needs
3. **Business Logic** - Technical choices support business goals
4. **Architecture Coherence** - Components work together effectively

### Conflict Resolution
1. **New Information Priority** - Recent context updates override old assumptions
2. **User Override** - Manual user inputs take precedence in Assisted mode
3. **Validation Feedback** - Testing results can update context assumptions
4. **EMBED Confidence** - Higher confidence responses override lower confidence

## Context Storage and Retrieval

### Storage Format
```yaml
workflow_context:
  session_id: "session_2026_001"
  project_id: "project_xyz"
  mode: "assisted"  # assisted | auto_pilot | manual

  variables:
    project_domain: "Healthcare data analytics"
    target_market: "SMB healthcare providers"
    geography: ["US", "EU"]
    user_personas: ["Dr. Smith - Primary Care Physician", "Nurse Johnson - Clinic Manager"]

  decisions:
    tech_stack: "React + Node.js + PostgreSQL"
    architecture: "Microservices with API Gateway"
    security: "HIPAA compliant with encryption"

  constraints:
    timeline: "6 months to MVP"
    budget: "$500K development budget"
    compliance: "HIPAA, GDPR compliance required"

  history:
    - timestamp: "2026-01-19T14:30:00Z"
      step: "research/domain-analysis"
      action: "market_size_defined"
      value: "TAM: $50B, SAM: $5B"
```

### Retrieval Rules
1. **Current Step Context** - Load context relevant to current workflow step
2. **Historical Context** - Include previous decisions that impact current step
3. **Cross-Reference Context** - Include related context from parallel workflow branches
4. **Validation Context** - Include constraints and requirements for validation

## Context Update Triggers

### Automatic Updates
- **Step Completion** - New decisions added to context
- **EMBED Response** - High-confidence responses update context variables
- **User Approval** - User-approved changes update context
- **Validation Results** - Testing feedback updates assumptions

### Manual Updates
- **User Override** - User can manually update context variables
- **Requirement Changes** - Business requirement changes update context
- **Scope Changes** - Project scope changes update boundaries
- **Technical Changes** - Technology or architecture changes update technical context

## Context Lifecycle

### Creation
- **Initialization** - Created when workflow starts
- **Seed Data** - Initial project information loaded
- **Mode Configuration** - Context rules set based on selected mode

### Maintenance
- **Incremental Updates** - Context grows with each completed step
- **Version Control** - Context versions maintained for rollback
- **Conflict Resolution** - Inconsistencies resolved automatically or with user input

### Cleanup
- **Completion** - Final context saved with workflow results
- **Archival** - Context stored for future reference
- **Export** - Context can be exported for use in other workflows

## Mode-Specific Context Handling

### Assisted Mode
- **User Review Required** - Context updates require user approval
- **Editable Context** - Users can modify context variables
- **Feedback Loop** - User corrections update context rules

### Auto-Pilot Mode
- **Automatic Updates** - Context updates without user interaction
- **Confidence Filtering** - Only high-confidence updates accepted
- **Fallback Handling** - Low-confidence items flagged for later review

### Manual Mode
- **User-Driven Context** - All context updates manual
- **Full Control** - Users control all context variables
- **Validation Support** - EMBER provides validation suggestions
