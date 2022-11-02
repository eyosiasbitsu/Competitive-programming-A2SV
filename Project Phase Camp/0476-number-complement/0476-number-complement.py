class Solution:
    def findComplement(self, num: int) -> int:
        
        result = 0
        power = 0
        
        while num:
            last_bit = num & 1
            num >>= 1
            
            if last_bit == 0:
                result += (2**power)
            
            power += 1
        
        return result