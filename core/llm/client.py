from core.tools.registry import TOOLS
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

class LLMClient:
    def __init__(self, model):
        self.client = Groq()
        self.model = model

    def call(self, messages):
        completion = self.client.chat.completions.create(messages=messages, model=self.model, tools=TOOLS)

        message = completion.choices[0].message

        return {
            "content": message.content,
            "tool_calls": message.tool_calls
        }
