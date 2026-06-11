from fastapi import APIRouter
from api.chat import chatController
from api.chat.chatSchema import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/")
async def chat(body: ChatRequest) -> ChatResponse:
    return chatController.handleChat(body)
