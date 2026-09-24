"""Temporary local auth probe — delete after debugging."""
import json
import os
import urllib.error
import urllib.request
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")
key = (os.getenv("GEMINI_API_KEY") or "").strip().strip('"').strip("'")
print("prefix", key[:4], "len", len(key))

body = json.dumps({"contents": [{"parts": [{"text": "Say hi"}]}]}).encode()


def post(url: str, headers: dict) -> None:
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(headers.get("x-goog-api-key") and "header" or "query", "OK", r.status)
    except urllib.error.HTTPError as e:
        print(headers.get("x-goog-api-key") and "header" or "query", "HTTP", e.code, e.read()[:200])


post(
    f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={key}",
    {"Content-Type": "application/json"},
)
post(
    "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent",
    {"Content-Type": "application/json", "x-goog-api-key": key},
)

try:
    from google import genai

    client = genai.Client(api_key=key)
    r = client.models.generate_content(model="gemini-2.5-flash", contents="Say hi")
    print("sdk OK", (r.text or "")[:40])
    chat = client.chats.create(model="gemini-2.5-flash")
    stream = chat.send_message_stream("Count to 3")
    chunks = "".join(getattr(c, "text", "") or "" for c in stream)
    print("stream OK", chunks[:40])
except Exception as exc:
    print("sdk FAIL", str(exc)[:240])
