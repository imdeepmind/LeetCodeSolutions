# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxValue = float('-inf')

        def dfs(node):
            nonlocal maxValue

            if not node: return 0

            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            maxValue = max(maxValue, node.val + leftMax + rightMax)

            return max(leftMax, rightMax) + node.val
        
        dfs(root)
        return maxValue

