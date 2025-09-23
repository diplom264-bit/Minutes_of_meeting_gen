# Deploy to Your Hugging Face Space

## 🚀 Quick Deploy Steps

### 1. Clone Your HF Space
```bash
git clone https://huggingface.co/spaces/donkey-bait/minutes-meeting-ai
cd minutes-meeting-ai
```

### 2. Copy Files from This Project
```bash
# Copy main files
cp ../app_gradio.py app.py
cp ../transcribe.py .
cp ../llm.py .
cp ../docx_utils.py .
cp ../requirements_hf.txt requirements.txt
```

### 3. Add Secrets
Create `.env` file (for local testing):
```bash
ASSEMBLYAI_API_KEY=872b8b9caa2542f7ae9c252fbd584641
OPENROUTER_API_KEY=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
```

### 4. Push to HF Space
```bash
git add .
git commit -m "Add Minutes of Meeting Generator"
git push
```

### 5. Add Secrets in HF Interface
1. Go to your Space: https://huggingface.co/spaces/donkey-bait/minutes-meeting-ai
2. Click "Settings" → "Repository secrets"
3. Add:
   - `ASSEMBLYAI_API_KEY` = `872b8b9caa2542f7ae9c252fbd584641`
   - `OPENROUTER_API_KEY` = `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`

## ✅ Your app will be live at:
https://huggingface.co/spaces/donkey-bait/minutes-meeting-ai

**All files are ready in this project - just copy and push!**