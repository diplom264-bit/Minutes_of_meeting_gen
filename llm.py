import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def generate_mom(transcript):
    """Generate Minutes of Meeting using OpenRouter API"""
    api_key = os.getenv('OPENROUTER_API_KEY')
    
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
        "model": "deepseek/deepseek-chat",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )
    
    result = response.json()["choices"][0]["message"]["content"]
    
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