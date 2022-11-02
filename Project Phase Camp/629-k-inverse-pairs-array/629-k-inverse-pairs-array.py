class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        
        if k == 0:
            return 1
        
        dp = [[0]*(k + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            dp[i][0] = 1
        
        if n < 2:
            return dp[n][k]
        
        dp[2][1] = 1
        
        for r in range(3, n + 1):
            mx = min(k, (n*(n - 1))//2)
            for c in range(1,mx + 1):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
                if c >= r:
                    dp[r][c] -= dp[r - 1][c - r]
        
        return dp[n][k]%mod
        