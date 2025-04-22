# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([(root, root.val)])
        good_nodes = 0

        while q:
            for _ in range(len(q)):
                node, max_val = q.popleft()

                if node:
                    if node.left:
                        q.append((node.left, max(max_val, node.val)))
                    
                    if node.right:
                        q.append((node.right,  max(max_val, node.val)))
                    
                    if node.val >= max_val:
                        good_nodes += 1

        return good_nodes        