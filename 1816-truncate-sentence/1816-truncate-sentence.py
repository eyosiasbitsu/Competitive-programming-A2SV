class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        for i in range(len(s)):
            if s[i] == " ":
                k -= 1
            
            if k == 0:
                break
        
        return s[:i] if i < len(s) - 1 else s