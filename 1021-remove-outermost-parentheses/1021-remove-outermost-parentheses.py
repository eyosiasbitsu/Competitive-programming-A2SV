class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ar = []
        idx = 0
        n = 0
        
        for i in range(len(s)):
            if s[i] == "(":
                n += 1
            else:
                n -= 1
                
            if n == 0:
                ar.append(s[idx: i + 1])
                idx = i + 1
        
        print(ar)
        st = ""
        for i in ar:
            st += (i[1:-1])
            
        return st