# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
            
        def find_middle(root):
            slow, fast = root, root

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            return slow
        
        def reversed_list(root):
            prev, current = None, root

            while current:
                temp = current.next
                current.next = prev

                prev = current
                current = temp
            
            return prev
        
        def divide_list(root, middle):
            current = root

            while current.next:
                if current.next == middle:
                    current.next = None
                    break

                current = current.next
            
            return root
        
        middle = find_middle(head)
        reversed_middle = reversed_list(middle)
        start = divide_list(head, middle)

        res = ListNode(0)
        anchor = res

        while start or reversed_middle:
            if start:
                res.next = start
                start = start.next
                res = res.next
            
            if reversed_middle:
                res.next = reversed_middle
                reversed_middle = reversed_middle.next
                res = res.next
        
        return anchor.next
