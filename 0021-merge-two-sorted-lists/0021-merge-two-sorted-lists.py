# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode(0)
        head = merged

        while list1 or list2:
            if list1 and list2:
                if list1.val > list2.val:
                    merged.next = ListNode(list2.val)
                    merged = merged.next
                    list2 = list2.next
                else:
                    merged.next = ListNode(list1.val)
                    merged = merged.next
                    list1 = list1.next
            else:
                if list1:
                    merged.next = ListNode(list1.val)
                    merged = merged.next
                    list1 = list1.next
                
                if list2:
                    merged.next = ListNode(list2.val)
                    merged = merged.next
                    list2 = list2.next
        
        return head.next