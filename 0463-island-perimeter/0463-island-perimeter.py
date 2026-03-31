class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(i=0, j=0):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 1
            elif (i ,j) in visit:
                return 0
            
            visit.add((i, j))
            return dfs(i-1, j) + dfs(i, j-1) + dfs(i+1, j) + dfs(i, j+1)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    return dfs(i, j)

        return 0