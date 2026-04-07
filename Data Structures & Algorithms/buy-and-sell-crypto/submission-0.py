class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_seen = prices[0]
        for p in prices:
            min_seen = min(min_seen, p)
            max_profit = max(max_profit, p - min_seen)
        
        return max_profit