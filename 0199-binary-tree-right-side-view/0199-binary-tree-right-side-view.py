# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        res = []

        while queue:
            val = None

            for _ in range(len(queue)):
                node = queue.popleft()

                if node:
                    if node.left:
                        queue.append(node.left)
                    
                    if node.right:
                        queue.append(node.right)

                    val = node.val
            
            if val:
                res.append(val)

        return res
            