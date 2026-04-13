class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = 0
        while l <= r:
            k = (l + r) // 2
            if self.isCorrect(piles, k, h) > 0:
                r = k - 1
                ans = k 
            else:
                l = k + 1
        
        return ans



    def isCorrect(self, piles, k, h):
        total = 0
        for pile in piles:
            total += math.ceil(pile / k)
        
        if total <= h:
            return 1 # is a valid k
        else:
            return -1 # is not a valid k
        
