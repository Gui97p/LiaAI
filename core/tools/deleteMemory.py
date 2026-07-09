from core.tools.registry import tool
from core.memory.sqlite import getMemoryStore

@tool('deleteMemory')
def deleteMemory(factId: int) -> str:
    getMemoryStore().delete(id=int(factId))

    return "Memory deleted successfully"
