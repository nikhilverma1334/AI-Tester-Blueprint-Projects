
from tools.llm_engine import generate_test_cases_logic
import json

print("[INFO] Initiating Handshake with Ollama...")

try:
    # Test input
    test_input = "Login feature: user enters username and password, clicks login. If valid, redirect to dashboard. If invalid, show error."
    
    print(f"[INFO] Sending test payload: '{test_input}'")
    
    response = generate_test_cases_logic(test_input)
    
    print("\n[INFO] Raw Response received:")
    print(response[:200] + "..." if len(response) > 200 else response)
    
    # Validation
    if "{" in response and "}" in response:
        print("\n[SUCCESS] Handshake SUCCESS: JSON structure detected.")
    else:
        print("\n[WARNING] Handshake WARNING: Response might not be valid JSON.")
        
except Exception as e:
    print(f"\n[ERROR] Handshake FAILED: {e}")
