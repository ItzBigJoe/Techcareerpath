import os
import json

# Define the model ID
MODEL_ID = "gpt-4o-mini"  # Using a fast and cost-effective model

def get_ai_client():
    """Lazily initialize the OpenAI client to avoid errors when API key is missing during import."""
    try:
        from openai import OpenAI
    except ImportError:
        return None

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None
    try:
        return OpenAI(api_key=api_key)
    except Exception:
        return None

def generate_result(answers):
    prompt = f"""
    Analyze these career assessment answers: {answers}

    Return ONLY a valid JSON object with this exact structure:
    {{
      "career": "Recommended Career Name",
      "score": integer (0-100),
      "skills": {{"SkillName": score_integer, ...}},
      "gaps": ["Gap 1", "Gap 2", ...]
    }}
    """

    client = get_ai_client()
    
    if not client:
        # Fallback for missing API key or client initialization failure
        return {
            "career": "Technical Path",
            "score": 50,
            "skills": {"General": 50},
            "gaps": ["Error: OpenAI API Key not found. Please set OPENAI_API_KEY in your environment variables."]
        }

    try:
        response = client.chat.completions.create(
            model=MODEL_ID,
            messages=[
                {"role": "system", "content": "You are a career counseling AI that analyzes skill assessments and returns JSON data."},
                {"role": "user", "content": prompt}
            ],
            response_format={ "type": "json_object" }
        )
        
        if not response.choices or len(response.choices) == 0:
            raise ValueError('No choices in response from OpenAI')
            
        content = response.choices[0].message.content
        if not content:
            raise ValueError("Empty response from OpenAI")
            
        return json.loads(content)
    except Exception as e:
        print(f"AI Error: {e}")
        return {
            "career": "Technical Path",
            "score": 50,
            "skills": {"General": 50},
            "gaps": [f"AI Error: {str(e)}"]
        }
