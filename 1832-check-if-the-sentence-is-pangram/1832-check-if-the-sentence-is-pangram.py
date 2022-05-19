class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ar = [False for _ in range(26)]
        
        for c in sentence:
            ar[ord(c)-ord('a')] |= True
        
        for b in ar:
            if not b:
                return False
        
        return True