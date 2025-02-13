# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def calculateDiameter(root):
            nonlocal max_depth

            if not root:
                return 0

            left, right = calculateDiameter(root.left), calculateDiameter(root.right)

            max_depth = max(max_depth, left+right)

            return max(left, right) + 1
        
        calculateDiameter(root)

        return max_depth

