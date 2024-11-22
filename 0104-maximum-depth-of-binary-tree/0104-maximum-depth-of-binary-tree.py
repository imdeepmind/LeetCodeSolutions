# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def calculate_depth(root, currentDepth=0):
            if not root:
                return currentDepth
            
            currentDepth += 1
            
            left_depth = calculate_depth(root.left, currentDepth)
            right_depth = calculate_depth(root.right, currentDepth)

            return max(left_depth, right_depth)
        
        return calculate_depth(root)