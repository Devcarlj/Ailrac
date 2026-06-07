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

T = TypeVar("T")


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
    key = (api_key or os.getenv("GEMINI_API_KEY") or "").strip()
    if not key:
        return None
    return genai.Client(api_key=key, http_options=default_http_options())


def get_shared_client() -> genai.Client | None:
    global _client
    if _client is None:
        _client = create_genai_client()
    return _client


def reset_shared_client() -> None:
    """Drop cached client (tests or API key rotation)."""
    global _client
    _client = None


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
