class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} 

    def get(self, key: int) -> int:
        """Returns the value of the key if it exists in the cache, otherwise -1."""
        if key in self.cache:
            self.cache[key] = self.cache.pop(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int):
        """Updates the value of the key if it exists, otherwise inserts the key-value pair."""
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            self.cache.pop(next(iter(self.cache)))

        self.cache[key] = value
