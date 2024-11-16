"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
            
        copiedList = {}

        start = head

        while start:
            copiedList[start] = ListNode(start.val)
            start = start.next
        
        start = head

        while start:
            copiedList[start].random = copiedList[start.random] if start.random else None
            copiedList[start].next = copiedList[start.next] if start.next else None
                
            start = start.next

        return copiedList[head]