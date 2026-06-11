from core.agent.assistant import Assistant
from api.chat.chatSchema import ChatRequest, ChatResponse

client = Assistant()

def handleChat(body: ChatRequest) -> ChatResponse:
    result = client.ask(body.content, body.capabilities or {})
    return ChatResponse(**result)
