class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for k in range(i + 1, len(temperatures)):
                if temperatures[k] > temperatures[i]:
                    res[i] = (k - i)
                    break
        return res