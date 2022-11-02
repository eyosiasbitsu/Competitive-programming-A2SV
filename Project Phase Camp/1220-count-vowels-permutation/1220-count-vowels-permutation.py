class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        dp = [1,1,1,1,1]
        
        a,e,i,o,u = 0, 1, 2, 3, 4
        
        for j in range(2, n + 1):
            temp = [0, 0, 0, 0, 0]
            
            temp[a] = (dp[e] + dp[i] + dp[u])% (10**9+7)
            temp[e] = (dp[a] + dp[i])% (10**9+7)
            temp[i] = (dp[e] + dp[o])% (10**9+7)
            temp[o] = dp[i]
            temp[u] = dp[i] + dp[o]
            
            dp = temp
        
        return sum(dp)% (10**9+7)