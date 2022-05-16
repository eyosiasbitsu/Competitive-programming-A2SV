class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = 1
        idx = 0
        for i in range(len(s)//2,0,-1):
            if len(s) % i == 0:
                if s == s[:i]*(len(s)//i):
                    return True
        
        return False
        
        