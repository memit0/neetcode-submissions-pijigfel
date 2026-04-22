class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0] == 1:
            return -1

        
        q = deque()
        visit = set()
        q.append((0,0))
        visit.add((0,0))

        length = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1,-1], [1,-1], [-1,1]]
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if nr == ROWS or nc == COLS or (nr, nc) in visit or grid[nr][nc] == 1 or min(nr, nc) < 0:
                        continue
                    q.append((nr,nc))
                    visit.add((nr,nc))
            
            length += 1
        
        return -1
