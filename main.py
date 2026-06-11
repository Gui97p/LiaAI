from fastapi import FastAPI
from api.chat.chatRoute import router as chatRouter
from api.audio.audioRoute import router as AudioRouter

app = FastAPI()
app.include_router(chatRouter, prefix='/api/chat')
app.include_router(AudioRouter, prefix='/api/audio')