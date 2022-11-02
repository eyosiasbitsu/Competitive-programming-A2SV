class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        var = 1
        
        while var < n:
            var *= 4
            
        return var == n