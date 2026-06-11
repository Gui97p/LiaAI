from core.agent.assistant import Assistant

client = Assistant()

def handleChat(body):
    return client.ask(body['content'], body['capabilities'])
