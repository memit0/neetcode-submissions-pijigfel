class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Input: 2d matrix
        # Return: True, False

        # Check each column to ensure no numbers are duplicates
        # Check each row to ensure no numbers are duplicates
        # Check each 3x3 grud to ensure no numbers are duplicates

        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(9):
            row_seen = set()
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                # append to the correct box based on r, c
                box_index = (r // 3) * 3 + (c // 3)
                
                if val in row_seen or val in cols[c] or val in boxes[box_index]: 
                    return False
                row_seen.add(val)
                cols[c].add(val)
                boxes[box_index].add(val)

        return True