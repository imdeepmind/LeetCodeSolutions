# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoList(self, l1, l2):
        current = ListNode()
        anchor = current

        while l1 and l2:
            if l1.val > l2.val:
                current.next = ListNode(l2.val)
                l2 = l2.next
                current = current.next
            else:
                current.next = ListNode(l1.val)
                l1 = l1.next
                current = current.next

        current.next = l1 or l2
        
        return anchor.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        head = self.mergeTwoList(lists[0], lists[1])
        index = 2

        while len(lists) > index:
            head = self.mergeTwoList(head, lists[index])

            index += 1
        
        return head
