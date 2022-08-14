class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = {}
        
        def dfs(idx1, idx2):
            if idx1 == len(text1) or idx2 == len(text2):
                return 0
            
            if (idx1, idx2) not in dp:
                if text1[idx1] == text2[idx2]:
                    dp[(idx1, idx2)] = 1 + dfs(idx1 + 1, idx2 + 1)
                
                else:
                    dp[(idx1, idx2)] = max(dfs(idx1 + 1, idx2), dfs(idx1, idx2 + 1))
            
            return dp[(idx1, idx2)]
        
        return dfs(0,0)