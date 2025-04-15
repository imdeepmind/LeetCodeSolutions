class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy, sell = 0, 1

        while len(prices) > sell:
            if prices[sell] > prices[buy]:
                max_profit = max(prices[sell] - prices[buy], max_profit)
            else:
                buy = sell
            
            sell += 1
        
        return max_profit
