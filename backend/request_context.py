"""Per-request context for the active chat conversation (tool approval routing)."""

from __future__ import annotations

import contextvars
import threading
from dataclasses import dataclass, field

_conversation_id: contextvars.ContextVar[str | None] = contextvars.ContextVar(
    "conversation_id", default=None
)

_telegram_chat_id: contextvars.ContextVar[str | None] = contextvars.ContextVar(
    "telegram_chat_id", default=None
)

# Control-session state is keyed by conversation_id so concurrent requests stay isolated.
# Gemini may invoke tools on worker threads where contextvars do not propagate; callers
# should set conversation_id before entering the router (main.py / services.py).
_session_lock = threading.RLock()


@dataclass
class _ControlSession:
    python_submitted: bool = False
    launched: frozenset[str] = field(default_factory=frozenset)
    typed: tuple[str, ...] = ()


_sessions: dict[str, _ControlSession] = {}
_NO_CONVERSATION_KEY = "__no_conversation__"


def _session_key() -> str:
    conv_id = get_conversation_id()
    return conv_id if conv_id is not None else _NO_CONVERSATION_KEY


def set_conversation_id(conv_id: str | None):
    return _conversation_id.set(conv_id)


def reset_conversation_id(token) -> None:
    _conversation_id.reset(token)


def get_conversation_id() -> str | None:
    return _conversation_id.get()


def _session_key() -> str:
    return get_conversation_id() or ""


def set_telegram_chat_id(chat_id: str | None):
    return _telegram_chat_id.set(chat_id)


def reset_telegram_chat_id(token) -> None:
    _telegram_chat_id.reset(token)


def get_telegram_chat_id() -> str | None:
    return _telegram_chat_id.get()


def reset_control_session() -> None:
    """Clear per-request control-tool state for the active conversation (call once at router entry)."""
    key = _session_key()
    with _session_lock:
        _sessions[key] = _ControlSession()


def _get_session() -> _ControlSession:
    key = _session_key()
    with _session_lock:
        if key not in _sessions:
            _sessions[key] = _ControlSession()
        return _sessions[key]


def claim_python_submission() -> bool:
    """Mark script queued; return False if another tool already claimed this request."""
    with _session_lock:
        session = _get_session()
        if session.python_submitted:
            return False
        session.python_submitted = True
        return True


def was_python_submitted() -> bool:
    with _session_lock:
        return _get_session().python_submitted


def record_launch(app_name: str) -> None:
    name = (app_name or "").strip().lower()
    if not name:
        return
    with _session_lock:
        session = _get_session()
        session.launched = session.launched | {name}


def was_launched(app_name: str) -> bool:
    name = (app_name or "").strip().lower()
    with _session_lock:
        return name in _get_session().launched


def get_launched_apps() -> frozenset[str]:
    with _session_lock:
        return _get_session().launched


def record_typed(text: str) -> None:
    if not text:
        return
    with _session_lock:
        session = _get_session()
        session.typed = session.typed + (text,)


def get_typed_fragments() -> tuple[str, ...]:
    with _session_lock:
        return _get_session().typed


def skip_immediate_control_tool(tool_name: str) -> str | None:
    """Block launch/type/click tools after run_python_code queued in this request."""
    if was_python_submitted():
        return (
            f"Skipped {tool_name}: automation is handled by the run_python_code script "
            "awaiting your approval — do not duplicate actions."
        )
    return None
