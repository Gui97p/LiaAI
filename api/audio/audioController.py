from fastapi import UploadFile
from core.audio.transcriber import LLMTranscriber

client = LLMTranscriber("whisper-large-v3")

async def handleTranscribe(file: UploadFile):
    audio = await file.read()
    result = client.call(audio)

    return result
