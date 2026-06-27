# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kount = k
        res = root.val

        def dfs(head):
            nonlocal kount, res
            if not head:
                return
            
            dfs(head.left)
            if kount == 0:
                return

            res = head.val
            kount -= 1
            dfs(head.right)

            return
        
        dfs(root)

        return res