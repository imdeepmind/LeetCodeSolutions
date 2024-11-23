# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return

            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join([str(r) for r in res])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        res = data.split(",")
        i = 0

        def dfs():
            nonlocal i

            if res[i] == 'N':
                i += 1
                return None
            
            root = TreeNode(res[i])
            i += 1
            root.left = dfs()
            root.right = dfs()

            return root
        
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))