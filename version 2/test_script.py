#!/usr/bin/env python3
"""
Test script for MoM Generator v2
"""

import os
from src.transcription import AudioTranscriber
from src.mom_generator import MoMGenerator

def test_transcription():
    """Test audio transcription"""
    print("Testing transcription...")
    
    # You can add a sample audio file to test
    # transcriber = AudioTranscriber(model_size="base")
    # transcript = transcriber.transcribe_audio("audio_samples/sample.wav")
    # print(f"Transcript: {transcript}")
    
    print("Transcription test skipped - no sample audio file")

def test_mom_generation():
    """Test MoM generation with sample transcript"""
    print("Testing MoM generation...")
    
    sample_transcript = """
    Good morning everyone. This is our weekly team meeting on January 15th, 2024. 
    Present today are John Smith, Sarah Johnson, and Mike Davis.
    
    First agenda item is the project timeline. John mentioned that we need to complete 
    the API development by February 1st. Sarah will handle the frontend integration.
    
    We decided to use React for the frontend and Node.js for the backend.
    
    Action items: John will finish the API documentation by January 20th. 
    Sarah will start the frontend development next week.
    
    Next meeting is scheduled for January 22nd at 10 AM.
    """
    
    api_key = "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"
    
    mom_generator = MoMGenerator(api_key)
    result = mom_generator.generate_mom(sample_transcript)
    
    print("MoM Generation Result:")
    print(result)

if __name__ == "__main__":
    test_transcription()
    print("\n" + "="*50 + "\n")
    test_mom_generation()