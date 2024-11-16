# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def get_list_length(list):
            start = list
            length = 0

            while start:
                length += 1
                start = start.next

            return length

        head_a_length, head_b_length = get_list_length(headA), get_list_length(headB)

        big_node = headA if head_a_length > head_b_length else headB
        small_node = headA if head_a_length <= head_b_length else headB

        for _ in range(max(head_a_length, head_b_length) - min(head_a_length, head_b_length)):
            big_node = big_node.next

        while big_node and small_node:
            if big_node == small_node:
                return big_node

            big_node = big_node.next
            small_node = small_node.next

        return None