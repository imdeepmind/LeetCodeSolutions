# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(head):
            if not head:
                return

            head.left, head.right = head.right, head.left
            self.invertTree(head.left)
            self.invertTree(head.right)

            return root

        return invert(root)

