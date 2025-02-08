# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def calculateDepth(root, max_depth=0):
            if not root:
                return max_depth
            
            left_max = calculateDepth(root.left, max_depth+1)
            right_max = calculateDepth(root.right, max_depth+1)

            return max(left_max, right_max)
        
        return calculateDepth(root)
            
