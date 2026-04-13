class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # based on the contraint o(log(n*m)) we know we need to run binary search twice
        # run once to find row then again to find col

        l, r = 0, len(matrix) - 1
        while l <= r:
            row = (l+r) // 2
            if matrix[row][0] < target and matrix[row][-1] < target:
                l = row + 1
            elif matrix[row][0] > target and matrix[row][-1] > target:
                r = row - 1
            else:
                break # else we're in the correct row just break out of trying to find the row
        
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            col = (l+r) // 2
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = col + 1
            else:
                r = col - 1
        print(row,col)
        return False
