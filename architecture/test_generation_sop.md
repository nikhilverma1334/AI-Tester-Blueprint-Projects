# SOP: Automated Test Case Generation

## Goal
To generate a comprehensive, structured test suite (JSON format) from a given user input (requirement or code snippet) using a local LLM.

## Inputs
- **Input Text**: String (Natural language requirement or Code block).
- **Model Name**: String (e.g., `llama3.2`).
- **Template**: Dictionary (Strict JSON schema).

## Logic Flow
1.  **Receive Input**: User submits text via Streamlit UI.
2.  **Validation**: Check if input is not empty.
3.  **Prompt Construction**:
    - Inject "Identity": Expert QA Automation Architect.
    - Inject "Context": Input text.
    - Inject "Constraint": Strict JSON Schema (The "Proper Template").
4.  **Execution (Action Layer)**:
    - Call `ollama.chat` with the constructed prompt.
    - Set `format='json'` (if supported by model/library) or use prompt engineering to enforce it.
5.  **Parsing & Validation (Nexus Layer)**:
    - Extract JSON substring from response.
    - Validate against the defined schema keys.
    - If valid: Return Dict.
    - If invalid: Return Error.
6.  **Output**: Structured Dictionary ready for UI rendering.

## Edge Cases
- **Ollama Down**: Catch `ConnectionError` and return user-friendly message.
- **Model Missing**: Catch `ModelNotFoundError` and suggest `ollama pull`.
- **Invalid JSON**: If LLM chats instead of outputting JSON, attempt regex extraction. If that fails, show raw text.
- **Empty Response**: Retry once, then fail.
