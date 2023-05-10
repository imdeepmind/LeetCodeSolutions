# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
l = []

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.l = []
        return self._preorderTraversal(root)
    
    def _preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        
        self.l.append(root.val)
        
        if root.left:
            self._preorderTraversal(root.left)
        
        if root.right:
            self._preorderTraversal(root.right)
        
        return self.l
