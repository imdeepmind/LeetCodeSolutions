# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, None
        start = None

        while list1 or list2:
            if not list1:
                curr = ListNode(list2.val, None)
                list2 = list2.next
            elif not list2:
                curr = ListNode(list1.val, None)
                list1 = list1.next
            elif list1.val < list2.val:
                curr = ListNode(list1.val, None)
                list1 = list1.next
            else:
                curr = ListNode(list2.val, None)
                list2 = list2.next
            
            if not start:
                start = curr
            
            if not prev:
                prev = curr
            else:
                prev.next = curr
                prev = curr
        
        return start