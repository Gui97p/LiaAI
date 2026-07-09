from core.tools.registry import tool
from core.memory.sqlite import getMemoryStore

@tool('saveMemory')
def saveMemory(fact: str, category: str) -> str:
    memory = getMemoryStore().create(fact=fact, category=category)

    if memory is not None:
        return "Memory saved successfully"
    else:
        return "Error on saving memory"
