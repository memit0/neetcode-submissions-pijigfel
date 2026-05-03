class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefix = [[0]]
            return 

        self.prefix = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for r in range(len(matrix)):
            row_sum = 0
            for c in range(len(matrix[0])):
                row_sum += matrix[r][c]
                above = self.prefix[r - 1][c] if r > 0 else 0
                self.prefix[r][c] = above + row_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight = self.prefix[row2][col2]
        top = self.prefix[row1 - 1][col2] if row1 > 0 else 0
        left = self.prefix[row2][col1 - 1] if col1 > 0 else 0
        topLeft = self.prefix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return bottomRight - top - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)