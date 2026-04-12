class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i < m+n and j < n:
            if i >= m + j or nums2[j] < nums1[i]:
                self.shift(nums1, i, m - 1 + j)
                nums1[i] = nums2[j]
                j += 1

            i += 1 
        
    def shift(self, arr, s, j): 
        for i in range(j, s - 1, -1):
            arr[i+1] = arr[i]
    

