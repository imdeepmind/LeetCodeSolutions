class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):
            if r < 0 or c < 0:
                return 0
            
            if r >= ROWS or c >= COLS:
                return 0
            
            if grid[r][c] != 1:
                return 0
            
            if (r, c) in visited:
                return 0
            
            visited.add((r, c))

            s = 0
            for dr, dc in directions:
                s += dfs(r + dr, c + dc)
            
            return 1 + s

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(dfs(r, c), max_area)
        
        return max_area