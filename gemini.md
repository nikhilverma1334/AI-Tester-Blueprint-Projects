# Project Constitution: Local LLM Testcase Generator

## 1. Project Goal
Create a local Chat UI where users enter requirements/code, and the system uses Ollama (Llama 3.2) to generate structured test cases based on a defined template.

## 2. Architecture: A.N.T. Three-Layer System
- **Trigger Layer (Frontend)**: **Streamlit** Web Interface.
    - Chat input field.
    - Display area for generated test cases.
    - specialized "Template" selection (optional).
- **Nexus Layer (Logic)**:
    - Prompt Engineering: Injecting the "Proper Template" into the context.
    - Response Parsing: Converting LLM output to structured UI elements.
- **Action Layer (Integration)**:
    - `ollama` Python library client.
    - `model='llama3.2'`.

## 3. Data Schema: The "Proper Template"
The system will force the LLM to adhere to this JSON structure:

```json
{
  "test_suite_summary": {
    "feature": "string",
    "total_tests": "integer"
  },
  "test_cases": [
    {
      "id": "TC-XXX",
      "title": "Short descriptive title",
      "type": "Functional | Negative | Boundary | Security",
      "priority": "P0 | P1 | P2",
      "preconditions": "list of strings",
      "steps": [
        "1. Step description",
        "2. Step description"
      ],
      "expected_result": "Clear pass/fail criteria"
    }
  ]
}
```

## 4. Architectural Invariants
1. **Local Only**: No data leaves the machine (localhost:11434).
2. **Model Pinning**: Always use `llama3.2` unless overridden.
3. **Fail-Safe**: If Ollama is down, show a clear "Please start Ollama" message in the UI.
4. **Structured Output**: Provide valid JSON for code usage, and formatted Markdown for human reading.
