"""
In-memory store for UI/HTTP code-execution approvals.
Blocks the privileged tool thread until the user approves or denies in the app.
"""

from __future__ import annotations

import logging
import threading
import time
import uuid
from dataclasses import dataclass, field
from typing import Any, Optional

logger = logging.getLogger("ailrac.code_approval")

APPROVAL_TIMEOUT_SECONDS = 300


@dataclass
class PendingExecution:
    id: str
    code: str
    conversation_id: Optional[str]
    created_at: float
    dispatch_on_approve: bool = True
    _event: threading.Event = field(default_factory=threading.Event, repr=False)
    _approved: Optional[bool] = field(default=None, repr=False)


_lock = threading.Lock()
_pending: Optional[PendingExecution] = None
_resolved_approval_ids: set[str] = set()


def create_pending_approval(
    code: str,
    conversation_id: Optional[str] = None,
    *,
    dispatch_on_approve: bool = True,
) -> str:
    """Register code awaiting approval; returns approval id."""
    global _pending
    with _lock:
        if _pending is not None:
            logger.warning("[APPROVAL] Superseding previous pending execution %s", _pending.id)
            _pending._approved = False
            _pending._event.set()

        pending = PendingExecution(
            id=str(uuid.uuid4()),
            code=code,
            conversation_id=conversation_id,
            created_at=time.time(),
            dispatch_on_approve=dispatch_on_approve,
        )
        _pending = pending
        logger.info("[APPROVAL] Pending execution created: %s", pending.id)
        return pending.id


def wait_for_approval(approval_id: str, timeout_seconds: int = APPROVAL_TIMEOUT_SECONDS) -> bool:
    """Block until approved, denied, superseded, or timed out."""
    global _pending
    with _lock:
        if _pending is None or _pending.id != approval_id:
            return False
        pending = _pending

    signaled = pending._event.wait(timeout=timeout_seconds)

    with _lock:
        if _pending is not None and _pending.id == approval_id:
            _pending = None

    if not signaled:
        logger.warning("[APPROVAL] Timed out waiting for %s", approval_id)
        return False
    return pending._approved is True


def resolve_approval(approval_id: str, approved: bool) -> bool:
    """Approve or deny; on approve, dispatch execution in the background."""
    global _pending
    snapshot: Optional[dict[str, Any]] = None
    with _lock:
        if approval_id in _resolved_approval_ids:
            logger.info("[APPROVAL] Ignoring duplicate resolve for %s", approval_id)
            return True
        if _pending is None or _pending.id != approval_id:
            return False
        snapshot = {
            "code": _pending.code,
            "conversation_id": _pending.conversation_id,
            "dispatch_on_approve": _pending.dispatch_on_approve,
        }
        _pending._approved = approved
        _pending._event.set()
        _pending = None
        _resolved_approval_ids.add(approval_id)

    logger.info(
        "[APPROVAL] Resolved %s as %s",
        approval_id,
        "approved" if approved else "denied",
    )

    if approved and snapshot and snapshot.get("dispatch_on_approve", True):
        from execution_guard import dispatch_approved_execution

        dispatch_approved_execution(snapshot["code"], snapshot.get("conversation_id"))
    return True


def get_pending_approval() -> Optional[dict[str, Any]]:
    """Snapshot for GET /api/execution/pending."""
    with _lock:
        if _pending is None:
            return None
        return {
            "id": _pending.id,
            "code": _pending.code,
            "conversation_id": _pending.conversation_id,
            "created_at": _pending.created_at,
        }


def get_pending_approval_id_for_code(code: str) -> Optional[str]:
    """Reuse an in-flight approval when the same script is submitted twice."""
    normalized = (code or "").strip()
    if not normalized:
        return None
    with _lock:
        if _pending is None:
            return None
        if _pending.code.strip() == normalized and _pending._approved is None:
            return _pending.id
    return None
