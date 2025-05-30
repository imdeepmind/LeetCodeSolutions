"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            all_same = True

            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        all_same = False
                        break
            
            if all_same:
                return Node(grid[r][c], True)
            
            n = n // 2
            top_left = dfs(n, r, c)
            top_right = dfs(n , r, c + n)
            bottom_left = dfs(n, r + n, c)
            bottom_right = dfs(n, r + n, c + n)

            return Node(
                grid[r][c],
                False,
                top_left,
                top_right,
                bottom_left,
                bottom_right
            )
        
        return dfs(len(grid), 0, 0)