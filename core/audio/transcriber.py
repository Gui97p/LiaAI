from groq import Groq
from dotenv import load_dotenv
load_dotenv()

class LLMTranscriber:
    def __init__(self, model):
        self.client = Groq()
        self.model = model

    def call(self, audio):
        transcription = self.client.audio.transcriptions.create(
            file=audio,
            model=self.model,
            language="pt"
        )

        return transcription.text
