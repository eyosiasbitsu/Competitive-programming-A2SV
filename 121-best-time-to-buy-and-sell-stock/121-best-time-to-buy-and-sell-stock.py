class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        big = -1
        
        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > big:
                big = prices[i]
            
            res = max(big - prices[i], res)
        
        return res