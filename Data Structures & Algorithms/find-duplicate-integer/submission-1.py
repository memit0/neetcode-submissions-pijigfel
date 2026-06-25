class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i - 1] or nums[i] == nums[i + 1]:
                return nums[i]
        

# nums=[7,9,7,4,2,8,7,7,1,5]