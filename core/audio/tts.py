import edge_tts
import io

class LLMTTS:
    def __init__(self, model):
        self.model = model

    async def call(self, text):
        communicate = edge_tts.Communicate(text, voice=self.model)
        buffer = io.BytesIO()

        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                buffer.write(chunk["data"])

        buffer.seek(0)
        return buffer
