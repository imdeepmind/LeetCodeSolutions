# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_same_tree(self, p, q):
        if not p and q:
            return False
        
        if p and not q:
            return False
        
        if not p and not q:
            return True
        
        if p.val != q.val:
            return False
        
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if root.val == subRoot.val:
            return self.is_same_tree(root, subRoot)
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)