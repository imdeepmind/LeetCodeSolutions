# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(head):
            if not head:
                return
            
            res.append(head.val)
            dfs(head.left)
            dfs(head.right)
        
        dfs(root)

        return res