class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        
        for i in range(len(strs)):
            cur = [0]*26
            
            for c in strs[i]:
                cur[ord(c) - ord('a')] += 1
            
            res[tuple(cur)].append(strs[i])
        
        return res.values()