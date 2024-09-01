# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return 
        
        if root.val == p.val or root.val == q.val:
            return root

        # Check if q and p are in different sides of the tree
        if root.val > p.val and root.val < q.val:
            return root
        
        if root.val > q.val and root.val < p.val:
            return root
        
        # Check if p and q are on the left side of the tree, so max (p, q) is smaller than root
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # Check if p and q are on the right side of the tree, so max (p, q) is smaller than root
        return self.lowestCommonAncestor(root.right, p, q)