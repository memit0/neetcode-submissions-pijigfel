class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = collections.Counter(nums)

        for val in freq.values():
            if val > 1:
                return True
        
        return False