class HashTableDoubleHashing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash1(self, key):
        return key % self.size

    def hash2(self, key):
        return 1 + (key % (self.size - 1))

    def insert(self, key, value):
        idx1 = self.hash1(key)
        idx2 = self.hash2(key)
        for i in range(self.size):
            probe_idx = (idx1 + i * idx2) % self.size
            if self.table[probe_idx] is None or self.table[probe_idx][0] == key:
                self.table[probe_idx] = (key, value)
                return

    def get(self, key):
        idx1 = self.hash1(key)
        idx2 = self.hash2(key)
        for i in range(self.size):
            probe_idx = (idx1 + i * idx2) % self.size
            if self.table[probe_idx] is None:
                return None
            if self.table[probe_idx][0] == key:
                return self.table[probe_idx][1]
        return None
