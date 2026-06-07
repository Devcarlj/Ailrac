@echo off
echo Starting Ailrac AI Assistant (Backend + Frontend)...
cd /d "%~dp0"
start "Ailrac Backend" cmd /c "start_backend.bat"
start "Ailrac Frontend" cmd /c "start_frontend.bat"
echo Services launched. You can access the UI at http://localhost:5173/
timeout /t 5
