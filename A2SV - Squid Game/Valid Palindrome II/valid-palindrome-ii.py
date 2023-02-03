class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                return self.isPalindrome(s[i:j]) or self.isPalindrome(s[i + 1:j+1])
            
            i += 1
            j -= 1
        
        return True
    
    def isPalindrome(self, word):
        i = 0
        j = len(word) - 1
        
        while i < j:
            if word[i] != word[j]:
                return False
            
            i += 1
            j -= 1
            
        return True
