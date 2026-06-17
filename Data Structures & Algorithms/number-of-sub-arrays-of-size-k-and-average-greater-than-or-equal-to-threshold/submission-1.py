class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # all sub-arrays of size k that have a average greater than or equal to threshold
        # average sum(subarray) / len(subarray)
        # return the total number of subarrays with this contraint
        l = 0
        res = 0
        for r in range(k-1, len(arr)):
            # Check if the subarray average is greater than or equal to treshold
            if sum(arr[l:r+1]) / len(arr[l:r+1]) >= threshold:
                res += 1  
            l += 1
        return res
