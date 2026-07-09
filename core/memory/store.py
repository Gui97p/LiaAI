from dataclasses import dataclass

@dataclass
class Memory:
    fact: str
    category: str
    id: int = None
    createdAt: str = None
