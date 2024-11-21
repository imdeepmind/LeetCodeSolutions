# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp
        
        return prev
    
    def divideIntoBatches(self, head: ListNode, k: int) -> list:
        if k <= 0:
            raise ValueError("Batch size k must be greater than 0.")
        
        batches = []
        current = head

        while current:
            batch_head = current 
            prev = None
            
            counter = 0
            for _ in range(k):
                if not current:
                    break
                prev = current
                current = current.next
                counter += 1
            
            if prev:
                prev.next = None
            
            batches.append((batch_head, counter))
        
        return batches

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        batches = self.divideIntoBatches(head, k)
        reversed_batch = [self.reverseList(batch[0]) if batch[1] == k else batch[0] for batch in batches]

        node = ListNode()
        anchor = node

        for batch in reversed_batch:
            node.next = batch

            while node.next:
                node = node.next

        return anchor.next