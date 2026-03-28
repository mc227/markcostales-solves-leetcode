class RehashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def _hash_function(self,key):
        return hash(key) % self.size

    def _rehash(self):
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0

        for item in old_table:
            if item is not None:
                for key, value in item:
                    self.insert(key,value)
    
    def insert(self,key,value):
        if self.count / self.size > 0.7:
            self._rehash()

        