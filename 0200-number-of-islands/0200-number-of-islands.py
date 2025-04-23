class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        no_of_islands = 0
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(i, j):
            if i < 0 or j < 0:
                return
            
            if i >= ROWS or j >= COLS:
                return 
            
            if grid[i][j] == "0":
                return
            
            if (i, j) in visited:
                return

            if grid[i][j] == "1":
                visited.add((i, j))
                for dr, dc in directions:
                    dfs(i + dr, j + dc)
            
            return
                
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i, j)
                    no_of_islands += 1

        return no_of_islands