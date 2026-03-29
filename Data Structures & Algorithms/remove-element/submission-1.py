class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, k = 0, len(nums) - 1
        while i <= k:
            if nums[i] == val:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 1
                # do not increment i; the swapped-in value at i needs checking
            else:
                i += 1
        return k + 1