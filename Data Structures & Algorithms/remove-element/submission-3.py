class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, k = 0, len(nums) - 1
        while i <= k:
            if nums[k] == val:
                k -= 1
            elif nums[i] == val:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 1
                i += 1
            else:
                i += 1
        return k + 1