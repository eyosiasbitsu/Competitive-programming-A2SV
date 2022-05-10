class Solution:
    def climbStairs(self, n: int) -> int:
            
            self.cach = {}
        
            def dp(n,st):
                if st == n or st == n-1:
                    return 1

                if st not in self.cach:
                    self.cach[st] = dp(n,st + 1) + dp(n, st+2)

                return self.cach[st]
            
            return dp(n,0)
            
            
        
            