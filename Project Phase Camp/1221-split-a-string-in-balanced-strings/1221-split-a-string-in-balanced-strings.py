class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        countl = 0
        countr = 0
        l = 0
        r = 0
        result = 0
        
        while r < len(s):
            if s[r] == "R":
                countr += 1
            
            else:
                countl += 1
                
            if countl == countr:
                result += 1
                countl = 0
                countr = 0
            
            r += 1
            
        return result
    
    
    
    
    
    
    
    