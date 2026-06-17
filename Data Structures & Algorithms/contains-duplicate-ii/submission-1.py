class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # nums[i] == nums[j]
        # abs(i - j) <= k

        # nums = [1,2,3,1] k = 3
        # window size: 4 (k + 1)
        # r - l + 1 <= k + 1 -> r - l <= k

        # return true if there are equal indices
        # return false if no equal indices

        hashset = set()
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                hashset.remove(nums[l])
                l += 1
            if nums[r] in hashset:
                return True
            hashset.add(nums[r])
        
        return False