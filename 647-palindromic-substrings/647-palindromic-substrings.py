class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        
        for i in range(len(s)):
            count = 0
            
            l,r = i, i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                count += 1
                l -= 1
                r += 1
            
            l,r = i, i + 1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                count += 1
                l -= 1
                r += 1
            
            res += count
        
        return res
                
                
                
                
                
                
                
                
                