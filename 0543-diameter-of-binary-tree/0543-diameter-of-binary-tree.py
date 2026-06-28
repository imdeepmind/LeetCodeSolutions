# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        md = 0
        def dfs(head):
            nonlocal md

            if not head:
                return 0
            
            ld = dfs(head.left)
            rd = dfs(head.right)

            md = max(md, ld + rd)

            return 1 + max(ld, rd)
        
        dfs(root)

        return md
