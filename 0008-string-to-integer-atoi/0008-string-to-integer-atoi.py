class Solution:
    def myAtoi(self, s: str) -> int:
        
        stk = []
        isNeg = False
        seen = 0
        
        for i in range(len(s)):
            if s[i] == "-" or s[i] == "+":
                if seen != 0 or stk:
                    break
                    
                if s[i] == "-":
                    isNeg = True
                
                seen += 1
                stk.append(0)
                
            elif ((s[i] != " " and not s[i].isnumeric()) or 
                    (not s[i].isnumeric() and stk) ):
                break
            
            elif s[i].isnumeric():
                stk.append(int(s[i]))
        
        res = 0
        for n in stk:
            res = res*10 + n
        
        if isNeg:
            return max(-res, -2147483648)
        
        return min(res, 2147483647)
                           