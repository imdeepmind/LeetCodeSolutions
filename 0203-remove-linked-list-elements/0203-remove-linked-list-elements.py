# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        start = head
        tail = None

        while start:
            if start.val == val:
                if tail:
                    tail.next = start.next
                else:
                    head = start.next
            else:
                tail = start

            start = start.next
        return head
