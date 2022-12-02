class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False
        
        else:
            c1 = Counter(word1)
            c2 = Counter(word2)
            
            if (c1.keys() == (c2.keys())
            and sorted(c1.values()) == sorted(c2.values())):
                return True

            return False