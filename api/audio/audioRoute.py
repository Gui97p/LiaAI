from fastapi import APIRouter, UploadFile
from fastapi.responses import StreamingResponse
from api.audio import audioController
from api.audio.audioSchema import TTSRequest

router = APIRouter()

@router.post("/transcribe")
async def transcribe(file: UploadFile):
    return await audioController.handleTranscribe(file)

@router.post("/tts")
async def tts(body: TTSRequest) -> StreamingResponse:
    return await audioController.handleTTS(body.content)
