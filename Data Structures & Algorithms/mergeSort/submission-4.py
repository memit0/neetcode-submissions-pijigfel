# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs)-1)
    
    def mergeSortHelper(self, arr, s, e):
        if (e - s) <= 0:
            return arr

        m = (s + e) // 2

        self.mergeSortHelper(arr, s, m) # sort left half recursively in place
        self.mergeSortHelper(arr, m + 1, e) # sort right half recursively in place

        self.merge(arr, s, m, e)

        return arr


    def merge(self, arr, s, m, e):
        left_arr = arr[s:m+1]
        right_arr = arr[m+1:e+1]

        i, j, k = 0, 0, s # the start of where we want to insert could change

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i].key <= right_arr[j].key:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
        


        


    
