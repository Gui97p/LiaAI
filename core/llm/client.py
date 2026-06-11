from groq import Groq
from dotenv import load_dotenv
load_dotenv()

class LLMClient:
    def __init__(self, model):
        self.client = Groq()
        self.model = model

    def call(self, messages, tools):
        completion = self.client.chat.completions.create(
            messages=messages, 
            model=self.model, 
            tools=tools, 
            temperature=0.4,
            max_tokens=400,
        )

        message = completion.choices[0].message

        return {
            "content": message.content,
            "tool_calls": message.tool_calls
        }
