class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)

        arr = []
        for num, cnt in freq.items():
            arr.append((cnt, num))
        arr.sort()

        res = []
        for _ in range(k):
            res.append(arr.pop()[1])
        return res
