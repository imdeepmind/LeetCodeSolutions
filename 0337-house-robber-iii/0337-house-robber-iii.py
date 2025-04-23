# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(head):
            if not head:
                return [0, 0]
            
            left = dfs(head.left)
            right = dfs(head.right)

            return [
                head.val + left[1] + right[1],
                max(left) + max(right)
            ]
        
        return max(dfs(root))