# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(head):
            nonlocal res

            if not head:
                return 0
            
            left_height = dfs(head.left)
            right_height = dfs(head.right)

            res = max(res, left_height + right_height)

            return 1 + max(left_height, right_height)
        
        dfs(root)

        return res