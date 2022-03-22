class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        maxidx = {}
        
        for i in range(len(s)):
            maxidx[s[i]] = i
        
        ar = []
        r = maxidx[s[0]]
        l = 0
        i = 1
        
        while i < len(s):
            
            if maxidx[s[i]] > r and i < r:
                r = maxidx[s[i]]
            elif i == r + 1:
                ar.append(r - l + 1)
                l = i
                r = maxidx[s[i]]
            i += 1
            
        ar.append(r-l+1)
        
        return ar