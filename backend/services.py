import asyncio
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import threading
from pathlib import Path
import pyttsx3
import speech_recognition as sr
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

from database import (
    get_settings,
    update_settings,
    add_message,
    get_conversations,
    create_conversation,
    touch_conversation,
)
from ailrac_core import ailrac_core_router
from request_context import (
    set_conversation_id,
    reset_conversation_id,
    set_telegram_chat_id,
    reset_telegram_chat_id,
)
from bot_state import BotMode, get_global_mode, mode_to_api_dict, set_mode_global_and_chat

from code_approval import create_pending_approval, wait_for_approval
from telegram_approval import (
    attach_telegram_approval_handlers,
    send_approval_sync,
    telegram_post_init,
)

# Persistent Telegram reply keyboard for mode switching
MODE_REPLY_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton("🔍 Search Mode"), KeyboardButton("🎮 Control Mode")],
    ],
    resize_keyboard=True,
    is_persistent=True,
)

SEARCH_MODE_LABELS = {
    "🔍 search mode",
    "[🔍 search mode]",
    "search mode",
    "/search",
}
CONTROL_MODE_LABELS = {
    "🎮 control mode",
    "[🎮 control mode]",
    "control mode",
    "/control",
}

DANGEROUS_PATTERNS = [
    "del ",
    "rmdir",
    "rd /s",
    "format ",
    "taskkill",
    "reg delete",
    "net user",
    "cipher /w",
    "bcdedit",
    "icacls",
    "runas",
    "shutdown",
    "sfc /",
    "dism",
    "diskpart",
]

DANGEROUS_APPS = {"cmd", "powershell", "regedit", "taskmgr"}

DANGEROUS_KEYS = {"alt+f4", "ctrl+alt+del", "win+l", "win+r", "win+x"}

_BENIGN_COMMAND_RES = [
    re.compile(
        r"\b(?:open|launch|start|run)\s+(?!(?:cmd|powershell|regedit|task\s*manager)\b)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:turn|raise|lower|increase|decrease|set|change)\s+(?:the\s+)?volume\b",
        re.IGNORECASE,
    ),
    re.compile(r"\bvolume\s*(?:up|down|mute|unmute)?\b", re.IGNORECASE),
    re.compile(
        r"\b(?:mute|unmute|play|pause|skip|next|previous)\s+(?:track|song|music|spotify)?\b",
        re.IGNORECASE,
    ),
    re.compile(r"\bplay\s+(?:spotify|music|a\s+song)\b", re.IGNORECASE),
    re.compile(r"\b(?:type|write)\s+.+\b", re.IGNORECASE),
    re.compile(r"\b(?:click|move)\s+(?:the\s+)?(?:mouse|cursor)\b", re.IGNORECASE),
]

_DESTRUCTIVE_COMMAND_RES = [
    re.compile(
        r"\b(?:delete|remove|uninstall|format|wipe)\s+(?:all|my|the|this|files?|folders?|apps?|programs?)\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:shutdown|restart|reboot|lock\s+(?:my|the|pc|computer|screen))\b",
        re.IGNORECASE,
    ),
    re.compile(r"\b(?:kill|end)\s+(?:process|task)\b", re.IGNORECASE),
    re.compile(r"\bregistry\b", re.IGNORECASE),
]


def _is_benign_user_command(text: str) -> bool:
    """Common safe PC commands that should run without a Telegram approval card."""
    t = (text or "").lower().strip()
    if not t or not any(pattern.search(t) for pattern in _BENIGN_COMMAND_RES):
        return False
    if any(p in t for p in DANGEROUS_PATTERNS):
        return False
    if any(
        f"open {app}" in t or f"run {app}" in t or f"launch {app}" in t
        for app in DANGEROUS_APPS
    ):
        return False
    if any(k in t for k in DANGEROUS_KEYS):
        return False
    if any(pattern.search(t) for pattern in _DESTRUCTIVE_COMMAND_RES):
        return False
    return True


def classify_risk(text: str) -> bool:
    """
    Returns True if the command text looks dangerous enough to require approval.
    Works on raw natural language — check for intent keywords, not just exact commands.
    """
    if _is_benign_user_command(text):
        return False

    t = text.lower().strip()
    if any(p in t for p in DANGEROUS_PATTERNS):
        return True
    if any(
        f"open {app}" in t or f"run {app}" in t or f"launch {app}" in t
        for app in DANGEROUS_APPS
    ):
        return True
    if any(k in t for k in DANGEROUS_KEYS):
        return True
    if any(pattern.search(t) for pattern in _DESTRUCTIVE_COMMAND_RES):
        return True
    if any(word in t for word in ("shutdown", "restart", "reboot", "format", "taskkill")):
        return True
    return False


def build_approval_card(text: str, summary: str, precaution: str) -> str:
    """Format the message passed to send_approval_sync for dangerous PC control."""
    return (
        "🛡️ Approval Required — Ailrac PC Control\n\n"
        f"📋 What will happen:\n{summary}\n\n"
        f"🚨 Precaution:\n{precaution}\n\n"
        f'Original command: "{text}"'
    )


def get_risk_summary(text: str) -> tuple[str, str]:
    """Ask Gemini to summarize what this command will do and what the risk is."""
    from ailrac_core import GEMINI_FLASH_MODEL
    from gemini_client import call_with_server_retry, get_shared_client

    try:
        client = get_shared_client()
        if not client:
            raise RuntimeError("GEMINI_API_KEY not configured")
        prompt = (
            f'The user sent this command to a PC automation bot: "{text}"\n\n'
            "Reply ONLY with a JSON object, no markdown:\n"
            '{"summary": "one sentence: exactly what will happen on the PC", '
            '"precaution": "one sentence: the specific risk or danger, or null if safe"}'
        )
        response = call_with_server_retry(
            lambda: client.models.generate_content(
                model=GEMINI_FLASH_MODEL, contents=prompt
            ),
            label="risk_summary",
        )
        raw = response.text.strip().strip("```").lstrip("json").strip()
        data = json.loads(raw)
        summary = data.get("summary", text)
        precaution = data.get("precaution") or "This action may be irreversible."
        return summary, precaution
    except Exception as exc:
        print(f"[WARNING] get_risk_summary failed: {exc}")
        return text, "This action may be irreversible."


def _normalize_mode_label(text: str) -> str:
    return (text or "").strip().lower()


def _parse_mode_from_user_text(text: str) -> BotMode | None:
    normalized = _normalize_mode_label(text)
    if normalized in SEARCH_MODE_LABELS or normalized.endswith("search mode"):
        return BotMode.SEARCH
    if normalized in CONTROL_MODE_LABELS or normalized.endswith("control mode"):
        return BotMode.CONTROL
    return None


def _telegram_authorized(update: Update) -> bool:
    user_id = update.effective_user.id if update.effective_user else None
    my_id = int(os.getenv("MY_TELEGRAM_ID", "0"))
    return bool(user_id and user_id == my_id)


async def _reply_mode_switch(update: Update, mode: BotMode) -> None:
    if not _telegram_authorized(update):
        await update.message.reply_text("⛔ Unauthorized access. Access Denied.")
        return

    chat_id = update.effective_chat.id if update.effective_chat else None
    set_mode_global_and_chat(mode, chat_id)
    update_settings({"bot_mode": mode.value})

    if mode == BotMode.SEARCH:
        label = (
            "🔍 **Search Mode** active\n\n"
            "Web search enabled · Local OS automation fully locked."
        )
    else:
        label = (
            "🎮 **Control Mode** active\n\n"
            "Local OS access enabled · Web access fully blocked."
        )

    await update.message.reply_text(
        f"{label}\n\nRuntime: `{mode_to_api_dict()['current_mode']}`",
        reply_markup=MODE_REPLY_KEYBOARD,
        parse_mode="Markdown",
    )


async def handle_search_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await _reply_mode_switch(update, BotMode.SEARCH)


async def handle_control_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await _reply_mode_switch(update, BotMode.CONTROL)


async def handle_start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not _telegram_authorized(update):
        await update.message.reply_text("⛔ Unauthorized access. Access Denied.")
        return

    current = get_global_mode().value
    await update.message.reply_text(
        "Ailrac Telegram gateway online.\n\n"
        f"Current mode: **{current}**\n"
        "Use /search or /control, or the keyboard below.",
        reply_markup=MODE_REPLY_KEYBOARD,
        parse_mode="Markdown",
    )

# ─── VOICE REQUEST DETECTION ───

VOICE_REQUEST_PATTERNS = [
    r"\bread (it|this|that|aloud|out loud)\b",
    r"\bspeak (it|this|that|aloud)\b",
    r"\bwith your voice\b",
    r"\buse your voice\b",
    r"\bsay it out loud\b",
    r"\bvoice (it|this|that)\b",
    r"\bout loud\b",
    r"\bcan you read\b",
    r"\bplease read\b",
]

READ_LAST_MESSAGE_PATTERNS = [
    r"^read (it|that|this)( aloud| with your voice| out loud)?[.!?]?$",
    r"^speak (it|that|this)[.!?]?$",
    r"\bread (your |the )?(last|previous) (answer|message|response)\b",
    r"\bread (it |that )?with your voice\b",
    r"^can you read (it|that|this)[.!?]?$",
]


def user_requests_voice(user_input: str) -> bool:
    """True when the user explicitly asks Ailrac to read/speak aloud."""
    if not user_input:
        return False
    clean = user_input.lower().strip()
    return any(re.search(pattern, clean) for pattern in VOICE_REQUEST_PATTERNS)


def is_read_last_message_only(user_input: str) -> bool:
    """True when the user only wants the previous answer read aloud (no new AI reply)."""
    if not user_input:
        return False
    clean = user_input.lower().strip()
    return any(re.search(pattern, clean) for pattern in READ_LAST_MESSAGE_PATTERNS)


def ensure_voice_output_enabled() -> bool:
    """Turns on voice output in settings. Returns True if it was just enabled."""
    settings = get_settings()
    if not settings.get("voice_output_enabled"):
        update_settings({"voice_output_enabled": True})
        print("[INFO] Voice output auto-enabled (user requested speech).")
        return True
    return False


# ─── TTS VOICE OUTPUT ───

JARVIS_PIPER_MODEL = r"C:\Users\Lenovo\Downloads\Jarvis\jarvis-medium.onnx"


def prepare_text_for_speech(text: str) -> str:
    """Strips markdown, tags, and symbols so TTS reads the full message aloud."""
    if not text:
        return ""

    cleaned = text
    cleaned = re.sub(r"\[SCREENSHOT_TAKEN\][^\n\r]*", " ", cleaned)
    cleaned = re.sub(r"```[\s\S]*?```", " ", cleaned)
    cleaned = re.sub(r"`([^`]+)`", r"\1", cleaned)
    cleaned = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", cleaned)
    cleaned = re.sub(r"\*\*([^*]+)\*\*", r"\1", cleaned)
    cleaned = re.sub(r"\*([^*]+)\*", r"\1", cleaned)
    cleaned = re.sub(r"^#+\s*", "", cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r"^[\-\*]\s+", "", cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r"[\U0001F300-\U0001FAFF\U00002600-\U000027BF]", " ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def split_into_sentences(text: str):
    """Splits text into clean, printable sentences for TTS chunking."""
    text = re.sub(r"\n+", ". ", text)
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks = [s.strip() for s in sentences if s.strip()]
    if not chunks and text.strip():
        return [text.strip()]
    return chunks

def _speak_with_windows_sapi(speech_text: str) -> bool:
    """Uses built-in Windows SAPI — reliable for full-length speech."""
    try:
        import win32com.client

        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Rate = 0
        speaker.Volume = 100
        speaker.Speak(speech_text, 0)
        return True
    except Exception as e:
        print(f"[WARN] Windows SAPI TTS failed: {e}")
        return False


def _speak_with_piper_jarvis(speech_text: str, abort_check, controller: "TTSController") -> bool:
    """Synthesizes speech with the local Piper J.A.R.V.I.S. model and plays the WAV."""
    wav_path = None
    try:
        import winsound

        if not os.path.isfile(JARVIS_PIPER_MODEL):
            print(f"[WARN] J.A.R.V.I.S. model not found: {JARVIS_PIPER_MODEL}")
            return False

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            wav_path = tmp.name

        proc = subprocess.Popen(
            [
                sys.executable,
                "-m",
                "piper",
                "-m",
                JARVIS_PIPER_MODEL,
                "-f",
                wav_path,
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
        )
        controller.piper_process = proc

        try:
            _, stderr = proc.communicate(input=speech_text, timeout=180)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.communicate()
            print("[WARN] Piper J.A.R.V.I.S. synthesis timed out.")
            return False

        if abort_check():
            return False
        if proc.returncode != 0:
            print(f"[WARN] Piper J.A.R.V.I.S. failed: {stderr.strip()}")
            return False
        if not os.path.isfile(wav_path) or os.path.getsize(wav_path) == 0:
            print("[WARN] Piper J.A.R.V.I.S. produced no audio.")
            return False

        winsound.PlaySound(wav_path, winsound.SND_FILENAME)
        return not abort_check()
    except Exception as e:
        print(f"[WARN] Piper J.A.R.V.I.S. TTS failed: {e}")
        return False
    finally:
        controller.piper_process = None
        if wav_path and os.path.isfile(wav_path):
            try:
                os.unlink(wav_path)
            except OSError:
                pass


def _speak_one_utterance(speech_text: str, abort_check, controller: "TTSController") -> bool:
    """Speak a single phrase or sentence (used by streaming and batch TTS)."""
    if not speech_text or abort_check():
        return False

    voice_profile = get_settings().get("assistant_voice_profile", "default")

    if voice_profile == "jarvis" and not abort_check():
        if _speak_with_piper_jarvis(speech_text, abort_check, controller):
            return True

    if os.name == "nt" and not abort_check():
        if _speak_with_windows_sapi(speech_text):
            return True

    if not abort_check():
        return _speak_with_pyttsx3(speech_text, abort_check)

    return False


def _speak_with_pyttsx3(speech_text: str, abort_check) -> bool:
    """Fallback TTS via pyttsx3."""
    try:
        try:
            engine = pyttsx3.init("sapi5")
        except Exception:
            engine = pyttsx3.init()
        engine.setProperty("rate", 170)
        for chunk in split_into_sentences(speech_text):
            if abort_check():
                break
            engine.say(chunk)
        engine.runAndWait()
        try:
            engine.stop()
        except Exception:
            pass
        return True
    except Exception as e:
        print(f"[WARN] pyttsx3 TTS failed: {e}")
        return False


class TTSController:
    def __init__(self):
        self.engine = None
        self.piper_process = None
        self.lock = threading.Lock()
        self.is_speaking = False
        self.abort = False
        self.speak_generation = 0

    def speak(self, text: str, force: bool = False):
        """Speaks the full cleaned response aloud."""
        if not force:
            settings = get_settings()
            if not settings.get("voice_output_enabled"):
                return

        speech_text = prepare_text_for_speech(text)
        if not speech_text:
            print("[WARN] No speakable text after cleaning.")
            return

        self.stop()
        time.sleep(0.15)

        with self.lock:
            self.speak_generation += 1
            generation = self.speak_generation
            self.abort = False

        def run():
            try:
                with self.lock:
                    if generation != self.speak_generation:
                        return
                    self.is_speaking = True

                print(f"[Ailrac Speaking] Reading {len(speech_text)} characters.")

                def aborted():
                    with self.lock:
                        return self.abort or generation != self.speak_generation

                for chunk in split_into_sentences(speech_text):
                    if aborted():
                        break
                    _speak_one_utterance(chunk, aborted, self)

            except Exception as e:
                print(f"[ERROR] Voice Output Error: {str(e)}")
            finally:
                with self.lock:
                    if generation == self.speak_generation:
                        self.is_speaking = False
                        self.engine = None
                        self.abort = False
                print("[Ailrac Speaking] Finished speaking.")

        t = threading.Thread(target=run, daemon=True)
        t.start()

    def stop(self):
        """Immediately stops the TTS engine (does not cancel a pending new speak)."""
        with self.lock:
            self.abort = True
            if self.piper_process:
                try:
                    self.piper_process.terminate()
                except Exception as e:
                    print(f"[ERROR] Stopping Piper process failed: {e}")
                self.piper_process = None
            if self.engine:
                try:
                    self.engine.stop()
                except Exception as e:
                    print(f"[ERROR] Stopping engine failed: {e}")
            self.is_speaking = False
        if os.name == "nt":
            try:
                import winsound

                winsound.PlaySound(None, winsound.SND_PURGE)
            except Exception:
                pass

tts_controller = TTSController()


def ailrac_speak(
    text: str,
    user_input: str = None,
    force: bool = False,
    *,
    skip_if_streamed: bool = False,
):
    """Speaks text. Auto-enables voice output when the user asks to read aloud."""
    if skip_if_streamed:
        try:
            from streaming_tts import streaming_tts_used_audio

            if streaming_tts_used_audio():
                return
        except ImportError:
            pass

    should_force = force
    if user_input and user_requests_voice(user_input):
        ensure_voice_output_enabled()
        should_force = True
    tts_controller.speak(text, force=should_force)


def start_response_streaming_tts(*, force: bool = False):
    """Begin streaming TTS for the active request (non-blocking)."""
    from streaming_tts import begin_streaming_tts

    return begin_streaming_tts(force=force)


def stop_response_streaming_tts(token) -> None:
    from streaming_tts import end_streaming_tts

    end_streaming_tts(token)


def try_read_last_assistant_message(user_input: str, conversation_id: str) -> bool:
    """If the user only wants the last answer read aloud, speak it and return True."""
    if not conversation_id or not is_read_last_message_only(user_input):
        return False

    from database import get_messages

    messages = get_messages(conversation_id)
    last_assistant = None
    for msg in reversed(messages):
        if msg["role"] == "assistant":
            last_assistant = msg
            break

    if not last_assistant:
        return False

    ensure_voice_output_enabled()
    ailrac_speak(last_assistant["content"], user_input=user_input, force=True)
    return True


# ─── HELPER FOR PERSISTENCE ───

def get_or_create_conversation(channel_name: str) -> str:
    """Finds the most recently active conversation to append to, or creates a new one."""
    convs = get_conversations()
    if convs:
        latest = convs[0]
        # If updated within the last 30 minutes, reuse it
        try:
            updated_at = datetime.fromisoformat(latest["updated_at"])
            delta = datetime.utcnow() - updated_at
            if delta.total_seconds() < 1800:
                return latest["id"]
        except Exception:
            pass
    
    # Create new conversation
    title = f"{channel_name} Session - {datetime.now().strftime('%b %d, %H:%M')}"
    new_conv = create_conversation(title)
    return new_conv["id"]


# ─── MICROPHONE VOICE INPUT LOOP ───

def listen_to_mic():
    """Listens to the local microphone safely and returns recognized text."""
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            # Short listen timeout and phrase limit to keep it responsive
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=8)
            spoken_text = recognizer.recognize_google(audio)
            return spoken_text
    except (sr.WaitTimeoutError, sr.UnknownValueError):
        return None
    except Exception as e:
        # Avoid flood of logs if mic is temporarily busy
        time.sleep(1)
        return None

def voice_input_worker():
    """Continuously runs the mic listener if voice input is enabled."""
    print("[INFO] Local Voice Input service initialized.")
    while True:
        try:
            settings = get_settings()
            if settings.get("voice_input_enabled"):
                print("\n[INFO] Ailrac is listening locally... Speak now!")
                user_voice = listen_to_mic()
                if user_voice:
                    print(f"[You Said] {user_voice}")
                    
                    # 1. Get or create active conversation
                    conv_id = get_or_create_conversation("Voice")
                    
                    # 2. Persist user voice message
                    add_message(conv_id, "user", user_voice)
                    
                    # 3. Fetch history for AI context
                    from database import get_messages
                    all_msgs = get_messages(conv_id)
                    history_for_ai = [
                        {"role": m["role"], "content": m["content"]}
                        for m in all_msgs[:-1]
                    ]
                    
                    # 4. Generate AI response (stream tokens to TTS while model runs)
                    stream_token = start_response_streaming_tts(force=True)
                    ctx_token = set_conversation_id(conv_id)
                    try:
                        ai_response = ailrac_core_router(user_voice, history_for_ai)
                    finally:
                        reset_conversation_id(ctx_token)
                        stop_response_streaming_tts(stream_token)

                    # 5. Persist assistant message
                    add_message(conv_id, "assistant", ai_response)
                    touch_conversation(conv_id)

                    # 6. Speak any remainder not already streamed
                    ailrac_speak(
                        ai_response,
                        user_input=user_voice,
                        skip_if_streamed=True,
                    )
            else:
                # Sleep and wait if disabled
                time.sleep(2)
        except Exception as e:
            print(f"[ERROR] Voice Input loop error: {e}")
            time.sleep(3)


# ─── TELEGRAM CHANNEL HANDLERS ───

async def handle_telegram_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Processes incoming Telegram bot messages."""
    settings = get_settings()
    if not settings.get("telegram_enabled"):
        # If disabled in settings, ignore or politely decline
        return

    user_id = update.message.from_user.id
    my_id = int(os.getenv("MY_TELEGRAM_ID", "0"))

    if user_id != my_id:
        await update.message.reply_text("⛔ Unauthorized access. Access Denied.")
        return

    incoming_text = update.message.text
    if not incoming_text:
        return

    print(f"[Telegram] Received Command: '{incoming_text}'")

    mode_switch = _parse_mode_from_user_text(incoming_text)
    if mode_switch is not None:
        await _reply_mode_switch(update, mode_switch)
        return

    if classify_risk(incoming_text):
        summary, precaution = await asyncio.to_thread(get_risk_summary, incoming_text)
        card = build_approval_card(incoming_text, summary, precaution)

        approval_id = create_pending_approval(
            code=card,
            conversation_id=str(user_id),
            dispatch_on_approve=False,
        )
        send_approval_sync(approval_id, card)

        await update.message.reply_text(
            f"⏳ *Approval required*\n\n"
            f"📋 {summary}\n\n"
            f"🚨 {precaution or 'Proceed with caution.'}\n\n"
            f"Check Telegram for the approval card. Auto-cancels in 30s.",
            parse_mode="Markdown",
            reply_markup=MODE_REPLY_KEYBOARD,
        )

        approved = await asyncio.to_thread(wait_for_approval, approval_id, 30)

        if not approved:
            await update.message.reply_text(
                "❌ Action cancelled or timed out.",
                reply_markup=MODE_REPLY_KEYBOARD,
            )
            return

        await update.message.reply_text(
            "✅ Approved — executing...",
            reply_markup=MODE_REPLY_KEYBOARD,
        )

    try:
        # 1. Get or create active conversation
        conv_id = get_or_create_conversation("Telegram")
        
        # 2. Persist user message
        add_message(conv_id, "user", incoming_text)
        
        # 3. Fetch context history
        from database import get_messages
        all_msgs = get_messages(conv_id)
        history_for_ai = [
            {"role": m["role"], "content": m["content"]}
            for m in all_msgs[:-1]
        ]
        
        # 4. Generate AI response (mode from bot_state; chat_id for per-session override)
        chat_id = update.effective_chat.id if update.effective_chat else None
        stream_token = start_response_streaming_tts(
            force=bool(settings.get("voice_output_enabled"))
        )
        ctx_conv = set_conversation_id(conv_id)
        ctx_chat = set_telegram_chat_id(str(chat_id) if chat_id is not None else None)
        try:
            ai_response = await asyncio.to_thread(
                ailrac_core_router,
                incoming_text,
                history_for_ai,
                chat_id=chat_id,
            )
        finally:
            reset_telegram_chat_id(ctx_chat)
            reset_conversation_id(ctx_conv)
            stop_response_streaming_tts(stream_token)
        
        # 5. Persist response (skip empty — script approval card is the UI)
        if ai_response and ai_response.strip():
            add_message(conv_id, "assistant", ai_response)
        touch_conversation(conv_id)
        
        # 6. Send reply back to Telegram
        screenshot_path = None
        clean_response = (ai_response or "").strip()
        
        if "[SCREENSHOT_TAKEN]" in ai_response:
            match = re.search(r"\[SCREENSHOT_TAKEN\]\s*([^\n\r]+)", ai_response)
            if match:
                screenshot_path = match.group(1).strip()
                # Clean up any trailing space or punctuation from python path parsing
                screenshot_path = screenshot_path.strip().rstrip(".").rstrip("\"").rstrip("'")
                clean_response = ai_response.replace(match.group(0), "").strip()
            else:
                clean_response = ai_response.replace("[SCREENSHOT_TAKEN]", "").strip()
                backend_dir = os.path.dirname(os.path.abspath(__file__))
                screenshot_path = os.path.join(backend_dir, "temp_screenshot.png")
        
        if clean_response:
            await update.message.reply_text(
                clean_response,
                reply_markup=MODE_REPLY_KEYBOARD,
            )
            
        if screenshot_path and os.path.exists(screenshot_path):
            try:
                with open(screenshot_path, "rb") as photo_file:
                    await update.message.reply_photo(photo=photo_file)
            except Exception as photo_err:
                print(f"[ERROR] Failed to send Telegram photo: {photo_err}")
                if not clean_response:
                    await update.message.reply_text("❌ Failed to load screenshot.")
        
        # 7. Speak response locally on host PC (without screenshot tag)
        if clean_response:
            ailrac_speak(
                clean_response,
                user_input=incoming_text,
                skip_if_streamed=True,
            )

    except Exception as e:
        print(f"[ERROR] Error handling Telegram message: {e}")
        await update.message.reply_text(f"❌ Error processing request: {e}")

_telegram_lock_handle = None
_background_services_started = False


def _acquire_telegram_gateway_lock() -> bool:
    """Only one process may poll Telegram (prevents duplicate replies / double exec)."""
    global _telegram_lock_handle
    lock_path = Path(__file__).resolve().parent / ".telegram_gateway.lock"
    try:
        handle = open(lock_path, "w")
        if sys.platform == "win32":
            import msvcrt

            msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl

            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        handle.write(str(os.getpid()))
        handle.flush()
        _telegram_lock_handle = handle
        return True
    except OSError:
        try:
            handle.close()
        except Exception:
            pass
        return False


def run_telegram_loop():
    """Runs the Telegram gateway polling listener."""
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token or "your_" in token or ":" not in token:
        print("[WARNING] Telegram BOT_TOKEN is missing or placeholder. Telegram service inactive.")
        return

    if not _acquire_telegram_gateway_lock():
        print(
            "[WARNING] Telegram gateway already running in another Ailrac process — "
            "skipping duplicate poller (fixes double messages/actions)."
        )
        return

    print("[INFO] Initializing Telegram Gateway...")
    try:
        app = (
            Application.builder()
            .token(token)
            .post_init(telegram_post_init)
            .build()
        )
        attach_telegram_approval_handlers(app)
        app.add_handler(CommandHandler("start", handle_start_command))
        app.add_handler(CommandHandler("search", handle_search_command))
        app.add_handler(CommandHandler("control", handle_control_command))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_telegram_message))
        print("📱 Telegram Gateway ONLINE.")
        app.run_polling(close_loop=False)
    except Exception as e:
        print(f"[ERROR] Telegram Gateway failed to start: {e}")


# ─── SERVICES INTERFACE ───

def start_background_services():
    """Starts background threads for mic listening and Telegram bot."""
    global _background_services_started
    if _background_services_started:
        return
    _background_services_started = True

    # Voice input thread
    voice_thread = threading.Thread(target=voice_input_worker, daemon=True)
    voice_thread.start()

    # Telegram thread
    telegram_thread = threading.Thread(target=run_telegram_loop, daemon=True)
    telegram_thread.start()
