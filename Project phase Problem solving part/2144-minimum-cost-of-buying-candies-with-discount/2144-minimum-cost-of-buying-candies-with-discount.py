class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        count = 0
        res = 0
        
        for i in range(len(cost) - 1,-1,-1):
            if count == 2:
                count = 0
            
            else:
                res += cost[i]
                count += 1
        
        return res