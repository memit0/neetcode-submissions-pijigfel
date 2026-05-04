class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = [[0] * 9 for _ in range(9)]
        boxes = [[0] * 9 for _ in range(9)]
        for r in range(len(board)):
            row_set = set()
            for c in range(len(board[0])):
                v = board[r][c]
                if v == '.':
                    continue
                
                box_idx = (r // 3) * 3 + (c // 3)

                if v in boxes[box_idx] or v in row_set or v in col[c]:
                    return False

                row_set.add(v)
                col[c].append(v)
                boxes[box_idx].append(v)
        return True