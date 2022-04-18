class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        pr = prices[0]
        
        for i in prices:
            
            if i < pr:
                pr = i
            if i - pr > profit:
                profit = i - pr
                
        return profit