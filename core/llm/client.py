from groq import Groq
from dotenv import load_dotenv
load_dotenv()

class LLMClient:
    def __init__(self, model):
        self.client = Groq()
        self.model = model

    def call(self, messages, tools, forceText=False):
        params = dict(messages=messages, model=self.model, tools=tools)
        if forceText:
            params["tool_choice"] = "none"

        completion = self.client.chat.completions.create(**params)

        message = completion.choices[0].message

        return {
            "content": message.content,
            "tool_calls": message.tool_calls
        }
