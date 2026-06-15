class Solution:
    def trap(self, height: List[int]) -> int:
        leftArray, rightArray = [], []
        leftMax, rightMax = height[0], height[-1]
        
        for n in height:
            leftMax = max(leftMax, n)
            leftArray.append(leftMax)
        
        for n in reversed(height):
            rightMax = max(rightMax, n)
            rightArray.append(rightMax)
        
        rightArray.reverse()

        res = 0
        for i in range(len(height)):
            minValue = min(rightArray[i], leftArray[i])

            res += minValue - height[i]
        
        return res
