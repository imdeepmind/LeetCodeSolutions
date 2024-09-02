# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _isValidBST(self, head, leftRange, rightRange):
        if not head:
            return True
       
        if not (leftRange < head.val and head.val < rightRange):
            return False
       
        return (
            self._isValidBST(head.left, leftRange, head.val) and
            self._isValidBST(head.right, head.val, rightRange)
        )

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isValidBST(root, float('-inf'), float('inf'))
