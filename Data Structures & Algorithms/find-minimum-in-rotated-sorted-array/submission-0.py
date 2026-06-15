class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                # minimum is in the right half
                l = mid + 1
            else:
                # minimum is in the left half
                r = mid
        
        return nums[l] 


        

             

        
