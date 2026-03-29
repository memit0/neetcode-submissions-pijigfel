class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        i = 0
        max_count = 0
        while i < len(nums):
            count += 1
            if nums[i] == 0:
                count = 0
            max_count = max(count, max_count)
            i += 1

        return max_count