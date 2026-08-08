# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.mergeSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
    
    def mergeSortHelper(self, pairs, s, e):
        if e - s + 1 <= 1:
            return

        m = (s + e) // 2

        self.mergeSortHelper(pairs, s, m)
        self.mergeSortHelper(pairs, m + 1, e)

        self.merge(pairs, s, m, e)

    def merge(self, pairs, s, m, e):
        leftArray = pairs[s:m+1]
        rightArray = pairs[m+1:e+1]

        i, j, k = 0, 0, s

        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i].key <= rightArray[j].key:
                pairs[k] = leftArray[i]
                i += 1
            else:
                pairs[k] = rightArray[j]
                j += 1
            k += 1

        while i < len(leftArray):
            pairs[k] = leftArray[i]
            i += 1
            k += 1

        
        while j < len(rightArray):
            pairs[k] = rightArray[j]
            j += 1
            k += 1


            
