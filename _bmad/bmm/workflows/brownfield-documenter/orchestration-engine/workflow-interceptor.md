# Workflow Interceptor
# Core component for intercepting questions from BMM workflows and routing to EMBER

## Overview

The Workflow Interceptor is the central orchestration component that monitors BMM workflow execution, detects user questions, and routes them to EMBER for intelligent responses based on the selected interaction mode.

## Architecture

### Core Components

1. **Question Detector** - Identifies questions in workflow execution
2. **Context Extractor** - Gathers relevant context for EMBER prompts
3. **Mode Router** - Routes questions based on interaction mode
4. **Response Injector** - Inserts EMBER responses back into workflows
5. **State Manager** - Maintains workflow execution state

### Integration Points

```
BMM Workflow Execution
        ↓ (question detected)
Workflow Interceptor
        ↓ (context extraction)
EMBED Mapping Engine
        ↓ (prompt generation)
EMBED Workflow
        ↓ (intelligent response)
Response Injector
        ↓ (answer injection)
BMM Workflow Execution (continues)
```

## Question Detection

### Detection Methods

#### 1. Pattern-Based Detection
**Question Patterns:**
- "What is..." questions
- "How should..." questions
- "Define..." questions
- "Choose..." questions
- "Select..." questions

**Code Detection:**
```yaml
question_patterns:
  - pattern: "What is the (.+) for (.+)?"
    type: "definition_request"
  - pattern: "How should (.+) (.+) (.+)?"
    type: "methodology_request"
  - pattern: "Define (.+) (.+)"
    type: "specification_request"
```

#### 2. Step-Based Detection
**Known Question Points:**
```yaml
workflow_questions:
  research/domain-analysis:
    - step: "market_size"
      question: "What is the market size?"
      context: ["product_domain", "geography"]

  create-product-brief/vision:
    - step: "product_vision"
      question: "What is the product vision?"
      context: ["product_idea", "target_market"]
```

#### 3. Dynamic Detection
**Runtime Question Identification:**
- Monitor workflow execution logs
- Detect user input prompts
- Identify decision points requiring answers

### Context Extraction

#### Context Sources
1. **Workflow State** - Current workflow variables and decisions
2. **Step Context** - Information from current workflow step
3. **Historical Context** - Previous decisions and answers
4. **Project Context** - Overall project information and constraints

#### Context Enrichment
```yaml
context_enrichment:
  question: "What is the market size for healthcare analytics?"
  extracted_context:
    product_domain: "healthcare analytics"
    geography: "US market"
    industry: "healthcare technology"
    additional_vars:
      - time_horizon: "2026-2030"
      - data_sources: "statista, mckinsey"
```

## Mode-Based Routing

### Assisted Mode Routing
```yaml
assisted_mode:
  detection: "question_detected"
  actions:
    - extract_context
    - generate_ember_prompt
    - call_ember_workflow
    - present_suggestion_to_user
    - wait_for_user_approval
    - inject_approved_response
    - update_context
    - continue_workflow
```

### Auto-Pilot Mode Routing
```yaml
auto_pilot_mode:
  detection: "question_detected"
  actions:
    - extract_context
    - check_confidence_threshold
    - generate_ember_prompt
    - call_ember_workflow
    - validate_response_confidence
    - inject_response_automatically
    - update_context
    - continue_workflow
```

### Manual Mode Routing
```yaml
manual_mode:
  detection: "question_detected"
  actions:
    - extract_context
    - generate_validation_suggestions_only
    - allow_user_manual_input
    - optional_ember_validation
    - continue_workflow
```

## Response Injection

### Injection Methods

#### 1. Direct Variable Injection
```yaml
injection_type: "variable_replacement"
workflow_variable: "market_size"
ember_response: "TAM: $50B, SAM: $5B, SOM: $500M"
result: "market_size = 'TAM: $50B, SAM: $5B, SOM: $500M'"
```

#### 2. Form Field Population
```yaml
injection_type: "form_population"
form_field: "user_personas"
ember_response: |
  ## Primary User Persona
  **Name:** Dr. Smith
  **Role:** Primary Care Physician
  **Goals:** Improve patient outcomes
result: "Form field populated with structured persona data"
```

#### 3. Document Insertion
```yaml
injection_type: "document_insertion"
target_document: "architecture.md"
insertion_point: "## System Context"
ember_response: "The system integrates with EHR systems via FHIR API"
result: "Content inserted into documentation"
```

### Injection Validation
- **Format Compliance** - Ensure response matches expected format
- **Context Consistency** - Verify response aligns with existing context
- **Completeness Check** - Confirm all required fields are populated

## State Management

### Workflow State Tracking
```yaml
workflow_state:
  session_id: "session_2026_001"
  current_workflow: "research"
  current_step: "domain-analysis/market_size"
  mode: "assisted"
  intercepted_questions: 15
  injected_responses: 14
  pending_approvals: 1
```

### Context State Preservation
- **Variable State** - Track all workflow variables
- **Decision History** - Log all major decisions
- **EMBED Interactions** - Record EMBER confidence scores and responses
- **User Interactions** - Track approvals and rejections

## Error Handling and Recovery

### Common Error Scenarios

#### 1. EMBER Response Timeout
```
error: "EMBED response timeout after 30 seconds"
recovery:
  - fallback_to_manual_input
  - flag_for_later_review
  - continue_workflow_with_placeholder
```

#### 2. Low Confidence Response
```
error: "EMBED confidence below threshold (0.7 < 0.8)"
recovery:
  - present_response_with_warning
  - require_user_override_approval
  - suggest_regeneration
```

#### 3. Context Inconsistency
```
error: "Response conflicts with existing context"
recovery:
  - highlight_conflict_to_user
  - present_alternatives
  - allow_context_update
```

### Recovery Strategies

#### Graceful Degradation
- **Auto-Pilot → Assisted** - Switch to user approval on low confidence
- **Assisted → Manual** - Allow full manual override
- **System Fallback** - Continue with placeholder values

#### User Notification
- **Error Alerts** - Notify user of interception issues
- **Status Updates** - Show EMBER processing status
- **Recovery Options** - Provide user recovery choices

## Performance Optimization

### Caching Strategies
- **Prompt Caching** - Cache generated EMBER prompts
- **Response Caching** - Cache EMBER responses for similar questions
- **Context Caching** - Cache extracted context for repeated patterns

### Parallel Processing
- **Batch Questions** - Process multiple questions simultaneously
- **EMBED Parallelization** - Run multiple EMBER instances
- **Workflow Parallelization** - Process independent workflow branches

### Monitoring and Metrics
```yaml
performance_metrics:
  average_response_time: "8.5 seconds"
  cache_hit_rate: "65%"
  error_rate: "2.1%"
  user_satisfaction: "94%"
```

## Security and Compliance

### Data Protection
- **Prompt Sanitization** - Remove sensitive data from EMBER prompts
- **Response Validation** - Check responses for data leakage
- **Audit Logging** - Log all EMBER interactions for compliance

### Access Control
- **Mode Permissions** - Control which modes are available per user
- **Question Filtering** - Filter sensitive questions from EMBER processing
- **Approval Workflows** - Require additional approvals for critical decisions

## Implementation Phases

### Phase 1: Core Interception (Week 1)
- Basic question detection
- Simple context extraction
- Manual mode routing
- Basic response injection

### Phase 2: EMBER Integration (Week 2)
- EMBER prompt generation
- Response processing
- Assisted mode implementation
- Error handling

### Phase 3: Auto-Pilot Mode (Week 3)
- Confidence-based routing
- Automatic injection
- Performance optimization
- Comprehensive testing

### Phase 4: Advanced Features (Week 4)
- Context preservation
- Learning and adaptation
- Advanced error recovery
- Production deployment

## Testing and Validation

### Unit Testing
- Question detection accuracy
- Context extraction completeness
- Response injection correctness
- Mode routing logic

### Integration Testing
- End-to-end workflow execution
- EMBER response quality
- User experience validation
- Performance benchmarking

### Production Validation
- A/B testing of modes
- User acceptance testing
- Error rate monitoring
- Performance optimization

## EMBER Consilium Integration

### Overview
Integration with EMBER consilium workflow for complex decision support during BMM workflow execution.

### Decision Complexity Assessment

#### Complexity Triggers
**Strategic Decisions:**
- Market entry/exit decisions
- Major investment decisions
- Partnership/alliance decisions
- Regulatory compliance decisions

**Technical Decisions:**
- Architecture selection decisions
- Technology stack decisions
- Infrastructure scaling decisions
- Security implementation decisions

**Business Decisions:**
- Pricing strategy decisions
- Market positioning decisions
- Resource allocation decisions
- Risk mitigation strategy decisions

#### Complexity Scoring
```yaml
decision_complexity:
  factors:
    - impact_level: "strategic/operational/tactical"
    - stakeholder_count: "1-5/6-15/16+"
    - time_pressure: "low/medium/high"
    - uncertainty_level: "low/medium/high"
    - resource_requirement: "low/medium/high"

  complexity_score: "1-5 scale"
  consilium_trigger_threshold: 4
```

### EMBER Consilium Workflow Calls

#### Workflow Invocation
```yaml
ember_consilium_call:
  trigger: "complex_decision_detected"
  workflow_path: "{project-root}/_bmad/bmm/workflows/ember-consilium/workflow.md"
  input_data:
    decision_context: "extracted_context"
    stakeholder_info: "workflow_stakeholders"
    constraints: "workflow_constraints"
    timeline: "decision_deadline"
  output_format: "structured_recommendation"
```

#### Context Passing
**Input to EMBER Consilium:**
```json
{
  "decision_topic": "Market expansion strategy for healthcare analytics platform",
  "stakeholders": ["CEO", "CTO", "CFO", "Product Manager"],
  "constraints": ["Budget: $2M", "Timeline: 6 months", "Risk tolerance: Medium"],
  "current_context": "BMM research workflow step 3",
  "evidence_available": ["market_analysis.pdf", "competitor_report.docx"],
  "decision_criteria": ["ROI > 15%", "Time-to-market < 6 months", "Risk < Medium"]
}
```

**Output from EMBER Consilium:**
```json
{
  "recommendation": "Proceed with cautious expansion",
  "confidence_score": 0.87,
  "rationale": "Evidence supports market opportunity with manageable risks",
  "implementation_plan": "Phased rollout with pilot program",
  "risk_mitigations": ["Pilot testing", "Phased investment", "Exit strategy"],
  "success_metrics": ["Market share growth", "Revenue increase", "Customer satisfaction"]
}
```

### Integration Workflow

#### Pre-Consilium Preparation
1. **Complexity Assessment** - Evaluate if decision requires consilium
2. **Context Compilation** - Gather all relevant information
3. **Stakeholder Alignment** - Confirm decision scope and constraints
4. **Evidence Packaging** - Prepare supporting documentation

#### Consilium Execution
1. **Workflow Launch** - Execute EMBER consilium with prepared context
2. **Progress Monitoring** - Track consilium analysis progress
3. **Result Reception** - Receive structured recommendation
4. **Confidence Validation** - Verify recommendation meets quality thresholds

#### Post-Consilium Integration
1. **Recommendation Processing** - Parse and validate consilium output
2. **Workflow Injection** - Integrate recommendation into BMM workflow
3. **User Presentation** - Present recommendation with confidence explanation
4. **Approval Workflow** - Obtain stakeholder approval if required

### Error Handling and Fallbacks

#### Consilium Failure Scenarios

##### Timeout or Unavailability
```
error: "EMBED consilium workflow unavailable"
fallback:
  - continue_with_standard_ember_processing
  - flag_decision_for_manual_review
  - schedule_followup_consilium_attempt
```

##### Low Confidence Recommendation
```
error: "EMBED consilium confidence below threshold (0.6 < 0.8)"
fallback:
  - present_recommendation_with_warnings
  - require_additional_evidence_gathering
  - escalate_to_human_expert_review
```

##### Context Incompatibility
```
error: "Provided context insufficient for consilium analysis"
fallback:
  - request_additional_context_from_user
  - use_simplified_consilium_mode
  - fall_back_to_standard_processing
```

### Performance Considerations

#### Execution Time Management
- **Consilium Timeout**: 15 minutes maximum
- **Parallel Processing**: Run consilium alongside continued workflow execution
- **Result Caching**: Cache consilium results for similar decisions

#### Resource Optimization
- **Selective Invocation**: Only call consilium for high-complexity decisions
- **Batch Processing**: Group related decisions for single consilium execution
- **Result Reuse**: Leverage previous consilium outputs for similar contexts

### Monitoring and Analytics

#### Consilium Usage Metrics
```yaml
consilium_metrics:
  total_calls: 45
  average_confidence: 0.82
  success_rate: 92%
  average_response_time: "8.7 minutes"
  decision_types:
    strategic: 15
    technical: 20
    business: 10
```

#### Effectiveness Tracking
- **Decision Quality**: Track success of consilium-recommended decisions
- **Time Savings**: Compare consilium-assisted vs manual decision times
- **User Satisfaction**: Survey stakeholders on consilium recommendation quality
- **Error Reduction**: Monitor reduction in decision-related errors

### Security and Governance

#### Data Protection
- **Context Sanitization**: Remove sensitive data before consilium calls
- **Access Logging**: Audit all consilium interactions
- **Result Encryption**: Secure consilium outputs and recommendations

#### Governance Controls
- **Decision Thresholds**: Define which decisions require consilium
- **Approval Workflows**: Require additional approvals for high-impact recommendations
- **Audit Trails**: Maintain complete decision history for compliance

### Implementation Roadmap

#### Phase 1: Basic Integration (Week 1)
- Simple consilium workflow calls
- Basic context passing
- Manual result integration
- Error handling setup

#### Phase 2: Advanced Integration (Week 2)
- Complexity-based triggering
- Automated context enrichment
- Parallel processing
- Result validation

#### Phase 3: Optimization (Week 3)
- Performance optimization
- Caching implementation
- Monitoring dashboard
- User experience refinements

#### Phase 4: Production Deployment (Week 4)
- Full integration testing
- Stakeholder training
- Production deployment
- Continuous monitoring
