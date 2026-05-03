class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        curSum = 0
        res = 0

        for num in nums:
            curSum += num
            res += counts.get(curSum - k, 0)
            counts[curSum] += 1
        
        return res