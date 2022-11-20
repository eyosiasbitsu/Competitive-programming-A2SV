class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        st = ""
        
        for c in reversed(s):
            if c != "-":
                st += c.upper()
        
        result = ""
        count = k
        
        for i in range(len(st)):
            result += st[i]
            count -= 1
            
            if count == 0 and i != len(st) - 1:
                count = k
                result += "-"
        
        return "".join(reversed(result))
        
    
    
    
    