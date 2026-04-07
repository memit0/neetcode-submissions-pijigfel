class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, n in enumerate(nums):
            diff = target - n
            if n in dic.keys():
                return sorted([i, dic[n]])
            dic[diff] = i