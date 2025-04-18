# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        res = []

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()

                if node:
                    if node.left:
                        queue.append(node.left)
                    
                    if node.right:
                        queue.append(node.right)
                    
                    level.append(node.val)
            
            if level:
                res.append(level)
        
        return res