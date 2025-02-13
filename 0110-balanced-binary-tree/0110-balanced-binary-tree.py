# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkBalance(root):
            if not root:
                return 0
            
            leftB = checkBalance(root.left)
            rightB = checkBalance(root.right)

            if abs(leftB - rightB) > 1 or leftB == -1 or rightB == -1:
                return -1
            
            return max(leftB, rightB) + 1
        
        return checkBalance(root) != -1