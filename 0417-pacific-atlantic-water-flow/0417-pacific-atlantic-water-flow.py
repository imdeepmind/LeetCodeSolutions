class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        pacific, atlantic = set(), set()

        def dfs(r, c, visits, prevHeight):
            if r < 0 or c < 0:
                return
            
            if r >= ROWS or c >= COLS:
                return
            
            if (r, c) in visits:
                return
            
            if heights[r][c] < prevHeight:
                return
            
            visits.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, visits, heights[r][c])
            
            return


        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res    
        