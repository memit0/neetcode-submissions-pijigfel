class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSums = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            self.prefixSums.append(total)
        

    def sumRange(self, left: int, right: int) -> int:
        preRight = self.prefixSums[right]
        preLeft = self.prefixSums[left - 1] if left > 0 else 0

        return (preRight - preLeft)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)