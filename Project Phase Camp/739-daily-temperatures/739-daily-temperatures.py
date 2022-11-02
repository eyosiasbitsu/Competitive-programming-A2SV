class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stk = []

        for i in range(len(temperatures) - 1, -1, -1):
            
            while stk and stk[-1][1] <= temperatures[i]:
                stk.pop()
                
            temp = 0
            
            if stk:
                temp = stk[-1][0] - i
                
            stk.append((i, temperatures[i]))
            temperatures[i] = temp
            
        return temperatures