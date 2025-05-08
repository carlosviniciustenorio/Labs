class HashTableRobinHood:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_func(self, key):
        return key % self.size

    def insert(self, key, value):
        idx = self.hash_func(key)
        probe_length = 0

        while True:
            current = self.table[idx]
            if current is None:
                self.table[idx] = (key, value, probe_length)
                return
            current_key, current_val, current_dist = current
            if current_key == key:
                self.table[idx] = (key, value, probe_length)
                return
            if probe_length > current_dist:
                # Swap (Robin Hood: steal spot)
                self.table[idx], key, value, probe_length = (key, value, probe_length), current_key, current_val, current_dist
            idx = (idx + 1) % self.size
            probe_length += 1

    def get(self, key):
        idx = self.hash_func(key)
        probe_length = 0
        while True:
            current = self.table[idx]
            if current is None:
                return None
            current_key, value, _ = current
            if current_key == key:
                return value
            idx = (idx + 1) % self.size
            probe_length += 1
