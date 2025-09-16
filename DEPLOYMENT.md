# Vercel Deployment Guide

## 🚀 Deploy to Vercel

### 1. Install Vercel CLI
```bash
npm install -g vercel
```

### 2. Login to Vercel
```bash
vercel login
```

### 3. Deploy from Repository
```bash
vercel --prod
```

### 4. Set Environment Variables
In Vercel Dashboard:
1. Go to your project settings
2. Add Environment Variables:
   - `ASSEMBLYAI_API_KEY` = your_assemblyai_key
   - `OPENROUTER_API_KEY` = your_openrouter_key

### 5. Alternative: Deploy via GitHub
1. Connect your GitHub repo to Vercel
2. Auto-deploy on push to main branch
3. Set environment variables in dashboard

## 📁 Vercel Structure
- `streamlit_app.py` - Main Streamlit app
- `api/index.py` - Serverless API functions
- `vercel.json` - Deployment configuration

## 🔧 Environment Variables Required
- `ASSEMBLYAI_API_KEY`
- `OPENROUTER_API_KEY`

## 📝 Notes
- Streamlit runs as serverless function
- API endpoints handle file processing
- Environment variables set in Vercel dashboard