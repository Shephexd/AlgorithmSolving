class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 1000000
        max_profit = 0
        
        for idx, p in enumerate(prices):
            if p < min_price:
                min_price = p
            elif p - min_price > max_profit:
                max_profit = p - min_price
        
        return max_profit

