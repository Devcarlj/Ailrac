import os
import sys
import webbrowser
import requests
import threading
from google import genai
import pyttsx3
import speech_recognition as sr
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent / "backend" / ".env")

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
MY_TELEGRAM_ID = int(os.getenv("MY_TELEGRAM_ID", "0"))

if not BOT_TOKEN or MY_TELEGRAM_ID == 0:
    print("❌ Missing TELEGRAM_BOT_TOKEN or MY_TELEGRAM_ID in backend/.env")
    sys.exit(1)

# Add backend to python path to import its core components
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))
from ailrac_core import ailrac_core_router

def ailrac_speak(text):
    """Creates a localized, thread-safe instance to voice out loud without hanging."""
    print(f"[Ailrac Speaking] {text}")
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 180)
        engine.say(text)
        engine.runAndWait()
        # Clean up the engine instance right away
        del engine
    except Exception as e:
        print(f"⚠️ Voice Output Error: {str(e)}")

def listen_to_mic():
    """Listens to the laptop microphone safely without crashing on silence."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎙️ Ailrac is listening locally... Speak now!")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=4, phrase_time_limit=8)
            print("🧠 Processing your voice...")
            spoken_text = recognizer.recognize_google(audio)
            print(f"[You Said] {spoken_text}")
            return spoken_text
        except (sr.WaitTimeoutError, sr.UnknownValueError):
            return None
        except Exception as e:
            print(f"⚠️ Mic Stream Reset: {str(e)}")
            return None

def run_voice_loop():
    """Runs the local microphone loop continuously."""
    ailrac_speak("Voice synthesis online.")
    while True:
        user_voice = listen_to_mic()
        if user_voice:
            result = ailrac_core_router(user_voice)
            ailrac_speak(result)

# ─── MASTER SYSTEM STARTUP ───
if __name__ == "__main__":
    print("🔋 Initializing Ailrac Voice Channel...")
    try:
        run_voice_loop()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down safely... Goodbye!")
        sys.exit(0)
