# Alternative Deployment Options

## 🚀 Railway (Recommended)
Railway supports larger applications and Docker containers.

### Deploy Steps:
1. Go to [railway.app](https://railway.app)
2. Connect your GitHub repository
3. Add environment variables:
   - `ASSEMBLYAI_API_KEY` = `872b8b9caa2542f7ae9c252fbd584641`
   - `OPENROUTER_API_KEY` = `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`
4. Deploy automatically

## 🐳 Render
Another good option for Streamlit apps.

### Deploy Steps:
1. Go to [render.com](https://render.com)
2. Connect GitHub repository
3. Choose "Web Service"
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
6. Add environment variables

## ☁️ Streamlit Cloud
Native Streamlit hosting.

### Deploy Steps:
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Connect GitHub repository
3. Add secrets in app settings:
   ```
   ASSEMBLYAI_API_KEY = "872b8b9caa2542f7ae9c252fbd584641"
   OPENROUTER_API_KEY = "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"
   ```

## 🔧 Local Docker
Test locally with Docker:
```bash
docker build -t mom-generator .
docker run -p 8501:8501 --env-file .env mom-generator
```

All options maintain 100% functionality!