class Solution:
    def fib(self, n: int) -> int:
        self.cach = {}
        
        def dp(num):
            if num == 1:
                return 1
            
            if num == 0:
                return 0
            
            if num not in self.cach:
                self.cach[num] = dp(num - 1) + dp(num - 2)
            
            return self.cach[num]
        
        return dp(n)