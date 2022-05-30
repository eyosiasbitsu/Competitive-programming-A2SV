class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d = abs(dividend)
        dv = abs(divisor)
        out = 0
        
        while d >= dv:
            temp = dv
            mul = 1
            
            while d >= temp:
                d -= temp
                out += mul
                mul += mul
                temp += temp
        
        if((dividend < 0 and divisor >= 0) or 
           (divisor < 0 and dividend >= 0)):
            out = -out
            
        print(out)
        return min(2147483647,max(-2147483648
,out))