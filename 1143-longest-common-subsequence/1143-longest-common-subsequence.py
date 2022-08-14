class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]
        
        for i in range(1,len(dp)):
            for j in range(1, len(dp[0])):
                c1 = text1[j - 1]
                c2 = text2[i - 1]
                
                if c1 == c2:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                
                else:
                    dp[i][j] = max(dp[i -1][j], dp[i][j - 1])
        
        return dp[-1][-1]