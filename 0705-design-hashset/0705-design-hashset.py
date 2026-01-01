class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.__set = [ListNode(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        curr = self.__set[key % len(self.__set)]

        # Handling colisions using linked list
        while curr.next:
            if curr.next.key == key:
                return
            
            curr = curr.next
        
        curr.next = ListNode(key)
        
    def remove(self, key: int) -> None:
        curr = self.__set[key % len(self.__set)]

        # Handling colisions using linked list
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            
            curr = curr.next
        
    def contains(self, key: int) -> bool:
        curr = self.__set[key % len(self.__set)]

        # Handling colisions using linked list
        while curr.next:
            if curr.next.key == key:
                return True
            
            curr = curr.next
        
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)