class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        
        t.sort()
        s.sort()
        
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        
        return t[-1]