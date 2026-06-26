# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def calculate(head):
            nonlocal res

            if not head:
                return 0
            
            left_diameter = calculate(head.left)
            right_diameter = calculate(head.right)

            res = max(res, left_diameter + right_diameter)

            return 1 + max(left_diameter, right_diameter)
        
        calculate(root)

        return res
