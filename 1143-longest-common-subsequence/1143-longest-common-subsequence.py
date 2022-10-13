class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = {}
        def dfs(i, j):
            if i == len(text1) or len(text2) == j:
                return 0
            
            if (i, j) not in dp:
                cur = 0
                if text1[i] == text2[j]:
                    cur = 1 + dfs(i + 1, j + 1)
                
                else:
                    cur = max(dfs(i + 1, j), dfs(i, j + 1))
                
                dp[(i, j)] = cur
            
            return dp[(i, j)]
        
        return dfs(0, 0)
    
    
    
    
    