class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        v1 = cost[0]
        v2 = cost[1]
        
        for i in range(2, len(cost)):
            temp = min(v1 + cost[i], v2 + cost[i])
            v1 = v2
            v2 = temp
        
        return min(v1, v2)