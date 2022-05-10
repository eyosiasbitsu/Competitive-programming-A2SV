class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        
        for i in range(len(s)):
            c = s[i]
            if stk and stk[-1][0] == c:
                stk[-1][1] += 1
            
            else:
                stk.append([c,1])
            
            if stk[-1][1] == k:
                stk.pop()
        
        res = ""
        
        for c,count in stk:
            res += (c*count)
        
        return res