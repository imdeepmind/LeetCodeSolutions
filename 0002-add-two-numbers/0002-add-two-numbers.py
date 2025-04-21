# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        anchor = res

        carry = 0

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next

            alpha = l1_val + l2_val + carry
            carry = 0

            if alpha > 9:
                alpha %= 10
                carry = 1
            
            res.next = ListNode(alpha)
            res = res.next
        
        if carry:
            res.next = ListNode(carry)
        
        return anchor.next