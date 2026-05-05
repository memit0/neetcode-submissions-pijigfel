class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (temperature, index)
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # Keep popping as long as the temperature is bigger and stack isn't empty
                stackT, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx
            stack.append((t,i))
        return res