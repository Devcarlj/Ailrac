import logging
import os
import sys
from pathlib import Path
from typing import Dict, Any

# Configure console encoding to prevent UnicodeEncodeError on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

from dotenv import load_dotenv

# Load .env before any other imports that use env vars
load_dotenv(Path(__file__).parent / ".env")

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from models import (
    ChatRequest,
    RenameRequest,
    ExecutionApproveRequest,
    PendingExecutionResponse,
    BotModeUpdateRequest,
)
from bot_state import (
    BotMode,
    get_global_mode,
    mode_to_api_dict,
    parse_mode_request,
    set_global_mode,
)
from request_context import set_conversation_id, reset_conversation_id
from code_approval import get_pending_approval, resolve_approval
from database import (
    init_db,
    create_conversation,
    get_conversations,
    get_conversation,
    delete_conversation,
    add_message,
    get_messages,
    get_settings,
    update_settings,
    update_conversation_title,
    touch_conversation,
)
from ailrac_core import ailrac_core_router
from services import (
    start_background_services,
    ailrac_speak,
    tts_controller,
    try_read_last_assistant_message,
    user_requests_voice,
    ensure_voice_output_enabled,
    start_response_streaming_tts,
    stop_response_streaming_tts,
)
from streaming_tts import stop_all_streaming_tts

app = FastAPI(title="Ailrac AI Backend", version="2.0.0")

# Allow the React dev server to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def _sync_bot_mode_from_db() -> None:
    """Restore persisted mode into the in-memory execution engine."""
    try:
        stored = get_settings().get("bot_mode", "search")
        set_global_mode(parse_mode_request(stored))
    except ValueError:
        set_global_mode(BotMode.SEARCH)


@app.on_event("startup")
def startup():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    )
    init_db()
    _sync_bot_mode_from_db()
    from gemini_client import get_client_configuration_error, get_shared_client

    get_shared_client()
    gemini_err = get_client_configuration_error()
    if gemini_err:
        print(f"[WARNING] Gemini unavailable: {gemini_err}")
    start_background_services()
    print("[INFO] Ailrac Backend v2.0 is running at http://localhost:8000")
    print("[INFO] API docs available at http://localhost:8000/docs")


# ─── HEALTH ───

@app.get("/api/health")
def health():
    return {"status": "ok", "version": "2.0.0"}


# ─── CHAT ───

@app.post("/api/chat")
def chat(req: ChatRequest):
    """Send a message, get an AI response. Creates a new conversation if needed."""
    if not req.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    conv_id = req.conversation_id
    is_new = False

    if not conv_id:
        # Auto-title from the first message
        title = req.message[:60] + ("..." if len(req.message) > 60 else "")
        conv = create_conversation(title)
        conv_id = conv["id"]
        is_new = True
    else:
        conv = get_conversation(conv_id)
        if not conv:
            raise HTTPException(status_code=404, detail="Conversation not found.")

    # Persist user message
    user_msg = add_message(conv_id, "user", req.message)

    # User only wants the previous answer read aloud — no new AI generation
    if try_read_last_assistant_message(req.message, conv_id):
        touch_conversation(conv_id)
        all_msgs = get_messages(conv_id)
        last_assistant = next(
            (m for m in reversed(all_msgs) if m["role"] == "assistant"), None
        )
        settings = get_settings()
        return {
            "conversation_id": conv_id,
            "is_new_conversation": is_new,
            "user_message": user_msg,
            "assistant_message": last_assistant,
            "conversation": get_conversation(conv_id),
            "settings": settings,
            "speak_started": True,
            "read_aloud_only": True,
        }

    # Fetch history BEFORE the message we just added (exclude it from context)
    all_msgs = get_messages(conv_id)
    history_for_ai = [
        {"role": m["role"], "content": m["content"]}
        for m in all_msgs[:-1]  # exclude the just-added user message
    ]

    voice_requested = user_requests_voice(req.message)
    if voice_requested:
        ensure_voice_output_enabled()

    settings = get_settings()
    speak_started = voice_requested or settings.get("voice_output_enabled")
    stream_token = (
        start_response_streaming_tts(force=voice_requested) if speak_started else None
    )

    # Run through the Ailrac brain (conversation id for UI code-approval routing)
    ctx_token = set_conversation_id(conv_id)
    try:
        ai_response = ailrac_core_router(req.message, history_for_ai)
    finally:
        reset_conversation_id(ctx_token)
        stop_response_streaming_tts(stream_token)

    # Persist AI response (skip empty when automation was queued to Telegram only)
    ai_msg = None
    if ai_response and ai_response.strip():
        ai_msg = add_message(conv_id, "assistant", ai_response)

    # Bump the conversation's updated_at timestamp
    touch_conversation(conv_id)

    # Batch-speak only if streaming TTS did not already play the response
    if ai_response and ai_response.strip():
        ailrac_speak(
            ai_response,
            user_input=req.message,
            force=voice_requested,
            skip_if_streamed=True,
        )

    return {
        "conversation_id": conv_id,
        "is_new_conversation": is_new,
        "user_message": user_msg,
        "assistant_message": ai_msg,
        "conversation": get_conversation(conv_id),
        "settings": settings,
        "speak_started": speak_started,
    }


# ─── CONVERSATIONS ───

@app.get("/api/conversations")
def list_conversations():
    return get_conversations()


@app.get("/api/conversations/{conv_id}")
def get_conv(conv_id: str):
    conv = get_conversation(conv_id)
    if not conv:
        raise HTTPException(status_code=404, detail="Conversation not found.")
    return conv


@app.get("/api/conversations/{conv_id}/messages")
def list_messages(conv_id: str):
    conv = get_conversation(conv_id)
    if not conv:
        raise HTTPException(status_code=404, detail="Conversation not found.")
    return get_messages(conv_id)


@app.delete("/api/conversations/{conv_id}")
def delete_conv(conv_id: str):
    conv = get_conversation(conv_id)
    if not conv:
        raise HTTPException(status_code=404, detail="Conversation not found.")
    delete_conversation(conv_id)
    return {"ok": True}


@app.patch("/api/conversations/{conv_id}")
def rename_conv(conv_id: str, req: RenameRequest):
    conv = get_conversation(conv_id)
    if not conv:
        raise HTTPException(status_code=404, detail="Conversation not found.")
    update_conversation_title(conv_id, req.title)
    return get_conversation(conv_id)


# ─── SETTINGS ───

@app.get("/api/settings")
def read_settings():
    return get_settings()


@app.put("/api/settings")
def write_settings(updates: Dict[str, Any]):
    update_settings(updates)
    return get_settings()


@app.get("/api/settings/mode")
def read_bot_mode():
    """Current global dual-mode execution state."""
    return mode_to_api_dict()


@app.post("/api/settings/mode")
def write_bot_mode(req: BotModeUpdateRequest):
    """Instantly switch Search vs Control for the whole runtime engine."""
    try:
        mode = parse_mode_request(req.mode)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    set_global_mode(mode)
    update_settings({"bot_mode": mode.value})
    return mode_to_api_dict()


# ─── CODE EXECUTION APPROVAL (human-in-the-loop UI) ───

@app.get("/api/execution/pending", response_model=PendingExecutionResponse)
def execution_pending():
    """Returns the script awaiting user approval while /api/chat is in progress."""
    pending = get_pending_approval()
    if not pending:
        return PendingExecutionResponse(pending=False)
    return PendingExecutionResponse(
        pending=True,
        id=pending["id"],
        code=pending["code"],
        conversation_id=pending.get("conversation_id"),
        created_at=pending.get("created_at"),
    )


@app.post("/api/execution/{approval_id}/approve")
def execution_approve(approval_id: str, body: ExecutionApproveRequest):
    if body.confirm.strip() != "y":
        raise HTTPException(
            status_code=400,
            detail="Type confirm exactly 'y' to approve execution.",
        )
    if not resolve_approval(approval_id, approved=True):
        raise HTTPException(status_code=404, detail="No pending execution with that id.")
    return {"status": "approved", "id": approval_id, "running_in_background": True}


@app.post("/api/execution/{approval_id}/deny")
def execution_deny(approval_id: str):
    if not resolve_approval(approval_id, approved=False):
        raise HTTPException(status_code=404, detail="No pending execution with that id.")
    return {"status": "denied", "id": approval_id}


# ─── VOICE CONTROL ───

@app.get("/api/voice/status")
def voice_status():
    return {"is_speaking": tts_controller.is_speaking}


@app.post("/api/voice/stop")
def voice_stop():
    stop_all_streaming_tts()
    tts_controller.stop()
    return {"status": "stopped"}


@app.post("/api/voice/speak")
def voice_speak(payload: Dict[str, Any]):
    """Read arbitrary text aloud; auto-enables voice output."""
    text = (payload.get("text") or "").strip()
    if not text:
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    ensure_voice_output_enabled()
    ailrac_speak(text, force=True)
    return {"status": "speaking", "settings": get_settings()}


if __name__ == "__main__":
    # reload=True spawns a reloader parent that can confuse background services
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
