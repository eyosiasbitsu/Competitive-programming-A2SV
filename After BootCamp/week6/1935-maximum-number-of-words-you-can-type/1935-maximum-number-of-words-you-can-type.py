class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        
        found_broken = 0
        res = 0
        
        for i in range(len(text)):
            if text[i] == " ":
                if not found_broken:
                    res += 1
                found_broken = 0
                
            elif text[i] in broken:
                found_broken += 1
        
        if not found_broken:
            res += 1
        
        return res
                    