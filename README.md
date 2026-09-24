
# Ailrac Agentic Dekstop Assistant v2.5
<img width="1920" height="1080" alt="ailrac" src="https://github.com/user-attachments/assets/6d3ef7ab-7695-4af0-b53b-0429d3534b13" />

Ailrac is a full-stack personal AI assistant featuring a beautiful **React (Vite) Frontend** (with dark minimalist theme, markdown syntax highlighting, voice input/output) and a robust **FastAPI Python Backend** (powered by Google Gemini 2.5 Flash, SQLite persistence, localized desktop automation, security settings, and Telegram gateway).

---

## 🚀 Quick Start

To start both the frontend dev server and the backend FastAPI server automatically, run the master script in the root directory:

```bash
# Double-click the file in Windows Explorer or run from terminal:
.\start_all.bat
```

This will launch two command windows:
1. **Ailrac Backend** running at `http://localhost:8000` (API documentation at `/docs`)
2. **Ailrac Frontend** running at `http://localhost:5173`

Open **[http://localhost:5173/](http://localhost:5173/)** in your browser to start chatting!

---

## 🔒 Security & Access Control

You can configure platform/domain blocks under **Settings ⚙️ -> Security**:
- **Facebook Access Protection**: Add `facebook.com` to the blocked list. The backend checks all inputs and will refuse to open, search, or interact with blocked platforms, keeping your personal accounts safe.
- **Safe Search**: Toggling Safe Search forces Google desktop searches opened by Ailrac to append `safe=active`.

---

## 🎛️ Input & Output Channels (Features)

Under **Settings ⚙️ -> Features**, you can toggle the following:
1. **🎙️ Voice Input (Microphone)**: When enabled, a background thread listens continuously via your microphone. Speak to Ailrac at any time!
2. **🔊 Voice Output**: When enabled, Ailrac speaks its responses aloud locally on your PC.
3. **📱 Telegram Gateway**: Control Ailrac remotely. When enabled and configured, Ailrac responds only to your Telegram account via a dedicated Telegram bot.

---

## ⚙️ Configuration

Environment variables are stored in [backend/.env](file:///c:/VScodes/Ailrac/backend/.env):
```env
GEMINI_API_KEY=your_gemini_key_here
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
MY_TELEGRAM_ID=your_telegram_numeric_id
```

---

## 📁 Project Structure

```
c:\VScodes\Ailrac\
├── backend/
│   ├── main.py              # FastAPI server & routes
│   ├── services.py          # Background Voice & Telegram services
│   ├── ailrac_core.py       # Gemini AI router & local commands
│   ├── database.py          # SQLite database wrapper
│   ├── security.py          # Security domain/safe search checks
│   ├── models.py            # Pydantic schemas
│   ├── .env                 # API keys & configuration
│   └── requirements.txt     # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── App.jsx          # Root component
│   │   ├── index.css        # dark minimalist styling
│   │   ├── hooks/
│   │   │   └── useChat.js   # API hook for conversation & settings
│   │   └── components/
│   │       ├── Sidebar.jsx        # Conversational history & menus
│   │       ├── ChatWindow.jsx     # Chat bubbles & markdown syntax rendering
│   │       ├── MessageInput.jsx   # Textbox & speech recognition button
│   │       └── SettingsModal.jsx  # Security & features toggles
│   ├── package.json
│   └── vite.config.js
├── start_backend.bat        # Runs Python backend
├── start_frontend.bat       # Runs React dev server
└── start_all.bat            # Launches backend + frontend together
```

# Ailrac
An AI Powered Desktop Assistant that can control your laptop remotely
 7bef7256a6cef7b37941ce5b3ff9647e2af2315a
