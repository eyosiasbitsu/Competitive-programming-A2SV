class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or len(words) == 0:
            return
        
        count = {}
        wordLength = len(words[0])
        res = []
        wordsLength = len(words)*wordLength
        
        for w in words:
            count[w] = count.get(w, 0) + 1
        
        for l in range(len(s) - wordsLength + 1):
            
            seen = {}
            
            for r in range(len(words)):
                wordindex = l + r * wordLength
                
                tempword = s[wordindex : wordindex + wordLength]
                
                if tempword not in count:
                    break
                
                seen[tempword] = seen.get(tempword, 0) + 1
                
                if seen[tempword] > count[tempword]:
                    break
            
            if seen == count:
                res.append(l)
        
        return res
