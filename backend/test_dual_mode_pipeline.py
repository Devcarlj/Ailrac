"""
Smoke tests for dual-mode + Telegram approval pipeline (no live Gemini/Telegram required).
Run: python test_dual_mode_pipeline.py
"""

from __future__ import annotations

import sys
import threading
import time

FAILURES: list[str] = []


def ok(msg: str) -> None:
    print(f"  OK  {msg}")


def fail(msg: str) -> None:
    print(f"  FAIL {msg}")
    FAILURES.append(msg)


def test_bot_state() -> None:
    print("\n[bot_state]")
    from bot_state import BotMode, get_global_mode, set_global_mode, mode_to_api_dict

    set_global_mode(BotMode.SEARCH)
    if get_global_mode() != BotMode.SEARCH:
        fail("SEARCH mode not set")
    else:
        ok("SEARCH mode")

    set_global_mode(BotMode.CONTROL)
    if mode_to_api_dict()["current_mode"] != "control":
        fail("mode_to_api_dict")
    else:
        ok("CONTROL mode + API dict")


def test_click_image_template_policy() -> None:
    print("\n[click_image]")
    from ailrac_core import _resolve_trusted_template, _trusted_assets_dir
    from pathlib import Path

    assets = _trusted_assets_dir()
    assets.mkdir(parents=True, exist_ok=True)
    sample = assets / "test_button.png"
    sample.write_bytes(
        b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01"
        b"\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89"
        b"\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4"
        b"\x00\x00\x00\x00IEND\xaeB`\x82"
    )
    try:
        resolved = _resolve_trusted_template("test_button.png")
        if resolved is None or resolved.name != "test_button.png":
            fail("trusted relative template should resolve")
        else:
            ok("resolves assets/*.png")

        if _resolve_trusted_template("https://evil.com/a.png") is not None:
            fail("http URL template must be rejected")
        else:
            ok("rejects web URL")

        if _resolve_trusted_template("../ailrac_core.py") is not None:
            fail("path traversal must be rejected")
        else:
            ok("rejects traversal")

        if _resolve_trusted_template("missing.png") is not None:
            fail("missing template must be rejected")
        else:
            ok("rejects missing file")

        if _resolve_trusted_template(r"C:\assets\test_button.png") is not None:
            fail("absolute path must be rejected")
        else:
            ok("rejects absolute path")

        if _resolve_trusted_template("paste from user: submit.png") is not None:
            fail("non-literal pasted path must be rejected")
        else:
            ok("rejects non-literal path")
    finally:
        if sample.is_file():
            sample.unlink()


def test_scan_and_sandbox() -> None:
    print("\n[execution_guard]")
    from execution_guard import (
        build_sandbox_globals,
        scan_payload_forbidden,
    )

    good = """
import time
ailrac_launch("notepad")
time.sleep(0.1)
"""
    blocked, reason = scan_payload_forbidden(good)
    if blocked:
        fail(f"valid script blocked: {reason}")
    else:
        ok("multi-step script passes scan")

    bad = "import os\nos.system('calc')"
    blocked, reason = scan_payload_forbidden(bad)
    if not blocked:
        fail("os.system should be blocked")
    else:
        ok(f"os blocked: {reason[:50]}…")

    blind = "pyautogui.screenshot()"
    blocked, _ = scan_payload_forbidden(blind)
    if not blocked:
        fail("screenshot read should be blocked")
    else:
        ok("blind typewriter blocks screenshot")

    g = build_sandbox_globals()
    if "ailrac_launch" not in g or "time" not in g:
        fail("sandbox missing ailrac_launch/time")
    else:
        ok("sandbox globals")

    from execution_guard import normalize_automation_script, _run_sandboxed_code_inprocess

    with_imports = normalize_automation_script(
        "import time\nimport pyautogui\nailrac_launch('notepad')\ntime.sleep(0.05)\n"
    )
    if "import " in with_imports:
        fail("normalize should strip time/pyautogui imports")
    else:
        ok("normalize strips redundant imports")

    sandbox_out = _run_sandboxed_code_inprocess(with_imports)
    if "Sandbox execution error" in sandbox_out or "__import__" in sandbox_out:
        fail(f"sandbox failed on typical script: {sandbox_out[:120]}")
    else:
        ok("sandbox runs script with stripped imports")

    from execution_guard import dedupe_automation_script
    from request_context import (
        record_launch,
        reset_control_session,
        reset_conversation_id,
        set_conversation_id,
    )

    ctx = set_conversation_id("test-dedupe-conv")
    try:
        reset_control_session()
        record_launch("notepad")
        deduped = dedupe_automation_script(
            "ailrac_launch('notepad')\ntime.sleep(0.05)\npyautogui.write('hi')\n"
        )
        if "ailrac_launch" in deduped:
            fail("dedupe should remove launch already done via launch_app")
        if "pyautogui.write" not in deduped:
            fail("dedupe should keep typing not yet performed")
        else:
            ok("dedupe strips duplicate launch lines")
    finally:
        reset_conversation_id(ctx)


def test_benign_automation_and_risk() -> None:
    print("\n[benign automation + risk gate]")
    from execution_guard import ApprovalQueued, execute_agent_action, is_benign_automation_script

    launch_script = "ailrac_launch('notepad')\ntime.sleep(0.1)\n"
    if not is_benign_automation_script(launch_script):
        fail("launch-only script should be benign")
    else:
        ok("launch-only script is benign")

    volume_script = "pyautogui.press('volumeup')\npyautogui.press('volumeup')\n"
    if not is_benign_automation_script(volume_script):
        fail("volume script should be benign")
    else:
        ok("volume script is benign")

    risky_script = "ailrac_launch('cmd')\ntime.sleep(0.1)\n"
    if is_benign_automation_script(risky_script):
        fail("cmd launch should not be benign")
    else:
        ok("cmd launch requires approval")

    try:
        execute_agent_action(launch_script, conversation_id="test-conv", skip_approval=False)
        ok("benign script runs without ApprovalQueued")
    except ApprovalQueued:
        fail("benign script should not queue approval")


def test_approval_flow() -> None:
    print("\n[code_approval + telegram enqueue]")
    from code_approval import create_pending_approval, get_pending_approval, resolve_approval
    from execution_guard import ApprovalQueued, execute_agent_action

    code = "ailrac_launch('powershell')\ntime.sleep(0.1)\n"
    try:
        execute_agent_action(code, conversation_id="test-conv", skip_approval=False)
        fail("execute_agent_action should raise ApprovalQueued")
    except ApprovalQueued:
        ok("non-blocking ApprovalQueued raised")

    pending = get_pending_approval()
    if not pending:
        fail("pending not registered after queue")
    else:
        ok("pending registered")

    aid = pending["id"]
    resolved = resolve_approval(aid, approved=False)
    if not resolved:
        fail("resolve_approval deny failed")
    else:
        ok("deny clears pending")

    if get_pending_approval() is not None:
        fail("pending should be cleared after deny")
    else:
        ok("pending cleared after resolve")


def test_control_prompt() -> None:
    print("\n[control mode prompt]")
    from ailrac_core import get_control_mode_system_instruction

    p = get_control_mode_system_instruction()
    for needle in (
        "blind typewriter",
        "ailrac_launch",
        "Approve & Run",
        "time.sleep",
    ):
        if needle.lower() not in p.lower():
            fail(f"prompt missing: {needle}")
        else:
            ok(f"prompt contains '{needle}'")


def test_api_if_running() -> None:
    print("\n[HTTP API — optional]")
    try:
        import urllib.request
        import json

        req = urllib.request.urlopen("http://127.0.0.1:8000/api/health", timeout=2)
        if req.status != 200:
            fail(f"health status {req.status}")
            return
        ok("backend reachable on :8000")

        req = urllib.request.urlopen("http://127.0.0.1:8000/api/settings/mode", timeout=2)
        data = json.loads(req.read().decode())
        if "current_mode" not in data:
            fail("GET /api/settings/mode shape")
        else:
            ok(f"GET mode → {data['current_mode']}")

        body = json.dumps({"mode": "search"}).encode()
        post = urllib.request.Request(
            "http://127.0.0.1:8000/api/settings/mode",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        resp = urllib.request.urlopen(post, timeout=2)
        out = json.loads(resp.read().decode())
        if out.get("current_mode") != "search":
            fail("POST /api/settings/mode")
        else:
            ok("POST mode switch")
    except Exception as exc:
        print(f"  SKIP backend not running ({exc})")


def main() -> int:
    print("Ailrac dual-mode + approval smoke tests")
    test_bot_state()
    test_click_image_template_policy()
    test_scan_and_sandbox()
    test_benign_automation_and_risk()
    test_approval_flow()
    test_control_prompt()
    test_api_if_running()

    print("\n" + "=" * 50)
    if FAILURES:
        print(f"FAILED ({len(FAILURES)}):")
        for f in FAILURES:
            print(f"  - {f}")
        return 1
    print("All automated checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
