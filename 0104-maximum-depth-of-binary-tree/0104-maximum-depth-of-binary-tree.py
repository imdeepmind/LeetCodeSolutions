# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkDepth(self, node, level):
        leftLevel = level
        rightLevel = level
        
        if node and node.left:
            leftLevel = self.checkDepth(node.left, level + 1)
        
        if node and node.right:
            rightLevel = self.checkDepth(node.right, level + 1)
        
        return leftLevel if leftLevel > rightLevel else rightLevel
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.checkDepth(root, 0) + 1