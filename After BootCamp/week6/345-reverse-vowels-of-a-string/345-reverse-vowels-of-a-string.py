class Solution:
    def reverseVowels(self, s: str) -> str:
        
        s = list(s)
        ar = {"e",'i','o','a','u','E','I','O','A','U'}
        l = 0
        r = len(s) - 1
        
        while l <= r:
            
            if s[l] in ar and s[r] in ar:
                s[l],s[r] = s[r],s[l]
                l += 1
                r -= 1
                
            if l <= r and s[r] not in ar:
                r -= 1
                
            if l <= r and s[l] not in ar:
                l += 1
                
        return "".join(s)
        