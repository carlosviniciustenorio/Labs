class HashTableLinearProbing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_func(self, key):
        return key % self.size

    def insert(self, key, value):
        idx = self.hash_func(key)
        for i in range(self.size):
            probe_idx = (idx + i) % self.size
            if self.table[probe_idx] is None or self.table[probe_idx][0] == key:
                self.table[probe_idx] = (key, value)
                return

    def get(self, key):
        idx = self.hash_func(key)
        for i in range(self.size):
            probe_idx = (idx + i) % self.size
            if self.table[probe_idx] is None:
                return None
            if self.table[probe_idx][0] == key:
                return self.table[probe_idx][1]
        return None
