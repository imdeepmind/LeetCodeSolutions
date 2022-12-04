class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, end = 0, 1
        maxProfit = 0
        
        while len(prices) > end:
            if prices[end] < prices[start]:
                start = end
            else:
                profit = prices[end] - prices[start]
                
                if profit > maxProfit:
                    maxProfit = profit
            
            end += 1
            
        return maxProfit