from google import genai
import os
import json

# Define the model ID
MODEL_ID = "gemini-1.5-flash"

def get_ai_client():
    """Lazily initialize the AI client to avoid errors when API key is missing during import."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return None
    try:
        return genai.Client(api_key=api_key)
    except Exception:
        return None

def generate_result(answers):
    prompt = f"""
    Analyze these answers: {answers}

    Return JSON:
    {{
      "career": "...",
      "score": 0-100,
      "skills": {{"Python":80,"SQL":60}},
      "gaps": ["Improve SQL"]
    }}
    """

    client = get_ai_client()
    
    if not client:
        # Fallback for missing API key or client initialization failure
        return {
            "career": "Technical Path",
            "score": 50,
            "skills": {"General": 50},
            "gaps": ["Missing API Key - Assessment using default result"]
        }

    try:
        res = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt
        )
        
        if not res or not res.text:
            raise ValueError("Empty response from AI")
            
        # The new SDK might return a cleaner response or we might still need to strip markdown
        raw = res.text.replace("```json","").replace("```","").strip()
        return json.loads(raw)
    except Exception as e:
        print(f"AI Error: {e}")
        return {
            "career": "Technical Path",
            "score": 50,
            "skills": {"General": 50},
            "gaps": [f"AI Error: {str(e)}"]
        }