class Solution:
    def minimumSum(self, num: int) -> int:
        num = list(str(num))
        
        num.sort()
        new1 = num[0] + num[-1]
        new2 = num[1] + num[2]
        
        return int(new2) + int(new1)
    
        
        