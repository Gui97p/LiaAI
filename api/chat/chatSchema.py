from pydantic import BaseModel
from typing import Optional

class ToolFunction(BaseModel):
    name: str
    arguments: dict

class ToolCall(BaseModel):
    id: str
    type: str
    function: ToolFunction

class ChatRequest(BaseModel):
    content: str
    capabilities: Optional[dict[str, list[str]]] = None

class ChatResponse(BaseModel):
    content: str
    tool_calls: Optional[list[ToolCall]] = None
