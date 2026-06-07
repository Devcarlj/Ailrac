import sqlite3
import uuid
import json
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent / "ailrac.db"


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id TEXT PRIMARY KEY,
            conversation_id TEXT NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            FOREIGN KEY (conversation_id) REFERENCES conversations(id) ON DELETE CASCADE
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
    """)

    # Insert defaults only if they don't exist
    defaults = {
        "blocked_domains": json.dumps(["facebook.com", "instagram.com"]),
        "voice_output_enabled": "false",
        "voice_input_enabled": "false",
        "telegram_enabled": "false",
        "safe_search": "true",
        "ai_model": "gemini",
        "bot_mode": "search",
        "assistant_voice_profile": "default",
    }
    for key, value in defaults.items():
        cur.execute(
            "INSERT OR IGNORE INTO settings (key, value) VALUES (?, ?)",
            (key, value),
        )

    conn.commit()
    conn.close()


# ─── CONVERSATIONS ───

def create_conversation(title: str) -> dict:
    conn = get_conn()
    cur = conn.cursor()
    now = datetime.utcnow().isoformat()
    conv_id = str(uuid.uuid4())
    cur.execute(
        "INSERT INTO conversations (id, title, created_at, updated_at) VALUES (?, ?, ?, ?)",
        (conv_id, title, now, now),
    )
    conn.commit()
    conn.close()
    return {"id": conv_id, "title": title, "created_at": now, "updated_at": now, "message_count": 0}


def get_conversations() -> list:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.*, COUNT(m.id) as message_count
        FROM conversations c
        LEFT JOIN messages m ON m.conversation_id = c.id
        GROUP BY c.id
        ORDER BY c.updated_at DESC
    """)
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_conversation(conv_id: str) -> dict | None:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.*, COUNT(m.id) as message_count
        FROM conversations c
        LEFT JOIN messages m ON m.conversation_id = c.id
        WHERE c.id = ?
        GROUP BY c.id
    """, (conv_id,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None


def update_conversation_title(conv_id: str, title: str):
    conn = get_conn()
    cur = conn.cursor()
    now = datetime.utcnow().isoformat()
    cur.execute(
        "UPDATE conversations SET title = ?, updated_at = ? WHERE id = ?",
        (title, now, conv_id),
    )
    conn.commit()
    conn.close()


def touch_conversation(conv_id: str):
    conn = get_conn()
    cur = conn.cursor()
    now = datetime.utcnow().isoformat()
    cur.execute("UPDATE conversations SET updated_at = ? WHERE id = ?", (now, conv_id))
    conn.commit()
    conn.close()


def delete_conversation(conv_id: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM messages WHERE conversation_id = ?", (conv_id,))
    cur.execute("DELETE FROM conversations WHERE id = ?", (conv_id,))
    conn.commit()
    conn.close()


# ─── MESSAGES ───

def add_message(conversation_id: str, role: str, content: str) -> dict:
    conn = get_conn()
    cur = conn.cursor()
    msg_id = str(uuid.uuid4())
    now = datetime.utcnow().isoformat()
    cur.execute(
        "INSERT INTO messages (id, conversation_id, role, content, timestamp) VALUES (?, ?, ?, ?, ?)",
        (msg_id, conversation_id, role, content, now),
    )
    conn.commit()
    conn.close()
    return {
        "id": msg_id,
        "conversation_id": conversation_id,
        "role": role,
        "content": content,
        "timestamp": now,
    }


def get_messages(conversation_id: str) -> list:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM messages WHERE conversation_id = ? ORDER BY timestamp ASC",
        (conversation_id,),
    )
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]


# ─── SETTINGS ───

def get_settings() -> dict:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT key, value FROM settings")
    rows = cur.fetchall()
    conn.close()
    raw = {r["key"]: r["value"] for r in rows}
    return {
        "blocked_domains": json.loads(raw.get("blocked_domains", "[]")),
        "voice_output_enabled": raw.get("voice_output_enabled", "false") == "true",
        "voice_input_enabled": raw.get("voice_input_enabled", "false") == "true",
        "telegram_enabled": raw.get("telegram_enabled", "false") == "true",
        "safe_search": raw.get("safe_search", "true") == "true",
        "ai_model": raw.get("ai_model", "gemini"),
        "bot_mode": raw.get("bot_mode", "search"),
        "assistant_voice_profile": raw.get("assistant_voice_profile", "default"),
    }


def update_settings(updates: dict):
    conn = get_conn()
    cur = conn.cursor()
    # Keys that should be stored as-is (not lowercased booleans)
    raw_string_keys = {"ai_model", "bot_mode", "assistant_voice_profile"}
    for key, value in updates.items():
        if key == "blocked_domains":
            value = json.dumps(value)
        elif key in raw_string_keys:
            value = str(value)
        else:
            value = str(value).lower()
        cur.execute(
            "INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)",
            (key, value),
        )
    conn.commit()
    conn.close()
