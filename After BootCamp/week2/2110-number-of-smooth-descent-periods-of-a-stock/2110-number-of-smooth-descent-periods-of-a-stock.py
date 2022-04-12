class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = 0
        i = 0
        j = 0
        self.dict1 = {}
        
        def dp(n):
            if n == 1:
                return 1
            
            if n not in self.dict1:
                self.dict1[n] = n + dp(n-1)
                
            return self.dict1[n]
        
        while j < len(prices):
            while j + 1 < len(prices) and prices[j] == prices[j+1] + 1:
                j += 1
            
            if j != i:
                res += dp(j - i + 1)
            else:
                res += 1
                
            j += 1
            i = j
            
        return res
            