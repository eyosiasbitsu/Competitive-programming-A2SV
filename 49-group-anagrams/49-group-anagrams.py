class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        
        for i in range(len(strs)):
            w = strs[i]
            w = sorted(w)
            w = "".join(w)
            
            dict1[w].append(strs[i])
                
        ar = []
        
        for k in dict1:
            ar.append(dict1[k])
        
        return ar