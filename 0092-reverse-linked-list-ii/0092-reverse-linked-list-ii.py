# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        leftAnchor, current = dummy, head

        for _ in range(left-1):
            leftAnchor, current = current, current.next
        
        prev = None

        for _ in range(right-left+1):
            temp = current.next
            current.next = prev

            prev = current
            current = temp
        
        leftAnchor.next.next = current
        leftAnchor.next = prev

        return dummy.next
        

