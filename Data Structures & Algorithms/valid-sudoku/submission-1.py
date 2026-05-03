class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            rows_seen = set()
            for c in range(9):
                v = board[r][c]

                if v == '.':
                    continue
                
                box_index = (r // 3) * 3 + (c // 3) # Calculate the box index

                if v in cols[c] or v in rows_seen or v in boxes[box_index]:
                    return False
                
                cols[c].add(v)
                rows_seen.add(v)
                boxes[box_index].add(v)

        return True