from core.agent.prompt import buildSystemPrompt
from core.llm.client import LLMClient
from core.memory.history import History
from core.tools.registry import REGISTRY
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
                    toolResponse = globalTool(tool)
                    toolsExecuted = True
                    if toolResponse is not None:
                        responseObject = {
                            "role": "tool",
                            "tool_call_id": tool.id,
                            "content": toolResponse
                        }
                        messages.append(responseObject)
                        self.history.insert('tool', responseObject)
                else:
                    localTools.append(tool)
                    messages.append({"role": "tool", 
                                "tool_call_id": tool.id, 
                                "content": "Pending client execution: " + tool.function.name})
            
            messages.append({"role": "system", "content": '''The messages marked as pending role have tools that will
                                be returned to the client for execution, while the messages marked as tool role are responses for tools
                                you asked. Now generate the final response for the user'''})    
            response = self.client.call(messages)


        self.history.insert('assistant', response['content'])
        return {
            "content": response['content'],
            "tool_calls": localTools
        }
