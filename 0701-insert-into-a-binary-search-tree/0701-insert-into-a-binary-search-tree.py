# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)
        if not root:
            return newNode

        head = root

        while head:
            if head.val >= val:
                if head.left:
                    head = head.left
                else:
                    head.left = newNode
                    break
            elif head.val < val:
                if head.right:
                    head = head.right
                else:
                    head.right = newNode
                    break
        
        return root