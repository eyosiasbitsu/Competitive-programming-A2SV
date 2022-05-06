class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        res = 0
        
        for sent in sentences:
            res = max(sent.count(" ") + 1,res)
        
        return res