# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.l = []
        return self._postorderTraversal(root)
    
    def _postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        
        if root.left:
            self._postorderTraversal(root.left)
        
        if root.right:
            self._postorderTraversal(root.right)
        
        
        self.l.append(root.val)
        
        return self.l
