class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        return self.toInt(firstWord) + self.toInt(secondWord) == self.toInt(targetWord)
    
    
    def toInt(self,word):
        res = 0
        
        for c in word:
            res = 10*res + ord(c) - ord("a")
        
        return res