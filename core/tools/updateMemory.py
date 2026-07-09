from core.tools.registry import tool
from core.memory.sqlite import getMemoryStore

@tool('updateMemory')
def updateMemory(factId: int, fact: str) -> str:
    memory = getMemoryStore().update(id=int(factId), fact=fact)

    if memory is not None:
        return "Memory updated successfully"
    else:
        return "Error on updating memory"
