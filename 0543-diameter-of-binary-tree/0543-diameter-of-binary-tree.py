# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def check_diameter(root):
            nonlocal diameter

            if not root:
                return 0
            
            left_diameter = check_diameter(root.left)
            right_diameter = check_diameter(root.right)

            diameter = max(diameter, left_diameter + right_diameter)

            return max(left_diameter, right_diameter) + 1
        
        check_diameter(root)

        return diameter