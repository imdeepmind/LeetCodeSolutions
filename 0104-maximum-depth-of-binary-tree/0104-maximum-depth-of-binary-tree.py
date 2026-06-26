# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def maxd(head):
            nonlocal max_depth

            if not head:
                return 0
            
            max_depth = 1 + max(maxd(head.left), maxd(head.right))

            return max_depth
        
        return maxd(root)
            