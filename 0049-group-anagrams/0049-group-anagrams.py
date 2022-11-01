class Solution:
    def groupAnagrams(self,  strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)
            
        for i in range(len(strs)):
            sorted_st = list(strs[i])
            sorted_st.sort()
            sorted_st = "".join(sorted_st)
            
            anagrams[sorted_st].append(strs[i])
        
        result = []
        for key in anagrams:
            result.append(anagrams[key])
        
        return result
        
        
        
        
        
        
        
        
        
        
        
        