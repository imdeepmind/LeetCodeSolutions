# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def calculateDepth(root, depth=0):
            if not root:
                return depth
            
            left_depth = calculateDepth(root.left, depth+1)
            right_depth = calculateDepth(root.right, depth+1)

            return max(left_depth, right_depth)
        
        return calculateDepth(root)
