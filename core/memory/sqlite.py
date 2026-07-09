import sqlite3
from core.memory.store import Memory

_instance: SQLiteMemoryStore = None
def getMemoryStore() -> SQLiteMemoryStore:
    global _instance
    if _instance is None:
        _instance = SQLiteMemoryStore()
    return _instance

class SQLiteMemoryStore:
    def __init__(self, path: str = "memory.db"):
        self.conn = sqlite3.connect(path)
        self._migrate()
    
    def _migrate(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fact TEXT NOT NULL,
                category TEXT NOT NULL,
                createdAt TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def create(self, fact: str, category: str) -> Memory:
        cursor = self.conn.execute('''
            INSERT INTO memories (fact, category) VALUES (?, ?)
        ''', (fact, category))
        self.conn.commit()

        return self.getById(cursor.lastrowid)

    def getById(self, id: int) -> Memory:
        obj = self.conn.execute('''
            SELECT * FROM memories WHERE id = ? 
        ''', (id,)).fetchone()

        return Memory(id=obj[0], fact=obj[1], category=obj[2], createdAt=obj[3])

    def getAll(self) -> list[Memory]:
        memoryList = self.conn.execute('''
            SELECT * FROM memories
        ''').fetchall()

        return list(map(lambda x: Memory(id=x[0], fact=x[1], category=x[2], createdAt=x[3]), memoryList))

    def update(self, id: int, fact: str) -> Memory:
        self.conn.execute('''
            UPDATE memories SET fact = ? WHERE id = ?
        ''', (fact, id))
        self.conn.commit()

        return self.getById(id)

    def delete(self, id: int) -> None:
        self.conn.execute('''
            DELETE FROM memories WHERE id = ?
        ''', (id,))
        self.conn.commit()
