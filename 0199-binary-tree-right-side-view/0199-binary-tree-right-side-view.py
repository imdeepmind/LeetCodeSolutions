# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            val = None

            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    if node.left:
                        q.append(node.left)
                    
                    if node.right:
                        q.append(node.right)
                
                    val = node.val
            
            if val != None:
                res.append(val)
        
        return res