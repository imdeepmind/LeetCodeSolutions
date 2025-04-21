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
        mapper = {}
        res = Node(0)
        anchor = res
        current = head

        while current:
            res.next = Node(current.val)
            mapper[current] = res.next

            res = res.next
            current = current.next
        
        current = head

        while current:
            if current.random:
                mapper[current].random = mapper[current.random]
            else:
                mapper[current].random = None
            
            current = current.next

        return anchor.next
        