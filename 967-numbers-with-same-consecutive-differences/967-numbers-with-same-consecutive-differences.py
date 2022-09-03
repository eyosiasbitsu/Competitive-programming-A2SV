class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        res = []
        
        def rec(left, num):
            if left == 1:
                res.append(num)
                return
            
            digit = int(str(num)[-1])
            
            if digit + k <= 9:
                rec(left - 1, num*10 + (digit + k))
            
            if digit - k >= 0:
                rec(left - 1, num*10 + (digit - k))
        
        for i in range(1,10):
            rec(n, i)
        
        return set(res)