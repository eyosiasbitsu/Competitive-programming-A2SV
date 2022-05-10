class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
    
        for w in words:
            if self.isplai(w):
                return w
        
        return ""
    
    def isplai(self,word):
        i = 0
        j = len(word) - 1
        
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
            
        return True
    