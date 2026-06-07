"""
Telegram inline-keyboard approval for pending automation scripts.
Delivers markdown code blocks to MY_TELEGRAM_ID with Approve / Reject buttons.
"""

from __future__ import annotations

import asyncio
import json
import logging
import os
import queue
import re
import urllib.error
import urllib.request
from typing import Any, Optional

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, ContextTypes

from code_approval import resolve_approval

logger = logging.getLogger("ailrac.telegram_approval")

CALLBACK_APPROVE_PREFIX = "ailrac_exec:approve:"
CALLBACK_DENY_PREFIX = "ailrac_exec:deny:"

_outbox: queue.Queue[dict[str, Any]] = queue.Queue()
_application: Optional[Application] = None
# Prevent duplicate approval cards (sync HTTP send + outbox retry for the same id).
_sent_approval_ids: set[str] = set()


def format_script_telegram_message(code: str, approval_id: str) -> str:
    """Markdown message with fenced Python block for the approval bubble."""
    safe_code = code.replace("```", "'''")
    return (
        "🛡️ *Ailrac — automation script approval required*\n\n"
        "Review the script below. It will *not* run until you tap "
        "*Approve & Run*. Domain isolation: outbound UI actions only.\n\n"
        f"```python\n{safe_code}\n```\n\n"
        f"_Request ID:_ `{approval_id[:8]}…`"
    )


def build_approval_inline_keyboard(approval_id: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "✅ Approve & Run",
                    callback_data=f"{CALLBACK_APPROVE_PREFIX}{approval_id}",
                ),
                InlineKeyboardButton(
                    "❌ Reject Command",
                    callback_data=f"{CALLBACK_DENY_PREFIX}{approval_id}",
                ),
            ],
        ]
    )


def _mark_approval_card_sent(approval_id: str) -> None:
    _sent_approval_ids.add(approval_id)


def _approval_card_already_sent(approval_id: str) -> bool:
    return approval_id in _sent_approval_ids


def send_approval_sync(approval_id: str, code: str) -> bool:
    """Send approval card immediately via Bot HTTP API (no outbox delay)."""
    if _approval_card_already_sent(approval_id):
        return True
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = _owner_chat_id()
    if not token or ":" not in token or "your_" in token or chat_id is None:
        enqueue_telegram_approval(approval_id, code)
        return False

    text = format_script_telegram_message(code, approval_id)
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "✅ Approve & Run",
                        "callback_data": f"{CALLBACK_APPROVE_PREFIX}{approval_id}",
                    },
                    {
                        "text": "❌ Reject Command",
                        "callback_data": f"{CALLBACK_DENY_PREFIX}{approval_id}",
                    },
                ]
            ]
        },
    }
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            if resp.status == 200:
                _mark_approval_card_sent(approval_id)
                logger.info("[TELEGRAM_APPROVAL] Sent approval card %s (sync)", approval_id)
                return True
    except urllib.error.HTTPError as exc:
        logger.warning("[TELEGRAM_APPROVAL] Sync send failed (%s); using outbox", exc)
    except Exception as exc:
        logger.warning("[TELEGRAM_APPROVAL] Sync send error (%s); using outbox", exc)

    enqueue_telegram_approval(approval_id, code)
    return False


def send_status_sync(text: str) -> bool:
    """Send a follow-up status message to the owner chat (post-execution)."""
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = _owner_chat_id()
    if not token or ":" not in token or "your_" in token or chat_id is None:
        return False

    payload = {
        "chat_id": chat_id,
        "text": text[:4096],
        "parse_mode": "Markdown",
    }
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status == 200
    except Exception as exc:
        logger.warning("[TELEGRAM_APPROVAL] Status send failed: %s", exc)
        return False


def enqueue_telegram_approval(approval_id: str, code: str) -> None:
    """Thread-safe: queue a script approval card for the Telegram polling loop."""
    if _approval_card_already_sent(approval_id):
        return
    _outbox.put({"approval_id": approval_id, "code": code})


def register_telegram_application(application: Application) -> None:
    global _application
    _application = application


def _owner_chat_id() -> Optional[int]:
    raw = os.getenv("MY_TELEGRAM_ID", "").strip()
    if not raw.isdigit():
        return None
    return int(raw)


async def _send_approval_card(application: Application, approval_id: str, code: str) -> None:
    if _approval_card_already_sent(approval_id):
        return
    chat_id = _owner_chat_id()
    if chat_id is None:
        logger.warning("[TELEGRAM_APPROVAL] MY_TELEGRAM_ID not set; skipping approval message")
        return

    text = format_script_telegram_message(code, approval_id)
    keyboard = build_approval_inline_keyboard(approval_id)

    await application.bot.send_message(
        chat_id=chat_id,
        text=text,
        parse_mode="Markdown",
        reply_markup=keyboard,
    )
    _mark_approval_card_sent(approval_id)
    logger.info("[TELEGRAM_APPROVAL] Sent approval card %s to chat %s", approval_id, chat_id)


async def approval_outbox_loop(application: Application) -> None:
    """Background task: drain approval queue and post inline-keyboard messages."""
    while True:
        try:
            job = await asyncio.to_thread(_outbox.get, True, 0.5)
        except queue.Empty:
            await asyncio.sleep(0.2)
            continue
        except Exception as exc:
            logger.exception("[TELEGRAM_APPROVAL] Outbox worker error: %s", exc)
            await asyncio.sleep(1)
            continue

        try:
            await _send_approval_card(
                application,
                job["approval_id"],
                job["code"],
            )
        except Exception as exc:
            logger.exception(
                "[TELEGRAM_APPROVAL] Failed to send approval %s: %s",
                job.get("approval_id"),
                exc,
            )


async def handle_execution_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Inline keyboard: approve runs script (unblocks waiter); reject purges pending."""
    query = update.callback_query
    if not query or not query.data:
        return

    await query.answer()

    owner_id = _owner_chat_id()
    user_id = query.from_user.id if query.from_user else None
    if owner_id is None or user_id != owner_id:
        await query.edit_message_text("⛔ Unauthorized.")
        return

    data = query.data
    approved = False
    approval_id: Optional[str] = None

    if data.startswith(CALLBACK_APPROVE_PREFIX):
        approval_id = data[len(CALLBACK_APPROVE_PREFIX) :]
        approved = True
    elif data.startswith(CALLBACK_DENY_PREFIX):
        approval_id = data[len(CALLBACK_DENY_PREFIX) :]
        approved = False
    else:
        return

    if not approval_id or not re.match(
        r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
        approval_id,
        re.IGNORECASE,
    ):
        await query.edit_message_text("⚠️ Invalid or expired approval request.")
        return

    resolved = resolve_approval(approval_id, approved=approved)
    if not resolved:
        await query.edit_message_text("⚠️ This script is no longer pending (expired or superseded).")
        return

    if approved:
        await query.edit_message_text(
            "✅ *Approved & Run* — executing script in sandbox…",
            parse_mode="Markdown",
        )
    else:
        await query.edit_message_text(
            "❌ *Reject Command* — script purged; execution cancelled.",
            parse_mode="Markdown",
        )


def attach_telegram_approval_handlers(application: Application) -> None:
    """Register callback handler for inline Approve / Reject buttons."""
    register_telegram_application(application)
    application.add_handler(CallbackQueryHandler(handle_execution_callback))


async def telegram_post_init(application: Application) -> None:
    """Start outbox worker (use Application.builder().post_init(telegram_post_init))."""
    register_telegram_application(application)
    application.create_task(approval_outbox_loop(application))
