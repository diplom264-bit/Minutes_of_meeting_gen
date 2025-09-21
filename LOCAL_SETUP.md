# Local Docker Setup

## 🐳 Quick Start

### Prerequisites
- Docker Desktop installed
- Git (optional)

### Option 1: One-Click Start (Windows)
```bash
run-local.bat
```

### Option 2: Manual Commands
```bash
# Build and run
docker-compose up --build

# Or step by step
docker build -t mom-generator .
docker run -p 8501:8501 --env-file .env mom-generator
```

## 🌐 Access
- **URL**: http://localhost:8501
- **Port**: 8501

## 🔧 Development Mode
For live code changes:
```bash
docker-compose up --build
```

## 🛑 Stop Application
```bash
docker-compose down
```

## 📝 Features
- ✅ Full functionality
- ✅ API keys pre-configured
- ✅ Auto-restart on failure
- ✅ Volume mounting for development
- ✅ Same as production environment

## 🔍 Troubleshooting
- **Port conflict**: Change `8501:8501` to `8502:8501` in docker-compose.yml
- **Build issues**: Run `docker system prune` and retry
- **API errors**: Check API keys in docker-compose.yml