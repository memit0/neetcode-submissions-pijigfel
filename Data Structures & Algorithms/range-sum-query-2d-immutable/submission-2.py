class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefix = [[0]]
            return

        n, m = len(matrix), len(matrix[0])
        self.prefix = [[0] * m for _ in range(n)]

        for r in range(n):
            row_sum = 0
            for c in range(m):
                row_sum += matrix[r][c]
                above = self.prefix[r-1][c] if r > 0 else 0
                self.prefix[r][c] = above + row_sum


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight = self.prefix[row2][col2]
        above = self.prefix[row1 - 1][col2] if row1 > 0 else 0
        left = self.prefix[row2][col1 - 1] if col1 > 0 else 0
        topLeft = self.prefix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
    
        return bottomRight - above - left + topLeft # since subtract by left and above the left and above both have the topleft section, so you're subtracting twice therefore you need to add once back