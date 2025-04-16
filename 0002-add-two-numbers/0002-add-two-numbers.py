# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        head = res
        carry = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next

            delta = carry + val1 + val2
            carry = 0

            if delta > 9:
                delta = delta % 10
                carry = 1
            
            res.next = ListNode(delta)
            res = res.next
        
        if carry:
            res.next = ListNode(1)
        
        return head.next

