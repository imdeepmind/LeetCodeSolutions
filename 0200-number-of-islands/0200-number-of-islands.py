class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        islands = 0
        visited = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0:
                return
            
            if r >= ROWS or c >= COLS:
                return
            
            if (r, c) in visited:
                return
            
            if grid[r][c] != "1":
                return
            
            visited.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
            return


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        
        return islands

