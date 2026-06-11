from core.agent.prompt import buildSystemPrompt
from core.llm.client import LLMClient
from core.memory.history import History
from core.tools.registry import REGISTRY, buildTools

import json

class Assistant:
    def __init__(self):
        self.client = LLMClient("openai/gpt-oss-120b")
        self.history = History()
    
    def ask(self, message, capabilities):
        self.history.insert('user', message)
        system = buildSystemPrompt()
        tools = buildTools(capabilities)

        messages = [{"role": "system", "content": system}]

        for h in self.history.get():
            messages.append({"role": h["role"], "content": h["content"]})
        
        response = self.client.call(messages, tools)

        localTools = []
        if response.get('tool_calls') is not None:
            messages.append({
                "role": "assistant",
                "content": response['content'],
                "tool_calls": response['tool_calls']
            })
            for tool in response.get('tool_calls'):
                globalTool = REGISTRY.get(tool.function.name)
                if globalTool != None:
                    args = json.loads(tool.function.arguments)
                    toolResponse = globalTool(**args)
                    
                    if toolResponse is not None:
                        responseObject = {
                            "role": "tool",
                            "tool_call_id": tool.id,
                            "content": toolResponse
                        }
                        messages.append(responseObject)
                        self.history.insert('tool', responseObject)
                else:
                    localTools.append({
                        "id": tool.id,
                        "type": tool.type,
                        "function": {
                            "name": tool.function.name,
                            "arguments": json.loads(tool.function.arguments)
                        }
                    })
                    messages.append({"role": "tool", 
                                "tool_call_id": tool.id, 
                                "content": "Executed by client. Do not call any more tools. Generate the final text response now."})
            
            messages.append({"role": "system", "content": "All tools have been handled. Respond only in text, do not request any tools."})    
            response = self.client.call(messages, tools=[])

        self.history.insert('assistant', response['content'])
        return {
            "content": response['content'],
            "tool_calls": localTools
        }
