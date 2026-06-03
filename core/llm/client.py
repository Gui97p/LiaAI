from groq import Groq

class LLMClient(Groq):
    def __init__(self):
        super().__init__()