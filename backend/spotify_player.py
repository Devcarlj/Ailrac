"""Spotify playback via desktop automation (keyboard search + mouse play; no Web API)."""

import logging
import os
import re
import subprocess
import time
from pathlib import Path

logger = logging.getLogger("ailrac.spotify")

_PLAY_RE = re.compile(
    r"^(?:please\s+)?(?:can you\s+)?(?:ailrac\s+)?play\s+"
    r"(?:(?:the\s+)?(?:song|track|music)\s+)?(?!spotify\b)(.+?)[.!?]*$",
    re.IGNORECASE,
)

_SUFFIXES_TO_STRIP = ("on spotify", "in spotify", "from spotify")

SPOTIFY_TRUSTED_MARKER = "# AILRAC_SPOTIFY"

# First search-result play control on the operator's display (screen coordinates).
_SPOTIFY_RESULT_PLAY_X = 1298
_SPOTIFY_RESULT_PLAY_Y = 220


def parse_play_query(user_input: str) -> str | None:
    """Extract track search query from e.g. 'Play Bohemian Rhapsody'."""
    text = user_input.strip()
    if not text:
        return None
    match = _PLAY_RE.match(text)
    if not match:
        return None

    query = match.group(1).strip()
    lower = query.lower()
    for suffix in _SUFFIXES_TO_STRIP:
        if lower.endswith(suffix):
            query = query[: -len(suffix)].strip()
            lower = query.lower()
            break

    if not query or lower in ("spotify", "music"):
        return None
    if re.search(r"\b(?:against|versus|vs\.?)\b", lower):
        return None
    return query[:200]


def launch_spotify_app() -> None:
    try:
        os.startfile("spotify")
    except OSError:
        subprocess.Popen("spotify", shell=True)


def _get_spotify_hwnd() -> int | None:
    try:
        import win32gui

        matches: list[int] = []

        def _collect(hwnd, _extra) -> bool:
            if win32gui.IsWindowVisible(hwnd):
                title = win32gui.GetWindowText(hwnd)
                if title and "spotify" in title.lower():
                    matches.append(hwnd)
            return True

        win32gui.EnumWindows(_collect, None)
        return matches[0] if matches else None
    except Exception:
        logger.debug("Could not find Spotify window", exc_info=True)
        return None


def focus_spotify_window() -> None:
    """Bring the Spotify desktop window to the foreground so keystrokes land correctly."""
    try:
        import win32con
        import win32gui

        hwnd = _get_spotify_hwnd()
        if not hwnd:
            return

        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        try:
            win32gui.SetForegroundWindow(hwnd)
        except Exception:
            # Windows may block foreground steal; Alt key trick sometimes helps.
            import pyautogui

            pyautogui.press("alt")
            win32gui.SetForegroundWindow(hwnd)
    except Exception:
        logger.debug("Could not focus Spotify window", exc_info=True)


def _open_spotify_search() -> None:
    """Focus Spotify inline search (Ctrl+L) and clear any previous query."""
    import pyautogui

    pyautogui.hotkey("ctrl", "l")
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.1)
    pyautogui.press("backspace")


def _try_click_play_button_template() -> bool:
    """Click a trusted assets/spotify_play.png template if the operator supplied one."""
    asset = Path(__file__).resolve().parent / "assets" / "spotify_play.png"
    if not asset.is_file():
        return False

    try:
        import pyautogui

        box = pyautogui.locateOnScreen(str(asset))
        if box is None:
            return False
        cx, cy = pyautogui.center(box)
        pyautogui.moveTo(cx, cy, duration=0.2)
        pyautogui.click()
        return True
    except Exception:
        logger.debug("spotify_play.png template click failed", exc_info=True)
        return False


def _click_first_search_result_with_mouse() -> None:
    """Click the first search result play control at the operator's screen coordinates."""
    import pyautogui

    time.sleep(1.5)

    if _try_click_play_button_template():
        return

    pyautogui.moveTo(_SPOTIFY_RESULT_PLAY_X, _SPOTIFY_RESULT_PLAY_Y, duration=0.2)
    time.sleep(0.15)
    pyautogui.click()


def play_track_via_keyboard(query: str) -> str:
    """
    Open Spotify, search with Ctrl+L, then mouse-click the first result to play.
    Requires the Spotify desktop app; optional assets/spotify_play.png for precision.
    """
    query = (query or "").strip()[:200]
    if not query:
        return "No song name provided. Sir."

    try:
        import pyautogui
    except ImportError:
        return "Desktop automation is unavailable (pyautogui missing). Sir."

    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.05

    try:
        launch_spotify_app()
        time.sleep(3.5)
        focus_spotify_window()
        time.sleep(0.3)

        _open_spotify_search()
        pyautogui.write(query, interval=0.04)
        pyautogui.press("enter")
        _click_first_search_result_with_mouse()

        return f"Searched Spotify for **{query}** and started playback. Sir."

    except Exception as exc:
        logger.exception("Spotify keyboard play failed for query=%r", query)
        return (
            f"Could not control Spotify via keyboard: {exc}. "
            "Make sure the Spotify desktop app is installed and try again. Sir."
        )


def build_trusted_spotify_script(query: str) -> str:
    """Canonical pyautogui script the LLM may emit; auto-approved when it matches this template."""
    safe_query = query.replace("\\", "\\\\").replace('"', '\\"')
    return f'''{SPOTIFY_TRUSTED_MARKER}
import time
import pyautogui
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.05
time.sleep(3.5)
pyautogui.hotkey("ctrl", "l")
time.sleep(0.5)
pyautogui.hotkey("ctrl", "a")
time.sleep(0.1)
pyautogui.press("backspace")
pyautogui.write("{safe_query}", interval=0.04)
pyautogui.press("enter")
time.sleep(1.5)
pyautogui.moveTo({_SPOTIFY_RESULT_PLAY_X}, {_SPOTIFY_RESULT_PLAY_Y}, duration=0.2)
time.sleep(0.15)
pyautogui.click()
time.sleep(0.15)
pyautogui.hotkey("win", "down")
'''


def is_trusted_spotify_automation(code: str) -> bool:
    """
    Only Spotify keyboard scripts marked with AILRAC_SPOTIFY and limited to
    pyautogui/time are allowed to skip the human approval gate.
    """
    if not code or SPOTIFY_TRUSTED_MARKER not in code:
        return False

    from execution_guard import scan_payload_forbidden

    blocked, _ = scan_payload_forbidden(code)
    if blocked:
        return False

    executable_lines: list[str] = []
    for line in code.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        executable_lines.append(stripped)

    if not executable_lines:
        return False

    for line in executable_lines:
        if line.startswith("import "):
            if line not in ("import time", "import pyautogui"):
                return False
            continue
        if line.startswith("pyautogui."):
            continue
        if line.startswith("time.sleep"):
            continue
        return False

    return any("pyautogui." in line for line in executable_lines)


def try_spotify_play(user_input: str) -> str | None:
    """Router hook: Play [song] via keyboard (no LLM, no approval modal)."""
    query = parse_play_query(user_input)
    if query is None:
        return None
    return play_track_via_keyboard(query)
