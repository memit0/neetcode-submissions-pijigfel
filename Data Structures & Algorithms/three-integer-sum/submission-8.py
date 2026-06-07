class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            l, r = i + 1, len(nums) -1

            # skip duplicates
            prev_num = nums[i-1] if i > 0 else float('inf')
            if prev_num == nums[i]:
                continue

            while l < r:
                # skip duplicates
                prev_num = nums[l-1] if l > i + 1 else float('inf')
                if prev_num == nums[l]:
                    l += 1 
                    continue

                current_sum = nums[i] + nums[l] + nums[r]

                if current_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif current_sum > 0:
                    r -= 1
                else:
                    l += 1
        
        return res
