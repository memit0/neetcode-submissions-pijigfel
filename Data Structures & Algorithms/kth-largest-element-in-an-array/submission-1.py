class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[len(nums)-k]

        # follow up solve without sorting

        nums = [-n for n in nums]
        heapq.heapify(nums)

        for i in range(k-1):
            heapq.heappop(nums)
        
        return -heapq.heappop(nums)