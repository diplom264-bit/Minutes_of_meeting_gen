# Deploy Now - Free Alternatives

## 🆓 Render (Recommended - No Account Blocks)
**Free 750 hours/month**

### Deploy Steps:
1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. New → Web Service
4. Connect repository: `diplom264-bit/Minutes_of_meeting_gen`
5. Build Command: `pip install -r requirements.txt`
6. Start Command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
7. Add Environment Variables:
   - `ASSEMBLYAI_API_KEY` = `872b8b9caa2542f7ae9c252fbd584641`
   - `OPENROUTER_API_KEY` = `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`
8. Deploy

## 🤗 Hugging Face Spaces (Completely Free)
**No limits, perfect for ML apps**

### Deploy Steps:
1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Create account
3. New Space → Streamlit
4. Upload files or connect GitHub
5. Add secrets in Settings
6. Deploy automatically

## 🚀 Railway (Free Tier)
**$5 free credit monthly**

### Deploy Steps:
1. Go to [railway.app](https://railway.app)
2. Deploy from GitHub
3. Select repository
4. Add environment variables
5. Deploy with Dockerfile

## 🐳 Local Docker (Always Works)
```bash
docker-compose up --build
```
Access: http://localhost:8501

**Render is fastest to deploy - takes 2 minutes!**