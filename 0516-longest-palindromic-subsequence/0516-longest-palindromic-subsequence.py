class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}
        
        def helper(i, j):
            if i == j:
                return 1
            
            if j < i:
                return 0
            
            if (i, j) not in dp:
                cur = 0
                if s[i] == s[j]:
                    cur = 2 + helper(i + 1, j - 1)
                
                else:
                    cur = max(helper(i + 1, j), helper(i , j - 1))
                
                dp[(i, j)] = cur
                
            return dp[(i, j)]
        
        return helper(0, len(s) - 1)
                
                
                
                