# Free Deployment Options

## 🆓 Render (Free Tier - Recommended)
Free tier with 750 hours/month.

### Deploy Steps:
1. Go to [render.com](https://render.com)
2. Connect GitHub repository
3. Choose "Web Service"
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
6. Add environment variables:
   - `ASSEMBLYAI_API_KEY` = `872b8b9caa2542f7ae9c252fbd584641`
   - `OPENROUTER_API_KEY` = `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`

## 🆓 Hugging Face Spaces (Completely Free)
Free hosting for ML apps.

### Deploy Steps:
1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Create new Space with Streamlit
3. Upload your files
4. Add secrets in Settings:
   - `ASSEMBLYAI_API_KEY` = `872b8b9caa2542f7ae9c252fbd584641`
   - `OPENROUTER_API_KEY` = `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`

## 🆓 Fly.io (Free Tier)
Free tier with 3 shared-cpu-1x machines.

### Deploy Steps:
1. Install flyctl: `curl -L https://fly.io/install.sh | sh`
2. Login: `flyctl auth login`
3. Launch: `flyctl launch`
4. Set secrets:
   ```bash
   flyctl secrets set ASSEMBLYAI_API_KEY=872b8b9caa2542f7ae9c252fbd584641
   flyctl secrets set OPENROUTER_API_KEY=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
   ```
5. Deploy: `flyctl deploy`

## 🆓 Koyeb (Free Tier)
Free tier with 512MB RAM.

### Deploy Steps:
1. Go to [koyeb.com](https://koyeb.com)
2. Connect GitHub repository
3. Choose Docker deployment
4. Add environment variables
5. Deploy automatically

## 🔧 Local Docker (Always Free)
```bash
run-local.bat
```

All options maintain 100% functionality!