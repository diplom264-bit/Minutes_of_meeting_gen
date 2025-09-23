# Connect GitHub to Hugging Face

## 🔗 Method 1: Direct GitHub Connection

### 1. Create Hugging Face Space
1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Click "Create new Space"
3. Name: `meeting-minutes-ai`
4. SDK: **Gradio**
5. Check "Link to GitHub repository"
6. Repository: `diplom264-bit/Minutes_of_meeting_gen`
7. Path in repo: `/` (root)
8. Create Space

### 2. Auto-sync Setup
- Hugging Face will automatically sync with your GitHub repo
- Any push to GitHub will update the Space
- Files needed in root: `app.py`, `transcribe.py`, `llm.py`, `docx_utils.py`, `requirements.txt`

## 🔗 Method 2: Manual Upload

### 1. Create Space (Gradio SDK)
2. Upload files directly:
   - Rename `app_gradio.py` to `app.py`
   - Upload `transcribe.py`, `llm.py`, `docx_utils.py`
   - Upload `requirements_hf.txt` as `requirements.txt`

## 🔑 Add Secrets
In Space Settings → Repository secrets:
```
ASSEMBLYAI_API_KEY=872b8b9caa2542f7ae9c252fbd584641
OPENROUTER_API_KEY=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
```

## 📝 Minimal Requirements
Use `requirements_hf.txt` (Gradio is pre-installed on HF):
```
requests==2.31.0
python-docx==0.8.11
python-dotenv==1.0.0
```

**Method 1 is recommended** - automatic sync with GitHub!