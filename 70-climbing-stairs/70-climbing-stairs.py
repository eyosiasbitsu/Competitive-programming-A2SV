class Solution:
    def climbStairs(self, n: int) -> int:
        
        f = 0
        fv = 1
        s = 1
        sv = 1
        
        for i in range(2, n + 1):
            temp = fv + sv
            f = s
            fv = sv
            s = i
            sv = temp
            
        return sv