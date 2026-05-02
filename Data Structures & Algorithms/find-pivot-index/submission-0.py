class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix, postfix = [], []
        total = 0 
        for num in nums:
            total += num
            prefix.append(total)

        total = 0
        reverse_nums = reversed(nums)
        for num in reverse_nums:
            total += num
            postfix.append(total)

        postfix = reversed(postfix)
        i = 0
        for x, y in zip(prefix, postfix):
            print(x,y)
            if x == y:
                return i
            i += 1

        return -1