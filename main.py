from fastapi import FastAPI
from api.chat.chatRoute import router as chatRouter

app = FastAPI()
app.include_router(chatRouter, prefix='/api')
