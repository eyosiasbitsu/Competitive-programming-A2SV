class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i = 0
        
        for k in range(len(words)):
            temp = words[k]
            
            j = 0
            
            if i >= len(s):
                return True
            
            while j < len(temp) and i < len(s) and s[i] == temp[j]:
                i += 1
                j += 1
                
            if j < len(temp):
                return False
            
        return i >= len(s)