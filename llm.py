import requests
import json
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def generate_mom(transcript):
    """Generate Minutes of Meeting using OpenRouter API"""
    # Try Streamlit secrets first, then environment variables
    try:
        api_key = st.secrets["OPENROUTER_API_KEY"]
    except:
        api_key = os.getenv('OPENROUTER_API_KEY')
    
    if not api_key:
        raise Exception("OpenRouter API key not found in secrets or environment variables")
    
    # Debug: Check if key is being read
    if not api_key.startswith('sk-or-'):
        raise Exception(f"Invalid API key format. Key starts with: {api_key[:10]}...")
    
    prompt = """You are a meeting summarization assistant.
Your job is to transform raw meeting transcripts into clear, structured Minutes of Meeting (MoM).  
Always return output as a **valid JSON object** following the schema below.  
Do not invent content not present in the transcript.

JSON SCHEMA:
{
  "meeting_title": string,
  "date": string,
  "attendees": [string],
  "agenda_items": [string],
  "key_points": [string],
  "action_items": [
    {
      "task": string,
      "owner": string,
      "due_date": string
    }
  ],
  "next_steps": [string],
  "decisions_made": [string]
}

TRANSCRIPT:
""" + transcript

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "meta-llama/llama-3.2-3b-instruct:free",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )
    
    # Show response details for debugging
    st.write(f"Status Code: {response.status_code}")
    st.write(f"Response Headers: {dict(response.headers)}")
    
    try:
        response_data = response.json()
        st.write(f"Response Data: {response_data}")
    except Exception as e:
        raise Exception(f"JSON Parse Error. Status: {response.status_code}, Text: {response.text[:500]}")
    
    if "choices" not in response_data:
        raise Exception(f"No choices in response. Full response: {response_data}")
    
    result = response_data["choices"][0]["message"]["content"]
    
    # Extract JSON from response
    try:
        start = result.find('{')
        end = result.rfind('}') + 1
        json_str = result[start:end]
        return json.loads(json_str)
    except:
        # Fallback if JSON parsing fails
        return {
            "meeting_title": "Meeting Summary",
            "date": "Unknown",
            "attendees": ["Unknown"],
            "agenda_items": ["Discussion"],
            "key_points": [transcript[:200] + "..."],
            "action_items": [],
            "next_steps": [],
            "decisions_made": []
        }