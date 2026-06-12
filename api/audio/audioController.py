from fastapi import UploadFile
from fastapi.responses import StreamingResponse
from core.audio.transcriber import LLMTranscriber
from core.audio.tts import LLMTTS

transcriber = LLMTranscriber("whisper-large-v3")
tts         = LLMTTS('pt-BR-FranciscaNeural')

async def handleTranscribe(file: UploadFile):
    audio = await file.read()
    result = transcriber.call(audio, file.filename)

    return result

async def handleTTS(text: str):
    buffer = await tts.call(text)

    return StreamingResponse(buffer, media_type="audio/mpeg")
