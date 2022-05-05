class Solution:
    def fib(self, n: int) -> int:
        
        self.cach = {}
        
        def dp(n):
            if n <= 1:
                return n
            
            if n not in self.cach:
                self.cach[n] = dp(n-1) + dp(n-2)
            
            return self.cach[n]
        
        return dp(n)