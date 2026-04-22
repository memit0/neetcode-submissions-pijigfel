class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0] == 1:
            return -1

        q = deque()
        q.append((0,0))
        visit = set()
        visit.add((0,0))

        length = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                neighbors = [[0 , 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    nr, nc = dr + r, dc + c
                    if nr == ROWS or nc == COLS or min(nr, nc) < 0 or grid[nr][nc] == 1 or (nr, nc) in visit:
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc))
                
            length += 1
        
        return -1
