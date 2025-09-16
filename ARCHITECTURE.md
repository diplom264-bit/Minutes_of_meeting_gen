# Architecture Overview

## 📁 Project Structure
```
Minutes_of_meeting_gen/
├── app.py              # Streamlit frontend
├── transcribe.py       # AssemblyAI integration
├── llm.py             # OpenRouter LLM integration
├── docx_utils.py      # DOCX generation
├── requirements.txt   # Dependencies
├── .env.example       # Environment template
├── README.md          # Main documentation
├── SETUP.md           # Quick setup guide
└── ARCHITECTURE.md    # This file
```

## 🔄 Data Flow
```
Audio File → AssemblyAI → Transcript → OpenRouter → JSON MoM → DOCX
```

## 🧩 Components

### 1. Frontend (`app.py`)
- Streamlit web interface
- File upload handling
- Progress indicators
- JSON display and DOCX download

### 2. Transcription (`transcribe.py`)
- AssemblyAI API integration
- Audio file upload to AssemblyAI
- Polling for transcription completion
- Error handling for failed transcriptions

### 3. LLM Processing (`llm.py`)
- OpenRouter API integration
- DeepSeek model usage (free tier)
- Structured prompt template
- JSON parsing with fallback

### 4. Document Generation (`docx_utils.py`)
- python-docx integration
- Structured MoM formatting
- Professional document layout

## 🔧 API Integrations

### AssemblyAI
- **Purpose**: Audio transcription
- **Tier**: Free
- **Rate Limits**: Check AssemblyAI docs
- **Supported Formats**: MP3, WAV, M4A, MP4

### OpenRouter
- **Purpose**: LLM processing
- **Model**: DeepSeek (free tier)
- **Input**: Meeting transcript
- **Output**: Structured JSON MoM

## 📊 JSON Schema
```json
{
  "meeting_title": "string",
  "date": "string", 
  "attendees": ["string"],
  "agenda_items": ["string"],
  "key_points": ["string"],
  "action_items": [
    {
      "task": "string",
      "owner": "string", 
      "due_date": "string"
    }
  ],
  "next_steps": ["string"],
  "decisions_made": ["string"]
}
```