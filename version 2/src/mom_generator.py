import requests
import json
from typing import Dict

class MoMGenerator:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        
    def generate_mom(self, transcript: str) -> Dict:
        """Generate Minutes of Meeting from transcript"""
        prompt = f"""
Please analyze the following meeting transcript and generate a structured Minutes of Meeting (MoM) document.

TRANSCRIPT:
{transcript}

Please provide the output in the following JSON format:
{{
    "meeting_title": "Brief title for the meeting",
    "date": "Meeting date if mentioned, otherwise 'Not specified'",
    "attendees": ["List of attendees mentioned"],
    "key_decisions": ["List of key decisions made"],
    "action_items": [
        {{
            "task": "Description of the task",
            "assignee": "Person responsible",
            "deadline": "Deadline if mentioned"
        }}
    ],
    "discussion_points": ["Main topics discussed"],
    "next_meeting": "Next meeting details if mentioned"
}}

Ensure all fields are filled appropriately. If information is not available, use "Not specified" or empty arrays as appropriate.
"""

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "deepseek/deepseek-chat",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.3
        }
        
        response = requests.post(self.base_url, headers=headers, json=data)
        
        if response.status_code == 200:
            result = response.json()
            content = result['choices'][0]['message']['content']
            
            # Extract JSON from response
            try:
                start_idx = content.find('{')
                end_idx = content.rfind('}') + 1
                json_str = content[start_idx:end_idx]
                return json.loads(json_str)
            except:
                return {"error": "Failed to parse response", "raw_response": content}
        else:
            return {"error": f"API request failed: {response.status_code}", "details": response.text}