class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        totalIslands = 0

        def dfs(grid, r, c):
            ROWS, COLS = len(grid), len(grid[0])

            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == "0":
                return 
            
            if grid[r][c] == "1":
                grid[r][c] = "0"
            
            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    totalIslands += 1
                    dfs(grid, r, c)
        
        return totalIslands
        
