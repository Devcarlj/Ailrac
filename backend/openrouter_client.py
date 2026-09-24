"""OpenRouter API client: OpenAI-compatible multi-model access with retries.

Uses the standard openai SDK pointed at https://openrouter.ai/api/v1.
Supports tool-calling (function calling) and streaming for any model
available on OpenRouter (Claude, GPT-4o, DeepSeek, Llama, etc.).
"""

from __future__ import annotations

import json
import logging
import os
import time
from typing import TypeVar

from openai import OpenAI, APIError, APITimeoutError, RateLimitError

logger = logging.getLogger("ailrac.openrouter")

T = TypeVar("T")

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_REQUEST_TIMEOUT = 120  # seconds

_client: OpenAI | None = None


def get_openrouter_client() -> OpenAI | None:
    """Return a cached OpenAI client configured for OpenRouter, or None."""
    global _client
    if _client is not None:
        return _client
    key = os.getenv("OPENROUTER_API_KEY", "").strip()
    if not key:
        return None
    _client = OpenAI(
        api_key=key,
        base_url=OPENROUTER_BASE_URL,
        timeout=OPENROUTER_REQUEST_TIMEOUT,
        default_headers={
            "HTTP-Referer": "http://localhost:5173",
            "X-Title": "Ailrac AI Assistant",
        },
    )
    return _client


def reset_openrouter_client() -> None:
    """Drop cached client (tests or API key rotation)."""
    global _client
    _client = None


def call_with_openrouter_retry(fn, *, label: str, extra_attempts: int = 2):
    """Run an OpenRouter API call with backoff on 5xx / rate-limit errors."""
    delay = 2.0
    last_exc: Exception | None = None
    for attempt in range(1 + extra_attempts):
        try:
            return fn()
        except (APIError, APITimeoutError, RateLimitError) as exc:
            last_exc = exc
            if attempt >= extra_attempts:
                raise
            logger.warning(
                "[%s] OpenRouter error (attempt %s/%s), retrying in %.1fs: %s",
                label,
                attempt + 1,
                extra_attempts + 1,
                delay,
                exc,
            )
            time.sleep(delay)
            delay = min(delay * 2, 30.0)
    if last_exc is not None:
        raise last_exc
    raise RuntimeError("call_with_openrouter_retry: unreachable")


# ─── OpenAI Function-Calling Tool Schemas ────────────────────────────────────
# These mirror the Gemini tools in ailrac_core._privileged_tools() but in
# the OpenAI function-calling JSON format used by OpenRouter.

OPENROUTER_CONTROL_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "play_spotify",
            "description": (
                "Search Spotify and mouse-click the first result to play. "
                "No Premium API needed; no approval modal."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "song_query": {
                        "type": "string",
                        "description": "Song title, artist, or search phrase.",
                    }
                },
                "required": ["song_query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "click_image",
            "description": (
                "Click a known UI element by matching a trusted local PNG template on screen. "
                "Use only static filenames from assets/ (e.g. 'submit.png')."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "template_path": {
                        "type": "string",
                        "description": "Fixed assets filename such as 'spotify_search.png'.",
                    }
                },
                "required": ["template_path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "mouse_move",
            "description": "Move the mouse cursor to absolute screen coordinates (pixels, top-left origin).",
            "parameters": {
                "type": "object",
                "properties": {
                    "x": {"type": "integer", "description": "Horizontal pixel position."},
                    "y": {"type": "integer", "description": "Vertical pixel position."},
                    "duration": {
                        "type": "number",
                        "description": "Seconds for the move animation (0 = instant). Default 0.25.",
                    },
                },
                "required": ["x", "y"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "mouse_click",
            "description": "Click the mouse at screen coordinates, or at the current cursor if x/y omitted.",
            "parameters": {
                "type": "object",
                "properties": {
                    "x": {"type": "integer", "description": "Horizontal pixel position (optional)."},
                    "y": {"type": "integer", "description": "Vertical pixel position (optional)."},
                    "click_type": {
                        "type": "string",
                        "enum": ["left", "right", "double"],
                        "description": "'left', 'right', or 'double'. Default 'left'.",
                    },
                },
                "required": [],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "run_python_code",
            "description": (
                "Submit multi-step local automation — benign scripts auto-run; risky ones need approval. "
                "Use ONE script: ailrac_launch() -> time.sleep(2-3) -> pyautogui UI (outbound only). "
                "Allowed: pyautogui, time, ailrac_launch / launch_app helpers. "
                "Forbidden: os, subprocess, sys, shutil, network, file reads, screen capture, reading .env."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string",
                        "description": "Python using pyautogui, time, ailrac_launch (no imports for ailrac_launch).",
                    }
                },
                "required": ["code"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "open_browser",
            "description": "Opens a website URL in the default web browser on the host laptop.",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "The website URL to open.",
                    }
                },
                "required": ["url"],
            },
        },
    },
]


def strip_openrouter_prefix(model_id: str) -> str:
    """Remove the 'openrouter/' prefix from a model id for the API call.

    Example: 'openrouter/anthropic/claude-3.5-sonnet' -> 'anthropic/claude-3.5-sonnet'
    """
    if model_id.startswith("openrouter/"):
        return model_id[len("openrouter/"):]
    return model_id
