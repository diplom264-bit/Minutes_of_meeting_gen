# Deploy to Streamlit Cloud (New Account)

## 🆕 Create New GitHub Account
1. Go to [github.com](https://github.com)
2. Sign up with different email
3. Create new repository: `meeting-minutes-ai`

## 📤 Push Code to New Repo
```bash
# Add new remote
git remote add new-origin https://github.com/YOUR_NEW_USERNAME/meeting-minutes-ai.git

# Push to new repo
git push new-origin main
```

## ☁️ Deploy to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with NEW GitHub account
3. Click "New app"
4. Repository: `YOUR_NEW_USERNAME/meeting-minutes-ai`
5. Branch: `main`
6. Main file path: `app.py`
7. Click "Deploy"

## 🔑 Add Secrets
In Streamlit app settings → Secrets:
```toml
ASSEMBLYAI_API_KEY = "872b8b9caa2542f7ae9c252fbd584641"
OPENROUTER_API_KEY = "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"
```

## ✅ Alternative: Use Different Email
- Create new Streamlit account with different email
- Connect to existing GitHub repo
- Same deployment process

Your app will be live at: `https://meeting-minutes-ai-[random].streamlit.app`