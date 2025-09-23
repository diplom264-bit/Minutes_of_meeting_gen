# MoM Generator v2

An AI-powered Minutes of Meeting generator that transcribes audio files and creates structured meeting summaries.

## Features

- 🎵 **Audio Transcription**: Uses OpenAI Whisper for accurate speech-to-text
- 🤖 **AI-Powered Summarization**: Leverages Deepseek via OpenRouter for structured MoM generation
- 🌐 **Web Interface**: Simple Streamlit-based UI
- 📥 **Export Options**: Download results as JSON

## Technology Stack

- **STT Engine**: OpenAI Whisper (local processing)
- **LLM Engine**: Deepseek via OpenRouter API
- **UI Framework**: Streamlit
- **Audio Processing**: PyTorch/TorchAudio

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

3. **Usage**:
   - Enter your OpenRouter API key
   - Upload an audio file (MP3, WAV, M4A, etc.)
   - Click "Generate Minutes of Meeting"
   - Download the structured results

## Supported Audio Formats

- MP3, WAV, M4A
- MP4, MPEG, MPGA
- WebM

## Output Structure

The generated MoM includes:
- Meeting title and date
- List of attendees
- Key decisions made
- Action items with assignees and deadlines
- Discussion points
- Next meeting details

## API Configuration

The application uses OpenRouter API with Deepseek model for cost-effective LLM processing.

## Limitations

- **Free Tier Only**: Designed for prototype/demo purposes
- **No Multi-user Support**: Single-session processing
- **File Size Limits**: Depends on available system memory
- **No Authentication**: Not suitable for sensitive data