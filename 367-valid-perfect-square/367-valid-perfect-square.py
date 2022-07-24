class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num
        n = 0
        
        while l < r:
            mid = (l+r)//2
            n += 1
            
            if mid**2 < num:
                l = mid + 1
            
            elif mid**2 > num:
                r = mid
            
            else:
                return True
        
        return False or num == 1