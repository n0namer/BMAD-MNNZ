# Search-Decision Protocol (Central)

Use this protocol for any decision, ambiguity, or prioritization:

1) Search order (simple -> complex)
   - CLI Claude Flow memory search (global)
   - Local MD search (rg) in _bmad-output/life-os
   - Web/MCP search (only if still ambiguous)

2) Evidence snapshot
   - Summarize key evidence in 3-6 bullets
   - Record evidence in project journal or workflow plan using this format:
     - Evidence: {source} -> {finding}
     - Evidence: {source} -> {finding}
     - Decision: {option selected}
     - Confidence: {high/medium/low}
     - Rationale: {why}

3) Consilium decision
   - Rank 2-4 options with pros/cons
   - Provide a recommendation and confidence (high/medium/low)

4) User choice
   - If confidence is low -> ask user to choose
   - If confidence is high -> proceed and note rationale

Source of truth: data/mcp_search_system_prompt_xml.md
