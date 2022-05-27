class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        
        for c in word:
            if c.isupper():
                count += 1
                
        return True if ((count == 1 and word[0].isupper()) or
                         count == len(word) or
                       count == 0) else False