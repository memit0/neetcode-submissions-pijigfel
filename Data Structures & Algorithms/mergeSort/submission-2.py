# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs)-1)

    def mergeSortHelper(self, pairs, s, e):
        if e - s + 1 <= 1:
            return pairs
        
        m = (s + e) // 2 

        self.mergeSortHelper(pairs, s, m)
        self.mergeSortHelper(pairs, m + 1, e)

        self.merge(pairs, s, m, e)

        return pairs

    def merge(self, pairs, s, m, e):
        left_array = pairs[s: m + 1]
        right_array = pairs[m + 1: e + 1]
        
        i, j, k = 0, 0, s 

        while i < len(left_array) and j < len(right_array):
            left_val, right_val = left_array[i], right_array[j]

            if left_val.key <= right_val.key:
                pairs[k] = left_val
                i += 1
            else:
                pairs[k] = right_val
                j += 1
            k += 1
        
        while i < len(left_array):
            pairs[k] = left_array[i]
            i += 1
            k += 1
        while j < len(right_array):
            pairs[k] = right_array[j]
            j += 1
            k += 1
        


    
