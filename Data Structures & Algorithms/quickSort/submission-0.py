# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.helper(pairs, 0, len(pairs)-1)

    def helper(self, arr, s, e): 
        #base case:
        if e <= s:
            return arr
        
        pivot = arr[e].key
        left = s

        for i in range(s, e):
            if arr[i].key < pivot:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1

        arr[e], arr[left] = arr[left], arr[e]

        
        self.helper(arr, s, left-1)
        self.helper(arr, left+1, e)
        
        return arr
