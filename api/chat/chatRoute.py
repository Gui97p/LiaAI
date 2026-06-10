from fastapi import APIRouter, Request
from api.chat import chatController

router = APIRouter()

@router.post("/chat")
async def chat(request: Request):
    body = await request.json()
    return chatController.handleChat(body)
