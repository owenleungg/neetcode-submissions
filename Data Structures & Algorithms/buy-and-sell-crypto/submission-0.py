class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_buy = 999
        for i in range(len(prices)):
            if prices[i] < lowest_buy:
                lowest_buy = prices[i]
            profit = prices[i] - lowest_buy
            if profit > max_profit:
                max_profit = profit
        return max_profit