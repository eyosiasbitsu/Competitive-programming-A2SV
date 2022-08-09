class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        ar = ['' for _ in range(numRows)]
        
        i = 0
        j = 0
        
        while i < len(s) and j < numRows:
            ar[j] += s[i]
            i += 1
            j += 1
        
        j -= 2
        
        up = True
        
        while i < len(s):
            if up:
                while i < len(s) and j >= 0:
                    ar[j] += s[i]
                    j -= 1
                    i += 1
                
                j += 2
                up = False
            
            else:
                while i < len(s) and j < numRows:
                    ar[j] += s[i]
                    j += 1
                    i += 1
                
                j -= 2
                up = True
        
        res = ''.join(ar)
        return res
                    
                
                
                
                
                
                
                
                