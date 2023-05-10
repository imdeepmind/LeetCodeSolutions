# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.l = []
        return self._inorderTraversal(root)
    
    def _inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        
        if root.left:
            self._inorderTraversal(root.left)
        
        self.l.append(root.val)
        
        if root.right:
            self._inorderTraversal(root.right)
        
        
        return self.l
