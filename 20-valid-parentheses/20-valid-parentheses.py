class Solution:
    def isValid(self, s: str) -> bool:
        
        stk = []
        
        for c in s:
            if not stk:
                stk.append(c)
            
            elif ((stk[-1] == '{' and c == '}') or
                  (stk[-1] == '[' and c == ']') or
                  (stk[-1] == '(' and c == ')')):
                stk.pop()
            
            else:
                stk.append(c)
        
        return not stk