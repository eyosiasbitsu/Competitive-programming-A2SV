class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.cach = {}
    
        def dp(idx1,idx2):
            if idx1 >= len(text1) or idx2 >= len(text2):
                return 0
            
            if (idx1,idx2) not in self.cach:
                
                if text1[idx1] == text2[idx2]:
                    self.cach[(idx1,idx2)] = 1 + dp(idx1 + 1, idx2 + 1)
                else:
                    self.cach[(idx1,idx2)] = max(dp(idx1 + 1, idx2) ,dp(idx1,idx2 + 1))
            
            return self.cach[(idx1,idx2)]
        
        return dp(0,0)
        