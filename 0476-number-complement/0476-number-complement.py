class Solution:
    def findComplement(self, num: int) -> int:
        
        comp = []
        while num:
            if num%2 == 0:
                comp.append(1)
            
            else:
                comp.append(0)
                
            num //= 2
        
        while comp and comp[-1] == 1:
            comp.pop()
                
        res = 0
        p = 0
        for i in range(len(comp)):
            res += (comp[i]*2**(p))
            p += 1
        
        return res
            
            
            
            
            