class Solution:
    def findComplement(self, num: int) -> int:
        
        res = 0
        _pow = 0
        
        while num:
            last_bit = num & 1
            num >>= 1
            
            if last_bit == 0:
                res += 2**(_pow)
                
            _pow += 1
        
        return res
            
            
            
            
            