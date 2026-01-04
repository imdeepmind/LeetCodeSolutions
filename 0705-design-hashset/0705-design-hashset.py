class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.__set = [ListNode(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        cur = self.__set[key % len(self.__set)]

        while cur.next:
            if cur.next.key == key:
                return
            
            cur = cur.next
        
        cur.next = ListNode(key)
        
    def remove(self, key: int) -> None:
        cur = self.__set[key % len(self.__set)]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            
            cur = cur.next
        
        return

    def contains(self, key: int) -> bool:
        cur = self.__set[key % len(self.__set)]

        while cur.next:
            if cur.next.key == key:
                return True
            
            cur = cur.next
        
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)