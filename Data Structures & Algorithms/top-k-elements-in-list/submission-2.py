class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)

        res = [key for key, count in freq.most_common(k)]
        
        return res