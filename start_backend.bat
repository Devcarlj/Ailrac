@echo off
echo Starting Ailrac Python Backend...
cd /d "%~dp0"
call venv\Scripts\activate.bat
python backend/main.py
pause
