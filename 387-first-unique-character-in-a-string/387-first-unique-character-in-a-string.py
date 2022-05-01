class Solution:
    def firstUniqChar(self, s: str) -> int:
        idx = defaultdict(list)
        
        for i in range(len(s)):
            idx[s[i]].append(i)
        
        res = 100000
        for k in idx:
            if len(idx[k]) == 1 and idx[k][0] < res:
                res = idx[k][0]
                
        return res if res < 100000 else -1