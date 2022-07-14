class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        for i in range(len(s)):
            r = i
            l = i
            temp = 0
            
            while r < len(s) and l >= 0 and s[l] == s[r]:
                if r-l + 1 > len(res):
                    res = s[l : r+1]
                    
                r += 1
                l -= 1
            
            r,l = i,i-1
            
            while r < len(s) and l >= 0 and s[l] == s[r]:
                if r-l + 1 > len(res):
                    res = s[l : r+1]
                    
                r += 1
                l -= 1
                
        return res