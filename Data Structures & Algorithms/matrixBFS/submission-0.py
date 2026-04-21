class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1

        q = deque()
        q.append((0,0))
        visited = set()
        visited.add((0,0))

        length = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                 
                neighbors = [[0,1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr, nc) in visited or grid[nr][nc] == 1:
                        continue # skip the invalid neighbor and move onto next

                    q.append((nr, nc))
                    visited.add((nr, nc))
            length += 1
        return -1