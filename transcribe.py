import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

def transcribe_audio(audio_file_path):
    """Transcribe audio using AssemblyAI API"""
    api_key = os.getenv('ASSEMBLYAI_API_KEY')
    
    # Upload file
    upload_url = "https://api.assemblyai.com/v2/upload"
    headers = {"authorization": api_key}
    
    with open(audio_file_path, "rb") as f:
        response = requests.post(upload_url, headers=headers, files={"file": f})
    
    audio_url = response.json()["upload_url"]
    
    # Request transcription
    transcript_url = "https://api.assemblyai.com/v2/transcript"
    data = {"audio_url": audio_url}
    
    response = requests.post(transcript_url, json=data, headers=headers)
    transcript_id = response.json()["id"]
    
    # Poll for completion
    polling_url = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
    
    while True:
        response = requests.get(polling_url, headers=headers)
        status = response.json()["status"]
        
        if status == "completed":
            return response.json()["text"]
        elif status == "error":
            raise Exception("Transcription failed")
        
        time.sleep(3)