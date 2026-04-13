# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortHelper(pairs, 0, len(pairs)-1)
        
    def quickSortHelper(self, arr, s, e):
        if e - s <= 0:
            return arr

        left, pivot_index = s, e

        for i in range(s, e):
            if arr[i].key < arr[pivot_index].key:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1

        
        arr[left], arr[pivot_index] = arr[pivot_index], arr[left] # pivot is now at left index

        # split the arrays based on where the pivot is (not including pivot because it's already sorted!)
        self.quickSortHelper(arr, s, left - 1) 
        self.quickSortHelper(arr, left + 1, e)

        return arr


