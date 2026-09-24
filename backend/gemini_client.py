"""Shared Gemini API client: timeouts, SDK retries, and app-level 500 recovery."""

from __future__ import annotations

import logging
import os
import time
from collections.abc import Callable
from typing import TypeVar

from google import genai
from google.genai import types
from google.genai.errors import ServerError

logger = logging.getLogger("ailrac.gemini")

# Short client timeouts can surface as misleading 500 INTERNAL responses.
GEMINI_REQUEST_TIMEOUT_MS = 120_000

_client: genai.Client | None = None
_client_configuration_error: str | None = None

T = TypeVar("T")

_AI_STUDIO_KEY_URL = "https://aistudio.google.com/apikey"


def normalize_gemini_api_key(raw: str) -> str:
    """Strip whitespace and optional quoting from .env values."""
    key = (raw or "").strip()
    if len(key) >= 2 and key[0] == key[-1] and key[0] in "\"'":
        key = key[1:-1].strip()
    return key


def gemini_api_key_configuration_error(key: str) -> str | None:
    """Return a user-safe message when *key* is missing or the wrong credential type."""
    if not key:
        return "GEMINI_API_KEY is not configured in backend/.env."
    lower = key.lower()
    if lower.startswith("bearer "):
        key = key[7:].strip()
        lower = key.lower()
    if key.startswith(("ya29.", "AQ.")):
        return (
            "GEMINI_API_KEY is an OAuth access token (from gcloud auth or a Google login), "
            f"not a Gemini API key. Create an API key at {_AI_STUDIO_KEY_URL} "
            "and set GEMINI_API_KEY in backend/.env, then restart the backend."
        )
    if key.startswith("eyJ"):
        return (
            "GEMINI_API_KEY looks like a JWT or service-account token, not a Gemini API key. "
            f"Use an API key from {_AI_STUDIO_KEY_URL} instead."
        )
    if key.startswith("sk-or-"):
        return (
            "GEMINI_API_KEY looks like an OpenRouter key. "
            "Put it in OPENROUTER_API_KEY and use a Gemini key from "
            f"{_AI_STUDIO_KEY_URL} for GEMINI_API_KEY."
        )
    if not key.startswith("AIza"):
        logger.warning(
            "GEMINI_API_KEY does not start with AIza; if Gemini returns 401, "
            "replace it with a key from Google AI Studio."
        )
    return None


def format_gemini_user_error(exc: Exception) -> str:
    """Turn SDK/auth failures into actionable setup guidance."""
    text = str(exc)
    upper = text.upper()
    if "ACCESS_TOKEN_TYPE_UNSUPPORTED" in upper or (
        "401" in text and "UNAUTHENTICATED" in upper
    ):
        return (
            "Invalid Gemini credentials: an OAuth access token was used instead of an API key. "
            f"Create a key at {_AI_STUDIO_KEY_URL}, set GEMINI_API_KEY in backend/.env, "
            "and restart the backend."
        )
    if "401" in text and ("UNAUTHENTICATED" in upper or "invalid authentication" in text.lower()):
        return (
            "Gemini authentication failed (401). Verify GEMINI_API_KEY in backend/.env is a "
            f"current key from {_AI_STUDIO_KEY_URL}, then restart the backend."
        )
    return text


def default_http_options() -> types.HttpOptions:
    return types.HttpOptions(
        timeout=GEMINI_REQUEST_TIMEOUT_MS,
        retry_options=types.HttpRetryOptions(
            attempts=5,
            initial_delay=1.0,
            max_delay=60.0,
            http_status_codes=[408, 429, 500, 502, 503, 504],
        ),
    )


def create_genai_client(api_key: str | None = None) -> genai.Client | None:
    global _client_configuration_error
    key = normalize_gemini_api_key(api_key or os.getenv("GEMINI_API_KEY") or "")
    config_err = gemini_api_key_configuration_error(key)
    if config_err:
        _client_configuration_error = config_err
        return None
    _client_configuration_error = None
    return genai.Client(api_key=key, http_options=default_http_options())


def get_shared_client() -> genai.Client | None:
    global _client
    if _client is None:
        _client = create_genai_client()
    return _client


def reset_shared_client() -> None:
    """Drop cached client (tests or API key rotation)."""
    global _client, _client_configuration_error
    _client = None
    _client_configuration_error = None


def get_client_configuration_error() -> str | None:
    """Return a safe, actionable explanation when the Gemini client is unavailable."""
    if _client is not None:
        return None
    if _client_configuration_error is None:
        create_genai_client()
    return _client_configuration_error


def call_with_server_retry(
    fn: Callable[[], T],
    *,
    label: str,
    extra_attempts: int = 2,
) -> T:
    """
    Run a Gemini API call with extra backoff when Google still returns 500
    after the SDK's built-in HTTP retries.
    """
    delay = 2.0
    last_exc: ServerError | None = None
    for attempt in range(1 + extra_attempts):
        try:
            return fn()
        except ServerError as exc:
            last_exc = exc
            if attempt >= extra_attempts:
                raise
            logger.warning(
                "[%s] Gemini server error (attempt %s/%s), retrying in %.1fs: %s",
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
    raise RuntimeError("call_with_server_retry: unreachable")
