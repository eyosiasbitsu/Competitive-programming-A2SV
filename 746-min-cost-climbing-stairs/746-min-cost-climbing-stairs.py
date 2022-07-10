class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        
        def rec(idx):
            if idx >= len(cost):
                return 0
            
            if idx not in dp:
                dp[idx] = cost[idx] + min(rec(idx + 1), rec(idx + 2))
            return dp[idx]
        
        return min(rec(0),rec(1))
                