class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        l = 0
        r = 3
        res = 0
        
        while r <= len(s):
            cur = set(s[l:r])
            
            if len(cur) == 3:
                res += 1
            
            r += 1
            l += 1
        
        return res