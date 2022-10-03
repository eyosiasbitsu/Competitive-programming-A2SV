class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        stk = []
        res = 0
        
        for i in range(len(colors)):
            while (stk and neededTime[stk[-1]] < neededTime[i] and 
                   colors[stk[-1]] == colors[i]):
                res += neededTime[stk.pop()]
                
            if (stk and neededTime[stk[-1]] >= neededTime[i] and 
                   colors[stk[-1]] == colors[i]):
                res += neededTime[i]
                continue
            
            stk.append(i)
        
        return res