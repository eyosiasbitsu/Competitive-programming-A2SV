class Solution:
    def numDecodings(self, s: str) -> int:
        
        self.cach = {}
        
        def dp(idx):
            if idx >= len(s):
                return 1
            
            if s[idx] == "0":
                return 0
            
            if idx == len(s) - 1 and s[idx] != 0:
                return 1
            
            if idx not in self.cach:
                if s[idx] == "1":
                    self.cach[idx] = dp(idx+1) + dp(idx+2)
                    
                elif s[idx] == "2":
                    self.cach[idx] = dp(idx + 1)
                    
                    if idx < len(s) - 1 and s[idx + 1] <= '6':
                        self.cach[idx] += dp(idx+2)
                        
                else:
                    self.cach[idx] = dp(idx+1)
                    
            return self.cach[idx]
        
        return dp(0)