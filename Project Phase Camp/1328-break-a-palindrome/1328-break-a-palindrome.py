class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        if len(palindrome) == 1:
            return ""
        
        l = list(palindrome)
        
        for i in range(len(l)//2):
            c = l[i]
            
            if c != "a":
                l[i] = "a"
                return "".join(l)
        
        l[-1] = "b"
        
        return "".join(l)