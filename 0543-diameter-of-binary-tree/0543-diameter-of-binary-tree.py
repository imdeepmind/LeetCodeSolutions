# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def calculate_diameter(head):
            nonlocal diameter

            if not head:
                return 0
            
            left_diameter = calculate_diameter(head.left)
            right_diameter = calculate_diameter(head.right)

            diameter = max(diameter, left_diameter + right_diameter)

            return max(left_diameter, right_diameter) + 1
        
        calculate_diameter(root)

        return diameter

