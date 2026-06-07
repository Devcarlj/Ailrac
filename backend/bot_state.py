"""Thread-safe dual-mode execution state (Search vs Control)."""

from __future__ import annotations

import threading
from enum import Enum
from typing import Dict, Optional, Union

ChatId = Union[int, str]


class BotMode(str, Enum):
    SEARCH = "search"
    CONTROL = "control"

    @classmethod
    def from_value(cls, value: str) -> "BotMode":
        normalized = (value or "").strip().lower()
        if normalized in ("search", "s"):
            return cls.SEARCH
        if normalized in ("control", "c"):
            return cls.CONTROL
        raise ValueError(f"Invalid bot mode: {value!r}. Use 'search' or 'control'.")


_lock = threading.RLock()
_global_mode: BotMode = BotMode.SEARCH
_chat_modes: Dict[str, BotMode] = {}


def _normalize_chat_id(chat_id: Optional[ChatId]) -> Optional[str]:
    if chat_id is None:
        return None
    return str(chat_id)


def get_global_mode() -> BotMode:
    """Returns the global default mode (web dashboard and new sessions)."""
    with _lock:
        return _global_mode


def set_global_mode(mode: BotMode) -> BotMode:
    """Sets the global mode; does not remove per-chat overrides."""
    global _global_mode
    if not isinstance(mode, BotMode):
        mode = BotMode.from_value(str(mode))
    with _lock:
        _global_mode = mode
        return _global_mode


def get_mode(chat_id: Optional[ChatId] = None) -> BotMode:
    """Alias for effective mode: per-chat override or global default."""
    return get_effective_mode(chat_id)


def get_effective_mode(chat_id: Optional[ChatId] = None) -> BotMode:
    with _lock:
        key = _normalize_chat_id(chat_id)
        if key and key in _chat_modes:
            return _chat_modes[key]
        return _global_mode


def set_mode(mode: BotMode, chat_id: Optional[ChatId] = None) -> BotMode:
    """
    Sets mode for a specific chat, or the global default when chat_id is None.
    Telegram /search and /control update global mode so the dashboard stays in sync.
    """
    if not isinstance(mode, BotMode):
        mode = BotMode.from_value(str(mode))

    key = _normalize_chat_id(chat_id)
    with _lock:
        if key is None:
            global _global_mode
            _global_mode = mode
            return _global_mode
        _chat_modes[key] = mode
        return _chat_modes[key]


def set_mode_global_and_chat(mode: BotMode, chat_id: Optional[ChatId] = None) -> BotMode:
    """Updates global runtime state and optional chat override (Telegram sync)."""
    set_global_mode(mode)
    if chat_id is not None:
        set_mode(mode, chat_id)
    return get_global_mode()


def clear_chat_mode(chat_id: ChatId) -> None:
    key = _normalize_chat_id(chat_id)
    if not key:
        return
    with _lock:
        _chat_modes.pop(key, None)


def mode_to_api_dict() -> dict:
    return {"current_mode": get_global_mode().value}


def parse_mode_request(value: str) -> BotMode:
    return BotMode.from_value(value)
