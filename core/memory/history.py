class History:
    def __init__(self, size=50):
        self._history = []
        self.size = size
    
    def get(self):
        return self._history
    
    def insert(self, role, content):
        self._history.append({"role": role, "content": content})
        if len(self._history) > self.size:
            self._history = self._history[-self.size:]
