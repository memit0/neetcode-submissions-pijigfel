# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs)-1)
        return pairs
        
    def quickSortHelper(self, arr, s, e):
        # If the length is less than 1 base case return arr
        if e - s + 1 <= 1:
            return
        # pick pivot and left pointer
        left, pivot = s, arr[e]

        # in the range if arr[i] less than pivot
        for i in range(s, e):     
            # swap elements
            if arr[i].key < pivot.key:
                arr[left], arr[i] = arr[i], arr[left]
                # increment left 
                left += 1

        # move pivot in between left and right sides
        arr[e] = arr[left]
        arr[left] = pivot

        # quick sort left 
        self.quickSortHelper(arr, s, left-1)

        # quick sort right
        self.quickSortHelper(arr, left+1, e)

