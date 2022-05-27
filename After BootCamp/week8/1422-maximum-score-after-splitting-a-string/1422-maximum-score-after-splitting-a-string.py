class Solution:
    def maxScore(self, s: str) -> int:
        nz = [0 for _ in range(len(s))]
        no = [0 for _ in range(len(s) + 1)]
        
        if len(s) == 2:
            if (s[0] == '1' and s[1] == '0'):
                return 0
            
            if (s[0] == '1' or s[1] == '0'):
                return 1
            
            return 2
        for i in range(len(s)):
            if s[i] == '0':
                nz[i] = 1 + nz[i - 1]
            else:
                nz[i] = nz[i - 1]
        
        for i in range(len(s) - 1,-1,-1):
            if s[i] == '1':
                no[i] = 1 + no[i + 1]
            
            else:
                no[i] = no[i + 1]
        
        res = 0
        
        for i in range(1,len(nz)-1):
            res = max(res,nz[i] + no[i])
        
        return res