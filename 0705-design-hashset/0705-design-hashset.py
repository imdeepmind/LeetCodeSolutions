class MyHashSet:

    def __init__(self):
        self.mapper = {}

    def add(self, key: int) -> None:
        self.mapper[key] = 1

    def remove(self, key: int) -> None:
        if key in self.mapper:
            del self.mapper[key]

    def contains(self, key: int) -> bool:
        return key in self.mapper
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)