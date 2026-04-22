class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))

        time = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    nr, nc = dr + r, dc + c
                    if nr == ROWS or nc == COLS or min(nr, nc) < 0 or (nr, nc) in visit or grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] = 2
                    q.append((nr,nc))
                    visit.add((nr,nc))
            if q:
                time += 1
                
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return time
