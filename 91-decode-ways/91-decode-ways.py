class Solution:
    def numDecodings(self, s: str) -> int:
        self.cach = {}
        
        def dp(i):
            if i >= len(s):
                return 1
            
            if i in self.cach:
                return self.cach[i]
            
            if s[i] == "0":
                return 0
            
            res = dp(i + 1)
            
            if((i+1 < len(s)) and 
               (s[i] == "1" or 
                (s[i] == "2" and s[i+1] in "0123456"))):
                res += dp(i+2)
            
            self.cach[i] = res
            
            return res
        
        return dp(0)
            