# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMiddle(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def divideList(self, head, middle):
        start = head

        while start.next:
            if start.next == middle:
                start.next = None
                break

            start = start.next

        return head

    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev

            prev, curr = curr, temp
        
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return head

        # find middle node
        middle = self.findMiddle(head)

        start = self.divideList(head, middle)

        # # Reverse the "middle" linked list
        reversedMiddle = self.reverseList(middle)

        res = ListNode()
        anchor = res

        while start or reversedMiddle:
            if start:
                res.next = start
                res = res.next
                start = start.next
            
            if reversedMiddle:
                res.next = reversedMiddle
                res = res.next
                reversedMiddle = reversedMiddle.next
        
        return anchor