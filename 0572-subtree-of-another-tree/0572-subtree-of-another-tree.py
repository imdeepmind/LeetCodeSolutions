# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True

        if p == None or q == None:
            return False
            
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        
        if root.val == subRoot.val:
            temp = self.isSameTree(root, subRoot)

            if temp:
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)