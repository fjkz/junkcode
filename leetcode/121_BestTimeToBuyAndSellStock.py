class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = 10**4 + 1
        max_profit = 0
        for p in prices:
            max_profit = max(max_profit, p - lowest_price)
            lowest_price = min(lowest_price, p)
        return max_profit
