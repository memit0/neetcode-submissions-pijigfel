class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # The algorithm needs to be o(n) no sorting

        # Return (int) longest consecutive array (1,2,3,4)
        # Doesn't have to be consecutive in the array itself

        numSet = set(nums)
        longest = 0

        for n in nums:
            # Check if it's the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
                
        return longest



        
