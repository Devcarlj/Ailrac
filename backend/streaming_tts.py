"""
Streaming TTS — decoupled from HTTP response, SQLite persistence, and UI delivery.

Token deltas from the LLM are fed into a background worker that speaks complete
phrases/sentences as soon as they are available (Piper J.A.R.V.I.S. or system voice).
"""

from __future__ import annotations

import contextvars
import queue
import re
import threading
from typing import Any

from database import get_settings

_stream_session: contextvars.ContextVar["StreamingTTSSession | None"] = contextvars.ContextVar(
    "streaming_tts_session", default=None
)

_active_session_lock = threading.Lock()
_active_session: "StreamingTTSSession | None" = None

_SENTINEL = object()

# Speak first phrase early (before a full sentence terminator) for lower latency.
_EARLY_MIN_CHARS = 28
_EARLY_MIN_WORDS = 5
_EARLY_MAX_WORDS = 10


class StreamingTTSSession:
    """Per-request streaming speech session with a background playback queue."""

    def __init__(self, controller: Any, *, force: bool = False):
        self.controller = controller
        self.force = force
        self.buffer = ""
        self._queued_any = False
        self._closed = False
        self._generation = 0
        self._q: queue.Queue = queue.Queue()
        self._worker: threading.Thread | None = None
        self._lock = threading.Lock()

    @property
    def fed_any_audio(self) -> bool:
        return self._queued_any

    def _voice_enabled(self) -> bool:
        if self.force:
            return True
        return bool(get_settings().get("voice_output_enabled"))

    def start(self) -> None:
        self.controller.stop()
        with self.controller.lock:
            self.controller.speak_generation += 1
            gen = self.controller.speak_generation
            self.controller.abort = False
            self.controller.is_speaking = True
        self._generation = gen
        self._worker = threading.Thread(
            target=self._run_worker, args=(gen,), daemon=True, name="streaming-tts"
        )
        self._worker.start()

    def feed(self, delta: str) -> None:
        if not delta or self._closed or not self._voice_enabled():
            return
        with self._lock:
            self.buffer += delta
            self._enqueue_ready_chunks()

    def finish(self) -> None:
        if self._closed:
            return
        self._closed = True
        with self._lock:
            self._flush_remainder()
        self._q.put(_SENTINEL)

    def cancel(self) -> None:
        self._closed = True
        self.controller.stop()
        while True:
            try:
                self._q.get_nowait()
            except queue.Empty:
                break
        self._q.put(_SENTINEL)

    def _enqueue_sentence(self, raw: str) -> None:
        from services import prepare_text_for_speech

        cleaned = prepare_text_for_speech(raw)
        if not cleaned:
            return
        self._queued_any = True
        self._q.put(cleaned)
        preview = cleaned if len(cleaned) <= 72 else cleaned[:72] + "..."
        print(f"[Stream TTS] Queued ({len(cleaned)} chars): {preview}")

    def _enqueue_ready_chunks(self) -> None:
        # Complete sentences first (. ! ?)
        while True:
            m = re.search(r"(.+?[.!?])(?:\s+|\n+|$)", self.buffer, re.DOTALL)
            if not m:
                break
            sentence = m.group(1).strip()
            self.buffer = self.buffer[m.end() :]
            self._enqueue_sentence(sentence)

        if self._queued_any:
            return

        # Early first phrase so the user hears audio before the full reply finishes.
        stripped = self.buffer.rstrip()
        if len(stripped) < _EARLY_MIN_CHARS:
            return
        if not self.buffer.endswith((" ", "\n", ",", ";", ":", "!", "?", ".")):
            return

        words = stripped.split()
        if len(words) < _EARLY_MIN_WORDS:
            return

        take = min(_EARLY_MAX_WORDS, len(words))
        phrase = " ".join(words[:take])
        if len(phrase) < _EARLY_MIN_CHARS and take < len(words):
            take = min(take + 2, len(words))
            phrase = " ".join(words[:take])

        remainder = words[take:]
        self.buffer = (" ".join(remainder) + " ") if remainder else ""
        self._enqueue_sentence(phrase)

    def _flush_remainder(self) -> None:
        tail = self.buffer.strip()
        self.buffer = ""
        if tail:
            self._enqueue_sentence(tail)

    def _run_worker(self, generation: int) -> None:
        from services import _speak_one_utterance

        def aborted() -> bool:
            with self.controller.lock:
                return (
                    self.controller.abort
                    or generation != self.controller.speak_generation
                )

        try:
            while True:
                try:
                    item = self._q.get(timeout=0.25)
                except queue.Empty:
                    if self._closed and self._q.empty():
                        break
                    continue

                if item is _SENTINEL:
                    break
                if aborted():
                    break

                with self.controller.lock:
                    self.controller.is_speaking = True

                _speak_one_utterance(str(item), aborted, self.controller)

        except Exception as exc:
            print(f"[ERROR] Streaming TTS worker failed: {exc}")
        finally:
            _clear_active_session_if(self)
            with self.controller.lock:
                if generation == self.controller.speak_generation:
                    self.controller.is_speaking = False
                    self.controller.abort = False
            print("[Stream TTS] Playback worker finished.")


def _set_active_session(session: "StreamingTTSSession | None") -> None:
    global _active_session
    with _active_session_lock:
        _active_session = session


def _clear_active_session_if(session: "StreamingTTSSession") -> None:
    global _active_session
    with _active_session_lock:
        if _active_session is session:
            _active_session = None


def stop_all_streaming_tts() -> None:
    """Cancel the globally active streaming session (e.g. user clicked Stop Speaking)."""
    with _active_session_lock:
        session = _active_session
        _active_session = None
    if session is not None:
        session.cancel()


def begin_streaming_tts(*, force: bool = False):
    """Start a streaming TTS session for the current request context."""
    if not force and not get_settings().get("voice_output_enabled"):
        return None

    from services import tts_controller

    session = StreamingTTSSession(tts_controller, force=force)
    session.start()
    _set_active_session(session)
    return _stream_session.set(session)


def end_streaming_tts(token) -> None:
    """Flush remaining text and let the background worker finish queued audio."""
    try:
        session = _stream_session.get()
        if session is not None:
            session.finish()
    finally:
        if token is not None:
            _stream_session.reset(token)


def cancel_streaming_tts(token) -> None:
    try:
        session = _stream_session.get()
        if session is not None:
            session.cancel()
    finally:
        if token is not None:
            _stream_session.reset(token)


def is_streaming_tts_active() -> bool:
    session = _stream_session.get()
    return session is not None and not session._closed


def feed_streaming_tts(delta: str) -> None:
    session = _stream_session.get()
    if session is not None and not session._closed and delta:
        session.feed(delta)


def streaming_tts_used_audio() -> bool:
    session = _stream_session.get()
    return bool(session and session.fed_any_audio)
