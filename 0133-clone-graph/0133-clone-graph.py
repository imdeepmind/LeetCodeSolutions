"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        mapper = {}

        def clone_nodes(node):
            if not node:
                return
 
            mapper[node] = Node(node.val, [])

            for child in node.neighbors:
                if child not in mapper:
                    clone_nodes(child)
            
            return

        def clone_edges(node):
            if not node:
                return
            
            if mapper[node].neighbors:
                return
            
            neighbors = []
            for child in node.neighbors:
                neighbors.append(mapper[child])
            
            mapper[node].neighbors = neighbors

            for child in node.neighbors:
                clone_edges(child)
            
            return
            
        clone_nodes(node)
        clone_edges(node)

        return mapper[node]


