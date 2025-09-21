@echo off
echo Starting Minutes of Meeting Generator...
echo.
echo Building Docker image...
docker-compose build
echo.
echo Starting application...
docker-compose up
echo.
echo App will be available at: http://localhost:8501
pause