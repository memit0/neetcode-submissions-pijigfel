class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        arr = []
        
        for key, val in cnt.items():
            arr.append((val,key))

        arr.sort()
        res = []
        print(arr)

        for i in range(k):
            if arr:
                res.append(arr.pop()[1])

        return res