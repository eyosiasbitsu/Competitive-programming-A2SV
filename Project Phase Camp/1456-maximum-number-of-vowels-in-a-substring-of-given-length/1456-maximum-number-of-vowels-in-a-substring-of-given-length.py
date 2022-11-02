class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vouls = {'a', 'e', 'i', 'o', 'u'}
        l = 0
        r = 0
        count = 0
        
        while r < k:
            if s[r] in vouls:
                count += 1
            
            r += 1
            
        res = count
        while r < len(s):
            if s[l] in vouls:
                count -= 1
            
            if s[r] in vouls:
                count += 1
                
            res = max(res, count)
            r += 1
            l += 1
        
        return res
            
            
            
            
            
            
            
            