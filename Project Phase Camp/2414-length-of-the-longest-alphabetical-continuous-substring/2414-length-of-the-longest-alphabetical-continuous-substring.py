class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        
        stk = []
        res = 0
        
        for c in s:
            while stk and ord(stk[-1]) - ord(c) != -1:
                stk.pop()
            
            stk.append(c)
            res = max(res, len(stk))
        
        return res