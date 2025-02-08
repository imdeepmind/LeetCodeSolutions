class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1

        max_profit = 0

        while len(prices) > sell:
            if prices[sell] > prices[buy]:
                max_profit = max(prices[sell] - prices[buy], max_profit)
            else:
                buy = sell
            
            sell += 1
        
        return max_profit
