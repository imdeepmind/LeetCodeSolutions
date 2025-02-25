# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def is_balanced(root):
            if not root:
                return 0
            
            left = is_balanced(root.left)
            right = is_balanced(root.right)

            if abs(left - right) > 1 or left == -1 or right == -1:
                return -1
            
            return max(left, right) + 1
        
        return is_balanced(root) != -1
            
