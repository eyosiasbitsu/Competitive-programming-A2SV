class Solution:
    def climbStairs(self, n: int) -> int:
        
        fv = 1
        sv = 1
        
        for i in range(2, n + 1):
            temp = fv + sv
            fv = sv
            sv = temp
            
        return sv