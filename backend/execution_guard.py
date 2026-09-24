"""
Zero-trust execution guards for Ailrac.
Blocks prompt-injection payloads, requires human approval for exec(), and redacts secrets.
"""

from __future__ import annotations

import builtins
import hashlib
import io
import logging
import os
import re
import sys
import threading
import time
from typing import Any

logger = logging.getLogger("ailrac.execution_guard")

# ─── Exceptions ───


class SafetyViolation(Exception):
    """Raised when code or output fails a security policy."""


class ApprovalDenied(SafetyViolation):
    """User did not approve execution at the human-in-the-loop gate."""


class ApprovalQueued(Exception):
    """Script is queued for Telegram/dashboard approval — return to user immediately."""

    def __init__(self, approval_id: str):
        self.approval_id = approval_id
        super().__init__(approval_id)


# ─── Forbidden payload patterns (pre-approval; no user prompt) ───

FORBIDDEN_SUBSTRINGS = [
    ".env",
    "dotenv",
    "load_dotenv",
    "os.environ",
    "getenv(",
    "environ[",
    "TELEGRAM_BOT_TOKEN",
    "GEMINI_API_KEY",
    "OPENROUTER_API_KEY",
    "MY_TELEGRAM_ID",
    "credentials",
    "id_rsa",
    "passwd",
    "shadow",
    "api_key",
    "secret_key",
    "private_key",
    "token.json",
]

# Blind typewriter: block inbound reads from the host screen or clipboard.
BLIND_TYPEWRITER_FORBIDDEN_REGEXES = [
    re.compile(r"\bpyautogui\.screenshot\b", re.IGNORECASE),
    re.compile(r"\bpyautogui\.locate(?:OnScreen|AllOnScreen|Center)\b", re.IGNORECASE),
    re.compile(r"\bpyautogui\.pixel(?:MatchesColor|)?\b", re.IGNORECASE),
    re.compile(r"\bImageGrab\b", re.IGNORECASE),
    re.compile(r"\bmss\b", re.IGNORECASE),
    re.compile(r"\bpyperclip\b", re.IGNORECASE),
    re.compile(r"\bclipboard\b", re.IGNORECASE),
    re.compile(r"\bwin32gui\.GetWindowText\b", re.IGNORECASE),
    re.compile(r"\bGetForegroundWindow\b", re.IGNORECASE),
    re.compile(r"\bread_text\b", re.IGNORECASE),
    re.compile(r"\bOCR\b"),
    re.compile(r"\btesseract\b", re.IGNORECASE),
    re.compile(r"\bpaddleocr\b", re.IGNORECASE),
]

FORBIDDEN_REGEXES = [
    re.compile(r"\b(?:rmdir|unlink)\b", re.IGNORECASE),
    re.compile(r"\brm\s+-rf\b", re.IGNORECASE),
    re.compile(r"\bshutil\.rmtree\b", re.IGNORECASE),
    re.compile(r"\bos\.(?:remove|unlink|rmdir|system|popen|spawn|exec\w*|startfile)\b", re.IGNORECASE),
    re.compile(r"\bsubprocess\b", re.IGNORECASE),
    re.compile(r"\b(?:import|from)\s+os\b", re.IGNORECASE),
    re.compile(r"\b(?:import|from)\s+subprocess\b", re.IGNORECASE),
    re.compile(r"\b(?:import|from)\s+sys\b", re.IGNORECASE),
    re.compile(r"\b(?:import|from)\s+shutil\b", re.IGNORECASE),
    re.compile(r"\b(?:import|from)\s+pathlib\b", re.IGNORECASE),
    re.compile(r"\bopen\s*\([^)]*\.env", re.IGNORECASE),
    re.compile(r"\bformat\s*\(", re.IGNORECASE),
    re.compile(r"\bregistry\b", re.IGNORECASE),
    re.compile(r"\bwinreg\b", re.IGNORECASE),
    re.compile(r"\bctypes\b", re.IGNORECASE),
    re.compile(r"\bsocket\b", re.IGNORECASE),
    re.compile(r"\brequests\b", re.IGNORECASE),
    re.compile(r"\burllib\b", re.IGNORECASE),
    re.compile(r"\b__import__\b"),
    re.compile(r"\beval\s*\(", re.IGNORECASE),
    re.compile(r"\bexec\s*\(", re.IGNORECASE),
    re.compile(r"\bcompile\s*\(", re.IGNORECASE),
    re.compile(r"\bglobals\s*\(", re.IGNORECASE),
    re.compile(r"\blocals\s*\(", re.IGNORECASE),
    re.compile(r"\bgetattr\s*\(\s*__", re.IGNORECASE),
    re.compile(r"\b__builtins__\b"),
    re.compile(r"\b__class__\b"),
    re.compile(r"\b__subclasses__\b"),
    re.compile(r"\b__globals__\b"),
    re.compile(r"\b__code__\b"),
    re.compile(r"\bpickle\b", re.IGNORECASE),
    re.compile(r"\bbase64\b", re.IGNORECASE),
] + BLIND_TYPEWRITER_FORBIDDEN_REGEXES

# Allowed automation imports (checked before generic import bans).
_ALLOWED_IMPORT_LINES = (
    re.compile(r"^\s*import\s+time\s*$", re.MULTILINE),
    re.compile(r"^\s*from\s+time\s+import\s+", re.MULTILINE),
    re.compile(r"^\s*import\s+pyautogui\s*$", re.MULTILINE),
)

# Imports stripped before exec — modules are injected into the sandbox namespace.
_STRIP_IMPORT_LINES = (
    re.compile(r"^\s*from\s+ailrac_launch\s+import\s+.*$", re.MULTILINE | re.IGNORECASE),
    re.compile(r"^\s*import\s+ailrac_launch\s*$", re.MULTILINE | re.IGNORECASE),
    re.compile(r"^\s*from\s+launch_app\s+import\s+.*$", re.MULTILINE | re.IGNORECASE),
    re.compile(r"^\s*import\s+launch_app\s*$", re.MULTILINE | re.IGNORECASE),
    re.compile(r"^\s*import\s+time\s*$", re.MULTILINE),
    re.compile(r"^\s*from\s+time\s+import\s+.*$", re.MULTILINE),
    re.compile(r"^\s*import\s+pyautogui\s*$", re.MULTILINE),
    re.compile(r"^\s*from\s+pyautogui\s+import\s+.*$", re.MULTILINE),
)

_SANDBOX_IMPORTABLE = frozenset({"time", "pyautogui"})

APPROVAL_BORDER = (
    "╔══════════════════════════════════════════════════════════════════════╗\n"
    "║  ⚠️   AILRAC CODE EXECUTION — HUMAN APPROVAL REQUIRED   ⚠️           ║\n"
    "╠══════════════════════════════════════════════════════════════════════╣\n"
    "║  Untrusted content must NEVER run without your explicit consent.     ║\n"
    "╚══════════════════════════════════════════════════════════════════════╝"
)

# Minimal builtins exposed inside the sandboxed exec() namespace.
_SAFE_BUILTIN_NAMES = (
    "abs", "all", "any", "bool", "bytes", "chr", "dict", "enumerate",
    "filter", "float", "format", "frozenset", "int", "isinstance",
    "issubclass", "iter", "len", "list", "map", "max", "min", "next",
    "ord", "pow", "print", "range", "repr", "reversed", "round", "set",
    "slice", "sorted", "str", "sum", "tuple", "zip", "True", "False", "None",
)


def _sandbox_import(
    name: str,
    globals: Any = None,
    locals: Any = None,
    fromlist: tuple = (),
    level: int = 0,
) -> Any:
    """Whitelist-only __import__ for scripts that still contain import statements."""
    if level != 0:
        raise ImportError("relative imports are not allowed in automation scripts")
    top_level = name.split(".", 1)[0]
    if top_level not in _SANDBOX_IMPORTABLE:
        raise ImportError(
            f"import {name!r} is not allowed (use injected time, pyautogui, ailrac_launch)"
        )
    import importlib

    return importlib.import_module(name)


def _safe_builtins_dict() -> dict[str, Any]:
    out: dict[str, Any] = {}
    for name in _SAFE_BUILTIN_NAMES:
        if hasattr(builtins, name):
            out[name] = getattr(builtins, name)
    out["__import__"] = _sandbox_import
    return out


def _collect_secret_values() -> list[str]:
    """Environment values that must never appear in model output."""
    secrets: list[str] = []
    for key in ("GEMINI_API_KEY", "OPENROUTER_API_KEY", "TELEGRAM_BOT_TOKEN", "OPENAI_API_KEY", "ANTHROPIC_API_KEY"):
        val = os.getenv(key, "").strip()
        if len(val) >= 8:
            secrets.append(val)
    return secrets


# ─── Payload scanning ───


def normalize_automation_script(code: str) -> str:
    """Remove LLM import lines; time, pyautogui, and ailrac_launch are injected at exec."""
    normalized = (code or "").replace("\r\n", "\n")
    for pattern in _STRIP_IMPORT_LINES:
        normalized = pattern.sub("", normalized)
    return "\n".join(line for line in normalized.split("\n") if line.strip() != "").strip()


_AILRAC_LAUNCH_LINE = re.compile(
    r"^\s*(?:ailrac_launch|launch_app)\s*\(\s*['\"]([^'\"]+)['\"]\s*\)\s*$",
    re.IGNORECASE,
)

_recent_exec_lock = threading.Lock()
_recent_exec_fingerprints: dict[str, float] = {}
_EXEC_DEDUPE_SECONDS = 45.0


def dedupe_automation_script(code: str) -> str:
    """Drop launch/type lines already performed by other tools in this request."""
    from request_context import get_launched_apps, get_typed_fragments

    launched = {name.lower() for name in get_launched_apps()}
    typed = get_typed_fragments()
    if not launched and not typed:
        return code

    kept: list[str] = []
    for line in code.splitlines():
        launch_match = _AILRAC_LAUNCH_LINE.match(line.strip())
        if launch_match and launch_match.group(1).strip().lower() in launched:
            logger.info(
                "[CONTROL] Removed duplicate launch from script: %s",
                launch_match.group(1),
            )
            continue

        skip_line = False
        for fragment in typed:
            if not fragment:
                continue
            escaped = re.escape(fragment)
            if re.search(
                rf"pyautogui\.(?:write|typewrite)\s*\(\s*['\"]{escaped}['\"]",
                line,
                re.IGNORECASE,
            ):
                logger.info("[CONTROL] Removed duplicate typing from script")
                skip_line = True
                break
        if not skip_line:
            kept.append(line)

    return "\n".join(kept).strip()


def _prepare_automation_script(code: str) -> str:
    return dedupe_automation_script(normalize_automation_script(code))


def _execution_fingerprint(code: str) -> str:
    return hashlib.sha256(_prepare_automation_script(code).encode("utf-8")).hexdigest()


def _claim_execution_slot(code: str) -> bool:
    """Return False if the same script ran (or is running) within the dedupe window."""
    key = _execution_fingerprint(code)
    now = time.monotonic()
    with _recent_exec_lock:
        last = _recent_exec_fingerprints.get(key)
        if last is not None and (now - last) < _EXEC_DEDUPE_SECONDS:
            logger.warning(
                "[APPROVAL] Suppressed duplicate execution of the same script within %.0fs",
                _EXEC_DEDUPE_SECONDS,
            )
            return False
        _recent_exec_fingerprints[key] = now
        stale = [k for k, t in _recent_exec_fingerprints.items() if (now - t) >= _EXEC_DEDUPE_SECONDS]
        for k in stale:
            del _recent_exec_fingerprints[k]
    return True


def _strip_allowed_imports(normalized: str) -> str:
    """Remove allowed import lines so time.sleep is not blocked by import rules."""
    scrubbed = normalized
    for pattern in _ALLOWED_IMPORT_LINES:
        scrubbed = pattern.sub("", scrubbed)
    return scrubbed


def scan_payload_forbidden(code: str) -> tuple[bool, str]:
    """
    Returns (is_blocked, reason).
    Blocked payloads are aborted before the approval UI is shown.
    """
    if not code or not code.strip():
        return True, "Empty code block."

    normalized = code.replace("\r\n", "\n")
    scan_target = _strip_allowed_imports(normalized)

    for token in FORBIDDEN_SUBSTRINGS:
        if token.lower() in scan_target.lower():
            logger.warning("[SECURITY] Blocked forbidden substring: %s", token)
            return True, f"Forbidden token detected: {token!r}"

    for pattern in FORBIDDEN_REGEXES:
        match = pattern.search(scan_target)
        if match:
            logger.warning("[SECURITY] Blocked regex match: %s", match.group(0))
            return True, f"Forbidden pattern detected: {match.group(0)!r}"

    return False, ""


def structural_extract_python(text: str) -> str | None:
    """
    Privileged-model structural filter: extract a single executable Python block.
    Returns None if the text does not look like intentional code.
    """
    if not text or not text.strip():
        return None

    fenced = re.findall(r"```(?:python|py)?\s*\n([\s\S]*?)```", text, re.IGNORECASE)
    if fenced:
        block = fenced[-1].strip()
        if block and not scan_payload_forbidden(block)[0]:
            return block
        return None

    stripped = text.strip()
    lines = stripped.splitlines()
    code_like = sum(
        1
        for ln in lines
        if ln.strip().startswith(
            (
                "import ",
                "from ",
                "def ",
                "class ",
                "pyautogui.",
                "ailrac_launch",
                "launch_app",
                "time.sleep",
                "print(",
                "for ",
                "while ",
            )
        )
    )
    if code_like >= 2 and len(lines) <= 80:
        if not scan_payload_forbidden(stripped)[0]:
            return stripped

    return None


# ─── Human approval gate ───

_BENIGN_BLOCKED_LAUNCH_TARGETS = frozenset(
    {"cmd", "command prompt", "powershell", "regedit", "taskmgr", "task manager"}
)

_SCRIPT_LAUNCH_CALL_RE = re.compile(
    r"(?:ailrac_launch|launch_app)\s*\(\s*['\"]([^'\"]+)['\"]",
    re.IGNORECASE,
)

_SCRIPT_DANGEROUS_LINE_SNIPPETS = (
    "alt+f4",
    "alt + f4",
    "ctrl+alt",
    "ctrl + alt",
    "win+l",
    "win + l",
    "win+r",
    "win + r",
    "win+x",
    "win + x",
    "shift+esc",
    "taskkill",
    "shutdown",
    "restart",
    "reboot",
    "powershell",
    "cmd.exe",
    "reg delete",
    "format ",
)

_DANGEROUS_HOTKEY_CALL_RE = re.compile(
    r"hotkey\s*\(\s*"
    r"(?:"
    r'["\']win["\']\s*,\s*["\'](?:l|r|x)["\']'
    r"|"
    r'["\']alt["\']\s*,\s*["\']f4["\']'
    r"|"
    r'["\']ctrl["\']\s*,\s*["\']alt["\']\s*,\s*["\']del["\']'
    r"|"
    r'["\']ctrl["\']\s*,\s*["\']shift["\']\s*,\s*["\']esc["\']'
    r")",
    re.IGNORECASE,
)

_ALLOWED_BENIGN_PYAUTOGUI = (
    "write(",
    "typewrite(",
    "press(",
    "hotkey(",
    "moveTo(",
    "click(",
    "doubleClick(",
    "rightClick(",
    "scroll(",
    "mouseDown(",
    "mouseUp(",
    "keyDown(",
    "keyUp(",
    "drag(",
    "dragTo(",
)


def is_benign_automation_script(code: str) -> bool:
    """
    True for low-risk outbound UI scripts (launch app, volume, typing, clicks).
    These run immediately without Telegram/dashboard approval.
    """
    if not code or not code.strip():
        return False

    blocked, _ = scan_payload_forbidden(code)
    if blocked:
        return False

    prepared = _prepare_automation_script(code)
    for match in _SCRIPT_LAUNCH_CALL_RE.finditer(prepared):
        if match.group(1).strip().lower() in _BENIGN_BLOCKED_LAUNCH_TARGETS:
            return False

    lower_script = prepared.lower()
    if any(snippet in lower_script for snippet in _SCRIPT_DANGEROUS_LINE_SNIPPETS):
        return False

    executable_lines: list[str] = []
    for line in prepared.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        executable_lines.append(stripped)

    if not executable_lines:
        return False

    for line in executable_lines:
        lower_line = line.lower()
        if line.startswith("import "):
            if line not in ("import time", "import pyautogui"):
                return False
            continue
        if line.startswith(("pyautogui.FAILSAFE", "pyautogui.PAUSE")):
            continue
        if line.startswith(("ailrac_launch(", "launch_app(", "time.sleep(", "print(")):
            continue
        if line.startswith("pyautogui."):
            if _DANGEROUS_HOTKEY_CALL_RE.search(line):
                return False
            if not any(method in line for method in _ALLOWED_BENIGN_PYAUTOGUI):
                return False
            continue
        return False

    return True


def _prompt_terminal_approval(code: str) -> None:
    print(APPROVAL_BORDER)
    print("\n--- Proposed script (review carefully) ---\n")
    print(code)
    print("\n--- End of script ---\n")
    print("Type exactly 'y' to approve execution. Any other input aborts.\n> ", end="", flush=True)

    try:
        answer = input().strip()
    except EOFError as exc:
        raise ApprovalDenied("Approval input ended unexpectedly.") from exc

    if answer != "y":
        raise ApprovalDenied(
            f"Execution blocked: approval not granted (received {answer!r}, expected 'y')."
        )


def _use_terminal_approval() -> bool:
    """Only when AILRAC_TERMINAL_APPROVAL=true — never infer from isatty() (breaks under Uvicorn)."""
    return os.getenv("AILRAC_TERMINAL_APPROVAL", "").strip().lower() in ("1", "true", "yes")


def _queue_for_approval(code: str, conversation_id: str | None = None) -> str:
    """Register pending script, push Telegram card, return immediately (no blocking wait)."""
    from code_approval import create_pending_approval, get_pending_approval_id_for_code
    from telegram_approval import send_approval_sync

    prepared = _prepare_automation_script(code)
    existing_id = get_pending_approval_id_for_code(prepared)
    if existing_id:
        logger.info("[APPROVAL] Reusing in-flight approval %s", existing_id)
        return existing_id

    approval_id = create_pending_approval(prepared, conversation_id)
    send_approval_sync(approval_id, prepared)
    return approval_id


def _request_human_approval_blocking(code: str, conversation_id: str | None = None) -> None:
    """Terminal-only blocking gate (AILRAC_TERMINAL_APPROVAL=true)."""
    from code_approval import create_pending_approval, wait_for_approval

    approval_id = create_pending_approval(code, conversation_id)
    approved = wait_for_approval(approval_id)
    if not approved:
        raise ApprovalDenied(
            "Execution was denied or timed out. Approve via Telegram "
            "[✅ Approve & Run] or the Ailrac dashboard, Sir."
        )


def dispatch_approved_execution(code: str, conversation_id: str | None = None) -> None:
    """Run approved script in a background thread; notify Telegram + conversation when done."""
    if not _claim_execution_slot(code):
        return

    def _worker() -> None:
        from telegram_approval import send_status_sync

        try:
            normalized = _prepare_automation_script(code)
            result = _run_sandboxed_code(normalized)
            summary = f"✅ **Automation finished**\n\n{result[:3000]}"
            send_status_sync(summary)
            if conversation_id:
                from database import add_message, get_messages, touch_conversation

                recent = get_messages(conversation_id)
                last = recent[-1] if recent else None
                if not (
                    last
                    and last.get("role") == "assistant"
                    and (last.get("content") or "").startswith("✅ **Automation finished**")
                ):
                    add_message(conversation_id, "assistant", summary)
                touch_conversation(conversation_id)
        except Exception as exc:
            logger.exception("[APPROVAL] Background execution failed")
            send_status_sync(f"❌ **Automation failed:** {exc}")

    threading.Thread(target=_worker, name="ailrac-approved-exec", daemon=True).start()


# ─── Sandboxed exec ───


def _sandbox_launch_app(app_name: str) -> str:
    """Whitelisted app spawn for approved multi-step scripts (no raw os/subprocess in user code)."""
    from ailrac_core import launch_app

    return launch_app(app_name)


def build_sandbox_globals() -> dict[str, Any]:
    """Restricted globals for exec(); outbound UI only — no os/subprocess in user code."""
    import time as _time_module

    try:
        import pyautogui as _pyautogui
    except ImportError:
        _pyautogui = None

    safe_globals: dict[str, Any] = {
        "__builtins__": _safe_builtins_dict(),
        "__name__": "__ailrac_sandbox__",
        "__doc__": None,
        "time": _time_module,
        "ailrac_launch": _sandbox_launch_app,
        "launch_app": _sandbox_launch_app,
    }
    if _pyautogui is not None:
        safe_globals["pyautogui"] = _pyautogui
    return safe_globals


def _run_sandboxed_code(code: str) -> str:
    """Run on the calling thread — pyautogui on Windows requires the main thread."""
    try:
        return _run_sandboxed_code_inprocess(code)
    except BaseException as exc:
        return redact_secrets(f"Sandbox execution error: {exc}")


def _run_sandboxed_code_inprocess(code: str) -> str:
    sandbox_globals = build_sandbox_globals()
    sandbox_locals: dict[str, Any] = {}
    stdout_capture = io.StringIO()
    stderr_capture = io.StringIO()

    import contextlib

    with contextlib.redirect_stdout(stdout_capture), contextlib.redirect_stderr(stderr_capture):
        exec(compile(code, "<ailrac_agent_action>", "exec"), sandbox_globals, sandbox_locals)

    out = stdout_capture.getvalue()
    err = stderr_capture.getvalue()
    combined = ""
    if out:
        combined += f"[Output]\n{out}"
    if err:
        combined += f"\n[Stderr]\n{err}"
    if not combined.strip():
        combined = "[Output]\n(no printed output)"
    return redact_secrets(combined.strip())


def execute_agent_action(
    code: str,
    *,
    conversation_id: str | None = None,
    skip_approval: bool = False,
) -> str:
    """
    Dual-gate executor:
    1) Static payload scan (silent abort on hit)
    2) Human approval (terminal 'y' or React UI) — skipped only for trusted Spotify scripts
    3) Sandboxed exec() with redacted stdout/stderr
    """
    try:
        code = _prepare_automation_script(code)
        is_blocked, reason = scan_payload_forbidden(code)
        if is_blocked:
            logger.error("[SECURITY] Payload blocked pre-approval: %s", reason)
            raise SafetyViolation(
                f"🛡️ **Security block** — Generated script was rejected before execution.\n"
                f"Reason: {reason}\n\nSir."
            )

        if not skip_approval:
            if _use_terminal_approval():
                _prompt_terminal_approval(code)
            elif is_benign_automation_script(code):
                logger.info("[APPROVAL] Auto-running benign automation script (no confirmation)")
            else:
                approval_id = _queue_for_approval(code, conversation_id)
                raise ApprovalQueued(approval_id)
        else:
            logger.info("[APPROVAL] Auto-running pre-approved script")
        return _run_sandboxed_code(code)

    except ApprovalQueued:
        raise
    except (SafetyViolation, ApprovalDenied):
        raise
    except Exception as exc:
        logger.exception("[SECURITY] Sandboxed execution failed")
        return redact_secrets(f"Sandbox execution error: {exc}")


# ─── Output redaction ───


def redact_secrets(text: str) -> str:
    """Redact API keys and tokens from any user-visible string."""
    if not text:
        return text

    redacted = text
    for secret in _collect_secret_values():
        if secret in redacted:
            redacted = redacted.replace(secret, "[REDACTED_SECRET]")
        partial = secret[:12]
        if len(partial) >= 8 and partial in redacted:
            redacted = re.sub(re.escape(partial) + r"[\w\-\.]*", "[REDACTED_SECRET]", redacted)

    redacted = re.sub(
        r"(?i)(gemini_api_key|openrouter_api_key|telegram_bot_token|api[_-]?key)\s*[=:]\s*\S+",
        r"\1=[REDACTED_SECRET]",
        redacted,
    )
    return redacted
