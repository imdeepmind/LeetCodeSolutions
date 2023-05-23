# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLeaf(self, node: TreeNode):
        if node.left or node.right:
            return False
        
        return True
    
    def minDepth(self, root: Optional[TreeNode], leaf_dist = 99999, node_depth = 0) -> int:
        if not root:
            return 0
        
        node_depth += 1
        
        
        if self.isLeaf(root):
            if node_depth <= leaf_dist:
                leaf_dist = node_depth
        
        if root.left:
            leaf_dist = self.minDepth(root.left, leaf_dist, node_depth)
        
        if root.right:
            leaf_dist = self.minDepth(root.right, leaf_dist, node_depth)
        
        return leaf_dist