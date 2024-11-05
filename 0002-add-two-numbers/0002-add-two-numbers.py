# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        i, j = l1, l2
        result = []

        while i or j:
            first_val = 0
            second_val = 0

            if i: 
                first_val = i.val
                i = i.next
            
            if j:
                second_val = j.val
                j = j.next
            
            s = first_val + second_val + carry

            if s >= 10:
                result.append(s % 10)
                carry = 1
            else:
                result.append(s)
                carry = 0

        if carry:
            result.append(1)
        
        res = None
        current = None

        for num in result:
            temp = ListNode(num)

            if current != None:
                current.next = temp
                current = current.next
            else:
                current = temp
                res = temp

        return res