class Solution:
    def climbStairs(self, n: int) -> int:
        
        f = (0, 1)
        s = (1, 1)
        
        for i in range(2, n + 1):
            temp = (i, f[1] + s[1])
            f = s
            s = temp
        
        return s[1]