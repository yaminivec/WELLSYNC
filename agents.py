import os
from google import genai
from prompts import WORKOUT_PROMPT, DIET_PROMPT, EXPLANATION_PROMPT

# Get API key from environment/Streamlit Secrets
api_key = os.environ.get("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found! Add it in Streamlit Secrets.")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Generic Gemini call
def call_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

# Agents
def workout_agent(data):
    return call_gemini(WORKOUT_PROMPT.format(**data))

def diet_agent(data):
    return call_gemini(DIET_PROMPT.format(**data))

def explanation_agent(data):
    return call_gemini(EXPLANATION_PROMPT.format(**data))
