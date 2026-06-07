class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initialize two pointers left, right
        # while left < right: check for a pair that equals target
        # return left + 1, right + 1

        left, right = 0, len(numbers) - 1
        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left+1, right+1]
            elif current > target:
                right -= 1
            else:
                left += 1

