# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        def dfs(head, minVal):
            nonlocal good_nodes

            if not head:
                return
            
            if head.val >= minVal:
                good_nodes += 1
                minVal = head.val
            
            dfs(head.left, minVal)
            dfs(head.right, minVal)

            return
        
        dfs(root, root.val)

        return good_nodes