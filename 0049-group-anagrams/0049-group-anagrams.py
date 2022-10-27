class Solution:
    def groupAnagrams(self,  strs: List[str]) -> List[List[str]]:
        
        words = defaultdict(list)
        
        for i in range(len(strs)):
            word = "".join(sorted(strs[i]))
            words[word].append(i)
        
        result = []
        for word in words:
            temp = []
            for idx in words[word]:
                temp.append(strs[idx])
                
            result.append(temp)
            
        return result