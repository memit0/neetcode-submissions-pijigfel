class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        i, j = 0, len(heights) -1

        while i <= j:
            total = (j - i) * min(heights[i], heights[j])

            maxArea = max(maxArea, total)

            if heights[j] < heights[i]:
                j -= 1
            else:
                i += 1

        return maxArea
