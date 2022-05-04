class Solution:
    def isValid(self, s: str) -> bool:
        
        stk = []
        
        for i in s:
            if not stk:
                stk.append(i)
            
            elif ((stk[-1] == "{" and i == "}")
                  or (stk[-1] == "[" and i == "]")
                  or (stk[-1] == "(" and i == ")")):
                  stk.pop()
            
            else:
                stk.append(i)
        
        return len(stk) == 0