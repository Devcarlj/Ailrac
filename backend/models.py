from pydantic import BaseModel
from typing import Optional, List, Any, Dict


class ChatRequest(BaseModel):
    conversation_id: Optional[str] = None
    message: str


class MessageOut(BaseModel):
    id: str
    conversation_id: str
    role: str
    content: str
    timestamp: str


class ConversationOut(BaseModel):
    id: str
    title: str
    created_at: str
    updated_at: str
    message_count: int = 0


class RenameRequest(BaseModel):
    title: str


class ExecutionApproveRequest(BaseModel):
    """Optional explicit confirm; must be exactly 'y' when provided."""
    confirm: str = "y"


class PendingExecutionResponse(BaseModel):
    pending: bool
    id: Optional[str] = None
    code: Optional[str] = None
    conversation_id: Optional[str] = None
    created_at: Optional[float] = None


class BotModeUpdateRequest(BaseModel):
    mode: str
