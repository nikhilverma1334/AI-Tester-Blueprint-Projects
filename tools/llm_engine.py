
import json
import ollama

def get_test_case_template():
    return {
        "test_suite_summary": {
            "feature": "Name of the feature being tested",
            "total_tests": 0
        },
        "test_cases": [
            {
                "id": "TC-001",
                "title": "Title of the test case",
                "type": "Positive", # or "Negative", "Boundary", "Security"
                "priority": "P1",
                "preconditions": ["Precondition 1"],
                "steps": ["Step 1", "Step 2"],
                "expected_result": "Expected behavior"
            }
        ]
    }

def generate_test_cases_logic(input_text, model_name="llama3.2"):
    """
    Generates test cases using Ollama based on the input text and strict JSON template.
    """
    
    system_prompt = f"""
    You are an expert QA Automation Architect.
    Your task is to generate a comprehensive test suite for the following requirement/code.
    
    You must output strictly valid JSON format.
    Do not add any conversational text before or after the JSON.
    
    Follow this exact JSON structure:
    {json.dumps(get_test_case_template(), indent=2)}
    
    Ensure you cover:
    1. Functional scenarios (Positive flows)
    2. Negative scenarios (Error handling)
    3. Edge cases (Boundary values)
    
    If the user input is code, analyze the logic to create unit test scenarios.
    If the user input is a requirement, generate acceptance test scenarios.
    """
    
    try:
        # SOP Step 4: Execution
        # We explicitly ask for JSON mode if the model supports it, but standard prompt engineering 
        # is the most reliable cross-model method currently.
        response = ollama.chat(model=model_name, messages=[
            {
                'role': 'system',
                'content': system_prompt,
            },
            {
                'role': 'user',
                'content': input_text,
            },
        ])
        
        content = response['message']['content']
        
        # SOP Step 5: Parsing & Validation
        # Robust extraction: find the first '{' and the last '}'
        start_idx = content.find('{')
        end_idx = content.rfind('}')
        
        if start_idx != -1 and end_idx != -1:
            json_str = content[start_idx:end_idx+1]
            return json_str
        else:
            # Fallback: Return raw content if no JSON structure found
            return content
            
    except Exception as e:
        # SOP Edge Case: Ollama Connection/Model Error
        error_msg = str(e)
        if "connection" in error_msg.lower():
            return json.dumps({"error": "Ollama is not running. Please run 'ollama serve' or start the Ollama app."})
        elif "not found" in error_msg.lower():
             return json.dumps({"error": f"Model '{model_name}' not found. Please Run 'ollama pull {model_name}' in your terminal."})
        return json.dumps({"error": f"System Error: {error_msg}"})
