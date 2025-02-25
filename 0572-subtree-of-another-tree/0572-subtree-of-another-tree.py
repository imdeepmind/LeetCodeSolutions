# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(p, q):
            if not p and not q:
                return True
            
            if not p and q:
                return False
            
            if p and not q:
                return False
            
            if p.val != q.val:
                return False
            
            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
        
        if not root:
            return False
            
        if root.val == subRoot.val:
            if is_same_tree(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
