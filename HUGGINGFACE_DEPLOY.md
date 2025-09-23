# Deploy to Hugging Face Spaces with Gradio

## 🚀 Quick Deploy Steps

### 1. Create Hugging Face Account
1. Go to [huggingface.co](https://huggingface.co)
2. Sign up for free account
3. Go to [Settings → Tokens](https://huggingface.co/settings/tokens)
4. Create new token with **write** permissions

### 2. Create New Space
1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Click "Create new Space"
3. Space name: `meeting-minutes-generator`
4. License: `MIT`
5. SDK: `Gradio`
6. Hardware: `CPU basic` (free)
7. Click "Create Space"

### 3. Clone and Setup
```bash
# Clone the space
git clone https://huggingface.co/spaces/YOUR_USERNAME/meeting-minutes-generator
cd meeting-minutes-generator

# Copy files from our project
cp ../app_gradio.py app.py
cp ../transcribe.py .
cp ../llm.py .
cp ../docx_utils.py .
cp ../requirements.txt .
```

### 4. Add Secrets
1. Go to your Space settings
2. Click "Settings" → "Repository secrets"
3. Add secrets:
   - `ASSEMBLYAI_API_KEY` = `872b8b9caa2542f7ae9c252fbd584641`
   - `OPENROUTER_API_KEY` = `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`

### 5. Deploy
```bash
git add .
git commit -m "Add Minutes of Meeting Generator"
git push
```

## ✅ Features in Gradio Version
- 🎵 Audio file upload
- 📝 AI transcription
- 🤖 MoM generation
- 📄 DOCX download
- 🧪 Testing mode (saved transcript)
- 🔒 Secure API keys

Your app will be live at: `https://huggingface.co/spaces/YOUR_USERNAME/meeting-minutes-generator`