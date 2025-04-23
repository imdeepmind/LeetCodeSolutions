# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')

        def calculate_path_sum(root):
            nonlocal max_path

            if not root:
                return 0

            left = calculate_path_sum(root.left)
            right = calculate_path_sum(root.right)
            
            max_path = max(max_path, root.val + left + right)

            return max(left, right) + root.val
        
        calculate_path_sum(root)

        return max_path