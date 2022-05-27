class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        w1 = defaultdict(int)
        w2 = defaultdict(int)
        
        for c in word1:
            w1[c] += 1
        
        for c in word2:
            w2[c] += 1
        
        for c in w2:
            if abs(w2[c] - w1[c]) > 3:
                return False
            
        for c in w1:
            if abs(w2[c] - w1[c]) > 3:
                return False
            
        return True