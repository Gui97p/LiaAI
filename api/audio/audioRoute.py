from fastapi import APIRouter, UploadFile
from api.audio import audioController

router = APIRouter()

@router.post("/transcribe")
async def transcribe(file: UploadFile):
    return await audioController.handleTranscribe(file)
