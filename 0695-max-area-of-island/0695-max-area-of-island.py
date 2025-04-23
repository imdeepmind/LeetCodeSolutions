class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0:
                return 0
            
            if r >= ROWS or c >= COLS:
                return 0
            
            if (r, c) in visited:
                return 0
            
            if grid[r][c] == 0:
                return 0

            visited.add((r, c))

            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)


        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = max(dfs(r, c), area)

        return area