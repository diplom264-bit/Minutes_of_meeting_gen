# Quick Setup Guide

## 🚀 Get Started in 3 Steps

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Keys
Create a `.env` file in the project root:
```bash
ASSEMBLYAI_API_KEY=your_assemblyai_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
```

### 3. Run the App
```bash
streamlit run app.py
```

## 🔑 Getting API Keys

### AssemblyAI (Free Tier)
1. Visit [AssemblyAI](https://www.assemblyai.com/)
2. Sign up for free account
3. Get API key from dashboard

### OpenRouter (Free Tier)
1. Visit [OpenRouter](https://openrouter.ai/)
2. Sign up for free account
3. Get API key from dashboard
4. Uses DeepSeek model (free tier)

## 📱 Usage
1. Open browser at `http://localhost:8501`
2. Upload audio file (MP3, WAV, M4A, MP4)
3. Click "Generate Minutes of Meeting"
4. Download DOCX file

## 🛠️ Troubleshooting
- Ensure API keys are valid
- Check internet connection for API calls
- Supported audio formats: MP3, WAV, M4A, MP4
- Max file size depends on AssemblyAI limits