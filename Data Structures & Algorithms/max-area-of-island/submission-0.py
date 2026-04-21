class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(grid, r, c):
            ROWS, COLS = len(grid), len(grid[0])

            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0

            grid[r][c] = 0  # mark visited

            return (1 +
                dfs(grid, r + 1, c) +
                dfs(grid, r - 1, c) +
                dfs(grid, r, c + 1) +
                dfs(grid, r, c - 1))
        

        maxArea = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res = dfs(grid, r, c)
                    maxArea = max(maxArea, res)
        
        return maxArea