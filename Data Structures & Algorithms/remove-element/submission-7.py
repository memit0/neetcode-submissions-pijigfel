class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Two pointer approach with swapping 
        # nums = [3,2,2,3] val=3
        # left, right = 0, 3

        # move right pointer after swap
        # move left pointer if current element at position is not val
        # keep going until left < right
        # return the index of the left pointer

        # Input: nums = [0,1,2,2,3,0,4,2], val = 2
        # [0,1,2,2,3,0,4,2]
        # [0,1,4,2,3,0,2,2]
        
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                # Swap 
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        
        return left