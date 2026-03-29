class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = -1
        for i in range(len(arr)-1, -1, -1):
            current_element = arr[i]

            arr[i] = current_max

            current_max = max(current_max, current_element)

        return arr