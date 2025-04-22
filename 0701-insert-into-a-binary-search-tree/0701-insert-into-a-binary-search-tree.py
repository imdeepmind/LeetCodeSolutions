# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        anchor = root

        if not root:
            return TreeNode(val)

        while root:
            if root.val > val:
                if not root.left:
                    break

                root = root.left
            else:
                if not root.right:
                    break
                root = root.right
        
        if root.val > val:
            root.left = TreeNode(val)
        else:
            root.right = TreeNode(val)
        
        return anchor