from src.agent.prompt import buildSystemPrompt
from src.llm.client import LLMClient
from src.memory.history import History

class Assistant:
    def __init__(self):
        self.client = LLMClient("openai/gpt-oss-120b")
        self.history = History()
    
    def ask(self, message):
        self.history.insert('user', message)
        system = buildSystemPrompt()

        messages = [{"role": "system", "content": system}]

        for h in self.history.get():
            messages.append({"role": h["role"], "content": h["content"]})
        
        response = self.client.call(messages)

        self.history.insert('assistant', response['content'])

        return response
