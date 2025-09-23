import whisper
import os

class AudioTranscriber:
    def __init__(self, model_size="base"):
        """Initialize Whisper model"""
        self.model = whisper.load_model(model_size)
    
    def transcribe_audio(self, audio_file_path):
        """Transcribe audio file to text"""
        if not os.path.exists(audio_file_path):
            raise FileNotFoundError(f"Audio file not found: {audio_file_path}")
        
        result = self.model.transcribe(audio_file_path)
        return result["text"].strip()