class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visits = set()
        def dfs(i, j):
            if i < 0 or j < 0:
                return 1

            if i >= len(grid) or j >= len(grid[0]):
                return 1

            if grid[i][j] == 0:
                return 1
            
            if (i,j) in visits:
                return 0
            
            visits.add((i,j))
            
            return dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    return dfs(i, j)