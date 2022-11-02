class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sn = set(sentence)
        
        return len(sn) == 26