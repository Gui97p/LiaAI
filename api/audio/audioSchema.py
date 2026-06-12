from pydantic import BaseModel

class TTSRequest(BaseModel):
    content: str
