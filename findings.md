# Findings & Research

## Requirements Analysis
- **Goal**: Local LLM Testcase generator.
- **Tooling**: Ollama (Llama 3.2).
- **OS**: Windows.
- **Interface**: Chat UI.

## Discovery: B.L.A.S.T. Answers
1. **North Star**: Local LLM Testcase generator with a standard Template, using Ollama (Llama 3.2).
2.  **Integrations**: Ollama (Local API).
3.  **Source of Truth**: User Input (Chat).
4.  **Delivery Payload**: UI Chat (Streamlit recommended for local Python tools).
5.  **Behavioral Rules**: Direct Input-to-Output generation.

## Research Findings (Ollama & Test Generation)
- **Library**: `ollama` Python library.
- **Model**: `llama3.2` (Need to remember to `ollama pull llama3.2` if not present).
- **Patterns**:
    - **Persona**: QA Automation Architect.
    - **Few-Shot**: Use the "Proper Template" as a few-shot example in the prompt.
    - **Output**: JSON schema matching the template.
