# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def is_same(p, q):
            if not p and q:
                return False
            
            if not q and p:
                return False
            
            if not p and not q:
                return True
            
            return p.val == q.val and is_same(p.left, q.left) and is_same(p.right, q.right)
        
        return is_same(p, q)