class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        chose = prices[0]
        profit = 0
        
        for i in prices:
            if i < chose:
                chose = i
            else:
                profit = max(profit,i-chose)
        
        return profit