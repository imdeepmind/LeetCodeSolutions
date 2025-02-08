# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def calculate(root):
            nonlocal diameter

            if not root:
                return 0

            left_diameter = calculate(root.left)
            right_diameter = calculate(root.right)

            diameter = max(diameter, left_diameter + right_diameter)

            return max(left_diameter, right_diameter) + 1
        
        calculate(root)

        return diameter

            

