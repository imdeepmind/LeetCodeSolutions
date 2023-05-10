# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash = {}
        node = head
        prev = None
        
        while node:
            if node.val not in hash:
                hash[node.val] = 1
                prev = node
                node = node.next if node.next else None
            else:
                prev.next = node.next if node.next else None
                node = node.next if node.next else None
        
        return head