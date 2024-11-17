# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, targetSum, currentSum):
            if not root:
                return False

            currentSum += root.val

            if targetSum == currentSum and not root.left and not root.right:
                return True

            return dfs(root.right, targetSum, currentSum) or dfs(root.left, targetSum, currentSum)
        
        return dfs(root, targetSum, 0)
