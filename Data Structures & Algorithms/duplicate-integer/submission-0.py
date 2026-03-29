class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_list = []
        for num in nums:
            if num in new_list:
                return True
            else:
                new_list.append(num)
        return False  
         