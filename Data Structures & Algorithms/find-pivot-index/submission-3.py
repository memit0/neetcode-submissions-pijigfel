class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            leftSum += nums[i]
            rightSum = total - leftSum

            if leftSum - nums[i] == rightSum: # numbers strictly to the left; doesn't include the pivot
                return i
        
        return -1