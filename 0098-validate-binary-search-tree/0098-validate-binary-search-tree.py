# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(head, minVal, maxVal):
            if not head:
                return True
            
            if head.val > minVal and maxVal > head.val:
                return is_valid(head.left, minVal, head.val) and is_valid(head.right, head.val, maxVal)
            
            return False
        
        return is_valid(root, float('-inf'), float('inf'))
            
