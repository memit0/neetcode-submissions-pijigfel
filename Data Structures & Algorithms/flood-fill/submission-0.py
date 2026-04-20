class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initVal = image[sr][sc]

        def dfs(image, r, c):
            ROWS, COLS = len(image), len(image[0])
            if min(r,c) < 0 or r == ROWS or c == COLS or image[r][c] != initVal or image[r][c] == color:
                return
            
            if image[r][c] != color:
                image[r][c] = color
            
            dfs(image, r+1, c)
            dfs(image, r-1, c)
            dfs(image, r, c+1)
            dfs(image, r, c-1)

        dfs(image, sr, sc)
        return image

