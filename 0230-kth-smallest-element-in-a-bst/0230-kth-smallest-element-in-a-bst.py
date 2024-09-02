# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _parse_tree(self, root, resps, k):
        if len(resps) > k:
            return

        if not root:
            return

        self._parse_tree(root.left, resps, k)
        resps.append(root.val)
        self._parse_tree(root.right, resps, k)

        return

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        resps = []
        self._parse_tree(root, resps, k)

        return resps[k - 1]