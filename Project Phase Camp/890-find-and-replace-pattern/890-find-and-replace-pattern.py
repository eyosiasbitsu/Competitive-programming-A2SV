class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def is_same(w, pat):
            if len(w) != len(pat):
                return False
            
            dict1 = {}
            dict2 = {}
            
            for i in range(len(pat)):
                if (w[i] not in dict1 and 
                    pat[i] not in dict2):
                    
                    dict1[w[i]] = pat[i]
                    dict2[pat[i]] = w[i]
                
                
                if ((w[i] in dict1 and 
                     pat[i] not in dict2) or
                   (w[i] not in dict1 and 
                    pat[i] in dict2)):
                    return False
                
                if((w[i] in dict1 and 
                    pat[i] in dict2) and
                   (dict1[w[i]] != pat[i] or 
                    dict2[pat[i]] != w[i])):
                    return False 
            
            return True
        
        res = []
        
        for w in words:
            if is_same(w, pattern):
                res.append(w)
        
        return res
                
                
                
                
                
                
                
                
                
                
                    