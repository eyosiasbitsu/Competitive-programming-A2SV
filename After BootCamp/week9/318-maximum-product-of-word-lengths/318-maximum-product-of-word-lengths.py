class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        for i in range(len(words)):
            l = len(words[i])
            
            words[i] = (set(words[i]),l)
        
        res = 0
        
        for i in range(len(words)-1):
            for j in range(i+1 ,len(words)):
                w1,l1 = words[i]
                w2,l2 = words[j]
                
                if not set.intersection(w1,w2):
                    res = max(res,l1*l2)
        
        return res