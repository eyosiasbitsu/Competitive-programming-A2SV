class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                return self.ispali(s[i:j]) or self.ispali(s[i + 1:j+1])
            
            i += 1
            j -= 1
        
        return True
    
    def ispali(self,word):
        i,j = 0,len(word)-1
        
        while i < j:
            if word[i] != word[j]:
                return False
            
            i += 1
            j -= 1
            
        return True